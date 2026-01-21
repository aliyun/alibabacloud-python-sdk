# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSiteMonitorsRequest(DaraModel):
    def __init__(
        self,
        is_delete_alarms: bool = None,
        region_id: str = None,
        task_ids: str = None,
    ):
        # Specifies whether to delete the alert rules configured for the site monitoring tasks. Valid values:
        # 
        # *   true (default value)
        # *   false
        self.is_delete_alarms = is_delete_alarms
        self.region_id = region_id
        # The IDs of the site monitoring tasks that you want to delete. Separate multiple task IDs with commas (,).
        # 
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_delete_alarms is not None:
            result['IsDeleteAlarms'] = self.is_delete_alarms

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDeleteAlarms') is not None:
            self.is_delete_alarms = m.get('IsDeleteAlarms')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

