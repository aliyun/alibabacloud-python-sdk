# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
    ):
        # The alert rule ID.
        # 
        # For more information about how to obtain the ID of an alert rule, see [GetAlertRules](https://help.aliyun.com/document_detail/2612348.html).
        # 
        # This parameter is required.
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        return self

