echo "
test generate proof
"

filename=$(curl -s -H "Content-Type: application/json" -X POST http://47.88.54.59:5000/generate -d '{"target": "apifootball.com/api/?action=get_events&APIkey=c28349114bd830cda823625906827385b204ea83e731b00499f89ebf2a6bf66d&country_id=169&league_id=62&from=2018-8-19&to=2018-8-21&match_id=306321"}')

echo "proof file name: ${filename}"

echo "
test download proof
"
# download proof
wget http://47.88.54.59:5000/download/$filename

echo "

test save proof to ipfs

"
# save to ipfs
ipfspath=$(curl -s -H "Content-Type: application/json" -X POST http://47.88.54.59:5000/ipfs/$filename)

echo "ipfs path: ${ipfspath}"

echo "
test verify proof
"
# verify proof
result=$(curl -s -H "Content-Type: application/json" -X POST http://47.88.54.59:5000/review/$filename)

echo "verify result:\n${result}"

# all in one
# curl -H "Content-Type: application/json" -X POST http://47.88.54.59:5000/foo -d '{"target": "apifootball.com/api/?action=get_events&APIkey=c28349114bd830cda823625906827385b204ea83e731b00499f89ebf2a6bf66d&country_id=169&league_id=62&from=2018-8-19&to=2018-8-21&match_id=306321"}'

#
