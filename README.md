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

* (Wifi permitting) Show the same tests running on a couple different browser/OS combinations on the server cloud at SauceLabs -- talking through a tunnel to the local firewalled application.

Detailed plan:

* Mark prep before talk:

    * <s>Put our little test page on a "Github page", including these notes.</s>

    * <s>Get rid of old venv, set up new venv: `"\Users\mark\Desktop\Program Files\Python2.7\Scripts\virtualenv" venv-selenium`</s>

    * <s>Download Selenium IDE</s>
    
    * Uninstall Selenium IDE
    
    * <s>Download selenium python package</s>
    
    * <s>Get pip install to use local file</s> - pip install <local file path>
    
    * <s>Put raw Python test case, and modified Python test case into the git repo.</s>

    * <s>get sauce IE test code ready and check into repository</s>

    * Immediately before talk:
        * run sauce connnect in terminal
        * terminal at github root ready to run python -m SimpleHTTPServer
        * In Firefox, open localhost:8000, seleniumhq, saucelabs home
        * terminal in Desktop\code4lib ready to run the test files with set SAUCE_USER & set SAUCE_KEY ready.
        * have gvim open to sauce labs test

    * So need 3 terminals and 3 webpages open

* Martin prep before talk: 

    * Make a page of links that we can show at end of talk

    * Resolve merge diffs and push this stuff to github

    * Immediately before talk:

        * Open phantomjs web page in Chrome

        * uninstall selenium Ruby bindings:
    `sudo gem uninstall selenium-webdriver` [need different way in Windows]

        * Reset the test directory - remove phantomjs.exe, test ruby and python
          files.

        * Make sure both mics are on.


* 2 min - Martin talks intro, Mark installs software: Selenium, plus Selenium IDE

    * Start sample app in Python from index.html directory:
         python -m SimpleHTTPServer 8000

    * Open sample app, locally:
         http://localhost:8000/](http://localhost:8000)
   
    * talk about being able to test the text response being returned but not the javascript interaction

    * Start Firefox, go to [http://www.seleniumhq.org/download/](http://www.seleniumhq.org/download/) to show people. But install from local file, then restart Firefox.


* 5 min - Mark - Show the little test app, write a test using Selenium IDE, run in Firefox, translate to Python, make it actually test something useful.

    * Start recording in Selenium IDE

    * First thing you do is hit Submit, which puts up Validation stuff.

    * Fill out form, demo the validation, stop recording.

    * Export test case as Python -> unittest webdriver

    * Also export test case as Ruby -> unit::test
    
    * Run code, see fail due to lack of virtualenv
    
    * make venv, pip install local selenium
    
    * Review code. 

        * Run test - it should work!
[need command here] python selenium-webdriver-test.py (something like that)

         * but didn't test (*assert*) anything
         * add this before click - should fail `self.assertTrue(driver.find_element_by_css_selector("small.error").is_displayed())`

    * Show the test failing first

    * Fix failure

    * [research how you’d get the second element, in case somebody asks -- some kind of css selector?]


* 5 min - Martin - Take that test, show in Ruby. Make a change, demonstrate running in PhantomJS.

    * Make the same test run in Ruby

        * Install ruby gem for selenium-webdriver:
`gem install --local selenium-webdriver-2.40.0.gem --no-rdoc --no-ri`

        * In the exported selenium test, change `${receiver}` to `@driver` (the ide has a bug).

        * Run and watch Firefox go through it's paces

        * Add code to check for errors before and after click. Like: `assert_true @driver.find_element(:css, "small.error").displayed?`

    * Install PhantomJS:

        * `cd code4lib-talk` (if necessary)

        * `.\phantomjs-1.9.7-windows.zip`

        * extract all

        * `copy phantomjs-1.9.7-windows\phantomjs-1.9.7-windows\phantomjs.exe .`

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

