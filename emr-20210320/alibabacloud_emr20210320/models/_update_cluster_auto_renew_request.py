# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class UpdateClusterAutoRenewRequest(DaraModel):
    def __init__(
        self,
        auto_renew_instances: List[main_models.AutoRenewInstance] = None,
        cluster_auto_renew: bool = None,
        cluster_auto_renew_duration: int = None,
        cluster_auto_renew_duration_unit: str = None,
        cluster_id: str = None,
        region_id: str = None,
        renew_all_instances: bool = None,
    ):
        # The list of ECS instances for which to enable auto-renewal. This parameter takes effect only when RenewAllInstances is not set to true.
        self.auto_renew_instances = auto_renew_instances
        # Specifies whether to enable auto-renewal for the cluster. Valid values:
        # 
        # - true: Enables auto-renewal.
        # 
        # - false: Disables auto-renewal.
        # 
        # Default value: false.
        self.cluster_auto_renew = cluster_auto_renew
        # The auto-renewal duration for the cluster. This parameter takes effect only when ClusterAutoRenew is set to true.
        # If ClusterAutoRenewDurationUnit is set to Month, the valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. If ClusterAutoRenewDurationUnit is set to Year, the valid values are 1, 2, and 3.
        self.cluster_auto_renew_duration = cluster_auto_renew_duration
        # The unit of the auto-renewal duration. Valid values:
        # 
        # - Month
        # 
        # - Year
        # 
        # Default value: Month.
        self.cluster_auto_renew_duration_unit = cluster_auto_renew_duration_unit
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable auto-renewal for all ECS instances in the cluster. Valid values:
        # 
        # - true: Enables auto-renewal for all ECS instances in the cluster. The default auto-renewal duration is one month.
        # 
        # - false: Does not enable auto-renewal for all ECS instances in the cluster. You can specify the ECS instances for which to enable auto-renewal in the AutoRenewInstances parameter.
        # 
        # Default value: false.
        self.renew_all_instances = renew_all_instances

    def validate(self):
        if self.auto_renew_instances:
            for v1 in self.auto_renew_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoRenewInstances'] = []
        if self.auto_renew_instances is not None:
            for k1 in self.auto_renew_instances:
                result['AutoRenewInstances'].append(k1.to_map() if k1 else None)

        if self.cluster_auto_renew is not None:
            result['ClusterAutoRenew'] = self.cluster_auto_renew

        if self.cluster_auto_renew_duration is not None:
            result['ClusterAutoRenewDuration'] = self.cluster_auto_renew_duration

        if self.cluster_auto_renew_duration_unit is not None:
            result['ClusterAutoRenewDurationUnit'] = self.cluster_auto_renew_duration_unit

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renew_all_instances is not None:
            result['RenewAllInstances'] = self.renew_all_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_renew_instances = []
        if m.get('AutoRenewInstances') is not None:
            for k1 in m.get('AutoRenewInstances'):
                temp_model = main_models.AutoRenewInstance()
                self.auto_renew_instances.append(temp_model.from_map(k1))

        if m.get('ClusterAutoRenew') is not None:
            self.cluster_auto_renew = m.get('ClusterAutoRenew')

        if m.get('ClusterAutoRenewDuration') is not None:
            self.cluster_auto_renew_duration = m.get('ClusterAutoRenewDuration')

        if m.get('ClusterAutoRenewDurationUnit') is not None:
            self.cluster_auto_renew_duration_unit = m.get('ClusterAutoRenewDurationUnit')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewAllInstances') is not None:
            self.renew_all_instances = m.get('RenewAllInstances')

        return self

