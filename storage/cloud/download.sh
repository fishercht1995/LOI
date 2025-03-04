#!/bin/bash

LOG_FILE="../../execution_time.log"

# 记录开始时间
start_time=$(date +%s)
start_time_human=$(date "+%Y-%m-%d %H:%M:%S")

# 执行命令
echo "Executing: $*" | tee -a "$LOG_FILE"
echo "Start Time: $start_time_human" | tee -a "$LOG_FILE"

ls

# 记录结束时间
end_time=$(date +%s)
end_time_human=$(date "+%Y-%m-%d %H:%M:%S")

# 计算执行时间
execution_time=$((end_time - start_time))

# 记录到日志
echo "End Time: $end_time_human" | tee -a "$LOG_FILE"
echo "Execution Time: ${execution_time} seconds" | tee -a "$LOG_FILE"
