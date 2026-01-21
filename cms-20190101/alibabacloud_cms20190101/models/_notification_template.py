# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NotificationTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        en_content: str = None,
        en_item_content: str = None,
        en_title: str = None,
        name: str = None,
        type: str = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
        wraper_type: str = None,
        zh_content: str = None,
        zh_item_content: str = None,
        zh_title: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.en_content = en_content
        self.en_item_content = en_item_content
        self.en_title = en_title
        # This parameter is required.
        self.name = name
        self.type = type
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid
        self.wraper_type = wraper_type
        self.zh_content = zh_content
        self.zh_item_content = zh_item_content
        self.zh_title = zh_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.en_content is not None:
            result['EnContent'] = self.en_content

        if self.en_item_content is not None:
            result['EnItemContent'] = self.en_item_content

        if self.en_title is not None:
            result['EnTitle'] = self.en_title

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.wraper_type is not None:
            result['WraperType'] = self.wraper_type

        if self.zh_content is not None:
            result['ZhContent'] = self.zh_content

        if self.zh_item_content is not None:
            result['ZhItemContent'] = self.zh_item_content

        if self.zh_title is not None:
            result['ZhTitle'] = self.zh_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnContent') is not None:
            self.en_content = m.get('EnContent')

        if m.get('EnItemContent') is not None:
            self.en_item_content = m.get('EnItemContent')

        if m.get('EnTitle') is not None:
            self.en_title = m.get('EnTitle')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('WraperType') is not None:
            self.wraper_type = m.get('WraperType')

        if m.get('ZhContent') is not None:
            self.zh_content = m.get('ZhContent')

        if m.get('ZhItemContent') is not None:
            self.zh_item_content = m.get('ZhItemContent')

        if m.get('ZhTitle') is not None:
            self.zh_title = m.get('ZhTitle')

        return self

