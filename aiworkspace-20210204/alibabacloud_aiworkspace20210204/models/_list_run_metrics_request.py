# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRunMetricsRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        max_results: int = None,
        page_token: int = None,
    ):
        # The metric key of the run.
        # 
        # This parameter is required.
        self.key = key
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.page_token is not None:
            result['PageToken'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')

        return self

