# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceRecord(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        last_modify_time: int = None,
        tag: str = None,
        value: str = None,
    ):
        # The record creation time, a UNIX timestamp in seconds. This field is returned only in responses.
        self.create_time = create_time
        # The record ID. If this field is not specified during creation or batch write, the server automatically generates it. If specified, the provided ID is used.
        self.id = id
        # The record last modification time, a UNIX timestamp in seconds. This field is returned only in responses.
        self.last_modify_time = last_modify_time
        # The record tag.
        self.tag = tag
        # The record content, which is a string encoded from a JSON object.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.tag is not None:
            result['tag'] = self.tag

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

