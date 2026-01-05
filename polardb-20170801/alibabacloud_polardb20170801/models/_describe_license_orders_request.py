# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLicenseOrdersRequest(DaraModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
        purchase_channel: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        virtual_order: bool = None,
    ):
        # The ID of the Alibaba Cloud order. The value can be the ID of a virtual order.
        self.aliyun_order_id = aliyun_order_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The plan type. Valid values:
        # 
        # *   single_node_subscribe: Single-node Edition (Subscription).
        # *   single_node_long_term: Single-node Edition (Long-term).
        # *   primary_backup_subscribe: HA Edition (Subscription).
        # *   primary_backup_long_term: HA Edition (Long-term).
        # *   pre_generation_long_term: Pre-generated (Long-term).
        self.package_type = package_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The purchase channel. Valid values: aliyun_market and aliyun_public. aliyun_market specifies Alibaba Cloud Marketplace. aliyun_public specifies the PolarDB buy page.
        self.purchase_channel = purchase_channel
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to query only virtual orders.
        self.virtual_order = virtual_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.purchase_channel is not None:
            result['PurchaseChannel'] = self.purchase_channel

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.virtual_order is not None:
            result['VirtualOrder'] = self.virtual_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PurchaseChannel') is not None:
            self.purchase_channel = m.get('PurchaseChannel')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VirtualOrder') is not None:
            self.virtual_order = m.get('VirtualOrder')

        return self

