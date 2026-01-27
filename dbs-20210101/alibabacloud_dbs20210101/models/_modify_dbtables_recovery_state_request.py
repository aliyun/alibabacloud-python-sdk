# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBTablesRecoveryStateRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        cluster_name: str = None,
        instance_id: str = None,
        region_code: str = None,
        retention: str = None,
    ):
        self.category = category
        self.cluster_name = cluster_name
        self.instance_id = instance_id
        self.region_code = region_code
        self.retention = retention

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.retention is not None:
            result['Retention'] = self.retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        return self

