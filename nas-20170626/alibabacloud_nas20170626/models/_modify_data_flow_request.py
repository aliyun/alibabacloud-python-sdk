# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataFlowRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        throughput: int = None,
    ):
        # Ensures the idempotency of the request. Generate a parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # The description of the data flow. 
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter and cannot start with http:// or https://.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a check request without creating the instance. The check items include whether required parameters are specified, the request format, business limitations, and NAS inventory. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned, but FileSystemId is empty.
        # - false (default): Sends a normal request. After the check passes, the instance is directly created.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum transmission bandwidth of the data flow. Unit: MB/s.
        # Valid values: 
        # 
        # - 600
        # - 1200
        # - 1500
        # 
        # > The transmission bandwidth of the data flow must be less than the I/O bandwidth of the file system. This parameter is required when the file system type is CPFS.
        self.throughput = throughput

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

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        return self

