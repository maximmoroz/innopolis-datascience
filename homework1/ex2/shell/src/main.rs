use std::process::Command;
use std::io;
use rustyline::error::ReadlineError;
use rustyline::Editor;
use std::io::Write;

fn handle_input(cmd_line: String) {
    let split: Vec<String> = cmd_line.split_whitespace().map (|s| String::from(s)).collect();
    let exec_name = &split[0];

    let mut cmd = Command::new(exec_name);
    cmd.args(&split[1..]);
    match cmd.output() {
        Ok(output) => {
            io::stderr().write_all(&*output.stderr).expect("stderr failed");
            io::stdout().write_all(&*output.stdout).expect("stdout failed");
        }
        Err(e) => {
            println!("Exec failure: {}", e.to_string());
        }
    }
}

fn main() {
    println!("Rust shell for Innopolis Data Science!");
    // `()` can be used when no completer is required
    let mut rl = Editor::<()>::new();
    if rl.load_history("history.txt").is_err() {
        println!("No previous history.");
    }
    loop {
        let readline = rl.readline("DS>> ");
        match readline {
            Ok(line) => {
                rl.add_history_entry(line.as_str());
                handle_input(line);
            },
            Err(ReadlineError::Interrupted) => {
                println!("CTRL-C");
                break
            },
            Err(ReadlineError::Eof) => {
                println!("CTRL-D");
                break
            },
            Err(err) => {
                println!("Error: {:?}", err);
                break
            }
        }
    }
    rl.save_history("history.txt").unwrap();
}
