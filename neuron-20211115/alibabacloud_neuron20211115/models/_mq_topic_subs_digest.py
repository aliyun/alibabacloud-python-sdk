# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MqTopicSubsDigest(DaraModel):
    def __init__(
        self,
        message_model: str = None,
        service_id: str = None,
        service_name: str = None,
        subs_expression: str = None,
    ):
        self.message_model = message_model
        self.service_id = service_id
        self.service_name = service_name
        self.subs_expression = subs_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_model is not None:
            result['MessageModel'] = self.message_model

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.subs_expression is not None:
            result['SubsExpression'] = self.subs_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SubsExpression') is not None:
            self.subs_expression = m.get('SubsExpression')

        return self

