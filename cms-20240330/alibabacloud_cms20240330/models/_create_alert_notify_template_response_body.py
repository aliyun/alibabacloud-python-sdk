# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlertNotifyTemplateResponseBody(DaraModel):
    def __init__(
        self,
        alert_notify_template_id: str = None,
        request_id: str = None,
    ):
        self.alert_notify_template_id = alert_notify_template_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notify_template_id is not None:
            result['alertNotifyTemplateId'] = self.alert_notify_template_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertNotifyTemplateId') is not None:
            self.alert_notify_template_id = m.get('alertNotifyTemplateId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

