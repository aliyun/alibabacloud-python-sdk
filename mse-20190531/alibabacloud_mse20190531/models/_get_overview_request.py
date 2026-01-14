# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOverviewRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        period: int = None,
        region: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The query time. Unit: days. For example, if you set this parameter to 30, the governance rules within the last 30 days are queried.
        self.period = period
        # The ID of the region.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.period is not None:
            result['Period'] = self.period

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

