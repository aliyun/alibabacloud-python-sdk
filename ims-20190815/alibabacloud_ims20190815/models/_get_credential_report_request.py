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
        # The number of entries per page. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be true.
        # 
        # Valid values: 1 to 3501. Default value: 3501.
        self.max_items = max_items
        # The token that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.``
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

