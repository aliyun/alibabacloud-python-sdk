# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScanResultsByEngineRequest(DaraModel):
    def __init__(
        self,
        baseline_state: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        package_name: str = None,
    ):
        # 按 baseline_state 过滤 findings。值为 new/unchanged/absent/updated 之一。
        self.baseline_state = baseline_state
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_state is not None:
            result['baselineState'] = self.baseline_state

        if self.lang is not None:
            result['lang'] = self.lang

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.package_name is not None:
            result['packageName'] = self.package_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baselineState') is not None:
            self.baseline_state = m.get('baselineState')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('packageName') is not None:
            self.package_name = m.get('packageName')

        return self

