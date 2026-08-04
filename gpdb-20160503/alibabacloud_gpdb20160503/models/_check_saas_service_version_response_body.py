# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSaasServiceVersionResponseBody(DaraModel):
    def __init__(
        self,
        can_upgrade: bool = None,
        message: str = None,
        request_id: str = None,
        service_id: str = None,
    ):
        # Indicates whether the service can be upgraded.
        self.can_upgrade = can_upgrade
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_upgrade is not None:
            result['CanUpgrade'] = self.can_upgrade

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanUpgrade') is not None:
            self.can_upgrade = m.get('CanUpgrade')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        return self

