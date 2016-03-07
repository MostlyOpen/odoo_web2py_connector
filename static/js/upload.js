$(document).ready(function(){
  //Função para listar os arquivos existentes
  $('#file_set_files option:selected').each(function(){
    var file = $(this).text();
    var p = '<p id="'+file+'">';
    p += '<a class="btn btn-success btn-download" href="http://'+window.location.host+'/odoo_web2py_connector/default/download/'+file+'">Arquivo</a>';
    p += '<button type="button" class="btn btn-danger excluir"><span class="icon-white icon-trash"></span></button></p>';
    $('#file_set_files').parent().append(p);
  });
  //Função para excluir os arquivos
  $('button.excluir').click(function(){
      var arq = $(this).parent().attr('id');
      $(this).parent().hide();
      $.ajax({
          url: 'http://'+window.location.host+'/odoo_web2py_connector/upload/delete_file/'+arq,
          type: 'post',
          data: arq,
          success: function(data){
            if (data != 'erro'){
              $('#file_set_files option:selected').each(function(){
                  var file = $(this).text();
                  if(file == data){
                  $(this).remove();
                  }
              });
            }else{                            
              alert('Erro ao excluir arquivo!');
            }
        },
        error: function(){
          alert('Erro ao excluir arquivo, verifique sua conexão!');
        }
      });
  });
  //Função para tratar os uploads via ajax
  arquivos = $('#file_set_files');
  arquivos.parent().append('<input class="upload" id="file_upload" name="file_upload" type="file">');
  arquivos.hide();
  $('#file_upload').pekeUpload({
    btnText: 'Adicionar',
    url: 'http://' + window.location.host + '/odoo_web2py_connector/album/upload_file',
    theme: 'bootstrap',
    showErrorAlerts: false,
    onFileError: function(file,error){
      $('#file_set_files').append($('<option>', {value: error, text: error, selected: true}));
      var div = '<div class="alert alert-success">';
      div += '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>';
      div += '<p>'+file['name']+' adicionado com sucesso!</p></div>'
      $('div.pekecontainer').append(div);
    }
  });
});