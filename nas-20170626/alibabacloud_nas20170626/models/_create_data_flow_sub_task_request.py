# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateDataFlowSubTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        condition: main_models.CreateDataFlowSubTaskRequestCondition = None,
        data_flow_id: str = None,
        data_flow_task_id: str = None,
        dry_run: bool = None,
        dst_file_path: str = None,
        file_system_id: str = None,
        src_file_path: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The check conditions. The check must be passed after the following conditions are specified.
        self.condition = condition
        # The ID of the data flow.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The ID of the data flow task.
        # 
        # >  Only the IDs of data streaming tasks are supported.
        # 
        # This parameter is required.
        self.data_flow_task_id = data_flow_task_id
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no data streaming subtask is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the DataFlowSubTaskId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a data streaming subtask is created.
        self.dry_run = dry_run
        # The path of the destination file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        # 
        # This parameter is required.
        self.dst_file_path = dst_file_path
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The path of the source file. Limits:
        # 
        # *   The path must be 1 to 1,023 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start with a forward slash (/).
        # *   The path must end with the file name.
        # 
        # This parameter is required.
        self.src_file_path = src_file_path

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dst_file_path is not None:
            result['DstFilePath'] = self.dst_file_path

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.src_file_path is not None:
            result['SrcFilePath'] = self.src_file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Condition') is not None:
            temp_model = main_models.CreateDataFlowSubTaskRequestCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DstFilePath') is not None:
            self.dst_file_path = m.get('DstFilePath')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('SrcFilePath') is not None:
            self.src_file_path = m.get('SrcFilePath')

        return self

class CreateDataFlowSubTaskRequestCondition(DaraModel):
    def __init__(
        self,
        modify_time: int = None,
        size: int = None,
    ):
        # The modification time. The value must be a UNIX timestamp. Unit: ns.
        self.modify_time = modify_time
        # The file size. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

