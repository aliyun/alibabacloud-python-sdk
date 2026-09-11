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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # The conflict policy for files with the same name.
        # Valid values:
        # 
        # - SKIP_THE_FILE: Skips files with the same name.
        # - KEEP_LATEST: Compares the update time and keeps the latest version.
        # - OVERWRITE_EXISTING: Forcibly overwrites files with the same name.
        # > This parameter is required when the file system type is CPFS for Lingjun.
        self.conflict_policy = conflict_policy
        # Specifies whether to enable automatic creation of the folder if it does not exist.
        # Valid values:
        # 
        # - true: Automatic creation of the folder is enabled.
        # - false (default): Automatic creation of the folder is not enabled.
        # 
        # > - This parameter takes effect when TaskAction is set to Import.
        # > - Only CPFS for Lingjun 2.6.0 and later support this feature.
        self.create_dir_if_not_exist = create_dir_if_not_exist
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The type of data on which the data flow task operates.
        # 
        # Valid values:
        # 
        # - Metadata: the metadata of files, including attributes such as timestamp, ownership, and permission. If you select Metadata, only the metadata of files is imported. You can see the file, but when you access the file data, the data is loaded from the source storage on demand.
        # - Data: the data blocks of files.
        # - MetaAndData: the metadata and data blocks of files.
        # > When TaskAction is set to Evict, the DataType parameter is required.
        self.data_type = data_type
        # The source directory of the data.
        # 
        # Limits:
        # - The value must be 1 to 1,023 characters in length.
        # - The value must be encoded in UTF-8.
        # - The value must start and end with a forward slash (/).
        # - Only one directory can be specified at a time.
        # - When TaskAction is set to Export, this directory must be a relative path within FileSystemPath.
        # - When TaskAction is set to Import, this directory must be a relative path within SourceStoragePath.
        # - When TaskAction is set to StreamExport, this directory must be a relative path within FileSystemPath.
        # - When TaskAction is set to StreamImport, this directory must be a relative path within SourceStoragePath.
        # > StreamImport and StreamExport are supported only by CPFS for Lingjun 2.6.0 and later.
        # Directory, EntryList, and TransferFileListPath are mutually exclusive parameters. You can specify only one of them.
        self.directory = directory
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity, verifies inventory, and performs other checks without actually creating the instance or incurring fees.
        # 
        # Valid values:
        # 
        # - true: sends a dry run request without creating the instance. The check items include whether required parameters are specified, the request format, business limits, and File Storage NAS inventory. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but TaskId is empty.
        # - false (default): sends a normal request. After the check succeeds, the instance is directly created.
        self.dry_run = dry_run
        # The target directory to which the data flow task is mapped.
        # Limits:
        #  - The value must start and end with a forward slash (/). /../ is not supported.
        #  - The value must be 1 to 1,023 characters in length.
        #  - The value must be encoded in UTF-8.
        #  - Only one directory can be specified at a time.
        #  - When TaskAction is set to Export, this directory must be a relative path within SourceStoragePath.
        #  - When TaskAction is set to Import, this directory must be a relative path within FileSystemPath.
        #  - When TaskAction is set to StreamExport, this directory must be a relative path within SourceStoragePath.
        #  - When TaskAction is set to StreamImport, this directory must be a relative path within FileSystemPath.
        # > StreamImport and StreamExport are supported only by CPFS for Lingjun 2.6.0 and later.
        self.dst_directory = dst_directory
        # The list of files on which the data flow task is executed.
        # 
        # Limits:
        # 
        # - The value must be encoded in UTF-8.
        # - The total length of the file list must be less than 64 KB.
        # - The file list must be in JSON format.
        # - The path of each file must be 1 to 1,023 characters in length and must start with a forward slash (/).
        # - When TaskAction is set to Import, each element in the list represents an OSS object name.
        # - When TaskAction is set to Export, each element in the list represents a CPFS file path.
        # > Directory, EntryList, and TransferFileListPath are mutually exclusive parameters. You can specify only one of them.
        self.entry_list = entry_list
        # The file system ID.
        # 
        # - General-purpose CPFS: The ID must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # Filters directories under the specified directory and transfers the content of the included folders.
        # 
        # > - This parameter takes effect only when the Directory parameter is specified.
        # > - The path of each folder must be 1 to 1,023 characters in length and must start and end with a forward slash (/). The total length cannot exceed 3,000 characters.
        # > - Only CPFS for Lingjun supports this feature.
        self.includes = includes
        # If you specify SrcTaskId, enter the data flow task ID. The system copies the TaskAction, DataType, and EntryList parameter information from the specified data flow task. You do not need to specify these parameters separately.
        # > Data flow streaming tasks are not supported.
        self.src_task_id = src_task_id
        # The data flow node type.
        # 
        # Valid values:
        # 
        # - Import: data import from the source storage to CPFS.
        # - Export: exports specified data from CPFS to the source storage.
        # - StreamImport: batch data import from the source storage to CPFS.
        # - StreamExport: batch exports specified data from CPFS to the source storage.
        # - Evict: releases data blocks of files on CPFS. After the release, only metadata is retained on CPFS. You can still query the file, but the data blocks are purged and do not occupy storage capacity on CPFS. When you access the file data, the data is loaded from the source storage on demand.
        # - Inventory: obtains the file checklist managed by the data stream on CPFS. This provides the cache status of files in the data stream.
        # > CPFS for Lingjun supports only Import, Export, StreamImport, and StreamExport. StreamImport and StreamExport are supported only by CPFS for Lingjun 2.6.0 and later.
        self.task_action = task_action
        # The OSS directory. Data is synchronized based on the content of CSV files in the OSS directory. Limits:
        # - The value must start and end with a forward slash (/).
        # 
        # - The value is case-sensitive.
        # 
        # - The value must be 1 to 1,023 characters in length.
        # 
        # - The value must be encoded in UTF-8.
        # 
        # 
        # >- TransferFileListPath, Directory, and EntryList are mutually exclusive parameters. You can specify only one of them.
        # >- This parameter specifies an existing path in OSS. The \\*.csv files in the path are stored in OSS.
        # > - TransferFileListPath supports only Import and Export.
        # > - For Import, the files or directories specified in the CSV files are imported from OSS to CPFS.
        # > - For Export, the files or directories specified in the CSV files are exported from CPFS to OSS.
        # > - The CSV file must contain the Name and Type columns. Name is a relative path. Type supports two values: dir and file. If Type is dir, the Name value must end with a forward slash (/).
        # >- Only CPFS for Lingjun supports this feature.
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

