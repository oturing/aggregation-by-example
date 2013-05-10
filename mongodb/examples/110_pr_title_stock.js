var query = {
    $project : {
        stock: 1
    }
};

var response = db.books.aggregate(query);
response.result.forEach(printjson);
