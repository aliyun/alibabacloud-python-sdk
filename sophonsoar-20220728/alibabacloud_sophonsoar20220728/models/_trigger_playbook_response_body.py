# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trigger_uuid: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The running UUID of the playbook. This parameter is used to query the running result of the playbook.
        self.trigger_uuid = trigger_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trigger_uuid is not None:
            result['TriggerUuid'] = self.trigger_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TriggerUuid') is not None:
            self.trigger_uuid = m.get('TriggerUuid')

        return self

