const fs = require('fs');

// Читаем закодированный файл
const encodedContent = fs.readFileSync('Bm Create.txt', 'utf8');

console.log('Начинаем продвинутое декодирование...');

// Убираем префикс "javascript:javascript%3A"
let decoded = encodedContent.replace(/^javascript:javascript%3A\s*/, '');

// Первый этап - URL декодирование
decoded = decodeURIComponent(decoded);

console.log('Этап 1: URL декодирование завершено');

// Анализируем структуру кода
console.log('Структура кода:', decoded.substring(0, 200) + '...');

// Попытка безопасного выполнения для получения декодированного содержимого
try {
    // Заменяем eval на функцию, которая возвращает результат вместо выполнения
    let safeCode = decoded;
    
    // Ищем eval(...) и пытаемся извлечь его аргумент
    const evalMatch = safeCode.match(/eval\((.+)\)$/s);
    if (evalMatch) {
        console.log('Найден eval, пытаемся декодировать его содержимое...');
        
        // Создаем безопасную среду выполнения
        const vm = require('vm');
        const sandbox = {
            String: String,
            Math: Math,
            console: console,
            decodeURIComponent: decodeURIComponent,
            escape: escape,
            result: null
        };
        
        // Заменяем eval на сохранение результата
        const modifiedCode = safeCode.replace(/eval\(/, 'result = (');
        
        try {
            vm.createContext(sandbox);
            vm.runInContext(modifiedCode, sandbox, { timeout: 5000 });
            
            if (sandbox.result) {
                console.log('Успешно декодировано!');
                fs.writeFileSync('final_decoded.js', sandbox.result);
                console.log('Декодированный код сохранен в final_decoded.js');
                
                // Показываем первые строки декодированного кода
                console.log('\nПервые строки декодированного кода:');
                console.log(sandbox.result.substring(0, 500) + '...');
            } else {
                console.log('Не удалось получить результат декодирования');
            }
        } catch (vmError) {
            console.log('Ошибка виртуальной машины:', vmError.message);
            
            // Альтернативный подход - ручной анализ
            console.log('Пытаемся альтернативный подход...');
            analyzeManually(decoded);
        }
    } else {
        console.log('eval не найден, анализируем вручную...');
        analyzeManually(decoded);
    }
    
} catch (error) {
    console.error('Ошибка при декодировании:', error.message);
    analyzeManually(decoded);
}

function analyzeManually(code) {
    console.log('\nРучной анализ структуры кода:');
    
    // Ищем основные паттерны
    const patterns = [
        /var\s+_0x[a-f0-9]+\s*=\s*\[([^\]]+)\]/,
        /function\s+_0x[a-f0-9]+\([^)]*\)/g,
        /"([^"]{10,})"/g
    ];
    
    patterns.forEach((pattern, index) => {
        const matches = code.match(pattern);
        if (matches) {
            console.log(`Паттерн ${index + 1} найден:`, matches.length, 'совпадений');
            if (index === 0 && matches[1]) {
                console.log('Массив строк:', matches[1].substring(0, 100) + '...');
            }
        }
    });
    
    // Сохраняем промежуточный результат
    fs.writeFileSync('manual_analysis.js', code);
    console.log('Промежуточный результат сохранен в manual_analysis.js');
}

console.log('\nДекодирование завершено!');