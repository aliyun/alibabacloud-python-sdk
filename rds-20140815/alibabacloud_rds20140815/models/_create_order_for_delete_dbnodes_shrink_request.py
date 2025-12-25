# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrderForDeleteDBNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        commodity_code: str = None,
        dbinstance_id: str = None,
        dbnode_id_shrink: str = None,
        engine_version: str = None,
        node_type: str = None,
        owner_id: int = None,
        promotion_code: str = None,
        region_id: str = None,
        resource: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # 1.  **true**: You must make sure that your account balance is sufficient.
        # 2.  **false**: An unpaid order is generated.
        # 
        # >  Default value: true. If your account balance is insufficient, you can set the AutoPay parameter to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # The additional business information about the instance.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The commodity code. Valid values:
        # 
        # *   **bards**: The instance is a pay-as-you-go primary instance.
        # *   **rds**: The instance is a subscription primary instance.
        # *   **rords**: The instance is a pay-as-you-go read-only instance.
        # *   **rds_rordspre_public_cn**: The instance is a subscription read-only instance.
        # *   **bards_intl**: The instance is a pay-as-you-go primary instance.
        # *   **rds_intl**: The instance is a subscription primary instance.
        # *   **rords_intl**: The instance is a pay-as-you-go read-only instance.
        # *   **rds_rordspre_public_intl**: The instance is a subscription read-only instance.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) operation to query the ID of the instance.
        self.dbinstance_id = dbinstance_id
        # An array that consists of information about the ID of the node.
        self.dbnode_id_shrink = dbnode_id_shrink
        # The database engine version of the instance. Valid values:
        # 
        # Valid values if you set Engine to MySQL: **5.5, 5.6, 5.7, and 8.0**
        self.engine_version = engine_version
        # The type of the database node. Valid values:
        # 
        # *   **Master**: the primary node
        # *   **Slave**: the secondary node
        self.node_type = node_type
        self.owner_id = owner_id
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the most recent region list.
        self.region_id = region_id
        # The resources.
        self.resource = resource
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbnode_id_shrink is not None:
            result['DBNodeId'] = self.dbnode_id_shrink

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id_shrink = m.get('DBNodeId')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

