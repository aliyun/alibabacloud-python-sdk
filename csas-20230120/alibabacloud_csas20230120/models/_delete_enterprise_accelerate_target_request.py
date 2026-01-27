# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteEnterpriseAccelerateTargetRequest(DaraModel):
    def __init__(
        self,
        eap_id: str = None,
        target: List[str] = None,
    ):
        # This parameter is required.
        self.eap_id = eap_id
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

