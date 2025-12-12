<?php
echo "<pre>";
echo "Current Working Directory: " . getcwd() . "\n";
echo "Script Path: " . __FILE__ . "\n";
echo "------------------------------------------------\n";
$cssPath = 'css/estilo.css';
$cssAbsPath = __DIR__ . '/css/estilo.css';

echo "Checking relative path: '$cssPath'\n";
if (file_exists($cssPath)) {
    echo " [OK] File exists via relative path.\n";
    echo " File Perms: " . substr(sprintf('%o', fileperms($cssPath)), -4) . "\n";
} else {
    echo " [ERROR] File NOT found via relative path.\n";
}

echo "Checking absolute path: '$cssAbsPath'\n";
if (file_exists($cssAbsPath)) {
    echo " [OK] File exists via absolute path.\n";
} else {
    echo " [ERROR] File NOT found via absolute path.\n";
}

echo "------------------------------------------------\n";
echo "Directory Permissions (css/):\n";
if (file_exists('css')) {
    echo " [OK] 'css' directory exists.\n";
    echo " Dir Perms: " . substr(sprintf('%o', fileperms('css')), -4) . "\n";
} else {
    echo " [ERROR] 'css' directory not found.\n";
}
echo "</pre>";
