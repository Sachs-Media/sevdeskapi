from unittest import TestCase
from sevdeskapi.models.contact import Contact


class ContactTestCase(TestCase):

    def test_simplecontact(self):

        c = Contact(familyName="famvalue",
                    sureName="surname",
                    title="title",
                    description="description",
                    gender="m")

        self.assertEqual(c.get_dict(), {'familyname': 'famvalue', 'surename': 'surname', 'titel': 'title', 'description': 'description', 'gender': 'm'})

        c = Contact(familyName="famvalue",
                    sureName="surname",
                    title="title",
                    description="description",
                    gender="m",
                    anotherarg="foo")

        self.assertEqual(c.get_dict(), {'familyname': 'famvalue', 'surename': 'surname', 'titel': 'title', 'description': 'description', 'gender': 'm'})


    def test_nested(self):
        c = Contact(familyName="famvalue",
                    sureName="surname",
                    title="title",
                    description="description",
                    gender="m",
                    **{"category[id]": 234})
        self.assertTrue(hasattr(c, "category"))
        self.assertEqual(c.category.id, 234)
        self.assertDictEqual(c.get_dict(), {'familyname': 'famvalue', 'surename': 'surname', 'titel': 'title', 'description': 'description', 'gender': 'm', 'category[id]': 234})

