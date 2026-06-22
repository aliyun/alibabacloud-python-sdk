# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationConfig(DaraModel):
    def __init__(
        self,
        config_description: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # A description of the modification.
        self.config_description = config_description
        # The name of the application configuration file.
        self.config_file_name = config_file_name
        # The configuration item key.
        self.config_item_key = config_item_key
        # The configuration item value.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        return self

