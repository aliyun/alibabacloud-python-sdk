# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUnknownThreatDetectProcessRequest(DaraModel):
    def __init__(
        self,
        process_id: str = None,
        remark: str = None,
    ):
        # The process ID.
        self.process_id = process_id
        # The remark for the process.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

