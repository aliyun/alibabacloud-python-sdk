# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        business_info: str = None,
        commodity_code: str = None,
        coupon_no: str = None,
        dbinstances: str = None,
        order_param_out: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The commodity code of the instance. Valid values:
        # 
        # - **dds**: pay-as-you-go ReplicaSet instance.
        # 
        # - **badds**: subscription ReplicaSet instance.
        # 
        # - **dds_sharding**: pay-as-you-go sharded cluster instance.
        # 
        # - **badds_sharding**: subscription sharded cluster instance.
        # 
        # - **badds_sharding_intl**: subscription sharded cluster instance on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        # 
        # - **dds_sharding_intl**: pay-as-you-go sharded cluster instance on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        # 
        # - **badds_sharding_jp**: subscription sharded cluster instance on the Alibaba Cloud Japan Website.
        # 
        # - **badds_intl**: subscription ReplicaSet instance on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        # 
        # - **dds_intl**: pay-as-you-go ReplicaSet instance on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        self.commodity_code = commodity_code
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **default** or **null** (default): A coupon is used.
        # 
        # - **youhuiquan_promotion_option_id_for_blank**: A coupon is not used.
        self.coupon_no = coupon_no
        # A JSON string that contains information about the instance. For more information about the parameters and JSON examples, see [DBInstances parameter of the DescribePrice operation](https://help.aliyun.com/document_detail/197291.html).
        # 
        # This parameter is required.
        self.dbinstances = dbinstances
        # Specifies whether to return the order parameters. Valid values:
        # 
        # - **false** (default): The order parameters are not returned.
        # 
        # - **true**: The order parameters are returned.
        self.order_param_out = order_param_out
        # The order type. Valid values:
        # 
        # - **BUY**: Creates an instance.
        # 
        # - **UPGRADE**: Changes the configuration of an instance.
        # 
        # - **RENEW**: Renews an instance.
        # 
        # This parameter is required.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The product code. The default value is **dds**.
        self.product_code = product_code
        # The region ID. Call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the region ID.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
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
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances

        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

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
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')

        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

