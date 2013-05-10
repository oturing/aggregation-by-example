var query = {
    $project : {
        _id: 0,
        stock: 1
    }
};

var response = db.books.aggregate(query);
response.result.forEach(printjson);
