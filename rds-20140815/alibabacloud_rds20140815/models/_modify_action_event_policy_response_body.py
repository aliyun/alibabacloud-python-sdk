# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyActionEventPolicyResponseBody(DaraModel):
    def __init__(
        self,
        enable_event_log: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # Indicates whether the event history feature is enabled.
        self.enable_event_log = enable_event_log
        # The ID of the region for which the event history feature is enabled or disabled.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_event_log is not None:
            result['EnableEventLog'] = self.enable_event_log

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEventLog') is not None:
            self.enable_event_log = m.get('EnableEventLog')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

