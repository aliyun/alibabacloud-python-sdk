# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataSourceRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        description: str = None,
        name: str = None,
        oss_key: str = None,
        reg_id: str = None,
        type: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Data source description.
        self.description = description
        # Data source name.
        # 
        # This parameter is required.
        self.name = name
        # OSS file key.
        # 
        # This parameter is required.
        self.oss_key = oss_key
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Data source type
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

