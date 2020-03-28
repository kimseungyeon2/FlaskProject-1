$(document).ready(function(){
    const Ajax = new Service();
    const Image = new ImgFile();
    const reader = new FileReader();
    const $drop = $("#drop");
    const $form = $("#form");
    const $submit = $('#submit');
    //total message close
    $drop.on('dragleave',function(event){
        return false;
    });
    $drop.on('dragover',function(event){
        return false;
    });
    $drop.on('drop',function(event){
        //image preview
        Image.setFile(event.originalEvent.dataTransfer.files[0]);
        Image.imgPreview(reader);
        return false;
    }); 
    
    $drop.on('click',function(){
        $form.find('input').click();
    });

    $form.find('input').on('change',function(event){        
        //imgPreview
        Image.setFile(event.target.files[0]);
        Image.imgPreview(reader);
    });

    $submit.on('click',function(){
        for (const index in Image.getFile()) {
            let formData = {
                'lang':$form.find('select').val(),
                'file':Image.getFile()[index]
            };
            Ajax.setFormData(formData);
            $('#resultBox').append($('<h3>').text(Ajax.post('/main')));   
        }
    });

    reader.onload = (event) => {
        // document.
        let imgDiv = $('<div>');
        imgDiv.addClass('col-md-4');
        
        let imgTag = $('<img/>');
        imgTag.attr('src',event.target.result);
        
        let imgI = $('<i>');
        imgI.addClass('trash alternate outline icon');

        imgI.on('click',function(event){
            Image.removeFile($(event.currentTarget).closest('div').index());
            $(event.currentTarget).closest('div').remove();
            return false;
        });

        $drop.find('#imgBox').append(
            imgDiv.append(imgTag).append(
                $('<span>').text(Image.getFile()[Image.getFile().length-1].name)).append(
                    imgI
                ));
    }
    $('#loginBtn').on('click',function(){
        $('.ui.login.modal').modal('show');
        $('#moveRegister').on('click',function(){
            $('.ui.register.modal').modal('show');
            $('#moveLogin').on('click',function(){
                $('.ui.login.modal').modal('show');
            });
        });
        return false;
    });

    $('#formRegister').on('click',function(){
        let formData = {
            'username':$('input[name="regi-username"]').val(),
            'password':$('input[name="regi-password"]').val()
        };
        Ajax.setFormData(formData);

        if(Ajax.put('/')){
            $('input[name="login-username"]').attr('value',$('input[name="regi-username"]').val());
            $('input[name="login-password"]').attr('value',$('input[name="regi-password"]').val());
            $('#formLogin').click();
        }else{
            //err
        }
        return false;
    });

    //LogIn
    $('#formLogin').on('click',function(){
        let formData = {
            'username':$('input[name="login-username"]').val(),
            'password':$('input[name="login-password"]').val()
        };
        Ajax.setFormData(formData);
        
        if(Ajax.post('/')){            
            window.location.reload();
        }else{
            //err
        }
    });


    //Logout
    $('#logoutBtn').on('click',function(){
        if(confirm('정말 로그아웃 하시겠습니까?')){            
            Ajax.setFormData(false);
            if(Ajax.delete('/')){
                window.location.reload();
            }else{
                //err
            }
        }
    });

    // message 닫기
    $('.message .close').on('click', function() {
        $(this).closest('.message').transition('fade');
    });



});