# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceArmsAlertConfig(DaraModel):
    def __init__(
        self,
        arms_alerts_enable: str = None,
        arms_alerts_webhook_url: str = None,
    ):
        self.arms_alerts_enable = arms_alerts_enable
        self.arms_alerts_webhook_url = arms_alerts_webhook_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arms_alerts_enable is not None:
            result['armsAlertsEnable'] = self.arms_alerts_enable

        if self.arms_alerts_webhook_url is not None:
            result['armsAlertsWebhookUrl'] = self.arms_alerts_webhook_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsAlertsEnable') is not None:
            self.arms_alerts_enable = m.get('armsAlertsEnable')

        if m.get('armsAlertsWebhookUrl') is not None:
            self.arms_alerts_webhook_url = m.get('armsAlertsWebhookUrl')

        return self

