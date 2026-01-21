# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorAttributeRequest(DaraModel):
    def __init__(
        self,
        include_alert: bool = None,
        region_id: str = None,
        task_id: str = None,
    ):
        # Specifies whether to return the information of the alert rules that are configured for the site monitoring task. Valid values:
        # 
        # *   true: The system returns the information of the alert rules that are configured for the site monitoring task.
        # *   false (default): The system does not return the information of the alert rules that are configured for the site monitoring task.
        self.include_alert = include_alert
        self.region_id = region_id
        # The ID of the site monitoring task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_alert is not None:
            result['IncludeAlert'] = self.include_alert

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeAlert') is not None:
            self.include_alert = m.get('IncludeAlert')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

