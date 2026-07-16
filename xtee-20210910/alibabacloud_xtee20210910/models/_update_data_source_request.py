# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        oss_key: str = None,
        reg_id: str = None,
        type: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The description.
        self.description = description
        # The primary key ID.
        # 
        # This parameter is required.
        self.id = id
        # The data source name.
        self.name = name
        # The OSS file key.
        self.oss_key = oss_key
        # The region code.
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # The data source type.
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

        if self.id is not None:
            result['id'] = self.id

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

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

