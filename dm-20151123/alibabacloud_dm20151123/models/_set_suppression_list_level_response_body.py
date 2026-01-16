# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSuppressionListLevelResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        suppression_list_level: str = None,
    ):
        self.request_id = request_id
        self.suppression_list_level = suppression_list_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suppression_list_level is not None:
            result['SuppressionListLevel'] = self.suppression_list_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuppressionListLevel') is not None:
            self.suppression_list_level = m.get('SuppressionListLevel')

        return self

