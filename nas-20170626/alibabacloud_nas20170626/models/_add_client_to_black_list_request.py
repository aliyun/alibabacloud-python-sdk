# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddClientToBlackListRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        client_token: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The IP address of the client to add.
        # 
        # This parameter is required.
        self.client_ip = client_ip
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the region where the file system resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

