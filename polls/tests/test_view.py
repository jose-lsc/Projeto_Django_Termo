from django.test import TestCase
from django.urls import reverse
from polls.models import Palavra, PalavraDia, Usuario
from polls.views import sortear_palavra, palavra_do_dia, termo
from django.contrib.auth.models import User

class QuestionIndexViewTests(TestCase):

    def setUp(self):
        Palavra.objects.create(conteudo= 'teste')
        self.user = User.objects.create_user(username='jo', password='jojo')
        self.client.login(username="jo", password="jojo")
        
    def test_existe_word_list(self):
        resposta = self.client.get(reverse("word_list"))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "polls/word_list.html")


    def test_existe_lobby(self):
        resposta = self.client.get(reverse("lobby"))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, "polls/Lobby.html")
 

    def test_sortear_palavra_e_string(self):
        palavra = sortear_palavra()
        self.assertIsInstance(palavra, str)

    def test_ver_se_existe_palavra_do_dia(self):
        palavra = palavra_do_dia()
        self.assertIsInstance(palavra, str)

    def test_ver_se_usuario_é_criado(self):
        usuario= self.client.post(reverse('termo'))
        self.assertTemplateUsed(usuario, "polls/Jogo.html")
        usuario_criado = Usuario.objects.get(user=self.user)
        self.assertIsNotNone(usuario_criado)

    def test_ver_se_a_palavra_esta_certa(self):
        resposta_certa = {"resposta": "teste"}
        usuario= self.client.post(reverse('termo'), resposta_certa)
        self.assertIn("acertou", usuario.context)
        self.assertTrue(usuario.context["acertou"])