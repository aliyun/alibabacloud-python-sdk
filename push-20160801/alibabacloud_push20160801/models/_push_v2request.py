# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class PushV2Request(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        idempotent_token: str = None,
        push_task: main_models.PushTask = None,
    ):
        # The AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # An idempotence parameter that prevents duplicate push notifications caused by retries from the API caller. If you use the same IdempotentToken within 15 minutes, only one push notification is sent, and subsequent calls return the result of the first successful push.
        # 
        # > 
        # > - The parameter format is a standard 36-character UUID (8-4-4-4-12). Each valid character is a hexadecimal digit in the range 0-9 or a-f, case-insensitive.
        # > - This parameter only prevents duplicate push notifications caused by retries. It cannot prevent duplicate push notifications caused by concurrent calls.
        self.idempotent_token = idempotent_token
        # The push task.
        # 
        # This parameter is required.
        self.push_task = push_task

    def validate(self):
        if self.push_task:
            self.push_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token

        if self.push_task is not None:
            result['PushTask'] = self.push_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')

        if m.get('PushTask') is not None:
            temp_model = main_models.PushTask()
            self.push_task = temp_model.from_map(m.get('PushTask'))

        return self

