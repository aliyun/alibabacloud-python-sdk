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
        # The key used to uniquely identify an action.
        self.action_key = action_key
        # The text used to display the action name in the user interface.
        self.action_text = action_text
        # Indicates whether the action is available.
        self.enable = enable
        # The URL to navigate to when the action is clicked.
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

