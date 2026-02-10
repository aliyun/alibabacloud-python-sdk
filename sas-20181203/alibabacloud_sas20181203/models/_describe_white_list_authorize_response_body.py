# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListAuthorizeResponseBody(DaraModel):
    def __init__(
        self,
        available_authorize_num: int = None,
        request_id: str = None,
    ):
        # The available quota.
        self.available_authorize_num = available_authorize_num
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_authorize_num is not None:
            result['AvailableAuthorizeNum'] = self.available_authorize_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAuthorizeNum') is not None:
            self.available_authorize_num = m.get('AvailableAuthorizeNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

