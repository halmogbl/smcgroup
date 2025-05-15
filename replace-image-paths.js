const fs = require('fs');
const path = require('path');

const baseDir = 'C:/Users/hmogbl/Development/smcgroupksa/smcgroup_rebuild/smcgroupksa.com';
const imagesDir = path.join(baseDir, 'images');
const imageUrlsPath = path.join(baseDir, 'image_urls.txt');

const htmlExtensions = ['.html', '.htm'];

// Read and map the image URLs
const imageUrls = fs.readFileSync(imageUrlsPath, 'utf-8')
  .split('\n')
  .filter(Boolean)
  .map(url => url.trim());

const filenameMap = new Map();
for (const url of imageUrls) {
  const filename = path.basename(url.split('?')[0]);
  filenameMap.set(url, filename);
}

// Recursively walk the directory to find HTML files
function walkAndProcess(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      walkAndProcess(fullPath);
    } else if (
      entry.isFile() &&
      htmlExtensions.includes(path.extname(entry.name).toLowerCase())
    ) {
      processHtmlFile(fullPath);
    }
  }
}

function processHtmlFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let originalContent = content;

  for (const [originalUrl, filename] of filenameMap.entries()) {
    const regex = new RegExp(originalUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
    content = content.replace(regex, `images/${filename}`);
  }

  if (content !== originalContent) {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Updated: ${filePath}`);
  }
}

// Start the process
walkAndProcess(baseDir);
