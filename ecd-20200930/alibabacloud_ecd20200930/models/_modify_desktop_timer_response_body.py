# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopTimerResponseBody(DaraModel):
    def __init__(
        self,
        desktop_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the cloud computers for which you successfully configure the scheduled task.
        self.desktop_ids = desktop_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

