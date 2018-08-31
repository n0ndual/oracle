target=$1

echo $target

echo "
test generate proof
"

filename=$(curl -s -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/generate -d '{"target": "'$target'"}')

echo "proof file name: ${filename}"

echo "
test verify proof
"
# verify proof
result=$(curl -s -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/review/$filename)

echo "verify result:\n${result}"
