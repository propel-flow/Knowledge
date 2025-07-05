
Looking at your code, **TinyMCE** would work best for your use case. Here's why:

**TinyMCE is ideal because:**

- It can be easily integrated into your existing iframe setup
- Has excellent link editing capabilities (right-click any link → edit URL, text, target)
- Can be initialized on-demand when you enter "edit mode"
- Handles dynamic HTML content well
- Free and well-documented

**How to integrate it:**

You'd modify your `loadPreview` function to optionally load TinyMCE instead of just displaying the HTML:

```javascript
// Add this to your head section
<script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.7.2/tinymce.min.js"></script>

// Modify your preview loading
function loadPreview(campaignId, editMode = false) {
    const htmlFileName = campaignId;
    previewHeader.textContent = `Preview: ${htmlFileName}`;
    
    if (htmlFiles.has(htmlFileName)) {
        if (editMode) {
            // Create editable version
            previewFrame.srcdoc = `
                <html>
                <head>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.7.2/tinymce.min.js"></script>
                </head>
                <body>
                    <div id="editableContent">${htmlFiles.get(htmlFileName)}</div>
                    <script>
                        tinymce.init({
                            selector: '#editableContent',
                            inline: true,
                            plugins: 'link image lists',
                            toolbar: 'bold italic link unlink',
                            menubar: false
                        });
                    </script>
                </body>
                </html>
            `;
        } else {
            // Regular preview
            previewFrame.srcdoc = htmlFiles.get(htmlFileName);
        }
    }
}
```

**Add edit controls to your header:**

```html
<button onclick="toggleEditMode()" id="editBtn">Edit HTML</button>
<button onclick="saveEditedHTML()" id="saveBtn" style="display:none">Save HTML</button>
```

**Link editing with TinyMCE:**

- Click any link → TinyMCE toolbar appears
- Click link button in toolbar → dialog opens with URL field
- Edit URL, link text, target (new window, etc.)
- Changes are immediately visible

This approach keeps your existing architecture while adding the editing capability you want, and TinyMCE's link editing is particularly user-friendly for your use case.