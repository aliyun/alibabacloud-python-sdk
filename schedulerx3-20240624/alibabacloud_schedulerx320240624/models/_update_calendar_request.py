# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCalendarRequest(DaraModel):
    def __init__(
        self,
        calendar_name: str = None,
        client_token: str = None,
        cluster_id: str = None,
        incremental: bool = None,
        months: str = None,
        year: int = None,
    ):
        # This parameter is required.
        self.calendar_name = calendar_name
        self.client_token = client_token
        # This parameter is required.
        self.cluster_id = cluster_id
        self.incremental = incremental
        # This parameter is required.
        self.months = months
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_name is not None:
            result['CalendarName'] = self.calendar_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.incremental is not None:
            result['Incremental'] = self.incremental

        if self.months is not None:
            result['Months'] = self.months

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarName') is not None:
            self.calendar_name = m.get('CalendarName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Incremental') is not None:
            self.incremental = m.get('Incremental')

        if m.get('Months') is not None:
            self.months = m.get('Months')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

