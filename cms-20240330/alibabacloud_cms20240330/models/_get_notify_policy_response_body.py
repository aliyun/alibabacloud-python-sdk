# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetNotifyPolicyResponseBody(DaraModel):
    def __init__(
        self,
        notify_policy: main_models.NotifyPolicy = None,
        request_id: str = None,
    ):
        # The notification policy object details, including the policy UUID, name, description, enabled status, and sub-entities such as notification policies (noise reduction, notification routing, and channels), subscriptions (event filtering, cross-workspace routing, and legacy product event subscriptions), and response plans (escalation, repeated notifications, automatic recovery, and action integration).
        self.notify_policy = notify_policy
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.notify_policy:
            self.notify_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_policy is not None:
            result['notifyPolicy'] = self.notify_policy.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPolicy') is not None:
            temp_model = main_models.NotifyPolicy()
            self.notify_policy = temp_model.from_map(m.get('notifyPolicy'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

