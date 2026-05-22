# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSitePauseResponseBody(DaraModel):
    def __init__(
        self,
        paused: bool = None,
        request_id: str = None,
    ):
        # Indicates whether ESA is paused on the website. Valid values:
        # 
        # *   true
        # *   false
        self.paused = paused
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paused is not None:
            result['Paused'] = self.paused

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

