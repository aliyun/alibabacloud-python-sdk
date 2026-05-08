# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterPayTypeRequest(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        used_time: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.db_cluster_id = db_cluster_id
        # The billing method of the cluster. Valid values:
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription type of the subscription cluster. Valid values:
        # 
        # *   **Year**: subscription on a yearly basis.
        # *   **Month**: subscription on a monthly basis.
        # 
        # >  This parameter must be specified when PayType is set to Prepaid.
        self.period = period
        # The order ID.
        self.region_id = region_id
        # The subscription period of the subscription cluster.
        # 
        # *   Valid values when Period is set to Year: 1, 2, and 3 (integer)
        # *   Valid values when Period is set to Month: 1 to 9 (integer)
        # 
        # > * This parameter is required if the PayType parameter is set to Prepaid.
        # > * Longer subscription periods offer more savings. Purchasing a cluster for one year is more cost-effective than purchasing the cluster for 10 or 11 months.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

