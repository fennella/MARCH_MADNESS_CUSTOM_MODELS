



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

    stats = ["SOS", "RPI", "PythW", "last10", "top25", "nonConf", "wp", "awp", "awayWP", "owp", "oowp", "pace", "ts", "efg", "ortg", "drtg", "nrtg", "ftr", "tovr", "dm", "orb", "erb", "blkp", "aps", "apa", "apd", "afbp", "ascp", "apip", "3pp", "ftp", "fgp", "aa", "as", "at", "ab", "aorb"];
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
            console.log(data);
        },
        error: function(error) {
            console.error(error);
        }
    
    });
}

