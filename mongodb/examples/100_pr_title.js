var query = {
    $project : {
        title: 1
    }
};

var response = db.books.aggregate(query);
response.result.forEach(printjson);
