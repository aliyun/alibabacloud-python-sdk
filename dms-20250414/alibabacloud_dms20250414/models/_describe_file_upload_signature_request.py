# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFileUploadSignatureRequest(DaraModel):
    def __init__(
        self,
        call_from: str = None,
        dms_unit: str = None,
    ):
        self.call_from = call_from
        self.dms_unit = dms_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_from is not None:
            result['CallFrom'] = self.call_from

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrom') is not None:
            self.call_from = m.get('CallFrom')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        return self

