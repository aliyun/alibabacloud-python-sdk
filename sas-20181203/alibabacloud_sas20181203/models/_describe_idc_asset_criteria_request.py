# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIdcAssetCriteriaRequest(DaraModel):
    def __init__(
        self,
        status: int = None,
        value: str = None,
    ):
        # Indicates whether the corresponding IP address is valid. Valid values:
        # - **0**: valid
        # - **1**: ignored
        # - **2**: invalid
        # - **3**: expired
        # - **4**: probe does not exist.
        self.status = status
        # The fuzzy match value entered when querying assets.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

