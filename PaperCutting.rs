use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

fn solve(n: i32, m: i32) -> i64 {
    let k1:i64 = (m*1).into();
    let k2:i64 = (n*1).into();
    return k1*k2 - 1;
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let first_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let n = first_multiple_input[0].trim().parse::<i32>().unwrap();

    let m = first_multiple_input[1].trim().parse::<i32>().unwrap();

    let result = solve(n, m);

    writeln!(&mut fptr, "{}", result).ok();
}
