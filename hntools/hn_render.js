const hermit = require("hermit");
const fs = require("fs");
const Async = require("async");

function getItems(jsonFilePath) {
    try {
        return JSON.parse(fs.readFileSync(jsonFilePath));
    } catch(e) {
        console.error("Unable to read/parse JSON file", jsonFilePath);
        return [];
    }
}

function renderItem(item, callback) {
    hermit(item.text, function(err, resp) {
        if (!err) {
            console.log(resp);
            console.log("---------------------------------------------------------------");
        }
        callback(err);
    });
}

function renderAllItems(itemList, callback) {
    Async.eachSeries(itemList, renderItem, callback);
}

function main() {
    let jsonFilePath = process.argv[2];

    if (jsonFilePath) {
        renderAllItems(getItems(jsonFilePath), function(err) {
            if (err) {
                console.error("Could not render", err);
            }
        })
    } else {
        console.error("Usage: node hn_render.js <json file of HN item list>")
    }
}

main();