# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FunagentVersionItem(DaraModel):
    def __init__(
        self,
        description: str = None,
        publish_content: List[str] = None,
        publish_time: str = None,
        version: str = None,
    ):
        self.description = description
        # 多条更新说明
        self.publish_content = publish_content
        # 日期或 ISO 8601 字符串
        self.publish_time = publish_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.publish_content is not None:
            result['publishContent'] = self.publish_content

        if self.publish_time is not None:
            result['publishTime'] = self.publish_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('publishContent') is not None:
            self.publish_content = m.get('publishContent')

        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

