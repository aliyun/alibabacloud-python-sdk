# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DeleteBackupClientResourceRequest(DaraModel):
    def __init__(
        self,
        client_ids: Dict[str, Any] = None,
    ):
        # A list of client IDs. The list can contain up to 100 client IDs.
        # 
        # This parameter is required.
        self.client_ids = client_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        return self

