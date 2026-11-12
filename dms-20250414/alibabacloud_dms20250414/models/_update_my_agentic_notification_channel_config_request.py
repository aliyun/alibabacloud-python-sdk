# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMyAgenticNotificationChannelConfigRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        config: str = None,
        enabled: bool = None,
    ):
        # The notification channel type. Currently, only FEISHU (Lark) is supported. Specifying other values results in a parameter error.
        # 
        # This parameter is required.
        self.channel = channel
        # The channel configuration in the format of a JSON object string. This parameter is not required if you do not update the binding information. Supports mobile (phone number) or email. You can bind or rebind a Lark account by using one of them at a time. If the existing masked values of mobile or email are passed as ******, they are not modified. openId is a read-only field and cannot be specified.
        self.config = config
        # Specifies whether to enable the notification channel. If this parameter is not specified, the original value is retained. When you only modify the switch, the Config parameter is not required, and the existing binding information remains unchanged.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.config is not None:
            result['Config'] = self.config

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

