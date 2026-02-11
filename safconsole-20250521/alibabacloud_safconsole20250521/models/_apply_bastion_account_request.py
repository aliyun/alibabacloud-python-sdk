# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyBastionAccountRequest(DaraModel):
    def __init__(
        self,
        mobile: int = None,
        project_id: int = None,
    ):
        # Mobile Phone Number
        self.mobile = mobile
        # Project ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

