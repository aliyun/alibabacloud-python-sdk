# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRefundPriceRequest(DaraModel):
    def __init__(
        self,
        billing_instance_ids: str = None,
        instance_id: str = None,
    ):
        self.billing_instance_ids = billing_instance_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_instance_ids is not None:
            result['billingInstanceIds'] = self.billing_instance_ids

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingInstanceIds') is not None:
            self.billing_instance_ids = m.get('billingInstanceIds')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

