# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppOperateAction(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_text: str = None,
        enable: bool = None,
        href: str = None,
    ):
        # 用于唯一标识一个操作行为
        self.action_key = action_key
        # 用于在界面中展示操作名称
        self.action_text = action_text
        # 标识该操作是否可用
        self.enable = enable
        # 点击操作时跳转的URL地址
        self.href = href

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_text is not None:
            result['ActionText'] = self.action_text

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.href is not None:
            result['Href'] = self.href

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionText') is not None:
            self.action_text = m.get('ActionText')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Href') is not None:
            self.href = m.get('Href')

        return self

