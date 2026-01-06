# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetModifyBEClusterInquiryRequest(DaraModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        cluster_id: str = None,
        commodity_code: str = None,
        compute_size: int = None,
        db_instance_id: str = None,
        modify_cluster_charge_type: bool = None,
        pre_cache_size: int = None,
        pre_compute_size: int = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The size of the elastic cache.
        self.cache_size = cache_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The cluster ID.
        self.cluster_id = cluster_id
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   selectdb_pre_public_intl: subscription commodity on the international site (alibabacloud.com)
        # *   selectdb_go_public_cn: pay-as-you-go commodity on the China site (aliyun.com)
        # *   selectdb_go_public_intl: pay-as-you-go commodity on the international site (alibabacloud.com)
        # *   selectdb_pre_public_cn: subscription commodity on the China site (aliyun.com)
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The number of elastic CPU cores.
        self.compute_size = compute_size
        # The instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # Specifies whether to change the billing method of the cluster.
        self.modify_cluster_charge_type = modify_cluster_charge_type
        # The size of the reserved cache.
        self.pre_cache_size = pre_cache_size
        # The number of reserved CPU cores.
        self.pre_compute_size = pre_compute_size
        # The billing cycle.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Minute
        # *   Hour
        # *   Day
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        self.promotion_option_no = promotion_option_no
        # The number of clusters whose specifications are to be changed.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.compute_size is not None:
            result['ComputeSize'] = self.compute_size

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.modify_cluster_charge_type is not None:
            result['ModifyClusterChargeType'] = self.modify_cluster_charge_type

        if self.pre_cache_size is not None:
            result['PreCacheSize'] = self.pre_cache_size

        if self.pre_compute_size is not None:
            result['PreComputeSize'] = self.pre_compute_size

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComputeSize') is not None:
            self.compute_size = m.get('ComputeSize')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('ModifyClusterChargeType') is not None:
            self.modify_cluster_charge_type = m.get('ModifyClusterChargeType')

        if m.get('PreCacheSize') is not None:
            self.pre_cache_size = m.get('PreCacheSize')

        if m.get('PreComputeSize') is not None:
            self.pre_compute_size = m.get('PreComputeSize')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

