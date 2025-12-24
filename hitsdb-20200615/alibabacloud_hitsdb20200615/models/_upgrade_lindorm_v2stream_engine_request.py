# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeLindormV2StreamEngineRequest(DaraModel):
    def __init__(
        self,
        custom_config: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        quantity: int = None,
        resource_group_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        spec: str = None,
        spec_id: str = None,
        upgrade_type: str = None,
    ):
        self.custom_config = custom_config
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.quantity = quantity
        self.resource_group_name = resource_group_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is required.
        self.spec = spec
        # This parameter is required.
        self.spec_id = spec_id
        # This parameter is required.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['CustomConfig'] = self.custom_config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomConfig') is not None:
            self.custom_config = m.get('CustomConfig')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        return self

