function ImgFile() {
    this.file = new Array();

    this.setFile = function(file){
        this.file.push(file);
    }
    this.getFile = function(){
        return this.file;
    }
    this.removeFile = function(index){
        // console.log("index"+typeof(index));
        console.log(index);
        
        console.log(this.file);
        this.file.splice(parseInt(index),1);
        console.log(this.file);
    }

    this.imgPreview = function(reader){
        reader.readAsDataURL(this.file[this.file.length-1]);
        return this.file[this.file.length-1].name;
    }
}