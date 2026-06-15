# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelDataFlowTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        task_id: str = None,
    ):
        # A client-generated token that you can use to ensure the idempotence of the request. The token must be unique across different requests.
        # 
        # The `ClientToken` value must be an ASCII string of 64 characters or less. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the `ClientToken`. The request ID is unique for each request.
        self.client_token = client_token
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run for the request.
        # 
        # A dry run checks for parameter validity and resource availability without actually canceling the task or incurring charges.
        # 
        # Valid values:
        # 
        # - `true`: Performs a dry run. The system checks the request for potential issues, including missing parameters, invalid formats, and service limits. If the check fails, the system returns an error message; otherwise, it returns a success code.
        # 
        # - `false` (default): Sends a normal request. After the request passes the check, the task is canceled.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - For a general-purpose CPFS instance, the ID must start with `cpfs-`, for example, `cpfs-125487****`.
        # 
        # - For a CPFS for AI Computing instance, the ID must start with `bmcpfs-`, for example, `bmcpfs-0015****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The data flow task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

