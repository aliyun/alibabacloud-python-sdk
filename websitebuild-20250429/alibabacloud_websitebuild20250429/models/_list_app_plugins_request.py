# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppPluginsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        max_results: int = None,
        next_token: str = None,
        phase: str = None,
        platform: str = None,
    ):
        self.biz_id = biz_id
        self.max_results = max_results
        self.next_token = next_token
        self.phase = phase
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.platform is not None:
            result['Platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        return self

