# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushTimesUsageRequest(DaraModel):
    def __init__(
        self,
        adjust: bool = None,
        adjust_date: int = None,
        client_token: str = None,
        instance_id: str = None,
        mark: str = None,
        times: int = None,
    ):
        self.adjust = adjust
        self.adjust_date = adjust_date
        # The client token used to ensure request idempotence. We recommend that you use a UUID. The same `ClientToken` can be submitted only once within 24 hours. Retries for the same operation must use the same `ClientToken`, and new operations must use a new `ClientToken`.
        self.client_token = client_token
        # The Alibaba Cloud Marketplace instance ID.
        self.instance_id = instance_id
        self.mark = mark
        # The number of uses to deduct. The value must be greater than 0.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust is not None:
            result['Adjust'] = self.adjust

        if self.adjust_date is not None:
            result['AdjustDate'] = self.adjust_date

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mark is not None:
            result['Mark'] = self.mark

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjust') is not None:
            self.adjust = m.get('Adjust')

        if m.get('AdjustDate') is not None:
            self.adjust_date = m.get('AdjustDate')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mark') is not None:
            self.mark = m.get('Mark')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

