# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportPrometheusRulesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        content: str = None,
        name: str = None,
        name_space: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.name_space = name_space
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.content is not None:
            result['Content'] = self.content

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

