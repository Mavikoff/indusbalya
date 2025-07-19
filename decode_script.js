const fs = require('fs');

// Читаем закодированный файл
const encodedContent = fs.readFileSync('Bm Create.txt', 'utf8');

console.log('Начинаем декодирование...');

// Убираем префикс "javascript:javascript%3A"
let decoded = encodedContent.replace(/^javascript:javascript%3A\s*/, '');

// Декодируем URL-кодирование
decoded = decodeURIComponent(decoded);

console.log('Первый этап декодирования (URL decode):');
console.log(decoded.substring(0, 500) + '...\n');

// Пытаемся выполнить дальнейшее декодирование, если это возможно
try {
    // Если это функция, которая возвращает декодированный код
    if (decoded.includes('function') && decoded.includes('eval')) {
        console.log('Обнаружена функция с eval. Попытка безопасного декодирования...');
        
        // Заменяем eval на console.log для безопасности
        const safeDecoded = decoded.replace(/eval\s*\(/g, 'console.log(');
        
        // Сохраняем безопасную версию для анализа
        fs.writeFileSync('decoded_safe.js', safeDecoded);
        console.log('Безопасная версия сохранена в decoded_safe.js');
    }
    
    // Сохраняем декодированную версию
    fs.writeFileSync('decoded.js', decoded);
    console.log('Декодированный код сохранен в decoded.js');
    
} catch (error) {
    console.error('Ошибка при декодировании:', error.message);
}

console.log('\nДекодирование завершено!');
console.log('Размер исходного файла:', encodedContent.length, 'символов');
console.log('Размер декодированного:', decoded.length, 'символов');