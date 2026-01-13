# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Configuration(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')

        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')

        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')

        return self

