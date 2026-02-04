# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomFieldResponseBody(DaraModel):
    def __init__(
        self,
        field_id: str = None,
        request_id: str = None,
    ):
        self.field_id = field_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

