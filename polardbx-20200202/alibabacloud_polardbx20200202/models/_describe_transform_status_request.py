# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTransformStatusRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        query_report: bool = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.query_report = query_report
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.query_report is not None:
            result['QueryReport'] = self.query_report

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('QueryReport') is not None:
            self.query_report = m.get('QueryReport')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

