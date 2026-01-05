# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateActivationCodeRequest(DaraModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        description: str = None,
        mac_address: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        system_identifier: str = None,
    ):
        # The Alibaba Cloud order ID (including the virtual order ID).
        # 
        # This parameter is required.
        self.aliyun_order_id = aliyun_order_id
        # The description of the activation code.
        self.description = description
        # The MAC address.
        # 
        # This parameter is required.
        self.mac_address = mac_address
        # The name of the activation code. The name can contain only letters, digits, underscores (_), and hyphens (-). The activation code file downloaded from the console is named based on this name.
        # 
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The system identifier of the database. This parameter is required if you set AllowEmptySystemIdentifier to false.
        self.system_identifier = system_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id

        if self.description is not None:
            result['Description'] = self.description

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.system_identifier is not None:
            result['SystemIdentifier'] = self.system_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SystemIdentifier') is not None:
            self.system_identifier = m.get('SystemIdentifier')

        return self

