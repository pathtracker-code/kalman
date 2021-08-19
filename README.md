1. Run the data processing scripts (`python convert_file_multi.py` and `python convert_file_single.py`)
2. Run the matlab bash scripts (`bash run_multidist.sh` and `bash run_singledist.sh`)
3. Check results (`python evaluate_multidist.py` and `python evaluate_singledist.py`)
- You can find successes and failures for multi-distractor PathTracker (70% acc) in multi_ex and single-distractor PathTracker (100% acc) in single_ex
4. Run the Sort Kalman filter with `bash run_sort_single.sh` or `bash run_sort_multi.sh`
