#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import base64
from urllib.parse import unquote

def extract_string_array(js_code):
    """
    Извлекает основной массив строк из обфусцированного кода
    """
    print("=== Извлечение массива строк ===\n")
    
    # Ищем функцию _0x4941, которая возвращает массив строк
    array_match = re.search(r"function _0x4941\(\)\s*\{\s*const _0x[a-f0-9]+=\s*(\[.*?\]);", js_code, re.DOTALL)
    
    if array_match:
        array_content = array_match.group(1)
        
        # Извлекаем все строки из массива
        strings = re.findall(r"'([^']*)'", array_content)
        
        print(f"✓ Найден основной массив строк: {len(strings)} элементов")
        
        # Декодируем escape-последовательности
        decoded_strings = []
        for s in strings:
            try:
                decoded = s.encode().decode('unicode_escape')
                decoded_strings.append(decoded)
            except:
                decoded_strings.append(s)
        
        return decoded_strings
    
    return []

def analyze_functionality(strings):
    """
    Анализирует функциональность на основе строк
    """
    print("\n=== Анализ функциональности ===\n")
    
    # Группируем строки по категориям
    categories = {
        'UI_Elements': [],
        'API_Endpoints': [],
        'Error_Messages': [],
        'Success_Messages': [],
        'Form_Fields': [],
        'URLs': [],
        'Facebook_Related': [],
        'Currencies': [],
        'Timezones': [],
        'Countries': []
    }
    
    for s in strings:
        if not s or len(s) < 2:
            continue
            
        s_lower = s.lower()
        
        # UI элементы
        if any(word in s_lower for word in ['button', 'div', 'span', 'input', 'select', 'option', 'form']):
            categories['UI_Elements'].append(s)
        
        # API endpoints
        elif s.startswith('/') and len(s) > 3:
            categories['API_Endpoints'].append(s)
        
        # URL
        elif s.startswith(('http', 'https')):
            categories['URLs'].append(s)
        
        # Сообщения об ошибках
        elif any(word in s_lower for word in ['error', 'failed', 'invalid', 'wrong']):
            categories['Error_Messages'].append(s)
        
        # Сообщения об успехе
        elif any(word in s_lower for word in ['success', 'complete', 'created', 'done']):
            categories['Success_Messages'].append(s)
        
        # Facebook связанные
        elif any(word in s_lower for word in ['facebook', 'graph', 'fb', 'adaccount']):
            categories['Facebook_Related'].append(s)
        
        # Валюты
        elif re.match(r'^[A-Z]{3}$', s) or any(word in s_lower for word in ['dollar', 'euro', 'pound', 'yen']):
            categories['Currencies'].append(s)
        
        # Часовые пояса
        elif 'gmt' in s_lower or '/gmt' in s_lower or 'timezone' in s_lower:
            categories['Timezones'].append(s)
        
        # Поля формы
        elif any(word in s for word in ['name=', 'value=', 'id=', 'class=']):
            categories['Form_Fields'].append(s)
    
    # Выводим результаты
    for category, items in categories.items():
        if items:
            print(f"📂 {category.replace('_', ' ')}: {len(items)} элементов")
            for item in items[:5]:  # показываем первые 5
                print(f"   - {item}")
            if len(items) > 5:
                print(f"   ... и еще {len(items) - 5}")
            print()

def extract_key_functionality(js_code, strings):
    """
    Извлекает ключевую функциональность
    """
    print("=== Ключевая функциональность ===\n")
    
    # Ищем основную функцию создания аккаунта
    create_functions = []
    for i, s in enumerate(strings):
        if 'create' in s.lower() and ('account' in s.lower() or 'ad' in s.lower()):
            create_functions.append((i, s))
    
    if create_functions:
        print("🔧 Функции создания аккаунтов:")
        for idx, func in create_functions:
            print(f"   [{idx}] {func}")
        print()
    
    # Ищем URL-ы API
    api_urls = [s for s in strings if 'graph.facebook' in s or 'api' in s.lower()]
    if api_urls:
        print("🌐 API URLs:")
        for url in api_urls:
            print(f"   - {url}")
        print()
    
    # Ищем токены и параметры доступа
    access_related = [s for s in strings if any(word in s.lower() for word in ['token', 'access', 'key', 'auth'])]
    if access_related:
        print("🔑 Параметры доступа:")
        for param in access_related[:10]:
            print(f"   - {param}")
        print()
    
    # Ищем бизнес-логику
    business_logic = [s for s in strings if any(word in s.lower() for word in ['business', 'manager', 'advertiser'])]
    if business_logic:
        print("💼 Бизнес-логика:")
        for logic in business_logic:
            print(f"   - {logic}")
        print()

def decode_hex_strings(js_code):
    """
    Декодирует hex-строки в коде
    """
    print("=== Декодирование hex-строк ===\n")
    
    hex_matches = re.findall(r'\\x([0-9a-fA-F]{2})', js_code)
    if hex_matches:
        print(f"🔢 Найдено hex-последовательностей: {len(hex_matches)}")
        
        # Попытка декодировать как текст
        try:
            hex_bytes = bytes([int(h, 16) for h in hex_matches[:100]])  # первые 100
            decoded_text = hex_bytes.decode('utf-8', errors='ignore')
            if decoded_text.strip():
                print(f"📝 Декодированный текст (фрагмент):")
                print(f"   {decoded_text[:200]}...")
        except Exception as e:
            print(f"❌ Не удалось декодировать hex: {e}")

def generate_readable_summary(strings):
    """
    Генерирует читаемое резюме функциональности
    """
    print("\n" + "="*60)
    print("                РЕЗЮМЕ АНАЛИЗА")
    print("="*60)
    
    # Определяем основную цель
    print("\n🎯 ОСНОВНАЯ ЦЕЛЬ:")
    if any('adaccount' in s.lower() for s in strings):
        print("   ✓ Создание рекламных аккаунтов Facebook/Meta")
    
    if any('business' in s.lower() for s in strings):
        print("   ✓ Управление бизнес-менеджером")
    
    # Определяем возможности
    print("\n⚙️ ВОЗМОЖНОСТИ ИНСТРУМЕНТА:")
    capabilities = []
    
    if any('currency' in s.lower() for s in strings):
        capabilities.append("Настройка валют")
    
    if any('timezone' in s.lower() for s in strings):
        capabilities.append("Настройка часовых поясов")
    
    if any('create' in s.lower() and 'account' in s.lower() for s in strings):
        capabilities.append("Автоматическое создание аккаунтов")
    
    if any('token' in s.lower() for s in strings):
        capabilities.append("Работа с токенами доступа")
    
    for cap in capabilities:
        print(f"   ✓ {cap}")
    
    # Предупреждения
    print("\n⚠️  ВАЖНЫЕ ПРЕДУПРЕЖДЕНИЯ:")
    print("   🚫 Этот инструмент может нарушать условия использования Facebook")
    print("   🚫 Использование может привести к блокировке аккаунтов")
    print("   🚫 Автоматизация создания аккаунтов может быть незаконной")
    print("   🚫 Рекомендуется использовать только официальные API")

def main():
    """
    Основная функция декодера
    """
    try:
        # Читаем файл
        with open('/workspace/AKR ad account create bookmark tools.txt', 'r', encoding='utf-8') as f:
            js_code = f.read().strip()
        
        print("🔍 ПРОДВИНУТЫЙ АНАЛИЗ AKR AD ACCOUNT TOOL")
        print("="*60)
        
        # Извлекаем массив строк
        strings = extract_string_array(js_code)
        
        if strings:
            # Анализируем функциональность
            analyze_functionality(strings)
            
            # Извлекаем ключевую функциональность
            extract_key_functionality(js_code, strings)
            
            # Декодируем hex-строки
            decode_hex_strings(js_code)
            
            # Генерируем резюме
            generate_readable_summary(strings)
            
            # Сохраняем результаты
            with open('/workspace/detailed_analysis.json', 'w', encoding='utf-8') as f:
                analysis_data = {
                    'tool_type': 'Facebook Ad Account Creation Bookmarklet',
                    'strings_count': len(strings),
                    'decoded_strings': strings[:500],  # первые 500 строк
                    'analysis_date': '2024',
                    'warnings': [
                        'Может нарушать ToS Facebook',
                        'Потенциально небезопасно',
                        'Использовать на свой риск'
                    ]
                }
                json.dump(analysis_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Детальный анализ сохранен в detailed_analysis.json")
            
        else:
            print("❌ Не удалось извлечь массив строк")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()