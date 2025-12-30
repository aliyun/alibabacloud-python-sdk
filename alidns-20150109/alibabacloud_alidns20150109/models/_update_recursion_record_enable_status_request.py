# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionRecordEnableStatusRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable_status: str = None,
        record_id: str = None,
    ):
        self.client_token = client_token
        self.enable_status = enable_status
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        return self

