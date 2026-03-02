# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDeveloperRequest(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
    ):
        self.enterprise_id = enterprise_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        return self

