# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClassesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        order_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The commodity code of the instance to query.
        # 
        # <props="china">
        # * **bards**: Pay-as-you-go primary instance.
        # * **rds**: Subscription primary instance.
        # * **rords**: Pay-as-you-go read-only instance.
        # * **rds_rordspre_public_cn**: Subscription read-only instance.
        # 
        # 
        # <props="intl">
        # * **bards_intl**: Pay-as-you-go primary instance.
        # * **rds_intl**: Subscription primary instance.
        # * **rords_intl**: Pay-as-you-go read-only instance.
        # * **rds_rordspre_public_intl**: Subscription read-only instance.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # >This parameter is required when you query the instance type list for read-only instances, which means you set the **CommodityCode** parameter to a commodity code for read-only instances.
        self.dbinstance_id = dbinstance_id
        # The database engine type. Valid values:
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # * **MariaDB**
        self.engine = engine
        # The type of order to query. Valid values:
        # * **BUY**: New purchase.
        # * **UPGRADE**: Configuration change.
        # * **RENEW**: Renewal.
        # * **CONVERT**: Billing method change.
        # 
        # This parameter is required.
        self.order_type = order_type
        self.owner_id = owner_id
        # The region ID. You can call DescribeRegions to obtain the region ID.
        # >This parameter is required if you use an Alibaba Cloud International Website account.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

