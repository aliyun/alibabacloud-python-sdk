# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportCalendarRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        months: str = None,
        name: str = None,
        year: int = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.months = months
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.months is not None:
            result['Months'] = self.months

        if self.name is not None:
            result['Name'] = self.name

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Months') is not None:
            self.months = m.get('Months')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

