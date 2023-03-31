#[macro_use]
extern crate honggfuzz;
extern crate cpython;

use cpython::{PyObject, PyResult, Python};

fn main() {
    loop {
        fuzz!(|data1: u64, data2: u64| {

            let gil = Python::acquire_gil();
            let py = gil.python();
            let script = py.import("logistic_regression")?;
            let result = script.call(py, "make_classification", (input,), None).unwrap();
        });
    }
}

