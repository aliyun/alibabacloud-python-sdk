# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDomainQuotaResponseBody(DaraModel):
    def __init__(
        self,
        size_quota: int = None,
        size_used: int = None,
        user_count_quota: int = None,
        user_count_used: int = None,
    ):
        self.size_quota = size_quota
        self.size_used = size_used
        self.user_count_quota = user_count_quota
        self.user_count_used = user_count_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota

        if self.size_used is not None:
            result['size_used'] = self.size_used

        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota

        if self.user_count_used is not None:
            result['user_count_used'] = self.user_count_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')

        if m.get('size_used') is not None:
            self.size_used = m.get('size_used')

        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')

        if m.get('user_count_used') is not None:
            self.user_count_used = m.get('user_count_used')

        return self

