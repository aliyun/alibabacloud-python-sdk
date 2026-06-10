# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppTemplateDictsRequest(DaraModel):
    def __init__(
        self,
        dict_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # Dictionary type
        self.dict_type = dict_type
        # Number of results per query.  
        # 
        # Valid range: 10 to 100. Default Value: 20.
        self.max_results = max_results
        # Token indicating the start of the next query. This value is empty if there is no next query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dict_type is not None:
            result['DictType'] = self.dict_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DictType') is not None:
            self.dict_type = m.get('DictType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

