function deleteID(charId) {
  fetch("/delete-id", {
    method: "POST",
    body: JSON.stringify({ charId: charId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
