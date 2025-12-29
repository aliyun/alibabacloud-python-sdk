# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class GetApplicationLogsOutput(DaraModel):
    def __init__(
        self,
        log_entrys: List[main_models.LogEntry] = None,
        next_offset: int = None,
        request_id: str = None,
    ):
        self.log_entrys = log_entrys
        self.next_offset = next_offset
        self.request_id = request_id

    def validate(self):
        if self.log_entrys:
            for v1 in self.log_entrys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logEntrys'] = []
        if self.log_entrys is not None:
            for k1 in self.log_entrys:
                result['logEntrys'].append(k1.to_map() if k1 else None)

        if self.next_offset is not None:
            result['nextOffset'] = self.next_offset

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_entrys = []
        if m.get('logEntrys') is not None:
            for k1 in m.get('logEntrys'):
                temp_model = main_models.LogEntry()
                self.log_entrys.append(temp_model.from_map(k1))

        if m.get('nextOffset') is not None:
            self.next_offset = m.get('nextOffset')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

