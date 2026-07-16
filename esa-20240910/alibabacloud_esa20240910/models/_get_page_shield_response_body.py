# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPageShieldResponseBody(DaraModel):
    def __init__(
        self,
        enable: str = None,
        report_uri: str = None,
        request_id: str = None,
        site_version: int = None,
    ):
        # The switch status. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.enable = enable
        # The report URI.
        self.report_uri = report_uri
        # The request ID.
        self.request_id = request_id
        # The version number of the site. For sites with version management enabled, you can use this parameter to specify the site version on which the configuration takes effect. The default value is 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.report_uri is not None:
            result['ReportUri'] = self.report_uri

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ReportUri') is not None:
            self.report_uri = m.get('ReportUri')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

