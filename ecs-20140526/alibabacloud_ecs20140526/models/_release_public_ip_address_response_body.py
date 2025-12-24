# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleasePublicIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        remain_times: str = None,
        request_id: str = None,
    ):
        # > This parameter is unavailable.
        self.remain_times = remain_times
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remain_times is not None:
            result['RemainTimes'] = self.remain_times

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainTimes') is not None:
            self.remain_times = m.get('RemainTimes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

