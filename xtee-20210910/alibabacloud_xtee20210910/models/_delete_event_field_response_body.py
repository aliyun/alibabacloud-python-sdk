# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEventFieldResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resule_object: bool = None,
    ):
        # ID of the request
        self.request_id = request_id
        # Result object
        self.resule_object = resule_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resule_object is not None:
            result['resuleObject'] = self.resule_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resuleObject') is not None:
            self.resule_object = m.get('resuleObject')

        return self

