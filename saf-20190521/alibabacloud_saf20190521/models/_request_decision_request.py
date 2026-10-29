# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RequestDecisionRequest(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        service_parameters: str = None,
    ):
        # The event code.
        self.event_code = event_code
        # The service input parameters. The value is a complete JSON string.
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

