# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageResultExtRequest(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        req_id: str = None,
    ):
        # The content of the information to be obtained. Multiple values are separated by commas.
        self.info_type = info_type
        # The reqId field returned by the Url Async Moderation API.
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_type is not None:
            result['InfoType'] = self.info_type

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        return self

