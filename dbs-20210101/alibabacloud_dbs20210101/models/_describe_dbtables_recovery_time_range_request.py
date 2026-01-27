# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBTablesRecoveryTimeRangeRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        instance_id: str = None,
        region_code: str = None,
    ):
        self.cluster_name = cluster_name
        self.instance_id = instance_id
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        return self

