# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DistApplicationDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        dist_strategy: str = None,
    ):
        # The application ID. To obtain the application ID, see ListApplications.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The list of data files to distribute, formatted as a JSON array string.
        # 
        # This parameter is required.
        self.data = data
        # The canary release distribution strategy, formatted as a JSON string. Multiple distribution strategies are supported. Default value: full distribution.
        self.dist_strategy = dist_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data is not None:
            result['Data'] = self.data

        if self.dist_strategy is not None:
            result['DistStrategy'] = self.dist_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DistStrategy') is not None:
            self.dist_strategy = m.get('DistStrategy')

        return self

