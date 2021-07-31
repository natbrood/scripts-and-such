// ==UserScript==
// @name         ROTA Ping
// @namespace    https://orangecyberdefense.com/
// @version      1.0
// @description  Ping when there is a case in the ROTA queue
// @author       Thijmen Kadijk
// @match        https://*.salesforce.com/*com
// @grant        GM_addStyle
//// @include      *
// @require      http://code.jquery.com/jquery-2.1.1.min.js
// ==/UserScript==

var soundData = 'https://dm0qx8t0i9gc9.cloudfront.net/previews/audio/BsTwCwBHBjzwub4i4/audioblocks-alert-fx-4-email-message-notification-4-email-message-notification_rK1QQef8RPL_NWM.mp3';
//var refreshsoundData = 'https://www.google.com/doenstexist.mp3';
var refreshsoundData = 'https://audio-previews.elements.envatousercontent.com/files/259410951/preview.mp3';
var repeat = 0
var pause = 1
console.log(pause)

function resettimer() {

    if (pause == 0) {
        setTimeout(() => {
            ROTA();                                                                //Call ROTA after 10 seconds
            console.log('Running ROTA');
            //console.log('pause status: '+pause);
        }, 1*1000);
    } else {
        setTimeout(() => {
            resettimer();
            console.log('Waiting');
            //console.log('pause status: '+pause);
        }, 1*1000)
    }
};

function ROTA(){
    setTimeout(() => {                                                             //wait for 10 seconds before first launch
        if(/No records to display/i.test (document.body.innerHTML) )
        {
            console.log('Found: "No records to display"')
            var audio = document.createElement("audio");
            audio.src = refreshsoundData;                                          //get pop
            //audio.play();
            console.log('skip audio')
            //setTimeout(function(){ location.reload(); }, 5*1000);
            document.getElementsByClassName("btn refreshListButton")[0].click();   //refresh view
            setTimeout(() => {
                resettimer();                                                      //call the refreshtimer
            }, 2*1000);

        } else if (/3 - Medium/i.test (document.body.innerHTML) & repeat < 2) {
            console.log('Found: "3 - Medium"')
            audio = document.createElement("audio");
            audio.src = soundData;                                                 //get pop
            audio.play();                                                          //play pop
            console.log('playing audio')
            if (repeat == 1) {
                setTimeout(() => {
                    alert ("A new case");                                          //Alert user
                }, 2*1000);
            }
            repeat += 1;
            resettimer();
        } else {
            console.error('Found none')
        }

        console.log('Repeat: '+repeat);
    }, 10*1000);                                                                   //cont. wait for 10 seconds before first launch
}

resettimer();



(function() {
  window.addEventListener("load", () => {
    addButton("ROTA: ▶");
  });

  function addButton(text, onclick, cssObj) {
    cssObj = cssObj || {
      position: "fixed",
      top: "8px",
      right: "150px",
      //"z-index": 3,
      fontWeight: "600",
      fontSize: "14px",
      //backgroundColor: "#00cccc",
      color: "orange",
      border: "none",
      padding: "-5px 20px"
    };
    let button = document.createElement("button"),
      btnStyle = button.style;
    document.body.appendChild(button);
    button.innerHTML = text;
    // Settin function for button when it is clicked.
    button.onclick = selectReadFn;
    Object.keys(cssObj).forEach(key => (btnStyle[key] = cssObj[key]));
    return button;
  }

  function selectReadFn() {
    var txt = document.getElementById("btnROTA");
    // Just to show button is pressed
    if (pause == 0) {
        pause = 1;
        this.innerHTML = "ROTA: ▶"


    } else {
        pause = 0;
        this.innerHTML = "ROTA: ❚❚"
    }
  }
})();
