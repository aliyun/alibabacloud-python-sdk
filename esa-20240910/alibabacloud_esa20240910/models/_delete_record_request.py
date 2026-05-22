# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRecordRequest(DaraModel):
    def __init__(
        self,
        record_id: int = None,
        security_token: str = None,
    ):
        # The record ID, which can be obtained by calling [ListRecords](https://help.aliyun.com/document_detail/2850265.html).
        # 
        # This parameter is required.
        self.record_id = record_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

