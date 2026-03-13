# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTreeDataResponseBody(DaraModel):
    def __init__(
        self,
        playbooks: str = None,
        request_id: str = None,
    ):
        # The returned information about the playbook. The value is a JSON string.
        self.playbooks = playbooks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbooks is not None:
            result['Playbooks'] = self.playbooks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbooks') is not None:
            self.playbooks = m.get('Playbooks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

