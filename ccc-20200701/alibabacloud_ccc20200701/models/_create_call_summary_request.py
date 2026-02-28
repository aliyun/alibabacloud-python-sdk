# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCallSummaryRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        context: str = None,
        customer_id: str = None,
        instance_id: str = None,
    ):
        self.contact_id = contact_id
        self.context = context
        self.customer_id = customer_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.context is not None:
            result['Context'] = self.context

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

