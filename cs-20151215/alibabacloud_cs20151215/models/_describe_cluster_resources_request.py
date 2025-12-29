# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterResourcesRequest(DaraModel):
    def __init__(
        self,
        with_addon_resources: bool = None,
    ):
        # Specifies whether to query the resources created by cluster components.
        self.with_addon_resources = with_addon_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_addon_resources is not None:
            result['with_addon_resources'] = self.with_addon_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('with_addon_resources') is not None:
            self.with_addon_resources = m.get('with_addon_resources')

        return self

