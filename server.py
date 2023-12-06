from flask import Flask, jsonify, request
from main import *
from flasgger import Swagger
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
swagger = Swagger(app)
@app.route("/get_items/", methods = ["GET"])
def get_items():
    """
    Получить информацию о всех книгах
    ---
    responses:
      200:
        description: A list of items.
        examples:
          data:
            - title: Example Title
              author: Example Author
              genre: Example Genre
              created_at: 2022-12-06
    """
    items = get_item()
    return jsonify({'data': items})

@app.route("/create_item/", methods = ["POST"])
def create_item_rq():
    """
    Добавление новой книги в таблицу
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ItemPydantic'
    responses:
      200:
        description: Item created successfully.
    definitions:
      ItemPydantic:
        type: object
        properties:
          title:
            type: string
          author:
            type: string
          genre:
            type: string
          created_at:
            type: string
        required:
          - title
          - author
          - genre
        example:
          title: "Title"
          author: "Author"
          genre: "Genre"
          created_at: "2022-12-15"
    """
    data = request.get_json()
    item = ItemPydentic(
        title = data.get('title', 'no title'),
        author = data.get('author', 'no author'),
        genre = data.get('genre', 'no genre'),
        created_at = data.get('created_at', date.today().strftime('%Y-%m-%d'))
    )
    create_item(item)
    return jsonify({'message':'created successfully'})


@app.route("/retrive_item/<int:item_id>/", methods = ["GET"])
def get_one_item(item_id):
    """
    Получить одну книгу по ID
    ---
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
    responses:
      200:
        description: Data of the specified item.
      404:
        description: Item not found.
    """
    item = retrieve_item(item_id)
    if not item:
        return jsonify({'message':'Not found'})
    return jsonify({'data': item})

@app.route("/update_item/<int:item_id>/", methods = ["PUT"])
def update(item_id):
    """
    Полностью обновить информацию о книге по ID
    ---
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ItemPydantic'
          examples:
          data:
            - title: Example Title
              author: Example Author
              genre: Example Genre
              created_at: 2022-12-06
    responses:
      200:
        description: Item updated successfully.
      404:
        description: Item not found.
        examples:
    definitions:
      ItemPydantic:
        type: object
        properties:
          title:
            type: string
          author:
            type: string
          genre:
            type: string
          created_at:
            type: string
        required:
          - title
          - author
          - genre
        example:
          title: "New Title"
          author: "New Author"
          genre: "New Genre"
          created_at: "2022-12-15"
    """
    data = request.get_json()
    ret_item = retrieve_item(item_id)
    if ret_item is None:
        return jsonify({'message':'Not found'}), 404
    
    item = ItemPydentic(
        title = data.get('title', 'no title'),
        author = data.get('author', 'no author'),
        genre = data.get('genre', 'no genre'),
        created_at = data.get('created_at', date.today().strftime('%Y-%m-%d'))
    )
    update_item(item_id, item)
    return jsonify({'message': 'Updated successfully'})
    
    

@app.route("/delete_item/<int:item_id>/", methods = ["DELETE"])
def delete(item_id):
    """
    Удалить книгу по ID
    ---
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
    responses:
      200:
        description: Item deleted successfully.
      404:
        description: Item not found.
    """
    del_item = retrieve_item(item_id)
    if del_item is None:
        return jsonify({"message":"Not found"}),404
    delete_item(item_id)
    return jsonify({"message":"deleted successfully"})

app.run(host='localhost', port = 8000)
# app.run(host='127.0.0.1', port=8000)