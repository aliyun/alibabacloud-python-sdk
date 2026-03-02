# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MqTopicDigest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        create_time: str = None,
        id: int = None,
        message_type: str = None,
        name: str = None,
        remark: str = None,
    ):
        self.alias = alias
        self.create_time = create_time
        self.id = id
        self.message_type = message_type
        self.name = name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

