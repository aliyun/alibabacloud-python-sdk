# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAppQuotaResponseBody(DaraModel):
    def __init__(
        self,
        active_license_count: int = None,
        app_id: str = None,
        license_count: int = None,
        request_id: str = None,
        usage_percent: float = None,
        workspace_id: str = None,
    ):
        self.active_license_count = active_license_count
        self.app_id = app_id
        self.license_count = license_count
        self.request_id = request_id
        self.usage_percent = usage_percent
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_license_count is not None:
            result['ActiveLicenseCount'] = self.active_license_count

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.license_count is not None:
            result['LicenseCount'] = self.license_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage_percent is not None:
            result['UsagePercent'] = self.usage_percent

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveLicenseCount') is not None:
            self.active_license_count = m.get('ActiveLicenseCount')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('LicenseCount') is not None:
            self.license_count = m.get('LicenseCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsagePercent') is not None:
            self.usage_percent = m.get('UsagePercent')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

