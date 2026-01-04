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
        # The ID of the application. To obtain the application ID, call the ListApplications operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The list of data files that you want to distribute. The value must be a JSON string.
        # 
        # This parameter is required.
        self.data = data
        # The canary release policy. The value must be a JSON string. You can specify multiple distribution policies. By default, all data files are distributed.
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

