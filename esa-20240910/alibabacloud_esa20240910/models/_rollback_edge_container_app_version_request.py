# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackEdgeContainerAppVersionRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        percentage: int = None,
        remarks: str = None,
        used_percent: bool = None,
        version_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        self.percentage = percentage
        # The remarks.
        self.remarks = remarks
        self.used_percent = used_percent
        # The ID of version that you want to roll back.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.used_percent is not None:
            result['UsedPercent'] = self.used_percent

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('UsedPercent') is not None:
            self.used_percent = m.get('UsedPercent')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

