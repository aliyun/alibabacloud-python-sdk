# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClassListRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        master_ha: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The commodity code. Valid values:
        # 
        # - polardb_sub: subscription for the Chinese mainland.
        # 
        # - polardb_sub_intl: subscription for regions in Hong Kong (China) and outside the Chinese mainland.
        # 
        # - polardb_payg: pay-as-you-go for the Chinese mainland.
        # 
        # - polardb_payg_intl: pay-as-you-go for regions in Hong Kong (China) and outside the Chinese mainland.
        # 
        # - polardb_sub_jushita: Jushita subscription.
        # 
        # - polardb_payg_jushita: Jushita pay-as-you-go.
        # 
        # - polardb_sub_cainiao: Cainiao subscription.
        # 
        # - polardb_payg_cainiao: Cainiao pay-as-you-go.
        # 
        # > * If you use an Alibaba Cloud China site account, you can view only the commodity codes for the Chinese mainland.
        # >
        # > * If you use an Alibaba Cloud international site account, you can view only the commodity codes for regions outside the Chinese mainland.
        # >
        # > * If you use a Jushita account, you can view only the commodity codes for Jushita.
        # >
        # > * If you use a Cainiao account, you can view only the commodity codes for Cainiao.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The number of nodes. Valid values:
        # 
        # - single: single node.
        # 
        # - cluster: cluster.
        # 
        # - all: single node and cluster.
        self.master_ha = master_ha
        # The order type. Valid values:
        # 
        # - BUY: new purchase.
        # 
        # - UPGRADE: changes the configuration.
        # 
        # - RENEW: renews the instance.
        # 
        # - CONVERT: changes the billing method.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # > This parameter is required if you use an Alibaba Cloud international site account.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.master_ha is not None:
            result['MasterHa'] = self.master_ha

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('MasterHa') is not None:
            self.master_ha = m.get('MasterHa')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

