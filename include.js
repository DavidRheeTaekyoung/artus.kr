// include.js
// HTML 파일을 로드하는 함수
function includeHTML(id, url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById(id).innerHTML = data;
        })
        .catch(error => {
            console.error(`${url} 로드 중 오류:`, error);
            document.getElementById(id).innerHTML = `<p>${url} 로드 실패</p>`;
        });
}

// DOM이 로드되면 실행
document.addEventListener('DOMContentLoaded', function() {
    includeHTML('header', 'header.html');
    includeHTML('footer', 'footer.html');
});