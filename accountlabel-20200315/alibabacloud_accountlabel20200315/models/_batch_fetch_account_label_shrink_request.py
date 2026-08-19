# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchFetchAccountLabelShrinkRequest(DaraModel):
    def __init__(
        self,
        instant: bool = None,
        label_series_list_shrink: str = None,
        organization: str = None,
        pk: int = None,
        token: str = None,
        user_name: str = None,
    ):
        self.instant = instant
        # This parameter is required.
        self.label_series_list_shrink = label_series_list_shrink
        # This parameter is required.
        self.organization = organization
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
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
        if self.instant is not None:
            result['Instant'] = self.instant

        if self.label_series_list_shrink is not None:
            result['LabelSeriesList'] = self.label_series_list_shrink

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.token is not None:
            result['Token'] = self.token

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instant') is not None:
            self.instant = m.get('Instant')

        if m.get('LabelSeriesList') is not None:
            self.label_series_list_shrink = m.get('LabelSeriesList')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

