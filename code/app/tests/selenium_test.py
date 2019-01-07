import unittest, os, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/")

    # navbar link tests
    def test_nav_thesis_link(self):
        ths = self.driver.find_element_by_id("thesis")
        ths.send_keys(Keys.RETURN)
        self.assertIn("thesis", self.driver.current_url)

    def test_nav_github_link(self):
        srcode = self.driver.find_element_by_id("sourcecode")
        srcode.send_keys(Keys.RETURN)
        self.assertIn("github", self.driver.current_url)

    def test_nav_mu_link(self):
        mui = self.driver.find_element_by_id("mu")
        mui.send_keys(Keys.RETURN)
        self.assertIn("computer-science", self.driver.current_url)

    def test_nav_brand_link(self):
        mui = self.driver.find_element_by_class_name("navbar-brand")
        mui.send_keys(Keys.RETURN)
        self.assertIn("localhost", self.driver.current_url)

    # upload page
    # dropzone number of files accepted tests
    def test_accepting_one_image(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/kite.jpeg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url

    def test_accepting_multiple_images(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/kite.jpeg\n/Users/deirdre/Desktop/cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" not in self.driver.current_url

    # image type tests
    def test_accepting_jpeg(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/kite.jpeg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url   

    def test_accepting_jpeg_u(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/kite2.JPEG")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url 

    def test_accepting_jpg(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("Users/deirdre/Desktop/cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url  

    def test_accepting_jpg_u(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("Users/deirdre/Desktop/cat2.JPG")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url 

    def test_accepting_png(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("Users/deirdre/Desktop/cat.png")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url  

    def test_accepting_png_u(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("Users/deirdre/Desktop/cat.PNG")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        assert "results" in self.driver.current_url 

    # div link tests
    def test_div_thesis_link(self):
        ths = self.driver.find_element_by_id("thesis2")
        ths.send_keys(Keys.RETURN)
        self.assertIn("thesis", self.driver.current_url)

    def test_div_github_link(self):
        srcode = self.driver.find_element_by_id("sourcecode2")
        srcode.send_keys(Keys.RETURN)
        self.assertIn("github", self.driver.current_url)

    def test_div_mu_link(self):
        mui = self.driver.find_element_by_id("mu2")
        mui.send_keys(Keys.RETURN)
        self.assertIn("computer-science", self.driver.current_url)   

    # results page
    def test_result_text(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/kite.jpeg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        parent = self.driver.find_element_by_id("reslist")
        child = parent.find_element_by_tag_name("li")
        self.assertIn("kite",child.text)

    def test_result_text_multiple(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/dog-cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        parent = self.driver.find_element_by_id("reslist")
        child = parent.find_elements_by_tag_name("li")
        self.assertIn("dog",child[0].text)
        self.assertIn("cat",child[1].text)

    # audio tag tests   
    def test_result_amount_audio_tags(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/dog-cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        li_tags = self.driver.find_element_by_id("reslist").find_elements_by_tag_name("li")
        audio_tags = self.driver.find_elements_by_tag_name("audio")
        self.assertEqual(len(li_tags),len(audio_tags))

    def test_result_pan_value_audio_tags(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/dog-cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        audio_tags = self.driver.find_elements_by_tag_name("audio")
        source_tags = []
        for x in audio_tags:
            xs = 0.0
            try:
                xs = float(x.find_element_by_tag_name("source").get_attribute("class"))
            except ValueError:
                xs = False
            self.assertTrue(isinstance( xs, float))
    
    def test_result_src_audio_tags(self):
        self.driver.find_element_by_id("myDropzone").click()
        self.driver.find_element_by_css_selector('input[type=file]').send_keys("/Users/deirdre/Desktop/dog-cat.jpg")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "resultrow")))
        audio_tags = self.driver.find_elements_by_tag_name("audio")
        source_tags = []
        for x in audio_tags:
            r = requests.head(x.find_element_by_tag_name("source").get_attribute("src"))
            self.assertEqual( 200, r.status_code )
  

    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()
