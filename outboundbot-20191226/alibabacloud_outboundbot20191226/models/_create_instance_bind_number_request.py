# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceBindNumberRequest(DaraModel):
    def __init__(
        self,
        instance_list: str = None,
        number: str = None,
    ):
        self.instance_list = instance_list
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

