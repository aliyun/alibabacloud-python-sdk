# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetEventCallbackRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_switch: str = None,
        callback_queue_name: str = None,
        callback_type: str = None,
        callback_url: str = None,
        event_type_list: str = None,
    ):
        # The authentication key. The key can be up to 32 characters in length and must contain uppercase letters, lowercase letters, and digits. This parameter takes effect only if you set CallbackType to **HTTP**.
        self.auth_key = auth_key
        # Specifies whether to enable callback authentication. This parameter takes effect only if you set CallbackType to **HTTP**. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.auth_switch = auth_switch
        # The name of the Simple Message Queue (SMQ) queue in the region. The name must start with ice-callback-.
        self.callback_queue_name = callback_queue_name
        # The callback method. Valid values:
        # 
        # *   **HTTP**
        # *   **MNS**
        self.callback_type = callback_type
        # The callback URL. This parameter is required if you set CallbackType to **HTTP**. The callback URL cannot exceed 256 bytes in length. You can specify only one callback URL.
        self.callback_url = callback_url
        # The type of the callback event. You can specify multiple values separated with commas (,). ProduceMediaComplete: indicates that the editing and production task is complete.
        self.event_type_list = event_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch

        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name

        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type

        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')

        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')

        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')

        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')

        return self

