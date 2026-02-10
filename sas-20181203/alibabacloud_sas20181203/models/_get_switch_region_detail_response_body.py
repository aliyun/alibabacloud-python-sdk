# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetSwitchRegionDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSwitchRegionDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSwitchRegionDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSwitchRegionDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_is_agree_modified: int = None,
        gmt_noticed: int = None,
        is_agree: str = None,
        is_noticed: str = None,
        need_notice: bool = None,
        need_switch: bool = None,
        region_status: List[main_models.GetSwitchRegionDetailResponseBodyDataRegionStatus] = None,
    ):
        # The time when the permissions were modified.
        self.gmt_is_agree_modified = gmt_is_agree_modified
        # The notification time.
        self.gmt_noticed = gmt_noticed
        # Indicates whether the migration is approved.
        self.is_agree = is_agree
        # Indicates whether the notification is sent.
        self.is_noticed = is_noticed
        # Specifies whether to notify the account.
        self.need_notice = need_notice
        # Specifies whether to switch.
        self.need_switch = need_switch
        # The status of the switching to the region.
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for v1 in self.region_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_is_agree_modified is not None:
            result['GmtIsAgreeModified'] = self.gmt_is_agree_modified

        if self.gmt_noticed is not None:
            result['GmtNoticed'] = self.gmt_noticed

        if self.is_agree is not None:
            result['IsAgree'] = self.is_agree

        if self.is_noticed is not None:
            result['IsNoticed'] = self.is_noticed

        if self.need_notice is not None:
            result['NeedNotice'] = self.need_notice

        if self.need_switch is not None:
            result['NeedSwitch'] = self.need_switch

        result['RegionStatus'] = []
        if self.region_status is not None:
            for k1 in self.region_status:
                result['RegionStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtIsAgreeModified') is not None:
            self.gmt_is_agree_modified = m.get('GmtIsAgreeModified')

        if m.get('GmtNoticed') is not None:
            self.gmt_noticed = m.get('GmtNoticed')

        if m.get('IsAgree') is not None:
            self.is_agree = m.get('IsAgree')

        if m.get('IsNoticed') is not None:
            self.is_noticed = m.get('IsNoticed')

        if m.get('NeedNotice') is not None:
            self.need_notice = m.get('NeedNotice')

        if m.get('NeedSwitch') is not None:
            self.need_switch = m.get('NeedSwitch')

        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k1 in m.get('RegionStatus'):
                temp_model = main_models.GetSwitchRegionDetailResponseBodyDataRegionStatus()
                self.region_status.append(temp_model.from_map(k1))

        return self

class GetSwitchRegionDetailResponseBodyDataRegionStatus(DaraModel):
    def __init__(
        self,
        ecs_count: int = None,
        gmt_plan_switch_time: int = None,
        region_id: str = None,
        status: int = None,
    ):
        # The number of ECS instances.
        self.ecs_count = ecs_count
        # The time when the migration is scheduled.
        self.gmt_plan_switch_time = gmt_plan_switch_time
        # The region in which the server resides.
        self.region_id = region_id
        # The migration status. Valid values:
        # 
        # *   **0**: pending
        # *   **1**: successful
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.gmt_plan_switch_time is not None:
            result['GmtPlanSwitchTime'] = self.gmt_plan_switch_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('GmtPlanSwitchTime') is not None:
            self.gmt_plan_switch_time = m.get('GmtPlanSwitchTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

