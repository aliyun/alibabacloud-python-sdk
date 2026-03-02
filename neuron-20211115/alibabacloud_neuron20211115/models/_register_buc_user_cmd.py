# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterBucUserCmd(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
        enterprise_name: str = None,
    ):
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')

        return self

