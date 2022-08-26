function deleteID(charId) {
  fetch("/delete-id", {
    method: "POST",
    body: JSON.stringify({ charId: charId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteMonster(id) {
  fetch("/deleteMonster-id", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = "/dm";
  });
}