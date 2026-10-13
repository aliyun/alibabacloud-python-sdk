# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelDataFlowAutoRefreshRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_flow_id: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        refresh_path: str = None,
    ):
        # Ensures the idempotence of the request. Generate a unique parameter value from your client to ensure that the value is unique among different requests.
        # 
        # The value of ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The data flow ID.
        # 
        # This parameter is required.
        self.data_flow_id = data_flow_id
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating the instance or incurring fees.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without creating the data flow. The dry run checks whether required parameters are specified, whether the request format is valid, and whether business dependencies are met. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but DataFlowId is empty.
        # - false (default): Sends a normal request. After the check succeeds, the instance is directly created.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directory for which you want to cancel the automatic update configuration.
        # 
        # Limits:
        # 
        # - The length must be 2 to 1,024 characters.
        # - The value must be encoded in UTF-8.
        # - The value must start and end with a forward slash (/).
        # 
        # > The directory must be an existing directory in CPFS and must be in a fileset for which data flow is enabled.
        # 
        # This parameter is required.
        self.refresh_path = refresh_path

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

        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path

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

        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')

        return self

