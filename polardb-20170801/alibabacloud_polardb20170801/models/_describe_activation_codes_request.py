# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActivationCodesRequest(DaraModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        mac_address: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        system_identifier: str = None,
    ):
        # The ID of the Alibaba Cloud order. The value can be the ID of a virtual order.
        # 
        # This parameter is required.
        self.aliyun_order_id = aliyun_order_id
        self.mac_address = mac_address
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SystemIdentifier') is not None:
            self.system_identifier = m.get('SystemIdentifier')

        return self

