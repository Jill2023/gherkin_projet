from behave import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from features.variables import url, timer, username, password, NomSite, NomTitre, NomTags

txt_username = "username"
txt_password = "password"
btn_login_id = "//button[text()='Connexion']"
lnk_Site = "HEADER_SITES_MENU_text"
lnk_creer_site = "HEADER_SITES_MENU_CREATE_SITE_text"
txt_NomSite = "//input[@name='title']"
btn_public = "CREATE_SITE_FIELD_VISIBILITY_CONTROL_OPTION0_BUTTON"
btn_creer_site = "//span[text()='Créer']"
img_configution = "//img[@class='alf-configure-icon alfresco-menus-AlfMenuBarPopup__icon alfresco-menus-AlfMenuItemIconMixin']"
personnaliser_site = "//a[@title='Personnaliser le site']"
image_wiki = "//img[@src='/share/res/components/images/page-wiki-page-64.png']"
lnk_target = "//div[@class='page-list-wrapper current-pages theme-border-3']"
btn_OK = "//button[text()='OK']"
lnk_wiki = "//a[text()='Wiki']"
btn_nouvelle_page = "//button[text()='Nouvelle page']"
txt_titre = "pageTitle"
txt_tags = "template_x002e_createform_x002e_wiki-create_x0023_default-tag-input-field"
btn_ajouter = "//button[text()='Ajouter']"
btn_enregistrer = "//button[text()='Enregistrer']"
lnk_list_page = "//a[text()='Liste des pages du wiki']"
btn_tag1 = "//div[@id='template_x002e_tags_x002e_wiki']//a[text()='"
btn_tag2 = "']"
lnk_supprimer = "//td[text()='Supprimer le site']"
lnk_OK = "//span[text()='OK']"
lnk_corbeille = "//a[@href='user-trashcan']"
txt_supprimer1 = "//div[text()='"
txt_supprimer2 = "']/ancestor::tr//button[text()='Supprimer']"
button_delete_ok = "//button[text()='OK']"

@given('se connecter avec un compte')
def seconnecter(context):
    context.driver = webdriver.Chrome((ChromeDriverManager().install()))
    context.driver.get(url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.NAME, txt_username).
    time.sleep(2)
    context.driver.find_element(By.NAME, txt_password).send_keys(anyting)
    time.sleep(2)
    context.driver.find_element(By.XPATH, btn_login_id).click()
    time.sleep(4)

@when('creer un site')
def creer_site(context):
    context.driver.find_element(By.ID, lnk_Site).click()
    time.sleep(4)
    context.driver.find(By.ID, lnk_creer_site).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, txt_NomSite).send_keys(NomSite)
    time.sleep(4)
    context.driver.find_element(By.ID, btn_public).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_creer_site).click()
    time.sleep(4)
    context.driver.refresh()
    context.driver.find_element(By.XPATH, img_configution).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, personnaliser_site).click()
    time.sleep(4)
     context.drive.refresh()                                 


@when('creer les pages wiki avec tag')
def creer_page(context):
    context.driver.find_element(By.XPATH, image_wiki).click()
    time.sleep(4)
    source = context.driver.find_element(By.XPATH, image_wiki)
    target = context.driver.find_element(By.XPATH, lnk_target)
    action = ActionChains(context.driver)
    action.drag_and_drop(source, target).perform()
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_OK).click()
    time.sleep(6)
    context.driver.find_element(By.XPATH, lnk_wiki).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_nouvelle_page).click()
    time.sleep(4)
    context.driver.find_element(By.NAME, txt_titre).send_keys(NomTitre)
    time.sleep(4)
    context.driver.find_element(By.ID, txt_tags).send_keys(NomTags)
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_ajouter).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_enregistrer).click()
    time.sleep(4)

@then('filtrer les pages wiki par tag')
def filtrer_page(context):
    context.driver.find_element(By.XPATH, lnk_list_page).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, btn_tag1 + NomTags + btn_tag2).click()
    time.sleep(4)

@then('supprimer le site')
def supprimer_site(context):
    context.driver.get(url + "site/" + NomSite + "/dashboard")
    context.driver.find_element(By.XPATH, img_configution).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, lnk_supprimer).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, lnk_OK ).click()
    time.sleep(4)
    context.driver.get(url+"user/" + username + "/user-trashcan")
    time.sleep(4)
    context.driver.find_element(By.XPATH, txt_supprimer1 + NomSite +txt_supprimer2).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, button_delete_ok).click()
    time.sleep(4)

@then('deconnecter')
def deconnecter(context):
    context.driver.quit()

