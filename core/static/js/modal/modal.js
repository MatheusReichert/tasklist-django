const taskModal = document.getElementById('taskModal');
const taskUpdateModal = document.getElementById('taskUpdateModal');
const openModalButton = document.getElementById('openModal');

const closeModalButtons = document.querySelectorAll('#taskModal .cancel-button');

const cancelButton = document.querySelectorAll('.cancel-button');
const editButtons = document.querySelectorAll('.edit-button');


openModalButton.addEventListener('click', () => {
  taskModal.showModal();
});

editButtons.forEach(button => {
  button.addEventListener('click', () => {
      // Obtendo o ID da tarefa associada ao botão de edição clicado
      const taskId = button.getAttribute('data-task-id');
      
      // Selecionando o modal de atualização da tarefa correspondente
      const taskUpdateModal = document.getElementById(`taskUpdateModal${taskId}`);
      
      // Abrindo o modal de atualização da tarefa correspondente
      if (taskUpdateModal) {
          taskUpdateModal.showModal();
      }
  });
});

closeModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    taskModal.close();
    taskUpdateModal.close();

  });
});

cancelButton.forEach(button => {
  button.addEventListener('click', () => {
      // Obtendo o ID da tarefa associada ao botão de edição clicado
      const taskId = button.getAttribute('data-task-id');
      
      // Selecionando o modal de atualização da tarefa correspondente
      const taskUpdateModal = document.getElementById(`taskUpdateModal${taskId}`);
      
      // Abrindo o modal de atualização da tarefa correspondente
      if (taskUpdateModal) {
          taskUpdateModal.close();
      }
  });
});

document.getElementById('edit-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Impede o envio do formulário padrão
  // Lógica para processar os dados do formulário aqui, sem recarregar a página ou adicionar parâmetros à URL
});