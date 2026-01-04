# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStorageVolumeRequest(DaraModel):
    def __init__(
        self,
        auth_password: str = None,
        auth_protocol: str = None,
        auth_user: str = None,
        description: str = None,
        ens_region_id: str = None,
        gateway_id: str = None,
        is_auth: str = None,
        is_enable: str = None,
        storage_id: str = None,
        volume_name: str = None,
    ):
        # The password of the CHAP protocol.
        self.auth_password = auth_password
        # The authentication protocol. Set the value to **CHAP**.
        self.auth_protocol = auth_protocol
        # The username of the CHAP protocol.
        self.auth_user = auth_user
        # The description of the volume. The description must be 2 to 128 characters in length. The description cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Specifies whether to enable authentication. Valid values:
        # 
        # *   **1**: Authentication is enabled.
        # *   **0** (default): Authentication is disabled.
        self.is_auth = is_auth
        # Indicates whether the volume is enabled. Valid values:
        # 
        # *   **1** (default): The volume is enabled.
        # *   **0**: The volume is disabled.
        self.is_enable = is_enable
        # The ID of the storage medium.
        # 
        # This parameter is required.
        self.storage_id = storage_id
        # The name of the volume. The name must be 2 to 128 characters in length. The name cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.volume_name = volume_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_password is not None:
            result['AuthPassword'] = self.auth_password

        if self.auth_protocol is not None:
            result['AuthProtocol'] = self.auth_protocol

        if self.auth_user is not None:
            result['AuthUser'] = self.auth_user

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.storage_id is not None:
            result['StorageId'] = self.storage_id

        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPassword') is not None:
            self.auth_password = m.get('AuthPassword')

        if m.get('AuthProtocol') is not None:
            self.auth_protocol = m.get('AuthProtocol')

        if m.get('AuthUser') is not None:
            self.auth_user = m.get('AuthUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('StorageId') is not None:
            self.storage_id = m.get('StorageId')

        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')

        return self

