# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        subscription: main_models.SubscriptionForView = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The subscription object.
        self.subscription = subscription

    def validate(self):
        if self.subscription:
            self.subscription.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.subscription is not None:
            result['subscription'] = self.subscription.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('subscription') is not None:
            temp_model = main_models.SubscriptionForView()
            self.subscription = temp_model.from_map(m.get('subscription'))

        return self

