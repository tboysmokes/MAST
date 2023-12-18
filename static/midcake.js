function loadMusic() {
  const file = document.getElementById('audioFile').files[0];
  if (!file) {
    alert('Please select an audio file!');
    return;
  }
  const audioPlayer = document.getElementById('musicPlayer');
  audioPlayer.src = URL.createObjectURL(file);
}
function openFunc() {
  document.getElementById("form-modal").style.display = "block";
}

function cancelFunc() {
  document.getElementById("form-modal").style.display = "none";
}

function openlogin() {
  let change = document.getElementById("changeBox");
  let change2 = document.getElementById("changeBox2");
  document.getElementById("formted1").style.display = "none";
  document.getElementById("formted").style.display = "block";
  change.style.display = "none";
  change2.style.display = "block";
}

function opensignin() {
  let change = document.getElementById("changeBox");
  let change2 = document.getElementById("changeBox2");
  document.getElementById("formted1").style.display = "block";
  document.getElementById("formted").style.display = "none";
  change.style.display = "block";
  change2.style.display = "none";
}

window.onclick = function (event) {
  if (event.target == document.getElementById("form-modal")) {
    document.getElementById("form-modal").style.display = "none";
    document.getElementById("formted1").style.display = "block";
    document.getElementById("formted").style.display = "none";
  }
};

window.onload = function () {
  let backgroundAudio = new Audio("bedtime/deep-cinematic-ballad_medium-178309.mp3");
  backgroundAudio.volume = 1;
  backgroundAudio.play();
};

function playMusic() {
  // Get the file input and audio elements
  

}

// script.js

// Your code here
const audio = new Audio("{{ url_for('static', filename = 'musicF/'+audio)}}"); // Create an audio element
let isPlaying = false; // Variable to track whether the audio is playing
let currentSongIndex = 0; // Index of the current song in the playlist
let playlist = document.getElementById('musicPlayer');// Playlist array

function playMusic() {
  if (isPlaying) {
    audio.pause();
  } else {
    audio.play();
  }
  isPlaying = !isPlaying;
  updatePlayPauseIcon();
}

function updatePlayPauseIcon() {
  const playPauseIcon = document.getElementById('play-pause');
  playPauseIcon.className = isPlaying ? 'fa fa-circle-pause fa-4x' : 'fa fa-circle-play fa-4x';
}


// Rest of the code remains the same

// Update the current time and progress bar as the audio plays
audio.addEventListener('timeupdate', function() {
  const currentTime = document.getElementById('current-time');
  const progressBar = document.getElementById('progress-bar');

  const minutes = Math.floor(audio.currentTime / 60);
  const seconds = Math.floor(audio.currentTime % 60);
  currentTime.innerText = `${minutes}:${seconds}`;

  progressBar.value = (audio.currentTime / audio.duration) * 100;
});

// Handle volume control


// for canceling the error message

function validateForm() {
  // For the errror message
  let house = document.getElementById("error-house");

  //For the all inputs fields
  let allInputs = document.getElementById("valid").value;

  // The innerhtml for the displaying error message

  let errorMessage = document.getElementById("text-error");

  // For the input of the error

  //for the rest specials
  let fullName = document.getElementsByName("name1")[0];
  let email = document.getElementsByName("email1")[0].value;
  let password1 = document.getElementsByName("pass1")[0].value;
  let password2 = document.getElementsByName("pass2")[0].value;

  // for the profile

  const getName = localStorage.getItem("FullName");
  let profilePlace = document.getElementById("fullName");

  if (allInputs == "" || allInputs == null) {
    //For checking the rest fields
    house.style.display = "block";
    errorMessage.innerHTML = "sorry this form must filled.";
    return false;
    // for the full name checking if it complete
  } else if (fullName.value == "" || fullName.value == null) {
    house.style.display = "block";
    errorMessage.innerHTML = "Please put your full name";
    return false;
    // for the email checking if it complete
  } else if (email == "" || email == null) {
    house.style.display = "block";
    errorMessage.innerHTML = "Please put your email.";
    return false;
    // for the password checking if it complete
  } else if (password1 == "" || password1 == null) {
    house.style.width = "35%";
    errorMessage.innerHTML = "Please put your password";
    return false;
  }
  // confirming if are the same password.
  else if (password2 != password1) {
    house.style.display = "block";
    errorMessage.innerHTML = "sorry please the password must be the same ";
    return false;
  } else if (password2 == null || password2 == "") {
    house.style.display = "block";
    errorMessage.innerHTML = "Please confirm password";
    return false;
  } else {
    localStorage.setItem("FullName", fullName.value);
    profilePlace.innerHTML = `${getName}`;
  }
}


function toggleDivs() {
  const div1 = document.getElementById('div1');
  const div2 = document.getElementById('div2');
  const chevronLeft = document.getElementById('chevron-left');
  const chevronRight = document.getElementById('chevron-right');

  // Toggle the visibility of the divs
  if (div1.style.display === 'none') {
    div1.style.display = 'block';
    div2.style.display = 'none';
    chevronLeft.style.display = 'inline';  // Show left chevron
    chevronRight.style.display = 'none';  // Hide right chevron
  } else {
    div1.style.display = 'none';
    div2.style.display = 'block';
    chevronLeft.style.display = 'none';  // Hide left chevron
    chevronRight.style.display = 'inline';  // Show right chevron
  }
}