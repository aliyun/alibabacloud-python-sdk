# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachPolicyConfig(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        config: str = None,
        name: str = None,
    ):
        self.class_name = class_name
        self.config = config
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

