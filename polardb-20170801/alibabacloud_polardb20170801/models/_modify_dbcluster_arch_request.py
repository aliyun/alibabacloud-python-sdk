# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterArchRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        dbcluster_id: str = None,
        hot_standby_cluster: str = None,
        promotion_code: str = None,
        region_id: str = None,
        standby_az: str = None,
    ):
        # Specifies whether to automatically use coupons. Valid values:
        # * true (default): Uses coupons.
        # * false: Does not use coupons.
        self.auto_use_coupon = auto_use_coupon
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the hot standby cluster. Valid values:
        # 
        # - **on**: Enables the hot standby cluster.
        # - **equal**: Enables the peer cluster.
        self.hot_standby_cluster = hot_standby_cluster
        # The coupon code. If this parameter is not specified, the default coupon is used.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query region information.
        self.region_id = region_id
        # The zone of the hot standby storage cluster. Valid values:
        # 
        # - **auto** (default): Automatically selected.
        # > When the HotStandbyCluster parameter is set to on, you can use the default value. When the HotStandbyCluster parameter is set to equal, you must specify a specific zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/98041.html) operation to query zone details.
        self.standby_az = standby_az

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.hot_standby_cluster is not None:
            result['HotStandbyCluster'] = self.hot_standby_cluster

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.standby_az is not None:
            result['StandbyAZ'] = self.standby_az

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('HotStandbyCluster') is not None:
            self.hot_standby_cluster = m.get('HotStandbyCluster')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StandbyAZ') is not None:
            self.standby_az = m.get('StandbyAZ')

        return self

