var query = {
    $group : {
        _id : null,
        count : {$sum : "$stock"}
    }
};

var response = db.books.aggregate(query);
response.result.forEach(printjson);
