# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCustomerLabelRequest(DaraModel):
    def __init__(
        self,
        endtime: str = None,
        label_series: str = None,
        label_types: List[str] = None,
        organization: str = None,
        pk: int = None,
        start_time: str = None,
        token: str = None,
        user_name: str = None,
    ):
        self.endtime = endtime
        # This parameter is required.
        self.label_series = label_series
        # This parameter is required.
        self.label_types = label_types
        # This parameter is required.
        self.organization = organization
        # This parameter is required.
        self.pk = pk
        self.start_time = start_time
        self.token = token
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endtime is not None:
            result['Endtime'] = self.endtime

        if self.label_series is not None:
            result['LabelSeries'] = self.label_series

        if self.label_types is not None:
            result['LabelTypes'] = self.label_types

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.pk is not None:
            result['PK'] = self.pk

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.token is not None:
            result['Token'] = self.token

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endtime') is not None:
            self.endtime = m.get('Endtime')

        if m.get('LabelSeries') is not None:
            self.label_series = m.get('LabelSeries')

        if m.get('LabelTypes') is not None:
            self.label_types = m.get('LabelTypes')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

