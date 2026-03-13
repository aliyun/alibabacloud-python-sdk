# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class Channel(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        required: bool = None,
        supported_channel_types: List[str] = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        self.properties = properties
        self.required = required
        self.supported_channel_types = supported_channel_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.required is not None:
            result['Required'] = self.required

        if self.supported_channel_types is not None:
            result['SupportedChannelTypes'] = self.supported_channel_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('SupportedChannelTypes') is not None:
            self.supported_channel_types = m.get('SupportedChannelTypes')

        return self

