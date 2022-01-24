# Created by jankub at 01/18/2022
# page url: https://the-internet.herokuapp.com/add_remove_elements/

Feature: Add Element button

    Scenario: Add Element button is loaded
        Given Add Element page url
        When page loaded
        Then button Add Element can be located on page


    Scenario Outline: Delete button adding
        Given Add Element page loaded
        When Add Element button clicked <number> of times
        Then <number> Delete buttons added
            Examples:
            |number|
            |1     |
            |10    |
            |99    |
