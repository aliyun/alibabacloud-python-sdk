# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetYikeCallbackConfigRequest(DaraModel):
    def __init__(
        self,
        callback_config: str = None,
        callback_url: str = None,
    ):
        # This parameter is required.
        self.callback_config = callback_config
        # This parameter is required.
        self.callback_url = callback_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            self.callback_config = m.get('CallbackConfig')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        return self

