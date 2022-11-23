echo "Compiling scss files"
for f in `find $(pwd)/src -name "*.scss"` 
do 
    css=$(echo "$f" | sed "s/scss/css/")
    sass "$f:$css" --no-source-map  
    echo " [x] Done $f"
    # sass "$f:$css" --source-map-urls=absolute
done