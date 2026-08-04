# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCustomerLabelRequest(DaraModel):
    def __init__(
        self,
        label_series: str = None,
        pk: int = None,
        token: str = None,
    ):
        self.label_series = label_series
        # This parameter is required.
        self.pk = pk
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_series is not None:
            result['LabelSeries'] = self.label_series

        if self.pk is not None:
            result['PK'] = self.pk

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelSeries') is not None:
            self.label_series = m.get('LabelSeries')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

