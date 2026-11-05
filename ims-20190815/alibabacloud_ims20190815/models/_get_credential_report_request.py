# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCredentialReportRequest(DaraModel):
    def __init__(
        self,
        max_items: str = None,
        next_token: str = None,
    ):
        # The maximum number of items to return. When the response is truncated because the maximum number of items is reached, the IsTruncated parameter is set to true.
        # 
        # Valid values: 1 to 3501. Default value: 3501.
        self.max_items = max_items
        # The token used to retrieve the next set of results when the response is truncated.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_items is not None:
            result['MaxItems'] = self.max_items

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

