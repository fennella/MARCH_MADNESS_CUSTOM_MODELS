function toViewResults() {

    document.getElementById("viewResultsDiv").style.display = "block";
    document.getElementById("viewResultsTag").style.textDecoration = "underline";
    document.getElementById("viewResultsTag").style.backgroundColor = "white";


    document.getElementById("createModelDiv").style.display = "none";
    document.getElementById("createModelTag").style.textDecoration = "none";
    document.getElementById("createModelTag").style.backgroundColor = "grey";
    
}

function toCreateModel() {

    document.getElementById("viewResultsDiv").style.display = "none";
    document.getElementById("viewResultsTag").style.textDecoration = "none";
    document.getElementById("viewResultsTag").style.backgroundColor = "grey";

    document.getElementById("createModelDiv").style.display = "block";
    document.getElementById("createModelTag").style.textDecoration = "underline";
    document.getElementById("createModelTag").style.backgroundColor = "white";

}



function resetUI() {


    var sliders = document.getElementsByTagName('input');
    var spans = document.getElementsByClassName('range-slider__value');
    for (var index = 0; index < sliders.length; ++index) {

        sliders[index].value = 0;
        spans[index].innerHTML = 0;
        applyNoFill(sliders[index]);
        
    }

}

function calculate() {

    stats = ["SOS", "RPI", "PythW", "last10", "top25", "nonConf", "wp", "awp", "awayWP", "owp", "oowp", "pace", "ts", "efg", "ortg", "drtg", "nrtg", "ftr", "tovr", "dm", "orb", "erb", "blkp", "aps", "apa", "apd", "afbp", "ascp", "apip", "threepp", "ftp", "fgp", "aa", "avgs", "at", "ab", "aorb"];
    weightsDict = {}

    var spans = document.getElementsByClassName('range-slider__value');
    
    for (var index = 0; index < spans.length; ++index) {

        weightsDict[index] = {"stat":stats[index], "weight":spans[index].innerHTML};

    }
    jsonModel = JSON.stringify(weightsDict);
    calcModel(jsonModel);

}

function calcModel(jsonModel) {

    $.ajax({

        url: 'calcModel',
        type: 'get',
        data: {
            'weightsDict': jsonModel
        },
        dataType: 'json',
        success: function (data) {
            displayResults(data);
        },
        error: function(error) {
            console.error(error);
        }
    
    });
}

function displayResults(data) {

    resetStyling();
    toViewResults();


    popBracket(data[0], "round-one", 32);
    popBracket(data[1], "round-two", 16);
    popBracket(data[2], "round-three", 8);
    popBracket(data[3], "round-four", 4);
    popBracket(data[4], "round-five", 2);
    popFinals(data);
    
    console.log(data);
}

function resetStyling() {

    var allTeams = document.getElementsByClassName("team");

    for (var i = 0; i < allTeams.length; i++) {
        allTeams[i].style.fontWeight = "normal";
    }

}

function popBracket(data, className, halfBracket) {

    var rounds = document.getElementsByClassName(className);
    var l_round = rounds[0];
    var r_round = rounds[1];
    
    for (var i = 0; i < halfBracket; i++) {

        l_round.getElementsByClassName("team")[i].innerHTML = data[i]["name"];
        r_round.getElementsByClassName("team")[i].innerHTML = data[i + halfBracket]["name"];

        if (i % 2 === 1) {
            if (data[i]["score"] > data[i - 1]["score"]) {
                l_round.getElementsByClassName("team")[i].style.fontWeight = "bold";
            } else {
                l_round.getElementsByClassName("team")[i - 1].style.fontWeight = "bold";
            }

            if (data[i + halfBracket]["score"] > data[i + halfBracket - 1]["score"]) {
                r_round.getElementsByClassName("team")[i].style.fontWeight = "bold";
            } else {
                r_round.getElementsByClassName("team")[i - 1].style.fontWeight = "bold";
            }
        }
    }
}

function popFinals(data) {

    document.getElementById("finals1").innerHTML = data[5][0]["name"];
    document.getElementById("finals2").innerHTML = data[5][1]["name"];

    if (data[5][0]["score"] > data[5][1]["score"]) {
        document.getElementById("finals1").style.fontWeight = "bold";
    } else {
        document.getElementById("finals2").style.fontWeight = "bold";
    }

    document.getElementById("championName").innerHTML = "Champion: " + data[6][0]["name"];




}