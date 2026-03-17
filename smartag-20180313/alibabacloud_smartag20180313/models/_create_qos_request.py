# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQosRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        qos_description: str = None,
        qos_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the QoS policy.
        # 
        # The description must be 1 to 512 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.qos_description = qos_description
        # The name of the QoS policy.
        # 
        # The name must be 2 to 100 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        # 
        # This parameter is required.
        self.qos_name = qos_name
        # The ID of the region where the QoS policy is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qos_description is not None:
            result['QosDescription'] = self.qos_description

        if self.qos_name is not None:
            result['QosName'] = self.qos_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QosDescription') is not None:
            self.qos_description = m.get('QosDescription')

        if m.get('QosName') is not None:
            self.qos_name = m.get('QosName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

