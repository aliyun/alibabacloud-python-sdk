# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContactRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        contact_name: str = None,
        type: str = None,
    ):
        # 渠道参数配置 JSON 字符串。IM 类型示例：{"channels":[{"channelType":"dingtalk","clientId":"xxx","clientSecret":"xxx","targetType":"group","targetId":"xxx","robotCode":"xxx"}]}
        # 
        # This parameter is required.
        self.config = config
        # 联系人名称（用户自定义，用于展示），同一用户下不可重名
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # 渠道大类，当前支持 IM
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
        if self.config is not None:
            result['Config'] = self.config

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

