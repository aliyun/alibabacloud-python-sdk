# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySessionByClientIdResponseBody(DaraModel):
    def __init__(
        self,
        online_status: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the ApsaraMQ for MQTT client is connected to the ApsaraMQ for MQTT broker. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.online_status = online_status
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

