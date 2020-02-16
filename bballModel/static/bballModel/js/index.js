function toViewResults() {

    document.getElementById("viewResultsDiv").style.display = "block";
    document.getElementById("viewResultsTag").style.textDecoration = "underline";

    document.getElementById("createModelDiv").style.display = "none";
    document.getElementById("createModelTag").style.textDecoration = "none";
    
}

function toCreateModel() {

    document.getElementById("viewResultsDiv").style.display = "none";
    document.getElementById("viewResultsTag").style.textDecoration = "none";

    document.getElementById("createModelDiv").style.display = "block";
    document.getElementById("createModelTag").style.textDecoration = "underline";

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
    toViewResults();
    console.log(data);
}

