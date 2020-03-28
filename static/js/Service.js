function Service() {
    this.formData;

    this.setFormData = function(data){
        this.formData = new FormData();
        if(data){
            for (const key in data) {
                this.formData.append(key,data[key]);
            }
        }   
    }

    this.post = function(path){
        let result;
        $.ajax({
            url:path,
            method:'POST',
            enctype : 'multipart/form-data',
            contentType : false,
            processData : false,
            async:false,  
            data:this.formData
        }).done(function(data){
            result = data;
        }).fail(function(err){
            result = err;
        });
        return result;
    }
    this.put = function(path){
        let result;
        $.ajax({
            url:path,
            method:'PUT',
            contentType : false,
            processData : false,
            async:false,
            data: this.formData
        }).done(function(data){ 
            result  = data;                      
        }).fail(function(err){
            result = err;
        });
        return result;
    }
    this.get = function(path){
        let result
        $.ajax({
            url:path,
            method:'GET',
            contentType : false,
            processData : false,
            async:false, 
            data:this.formData
        }).done(function(data){
            result = data;
        }).fail(function(err){
            result = err;
        });
        return result;
    }
    this.delete = function(path){
        let result
        $.ajax({
            url:path,
            method:'DELETE',
            contentType : false,
            processData : false,
            async:false, 
            data:this.formData
        }).done(function(data){
            result = data;
        }).fail(function(err){
            result = err;
        });
        return result;
    }
}