# -*- coding: utf-8 -*-

GOOGLE_CREDENTIALS = {
  "type": "service_account",
  "project_id": "licenca-postador",
  "private_key_id": "b4be4979e5aaf3c62404f60b187dd779953ffad2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1zwvzgkEwWvKr\nVwbu7MJF3x8xL3RbK7dyqxgiEedqB14VWWpVz+ThdL82L14BxKkGehmGMLfKHf7W\nlnaF05iLprFnETxb+g7N+HUd/g63jKtLi9PHHEs0CEuucvJ/Hp5oa1nJGyAZa3lH\njYYBNP6WcswfoznRwj+HCz4aOf5Dsi1RYZj+YCarnrrtcTMyi67qkZVGaOMGA20v\nYxJEseGvzwfkqEsts7KU2r4TI6WzDVlkndELbxpZyY5KLNjTzHj8DctdBw/7dB9b\nwfhLynnkC2cSDtsteTirFm/eenm0vwTfMcAiFDVYhnd6FARD7WHZni16UgX4GmJ+\nvnGW9JDfAgMBAAECggEAOwDP2x5Zs6zAdrTOrjmuLujjgZ3qADCm35MBSQVQeguc\nEAetx92pZTXzXE1xD9fYFx8HK5KiAvlLHC9GldX++suFZXKliSAVL+lDcRFji1Qe\nv2zItSTMjz1l+l6ZroGsXS0BvY+NElLb0EnwxHGDciYdcuMRP67v2Q7f/7j0eNlM\nMIueKPO9o6gaBBzgGKai9fPM3HV2JOYpJv8wjhVuKNU0yrsAsrEjOV+FR6GLMrI3\nuaTdYGP74S0PmOBPyxmcf7NsrORkzB62Oa4j8g7E+JCP3lG5JWN/+hVwTP8kc4Ug\nNKGjrUxOtB1aU5hSU4yKdr0JeY7kra9fuFK8BlC1IQKBgQD2alEgXYr1YeRzhdGJ\nhfaNobVZaccqSrLU9nG46h3UytOCZUFfLrzRhIrVNz/x061WedFAS2M9rAfxpIxD\nU5XPAzWAKVuM1iIF/EfOBEi1VqZY+2cAwdxOhbss41yrxucQGWoIwba0NFksofRi\nobpvb70nbECRnxvybhZJXFzLDwKBgQC84WjbdqWR398dKrWUEAqrTDimmLsouaBG\nN51aZc7w6Crv3PmEz/0aWbBAlvWv2Xv6iqVjFNZ0J1LYNyKaoqgTJDZs09L4k+dw\n+v5pln4VlrRVOXUgbBADakV1k4bW/APwqLn0gnCwtzlDXs1KwdT9zwB++fmk0qf5\n5XcUur8dMQKBgQCr+OMJfX8/ZcR0Q05LdizuB49zCXmwMFXCfwQ7E1kiazNV66jF\n7u5kIuZpi5ebBCoTEg1Rm8t0/RzGLhqd2jXRNeIewb5c+gzgtILAawj7Va/epgXq\n52EDhB1vZHYGhFg6SiJQXjFObsJVfen68/gTUZ5nZwthFfQBK4duR4GTTQKBgHIh\nAesaVhE+5OIK3I0K5Gd9Nv3za6PABkhncn0c515J6yfkriDCTH2PlCBzFyGamH9b\nJ3QnMy4cVMKxDgfCISzvxLMdi20IceCiyPekJ6uD1JNqlItywHpPzIivC9r7jKXu\nTe6gotck30UGE6YIWVrDqdkP0vj1EOq+7KVp8fEBAoGBAJUGpQgmnrgOG4EP37kH\n6W33hkn3BxSGG9Kd3aEni/EgOSAmoNbeuNygizJIofVHNCnPpevkc3sMR9Dkvawb\n7WQoqEYe1eyj4gvo56bWkdMHXCQFdmqgymtsk/POOm00f2yaYYGpajVz1WY3gxnL\ncu/p4IygbAAzV5rNDmxWPaPS\n-----END PRIVATE KEY-----\n",
  "client_email": "licenca-bot@licenca-postador.iam.gserviceaccount.com",
  "client_id": "104756459725741242918",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/licenca-bot%40licenca-postador.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta
import sys
import io
import traceback
import time
import random
import os
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
from ixbrowser_local_api import IXBrowserClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import requests
import socket
import subprocess

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

LOG_ERROS_FILE = "perfis_com_erro.txt"
CONFIG_FILE = "config.json"
WAIT_TIME_SECONDS = 15
stop_posting = False
start_time_posting_global = 0
posts_realizados_count_global = 0
DEFAULT_API_URL = "http://127.0.0.1:53200"
ALTERNATIVE_PORTS = [53201, 53202]

total_perfis_var = None
total_posts_var = None
posts_realizados_var = None
tempo_conclusao_var = None
prox_link_horario_var = None
perfis_treeview = None
ordem_postagem_var = None

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0: return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0: return f"{minutes}m {secs}s"
    else: return f"{secs}s"

def validate_api_url(api_url):
    return bool(re.match(r'^http://[a-zA-Z0-9.-]+:\d+$', api_url))

def check_port(host, port, log_text_func):
    try:
        with socket.create_connection((host, port), timeout=2):
            log_text_func(f"Porta {port} está aberta em {host}.\n"); return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        log_text_func(f"Porta {port} não está acessível em {host}.\n"); return False

def check_ixbrowser_process(log_text_func):
    if not PSUTIL_AVAILABLE:
        log_text_func("Aviso: psutil não instalado.\n"); return False
    try:
        for proc in psutil.process_iter(['name']):
            if 'ixbrowser' in proc.info['name'].lower():
                log_text_func(f"Processo IXBrowser: {proc.info['name']} (PID: {proc.pid})\n"); return True
        log_text_func("Nenhum processo IXBrowser encontrado.\n"); return False
    except Exception as e: log_text_func(f"Erro ao verificar processo IXBrowser: {e}\n"); return False

def test_api_manually(api_url, log_text_func):
    host = api_url.split(':')[1].strip('/'); port = int(api_url.split(':')[2])
    log_text_func(f"Testando conexão manual com {api_url}/api/v2/group/list...\n")
    if not check_ixbrowser_process(log_text_func): log_text_func("Dica: Inicie o IXBrowser.\n")
    if not check_port(host, port, log_text_func): log_text_func(f"Dica: API Local habilitada e porta {port} correta?\n")
    try:
        response = requests.post(f"{api_url}/api/v2/group/list", timeout=10)
        log_text_func(f"Teste manual API - HTTP: {response.status_code}\n")
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, list): return True, f"Conexão manual OK. Grupos: {len(data)}"
                elif isinstance(data, dict):
                    code=data.get('code'); msg=data.get('message'); groups_raw=data.get('data'); groups=groups_raw if isinstance(groups_raw,list) else []
                    if code == 0: return True, f"Conexão manual OK. Grupos: {len(groups)}"
                    else: return False, f"Erro API: Cód {code} - {msg}"
                return False, "Erro: Formato JSON inesperado."
            except ValueError: return False, "Erro: Resposta API não é JSON válido."
        else: return False, f"Erro: HTTP {response.status_code}"
    except requests.ConnectionError:
        log_text_func("Erro conexão manual API.\n")
        return False, "Erro: Não foi possível conectar API."
    except Exception as e: return False, f"Erro: {e}"

def get_all_groups(log_text_func, api_url):
    if not validate_api_url(api_url): log_text_func(f"Erro: API URL inválida: {api_url}.\n"); return []
    log_text_func(f"Obtendo grupos via API: {api_url}/api/v2/group/list...\n")
    try:
        client = IXBrowserClient(); groups_response = client.get_group_list()
        if groups_response is None:
            log_text_func("Erro: Resposta API None.\n"); return []
        if isinstance(groups_response, list):
            mapped = [{'group_name':g.get('title'), 'group_id':g.get('id')} for g in groups_response if g.get('title') and g.get('id')]
            return mapped
        code=getattr(client,'code',None); message=getattr(client,'message',None)
        if code != 0:
            log_text_func(f"Erro ao obter grupos: Cód {code} - {message}\n"); return []
        groups_data = groups_response.get('data', [])
        if not isinstance(groups_data, list): return []
        mapped = [{'group_name':gi.get('group_name'), 'group_id':gi.get('group_id')} for gi in groups_data if gi.get('group_name') and gi.get('group_id')]
        return mapped
    except Exception as e: log_text_func(f"Erro inesperado obter grupos: {e}\n"); return []

def test_api_connection(api_url, log_text_func):
    if not validate_api_url(api_url): return False, f"API URL inválida: {api_url}."
    try:
        host, port_str = api_url.split(":")[1].strip("/"), api_url.split(":")[2]; port = int(port_str)
        if not check_port(host, port, log_text_func):
            return False, f"Erro: Porta {port} inacessível."
        client = IXBrowserClient(); response = client.get_group_list()
        if response is None: return False, "Erro conexão: resposta None."
        if isinstance(response, list): return True, f"Conexão OK. Grupos: {len(response)}"
        code=getattr(client,"code",None); message=getattr(client,"message",None)
        if code != 0: return False, f"Erro API: Cód {code} - {message}"
        groups_data = response.get("data",[])
        return True, f"Conexão OK. Grupos: {len(groups_data)}"
    except Exception as e: return False, f"Erro: {e}"

def get_profiles_from_group(group_id, log_text_func, api_url):
    if not validate_api_url(api_url):
        log_text_func(f"Erro: API URL inválida: {api_url}.\n")
        return []
    
    all_profiles = []
    page = 1
    
    try:
        client = IXBrowserClient()
        client.api_url = api_url

        while True:
            log_text_func(f"Buscando perfis... Página: {page}\n")
            
            try:
                profiles_response = client.get_profile_list(group_id=group_id, page=page)
            except TypeError:
                if page == 1:
                    log_text_func("AVISO: A biblioteca não suporta paginação. Carregando apenas a primeira página de perfis.\n")
                    profiles_response = client.get_profile_list(group_id=group_id)
                else:
                    break

            if isinstance(profiles_response, dict) and profiles_response.get('code', -1) == 0:
                data_field = profiles_response.get('data', {})
                current_page_profiles = data_field.get('list', []) if isinstance(data_field, dict) else []
            elif isinstance(profiles_response, list):
                 current_page_profiles = profiles_response
            else:
                code = getattr(client, 'code', 'N/A')
                message = getattr(client, 'message', 'Resposta inválida da API')
                log_text_func(f"Erro ao obter perfis: Cód {code} - {message}\n")
                break

            if not current_page_profiles:
                log_text_func("Todos os perfis foram carregados (página vazia recebida).\n")
                break
            
            all_profiles.extend(current_page_profiles)
            
            if len(current_page_profiles) < 10:
                log_text_func("Última página de perfis alcançada.\n")
                break
                
            page += 1
            time.sleep(0.5)

    except Exception as e:
        log_text_func(f"Erro inesperado ao obter perfis: {e}\n")
        traceback.print_exc()
    
    log_text_func(f"Total de {len(all_profiles)} perfis carregados do grupo.\n")
    return all_profiles

def ler_perfis_grupos(group_id, log_text_func, api_url):
    profiles_data = get_profiles_from_group(group_id, log_text_func, api_url)
    dados_perfis = []
    if not profiles_data: return []
    for p_dict in profiles_data:
        p_id = p_dict.get('profile_id')
        p_name = p_dict.get('name', f'Perfil Sem Nome (ID: {p_id})')
        notes = p_dict.get('note', '')
        p_tag_name = p_dict.get('tag_name', '')
        if not p_id: continue
        group_url = extract_group_url_from_notes(notes, log_text_func)
        if group_url: dados_perfis.append((p_id, group_url, p_name, p_tag_name))
    return dados_perfis

def extract_group_url_from_notes(notes, log_text_func):
    if not notes or not isinstance(notes, str) or notes.strip() == '': return None
    url_pattern = r'https?://(?:www\.|web\.|m\.)?facebook\.com/groups/[a-zA-Z0-9._-]+/?|https?://(?:www\.|web\.|m\.)?facebook\.com/profile\.php\?id=\d+|https?://[^\s]+'
    match = re.search(url_pattern, notes)
    if match:
        url = match.group(0).strip()
        if "facebook.com/groups/" in url or "facebook.com/profile.php?id=" in url: return url
    return None

def salvar_configuracoes(email, grupo, links, textos, intervalo_perfis, intervalo_links, api_url, atraso_inicial_min):
    config = {"email":email,"grupo":grupo,"links":links,"textos":textos,"intervalo_perfis":intervalo_perfis,"intervalo_links":intervalo_links,"api_url":api_url,"atraso_inicial_min":atraso_inicial_min}
    try:
        with open(CONFIG_FILE,'w',encoding='utf-8') as f: json.dump(config,f,indent=4,ensure_ascii=False); return True
    except Exception as e: print(f"Erro salvar config: {e}"); return False

def carregar_configuracoes():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE,'r',encoding='utf-8') as f: return json.load(f)
        except: pass
    return {}

def verificar_licenca(email_usuario, log_text_func):
    if not email_usuario: return False
    try:
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_info(GOOGLE_CREDENTIALS, scopes=scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("LicencasFacebookPoster"); sheet = spreadsheet.worksheet("Licencas")
        registros = sheet.get_all_records(); hoje = datetime.now().date()
        for r in registros:
            if r.get('email') == email_usuario:
                status = r.get('status','').lower(); val_str = r.get('validade')
                if status != 'ativo': return False
                if not val_str: return False
                try:
                    validade = datetime.strptime(val_str,'%Y-%m-%d').date()
                    if validade < hoje: return False
                    return True
                except ValueError: return False
        return False
    except Exception as e: log_text_func(f"Erro verificar licença: {e}\n"); return False

def open_ixbrowser_profile(profile_id, log_text_func, api_url):
    if not validate_api_url(api_url): return None,None
    try:
        client=IXBrowserClient(); client.api_url=api_url
        res=client.open_profile(profile_id,cookies_backup=False,load_profile_info_page=False)
        code=getattr(client,'code',None); msg=getattr(client,'message',None)
        if isinstance(res,dict) and res.get("debugging_address") and res.get("webdriver"):
            drv_path=res.get('webdriver') or res.get('driver_path'); dbg_addr=res.get("debugging_address")
            if drv_path and dbg_addr: return drv_path,dbg_addr
        return None,None
    except Exception as e: return None,None

def close_ixbrowser_profile(profile_id, log_text_func, api_url):
    if not validate_api_url(api_url): return
    try:
        client=IXBrowserClient(); client.api_url=api_url
        client.close_profile(profile_id)
    except Exception as e: pass

def create_driver(driver_path, debugger_address, log_text_func):
    log_text_func("Configurando WebDriver Selenium...\n")
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress",debugger_address)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")
    chrome_options.add_argument("--window-size=375,812")
    chrome_options.add_argument("--disable-desktop-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    
    use_mobile_emulation = False
    
    if use_mobile_emulation:
        try:
            mobile_emulation = {
                "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            log_text_func("Configuração mobileEmulation aplicada.\n")
        except Exception as e_mobile:
            log_text_func(f"Aviso: mobileEmulation não suportado ({e_mobile}), usando argumentos alternativos.\n")
    else:
        log_text_func("Usando configuração via argumentos (mais compatível).\n")
    
    try:
        if not driver_path or not os.path.exists(driver_path): 
            log_text_func(f"ERRO CRÍTICO: ChromeDriver path '{driver_path}' não existe.\n")
            return None
        
        log_text_func(f"Usando ChromeDriver: {driver_path}\nConectando Debugger: {debugger_address}\n")
        service=Service(executable_path=driver_path)
        driver=webdriver.Chrome(service=service,options=chrome_options)
        
        time.sleep(2)
        
        try:
            driver.set_window_size(375, 812)
            log_text_func("Viewport definido: 375x812.\n")
            
            driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
                "width": 375,
                "height": 812,
                "deviceScaleFactor": 3,
                "mobile": True,
                "fitWindow": False
            })
            
            driver.execute_cdp_cmd('Emulation.setUserAgentOverride', {
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
                "platform": "iPhone"
            })
            
            log_text_func("Configurações aplicadas via CDP.\n")
        except Exception as e_cdp:
            log_text_func(f"Aviso: Algumas configurações CDP não aplicadas ({e_cdp}).\n")
        
        try:
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
                'source': """
                    Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                    window.navigator.chrome = {runtime: {}};
                    Object.defineProperty(navigator, 'languages', {get: () => ['pt-BR', 'pt', 'en-US', 'en']});
                    Object.defineProperty(navigator, 'plugins', {get: () => [
                        {name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format'},
                        {name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai', description: ''},
                        {name: 'Native Client', filename: 'internal-nacl-plugin', description: ''}
                    ]});
                    
                    if (!window.TouchEvent) {
                        window.TouchEvent = function() {};
                    }
                    
                    Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 5});
                    Object.defineProperty(navigator, 'msMaxTouchPoints', {get: () => 5});
                """
            })
            log_text_func("Scripts anti-detecção aplicados.\n")
        except Exception as e_script:
            log_text_func(f"Aviso: Scripts anti-detecção não aplicados ({e_script}).\n")
        
        log_text_func("WebDriver conectado com sucesso.\n")
        
        try:
            current_title = driver.title
            current_url = driver.current_url
            log_text_func(f"Status inicial - Título: '{current_title}', URL: '{current_url}'\n")
        except Exception as e:
            log_text_func(f"Aviso: Não foi possível obter status inicial ({e}).\n")
            
        return driver
        
    except WebDriverException as e_wd:
        log_text_func(f"ERRO WebDriverException: {e_wd}\n")
        if "cannot connect" in str(e_wd).lower() or "disconnected" in str(e_wd).lower():
            log_text_func("DICA: Navegador fechado/conexão perdida.\n")
        elif "version" in str(e_wd).lower():
            log_text_func(f"DICA: Incompatibilidade ChromeDriver e IXBrowser.\n")
        elif "invalid argument" in str(e_wd).lower() and "mobileEmulation" in str(e_wd):
            log_text_func("DICA: ChromeDriver não suporta mobileEmulation. Usando método alternativo...\n")
            return create_driver_fallback(driver_path, debugger_address, log_text_func)
        elif "chrome not reachable" in str(e_wd).lower():
            log_text_func("DICA: Chrome não acessível. Verifique se o perfil IXBrowser está aberto.\n")
        return None
    except Exception as e: 
        log_text_func(f"ERRO GERAL config WebDriver: {e}\n")
        traceback.print_exc()
        return None

def create_driver_fallback(driver_path, debugger_address, log_text_func):
    log_text_func("Tentando criar WebDriver com configuração básica (fallback)...\n")
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress",debugger_address)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")
    chrome_options.add_argument("--window-size=375,812")
    
    try:
        service=Service(executable_path=driver_path)
        driver=webdriver.Chrome(service=service,options=chrome_options)
        time.sleep(2)
        
        try:
            driver.set_window_size(375, 812)
            log_text_func("WebDriver básico criado com viewport.\n")
        except:
            pass
            
        return driver
    except Exception as e:
        log_text_func(f"ERRO também no fallback: {e}\n")
        return None

def verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func, screenshot_dir="fb_screenshots"):
    os.makedirs(screenshot_dir,exist_ok=True)
    log_text_func(f"Verificando bloqueio perfil ID: {profile_id} (Nome: {profile_name})...\n")
    try:
        time.sleep(random.uniform(4,6))
        page_title=driver.title.lower()
        page_url=driver.current_url.lower()
        
        try:
            body=driver.find_element(By.TAG_NAME,"body")
            content_snippet=body.text.lower()[:2000]
        except Exception as e_body:
            log_text_func(f"Aviso: Não foi possível obter conteúdo da página ({e_body}).\n")
            content_snippet = ""
        
        keywords=[
            "sua conta foi suspensa","conta restrita","conta bloqueada","confirme sua identidade",
            "atividade incomum","para sua segurança","restringimos sua conta","conta desabilitada",
            "você não pode usar o facebook","sua conta está restrita","ajude-nos a confirmar",
            "parece que sua conta enviou spam","verificação de segurança","algo deu errado",
            "temporariamente bloqueada","para evitar qualquer uso indevido","não pode fazer publicações",
            "padrões da comunidade","limite de quantas vezes","não pode usar este recurso",
            "tente novamente mais tarde","confirme que esta conta","conta hackeada",
            "your account has been suspended","account restricted","account disabled",
            "confirm your identity","unusual activity","for your security"
        ]
        
        url_parts=["/checkpoint","/challenge","/login/device-based/regular/login/",
                  "facebook.com/login.php","/account/disabled","/account/locked",
                  "/account_recovery","/security_check","/restricted","/support/"]
        
        safe_name=profile_name.replace(' ','_').replace('/','_').replace('\\','_')
        
        for kw in keywords:
            if kw in page_title:
                log_text_func(f"ALERTA(Título) Perfil {profile_id}({profile_name}): BLOQUEADO. KW: '{kw}'\n")
                ts=time.strftime("%Y%m%d-%H%M%S")
                sf=os.path.join(screenshot_dir,f"fb_bloq_tit_p{profile_id}_{safe_name}_{ts}.png")
                try:
                    driver.save_screenshot(sf)
                    log_text_func(f"Screenshot: {sf}\n")
                except Exception as e:
                    log_text_func(f"Falha screenshot: {e}\n")
                return True
        
        for up in url_parts:
            if up in page_url:
                if (up=="facebook.com/login.php" or "/login/device-based/regular/login/" in up) and any(k in page_title for k in ["facebook","feed","notícias","home","página inicial"]):
                    log_text_func(f"INFO: URL '{up}' ({profile_name}), título sugere login normal: '{driver.title}'.\n")
                else:
                    log_text_func(f"ALERTA(URL) Perfil {profile_id}({profile_name}): BLOQUEADO. URL suspeita: '{page_url}'\n")
                    ts=time.strftime("%Y%m%d-%H%M%S")
                    sf=os.path.join(screenshot_dir,f"fb_bloq_url_p{profile_id}_{safe_name}_{ts}.png")
                    try:
                        driver.save_screenshot(sf)
                        log_text_func(f"Screenshot: {sf}\n")
                    except Exception as e:
                        log_text_func(f"Falha screenshot: {e}\n")
                    return True
        
        if content_snippet:
            for kw in keywords:
                if kw in content_snippet:
                    log_text_func(f"ALERTA(Conteúdo) Perfil {profile_id}({profile_name}): BLOQUEADO. KW: '{kw}'\n")
                    ts=time.strftime("%Y%m%d-%H%M%S")
                    sf=os.path.join(screenshot_dir,f"fb_bloq_cont_p{profile_id}_{safe_name}_{ts}.png")
                    try:
                        driver.save_screenshot(sf)
                        log_text_func(f"Screenshot: {sf}\n")
                    except Exception as e:
                        log_text_func(f"Falha screenshot: {e}\n")
                    return True
        
        log_text_func(f"Perfil {profile_id}({profile_name}) passou verificações bloqueio.\n")
        return False
        
    except WebDriverException as e:
        log_text_func(f"WebDriverException verificar bloqueio ({profile_name}): {e}.\n")
        return True
    except Exception as e:
        log_text_func(f"Erro inesperado verificar bloqueio ({profile_name}): {e}\n")
        traceback.print_exc()
        return False

def convert_to_mobile_url(url):
    if "facebook.com" in url:
        mobile_url = url.replace("www.facebook.com", "m.facebook.com")
        mobile_url = mobile_url.replace("web.facebook.com", "m.facebook.com")
        if "m.facebook.com" not in mobile_url and "facebook.com" in mobile_url:
            mobile_url = mobile_url.replace("facebook.com", "m.facebook.com")
        return mobile_url
    return url

def post_to_facebook_group_mobile(driver, group_url, link, text, wait_time, profile_id, profile_name, erros_lista, log_text_func):
    if not driver:
        if not any(err_item[0] == profile_id for err_item in erros_lista):
            erros_lista.append((profile_id, profile_name))
        return False

    screenshot_dir = "fb_screenshots"; os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    safe_profile_name = profile_name.replace(' ','_').replace('/','_').replace('\\','_')
    screenshot_file_base = os.path.join(screenshot_dir, f"fb_err_p{profile_id}_{safe_profile_name}_{timestamp}")
    
    mobile_group_url = convert_to_mobile_url(group_url)
    log_text_func(f"--- Postando (Perfil {profile_id} - {profile_name}) ---\n")

    try:
        log_text_func(f"Navegando para o grupo: {mobile_group_url}\n")
        driver.get(mobile_group_url)
        time.sleep(random.uniform(8, 12))
        
        page_title = driver.title
        log_text_func(f"Página carregada: {page_title}\n")

        try:
            login_check = driver.find_elements(By.XPATH, "//a[contains(@href, 'login')] | //input[@name='email']")
            if login_check:
                log_text_func(f"ERRO: Perfil {profile_name} não está logado no Facebook.\n")
                driver.save_screenshot(f"{screenshot_file_base}_not_logged_in.png")
                
                # NOVA LÓGICA: Verificar bloqueio apenas quando há erro de login
                log_text_func(f"Erro de login detectado. Verificando se é bloqueio...\n")
                if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                    log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                else:
                    log_text_func(f"Perfil {profile_name} não está bloqueado, apenas deslogado.\n")
                
                if not any(err_item[0] == profile_id for err_item in erros_lista): 
                    erros_lista.append((profile_id, profile_name))
                return False
        except: pass

        log_text_func("Procurando o campo para iniciar postagem...\n")
        
        post_trigger_xpaths = [
            "//div[contains(text(), 'Escreva algo')]",
            "//span[contains(text(), 'Escreva algo')]",
            "//div[@role='button'][contains(., 'Escreva algo')]",
            "//div[contains(@aria-label, 'Escreva algo')]",
            
            "//div[contains(text(), 'Write something')]",
            "//span[contains(text(), 'Write something')]",
            "//div[@role='button'][contains(., 'Write something')]",
            
            "//div[contains(@data-sigil, 'composer')]",
            "//div[contains(@class, 'composerInput')]",
            "//div[@data-sigil='m-composer-text-input']",
            
            "//textarea[contains(@placeholder, 'No que você está pensando')]",
            "//textarea[contains(@placeholder, 'What')]",
            "//div[@contenteditable='true'][@role='textbox']",
            
            "//div[contains(@class, '_5rpu')]",
            "//div[contains(@class, 'mfss')]",
            "//*[contains(@placeholder, 'Escreva') or contains(@placeholder, 'Write')]",
        ]
        
        post_trigger = None
        for i, xp in enumerate(post_trigger_xpaths):
            try:
                log_text_func(f"Tentando XPath {i+1}: {xp}\n")
                elements = driver.find_elements(By.XPATH, xp)
                if elements:
                    for element in elements:
                        try:
                            if element.is_displayed() and element.is_enabled():
                                post_trigger = element
                                log_text_func(f"Gatilho de postagem encontrado (XPath {i+1}): {element.tag_name}\n")
                                break
                        except:
                            continue
                    if post_trigger:
                        break
            except Exception as e:
                log_text_func(f"Erro XPath {i+1}: {e}\n")
                continue

        if not post_trigger:
            log_text_func(f"ERRO CRÍTICO: Gatilho de postagem não encontrado.\n")
            driver.save_screenshot(f"{screenshot_file_base}_trigger_not_found.png")
            log_text_func(f"Screenshot salvo: {screenshot_file_base}_trigger_not_found.png\n")
            
            # NOVA LÓGICA: Verificar bloqueio apenas quando não encontra elementos de postagem
            log_text_func(f"Elementos de postagem não encontrados. Verificando se é bloqueio...\n")
            if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                log_text_func(f"Perfil {profile_name} está bloqueado.\n")
            else:
                log_text_func(f"Perfil {profile_name} não está bloqueado, problema na localização dos elementos.\n")
            
            try:
                with open(f"{screenshot_file_base}_page_source.html", "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
                log_text_func(f"HTML da página salvo para análise: {screenshot_file_base}_page_source.html\n")
            except Exception as e_html:
                log_text_func(f"Erro ao salvar HTML: {e_html}\n")
            
            if not any(err_item[0] == profile_id for err_item in erros_lista): 
                erros_lista.append((profile_id, profile_name))
            return False

        modal_aberto = False
        try:
            log_text_func("Clicando no gatilho de postagem (JavaScript)...\n")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", post_trigger)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", post_trigger)
            log_text_func("Aguardando modal/área de postagem abrir...\n")
            time.sleep(random.uniform(4, 7))
            modal_aberto = True
        except Exception as e_click:
            log_text_func(f"ERRO ao clicar no gatilho com JS: {e_click}\n")
            try:
                log_text_func("Tentando clique Selenium normal...\n")
                post_trigger.click()
                time.sleep(random.uniform(4, 7))
                modal_aberto = True
            except Exception as e_click2:
                log_text_func(f"ERRO: Falha ao clicar no gatilho: {e_click2}\n")
                driver.save_screenshot(f"{screenshot_file_base}_trigger_click_failed.png")
                
                # NOVA LÓGICA: Verificar bloqueio apenas quando falha ao clicar
                log_text_func(f"Falha ao clicar no elemento. Verificando se é bloqueio...\n")
                if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                    log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                else:
                    log_text_func(f"Perfil {profile_name} não está bloqueado, problema no clique do elemento.\n")
                
                if not any(err_item[0] == profile_id for err_item in erros_lista): 
                    erros_lista.append((profile_id, profile_name))
                return False

        if not modal_aberto:
            log_text_func(f"ERRO: Modal/área de postagem não abriu.\n")
            if not any(err_item[0] == profile_id for err_item in erros_lista): 
                erros_lista.append((profile_id, profile_name))
            return False

        log_text_func("Procurando campo 'Escreva algo...' no composer aberto...\n")
        composer_text_field_xpaths = [
            "//div[contains(text(), 'Escreva algo') and contains(@style, 'color')]",
            "//div[contains(text(), 'Escreva algo...')]",
            "//div[contains(@class, 'native-text') and contains(text(), 'Escreva algo')]",
            "//div[@role='button'][contains(text(), 'Escreva algo')]",
            
            "//div[contains(@aria-label, 'No que você está pensando')]",
            "//div[contains(@aria-label, 'What')]",
            "//div[contains(@aria-label, 'Crie um post')]",
            "//div[contains(@aria-label, 'Create a post')]",
            
            "//div[contains(@data-placeholder, 'Escreva')]",
            "//div[contains(@data-placeholder, 'Write')]",
            
            "//div[contains(@class, 'composer')]//div[@role='button']",
            "//div[contains(@data-sigil, 'composer')]//div[@role='button']",
        ]
        
        composer_field = None
        for i, xpath_comp in enumerate(composer_text_field_xpaths):
            try:
                log_text_func(f"Tentando XPath composer {i+1}: {xpath_comp}\n")
                elements = driver.find_elements(By.XPATH, xpath_comp)
                if elements:
                    for element in elements:
                        try:
                            if element.is_displayed() and element.is_enabled():
                                composer_field = element
                                log_text_func(f"Campo composer encontrado (XPath {i+1}): {element.tag_name}\n")
                                break
                        except:
                            continue
                    if composer_field:
                        break
            except Exception as e:
                log_text_func(f"Erro XPath composer {i+1}: {e}\n")
                continue

        if composer_field:
            log_text_func("Clicando no campo do composer para ativar área de texto...\n")
            try:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", composer_field)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", composer_field)
                time.sleep(random.uniform(3, 5))
                log_text_func("Campo do composer clicado. Aguardados 2 segundos. Colando link diretamente...\n")
                
                try:
                    actions = ActionChains(driver)
                    actions.send_keys(link).perform()
                    log_text_func(f"Link colado via ActionChains: {link}\n")
                    
                    log_text_func("Pressionando Tab para carregar preview do link...\n")
                    try:
                        actions = ActionChains(driver)
                        actions.send_keys(Keys.TAB).perform()
                        log_text_func("Tab pressionado para carregar preview.\n")
                    except Exception as e_tab:
                        log_text_func(f"Erro ao pressionar Tab: {e_tab}\n")
                        try:
                            actions = ActionChains(driver)
                            actions.send_keys(Keys.TAB).perform()
                            log_text_func("Tab pressionado novamente (fallback).\n")
                        except Exception as e_tab2:
                            log_text_func(f"Erro no Tab fallback: {e_tab2}\n")
                    
                    log_text_func("Aguardando 8s para preview do link carregar...\n")
                    time.sleep(8)
                    
                    log_text_func("Procurando campo de texto específico após Tab...\n")
                    try:
                        text_fields_after_tab = [
                            "//div[@role='button'][@aria-label='No que você está pensando? Crie um post.']",
                            "//div[@role='button'][contains(@aria-label, 'No que você está pensando')]",
                            "//div[@role='button'][contains(@aria-label, 'Crie um post')]",
                            
                            "//div[@role='button'][@aria-label='What\'s on your mind? Create a post.']",
                            "//div[@role='button'][contains(@aria-label, 'What\'s on your mind')]",
                            "//div[@role='button'][contains(@aria-label, 'Create a post')]",
                            
                            "//div[@data-focusable='true'][@role='button'][contains(@aria-label, 'pensando')]",
                            "//div[@data-focusable='true'][@role='button'][contains(@aria-label, 'post')]",
                            
                            "//div[@role='button'][@tabindex='0'][contains(@aria-label, 'post')]",
                            "//div[@role='button'][@data-focusable='true']",
                            
                            "//textarea[contains(@class, 'text')]",
                            "//textarea[@name='xc_message']", 
                            "//div[@contenteditable='true']",
                            "//textarea[not(contains(@style, 'display: none'))]",
                        ]
                        
                        text_field_found = None
                        for i, xpath in enumerate(text_fields_after_tab):
                            try:
                                log_text_func(f"Tentando localizar campo após Tab (XPath {i+1}): {xpath}\n")
                                elements = driver.find_elements(By.XPATH, xpath)
                                if elements:
                                    for element in elements:
                                        try:
                                            if element.is_displayed() and element.is_enabled():
                                                text_field_found = element
                                                log_text_func(f"Campo após Tab encontrado (XPath {i+1}): {element.tag_name}\n")
                                                break
                                        except:
                                            continue
                                    if text_field_found:
                                        break
                            except Exception as e_xpath:
                                log_text_func(f"Erro XPath {i+1} após Tab: {e_xpath}\n")
                                continue
                        
                        if text_field_found:
                            log_text_func("Campo de texto após Tab localizado. Clicando...\n")
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text_field_found)
                            time.sleep(1)
                            driver.execute_script("arguments[0].click();", text_field_found)
                            log_text_func("Clique realizado no campo após Tab.\n")
                            time.sleep(2)
                        else:
                            log_text_func("Campo de texto após Tab não encontrado. Usando ActionChains diretamente...\n")
                            actions = ActionChains(driver)
                            actions.click().perform()
                            time.sleep(1)
                            
                    except Exception as e_reclick:
                        log_text_func(f"Erro ao clicar no campo após Tab: {e_reclick}\n")
                        try:
                            actions = ActionChains(driver)
                            actions.click().perform()
                            log_text_func("Fallback: clique via ActionChains executado.\n")
                            time.sleep(1)
                        except Exception as e_fallback:
                            log_text_func(f"Erro no fallback após Tab: {e_fallback}\n")
                    
                    log_text_func("Limpando link (mantendo preview)...\n")
                    actions = ActionChains(driver)
                    if sys.platform == 'darwin':
                        actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
                    else:
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    time.sleep(0.5)
                    actions.send_keys(Keys.DELETE).perform()
                    time.sleep(2)
                    
                    # Só digita texto se não estiver vazio
                    if text and text.strip():
                        log_text_func(f"Digitando texto: {text}\n")
                        for char in text:
                            actions.send_keys(char).perform()
                            time.sleep(random.uniform(0.08, 0.15))
                    else:
                        log_text_func("Postagem sem texto (apenas preview do link).\n")
                    
                    log_text_func("Link e conteúdo processados com sucesso! Aguardando 5 segundos antes de procurar botão Publicar...\n")
                    
                    time.sleep(5)

                    log_text_func("Pressionando Tab para carregar preview do link...\n")
                    try:
                        actions = ActionChains(driver)
                        actions.send_keys(Keys.TAB).perform()
                        log_text_func("Tab pressionado para carregar preview.\n")
                    except Exception as e_tab:
                        log_text_func(f"Erro ao pressionar Tab: {e_tab}\n")
                        try:
                            actions = ActionChains(driver)
                            actions.send_keys(Keys.TAB).perform()
                            log_text_func("Tab pressionado novamente (fallback).\n")
                        except Exception as e_tab2:
                            log_text_func(f"Erro no Tab fallback: {e_tab2}\n")
                    
                    log_text_func("Procurando botão Publicar...\n")
                    
                    time.sleep(3)
                    
                    publish_buttons = [
                        "//span[@class='f2' and text()='POSTAR']",
                        "//span[contains(@class, 'f2')][contains(text(), 'POSTAR')]",
                        "//span[text()='POSTAR']",
                        
                        "//div[contains(@class, 'native-text')]/span[text()='POSTAR']",
                        "//div[@dir='auto']/span[text()='POSTAR']",
                        
                        "//div[@role='button'][.//span[text()='POSTAR']]",
                        "//div[@data-focusable='true'][.//span[text()='POSTAR']]",
                        "//div[@tabindex='0'][.//span[text()='POSTAR']]",
                        
                        "//span[contains(@style, 'color:#1763cf')][text()='POSTAR']",
                        "//span[contains(@style, 'color')][text()='POSTAR']",
                        
                        "//span[text()='Publicar']",
                        "//span[text()='ENVIAR']",
                        "//span[contains(@class, 'f2')][contains(text(), 'Publicar')]",
                        
                        "//span[text()='POST']",
                        "//span[text()='Post']",
                        "//span[contains(@class, 'f2')][contains(text(), 'POST')]",
                        
                        "//div[contains(@class, 'bg-s19')][.//span[text()='POSTAR']]",
                        "//div[@data-tti-phase='-1'][.//span[text()='POSTAR']]",
                        
                        "//div[@role='button'][contains(text(), 'POSTAR')]",
                        "//button[contains(text(), 'POSTAR')]",
                        "//div[@data-focusable='true'][contains(text(), 'POSTAR')]",
                        
                        "//span[contains(@class, 'f2')][contains(text(), 'POST') or contains(text(), 'POSTAR')]",
                        "//div[@role='button'][@tabindex='0'][last()]",
                    ]
                    
                    publish_btn = None
                    for i, btn_xpath in enumerate(publish_buttons):
                        try:
                            log_text_func(f"Procurando botão POSTAR (XPath {i+1}): {btn_xpath}\n")
                            elements = driver.find_elements(By.XPATH, btn_xpath)
                            if elements:
                                for element in elements:
                                    try:
                                        if element.is_displayed() and element.is_enabled():
                                            element_text = element.text.upper().strip()
                                            log_text_func(f"Elemento encontrado - Texto: '{element_text}', Tag: {element.tag_name}\n")
                                            
                                            if element.tag_name.lower() == 'span' and 'POSTAR' in element_text:
                                                parent_element = element.find_element(By.XPATH, "./..")
                                                if parent_element and parent_element.is_displayed() and parent_element.is_enabled():
                                                    publish_btn = parent_element
                                                    log_text_func(f"Botão POSTAR encontrado via span (XPath {i+1}): Parent={parent_element.tag_name}\n")
                                                    break
                                                else:
                                                    grandparent = parent_element.find_element(By.XPATH, "./..")
                                                    if grandparent and grandparent.is_displayed():
                                                        publish_btn = grandparent
                                                        log_text_func(f"Botão POSTAR encontrado via span (XPath {i+1}): Grandparent={grandparent.tag_name}\n")
                                                        break
                                            
                                            elif any(keyword in element_text for keyword in ['POSTAR', 'PUBLICAR', 'POST', 'ENVIAR']):
                                                publish_btn = element
                                                log_text_func(f"Botão POSTAR encontrado diretamente (XPath {i+1}): Texto='{element.text}'\n")
                                                break
                                            
                                            elif not element_text and element.get_attribute('role') == 'button':
                                                publish_btn = element
                                                log_text_func(f"Botão sem texto encontrado (XPath {i+1}): Role=button\n")
                                                break
                                                
                                    except Exception as e_btn_check:
                                        log_text_func(f"Erro ao verificar elemento {i+1}: {e_btn_check}\n")
                                        continue
                                        
                                if publish_btn:
                                    break
                        except Exception as e_xpath_btn:
                            log_text_func(f"Erro XPath botão {i+1}: {e_xpath_btn}\n")
                            continue
                    
                    if publish_btn:
                        log_text_func("Clicando no botão POSTAR...\n")
                        try:
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", publish_btn)
                            time.sleep(1)
                            driver.execute_script("arguments[0].click();", publish_btn)
                            log_text_func("Botão POSTAR clicado via JavaScript! Aguardando processamento...\n")
                            time.sleep(random.uniform(15, 20))
                            log_text_func(f"SUCESSO: Postagem concluída para {profile_name}!\n")
                            return True
                        except Exception as e_js_click:
                                                            log_text_func(f"Erro clique JavaScript: {e_js_click}\n")
                        try:
                                publish_btn.click()
                                log_text_func("Botão POSTAR clicado via Selenium! Aguardando processamento...\n")
                                time.sleep(random.uniform(15, 20))
                                log_text_func(f"SUCESSO: Postagem concluída para {profile_name}!\n")
                                return True
                        except Exception as e_selenium_click:
                                log_text_func(f"Erro clique Selenium: {e_selenium_click}\n")
                                
                                # NOVA LÓGICA: Verificar bloqueio apenas quando falha ao clicar no botão publicar
                                log_text_func(f"Falha ao clicar no botão publicar. Verificando se é bloqueio...\n")
                                if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                                    log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                                else:
                                    log_text_func(f"Perfil {profile_name} não está bloqueado, problema no clique do botão.\n")
                    else:
                        log_text_func("ERRO: Botão POSTAR não encontrado após inserir conteúdo.\n")
                        driver.save_screenshot(f"{screenshot_file_base}_no_publish_button.png")
                        
                        # NOVA LÓGICA: Verificar bloqueio apenas quando não encontra botão publicar
                        log_text_func(f"Botão publicar não encontrado. Verificando se é bloqueio...\n")
                        if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                            log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                        else:
                            log_text_func(f"Perfil {profile_name} não está bloqueado, problema na localização do botão.\n")
                        
                        try:
                            all_buttons = driver.find_elements(By.XPATH, "//button | //div[@role='button'] | //input[@type='submit']")
                            log_text_func(f"DEBUG: Encontrados {len(all_buttons)} botões na página:\n")
                            for idx, btn in enumerate(all_buttons[:10]):
                                try:
                                    btn_text = btn.text.strip()
                                    btn_tag = btn.tag_name
                                    is_displayed = btn.is_displayed()
                                    log_text_func(f"  Botão {idx+1}: {btn_tag} - Texto: '{btn_text}' - Visível: {is_displayed}\n")
                                except:
                                    log_text_func(f"  Botão {idx+1}: Erro ao obter informações\n")
                        except Exception as e_debug:
                            log_text_func(f"Erro no debug dos botões: {e_debug}\n")
                        
                except Exception as e_actions:
                    log_text_func(f"Erro ao usar ActionChains: {e_actions}\n")
                    
                    # NOVA LÓGICA: Verificar bloqueio apenas quando há erro nas ações
                    log_text_func(f"Erro nas ações do ActionChains. Verificando se é bloqueio...\n")
                    if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                        log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                    else:
                        log_text_func(f"Perfil {profile_name} não está bloqueado, problema nas ações.\n")
                    
                    try:
                        log_text_func("Tentando inserir conteúdo via JavaScript...\n")
                        js_code = f"""
                            var activeEl = document.activeElement;
                            console.log('Elemento ativo:', activeEl);
                            if (activeEl && (activeEl.tagName === 'TEXTAREA' || activeEl.contentEditable === 'true')) {{
                                if (activeEl.tagName === 'TEXTAREA') {{
                                    activeEl.value = '{link}';
                                    activeEl.dispatchEvent(new Event('input', {{ bubbles: true }}));
                                }} else {{
                                    activeEl.innerText = '{link}';
                                    activeEl.dispatchEvent(new Event('input', {{ bubbles: true }}));
                                }}
                                return 'success';
                            }} else {{
                                return 'no_active_element';
                            }}
                        """
                        result = driver.execute_script(js_code)
                        log_text_func(f"Resultado JavaScript: {result}\n")
                        
                        if result == 'success':
                            time.sleep(15)
                            
                            js_clear_and_text = f"""
                                var activeEl = document.activeElement;
                                if (activeEl) {{
                                    if (activeEl.tagName === 'TEXTAREA') {{
                                        activeEl.value = '{text}';
                                        activeEl.dispatchEvent(new Event('input', {{ bubbles: true }}));
                                    }} else {{
                                        activeEl.innerText = '{text}';
                                        activeEl.dispatchEvent(new Event('input', {{ bubbles: true }}));
                                    }}
                                    return 'text_inserted';
                                }}
                                return 'failed';
                            """
                            
                            if text and text.strip():
                                text_result = driver.execute_script(js_clear_and_text)
                                log_text_func(f"Texto inserido via JavaScript: {text_result}\n")
                            else:
                                log_text_func("Sem texto para inserir via JavaScript.\n")
                        
                    except Exception as e_js:
                        log_text_func(f"Erro JavaScript: {e_js}\n")
                
            except Exception as e_comp_click:
                log_text_func(f"Erro ao clicar no campo composer: {e_comp_click}\n")
                
                # NOVA LÓGICA: Verificar bloqueio apenas quando há erro ao clicar no composer
                log_text_func(f"Erro ao clicar no composer. Verificando se é bloqueio...\n")
                if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                    log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                else:
                    log_text_func(f"Perfil {profile_name} não está bloqueado, problema no clique do composer.\n")
        else:
            log_text_func("Campo composer não encontrado. Tentando método direto...\n")
            
            try:
                log_text_func("Tentando inserir link diretamente via ActionChains...\n")
                actions = ActionChains(driver)
                actions.send_keys(link).perform()
                time.sleep(15)
                
                if sys.platform == 'darwin':
                    actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
                else:
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                time.sleep(0.5)
                actions.send_keys(Keys.DELETE).perform()
                time.sleep(2)
                
                if text and text.strip():
                    for char in text:
                        actions.send_keys(char).perform()
                        time.sleep(0.1)
                else:
                    log_text_func("Método direto: postagem sem texto.\n")
                    
                log_text_func("Conteúdo inserido via método direto.\n")
                
            except Exception as e_direct:
                log_text_func(f"Erro método direto: {e_direct}\n")
                
                # NOVA LÓGICA: Verificar bloqueio apenas quando há erro no método direto
                log_text_func(f"Erro no método direto. Verificando se é bloqueio...\n")
                if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                    log_text_func(f"Perfil {profile_name} está bloqueado.\n")
                else:
                    log_text_func(f"Perfil {profile_name} não está bloqueado, problema no método direto.\n")

        if not any(err_item[0] == profile_id for err_item in erros_lista): 
            erros_lista.append((profile_id, profile_name))
        return False

    except Exception as e_general:
        log_text_func(f"ERRO GERAL ao postar: {e_general}\n")
        traceback.print_exc()
        
        # NOVA LÓGICA: Verificar bloqueio apenas quando há erro geral
        log_text_func(f"Erro geral detectado. Verificando se é bloqueio...\n")
        try:
            if verificar_bloqueio_perfil(driver, profile_id, profile_name, log_text_func):
                log_text_func(f"Perfil {profile_name} está bloqueado.\n")
            else:
                log_text_func(f"Perfil {profile_name} não está bloqueado, erro geral na postagem.\n")
        except Exception as e_verif:
            log_text_func(f"Erro ao verificar bloqueio após erro geral: {e_verif}\n")
        
        try:
            driver.save_screenshot(f"{screenshot_file_base}_general_exception.png")
            log_text_func(f"Screenshot de erro geral salvo: {screenshot_file_base}_general_exception.png\n")
        except:
            pass
        if not any(err_item[0] == profile_id for err_item in erros_lista):
            erros_lista.append((profile_id, profile_name))
        return False
    finally:
        log_text_func("-" * 40 + "\n")
    
    return False

def insert_item_in_treeview_safely(widget_root, tree_view_widget, item_id_val, item_values_tuple):
    if widget_root.winfo_exists() and tree_view_widget.winfo_exists():
        try:
            tree_view_widget.insert("", tk.END, iid=str(item_id_val), values=item_values_tuple)
        except Exception as e:
            print(f"Erro ao inserir item {item_id_val} na TreeView: {e}")

def create_gui():
    root_window = tk.Tk()
    root_window.title("AutoGroups v4.1")

    global total_perfis_var, total_posts_var, posts_realizados_var, tempo_conclusao_var, prox_link_horario_var, perfis_treeview, ordem_postagem_var
    total_perfis_var = tk.StringVar(value="Perfis: 0")
    total_posts_var = tk.StringVar(value="Total Posts: 0")
    posts_realizados_var = tk.StringVar(value="Realizados: 0")
    tempo_conclusao_var = tk.StringVar(value="Tempo: 0s")
    prox_link_horario_var = tk.StringVar(value="Próx. Link: --:--:--")
    ordem_postagem_var = tk.StringVar(value="aleatoria")

    # Tamanho da janela reduzido
    root_window.geometry("400x700")
    root_window.minsize(325, 225)

    log_area_widget = None
    
    def log_text_gui(message):
        nonlocal log_area_widget
        if log_area_widget and log_area_widget.winfo_exists():
            log_area_widget.configure(state='normal')
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_area_widget.insert(tk.END, f"[{timestamp}] {message}")
            log_area_widget.see(tk.END)
            log_area_widget.configure(state='disabled')
            root_window.update_idletasks()

    def limpar_log_action():
        nonlocal log_area_widget
        if log_area_widget and log_area_widget.winfo_exists():
            log_area_widget.configure(state='normal')
            log_area_widget.delete('1.0', tk.END)
            log_area_widget.configure(state='disabled')

    root_window.columnconfigure(0, weight=1)
    root_window.rowconfigure(1, weight=1)

    # Frame para botões principais (sempre visível)
    main_buttons_frame = ttk.Frame(root_window, padding="10")
    main_buttons_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,5))
    main_buttons_frame.columnconfigure(0, weight=1)
    main_buttons_frame.columnconfigure(1, weight=1)

    start_button_widget_ref = ttk.Button(main_buttons_frame, text="▶ Play", style="Accent.TButton")
    start_button_widget_ref.grid(row=0, column=0, sticky="ew", padx=(0,5))

    parar_button_widget_ref = ttk.Button(main_buttons_frame, text="⏹ Parar", state='disabled')
    parar_button_widget_ref.grid(row=0, column=1, sticky="ew", padx=(5,0))

    # Notebook para as abas
    notebook = ttk.Notebook(root_window)
    notebook.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5,10))

    # === ABA 1: CONFIGURAÇÃO ===
    config_frame = ttk.Frame(notebook)
    notebook.add(config_frame, text="Configuração")
    config_frame.columnconfigure(0, weight=1)

    # Grupo IXBrowser
    grupo_frame = ttk.Labelframe(config_frame, text="Grupo IXBrowser", padding="10")
    grupo_frame.grid(row=0, column=0, sticky="ew", pady=(10,10), padx=10)
    grupo_frame.columnconfigure(1, weight=1)

    ttk.Label(grupo_frame, text="Grupo:").grid(row=0, column=0, sticky=tk.W, padx=(0,5))
    grupo_combobox = ttk.Combobox(grupo_frame, width=30, state="readonly")
    grupo_combobox.grid(row=0, column=1, sticky="ew", pady=(0,5))

    refresh_button_widget = ttk.Button(grupo_frame, text="Atualizar")
    refresh_button_widget.grid(row=0, column=2, sticky=tk.E, padx=(5,0), pady=(0,5))

    # Ordem de Postagem
    ordem_frame = ttk.Labelframe(config_frame, text="Ordem de Postagem", padding="10")
    ordem_frame.grid(row=1, column=0, sticky="ew", pady=(0,10), padx=10)
    ttk.Radiobutton(ordem_frame, text="Aleatória", variable=ordem_postagem_var, value="aleatoria").pack(side=tk.LEFT, padx=10)
    ttk.Radiobutton(ordem_frame, text="Sequencial", variable=ordem_postagem_var, value="sequencial").pack(side=tk.LEFT, padx=10)

    # Filtro por Tag
    tag_filter_frame = ttk.Labelframe(config_frame, text="Filtro por Tag", padding="10")
    tag_filter_frame.grid(row=2, column=0, sticky="ew", pady=(0,10), padx=10)
    tag_filter_frame.columnconfigure(1, weight=1)
    ttk.Label(tag_filter_frame, text="Nome da Tag:").grid(row=0, column=0, sticky=tk.W, padx=(0,5))
    tag_filter_entry = ttk.Entry(tag_filter_frame, width=30)
    tag_filter_entry.grid(row=0, column=1, sticky="ew")
    root_window.tag_filter_entry = tag_filter_entry

    # === ABA 2: CONFIGURAÇÕES AVANÇADAS ===
    advanced_frame = ttk.Frame(notebook)
    notebook.add(advanced_frame, text="Configurações Avançadas")
    advanced_frame.columnconfigure(0, weight=1)

    # Conexão e Licença
    conexao_frame = ttk.Labelframe(advanced_frame, text="Conexão e Licença", padding="10")
    conexao_frame.grid(row=0, column=0, sticky="ew", pady=(10,10), padx=10)
    conexao_frame.columnconfigure(1, weight=1)

    ttk.Label(conexao_frame, text="API IXBrowser:").grid(row=0, column=0, sticky=tk.W, pady=2, padx=(0,5))
    api_url_entry = ttk.Entry(conexao_frame, width=35)
    api_url_entry.insert(0, DEFAULT_API_URL)
    api_url_entry.grid(row=0, column=1, sticky="ew", pady=2)
    test_api_button_widget = ttk.Button(conexao_frame, text="Testar")
    test_api_button_widget.grid(row=0, column=2, sticky=tk.E, padx=(5,0), pady=2)

    ttk.Label(conexao_frame, text="E-mail (Licença):").grid(row=1, column=0, sticky=tk.W, pady=2, padx=(0,5))
    email_entry = ttk.Entry(conexao_frame, width=35)
    email_entry.grid(row=1, column=1, sticky="ew", pady=2)
    verificar_button_widget = ttk.Button(conexao_frame, text="Verificar")
    verificar_button_widget.grid(row=1, column=2, sticky=tk.E, padx=(5,0), pady=2)

    # Conteúdo das Postagens
    conteudo_frame = ttk.Labelframe(advanced_frame, text="Conteúdo das Postagens", padding="10")
    conteudo_frame.grid(row=1, column=0, sticky="ew", pady=(0,10), padx=10)
    conteudo_frame.columnconfigure(0, weight=1)

    ttk.Label(conteudo_frame, text="Links (um por linha):").grid(row=0, column=0, sticky=tk.W, pady=(0,2))
    links_text = scrolledtext.ScrolledText(conteudo_frame, width=40, height=4, wrap=tk.WORD)
    links_text.grid(row=1, column=0, sticky="ew", pady=(0,5))

    ttk.Label(conteudo_frame, text="Textos (um por linha, opcional):").grid(row=2, column=0, sticky=tk.W, pady=(0,2))
    textos_text = scrolledtext.ScrolledText(conteudo_frame, width=40, height=4, wrap=tk.WORD)
    textos_text.grid(row=3, column=0, sticky="ew", pady=(0,5))

    # Intervalos
    intervalos_frame = ttk.Labelframe(advanced_frame, text="Intervalos", padding="10")
    intervalos_frame.grid(row=2, column=0, sticky="ew", pady=(0,10), padx=10)
    intervalos_frame.columnconfigure(1, weight=1)
    intervalos_frame.columnconfigure(3, weight=1)

    ttk.Label(intervalos_frame, text="Int. Perfis (s):").grid(row=0,column=0,sticky=tk.W,padx=(0,2),pady=2)
    intervalo_perfis_entry = ttk.Entry(intervalos_frame, width=8)
    intervalo_perfis_entry.insert(0,"45")
    intervalo_perfis_entry.grid(row=0,column=1,sticky=tk.W,padx=(0,10),pady=2)

    ttk.Label(intervalos_frame, text="Int. Links (min):").grid(row=0,column=2,sticky=tk.W,padx=(0,2),pady=2)
    intervalo_links_entry = ttk.Entry(intervalos_frame, width=8)
    intervalo_links_entry.insert(0,"3")
    intervalo_links_entry.grid(row=0,column=3,sticky=tk.W,padx=(0,10),pady=2)

    ttk.Label(intervalos_frame, text="Atraso Inicial (min):").grid(row=1, column=0, sticky=tk.W, padx=(0,2), pady=2)
    atraso_inicial_min_entry = ttk.Entry(intervalos_frame, width=8)
    atraso_inicial_min_entry.insert(0, "0")
    atraso_inicial_min_entry.grid(row=1, column=1, sticky=tk.W, padx=(0,10), pady=2)

    salvar_button_widget_ref = ttk.Button(advanced_frame, text="💾 Salvar Configurações")
    salvar_button_widget_ref.grid(row=3, column=0, sticky="e", pady=10, padx=10)

    # === ABA 3: ESTATÍSTICAS E STATUS ===
    stats_frame = ttk.Frame(notebook)
    notebook.add(stats_frame, text="Estatísticas e Status")
    stats_frame.columnconfigure(0, weight=1)
    stats_frame.rowconfigure(1, weight=1)
    stats_frame.rowconfigure(3, weight=1)

    # Estatísticas
    stats_info_frame = ttk.Labelframe(stats_frame, text="Estatísticas da Sessão", padding="10")
    stats_info_frame.grid(row=0, column=0, sticky="ew", pady=(10,10), padx=10)
    stats_info_frame.columnconfigure(0,weight=1)
    stats_info_frame.columnconfigure(1,weight=1)
    stats_info_frame.columnconfigure(2,weight=1)

    ttk.Label(stats_info_frame, textvariable=total_perfis_var).grid(row=0,column=0,sticky=tk.W,padx=5,pady=2)
    ttk.Label(stats_info_frame, textvariable=total_posts_var).grid(row=0,column=1,sticky=tk.W,padx=5,pady=2)
    ttk.Label(stats_info_frame, textvariable=posts_realizados_var).grid(row=0,column=2,sticky=tk.W,padx=5,pady=2)
    ttk.Label(stats_info_frame, textvariable=tempo_conclusao_var).grid(row=1,column=0,sticky=tk.W,padx=5,pady=2)
    ttk.Label(stats_info_frame, textvariable=prox_link_horario_var).grid(row=1,column=1,columnspan=2,sticky=tk.W,padx=5,pady=2)

    # Status dos Perfis
    perfis_status_frame = ttk.Labelframe(stats_frame, text="Status dos Perfis", padding="10")
    perfis_status_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10), padx=10)
    perfis_status_frame.columnconfigure(0, weight=1)
    perfis_status_frame.rowconfigure(0, weight=1)

    perfis_tree_columns = ("id", "nome", "posts_feitos", "status")
    perfis_treeview = ttk.Treeview(perfis_status_frame, columns=perfis_tree_columns, displaycolumns=("nome", "posts_feitos", "status"), show="headings", height=10)

    perfis_treeview.heading("nome", text="Nome do Perfil")
    perfis_treeview.heading("posts_feitos", text="Posts")
    perfis_treeview.heading("status", text="Status")

    perfis_treeview.column("id", width=0, stretch=tk.NO)
    perfis_treeview.column("nome", width=30, anchor=tk.W)
    perfis_treeview.column("posts_feitos", width=5, anchor=tk.CENTER)
    perfis_treeview.column("status", width=90, anchor=tk.CENTER)

    perfis_tree_scrollbar = ttk.Scrollbar(perfis_status_frame, orient="vertical", command=perfis_treeview.yview)
    perfis_treeview.configure(yscrollcommand=perfis_tree_scrollbar.set)

    perfis_treeview.grid(row=0, column=0, sticky="nsew")
    perfis_tree_scrollbar.grid(row=0, column=1, sticky="ns")

    # Logs
    logs_frame = ttk.Labelframe(stats_frame, text="Logs", padding="10")
    logs_frame.grid(row=2, column=0, sticky="ew", pady=(0,5), padx=10)
    logs_frame.columnconfigure(0, weight=1)

    log_controls_frame = ttk.Frame(logs_frame)
    log_controls_frame.grid(row=0, column=0, sticky="ew", pady=(0,5))
    log_controls_frame.columnconfigure(0, weight=1)
    
    limpar_log_button_widget_ref = ttk.Button(log_controls_frame, text="Limpar Logs", command=limpar_log_action)
    limpar_log_button_widget_ref.pack(side=tk.RIGHT)

    log_area_widget = scrolledtext.ScrolledText(logs_frame, height=8, state='disabled', wrap=tk.WORD, font=("Segoe UI", 9))
    log_area_widget.grid(row=1, column=0, sticky="ew")

    style = ttk.Style(root_window)
    style.configure("Accent.TButton", font="-weight bold -size 11", padding="8 12")

    # GUI Actions and Logic
    group_map_gui_local = {}
    config_loaded_gui_local = {}

    def populate_groups_action_gui(api_url):
        nonlocal group_map_gui_local, config_loaded_gui_local
        if not api_url or not validate_api_url(api_url):
            log_text_gui("API URL inválida.\n")
            grupo_combobox['values'] = []
            grupo_combobox.set("API Inválida")
            return
        groups = get_all_groups(log_text_gui, api_url)
        group_names = []
        group_map_gui_local.clear()
        current_selection = grupo_combobox.get()
        if not groups:
            log_text_gui("Nenhum grupo IXBrowser encontrado.\n")
            grupo_combobox['values'] = []
            grupo_combobox.set("Nenhum grupo")
            return
        for group in groups:
            group_name = group.get('group_name')
            group_id = group.get('group_id')
            if group_name and group_id:
                group_names.append(group_name)
                group_map_gui_local[group_name] = group_id
        grupo_combobox['values'] = sorted(group_names)
        if group_names:
            log_text_gui(f"Grupos atualizados: {len(group_names)}.\n")
            if current_selection in group_names:
                grupo_combobox.set(current_selection)
            elif config_loaded_gui_local.get("grupo") in group_names:
                grupo_combobox.set(config_loaded_gui_local.get("grupo"))
            else:
                grupo_combobox.current(0)
        else:
            grupo_combobox.set("Nenhum grupo")

    refresh_button_widget.configure(command=lambda: populate_groups_action_gui(api_url_entry.get().strip()))

    def test_api_action_gui_wrapper(api_url_param):
        if not api_url_param:
            log_text_gui("Erro: Insira API URL.\n")
            messagebox.showerror("Erro", "Insira API URL.")
            return
        log_text_gui(f"Testando API em {api_url_param}...\n")
        success, message = test_api_connection(api_url_param, log_text_gui)
        if success:
            messagebox.showinfo("Sucesso", message)
            populate_groups_action_gui(api_url_param)
        else:
            messagebox.showerror("Erro Conexão", message)
    
    test_api_button_widget.configure(command=lambda: test_api_action_gui_wrapper(api_url_entry.get().strip()))

    def verificar_email_e_salvar_action_gui():
        email = email_entry.get().strip()
        if not email:
            log_text_gui("Erro: Insira e-mail.\n")
            messagebox.showerror("Erro", "Insira seu e-mail.")
            return
        log_text_gui(f"Verificando licença para {email}...\n")
        if verificar_licenca(email, log_text_gui):
            messagebox.showinfo("Licença OK", f"Licença para {email} ativa.")
            salvar_action_gui()
        else:
            messagebox.showerror("Licença Inválida", f"Licença para {email} inválida/expirada.")
    
    verificar_button_widget.configure(command=verificar_email_e_salvar_action_gui)

    def salvar_action_gui():
        email=email_entry.get().strip()
        grupo=grupo_combobox.get()
        links=links_text.get("1.0",tk.END).strip()
        textos=textos_text.get("1.0",tk.END).strip()
        ip_str=intervalo_perfis_entry.get().strip()
        il_str=intervalo_links_entry.get().strip()
        au_str=api_url_entry.get().strip()
        atraso_inicial_min_str = atraso_inicial_min_entry.get().strip()
        try:
            int(ip_str); int(il_str)
            val_atraso = int(atraso_inicial_min_str)
            if val_atraso < 0: raise ValueError("Atraso não pode ser negativo")
        except ValueError:
            messagebox.showerror("Erro","Intervalos e Atraso Inicial devem ser números inteiros válidos.")
            return
        if not validate_api_url(au_str):
            messagebox.showerror("Erro","API URL inválida.")
            return
        if salvar_configuracoes(email,grupo,links,textos,ip_str,il_str,au_str, atraso_inicial_min_str):
            log_text_gui("Config salva!\n")
        else:
            messagebox.showerror("Erro","Não foi possível salvar.")
    
    salvar_button_widget_ref.configure(command=salvar_action_gui)

    def update_profile_in_treeview(root_widget, profile_id_to_update, values_tuple_all_cols):
        global perfis_treeview
        if perfis_treeview and root_widget.winfo_exists():
            try:
                item_id = str(profile_id_to_update)
                if perfis_treeview.exists(item_id):
                    perfis_treeview.item(item_id, values=values_tuple_all_cols)
            except Exception as e_tree_update:
                log_text_gui(f"Erro ao atualizar Treeview para perfil {profile_id_to_update}: {e_tree_update}\n")

    def run_posting_logic_thread(root_widget_param, email, grupo_id, grupo_nome, links, textos, api_url, intervalo_entre_perfis_segundos, intervalo_entre_links_minutos, atraso_inicial_minutos):
        global stop_posting, start_time_posting_global, posts_realizados_count_global, perfis_treeview, prox_link_horario_var
        
        intervalo_entre_links_segundos_calc = intervalo_entre_links_minutos * 60
        
        if atraso_inicial_minutos > 0:
            log_text_gui(f"Atraso inicial de {atraso_inicial_minutos} minuto(s) iniciado.\n")
            for i in range(atraso_inicial_minutos * 60, 0, -1):
                if stop_posting:
                    log_text_gui("Atraso interrompido.\n")
                    return
                min_restantes, seg_restantes = divmod(i, 60)
                tempo_formatado_restante = f"{min_restantes:02d}:{seg_restantes:02d}"
                if root_widget_param.winfo_exists() and prox_link_horario_var:
                    root_widget_param.after(0, lambda tf=tempo_formatado_restante: prox_link_horario_var.set(f"Atraso: {tf}"))
                if i % 10 == 0 or i < 10:
                    log_text_gui(f"Aguardando início... {tempo_formatado_restante}\n")
                time.sleep(1)
            log_text_gui("Atraso inicial concluído.\n")

        if perfis_treeview and root_widget_param.winfo_exists(): 
            root_widget_param.after(0, lambda: [perfis_treeview.delete(i) for i in perfis_treeview.get_children()])

        try:
            log_text_gui("Verificando licença...\n")
            if not verificar_licenca(email, log_text_gui): 
                log_text_gui("Licença inválida.\n")
                messagebox.showerror("Erro Licença", "Licença inválida.")
                return 

            log_text_gui(f"Buscando perfis grupo '{grupo_nome}'...\n")
            perfis_grupos_com_nomes_original = ler_perfis_grupos(grupo_id, log_text_gui, api_url)

            tag_para_filtrar = root_widget_param.tag_filter_entry.get().strip()
            perfis_grupos_com_nomes = [] 

            if not perfis_grupos_com_nomes_original:
                 log_text_gui("Nenhum perfil com URL válida encontrado.\n")
                 perfis_grupos_com_nomes = [] 
            elif tag_para_filtrar:
                log_text_gui(f"Filtrando perfis pela Tag: '{tag_para_filtrar}'...\n")
                for perfil_info in perfis_grupos_com_nomes_original:
                    if len(perfil_info) > 3 and perfil_info[3] and tag_para_filtrar.lower() in perfil_info[3].lower():
                        perfis_grupos_com_nomes.append(perfil_info)
            else:
                perfis_grupos_com_nomes = list(perfis_grupos_com_nomes_original)

            if not perfis_grupos_com_nomes: 
                if tag_para_filtrar and perfis_grupos_com_nomes_original:
                    messagebox.showerror("Erro", f"Nenhum perfil com a Tag '{tag_para_filtrar}' encontrado.")
                else:
                    messagebox.showerror("Erro", "Nenhum perfil com URL válida encontrado.")
                return 

            if not links:
                messagebox.showerror("Erro", "Nenhum link para postar.")
                return

            total_posts_por_perfil = len(links)
            
            if perfis_treeview and root_widget_param.winfo_exists():
                for perfil_data_init in perfis_grupos_com_nomes:
                    p_id_iter_init = perfil_data_init[0] 
                    p_name_iter_init = perfil_data_init[2] 
                    initial_values = (str(p_id_iter_init), p_name_iter_init, f"0 de {total_posts_por_perfil}", "Aguardando")
                    root_widget_param.after(0, lambda p_id_val=p_id_iter_init, vals=initial_values: insert_item_in_treeview_safely(root_widget_param, perfis_treeview, p_id_val, vals))
            
            total_posts_tentados = 0
            total_posts_sucesso = 0
            erros_lista = [] 
            num_perfis = len(perfis_grupos_com_nomes)
            num_links_total = len(links)
            total_calc = num_perfis * num_links_total 
            
            if total_perfis_var and root_widget_param.winfo_exists(): 
                root_widget_param.after(0, lambda: total_perfis_var.set(f"Perfis: {num_perfis}"))
            if total_posts_var and root_widget_param.winfo_exists(): 
                root_widget_param.after(0, lambda: total_posts_var.set(f"Total Posts: {total_calc}"))

            posts_feitos_por_perfil = {p_info[0]: 0 for p_info in perfis_grupos_com_nomes}
            
            if stop_posting: 
                log_text_gui("Interrompido antes de iniciar.\n")
                return
            
            log_text_gui(f"\n=== INICIANDO POSTAGENS ===\n")
            for link_idx, link in enumerate(links):
                if stop_posting: 
                    log_text_gui("Interrompido.\n")
                    break 
                
                log_text_gui(f"\n-- Link {link_idx+1}/{num_links_total}: {link} --\n")
                ordem_selecionada = ordem_postagem_var.get() 
                
                perfis_a_iterar = [] 
                if ordem_selecionada == "aleatoria":
                    perfis_a_iterar = random.sample(perfis_grupos_com_nomes, len(perfis_grupos_com_nomes))
                else:
                    perfis_a_iterar = list(perfis_grupos_com_nomes) 

                for perfil_idx_na_ordem, perfil_data in enumerate(perfis_a_iterar):
                    profile_id = perfil_data[0]
                    group_url = perfil_data[1]
                    profile_name = perfil_data[2]

                    if stop_posting: 
                        log_text_gui("Interrompido (perfil).\n")
                        break 
                    
                    posts_feitos_count_antes = posts_feitos_por_perfil.get(profile_id,0)
                    posts_feitos_display_antes = f"{posts_feitos_count_antes} de {total_posts_por_perfil}"

                    if root_widget_param.winfo_exists():
                        values_processando = (str(profile_id), profile_name, posts_feitos_display_antes, "Processando...")
                        root_widget_param.after(0, update_profile_in_treeview, root_widget_param, profile_id, values_processando)
                    
                    log_text_gui(f"\n- Link {link_idx+1}, Perfil {perfil_idx_na_ordem+1}/{num_perfis} (ID: {profile_id}, Nome: {profile_name}) -\n")
                    driver = None
                    profile_ok = True  # ALTERAÇÃO: Agora assume que o perfil está OK por padrão
                    status_interno = "Processando..." 
                    
                    try:
                        driver_path, debugger_address = open_ixbrowser_profile(profile_id, log_text_gui, api_url)
                        if driver_path and debugger_address:
                            driver = create_driver(driver_path, debugger_address, log_text_gui)
                            if driver:
                                # ALTERAÇÃO: Removida a verificação de bloqueio inicial
                                # A verificação agora só ocorre quando há erros durante a postagem
                                
                                if profile_ok:
                                    total_posts_tentados += 1
                                    if textos and any(t.strip() for t in textos):  # Se há textos não vazios
                                        text_escolhido = random.choice([t for t in textos if t.strip()])  # Escolhe apenas textos não vazios
                                        log_text_gui(f"Texto: {text_escolhido[:50]}...\n")
                                    else:
                                        text_escolhido = ""  # Texto vazio se não há textos configurados
                                        log_text_gui("Postagem sem texto (apenas link).\n")
                                    
                                    success = post_to_facebook_group_mobile(driver, group_url, link, text_escolhido, WAIT_TIME_SECONDS, profile_id, profile_name, erros_lista, log_text_gui)
                                    if success: 
                                        total_posts_sucesso += 1
                                        posts_realizados_count_global += 1
                                        posts_feitos_por_perfil[profile_id] += 1
                                        status_interno = "Postado" 
                                    else:
                                        status_interno = "Erro Postagem"

                                    if posts_realizados_var and root_widget_param.winfo_exists(): 
                                        root_widget_param.after(0, lambda: posts_realizados_var.set(f"Realizados: {posts_realizados_count_global}"))
                            else: 
                                log_text_gui(f"ERRO: WebDriver não criado.\n")
                                if not any(err[0] == profile_id for err in erros_lista): 
                                    erros_lista.append((profile_id, profile_name))
                                status_interno = "Erro WebDriver"
                        else: 
                             log_text_gui(f"ERRO: Falha ao abrir perfil.\n")
                             if not any(err[0] == profile_id for err in erros_lista): 
                                 erros_lista.append((profile_id, profile_name)) 
                             status_interno = "Erro API IXB"
                    except Exception as e_loop:
                         log_text_gui(f"ERRO loop perfil: {e_loop}\n")
                         if not any(err[0] == profile_id for err in erros_lista): 
                             erros_lista.append((profile_id, profile_name))
                         status_interno = "Erro Inesperado"
                    finally:
                        if driver:
                            try:
                                driver.quit()
                            except Exception as e_quit:
                                log_text_gui(f"Erro fechar WebDriver: {e_quit}\n")
                        if profile_id:
                            close_ixbrowser_profile(profile_id, log_text_gui, api_url)

                        current_posts_final_count = posts_feitos_por_perfil.get(profile_id, 0)
                        posts_feitos_display_final = f"{current_posts_final_count} de {total_posts_por_perfil}"
                        status_final = status_interno 

                        if stop_posting:
                            status_final = "Interrompido"
                        elif current_posts_final_count >= total_posts_por_perfil and status_interno == "Postado":
                            status_final = "Concluído"
                        elif status_interno == "Postado": 
                            status_final = "Aguardando Próx. Link"
                            
                        final_values = (str(profile_id), profile_name, posts_feitos_display_final, status_final)
                        if root_widget_param.winfo_exists():
                            root_widget_param.after(0, update_profile_in_treeview, root_widget_param, profile_id, final_values)
                            if tempo_conclusao_var:
                                t_decorrido = time.time()-start_time_posting_global
                                root_widget_param.after(0, lambda t=t_decorrido: tempo_conclusao_var.set(f"Tempo: {format_time(t)}"))

                        if perfil_idx_na_ordem < num_perfis - 1 and not stop_posting:
                            delay_proximo_perfil = random.uniform(intervalo_entre_perfis_segundos*0.8, intervalo_entre_perfis_segundos*1.2) 
                            log_text_gui(f"Aguardando ~{delay_proximo_perfil:.1f}s...\n")
                            time.sleep(delay_proximo_perfil)
                        elif link_idx < num_links_total - 1 and not stop_posting: 
                            delay_proximo_link = random.uniform(intervalo_entre_links_segundos_calc*0.8, intervalo_entre_links_segundos_calc*1.2)
                            log_text_gui(f"Aguardando próximo link ~{delay_proximo_link:.1f}s...\n")
                            horario_prox_link = (datetime.now() + timedelta(seconds=delay_proximo_link)).strftime('%H:%M:%S')
                            if prox_link_horario_var and root_widget_param.winfo_exists():
                                root_widget_param.after(0, lambda h=horario_prox_link: prox_link_horario_var.set(f"Próx. Link: ~{h}"))
                            time.sleep(delay_proximo_link)

            log_text_gui(f"\n{'='*15} RESUMO FINAL {'='*15}\n")
            log_text_gui(f"Posts TENTADOS: {total_posts_tentados}\nPosts SUCESSO: {total_posts_sucesso}\n")
            
            if erros_lista:
                nomes_unicos = sorted(list(set([item[1] for item in erros_lista])))
                log_text_gui(f"Perfis com ERRO ({len(nomes_unicos)}): {', '.join(nomes_unicos)}\n")
                try:
                    perfis_ja_logados = set()
                    if os.path.exists(LOG_ERROS_FILE):
                        with open(LOG_ERROS_FILE, 'r', encoding='utf-8') as f_read:
                            for line in f_read: 
                                perfis_ja_logados.add(line.strip())
                    novos_perfis = [nome for nome in nomes_unicos if nome not in perfis_ja_logados]
                    if novos_perfis:
                        with open(LOG_ERROS_FILE, 'a', encoding='utf-8') as f_append:
                            for nome_perfil in novos_perfis:
                                f_append.write(f"{nome_perfil}\n") 
                        log_text_gui(f"{len(novos_perfis)} novo(s) perfil(s) com erro adicionado(s).\n")
                except Exception as e_log_file:
                    log_text_gui(f"Erro ao salvar log: {e_log_file}\n")
            else:
                 log_text_gui("Nenhum erro registrado.\n")

        except Exception as e_main: 
            log_text_gui(f"ERRO CRÍTICO: {e_main}\n")
            if prox_link_horario_var and root_widget_param.winfo_exists():
                 root_widget_param.after(0, lambda: prox_link_horario_var.set("Próx. Link: Erro"))
        finally:
            def update_ui_after():
                 if root_widget_param.winfo_exists(): 
                     if start_button_widget_ref: start_button_widget_ref.configure(state='normal')
                     if verificar_button_widget: verificar_button_widget.configure(state='normal')
                     if salvar_button_widget_ref: salvar_button_widget_ref.configure(state='normal')
                     if test_api_button_widget: test_api_button_widget.configure(state='normal')
                     if refresh_button_widget: refresh_button_widget.configure(state='normal')
                     if limpar_log_button_widget_ref: limpar_log_button_widget_ref.configure(state='normal')
                     if parar_button_widget_ref: parar_button_widget_ref.configure(state='disabled')
                     if tempo_conclusao_var: 
                         t_final = time.time()-start_time_posting_global
                         tempo_conclusao_var.set(f"Tempo Total: {format_time(t_final)}")
                     log_text_gui("Interface reabilitada.\n")
            if root_widget_param.winfo_exists(): 
                root_widget_param.after(0, update_ui_after)

    def start_posting_action_gui(root_arg):
        nonlocal start_button_widget_ref, parar_button_widget_ref, group_map_gui_local
        global stop_posting, start_time_posting_global, posts_realizados_count_global, perfis_treeview, prox_link_horario_var
        
        stop_posting=False
        start_time_posting_global=time.time()
        posts_realizados_count_global=0

        # Reset GUI stats
        if total_perfis_var: total_perfis_var.set("Perfis: 0")
        if total_posts_var: total_posts_var.set("Total Posts: 0")
        if posts_realizados_var: posts_realizados_var.set(f"Realizados: {posts_realizados_count_global}")
        if tempo_conclusao_var: tempo_conclusao_var.set("Tempo: 0s")
        if prox_link_horario_var: prox_link_horario_var.set("Próx. Link: --:--:--")
        if perfis_treeview:
            for i in perfis_treeview.get_children():
                perfis_treeview.delete(i)

        log_text_gui("--- Validando Entradas ---\n")
        email=email_entry.get().strip()
        grupo_nome=grupo_combobox.get()
        links_str=links_text.get("1.0",tk.END).strip()
        textos_str=textos_text.get("1.0",tk.END).strip()
        api_url=api_url_entry.get().strip()
        
        # Validations
        if not email:
            log_text_gui("ERRO: E-mail vazio.\n")
            messagebox.showerror("Erro","Insira e-mail.")
            return
        if not validate_api_url(api_url):
            log_text_gui(f"ERRO: API URL inválida.\n")
            messagebox.showerror("Erro",f"API URL inválida.")
            return
        if not grupo_nome or grupo_nome in ["Nenhum grupo encontrado", "API Inválida"]:
            log_text_gui("ERRO: Grupo não selecionado.\n")
            messagebox.showerror("Erro","Selecione grupo.")
            return
            
        grupo_id=group_map_gui_local.get(grupo_nome)
        if not grupo_id:
            log_text_gui(f"Erro: ID grupo não encontrado.\n")
            messagebox.showerror("Erro",f"ID para '{grupo_nome}' não encontrado.")
            return
            
        links=[l for l in links_str.split('\n') if l.strip()]
        textos=[t for t in textos_str.split('\n') if t.strip()]
        
        if not links:
            log_text_gui("ERRO: Nenhum link.\n")
            messagebox.showerror("Erro","Insira link.")
            return
        
        if not textos:
            log_text_gui("AVISO: Nenhum texto configurado. Postagens serão feitas apenas com link.\n")
            textos = [""]  # Lista com string vazia para permitir postagem sem texto
            
        try:
            ip=int(intervalo_perfis_entry.get().strip())
            il=int(intervalo_links_entry.get().strip())
            atraso_val = int(atraso_inicial_min_entry.get().strip())
            if ip<0 or il<0 or atraso_val < 0:
                raise ValueError("Valores não podem ser negativos")
        except ValueError:
            log_text_gui("Erro: Intervalos/Atraso inválidos.\n")
            messagebox.showerror("Erro","Intervalos devem ser números inteiros não negativos.")
            return

        # Disable UI elements during posting
        if start_button_widget_ref: start_button_widget_ref.configure(state="disabled")
        if verificar_button_widget: verificar_button_widget.configure(state="disabled")
        if salvar_button_widget_ref: salvar_button_widget_ref.configure(state="disabled")
        if test_api_button_widget: test_api_button_widget.configure(state="disabled")
        if refresh_button_widget: refresh_button_widget.configure(state="disabled")
        if limpar_log_button_widget_ref: limpar_log_button_widget_ref.configure(state="disabled")
        if parar_button_widget_ref: parar_button_widget_ref.configure(state="normal")

        log_text_gui("--- Iniciando postagem ---\n")
        threading.Thread(target=run_posting_logic_thread, args=(root_arg, email, grupo_id, grupo_nome, links, textos, api_url, ip, il, atraso_val), daemon=True).start()

    start_button_widget_ref.configure(command=lambda: start_posting_action_gui(root_window))

    def stop_posting_action_gui_local():
        nonlocal parar_button_widget_ref
        global stop_posting, prox_link_horario_var
        if not stop_posting:
            stop_posting=True
            log_text_gui("!!! PARADA SOLICITADA !!!\n")
            if prox_link_horario_var and not any(x in prox_link_horario_var.get() for x in ["Concluído", "Sem Links", "N/A"]):
                if root_window.winfo_exists():
                    root_window.after(0, lambda: prox_link_horario_var.set("Próx. Link: Interrompendo..."))
        if parar_button_widget_ref:
            parar_button_widget_ref.configure(state='disabled')

    parar_button_widget_ref.configure(command=stop_posting_action_gui_local)

    # Load configurations on startup
    log_text_gui("Carregando config.json...\n")
    config_loaded_gui_local = carregar_configuracoes()
    if config_loaded_gui_local:
        email_entry.insert(0, config_loaded_gui_local.get("email",""))
        api_url_entry.delete(0, tk.END)
        api_url_entry.insert(0, config_loaded_gui_local.get("api_url", DEFAULT_API_URL))
        atraso_inicial_min_entry.delete(0, tk.END)
        atraso_inicial_min_entry.insert(0, config_loaded_gui_local.get("atraso_inicial_min", "0"))
        links_text.insert("1.0", config_loaded_gui_local.get("links",""))
        textos_text.insert("1.0", config_loaded_gui_local.get("textos",""))
        intervalo_perfis_entry.delete(0, tk.END)
        intervalo_perfis_entry.insert(0, config_loaded_gui_local.get("intervalo_perfis","45"))
        intervalo_links_entry.delete(0, tk.END)
        intervalo_links_entry.insert(0, config_loaded_gui_local.get("intervalo_links","3"))
        log_text_gui("Configurações carregadas.\n")
    else: 
        log_text_gui("Nenhum config.json. Usando padrões.\n")

    # Populate groups on startup and start main GUI loop
    initial_api_url=api_url_entry.get().strip()
    log_text_gui("Buscando grupos IXBrowser...\n")
    populate_groups_action_gui(initial_api_url)
    log_text_gui("Interface pronta.\n")
    root_window.mainloop()

if __name__ == "__main__":
    try: 
        create_gui()
    except Exception as main_e:
         print(f"ERRO FATAL AO INICIAR: {main_e}")
         traceback.print_exc()
         try:
             root_error_popup = tk.Tk()
             root_error_popup.withdraw()
             messagebox.showerror("Erro Crítico", f"Não foi possível iniciar a aplicação:\n\n{main_e}")
             root_error_popup.destroy()
         except:
             pass