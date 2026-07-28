# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeApplicationVersionRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        upgrade_policy: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The upgrade policy.
        self.upgrade_policy = upgrade_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.upgrade_policy is not None:
            result['UpgradePolicy'] = self.upgrade_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('UpgradePolicy') is not None:
            self.upgrade_policy = m.get('UpgradePolicy')

        return self

