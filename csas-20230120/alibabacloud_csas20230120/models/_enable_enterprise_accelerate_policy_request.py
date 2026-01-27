# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableEnterpriseAcceleratePolicyRequest(DaraModel):
    def __init__(
        self,
        eap_id: str = None,
    ):
        # This parameter is required.
        self.eap_id = eap_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        return self

