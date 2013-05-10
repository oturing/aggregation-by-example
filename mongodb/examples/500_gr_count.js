var query = {
    $group : {
        _id : null,
        count : {$sum : 1}
    }
};

var response = db.books.aggregate(query);
response.result.forEach(printjson);
