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
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The verification condition. The specified conditions must pass verification.
        self.condition = condition
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The data flow task ID.
        # >Only data flow streaming task IDs are supported.
        # 
        # This parameter is required.
        self.data_flow_task_id = data_flow_task_id
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a check request without creating the data flow. The check items include whether required parameters are specified, the request format, and business limit dependencies. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned, but DataFlowSubTaskId is empty.
        # - false (default): Sends a normal request and directly creates the instance after the check passes.
        self.dry_run = dry_run
        # The destination file path.
        # Limits:
        # - The value must be 1 to 1,023 characters in length.
        # - The value must be encoded in UTF-8.
        # - The value must start with a forward slash (/).
        # - The value must end with a file name.
        # 
        # This parameter is required.
        self.dst_file_path = dst_file_path
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The source file path.
        # Limits:
        # - The value must be 1 to 1,023 characters in length.
        # - The value must be encoded in UTF-8.
        # - The value must start with a forward slash (/).
        # - The value must end with a file name.
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
        # The modification time as a UNIX timestamp. Unit: ns.
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

