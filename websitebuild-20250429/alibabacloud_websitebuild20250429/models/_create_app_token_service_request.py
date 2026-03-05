# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppTokenServiceRequest(DaraModel):
    def __init__(
        self,
        create_action: str = None,
    ):
        self.create_action = create_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_action is not None:
            result['CreateAction'] = self.create_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateAction') is not None:
            self.create_action = m.get('CreateAction')

        return self

