# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProtocolMountTargetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        export_id: str = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # Ensures the idempotence of the request. Generate a value from your client that is unique among different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this delete request.
        # A dry run checks parameter validity and dependencies without actually deleting the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without deleting the export directory. The dry run checks whether required parameters are specified, whether the request format is valid, and whether business limit dependencies are met. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # 
        # - false (default): Sends a normal request. After the check passes, the instance is directly deleted.
        self.dry_run = dry_run
        # The ID of the export directory.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the protocol service.
        # 
        # This parameter is required.
        self.protocol_service_id = protocol_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        return self

