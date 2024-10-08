URL = "https://jayd719.github.io/sources/file1.txt";

function getData(URL) {
  const Data = $.get(URL, function () {}).fail(function () {
    alert("Counld Not Fetch Data");
  });
  return Data;
}

obj = getData(URL);

console.log(obj);
