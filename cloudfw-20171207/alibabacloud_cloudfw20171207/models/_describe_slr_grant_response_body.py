# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlrGrantResponseBody(DaraModel):
    def __init__(
        self,
        is_granted: bool = None,
        request_id: str = None,
        user_type: str = None,
    ):
        self.is_granted = is_granted
        self.request_id = request_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_granted is not None:
            result['IsGranted'] = self.is_granted

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGranted') is not None:
            self.is_granted = m.get('IsGranted')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

