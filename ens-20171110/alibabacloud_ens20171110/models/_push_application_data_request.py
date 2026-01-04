# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushApplicationDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        push_strategy: str = None,
        timeout: int = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data files that you want to push. The value must be a JSON string.
        # 
        # This parameter is required.
        self.data = data
        # The push policy in the canary release environment. The value must be a JSON string. You can specify multiple push policies. By default, all data files are pushed.
        self.push_strategy = push_strategy
        # This parameter does not take effect.
        self.timeout = timeout

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

        if self.push_strategy is not None:
            result['PushStrategy'] = self.push_strategy

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('PushStrategy') is not None:
            self.push_strategy = m.get('PushStrategy')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

