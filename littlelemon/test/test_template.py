from django.test import TestCase
from restaurant.forms import BookingForm

# Create your tests here.
class BookingFormTest(TestCase) :
    def test_render_field(self) :
        form = BookingForm()
        rendered_form = form.as_p()
        self.assertInHTML('<label for="id_name">Name:</label>', rendered_form)
        self.assertInHTML('<input type="text" name="name" maxlength="255" required="" id="id_name">', rendered_form)
        self.assertInHTML('<label for="id_guest_number">Guest number:</label>', rendered_form)
        self.assertInHTML('<input type="number" name="guest_number" required="" id="id_guest_number">', rendered_form)
        self.assertInHTML('<label for="id_date_of_reservation">Date of reservation:</label>', rendered_form)
        self.assertInHTML('<input type="text" name="date_of_reservation" required="" id="id_date_of_reservation">', rendered_form)
        self.assertInHTML('<label for="id_comment">Comment:</label>', rendered_form)
        self.assertInHTML('<textarea name="comment" cols="40" rows="10" id="id_comment"></textarea>', rendered_form)