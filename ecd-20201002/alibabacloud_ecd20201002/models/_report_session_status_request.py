# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportSessionStatusRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        session_change_time: int = None,
        session_id: str = None,
        session_status: str = None,
    ):
        # End user.
        self.end_user_id = end_user_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Duration of the session change.
        # 
        # This parameter is required.
        self.session_change_time = session_change_time
        # Session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # Session status.
        # 
        # This parameter is required.
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_change_time is not None:
            result['SessionChangeTime'] = self.session_change_time

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionChangeTime') is not None:
            self.session_change_time = m.get('SessionChangeTime')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        return self

