#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import html
from urllib.parse import unquote

def decode_javascript_bookmarklet(js_code):
    """
    Декодирует обфусцированный JavaScript код
    """
    print("=== Анализ JavaScript кода ===\n")
    
    # Проверяем, начинается ли код с javascript:
    if js_code.startswith('javascript:'):
        js_code = js_code[11:]  # Убираем javascript: префикс
        print("✓ Найден JavaScript букмарклет")
    
    # Ищем основные части кода
    print("\n=== Поиск ключевых элементов ===")
    
    # Ищем строки с URL
    urls = re.findall(r'https?://[^\s\'"]+', js_code)
    if urls:
        print(f"\n🔗 Найденные URLs:")
        for url in set(urls):
            print(f"  - {url}")
    
    # Ищем строки, которые могут быть закодированы
    encoded_strings = re.findall(r'_0x[a-f0-9]+\([^)]+\)', js_code)
    print(f"\n🔤 Найдено закодированных строк: {len(set(encoded_strings))}")
    
    # Ищем массивы строк
    string_arrays = re.findall(r'\[([^\]]*[\'"][^\]]*)\]', js_code)
    if string_arrays:
        print(f"\n📚 Найдено массивов строк: {len(string_arrays)}")
        
        # Попытаемся извлечь строки из первого массива
        if string_arrays:
            first_array = string_arrays[0]
            strings = re.findall(r"'([^']*)'", first_array)
            if strings:
                print(f"\n📝 Примеры строк из массива (первые 10):")
                for i, s in enumerate(strings[:10]):
                    if s:  # только непустые строки
                        try:
                            # Попытка декодировать escape-последовательности
                            decoded = s.encode().decode('unicode_escape')
                            print(f"  {i+1}. {decoded}")
                        except:
                            print(f"  {i+1}. {s}")
    
    # Ищем функции обфускации
    obfus_functions = re.findall(r'function\s+_0x[a-f0-9]+\([^{]+\{[^}]+\}', js_code)
    print(f"\n⚙️ Найдено функций обфускации: {len(obfus_functions)}")
    
    # Ищем домены и endpoints
    domains = re.findall(r'[a-zA-Z0-9.-]+\.(?:com|org|net|ru|facebook|graph|api)', js_code)
    if domains:
        print(f"\n🌐 Найденные домены:")
        for domain in set(domains):
            if len(domain) > 3:  # отфильтровываем короткие совпадения
                print(f"  - {domain}")
    
    # Ищем API endpoints
    api_endpoints = re.findall(r'/[a-zA-Z_][a-zA-Z0-9_/]*', js_code)
    interesting_endpoints = [ep for ep in set(api_endpoints) if len(ep) > 3 and 'adaccount' in ep.lower()]
    if interesting_endpoints:
        print(f"\n🔌 Интересные API endpoints:")
        for endpoint in interesting_endpoints:
            print(f"  - {endpoint}")
    
    # Ищем упоминания создания аккаунтов
    account_related = re.findall(r'[a-zA-Z_]*[Aa]ccount[a-zA-Z_]*|[a-zA-Z_]*[Cc]reate[a-zA-Z_]*', js_code)
    if account_related:
        print(f"\n👤 Термины, связанные с аккаунтами:")
        for term in set(account_related):
            if len(term) > 3:
                print(f"  - {term}")
    
    # Ищем параметры и токены
    tokens_params = re.findall(r'(?:token|access|key|id)[\w_]*', js_code, re.IGNORECASE)
    if tokens_params:
        print(f"\n🔑 Найденные параметры токенов/ключей:")
        for param in set(tokens_params):
            print(f"  - {param}")
    
    return js_code

def extract_readable_strings(js_code):
    """
    Извлекает читаемые строки из кода
    """
    print("\n\n=== Извлечение читаемых строк ===")
    
    # Ищем все строки в кавычках
    strings = re.findall(r"'([^']*)'|\"([^\"]*)\"", js_code)
    readable_strings = []
    
    for s1, s2 in strings:
        s = s1 or s2
        if s and len(s) > 3:  # только строки длиннее 3 символов
            try:
                decoded = s.encode().decode('unicode_escape')
                if any(char.isalpha() for char in decoded):  # содержит буквы
                    readable_strings.append(decoded)
            except:
                if any(char.isalpha() for char in s):
                    readable_strings.append(s)
    
    # Удаляем дубликаты и сортируем
    readable_strings = sorted(set(readable_strings))
    
    print(f"\n📖 Найдено читаемых строк: {len(readable_strings)}")
    
    # Группируем по категориям
    urls = [s for s in readable_strings if s.startswith(('http', 'https', '/'))]
    ui_elements = [s for s in readable_strings if any(word in s.lower() for word in ['button', 'div', 'span', 'input', 'select', 'option'])]
    messages = [s for s in readable_strings if any(word in s.lower() for word in ['error', 'success', 'create', 'account', 'complete'])]
    
    if urls:
        print(f"\n🔗 URLs и пути ({len(urls)}):")
        for url in urls[:10]:  # показываем первые 10
            print(f"  - {url}")
    
    if ui_elements:
        print(f"\n🎨 UI элементы ({len(ui_elements)}):")
        for elem in ui_elements[:10]:
            print(f"  - {elem}")
    
    if messages:
        print(f"\n💬 Сообщения ({len(messages)}):")
        for msg in messages[:10]:
            print(f"  - {msg}")

def main():
    """
    Основная функция для декодирования файла
    """
    try:
        with open('/workspace/AKR ad account create bookmark tools.txt', 'r', encoding='utf-8') as f:
            js_code = f.read().strip()
        
        print("AKR Ad Account Creation Tool - Decoder")
        print("=" * 50)
        
        # Анализируем код
        decoded_code = decode_javascript_bookmarklet(js_code)
        
        # Извлекаем читаемые строки
        extract_readable_strings(js_code)
        
        # Сохраняем результат в более читаемом виде
        with open('/workspace/decoded_analysis.txt', 'w', encoding='utf-8') as f:
            f.write("=== АНАЛИЗ AKR AD ACCOUNT CREATION TOOL ===\n\n")
            f.write("Это JavaScript букмарклет для создания рекламных аккаунтов AKR.\n")
            f.write("Код сильно обфусцирован для скрытия функциональности.\n\n")
            f.write("ВНИМАНИЕ: Использование таких инструментов может нарушать\n")
            f.write("условия использования рекламных платформ!\n\n")
            f.write("Исходный код:\n")
            f.write("-" * 50 + "\n")
            f.write(js_code)
        
        print(f"\n\n✅ Анализ завершен!")
        print(f"📄 Детальный анализ сохранен в: decoded_analysis.txt")
        
    except Exception as e:
        print(f"❌ Ошибка при декодировании: {e}")

if __name__ == "__main__":
    main()