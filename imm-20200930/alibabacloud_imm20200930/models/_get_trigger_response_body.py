# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetTriggerResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trigger: main_models.DataIngestion = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The trigger information.
        self.trigger = trigger

    def validate(self):
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Trigger') is not None:
            temp_model = main_models.DataIngestion()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

