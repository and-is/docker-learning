## Points

### Working with py
-i flag for interactive mode so that we can offer standard input, without this we can't even in attached mode.
-t flag provides pseudo terminal for that input.
can combine these two flags. need both of these ok. 
-i only can also suffice tho.
Using `docker start -a` won't work as well. we need to combine it with -i as well. We need no -t as no terminal reqd in this case as there's explicit attach here. 