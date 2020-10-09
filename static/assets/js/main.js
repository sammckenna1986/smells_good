// Get the element
$link = document.querySelector("#whatsapp-button");

// Generate url
$url = "whatsapp://send?text=" + window.location.href;

// Set url attribute of the link
$link.setAttribute('href', $url);