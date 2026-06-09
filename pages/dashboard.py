
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import Controllers.LoginController as LoginController



Path("aulas").mkdir(parents=True, exist_ok=True)



data = LoginController.loadall()
if data:
    names = data[0]
    users = data[1]
    passwords = data[2]


credentials = {
    "usernames": {
        users[i]: {
            "email": "",
            "name": names[i],
            "password": passwords[i]
        } for i in range(len(users))
    }
}


authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name='some_cookie_name',
    cookie_key='some_key',
    cookie_expiry_days=30
)


authenticator.login()

if st.session_state.get('authentication_status'):
    authenticator.logout('Logout', 'sidebar')

    try:
        
        #Filtros
        st.sidebar.header("Filtros")


    except FileNotFoundError:
        st.info("Nenhum arquivo de dados encontrado. Faça upload de um PDF para começar.")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}") 

elif st.session_state.get('authentication_status') is None:
    st.warning("Faça o login para continuar")