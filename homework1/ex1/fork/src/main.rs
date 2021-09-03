use nix::unistd::{fork, sleep};
use std::env::args;
use std::str::FromStr;

fn main() {
    let argv: Vec<String> = args().collect();
    assert_eq!(argv.len(), 2);
    let count = i32::from_str(&argv[1]).unwrap();
    for _ in 0..count {
        unsafe {
            let _pid = fork();
        }
        sleep(5);
    }
}
