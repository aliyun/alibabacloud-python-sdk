# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoSqlOptimizeStatusRequest(DaraModel):
    def __init__(
        self,
        instances: str = None,
        status: int = None,
    ):
        # The database instance IDs. Separate multiple IDs with commas (,).
        # 
        # >  You can specify up to 50 instance IDs.
        # 
        # This parameter is required.
        self.instances = instances
        # The status of the automatic SQL optimization feature. Valid values:
        # 
        # *   **0**: The automatic SQL optimization feature is disabled.
        # *   **1**: **SQL diagnosis and automatic index creation** is specified.
        # *   **3**: **SQL diagnosis only** is specified.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

