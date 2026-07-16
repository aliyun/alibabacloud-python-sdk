# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionOp(DaraModel):
    def __init__(
        self,
        op: str = None,
        payload: main_models.SubscriptionForModify = None,
        uuid: str = None,
    ):
        self.op = op
        # create/update 必填
        self.payload = payload
        # update/remove 必填
        self.uuid = uuid

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('payload') is not None:
            temp_model = main_models.SubscriptionForModify()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

