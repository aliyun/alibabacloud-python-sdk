# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQualityDistributionStatDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        stat_dim: str = None,
    ):
        # APP ID
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.start_date = start_date
        # This parameter is required.
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')

        return self

