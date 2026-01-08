# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageModerationResultRequest(DaraModel):
    def __init__(
        self,
        req_id: str = None,
    ):
        # The ReqId field returned by the asynchronous Image Moderation 2.0 API.
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.req_id is not None:
            result['ReqId'] = self.req_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        return self

