# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProtocolServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_service_id: str = None,
    ):
        # Ensures the idempotency of the request. Generate a value from your client that is unique across different requests.
        # 
        # The ClientToken value supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary across API requests.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this request. A dry run checks parameter validity and dependencies without actually modifying the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without modifying the protocol service. The check items include whether required parameters are specified, the request format, and business limit dependencies. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # - false (default): Sends a normal request. After the check passes, the protocol service is directly modified.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The protocol service ID.
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

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        return self

