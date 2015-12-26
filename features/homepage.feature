Feature: Registering a tester

Background:
Given I am on Home Page

Scenario:  Assert Home Screen Title
    When I open the home screen
    Then I must see the page title "Classe de Testes | Testes e Qualidade de Software"

Scenario:  Assert Header Title
    When I click on sub menu item "CURSO SELENIUM"
    Then I must see the header title "Curso Selenium"
