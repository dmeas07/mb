from django.test import SimpleTestCase


class SimplePageTest(SimpleTestCase)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_pages_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_homet_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_home_about_uses_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(respnose.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(respnose.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
    
