window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        errorSettings: { message: [""] }, // Suppress error message text
        packages: { '[+]': ['noerrors'] }
    },
    options: {
        renderActions: {
            addError: [10, "", ""], // Suppress error rendering
            addWarning: [10, "", ""] // Suppress warning rendering
        }
    },
    loader: { load: ['[tex]/noerrors'] }
};

document.getElementById('function').addEventListener('mouseenter', function() {
    this.addEventListener('input', handleInput)
});

function handleInput(){
    let input = this.value.replace(/\s/g, '');
    let latex = convertToLatex(input);
    document.getElementById('hover-box-id').innerHTML = `\\[${latex}\\]`;
    MathJax.typesetPromise();
}

function convertToLatex(infix) {
    return infix
        .replace(/\((.+?)\)\^\((1)\/(\d+)\)/g, '\\sqrt[$3]{$1}')
        .replace(/\^(\((\d+\/\d+|.*?)\))/g, '^{$2}')
        .replace(/\b(\d+)\^(\d+)\b/g, '$1^{$2}')
        .replace(/\b(\d+)\*(\d+)\b/g, '$1\\times$2')
        .replace(/\((.+?)\)\/\((.+?)\)/g, '\\frac{$1}{$2}')
        .replace(/\^(\(\d+\/\d+\))/g, '^{\\frac$1}')
        .replace(/\b([a-zA-Z])\/([a-zA-Z])\b/g, '\\frac{$1}{$2}')
        .replace(/\b(\d+)\/(\d+)\b/g, '\\frac{$1}{$2}')
        .replace(/\b(\d+)\/([a-zA-Z])\b/g, '\\frac{$1}{$2}')
        .replace(/\b([a-zA-Z])\/(\d+)\b/g, '\\frac{$1}{$2}');
}


