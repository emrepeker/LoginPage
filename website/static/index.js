function delete_node(noteID) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteID }), // Use the correct parameter name
  }).then((_res) => {
    window.location.href = "/";
  });
}
