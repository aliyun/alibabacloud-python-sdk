# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetSiteWafSettingsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        settings: main_models.WafSiteSettings = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Details of site WAF configuration.
        self.settings = settings

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Settings') is not None:
            temp_model = main_models.WafSiteSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        return self

