# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataFlowAutoRefreshRequest(DaraModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # The automatic update interval. CPFS checks the directory for data updates at each interval. If data updates exist, an automatic update task is started. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. This policy specifies how data updates from the source are imported to CPFS after the source data is updated. Valid values:
        # 
        # - None: Data updates from the source are not automatically imported to CPFS. You can import source data updates by using a dataflow task.
        # - ImportChanged: Data updates from the source are automatically imported to CPFS.
        self.auto_refresh_policy = auto_refresh_policy
        # Ensures the idempotency of the request. Generate a parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The dataflow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating an instance or incurring fees.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without creating an instance. The check items include whether required parameters are specified, the request format, business limits, and NAS inventory. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but FileSystemId is empty.
        # - false (default): Sends a normal request. After the check succeeds, the instance is directly created.
        self.dry_run = dry_run
        # The file system ID.
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
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval

        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')

        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

