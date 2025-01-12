
function fetchNotifications() {
    fetch('/notifications/')
    .then(response => response.text())  // Change this to expect JSON
    .then(data => {
        document.getElementById('notifications').innerHTML = data;
        updateNotificationsDisplay(data);  // Handle data to update the DOM
    });
}
setInterval(fetchNotifications, 30000);

function updateNotificationsDisplay(data) {
    const container = document.getElementById('notifications');
    container.innerHTML = '';  // Clear existing notifications
    data.forEach(notification => {
        const div = document.createElement('div');
        div.textContent = notification.message;  // Assuming 'message' is part of the notification data
        container.appendChild(div);
    });
}



function fetchNotifications() {
    fetch('/notifications/')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        updateNotificationsDisplay(data);
    })
    .catch(error => {
        console.error('Error fetching notifications:', error);
    });
}




// new codek

document.addEventListener('DOMContentLoaded', function() {
    function fetchNotifications() {
        fetch('/notifications/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            updateNotificationsDisplay(data.notifications);
        })
        .catch(error => {
            console.error('Error fetching notifications:', error);
        });
    }

    function updateNotificationsDisplay(notifications) {
        const container = document.getElementById('notifications');
        container.innerHTML = '';  // Clear existing notifications
        notifications.forEach(notification => {
            const div = document.createElement('div');
            div.textContent = notification.message;  // Using 'message' field from notification data
            container.appendChild(div);
        });
    }

    setInterval(fetchNotifications, 30000);  // Fetch notifications every 30 seconds
});
