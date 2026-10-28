# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAlertNotifyTemplatesRequest(DaraModel):
    def __init__(
        self,
        alert_notify_template_ids: List[str] = None,
    ):
        # The IDs of the notification templates.
        # 
        # This parameter is required.
        self.alert_notify_template_ids = alert_notify_template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_notify_template_ids is not None:
            result['alertNotifyTemplateIds'] = self.alert_notify_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertNotifyTemplateIds') is not None:
            self.alert_notify_template_ids = m.get('alertNotifyTemplateIds')

        return self

