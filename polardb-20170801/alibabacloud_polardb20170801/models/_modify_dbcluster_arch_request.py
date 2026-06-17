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
        self.auto_use_coupon = auto_use_coupon
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable a hot standby cluster. Valid values:
        # 
        # - **on**: Enables a hot standby cluster.
        # 
        # - **equal**: Enables a peer cluster.
        self.hot_standby_cluster = hot_standby_cluster
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # > For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/98041.html).
        self.region_id = region_id
        # The zone for the hot standby storage cluster. Valid values:
        # 
        # - **auto** (default): The system automatically selects a zone.
        # 
        # > The default value is valid only when \\`HotStandbyCluster\\` is set to \\`on\\`. A specific zone is required when \\`HotStandbyCluster\\` is set to \\`equal\\`. For more information about zones, see [DescribeZones](https://help.aliyun.com/document_detail/98041.html).
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

