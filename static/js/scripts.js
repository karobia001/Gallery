function CopyFunction() {
    var CopyFunction = document.getElementById("myInput");
    CopyFunction.select();
    document.execCommand("copy");
    alert("Copied the text: " + CopyFunction.value);
  }