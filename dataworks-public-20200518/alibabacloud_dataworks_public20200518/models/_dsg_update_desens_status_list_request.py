# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DsgUpdateDesensStatusListRequest(DaraModel):
    def __init__(
        self,
        desens_status: int = None,
        ids: List[int] = None,
    ):
        # This parameter is required.
        self.desens_status = desens_status
        # This parameter is required.
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desens_status is not None:
            result['DesensStatus'] = self.desens_status

        if self.ids is not None:
            result['Ids'] = self.ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensStatus') is not None:
            self.desens_status = m.get('DesensStatus')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        return self

