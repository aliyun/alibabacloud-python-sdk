# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListFilesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListFilesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The files returned.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The request ID. You can troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListFilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFilesResponseBodyData(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListFilesResponseBodyDataFiles] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of the files.
        self.files = files
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListFilesResponseBodyDataFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFilesResponseBodyDataFiles(DaraModel):
    def __init__(
        self,
        absolute_folder_path: str = None,
        auto_parsing: bool = None,
        biz_id: int = None,
        business_id: int = None,
        commit_status: int = None,
        connection_name: str = None,
        content: str = None,
        create_time: int = None,
        create_user: str = None,
        current_version: int = None,
        file_description: str = None,
        file_folder_id: str = None,
        file_id: int = None,
        file_name: str = None,
        file_type: int = None,
        is_max_compute: bool = None,
        last_edit_time: int = None,
        last_edit_user: str = None,
        node_id: int = None,
        owner: str = None,
        parent_id: int = None,
        use_type: str = None,
    ):
        # The path of the folder to which the file belongs.
        self.absolute_folder_path = absolute_folder_path
        # Specifies whether the automatic parsing feature is enabled for the file. Valid values:
        # 
        # *   true: The automatic parsing feature is enabled for the file.
        # *   false: The automatic parsing feature is not enabled for the file.
        # 
        # This parameter is equivalent to the Analyze Code parameter in the Dependencies section of the Properties panel in the [DataWorks console](https://workbench.data.aliyun.com/console).
        self.auto_parsing = auto_parsing
        # The ID of the workflow to which the file belongs. This parameter is deprecated and replaced by the BusinessId parameter.
        self.biz_id = biz_id
        # The ID of the workflow to which the file belongs.
        self.business_id = business_id
        # Indicates whether the latest code in the file is committed. Valid values: 0 and 1. The value 0 indicates that the latest code in the file is not committed. The value 1 indicates that the latest code in the file is committed.
        self.commit_status = commit_status
        # The ID of the compute engine instance that is used to run the node that corresponds to the file.
        self.connection_name = connection_name
        # This parameter is deprecated. You can call the [GetFile](~~173954#doc-api-dataworks-public-GetFile~~) operation to query the details of the file.
        self.content = content
        # The time when the file was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the file.
        self.create_user = create_user
        # The latest version number of the file.
        self.current_version = current_version
        # The description of the file.
        self.file_description = file_description
        # The ID of the folder to which the file belongs.
        self.file_folder_id = file_folder_id
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The type of the code in the file. Valid values: 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 99 (zero load), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (real-time synchronization), 1089 (cross-tenant collaboration), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (assignment), and 1221 (PyODPS 3).
        self.file_type = file_type
        # Indicates whether the file needs to be uploaded to MaxCompute if the file is a MaxCompute resource file.
        # 
        # This parameter is returned only if the file is a MaxCompute resource file.
        self.is_max_compute = is_max_compute
        # The time when the file was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_edit_time = last_edit_time
        # The ID of the Alibaba Cloud account that is used to last modify the file.
        self.last_edit_user = last_edit_user
        # The ID of the auto triggered node that is generated in the scheduling system after the file is committed.
        self.node_id = node_id
        # The ID of the Alibaba Cloud account used by the file owner.
        self.owner = owner
        # The ID of the node group file to which the current file belongs. This parameter is returned only if the current file is an inner file of the node group file.
        self.parent_id = parent_id
        # The module to which the file belongs. Valid values:
        # 
        # *   NORMAL: The file is used for DataStudio.
        # *   MANUAL: The file is used for a manually triggered node.
        # *   MANUAL_BIZ: The file is used for a manually triggered workflow.
        # *   SKIP: The files is used for a dry-run node in DataStudio.
        # *   ADHOCQUERY: The file is used for an ad hoc query.
        # *   COMPONENT: The file is used for a snippet.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute_folder_path is not None:
            result['AbsoluteFolderPath'] = self.absolute_folder_path

        if self.auto_parsing is not None:
            result['AutoParsing'] = self.auto_parsing

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.commit_status is not None:
            result['CommitStatus'] = self.commit_status

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.file_description is not None:
            result['FileDescription'] = self.file_description

        if self.file_folder_id is not None:
            result['FileFolderId'] = self.file_folder_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.is_max_compute is not None:
            result['IsMaxCompute'] = self.is_max_compute

        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time

        if self.last_edit_user is not None:
            result['LastEditUser'] = self.last_edit_user

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbsoluteFolderPath') is not None:
            self.absolute_folder_path = m.get('AbsoluteFolderPath')

        if m.get('AutoParsing') is not None:
            self.auto_parsing = m.get('AutoParsing')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CommitStatus') is not None:
            self.commit_status = m.get('CommitStatus')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('FileDescription') is not None:
            self.file_description = m.get('FileDescription')

        if m.get('FileFolderId') is not None:
            self.file_folder_id = m.get('FileFolderId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('IsMaxCompute') is not None:
            self.is_max_compute = m.get('IsMaxCompute')

        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')

        if m.get('LastEditUser') is not None:
            self.last_edit_user = m.get('LastEditUser')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

