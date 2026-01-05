# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAScriptsRequest(DaraModel):
    def __init__(
        self,
        ascript_ids: List[str] = None,
        ascript_names: List[str] = None,
        listener_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The AScript rule IDs. You can specify at most 20 IDs in each call.
        self.ascript_ids = ascript_ids
        # The AScript rule names. You can specify at most 10 names in each call.
        self.ascript_names = ascript_names
        # The listener IDs. You can specify at most 20 listener IDs in each call.
        self.listener_ids = listener_ids
        # The maximum number of entries to return.
        # 
        # Valid values: **1** to **100**.
        # 
        # Default value: **20**. If you do not specify this parameter, the default value is used.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.****
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascript_ids is not None:
            result['AScriptIds'] = self.ascript_ids

        if self.ascript_names is not None:
            result['AScriptNames'] = self.ascript_names

        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AScriptIds') is not None:
            self.ascript_ids = m.get('AScriptIds')

        if m.get('AScriptNames') is not None:
            self.ascript_names = m.get('AScriptNames')

        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

