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
        # The search conditions that are used to query assets. The value of this parameter is in the JSON format. Separate multiple search conditions with commas (,). Example: `[{"name":"riskStatus","value":"YES"},{"name":"riskLevel","value":"2"}]`.
        # 
        # >  Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        # 
        # This parameter is required.
        self.criteria = criteria
        # The filter condition for a grouping and aggregation query. Valid values:
        # 
        # *   **pod**
        # *   **appName**
        # *   **clusterId**
        # *   **namespace**
        # *   **image**
        # *   **containerScan**
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

