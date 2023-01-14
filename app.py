from flask import Flask, render_template, request
import mysqlite
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    # read index.html file
    return render_template('index.html')


@app.route("/create-user", methods=['GET'])
def create_user_view():
    # read index.html file
    return render_template('create-user.html')


@app.route("/create-user", methods=['POST'])
def do_create_user():
    signup_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO Customers"
    sql += "(`name`, `id`, `phone`, `address`, `age`, `occupation`, `signup_date`, `status`)"
    sql += " VALUES ("
    sql += f'"{request.form["name"]}",'
    sql += f'"{request.form["id"]}",'
    sql += f'"{request.form["phone"]}",'
    sql += f'"{request.form["address"]}",'
    sql += f'"{request.form["age"]}",'
    sql += f'"{request.form["occupation"]}",'
    sql += f'"{signup_date}",'
    # sql += f'"{request.form["photo"]}",'
    sql += f'"{request.form["status"]}"'
    sql += ")"

    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)
    return {"status": "success"}


@app.route("/delete-user", methods=['GET'])
def delete_user_view():
    return render_template('delete-user.html')


@app.route("/delete-user", methods=['POST'])
def do_delete_user():
    # update set status = 0
    sql = "UPDATE Customers SET status = 0 WHERE id = "
    sql += f'"{request.form["id"]}"'
    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)

    return {"status": "success"}


@app.route("/update-user", methods=['GET'])
def update_user_view():
    return render_template('update-user.html')


@app.route("/update-user", methods=['POST'])
def do_update_user():
    sql = "UPDATE Customers SET "
    sql += f'name = "{request.form["name"]}",'
    sql += f'phone = "{request.form["phone"]}",'
    sql += f'address = "{request.form["address"]}",'
    sql += f'age = "{request.form["age"]}",'
    sql += f'occupation = "{request.form["occupation"]}"'
    sql += f' WHERE id = "{request.form["id"]}"'

    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)

    return {"status": "success"}


@app.route("/search-user", methods=['GET'])
def get_user_view():
    return render_template('search-user.html')


@app.route("/search-user", methods=['POST'])
def do_get_user():
    sql = "SELECT * FROM Customers WHERE id = "
    sql += f'"{request.form["id"]}"'
    conn = mysqlite.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    data = {
        "name": result[0],
        "id": result[1],
        "phone": result[2],
        "address": result[3],
        "age": result[4],
        "occupation": result[5],
        "signup_date": result[6],
        "status": result[7]
    }

    # show the result in the html page
    return render_template('search-user.html', data=data)


@app.route("/create-order", methods=['GET'])
def create_order_view():
    return render_template('create-order.html')


@app.route("/create-order", methods=['POST'])
def do_create_order():
    total_price = int(request.form["quantity"]) * \
        int(request.form["unit_price"])
    sql = "INSERT INTO Orders"
    sql += "(`customer_id`, `order_date`, `expected_delivery_date`, `actual_delivery_date`, `item_name`, `unit`, `quantity`, `unit_price`, `total_price`, `supplier_name`, `supplier_id`)"
    sql += " VALUES ("
    sql += f'"{request.form["customer_id"]}",'
    sql += f'"{request.form["order_date"]}",'
    sql += f'"{request.form["expected_delivery_date"]}",'
    sql += f'"{request.form["actual_delivery_date"]}",'
    sql += f'"{request.form["item_name"]}",'
    sql += f'"{request.form["unit"]}",'
    sql += f'"{request.form["quantity"]}",'
    sql += f'"{request.form["unit_price"]}",'
    sql += f'"{total_price}",'
    sql += f'"{request.form["supplier_name"]}",'
    sql += f'"{request.form["supplier_id"]}"'
    sql += ")"

    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)
    return {"status": "success"}


@app.route("/search-order", methods=['GET'])
def get_order_view():
    return render_template('search-order.html')


@app.route("/search-order", methods=['POST'])
def do_get_order():
    sql = "SELECT * FROM Orders WHERE customer_id = "
    sql += f'"{request.form["customer_id"]}"'
    conn = mysqlite.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    data = []
    for row in result:
        data.append({
            "id": row[0],
            "customer_id": row[1],
            "order_date": row[2],
            "expected_delivery_date": row[3],
            "actual_delivery_date": row[4],
            "item_name": row[5],
            "unit": row[6],
            "quantity": row[7],
            "unit_price": row[8],
            "total_price": row[9],
            "supplier_name": row[10],
            "supplier_id": row[11]
        })

    # show the result in the html page
    return render_template('search-order.html', data=data)


@app.route("/update-order", methods=['GET'])
def update_order_view():
    return render_template('update-order.html')


@app.route("/update-order", methods=['POST'])
def do_update_order():
    total_price = int(request.form["quantity"]) * \
        int(request.form["unit_price"])
    sql = "UPDATE Orders SET "
    sql += f'customer_id = "{request.form["customer_id"]}",'
    sql += f'order_date = "{request.form["order_date"]}",'
    sql += f'expected_delivery_date = "{request.form["expected_delivery_date"]}",'
    sql += f'actual_delivery_date = "{request.form["actual_delivery_date"]}",'
    sql += f'item_name = "{request.form["item_name"]}",'
    sql += f'unit = "{request.form["unit"]}",'
    sql += f'quantity = "{request.form["quantity"]}",'
    sql += f'unit_price = "{request.form["unit_price"]}",'
    sql += f'total_price = "{total_price}",'
    sql += f'supplier_name = "{request.form["supplier_name"]}",'
    sql += f'supplier_id = "{request.form["supplier_id"]}"'
    sql += f' WHERE id = "{request.form["id"]}"'

    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)

    return {"status": "success"}


@app.route("/create-purchase", methods=['GET'])
def create_purchase_view():
    return render_template('create-purchase.html')


@app.route("/create-purchase", methods=['POST'])
def do_create_purchase():
    total_price = int(request.form["quantity"]) * \
        int(request.form["unit_price"])
    sql = "INSERT INTO Purchases"
    sql += "(`supplier_name`,`supplier_id`,`supplier_contact`,`item_name`,`quantity`,`unit`,`unit_price`,`total_price`,`storage_location`,`specification`,`purchase_date`)"
    sql += " VALUES ("
    sql += f'"{request.form["supplier_name"]}",'
    sql += f'"{request.form["supplier_id"]}",'
    sql += f'"{request.form["supplier_contact"]}",'
    sql += f'"{request.form["item_name"]}",'
    sql += f'"{request.form["quantity"]}",'
    sql += f'"{request.form["unit"]}",'
    sql += f'"{request.form["unit_price"]}",'
    sql += f'"{total_price}",'
    sql += f'"{request.form["storage_location"]}",'
    sql += f'"{request.form["specification"]}",'
    sql += f'"{request.form["purchase_date"]}"'
    sql += ")"

    conn = mysqlite.connect()
    mysqlite.execute(sql, conn=conn)
    return {"status": "success"}


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
