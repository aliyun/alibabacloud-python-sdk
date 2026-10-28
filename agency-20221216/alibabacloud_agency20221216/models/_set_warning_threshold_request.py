# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetWarningThresholdRequest(DaraModel):
    def __init__(
        self,
        uid: int = None,
        warning_value: str = None,
    ):
        # The UID of the reseller customer account.
        # 
        # This parameter is required.
        self.uid = uid
        # The percentage value. Valid values: 1 to 100. When the available credit drops below this percentage of the total credit limit, an alert email is sent to the reseller partner account.
        # 
        # This parameter is required.
        self.warning_value = warning_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uid is not None:
            result['Uid'] = self.uid

        if self.warning_value is not None:
            result['WarningValue'] = self.warning_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('WarningValue') is not None:
            self.warning_value = m.get('WarningValue')

        return self

