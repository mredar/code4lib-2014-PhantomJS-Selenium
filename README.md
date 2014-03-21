**PhantomJS+Selenium: Easy Automated Testing of AJAX-y UIs**

Code4lib 2014 presentation on testing web UI by [Martin Haye](http://github.com/martinhaye) and [Mark Redar](http://github.com/mredar).

Web user interfaces are demanding ever-more dynamism and polish, combining HTML5, AJAX, lots of CSS and jQuery (or ilk) to create autocomplete drop-downs, intelligent buttons, stylish alert dialogs, etc. How can you make automated tests for these highly complex and interactive UIs?

Part of the answer is PhantomJS. It’s a modern WebKit browser that’s "headless" (meaning it has no display) that can be driven from command-line Selenium unit tests. PhantomJS is dead simple to install, and its blazing speed and server-friendliness make continuous integration testing easy. You can write UI unit tests in {language-of-your-choice} and run them not just in PhantomJS but in Firefox and Chrome, plus a zillion browser/OS combinations at places like SauceLabs, TestingBot and BrowserStack.

In this double-team live code talk, we’ll explain all that while we demonstrate the following in real time:

* Start with nothing.

* Install Selenium bindings for Ruby and Python.

* In each language write a small test of an AJAX-y UI.

* Run the tests in Firefox, and fix bugs (in the test or UI) as needed.

* Install PhantomJS.

* Show the same tests running headless as part of a server-friendly test suite.

* (Wifi permitting) Show the same tests running on a couple different browser/OS combinations on the server cloud at SauceLabs – talking through a tunnel to the local firewalled application.

Detailed plan:

* Martin needs to translate this doc to Markdown


* Mark prep before talk:

    * <s>Put our little test page on a "Github page", including these notes.</s>

    * <s>Get rid of old venv, set up new venv: `"\Users\mark\Desktop\Program Files\Python2.7\Scripts\virtualenv" venv-selenium`</s>

    * <s>Download Selenium IDE</s>
    
    * Uninstall Selenium IDE
    
    * Download selenium python package
    
    * Get pip install to use local file

* Martin prep before talk: 

    * See if we can get two mics

    * Turn off wifi

    * uninstall selenium Ruby bindings:
`sudo gem uninstall selenium-webdriver`

    * Uninstall PhantomJS:
`rm ~/bin/phantomjs`
`rm –r ~/Downloads/phantomjs-1.9.7-macosx
`

    * Start Python server: `python -m SimpleHTTPServer`

* 2 min – Martin talks intro, Mark installs software: Selenium, plus Selenium IDE

    * Start sample app in Python from index.html directory:
         python -m SimpleHTTPServer 8000

    * Open sample app, locally:
         http://localhost:8000/](http://localhost:8000)
   
    * talk about being able to test the text response being returned but not the javascript interaction

    * Start Firefox, go to [http://www.seleniumhq.org/download/](http://www.seleniumhq.org/download/) to show people. But install from local file, then restart Firefox.


* 5 min – Show the little test app, write a test using Selenium IDE, run in Firefox, translate to Python, make it actually test something useful.

    * Start recording in Selenium IDE

    * First thing you do is hit Submit, which puts up Validation stuff.

    * Fill out form, demo the validation, stop recording.

    * Export test case as Python -> unittest webdriver

    * Also export test case as Ruby -> unit::test
    
    * Run code, see fail due to lack of virtualenv
    
    * make venv, pip install local selenium
    
    * Review code. 

        * Change self.baseURL to ""

        * Run test – it should work!
[need command here] python selenium-webdriver-test.py (something like that)

         * but didn't test (*assert*) anything
         * add this before click - should fail `self.assertTrue(driver.find_element_by_css_selector("small.error").is_displayed())`

    * Show the test failing first

    * Fix failure

    * Add after the first click a check for validation:

        * `self.assertEqual(driver.find_element_by_css_selector("small.error").text, "Passwords must be at least 8 characters with 1 capital letter, 1 number, and one special character.")`

        * [research how you’d get the second element, in case somebody asks… some kind of css selector?]

        * [Try this with assertIn instead]

    * Before click, insert this:

        * `self.assertFalse(driver.find_element_by_css_selector("small.error").is_displayed())`

    * After click, insert this:
    `self.assertTrue(driver.find_element_by_css_selector("small.error").is_displayed())`
    
    * Run again, show success


* 5 min – Take that test, show in Python and Ruby. Make a change, demonstrate running in PhantomJS.

    * Make the same test run in Ruby

        * Install ruby gem for selenium-webdriver:
`sudo gem install --local ~/Downloads/selenium-webdriver-2.40.0.gem --no-rdoc --no-ri`

        * In the exported selenium test, change `${receiver}` to `@driver` (the ide has a bug).

        * Run and watch Firefox go through it's paces

        * Add code to check for errors before and after click. Like: `assert_true @driver.find_element(:css, "small.error").displayed?`

    * Install PhantomJS:

        * `cd ~/Downloads`

        * `unzip phantomjs-1.9.7-macosx.zip`

        * `mv phantomjs-1.9.7-macosx/bin/phantomjs ~/bin`

        * `hash –r`

        * `phantomjs --version`

    * Change `@driver` line in setup method: `firefox` -> `phantomjs` (ruby), `Firefox` -> `PhantomJS` (Python)

    * Run test

    * Much quicker! No display! Scriptable! Run it on a server machine! A command-line regression suite, etc.


* 5 min: Demo Sauce Connect

    * [https://saucelabs.com/docs/connect](https://saucelabs.com/docs/connect)

    * Run sc.exe -u cdl-dsc -k <cdl-dsc-key>

    * Run test "selenium-webdriver-sauce-connect-test.py"

    * View results

    * TODO: test code with status updated....

    * [Mark will have this all set up in advance, show users the things he configured, then demo the app kicking off locally, running on Sauce, the cool video produced]

    * [Mark will include out how to update Sauce status at end of test]

