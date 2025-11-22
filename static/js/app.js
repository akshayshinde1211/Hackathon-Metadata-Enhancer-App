document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('uploadForm');
    const generateBtn = document.getElementById('generateBtn');
    const loadingState = document.getElementById('loadingState');
    const emptyState = document.getElementById('emptyState');
    const resultsContent = document.getElementById('resultsContent');

    // File Input Listeners
    setupFileInput('schemaFile', 'schemaFileName');
    setupFileInput('dataFile', 'dataFileName');
    setupFileInput('logsFile', 'logsFileName');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI State: Loading
        generateBtn.disabled = true;
        generateBtn.classList.add('opacity-50', 'cursor-not-allowed');
        emptyState.classList.add('hidden');
        resultsContent.classList.add('hidden');
        loadingState.classList.remove('hidden');
        loadingState.classList.add('flex');

        const formData = new FormData(form);

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error('Generation failed');

            const data = await response.json();
            renderResults(data);

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while generating metadata.');
        } finally {
            // UI State: Done
            loadingState.classList.add('hidden');
            loadingState.classList.remove('flex');
            generateBtn.disabled = false;
            generateBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }
    });

    function setupFileInput(inputId, labelId) {
        const input = document.getElementById(inputId);
        const label = document.getElementById(labelId);

        input.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                label.textContent = e.target.files[0].name;
                label.classList.add('text-white');
            }
        });
    }

    function renderResults(data) {
        resultsContent.classList.remove('hidden');

        // Overview
        document.getElementById('overviewText').textContent = data.overview;

        // Quality List
        const qualityList = document.getElementById('qualityList');
        qualityList.innerHTML = data.data_quality.map(item =>
            `<li class="flex items-start gap-2">
                <span class="text-red-400 mt-1">⚠</span>
                <span><strong class="text-slate-200">${item.field}:</strong> ${item.issue}</span>
            </li>`
        ).join('');

        // Usage Tips
        const usageList = document.getElementById('usageList');
        usageList.innerHTML = data.usage_tips.map(tip =>
            `<li class="flex items-start gap-2">
                <span class="text-blue-400 mt-1">💡</span>
                <span>${tip}</span>
            </li>`
        ).join('');

        // Technical Details
        const techDetails = document.getElementById('techDetails');
        techDetails.innerHTML = Object.entries(data.technical_details).map(([key, value]) =>
            `<div class="bg-slate-800/50 p-3 rounded-lg">
                <div class="text-xs text-slate-500 uppercase tracking-wider mb-1">${key.replace(/_/g, ' ')}</div>
                <div class="font-mono text-slate-200">${Array.isArray(value) ? value.join(', ') : value}</div>
            </div>`
        ).join('');
    }
});
