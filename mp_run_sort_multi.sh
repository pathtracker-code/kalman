# python sort.py --seq_path multi_npy
# Fig 3
# python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_32_32_32_separate_channels/0_dist/batch_5/0/ --out_path=sort_32_1
# python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_32_32_32_separate_channels/14_dist/batch_5/0/ --out_path=sort_32_14
# python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_32_32_32_separate_channels/25_dist/batch_5/0/ --out_path=sort_32_25 --alt_labeling

python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_64_32_32_separate_channels/0_dist/batch_5/0/ --out_path=sort_64_1
python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_64_32_32_separate_channels/14_dist/batch_5/0/ --out_path=sort_64_14
python mp_sort_cifs.py --seq_path /cifs/data/tserre_lrs/projects/prj_tracking/downsampled_constrained_red_blue_datasets_64_32_32_separate_channels/25_dist/batch_5/0/ --out_path=sort_64_25 --alt_labelin

# Fig 5
python mp_sort_cifs.py --out_path=sort_human_64_14 --seq_path=/cifs/data/tserre/CLPS_Serre_Lab/projects/prj_tracking/MTurk_videos_from_VM/downsampled_constrained_red_blue_64_32_32/14_dist_again_for_human_correlation/batch_0/0  #  --alt_labeling
python mp_sort_cifs.py --out_path=sort_human_64_25 --seq_path=/cifs/data/tserre/CLPS_Serre_Lab/projects/prj_tracking/MTurk_videos_from_VM/downsampled_constrained_red_blue_64_32_32/25_dist_again_for_human_correlation/batch_0/0  # --alt_labeling
python mp_sort_cifs.py --out_path=sort_human_128_14 --seq_path=/cifs/data/tserre/CLPS_Serre_Lab/projects/prj_tracking/MTurk_videos_from_VM/downsampled_constrained_red_blue_128_32_32/14_dist_again_for_human_correlation/batch_0/0  # --alt_labeling

