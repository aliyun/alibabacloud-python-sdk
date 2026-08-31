# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelDataFlowSubTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        data_flow_sub_task_id: str = None,
        data_flow_task_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The data flow streaming subtask ID.
        # 
        # This parameter is required.
        self.data_flow_sub_task_id = data_flow_sub_task_id
        # The data flow task ID.
        # 
        # This parameter is required.
        self.data_flow_task_id = data_flow_task_id
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating an instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without creating an instance. The check items include required parameters, request format, business limits, and NAS inventory. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # - false (default): Sends a normal request and creates the instance after the check passes.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # > Only CPFS for Lingjun (with the bmcpfs- prefix) file systems of version 2.6.0 or later are supported.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.data_flow_sub_task_id is not None:
            result['DataFlowSubTaskId'] = self.data_flow_sub_task_id

        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DataFlowSubTaskId') is not None:
            self.data_flow_sub_task_id = m.get('DataFlowSubTaskId')

        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

