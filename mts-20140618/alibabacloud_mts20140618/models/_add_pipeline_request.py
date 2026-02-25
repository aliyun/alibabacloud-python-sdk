# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPipelineRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        notify_config: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
        speed: str = None,
        speed_level: int = None,
    ):
        # The name of the MPS queue. The name can be up to 128 bytes in size.
        # 
        # This parameter is required.
        self.name = name
        # The Message Service (MNS) configuration.
        self.notify_config = notify_config
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role.
        self.role = role
        # The type of the MPS queue. Valid values:
        # 
        # *   **Boost**: MPS queue with transcoding speed boosted.
        # *   **Standard**: standard MPS queue.
        # *   **NarrowBandHDV2**: MPS queue that supports Narrowband HD 2.0.
        # *   **AIVideoCover**: MPS queue for intelligent snapshot capture.
        # *   **AIVideoTag**: MPS queue for video tagging. The supported regions are China (Shanghai), China (Beijing), and China (Hangzhou).
        # 
        # Default value: **Standard**.
        self.speed = speed
        # The level of the MPS queue. Valid values: **1 to 3**.
        self.speed_level = speed_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.notify_config is not None:
            result['NotifyConfig'] = self.notify_config

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role is not None:
            result['Role'] = self.role

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.speed_level is not None:
            result['SpeedLevel'] = self.speed_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyConfig') is not None:
            self.notify_config = m.get('NotifyConfig')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('SpeedLevel') is not None:
            self.speed_level = m.get('SpeedLevel')

        return self

