# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAtiAlertSettingsRequest(DaraModel):
    def __init__(
        self,
        alert_config: str = None,
        alert_group: str = None,
        client_token: str = None,
    ):
        self.alert_config = alert_config
        self.alert_group = alert_group
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            self.alert_config = m.get('AlertConfig')

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

