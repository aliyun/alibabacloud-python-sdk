# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstanceHealerRequest(DaraModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
        strategy: str = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.instance_id_list = instance_id_list
        self.strategy = strategy
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

