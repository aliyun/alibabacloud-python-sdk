# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        add_model: str = None,
    ):
        # This parameter is required.
        self.add_model = add_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_model is not None:
            result['AddModel'] = self.add_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddModel') is not None:
            self.add_model = m.get('AddModel')

        return self

