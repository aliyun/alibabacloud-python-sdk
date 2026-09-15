# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerGroupedFieldDetailRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        group_field: str = None,
    ):
        # The conditions for searching assets. This parameter is in JSON format. Separate multiple conditions with commas (,). Example: `[{"name":"riskStatus","value":"YES"},{"name":"riskLevel","value":"2"}]`.
        # > You can search for assets by conditions such as instance ID, instance name, VPC ID, region, and public IP address. Call [DescribeCriteria](~~DescribeCriteria~~) to query the supported search conditions.
        # 
        # This parameter is required.
        self.criteria = criteria
        # The search item. Valid values:
        # - **pod**: pod.
        # - **appName**: application name.
        # - **clusterId**: cluster ID.
        # - **namespace**: namespace.
        # - **image**: image.
        # - **containerScan**: container scan.
        # 
        # This parameter is required.
        self.group_field = group_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.group_field is not None:
            result['GroupField'] = self.group_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('GroupField') is not None:
            self.group_field = m.get('GroupField')

        return self

