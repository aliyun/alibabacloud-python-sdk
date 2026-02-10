# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyScheduleConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        request_id: str = None,
    ):
        # The configuration time. Unit: hours.
        # 
        # >  A value **0** indicates that asset fingerprint collection is disabled for this type of asset.
        self.config = config
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

