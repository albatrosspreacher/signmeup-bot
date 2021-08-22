function addItem(){
    let html = ``;
    html += `
    <div class="row">
            <div class="col">
            <input type="text" class="form-control" placeholder="Template Title">
            </div>
            <div class="col">
            <button type="button" class="btn btn-primary">Upload File</button>
            </div>
    </div>
    `;
    document.getElementById('templateTable').innerHTML+=html;
}