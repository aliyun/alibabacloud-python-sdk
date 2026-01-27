# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpLoginOrderItem(DaraModel):
    def __init__(
        self,
        class_: str = None,
        config_id: str = None,
        desc: str = None,
        enabled: bool = None,
        name: str = None,
        type: str = None,
    ):
        self.class_ = class_
        self.config_id = config_id
        self.desc = desc
        self.enabled = enabled
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

