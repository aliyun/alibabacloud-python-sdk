# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListEnterpriseAccelerateTargetsResponseBody(DaraModel):
    def __init__(
        self,
        eap_id: str = None,
        request_id: str = None,
        targets: List[str] = None,
        total: int = None,
    ):
        self.eap_id = eap_id
        self.request_id = request_id
        self.targets = targets
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.targets is not None:
            result['Targets'] = self.targets

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

