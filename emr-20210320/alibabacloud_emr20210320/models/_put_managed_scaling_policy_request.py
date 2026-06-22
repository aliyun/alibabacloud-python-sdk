# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class PutManagedScalingPolicyRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.ManagedScalingConstraints = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The maximum and minimum value constraints for the cluster.
        self.constraints = constraints
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.constraints:
            self.constraints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Constraints') is not None:
            temp_model = main_models.ManagedScalingConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

