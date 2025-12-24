# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImagePermissionResponseBody(DaraModel):
    def __init__(
        self,
        ali_uids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the Alibaba Cloud accounts with which the image is shared.
        self.ali_uids = ali_uids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uids is not None:
            result['AliUids'] = self.ali_uids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUids') is not None:
            self.ali_uids = m.get('AliUids')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

