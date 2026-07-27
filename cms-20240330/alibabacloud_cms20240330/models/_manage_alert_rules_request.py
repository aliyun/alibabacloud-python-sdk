# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ManageAlertRulesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ManageAlertRulesUnifiedActionInput = None,
        call_source: str = None,
    ):
        # The request body for managing alert rules. This body is shared by CREATE, UPDATE, PATCH, and BATCH_DELETE operations. Specify fields based on the action.
        self.body = body
        self.call_source = call_source

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.call_source is not None:
            result['callSource'] = self.call_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.ManageAlertRulesUnifiedActionInput()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('callSource') is not None:
            self.call_source = m.get('callSource')

        return self

