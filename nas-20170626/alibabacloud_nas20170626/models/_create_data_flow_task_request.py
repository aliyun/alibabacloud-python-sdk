# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataFlowTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        conflict_policy: str = None,
        create_dir_if_not_exist: bool = None,
        data_flow_id: str = None,
        data_type: str = None,
        directory: str = None,
        dry_run: bool = None,
        dst_directory: str = None,
        entry_list: str = None,
        file_system_id: str = None,
        includes: str = None,
        src_task_id: str = None,
        task_action: str = None,
        transfer_file_list_path: str = None,
    ):
        # A client-generated token that ensures the idempotence of the request. The token must be unique across different requests.
        # 
        # `ClientToken` can contain only ASCII characters and must not exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the `RequestId` of the API request as the `ClientToken`. The `RequestId` may be different for each API request.
        self.client_token = client_token
        # The conflict policy for files with the same name.
        # Valid values:
        # 
        # - SKIP_THE_FILE: Skips files with the same name.
        # 
        # - KEEP_LATEST: Compares update times and keeps the latest version.
        # 
        # - OVERWRITE_EXISTING: Forcibly overwrites files with the same name.
        # 
        # > This parameter is required if the file system is a CPFS AI-Computing Edition instance.
        self.conflict_policy = conflict_policy
        # Specifies whether to automatically create the directory if it does not exist.
        # Valid values:
        # 
        # - true: Automatically creates the directory.
        # 
        # - false (default): Does not automatically create the directory.
        # 
        # > * This parameter takes effect only when `TaskAction` is set to `Import`.
        # >
        # > * This parameter is supported only by CPFS AI-Computing Edition V2.6.0 and later.
        self.create_dir_if_not_exist = create_dir_if_not_exist
        # The ID of the data flow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The data type that the data flow task operates on.
        # 
        # Valid values:
        # 
        # - Metadata: The metadata of the file, including attributes such as timestamp, ownership, and permissions. If you select `Metadata`, only the file metadata is imported. You can see the file, but when you access the file data, it is loaded from the source storage on demand.
        # 
        # - Data: The data blocks of the file.
        # 
        # - MetaAndData: The metadata and data blocks of the file.
        self.data_type = data_type
        # The source directory of the data.
        # 
        # Limits:
        # 
        # - The length must be 1 to 1,023 characters.
        # 
        # - The directory must be UTF-8 encoded.
        # 
        # - The directory must start and end with a forward slash (`/`).
        # 
        # - Only one directory can be specified at a time.
        # 
        # - If `TaskAction` is `Export`, this directory must be a relative path within `FileSystemPath`.
        # 
        # - If `TaskAction` is `Import`, this directory must be a relative path within `SourceStoragePath`.
        # 
        # - If `TaskAction` is `StreamExport`, this directory must be a relative path within `FileSystemPath`.
        # 
        # - If `TaskAction` is `StreamImport`, this directory must be a relative path within `SourceStoragePath`.
        # 
        # > `StreamImport` and `StreamExport` are supported only by CPFS AI-Computing Edition V2.6.0 and later.
        self.directory = directory
        # Specifies whether to perform a dry run for this creation request.
        # 
        # A dry run checks parameter validity and inventory without creating an instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a check request without creating the instance. The system checks for required parameters, request format, business limits, and NAS inventory. If the check fails, an error is returned. If the check passes, an HTTP 200 status code is returned, but `TaskId` is empty.
        # 
        # - false (default): Sends a normal request and creates the instance after the check passes.
        self.dry_run = dry_run
        # The destination directory for the data flow task mapping.
        # Limits:
        # 
        # - The directory must start and end with a forward slash (`/`). The `/../` sequence is not supported.
        # 
        # - The length must be 1 to 1,023 characters.
        # 
        # - The directory must be UTF-8 encoded.
        # 
        # - Only one directory can be specified at a time.
        # 
        # - If `TaskAction` is `Export`, this directory must be a relative path within `SourceStoragePath`.
        # 
        # - If `TaskAction` is `Import`, this directory must be a relative path within `FileSystemPath`.
        # 
        # - If `TaskAction` is `StreamExport`, this directory must be a relative path within `SourceStoragePath`.
        # 
        # - If `TaskAction` is `StreamImport`, this directory must be a relative path within `FileSystemPath`.
        # 
        # > `StreamImport` and `StreamExport` are supported only by CPFS AI-Computing Edition V2.6.0 and later.
        self.dst_directory = dst_directory
        # The list of files for the data flow task to execute.
        # 
        # Limits:
        # 
        # - The list must be UTF-8 encoded.
        # 
        # - The total length of the file list must be less than 64 KB.
        # 
        # - The file list must be in JSON format.
        # 
        # - The path of a single file must be 1 to 1,023 characters in length and must start with a forward slash (`/`).
        # 
        # - If `TaskAction` is `Import`, each element in the list represents an OSS Object name.
        # 
        # - If `TaskAction` is `Export`, each element in the list represents a CPFS file path.
        self.entry_list = entry_list
        # The ID of the file system.
        # 
        # - CPFS General Purpose Edition: The ID must start with `cpfs-`, such as `cpfs-125487****`.
        # 
        # - CPFS AI-Computing Edition: The ID must start with `bmcpfs-`, such as `bmcpfs-0015****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # Filters the subdirectories under the `Directory` parameter and transfers the content of the filtered subdirectories.
        # 
        # > - This parameter takes effect only when the `Directory` parameter is specified.
        # >
        # > - The path of a single folder must be 1 to 1,023 characters in length and must start and end with a forward slash (`/`). The total length cannot exceed 3,000 characters.
        # >
        # > - This feature is supported only by CPFS AI-Computing Edition.
        self.includes = includes
        # If you specify `SrcTaskId`, enter the ID of a data flow task. The system copies the `TaskAction`, `DataType`, and `EntryList` parameter information from the specified task. You do not need to specify these parameters.
        # 
        # > Data flow streaming tasks are not supported.
        self.src_task_id = src_task_id
        # The type of the data flow task.
        # 
        # Valid values:
        # 
        # - Import: Imports specified data from the source storage to the CPFS file system.
        # 
        # - Export: Exports specified data from the CPFS file system to the source storage.
        # 
        # - StreamImport: Imports a large amount of specified data from the source storage to the CPFS file system.
        # 
        # - StreamExport: Exports a large amount of specified data from the CPFS file system to the source storage.
        # 
        # - Evict: Releases the data blocks of a file from the CPFS file system. After the release, only the metadata of the file is retained. You can still query the file, but its data blocks are cleared and no longer occupy storage capacity. When you access the file data, it is loaded from the source storage on demand.
        # 
        # - Inventory: Obtains the inventory of files managed by a data flow for the CPFS file system. This provides the cache status of files in the data flow.
        # 
        # > CPFS AI-Computing Edition supports only `Import`, `Export`, `StreamImport`, and `StreamExport`. `StreamImport` and `StreamExport` are supported only by CPFS AI-Computing Edition V2.6.0 and later.
        self.task_action = task_action
        # Specifies an OSS directory. Data is synchronized based on the content of the CSV files in this directory. The following limits apply.
        # 
        # - The path must start and end with a forward slash (`/`).
        # 
        # - The path is case-sensitive.
        # 
        # - The length must be between 1 and 1,023 characters.
        # 
        # - The path must be UTF-8 encoded.
        # 
        # > * `TransferFileListPath`, `Directory`, and `EntryList` are mutually exclusive. You can specify only one of them.
        # >
        # > * This parameter specifies an existing path in OSS. The `*.csv` files are stored in this path.
        # >
        # > * `TransferFileListPath` supports only the `Import` and `Export` features.
        # >
        # > * For an `Import` task, the files or directories specified in the CSV file are imported from OSS to the CPFS file system.
        # >
        # > * For an `Export` task, the files or directories specified in the CSV file are exported from the CPFS file system to OSS.
        # >
        # > * The CSV file must contain `Name` and `Type` columns. `Name` is the relative path. `Type` can be `dir` or `file`. If `Type` is `dir`, the `Name` value must end with a forward slash (`/`).
        # >
        # > * This feature is supported only by CPFS AI-Computing Edition.
        self.transfer_file_list_path = transfer_file_list_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.conflict_policy is not None:
            result['ConflictPolicy'] = self.conflict_policy

        if self.create_dir_if_not_exist is not None:
            result['CreateDirIfNotExist'] = self.create_dir_if_not_exist

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dst_directory is not None:
            result['DstDirectory'] = self.dst_directory

        if self.entry_list is not None:
            result['EntryList'] = self.entry_list

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.includes is not None:
            result['Includes'] = self.includes

        if self.src_task_id is not None:
            result['SrcTaskId'] = self.src_task_id

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.transfer_file_list_path is not None:
            result['TransferFileListPath'] = self.transfer_file_list_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConflictPolicy') is not None:
            self.conflict_policy = m.get('ConflictPolicy')

        if m.get('CreateDirIfNotExist') is not None:
            self.create_dir_if_not_exist = m.get('CreateDirIfNotExist')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DstDirectory') is not None:
            self.dst_directory = m.get('DstDirectory')

        if m.get('EntryList') is not None:
            self.entry_list = m.get('EntryList')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Includes') is not None:
            self.includes = m.get('Includes')

        if m.get('SrcTaskId') is not None:
            self.src_task_id = m.get('SrcTaskId')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TransferFileListPath') is not None:
            self.transfer_file_list_path = m.get('TransferFileListPath')

        return self

