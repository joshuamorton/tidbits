//first iteration, the base code they provided 176 boxes

//second iteration, replaced for loops with while loops, made life easier 176 boxes

//Third iteration
//added the check for next being free, and thus double sized squares
//sqaures reduced to 102, a significant improvement, but we can do better

var grid = this.getNavGrid().grid;
var tileSize = 4;
var y = 0;
while(y + tileSize < grid.length) {
    var x = 0;
    while(x + tileSize < grid[0].length) {
        var occupied = grid[y][x].length > 0;
        var next = grid[y][x+tileSize].length >0;
        if(!occupied) {
            if(!next) {
                this.addRect(x+tileSize, y+tileSize/2, 2* tileSize, tileSize);
                x += tileSize;
                this.wait();
            }else{
            this.addRect(x + tileSize / 2, y + tileSize / 2, tileSize, tileSize);
            this.wait();  // Hover over the timeline to help debug!
            }
        }
        x += tileSize;
    }
    y += tileSize;
}

// fourth iteration
//makes the longest lateral square possible
//squared further reduced to 54

var grid = this.getNavGrid().grid;
var tileSize = 4;
var y = 0;
while(y + tileSize < grid.length) {
    var x = 0;
    while(x + tileSize < grid[0].length) {
        var current = grid[y][x].length > 0;
        var length = 0;
        if (!current){
            while (!current) {
                length += 1;
                x += tileSize;
                current = grid[y][x].length > 0;
            }
            this.addRect(x - tileSize * length /2, y + tileSize / 2, length * tileSize, tileSize);
        }    
        x += tileSize;

    }
    y += tileSize;
}

//fifth iteration
//looks very different
//30 squares

//the main difference is the recursive check ("here") that looks through all previously 
//created rectangles and sees if any are the same width as, and touching, the current rectangle.  If so, it merges them (essentially)

var grid = this.getNavGrid().grid;
var tileSize = 4;
var y = 0;
while(y + tileSize < grid.length) { //O(n)
    var x = 0;
    while(x + tileSize < grid[0].length) { //O(n*m)
        var current = grid[y][x].length > 0;
        var length = 0;
        if (!current){
            while (!current) { //O(n^2*m)
                length += 1;
                x += tileSize;
                current = grid[y][x].length > 0;    
            }
            xPos = x - tileSize * length/2;
            width = length * tileSize;
            var myRect;
            var sameRectExists = false;
            for(var i = 0; i < this.spawnedRectangles.length; ++i) { //O(n^3m^2), I think?
                var rect = this.spawnedRectangles[i];
                if(rect.width == width && rect.pos.x == xPos && rect.pos.y+rect.height/2 == y) { //<- here
                    sameRectExists = true;
                    myRect = rect;
                }
            }
            if(sameRectExists) { 
                this.addRect(xPos, y + tileSize / 2- myRect.height / 2, width, tileSize+myRect.height);
                this.removeRectAt(myRect.pos.x, myRect.pos.y);
            }else{
                this.addRect(xPos, y + tileSize / 2, width, tileSize);
            }
        }    
        x += tileSize;
    }
    y += tileSize;
}

//all in all I wrote these between 1:30 and 2:55 this morning.

//sixth iteration
//adding a single change for staricase type situations
//hopefully this will be quick and easy, probably not though.

var grid = this.getNavGrid().grid;
var tileSize = 4;
var y = 0;
var rects = this.spawnedRectangles;
while(y + tileSize < grid.length) {
    var x = 0;
    while(x + tileSize < grid[0].length) {
        var occupied = grid[y][x].length > 0;
        if(!occupied) {
            this.addRect(x + tileSize / 2, y + tileSize / 2, tileSize, tileSize);
        }
        x += tileSize;
    }
    y += tileSize;
    //start with this
}
rects = this.spawnedRectangles;

function mergeBlocks(that,firstRect,secondRect) {
    if(firstRect.pos.x == secondRect.pos.x) { //the two blocks are stacked
        centerX = firstRect.pos.x;
        centerY = ( (firstRect.height * firstRect.pos.y) + (secondRect.height * secondRect.pos.y) ) / (firstRect.height + secondRect.height);
        width = firstRect.width;
        height = firstRect.height + secondRect.height;
        that.addRect(centerX, centerY, width, height);
        that.removeRectAt(firstRect.pos.x, firstRect.pos.y);
        that.removeRectAt(secondRect.pos.x, secondRect.pox.y);
    }else if(firstRect.pos.y == secondRect.pos.y) { //the two block are next to each other
        centerY = firstRect.pos.y;
        centerX = ( (firstRect.width * firstRect.pos.x) + (secondRect.width * secondRect.pos.x) ) / (firstRect.width + secondRect.width);
        height = firstRect.height;
        width = firstRect.width + secondRect.width;
        that.addRect(centerX, centerY, width, height);
        that.removeRectAt(firstRect.pos.x, firstRect.pos.y);
        that.removeRectAt(secondRect.pos.x, secondRect.pox.y);
    }
    rects = this.spawnedRectangles;
}

function rectExist(that,x,y) {
    var retval = false;
    var i = 0;
    while(i < rects.length) {
        var rect = rects[i];
        if( (x <= rect.pos.x + rect.width / 2 && x >= rect.pos.x - rect.width / 2) && (y <= rect.pos.y + rect.height / 2 && y >= rect.pos.y - rect.height / 2)) {
            retval = true;
            i = rect.length;
        }
        i += 1;
    }
    return retval;
}

var y = 0;
while(y + tileSize < grid.length) {
    var x = 0;
    while(x + tileSize < grid[0].length) {
        var occupied = grid[y][x].length > 0;
        var next = grid[y][x+tileSize].length >0;
        if(!occupied) {
            if(!next) {

            }else{
            this.addRect(x + tileSize / 2, y + tileSize / 2, tileSize, tileSize);
            this.wait();  // Hover over the timeline to help debug!
            }
        }
        x += tileSize;
    }
    y += tileSize;
}