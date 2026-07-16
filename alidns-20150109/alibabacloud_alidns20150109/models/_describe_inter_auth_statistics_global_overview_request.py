# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInterAuthStatisticsGlobalOverviewRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        overview_period: str = None,
        server_region: str = None,
    ):
        # The language of the returned availability zone names. Valid values:
        # 
        # - **zh-CN**: Chinese.
        # 
        # - **en-US** (default): English.
        self.accept_language = accept_language
        # A unique, client-generated token to ensure the idempotence of the request. The token must be a string of ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The statistical period.
        self.overview_period = overview_period
        # The ID of the region.
        self.server_region = server_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.overview_period is not None:
            result['OverviewPeriod'] = self.overview_period

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OverviewPeriod') is not None:
            self.overview_period = m.get('OverviewPeriod')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        return self

