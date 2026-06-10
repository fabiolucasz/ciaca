# CIACA - Cursos para Jovens Aprendizes

![Python](https://img.shields.io/badge/Python-3.9+-3776ab?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazon-aws&logoColor=white)

## 📋 Descrição

Plataforma educacional para cursos de jovens aprendizes, desenvolvida com Streamlit e dockerizada para fácil deploy na AWS.

## 🎯 Características

- Interface web moderna e responsiva
- Deploy automatizado com Docker
- Hospedagem em EC2 da AWS
- Escalável e fácil de manter

## 🚀 Quick Start

### Requisitos
- Docker e Docker Compose instalados
- Conta AWS (para deploy em produção)

### Executar Localmente
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/ciaca.git
cd ciaca

# Iniciar com Docker
docker compose up -d

# Acessar em http://localhost:80
```

## 📦 Deploy na AWS EC2

### Passo 1: Criar Key Pair
1. Acesse o console da AWS
2. Vá em EC2 → Key Pairs
3. Clique em "Create key pair"
4. Nomeie como `ciaca-key`
5. Baixe o arquivo `.pem`

### Passo 2: Configurar Security Group
1. Vá em EC2 → Security Groups
2. Clique em "Create security group"
3. Nome: `ciaca-sg`
4. Adicione as regras:
   - SSH (22) - de sua IP
   - HTTP (80) - de qualquer lugar
   - HTTPS (443) - de qualquer lugar

### Passo 3: Iniciar Instância
1. Vá em EC2 → Launch Instance
2. Selecione uma AMI (Ubuntu 22.04 LTS)
3. Selecione um tipo (t3.medium ou t3.small)
4. Configure:
   - Key pair: `ciaca-key`
   - Security group: `ciaca-sg`
5. Inicie a instância

### Passo 4: Conectar via SSH
```bash
chmod 400 ciaca-key.pem
ssh -i "ciaca-key.pem" ubuntu@SEU_PUBLIC_IP
```

### Passo 5: Configurar Docker
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Docker
sudo apt install docker.io -y

# Adicionar usuário ao grupo docker
sudo usermod -aG docker ubuntu

# Instalar Docker Compose
sudo apt install docker-compose -y

# Sair e reconectar para aplicar mudanças
exit
ssh -i "ciaca-key.pem" ubuntu@SEU_PUBLIC_IP
```

### Passo 6: Deploy da Aplicação
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/ciaca.git
cd ciaca

# Construir e iniciar
docker compose up -d

# Ver logs
docker compose logs -f
```

### Passo 7: Acessar a Aplicação
Abra seu navegador e acesse:
```
http://SEU_PUBLIC_IP
```

## 🔐 Configurando DNS (Opcional)

Se você tem um domínio:
1. Vá em Route 53 (AWS)
2. Crie um registro A apontando para o IP público
3. Configure um certificado SSL (AWS Certificate Manager)
4. Atualize o docker-compose.yml para usar HTTPS

## 📚 Tecnologias Utilizadas

- **Python 3.9+** - Linguagem de programação
- **Streamlit** - Framework web para aplicações de dados
- **Docker** - Containerização
- **Docker Compose** - Orquestração de containers
- **AWS EC2** - Hospedagem em nuvem

## 📝 Licença

MIT License

## 👤 Autor

**Fabio Lucas**

---

**Desenvolvido com ❤️ para educação**
