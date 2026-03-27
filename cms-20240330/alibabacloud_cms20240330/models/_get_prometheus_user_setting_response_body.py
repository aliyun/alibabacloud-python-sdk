# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetPrometheusUserSettingResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_user_setting: Dict[str, str] = None,
        request_id: str = None,
    ):
        self.prometheus_user_setting = prometheus_user_setting
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_user_setting is not None:
            result['prometheusUserSetting'] = self.prometheus_user_setting

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusUserSetting') is not None:
            self.prometheus_user_setting = m.get('prometheusUserSetting')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

