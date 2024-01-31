from userregistration import User
import pytest

@pytest.fixture
def user():
    return User('Deepak', 'Chandu', 'deepak@gmail.com', '91 9087765432', 'Abcd@1234')

class TestUser:

    def test_first_name_success(self, user):
        assert user.first_name == 'Deepak'

    def test_first_name_success2(self, user):
        user.first_name ='Josh'
        assert user.first_name == 'Josh'

    def test_first_name_success3(self, user):
        user.first_name ='YASH'
        assert user.first_name == 'YASH'

    def test_first_name_success4(self, user):
        user.first_name = 'DeE'
        assert user.first_name == 'DeE'

    def test_first_name_fail(self, user):
        user.first_name = 'deepak'
        assert isinstance(user.first_name, ValueError)

    def test_first_name_fail2(self, user):
        user.first_name = 'jOsh'
        assert isinstance(user.first_name, ValueError)

    def test_first_name_fail3(self, user):
        user.first_name = 'Ya'
        assert isinstance(user.first_name, ValueError)

    def test_first_name_fail4(self, user):
        user.first_name = 'Efg12G'
        assert isinstance(user.first_name, ValueError)

    def test_first_name_fail5(self, user):
        user.first_name = 'Ed'
        assert isinstance(user.first_name, ValueError)
    
    def test_last_name_success(self,user):
        assert user.last_name=='Chandu'
    
    def test_last_name_fail(self,user):
        user.last_name='Ch'
        assert isinstance(user.last_name, ValueError)
    
    def test_email_success(self,user):
        assert user.email=='deepak@gmail.com'

    def test_email2_success(self,user):
        user.email='abc@yahoo.com'
        assert user.email=='abc@yahoo.com'
    
    def test_email3_success(self,user):
        user.email='abc-100@yahoo.com'
        assert user.email=='abc-100@yahoo.com'

    def test_email4_success(self,user):
        user.email='abc.100@yahoo.com'
        assert user.email=='abc.100@yahoo.com'

    def test_email5_success(self,user):
        user.email='abc111@abc.com'
        assert user.email=='abc111@abc.com'

    def test_email6_success(self,user):
        user.email='abc@gmail.com.com'
        assert user.email=='abc@gmail.com.com'

    def test_email7_success(self,user):
        user.email='abc+100@gmail.com'
        assert user.email=='abc+100@gmail.com'
    
    def test_email_fail(self,user):
        user.email="abcgmail.com"
        assert isinstance(user.email, ValueError)
    
    def test_email2_fail(self,user):
        user.email="abc"
        assert isinstance(user.email, ValueError)
    
    def test_email3_fail(self,user):
        user.email="abc123@.com"
        assert isinstance(user.email, ValueError)

    def test_email_fail4(self,user):
        user.email="abc123@.com.com"
        assert isinstance(user.email, ValueError)

    def test_email_fail5(self,user):
        user.email="abc@gmail.a"
        assert isinstance(user.email, ValueError)

    def test_email_fail6(self,user):
        user.email=".abc@abc.com"
        assert isinstance(user.email, ValueError)

    def test_email_fail7(self,user):
        user.email=".abc123@gmail.a"
        assert isinstance(user.email, ValueError)
    
    def test_phno_success(self,user):
        assert user.phno=='91 9087765432'

    def test_phno2_success(self,user):
         user.phno="42 7997799689"
         assert user.phno=="42 7997799689"
    
    def test_phno3_success(self,user):
         user.phno="100 7997799645"
         assert user.phno=="100 7997799645"

    def test_phno4_success(self,user):
        user.phno="10 1234567890"
        assert user.phno=="10 1234567890"

    def test_phno_fail(self,user):
         user.phno="4234 7997799689"
         assert isinstance(user.phno, ValueError)
    
    def test_phno2_fail(self,user):
         user.phno="100 997799645"
         assert isinstance(user.phno, ValueError)

    def test_phno3_fail(self,user):
        user.phno="10 34567890"
        assert isinstance(user.phno, ValueError)