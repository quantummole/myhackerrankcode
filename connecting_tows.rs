use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'connectingTowns' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY routes
 */

fn connectingTowns(n: i32, routes: &[i32]) -> i32 {
    let mut start_value:i32 = 1;
    for (i, item) in routes.iter().enumerate(){
        start_value = start_value * item;
        start_value = start_value % 1234567;
    }
    return start_value;
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let t = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    for _ in 0..t {
        let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

        let routes: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();

        let result = connectingTowns(n, &routes);

        writeln!(&mut fptr, "{}", result).ok();
    }
}
