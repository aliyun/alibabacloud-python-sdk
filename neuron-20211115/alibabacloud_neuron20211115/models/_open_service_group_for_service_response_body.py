# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OpenServiceGroupForServiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_ids: List[int] = None,
    ):
        self.request_id = request_id
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        return self

