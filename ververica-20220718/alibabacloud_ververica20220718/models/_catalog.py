# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Catalog(DaraModel):
    def __init__(
        self,
        extension_conf: Dict[str, str] = None,
        name: str = None,
        properties: Dict[str, Any] = None,
    ):
        self.extension_conf = extension_conf
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension_conf is not None:
            result['extensionConf'] = self.extension_conf

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extensionConf') is not None:
            self.extension_conf = m.get('extensionConf')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        return self

