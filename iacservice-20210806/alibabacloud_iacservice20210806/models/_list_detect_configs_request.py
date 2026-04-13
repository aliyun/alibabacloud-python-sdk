# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDetectConfigsRequest(DaraModel):
    def __init__(
        self,
        detect_config_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.detect_config_name = detect_config_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_config_name is not None:
            result['detectConfigName'] = self.detect_config_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detectConfigName') is not None:
            self.detect_config_name = m.get('detectConfigName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

