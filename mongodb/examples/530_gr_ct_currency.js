var query = {
    $group : {
        _id : "$price.currency",
        count : {$sum : 1}
    }
}

var response = db.books.aggregate(query);
response.result.forEach(printjson);
