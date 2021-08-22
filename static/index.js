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

$(function() {
    $('#bemail').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/send_email',
          function(data) {
        //do nothing
      });
      return false;
    });
});