# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteServiceRecordRequest(DaraModel):
    def __init__(
        self,
        record_type: str = None,
    ):
        # The type of the association entry. Valid values:
        # logCorrelation: application log association
        # 
        # This parameter is required.
        self.record_type = record_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_type is not None:
            result['recordType'] = self.record_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        return self

