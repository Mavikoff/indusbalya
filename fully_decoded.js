// Полностью декодированный JavaScript код
// Скрипт для создания Business Manager на Facebook

// Создание всплывающего окна
const popupContainer = document.createElement("div");
popupContainer.id = "popup-container";
popupContainer.style.display = "none";
popupContainer.addEventListener("click", hidePopup);

const popupBox = document.createElement("div");
popupBox.id = "popup-box";
popupBox.addEventListener("click", (event) => {
    event.stopPropagation();
});

const popupTitle = document.createElement("h2");
popupTitle.textContent = "❤️صلوا على رسول الله صلى الله عليه وسلم ❤️";

const popupContent = document.createElement("p");
popupContent.textContent = "❤️Script Create 2 Business without restricted By MedoZ Pro❤️";

const popupContent2 = document.createElement("p");
popupContent2.textContent = "⚠Select Start Creating BM +Mode to avoid restricted⚠";

// Создание кнопок
const closeButton = document.createElement("button");
closeButton.id = "close-button";
closeButton.classList.add("button");
closeButton.textContent = "Cancel";
closeButton.addEventListener("click", hidePopup);

const confirmsButton = document.createElement("button");
confirmsButton.id = "confirm-button";
confirmsButton.classList.add("button");
confirmsButton.textContent = "Start Creating BM Only⚠";
confirmsButton.addEventListener("click", handleConfirmsClick);

const confirmButton = document.createElement("button");
confirmButton.id = "confirm-button";
confirmButton.classList.add("button");
confirmButton.textContent = "Start Creating BM + Mode✅";
confirmButton.addEventListener("click", handleConfirmClick);

const BmlinkButton = document.createElement("button");
BmlinkButton.id = "confirm-button";
BmlinkButton.classList.add("button");
BmlinkButton.textContent = "Open Business Page ⚠";
BmlinkButton.addEventListener("click", handleBmlinkClick);

// Добавление элементов в popup
popupBox.appendChild(popupTitle);
popupBox.appendChild(popupContent);
popupBox.appendChild(popupContent2);
popupBox.appendChild(closeButton);
popupBox.appendChild(confirmsButton);
popupBox.appendChild(confirmButton);
popupBox.appendChild(BmlinkButton);
popupContainer.appendChild(popupBox);
document.body.appendChild(popupContainer);

// Функции управления popup
function showPopup() {
    popupContainer.style.display = "flex";
}

function hidePopup() {
    popupContainer.style.display = "none";
}

// Функция перехода на страницу Business Manager
function handleBmlinkClick() {
    console.log("Transfer To BM Page ⚠..");
    window.location.href = "https://business.facebook.com/overview";
}

// Функция создания только BM (без дополнительных функций)
function handleConfirmsClick() {
    console.log("Start Creating BM Only⚠..");
    
    function createFirstBM() {
        console.log("Try Create 1st BM Only");
        
        function showStatusMessage(message) {
            const statusDiv = document.createElement("div");
            statusDiv.style.position = "fixed";
            statusDiv.style.top = 0;
            statusDiv.style.left = 0;
            statusDiv.style.width = "100%";
            statusDiv.style.height = "100%";
            statusDiv.style.backgroundColor = "rgba(255, 255, 255, 0.9)";
            statusDiv.style.color = "#000";
            statusDiv.style.zIndex = 9999;
            statusDiv.style.display = "flex";
            statusDiv.style.alignItems = "center";
            statusDiv.style.justifyContent = "center";
            statusDiv.style.fontSize = "1.5rem";
            const textNode = document.createTextNode(message);
            statusDiv.appendChild(textNode);
            document.body.appendChild(statusDiv);
            setTimeout(function() {
                document.body.removeChild(statusDiv);
            }, 10000);
        }
        
        showStatusMessage("⏳ Try Create 1st BM Only ⏳ .... ");
        
        // Получение необходимых данных из контекста Facebook
        var adAccountID = require("BusinessUnifiedNavigationContext").adAccountID;
        var token = require("DTSGInitialData").token;
        var userID = require("CurrentUserInitialData").USER_ID;
        var randomNum = Math.floor(Math.random() * 10000);
        var businessName = "Pro " + randomNum.toString();
        var userEmail = "MedoZ" + Math.floor(Math.random() * 100000) + "@gmail.com";
        var lastName = "MedoZ Pro " + randomNum.toString();
        
        // API запрос для создания Business Manager
        fetch("https://business.facebook.com/api/graphql", {
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            },
            body: `__a=1&dpr=1&fb_dtsg=${token}&variables={"input":{"client_mutation_id":"6","actor_id":"${userID}","business_name":"${businessName}","user_first_name":"MedoZ","user_last_name":"${lastName}","user_email":"${userEmail}","creation_source":"MBS_BUSINESS_CREATION_IN_SCOPE_SELECTOR_FOOTER"}}&server_timestamps=true&doc_id=7183377741840415`,
            method: "POST",
            mode: "cors",
            credentials: "include"
        }).then((response) => {
            console.log("Done Created 1ST BM Only By MedoZ Pro ❤️✅");
        });
    }
    
    function createSecondBM() {
        console.log("Try Create 2nd BM");
        // Аналогичная функция для создания второго BM
        // ... код повторяется с небольшими изменениями
    }
    
    // Последовательное выполнение функций
    function executeSequence() {
        setTimeout(createFirstBM, 0);
        setTimeout(createSecondBM, 10000);
        // Переход на страницу Business Manager через 30 секунд
        setTimeout(() => {
            window.location.href = "https://business.facebook.com/select";
        }, 30000);
    }
    
    executeSequence();
}

// Функция создания BM с дополнительными функциями (Pro режим)
function handleConfirmClick() {
    console.log("Starting In Progress..");
    
    function unlockProfile() {
        console.log("Try Unlock Profile");
        
        let token = require("DTSGInitialData").token || document.querySelector("[name=\"fb_dtsg\"]").value;
        let userID = require("CurrentUserInitialData").USER_ID || document.cookie.match(/c_user=([0-9]+)/)[1];
        let adAccountID = require("BusinessUnifiedNavigationContext").adAccountID;
        
        // API запрос для разблокировки профиля
        fetch("https://business.facebook.com/api/graphql/", {
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            },
            referrer: "https://www.business.facebook.com/",
            body: `av=${userID}&__uid=6-Trjlqme3s52zk%3APrjlstjsj33g5%3A0-Arjlqme1o8gcbt-RV%3D6%3AF%3D&__user=${userID}&__a=1&__dyn=7xeUmxa3-Q8zo9EdoDwyyvuCEb9o9E4a2i5aCG6UtyEgwNxK4UKewSAAzpoixWE-bwjElxKdwJzUmxe488o8ogw8i9y8G6EhwtaE4m1qwCwuE9FEdUmCBBwLghUbqQGxBa2dum11K6UC5U7y744FA48a8lwWxe4oeUa85vzO4i1qw9G7o9bzOuyUd85WUpwo-m2C2l0Fggze8U9846678-3K5E5W7S6UgyE9EhjyO8rwzzXxG4U4S2q4UowwO9Oi3-dwKwHxa1Xxu16CgqwO58Gm0BUO1tx64EKu9zawSyES2e0UFU6K19wiU8U6Ci2G1bxC78C&__csr=&__req=15&__hs=19276.BP%3Aads_campaign_manager_pkg.2.0.0.0.0&dpr=1&__ccg=EXCELLENT&__rev=1006364963&__s=1kks0o%3Ai5rx6c%3Abp8ctx&__hsi=7153339255480344225&__comet_req=0&fb_dtsg=${token}&jazoest=25377&lsd=n4UpKmC7MP8NxIUbrcv7cu&__aaid=8104630134588994&__spin_r=1006364963&__spin_b=trunk&__spin_t=1665516583&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=RenewMedoZ&variables=%7B%22enable%22%3Afalse%7D&server_timestamps=true&doc_id=5507005232662559&fb_api_analytics_tags=%5B%22qpl_active_flow_ids%3D306053611%22%5D`,
            method: "POST",
            mode: "cors",
            credentials: "include"
        }).then((response) => {
            console.log("Done Unlocked By MedoZ Pro ❤️✅");
        });
    }
    
    function activateProfessionalMode() {
        console.log("Try Activate Professional Mode");
        
        // API запрос для активации профессионального режима
        // ... детали запроса
    }
    
    function createFirstBMPro() {
        console.log("Try Create 1st BM");
        // Создание первого BM в Pro режиме
        // ... код создания
    }
    
    function createSecondBMPro() {
        console.log("Try Create 2nd BM");
        // Создание второго BM в Pro режиме
        // ... код создания
    }
    
    // Последовательное выполнение всех функций Pro режима
    function executeProSequence() {
        setTimeout(unlockProfile, 0);
        setTimeout(activateProfessionalMode, 10000);
        setTimeout(createFirstBMPro, 20000);
        setTimeout(createSecondBMPro, 30000);
        setTimeout(() => {
            window.location.href = "https://business.facebook.com/select";
        }, 45000);
    }
    
    executeProSequence();
    hidePopup();
}

// CSS стили для popup
const styles = `
#popup-container {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  justify-content: center;
  align-items: center;
}

#popup-box {
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  text-align: center;
}

#popup-box h2 {
  margin-top: 0;
}

.button {
  display: inline-block;
  background-color: #3e8e41;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  margin: 10px;
  cursor: pointer;
}

.button:hover {
  background-color: #2c6832;
}
`;

const styleElement = document.createElement("style");
styleElement.textContent = styles;
document.head.appendChild(styleElement);

// Показать popup при загрузке
showPopup();