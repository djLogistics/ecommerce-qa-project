# Test Cases

## E-Commerce Application Test Cases

| Test Case ID | Scenario              | Steps                                                                 | Expected Result                                      |
|--------------|----------------------|----------------------------------------------------------------------|------------------------------------------------------|
| TC-01        | Valid Login          | Navigate to site → Enter valid credentials → Click login             | User is redirected to the products page              |
| TC-02        | Invalid Password     | Enter valid username → Enter wrong password → Click login            | Error message is displayed                           |
| TC-03        | Empty Fields         | Leave fields blank → Click login                                     | Error message is displayed                           |
| TC-04        | Add Item to Cart     | Login → Click "Add to Cart" on a product                             | Item is added and cart icon updates                  |
| TC-05        | Remove Item from Cart| Add item → Go to cart → Click "Remove"                               | Item is removed from cart                            |
| TC-06        | Checkout Process     | Add item → Go to cart → Checkout → Enter info → Complete order       | Order confirmation page is displayed                 |
| TC-07        | End-to-End Flow      | Login → Add item → Go to cart → Verify item                          | User completes core shopping workflow successfully   |