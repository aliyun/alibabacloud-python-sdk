# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMachineCanRebootResponseBody(DaraModel):
    def __init__(
        self,
        can_reboot: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the server can be restarted. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.can_reboot = can_reboot
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_reboot is not None:
            result['CanReboot'] = self.can_reboot

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanReboot') is not None:
            self.can_reboot = m.get('CanReboot')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

