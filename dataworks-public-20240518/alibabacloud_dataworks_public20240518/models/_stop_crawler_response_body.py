# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopCrawlerResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
        stop_accepted: bool = None,
        success: bool = None,
    ):
        self.id = id
        self.request_id = request_id
        self.stop_accepted = stop_accepted
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stop_accepted is not None:
            result['StopAccepted'] = self.stop_accepted

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StopAccepted') is not None:
            self.stop_accepted = m.get('StopAccepted')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

