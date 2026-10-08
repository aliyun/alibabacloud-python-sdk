# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHealthCheckUrlRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        hc_url: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The health check URL of the application. The URL must start with `http://`, and can be up to 255 characters in length. Example: `http://127.0.0.1:8080/_ehc.html`. If this parameter is not specified, the health check URL of the application is not changed.
        self.hc_url = hc_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.hc_url is not None:
            result['hcURL'] = self.hc_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('hcURL') is not None:
            self.hc_url = m.get('hcURL')

        return self

