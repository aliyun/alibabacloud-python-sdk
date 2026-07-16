# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgenticSpaceRequest(DaraModel):
    def __init__(
        self,
        agentic_space_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
    ):
        # AgenticSpace Id。
        # 
        # This parameter is required.
        self.agentic_space_id = agentic_space_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating or deleting instances, and incurs no fees.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without deleting the instance. The check items include required parameters, request format, service limits, and NAS resource availability. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned, but FileSystemId is empty.
        # - false (default): Sends a normal request and deletes the instance after the check is passed.
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
        if self.agentic_space_id is not None:
            result['AgenticSpaceId'] = self.agentic_space_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticSpaceId') is not None:
            self.agentic_space_id = m.get('AgenticSpaceId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

