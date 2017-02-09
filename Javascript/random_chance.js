function slot (quarters, x) {
    if (x) {
        while (quarters > x) {
            if (Math.floor((Math.random() * 100) + 1) == 10) {
                console.log("You won");
                quarters += Math.floor((Math.random() * 51) + 50);
                console.log(quarters)
                break;
            }
            else {
                console.log("you lost")
            }
            quarters -= 1;
        }
    }
    else {
        while (quarters > 0) {
            if (Math.floor((Math.random() * 100) + 1) == 10) {
                console.log("You won");
                quarters += Math.floor((Math.random() * 51) + 50);
                console.log(quarters)
                break;
            }
            else {
                console.log("you lost");
            }
            quarters -= 1;
        }
    }

}
slot(10);
