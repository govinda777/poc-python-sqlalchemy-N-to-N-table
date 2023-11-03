import unittest
from unittest.mock import patch, Mock
from src.database import Database  # Import the Database class from your module

class TestDatabase(unittest.TestCase):

    @patch('sqlalchemy.create_engine')
    @patch('sqlalchemy.orm.sessionmaker')
    def test_database_initialization(self, MockSessionMaker, MockCreateEngine):
        # Mock the create_engine function to return a mock engine
        mock_engine = Mock()
        MockCreateEngine.return_value = mock_engine

        # Create an instance of the Database class
        db = Database()

        # Assert that create_engine was called with the correct URL
        MockCreateEngine.assert_called_once_with(Database.DATABASE_URL)

        # Assert that sessionmaker was called with the correct bind argument
        MockSessionMaker.assert_called_once_with(bind=mock_engine)

    @patch('sqlalchemy.orm.sessionmaker')
    def test_get_session(self, MockSessionMaker):
        # Mock the session methods
        mock_session = Mock()
        MockSessionMaker.return_value = mock_session

        db = Database()

        # Call the get_session method
        with db.get_session() as session:
            self.assertEqual(session, mock_session)

        # Ensure the session's close method was called
        mock_session.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
