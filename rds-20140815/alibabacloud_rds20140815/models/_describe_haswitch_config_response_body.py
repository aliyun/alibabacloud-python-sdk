# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHASwitchConfigResponseBody(DaraModel):
    def __init__(
        self,
        haconfig: str = None,
        manual_hatime: str = None,
        request_id: str = None,
    ):
        self.haconfig = haconfig
        self.manual_hatime = manual_hatime
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.haconfig is not None:
            result['HAConfig'] = self.haconfig

        if self.manual_hatime is not None:
            result['ManualHATime'] = self.manual_hatime

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAConfig') is not None:
            self.haconfig = m.get('HAConfig')

        if m.get('ManualHATime') is not None:
            self.manual_hatime = m.get('ManualHATime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

