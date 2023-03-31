#[macro_use]
extern crate honggfuzz;

extern crate cpython;

use cpython::{PyObject, PyResult, PyLong, PyTuple, Python};

fn main() {
    loop {
        fuzz!(|data: (i64, i64)| {

            let gil = Python::acquire_gil();
            let py = gil.python();
            let script = py.import("logistic_regression").unwrap();
            let high_i64 = data.0;
            let low_i64 = data.1;
            let py_high = py.eval(&format!("int({})", high_i64), None, None).unwrap();
            let py_low = py.eval(&format!("int({})", low_i64), None, None).unwrap();

            let args = PyTuple::new(py, &[py_high, py_low]);
            let result = script.call(py, "compare_concrete_scikit_predictions", args, None).unwrap();
        });
    }
}
