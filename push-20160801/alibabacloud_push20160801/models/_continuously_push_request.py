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
        # AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # Message ID.
        # 
        # Obtain this MessageId by calling the Push API with Target set to TBD. It represents a message already saved in the push system.
        # 
        # This parameter is required.
        self.message_id = message_id
        # Push target:
        # 
        # - **DEVICE**: Push by device
        # 
        # - **ACCOUNT**: Push by account
        # 
        # - **ALIAS**: Push by alias
        # 
        # Continuous push supports only these three target types.
        # 
        # This parameter is required.
        self.target = target
        # Specify values based on Target. Separate multiple values with commas. If you exceed the limit, split the push into multiple calls.
        # 
        # - Target=DEVICE: values such as `deviceid1,deviceid2` (up to 1,000 supported).
        # 
        # - Target=ACCOUNT: values such as `account1,account2` (up to 1,000 supported).
        # 
        # - Target=ALIAS: values such as `alias1,alias2` (up to 1,000 supported).
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

