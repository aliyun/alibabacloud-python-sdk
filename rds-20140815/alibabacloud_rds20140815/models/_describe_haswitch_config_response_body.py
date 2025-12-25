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
        # The status of the automatic primary/secondary switchover feature. Valid values:
        # 
        # *   **Auto:** The automatic primary/secondary switchover feature is enabled. The system automatically switches your workloads over from the instance to its secondary instance in the event of a fault.
        # *   **Manual:** The automatic primary/secondary switchover feature is temporarily disabled.
        self.haconfig = haconfig
        # The time when the automatic primary/secondary switchover feature is enabled again. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.manual_hatime = manual_hatime
        # The ID of the request.
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

