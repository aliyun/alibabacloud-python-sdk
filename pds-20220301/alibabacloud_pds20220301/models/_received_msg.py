# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ReceivedMsg(DaraModel):
    def __init__(
        self,
        has_read: bool = None,
        msg_category: str = None,
        msg_content: main_models.ReceivedMsgMsgContent = None,
        msg_id: str = None,
        msg_sub_category: str = None,
        msg_type: str = None,
        publish_at: int = None,
        read_at: int = None,
    ):
        self.has_read = has_read
        self.msg_category = msg_category
        self.msg_content = msg_content
        self.msg_id = msg_id
        self.msg_sub_category = msg_sub_category
        self.msg_type = msg_type
        self.publish_at = publish_at
        self.read_at = read_at

    def validate(self):
        if self.msg_content:
            self.msg_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_read is not None:
            result['has_read'] = self.has_read

        if self.msg_category is not None:
            result['msg_category'] = self.msg_category

        if self.msg_content is not None:
            result['msg_content'] = self.msg_content.to_map()

        if self.msg_id is not None:
            result['msg_id'] = self.msg_id

        if self.msg_sub_category is not None:
            result['msg_sub_category'] = self.msg_sub_category

        if self.msg_type is not None:
            result['msg_type'] = self.msg_type

        if self.publish_at is not None:
            result['publish_at'] = self.publish_at

        if self.read_at is not None:
            result['read_at'] = self.read_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('has_read') is not None:
            self.has_read = m.get('has_read')

        if m.get('msg_category') is not None:
            self.msg_category = m.get('msg_category')

        if m.get('msg_content') is not None:
            temp_model = main_models.ReceivedMsgMsgContent()
            self.msg_content = temp_model.from_map(m.get('msg_content'))

        if m.get('msg_id') is not None:
            self.msg_id = m.get('msg_id')

        if m.get('msg_sub_category') is not None:
            self.msg_sub_category = m.get('msg_sub_category')

        if m.get('msg_type') is not None:
            self.msg_type = m.get('msg_type')

        if m.get('publish_at') is not None:
            self.publish_at = m.get('publish_at')

        if m.get('read_at') is not None:
            self.read_at = m.get('read_at')

        return self

class ReceivedMsgMsgContent(DaraModel):
    def __init__(
        self,
        msg_data: Dict[str, Any] = None,
    ):
        self.msg_data = msg_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg_data is not None:
            result['msg_data'] = self.msg_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg_data') is not None:
            self.msg_data = m.get('msg_data')

        return self

