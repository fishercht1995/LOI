#!/bin/bash

LOG_FILE="../../execution_time.log"
temp_dir=$1
model=$2
for cloud in s3 gcp r2; 
do
    echo "Start Cloud $cloud"
    for compression in znn tensors; 
    do
        echo "Download file $compression"
        for i in {1..5};do
            rm -rf $temp_dir/*
            # 记录开始时间
            start_time=$(date +%s)
            start_time_human=$(date "+%Y-%m-%d %H:%M:%S")

            # 执行命令
            echo "Executing: $*"
            echo "Start Time: $start_time_human"
            python3 "${cloud}.py" "${model}-${compression}" "$temp_dir"

            # 记录结束时间
            end_time=$(date +%s)
            end_time_human=$(date "+%Y-%m-%d %H:%M:%S")

            # 计算执行时间
            execution_time=$((end_time - start_time))

            # 记录到日志
            echo "End Time: $end_time_human"
            echo "Execution Time: ${execution_time} seconds"
        done
    done
done
