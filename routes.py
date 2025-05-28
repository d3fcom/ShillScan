from flask import render_template, jsonify, request
from app import app
from utils import get_tokens, get_token_by_symbol, generate_mock_data, get_updated_tokens, update_token_data
import logging

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tokens')
def api_tokens():
    try:
        search_query = request.args.get('search', '')
        tokens = get_tokens(search_query)
        return jsonify([token.to_dict() for token in tokens])
    except Exception as e:
        logger.error(f"Error in api_tokens: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/token/<symbol>')
def api_token(symbol):
    try:
        token = get_token_by_symbol(symbol)
        if token:
            return jsonify(token.to_dict())
        return jsonify({'error': 'Token not found'}), 404
    except Exception as e:
        logger.error(f"Error in api_token: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/token/<symbol>')
def token_detail(symbol):
    try:
        token = get_token_by_symbol(symbol)
        if token:
            return render_template('token_detail.html', token=token)
        return render_template('404.html'), 404
    except Exception as e:
        logger.error(f"Error in token_detail: {str(e)}")
        return render_template('500.html'), 500

@app.route('/generate-mock-data')
def generate_data():
    try:
        generate_mock_data()
        return jsonify({'message': 'Mock data generated successfully'})
    except Exception as e:
        logger.error(f"Error in generate_data: {str(e)}")
        return jsonify({'error': 'Failed to generate mock data'}), 500

@app.route('/api/tokens/update')
def update_tokens():
    try:
        update_token_data()
        updated_tokens = get_updated_tokens()
        return jsonify(updated_tokens)
    except Exception as e:
        logger.error(f"Error in update_tokens: {str(e)}")
        return jsonify({'error': 'Failed to update tokens'}), 500
