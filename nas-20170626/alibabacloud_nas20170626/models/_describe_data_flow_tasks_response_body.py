# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowTasksResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        task_info: main_models.DescribeDataFlowTasksResponseBodyTaskInfo = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about dataflow tasks.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeDataFlowTasksResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class DescribeDataFlowTasksResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        task: List[main_models.DescribeDataFlowTasksResponseBodyTaskInfoTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['Task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k1 in m.get('Task'):
                temp_model = main_models.DescribeDataFlowTasksResponseBodyTaskInfoTask()
                self.task.append(temp_model.from_map(k1))

        return self

class DescribeDataFlowTasksResponseBodyTaskInfoTask(DaraModel):
    def __init__(
        self,
        conflict_policy: str = None,
        create_time: str = None,
        data_flow_id: str = None,
        data_type: str = None,
        directory: str = None,
        dst_directory: str = None,
        end_time: str = None,
        error_msg: str = None,
        file_system_path: str = None,
        filesystem_id: str = None,
        fs_path: str = None,
        includes: str = None,
        originator: str = None,
        progress: int = None,
        progress_stats: main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats = None,
        report_path: str = None,
        reports: main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskReports = None,
        source_storage: str = None,
        start_time: str = None,
        status: str = None,
        task_action: str = None,
        task_id: str = None,
        transfer_file_list_path: str = None,
    ):
        # The conflict policy for files with the same name. Valid values:
        # 
        # *   SKIP_THE_FILE: skips files with the same name.
        # *   KEEP_LATEST: compares the update time and keeps the latest version.
        # *   OVERWRITE_EXISTING: forcibly overwrites the existing file.
        self.conflict_policy = conflict_policy
        # The time when the task was created.
        self.create_time = create_time
        # The ID of the dataflow.
        self.data_flow_id = data_flow_id
        # The type of data on which operations are performed by the dataflow task. The following information is displayed:
        # 
        # *   Metadata: the metadata of a file, including the timestamp, ownership, and permission information of the file. If you select Metadata, only the metadata of the file is imported. You can only query the file. When you access the file data, the file is loaded from the source storage as required.
        # *   Data: the data blocks of the file.
        # *   MetaAndData: the metadata and data blocks of the file.
        # 
        # >  CPFS for Lingjun supports only the MetaAndData type.
        self.data_type = data_type
        # The directory in which the dataflow task is executed.
        self.directory = directory
        # The directory mapped to the dataflow task.
        self.dst_directory = dst_directory
        # The end time of the task.
        self.end_time = end_time
        # The cause of the task exception.
        # 
        # >  If this parameter is not returned or the return value is empty, no error occurs.
        self.error_msg = error_msg
        # The directory of the fileset in the CPFS file system.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be a fileset directory in the CPFS file system.
        # 
        # >  Only CPFS supports this parameter.
        self.file_system_path = file_system_path
        # The ID of the file system.
        self.filesystem_id = filesystem_id
        # The path of the smart directory.
        self.fs_path = fs_path
        # Filters subdirectories and transfers their contents.
        # 
        # >  Only CPFS for Lingjun supports this operation.
        self.includes = includes
        # The initiator of the dataflow task. The following information is displayed:
        # 
        # *   User: The task is initiated by a user.
        # *   System: The task is automatically initiated by CPFS based on the automatic update interval.
        # 
        # >  Only CPFS supports this parameter.
        self.originator = originator
        # The progress of the dataflow task. The number of operations that have been performed by the dataflow task.
        self.progress = progress
        # The progress of the dataflow task.
        self.progress_stats = progress_stats
        # The save path of dataflow task reports in the CPFS file system.
        # 
        # *   The task reports for a CPFS file system are generated in the `.dataflow_report` directory of the CPFS file system.
        # *   CPFS for Lingjun returns an OSS download link for you to download the task reports.
        self.report_path = report_path
        # The reports.
        # 
        # > 
        # 
        # *   Streaming tasks do not support reports.
        # 
        # *   If the WithReport parameter is set to True, the CPFS for Lingjun report data is returned.
        # 
        # *   Only CPFS for Lingjun supports the WithReport parameter.
        self.reports = reports
        # The access path of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Among them:
        # 
        # *   storage type: Only Object Storage Service (OSS) is supported.
        # 
        # *   account id: the UID of the account of the source storage.
        # 
        # *   path: the name of the OSS bucket. Limits:
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name can be up to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        # 
        # > 
        # 
        # *   The OSS bucket must be an existing bucket in the region.
        # 
        # *   Only CPFS for Lingjun V2.6.0 and later support the account id parameter.
        self.source_storage = source_storage
        # The start time of the task.
        self.start_time = start_time
        # The status of the dataflow task. The following information is displayed:
        # 
        # *   Pending: The dataflow task has been created and has not started.
        # *   Executing: The dataflow task is being executed.
        # *   Failed: The dataflow task failed to be executed. You can view the cause of the failure in the dataflow task report.
        # *   Completed: The dataflow task is completed. You can check that all the files have been correctly transferred in the dataflow task report.
        # *   Canceled: The dataflow task is canceled and is not completed.
        # *   Canceling: The dataflow task is being canceled.
        self.status = status
        # The type of the dataflow task. The following information is displayed:
        # 
        # *   Import: imports data stored in the source storage to a CPFS file system.
        # *   Export: exports specified data from a CPFS file system to the source storage.
        # *   StreamImport: imports the specified data from the source storage to a CPFS file system in streaming mode.
        # *   StreamExport: exports specified data from a CPFS file system to the source storage in streaming mode.
        # *   Evict: releases the data blocks of a file in a CPFS file system. After the eviction, only the metadata of the file is retained in the CPFS file system. You can still query the file. However, the data blocks of the file are cleared and do not occupy the storage space in the CPFS file system. When you access the file data, the file is loaded from the source storage as required.
        # *   Inventory: obtains the inventory list managed by a dataflow from the CPFS file system, providing the cache status of inventories in the dataflow.
        # 
        # >  Only CPFS for Lingjun V2.6.0 and later support StreamImport and StreamExport.
        self.task_action = task_action
        # The ID of the dataflow task.
        self.task_id = task_id
        # Specify the OSS directory and synchronize data based on the content of the CSV file in the OSS directory.
        # 
        # >  Only CPFS for Lingjun supports this operation.
        self.transfer_file_list_path = transfer_file_list_path

    def validate(self):
        if self.progress_stats:
            self.progress_stats.validate()
        if self.reports:
            self.reports.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_policy is not None:
            result['ConflictPolicy'] = self.conflict_policy

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.dst_directory is not None:
            result['DstDirectory'] = self.dst_directory

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id

        if self.fs_path is not None:
            result['FsPath'] = self.fs_path

        if self.includes is not None:
            result['Includes'] = self.includes

        if self.originator is not None:
            result['Originator'] = self.originator

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.progress_stats is not None:
            result['ProgressStats'] = self.progress_stats.to_map()

        if self.report_path is not None:
            result['ReportPath'] = self.report_path

        if self.reports is not None:
            result['Reports'] = self.reports.to_map()

        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.transfer_file_list_path is not None:
            result['TransferFileListPath'] = self.transfer_file_list_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictPolicy') is not None:
            self.conflict_policy = m.get('ConflictPolicy')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('DstDirectory') is not None:
            self.dst_directory = m.get('DstDirectory')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')

        if m.get('FsPath') is not None:
            self.fs_path = m.get('FsPath')

        if m.get('Includes') is not None:
            self.includes = m.get('Includes')

        if m.get('Originator') is not None:
            self.originator = m.get('Originator')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProgressStats') is not None:
            temp_model = main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats()
            self.progress_stats = temp_model.from_map(m.get('ProgressStats'))

        if m.get('ReportPath') is not None:
            self.report_path = m.get('ReportPath')

        if m.get('Reports') is not None:
            temp_model = main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskReports()
            self.reports = temp_model.from_map(m.get('Reports'))

        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TransferFileListPath') is not None:
            self.transfer_file_list_path = m.get('TransferFileListPath')

        return self

class DescribeDataFlowTasksResponseBodyTaskInfoTaskReports(DaraModel):
    def __init__(
        self,
        report: List[main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport] = None,
    ):
        self.report = report

    def validate(self):
        if self.report:
            for v1 in self.report:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Report'] = []
        if self.report is not None:
            for k1 in self.report:
                result['Report'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report = []
        if m.get('Report') is not None:
            for k1 in m.get('Report'):
                temp_model = main_models.DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport()
                self.report.append(temp_model.from_map(k1))

        return self

class DescribeDataFlowTasksResponseBodyTaskInfoTaskReportsReport(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        # The name of the report.
        # 
        # *   CPFS:
        # 
        #     TotalFilesReport: task reports.
        # 
        # *   CPFS for Lingjun:
        # 
        #     *   FailedFilesReport: failed file reports.
        #     *   SkippedFilesReport: skipped file reports.
        #     *   SuccessFilesReport: successful file reports.
        self.name = name
        # The report URL.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class DescribeDataFlowTasksResponseBodyTaskInfoTaskProgressStats(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_files: int = None,
        average_speed: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
        files_done: int = None,
        files_total: int = None,
        remain_time: int = None,
    ):
        # The actual amount of data for which the dataflow task is complete. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The actual number of files for which the dataflow task is complete.
        self.actual_files = actual_files
        # The average flow velocity. Unit: bytes/s.
        self.average_speed = average_speed
        # The amount of data (including skipped data) for which the dataflow task is complete. Unit: bytes.
        self.bytes_done = bytes_done
        # The amount of data scanned on the source. Unit: bytes.
        self.bytes_total = bytes_total
        # The number of files (including skipped files) for which the dataflow task is complete.
        self.files_done = files_done
        # The number of files scanned on the source.
        self.files_total = files_total
        # The estimated remaining execution time. Unit: seconds.
        self.remain_time = remain_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.actual_files is not None:
            result['ActualFiles'] = self.actual_files

        if self.average_speed is not None:
            result['AverageSpeed'] = self.average_speed

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.files_done is not None:
            result['FilesDone'] = self.files_done

        if self.files_total is not None:
            result['FilesTotal'] = self.files_total

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('ActualFiles') is not None:
            self.actual_files = m.get('ActualFiles')

        if m.get('AverageSpeed') is not None:
            self.average_speed = m.get('AverageSpeed')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('FilesDone') is not None:
            self.files_done = m.get('FilesDone')

        if m.get('FilesTotal') is not None:
            self.files_total = m.get('FilesTotal')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        return self

