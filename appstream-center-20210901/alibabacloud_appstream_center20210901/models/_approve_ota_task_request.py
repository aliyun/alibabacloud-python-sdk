# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveOtaTaskRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        ota_type: str = None,
        start_time: str = None,
        task_id: str = None,
    ):
        # The delivery group ID. You can call [ListAppInstanceGroup](~~ListAppInstanceGroup~~) to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The region ID of the delivery group. You can call [ListRegions](~~ListRegions~~) to query the list of regions supported by Wuying Cloud Application.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The over-the-air upgrade task type.
        # 
        # This parameter is required.
        self.ota_type = ota_type
        # The start time of the over-the-air upgrade task. Specify the time in ISO 8601 format.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.start_time = start_time
        # The over-the-air upgrade task ID. You can call [ListAppInstanceGroup](~~ListAppInstanceGroup~~) to obtain the ID.
        # 
        # > Each successful call of `ApproveOtaTask` causes the `TaskId` to change. Therefore, before calling this operation again, call `ListAppInstanceGroup` again to obtain the latest `TaskId`.
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
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.ota_type is not None:
            result['OtaType'] = self.ota_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

