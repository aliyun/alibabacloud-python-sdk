# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrometheusAlertRulesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        match_expressions: str = None,
        name: str = None,
        region_id: str = None,
        status: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.match_expressions = match_expressions
        self.name = name
        # This parameter is required.
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

