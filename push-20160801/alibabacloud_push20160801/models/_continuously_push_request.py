# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContinuouslyPushRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: str = None,
        target: str = None,
        target_value: str = None,
    ):
        # The AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The message ID.
        # 
        # The MessageId obtained after calling the Push operation and setting Target to TBD. It represents a message that has been saved to the push system.
        # 
        # This parameter is required.
        self.message_id = message_id
        # The push target:
        # 
        # - **DEVICE**: Push based on devices.
        # - **ACCOUNT**: Push based on accounts.
        # - **ALIAS**: Push based on aliases.
        # 
        # Continuous push supports only these three target types.
        # 
        # This parameter is required.
        self.target = target
        # Set this parameter based on Target. Separate multiple values with commas. If the limit is exceeded, push the message in multiple batches.
        # 
        # - If Target is set to DEVICE, the value is in the format of `deviceid1,deviceid2`. A maximum of 1,000 devices are supported.
        # - If Target is set to ACCOUNT, the value is in the format of `account1,account2`. A maximum of 1,000 accounts are supported.
        # - If Target is set to ALIAS, the value is in the format of `alias1,alias2`. A maximum of 1,000 aliases are supported.
        # 
        # This parameter is required.
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.target is not None:
            result['Target'] = self.target

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

