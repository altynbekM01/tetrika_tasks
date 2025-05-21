import pytest
from unittest.mock import patch, Mock
from task_2.solution import parse_letter_counts

HTML_PAGE = '''
<div class="mw-category-generated">
  <div id="mw-pages">
    <div class="mw-content-ltr">
      <div class="mw-category mw-category-columns">
        <div class="mw-category-group">
          <h3>А</h3>
          <ul>
            <li>Акула</li>
            <li>Антилопа</li>
          </ul>
        </div>
        <div class="mw-category-group">
          <h3>Б</h3>
          <ul>
            <li>Бобер</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
'''

@pytest.fixture
def mocked_response():
    mock = Mock()
    mock.status_code = 200
    mock.text = HTML_PAGE
    return mock

@patch("task_2.solution.requests.get")
def test_parse_letter_counts_single_page(mock_get, mocked_response):
    mock_get.return_value = mocked_response
    result = parse_letter_counts()
    assert result == {'А': 2, 'Б': 1}
