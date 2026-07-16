# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EntityMediaBasicInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        biz: str = None,
        create_time: str = None,
        entity_id: str = None,
        entity_media_id: str = None,
        modified_time: str = None,
        status: str = None,
        user_data: str = None,
    ):
        self.app_id = app_id
        self.biz = biz
        self.create_time = create_time
        self.entity_id = entity_id
        self.entity_media_id = entity_media_id
        self.modified_time = modified_time
        self.status = status
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.biz is not None:
            result['Biz'] = self.biz

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_media_id is not None:
            result['EntityMediaId'] = self.entity_media_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityMediaId') is not None:
            self.entity_media_id = m.get('EntityMediaId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

