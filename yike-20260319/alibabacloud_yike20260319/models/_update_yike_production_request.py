# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateYikeProductionRequest(DaraModel):
    def __init__(
        self,
        production_id: str = None,
        title: str = None,
    ):
        # The project ID.
        # 
        # This parameter is required.
        self.production_id = production_id
        # The project title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

