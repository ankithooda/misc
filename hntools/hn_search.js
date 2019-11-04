const request = require("request");
const Async = require("async");

const ITEMURL = "https://hacker-news.firebaseio.com/v0/item/<itemid>.json";

function getItem(itemId, callback) {
    let itemUrl = ITEMURL.replace("<itemid>", itemId);
    request(itemUrl, function(err, response, body) {
        if (err) {
            callback(err);
        } else {
            try {
                body = JSON.parse(body);
                callback(null, body);
            } catch(e) {
                callback("Could not parse response", e);
            }
        }
    });
}

function getItemChildren(item, callback) {
    Async.mapLimit(
        item.kids,
        10,
        getItem,
        callback
    );
}

function processItemId(itemId, regexList, callback) {
    Async.waterfall(
        [
            function(cb) {
                getItem(itemId, cb);
            },
            getItemChildren,
            function(items, cb) {
                regexList.forEach(function(regex) {
                    items = items.filter(function(item){
                        return regex.test(item.text);
                    });                
                });
                cb(null, items);
            }
        ],
        callback
    );
}
function main() {
    let itemId = process.argv[2];
    let keywords = process.argv[3];
    let regex = [];
    if (keywords) {
        regex = keywords.split(",").map(function(keyword) {
            return RegExp(keyword, "i")
        });
    }
    if (itemId) {
        processItemId(itemId, regex, function(err, processedItem){
            if (err) {
                console.error("Processing Failed", err);
            } else {
                console.log(JSON.stringify(processedItem));
            }
        });
    } else {
        console.error("Usage: node hn_search.js <itemid> <keyword1,keyword2>");
    }
}

main();