# ciaca
aulas do curso para jovens aprendizes

## Configurando o EC2

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
   - Custom TCP (8501) - de sua IP (para Streamlit)

### Passo 3: Iniciar Instância
1. Vá em EC2 → Launch Instance
2. Selecione uma AMI (Ubuntu 22.04 LTS)
3. Selecione um tipo (t3.medium ou t3.small)
4. Configure:
   - Key pair: ciaca-key
   - Security group: ciaca-sg
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
http://SEU_PUBLIC_IP:8501
```

## Configurando DNS (Opcional)

Se você tem um domínio:
1. Vá em Route 53 (AWS)
2. Crie um registro A apontando para o IP público
3. Configure um certificado SSL (AWS Certificate Manager)
4. Atualize o docker-compose.yml para usar HTTPS
