# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class EditSiteWafSettingsRequest(DaraModel):
    def __init__(
        self,
        settings: main_models.WafSiteSettings = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # WAF configuration information for the site, passed in JSON format.
        self.settings = settings
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
        self.site_id = site_id
        # Site version.
        self.site_version = site_version

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Settings') is not None:
            temp_model = main_models.WafSiteSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

