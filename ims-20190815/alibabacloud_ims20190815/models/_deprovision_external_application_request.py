# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeprovisionExternalApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the external application installed for the current account. You can obtain the ID by calling ListExternalApplications or ListApplicationProvisionInfos with SourceType set to external. If the application is not installed, you must first call ProvisionExternalApplication.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

