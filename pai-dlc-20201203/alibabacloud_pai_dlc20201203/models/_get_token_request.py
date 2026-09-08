# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetTokenRequest(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        target_id: str = None,
        target_type: str = None,
        token_settings: main_models.TokenSettings = None,
    ):
        # The expiration time of the sharing link in seconds. Default value: 604800. Minimum value: 0.
        self.expire_time = expire_time
        # The ID of the task to share.
        self.target_id = target_id
        # The type of the task to share. Valid values: job and tensorboard.
        self.target_type = target_type
        self.token_settings = token_settings

    def validate(self):
        if self.token_settings:
            self.token_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.token_settings is not None:
            result['TokenSettings'] = self.token_settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TokenSettings') is not None:
            temp_model = main_models.TokenSettings()
            self.token_settings = temp_model.from_map(m.get('TokenSettings'))

        return self

