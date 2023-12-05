from flask import Flask, request, jsonify


app = Flask(__name__)

#данные для постов и пользователей
posts = [
    {"id": 1, "title": "First post", "text": "Grozny"},
    {"id": 2, "title": "Second post", "text": "Gudurmes"},
    {"id": 3, "title": "Third post", "text": "Argun"},
    {"id": 4, "title": "Fourth post", "text": "Kurchaloy"},
    {"id": 5, "title": "Fifth post", "text": "Shali"},
    {"id": 6, "title": "Sixth post", "text": "Urus_Martan"},
]

users = [
    {"id": 1, "name": "Client 1"},
    {"id": 2, "name": "Client 2"},
    {"id": 3, "name": "Client 3"},
    {"id": 4, "name": "Client 4"},
    {"id": 5, "name": "Client 5"},
    {"id": 6, "name": "Client 6"},
]


# Роут для получения всех постов
@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    return jsonify({"посты": posts})


# Роут для получения всех пользователей
@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify({"клиенты": users})


# Рокт для получени поста по его идентификатору
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
     # Поиск поста с заданным идентификатором
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        # Если пост не найден, возвращаем ошибку
        return jsonify({"успешно": "Пост не найден"}), 404
    return jsonify({"пост": post})


# Роут для создания нового поста
@app.route('/api/posts', methods=['POST'])
def create_post():
    new_post = {
        "id": len(posts) + 1,
        "title": request.json.get('title', ''),
        "text": request.json.get('text', '')
    }
    # Создаем новый пост
    posts.append(new_post)
    return jsonify({"успешно": "Пост создан", "пост": new_post}), 201


#Роут для редактирования существующего поста
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
     # Поиск поста по идентификатору
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:

        # Если пост не найден, возвращаем ошибку
        return jsonify({"ошибка": "Пост не найден"}), 404
    
    # Редактирование данных поста
    post['title'] = request.json.get('title', post['title'])
    post['text'] = request.json.get('text', post['text'])
    return jsonify({"успешно": "Пост изменен", "пост": post})


# Роут для удаления поста
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    # Поиск поста по идентификатору
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
         # Если пост не найден, возвращаем ошибку
        return jsonify({"ошибка": "Пост не найден"}), 404
    # Удаление поста из списка
    posts.remove(post)
    return jsonify({"успешно": "Пост удален"})

if __name__ == '__main__':
    app.run(debug=True)
