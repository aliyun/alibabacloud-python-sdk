# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInspectionSchedulesRequest(DaraModel):
    def __init__(
        self,
        enabled: int = None,
        instance_id: str = None,
        page_num: int = None,
        page_size: int = None,
        schedule_id: str = None,
        security_token: str = None,
    ):
        self.enabled = enabled
        # This parameter is required.
        self.instance_id = instance_id
        self.page_num = page_num
        self.page_size = page_size
        self.schedule_id = schedule_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

