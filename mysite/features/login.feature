Feature: Login ke sistem

  Scenario: Berhasil login
    Given Saya berada di halaman login
    When Saya mengisi kolom "username" dan "password" dengan benar
    And Saya klik tombol "Sign In"
    And Saya dialihkan ke dashboard

  Scenario: Login dengan kredensial yang salah
    Given Saya berada di halaman login
    When Saya mengisi kolom "username" dan/atau "password" dengan salah
    And Saya klik tombol "Sign In"
    Then Saya melihat pop-up "Invalid email or password"
    And Saya tetap berada di halaman login
