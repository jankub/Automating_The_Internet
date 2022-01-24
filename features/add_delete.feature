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

    Scenario Outline: Delete button action
        Given Add Element page loaded and <number> of delete buttons visible
        When Any delete button clicked <number_click> of times
        Then <number_rem> of delete buttons remains
            Examples:
            |number|number_click|number_rem|
            |10    |10          |0         |
            |10    |8           |2         |
