# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UninstallMonitorAgentRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        sale_mode: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        return self

