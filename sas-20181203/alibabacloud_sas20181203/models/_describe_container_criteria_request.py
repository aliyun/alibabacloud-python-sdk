# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerCriteriaRequest(DaraModel):
    def __init__(
        self,
        group_field: str = None,
        value: str = None,
    ):
        # The search field. Valid values:
        # - **pod**: pod.
        # - **appName**: application name.
        # - **clusterId**: cluster ID.
        # - **namespace**: namespace.
        # - **image**: image.
        # - **containerScan**: container scan.
        self.group_field = group_field
        # The value of the search field. Fuzzy match is supported for application names, node names, namespaces, cluster names, public IP addresses, pod addresses, regions, pods, instance IDs, cluster IDs, and container IDs.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_field is not None:
            result['GroupField'] = self.group_field

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupField') is not None:
            self.group_field = m.get('GroupField')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

