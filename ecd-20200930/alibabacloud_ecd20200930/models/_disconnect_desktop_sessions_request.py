# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DisconnectDesktopSessionsRequest(DaraModel):
    def __init__(
        self,
        pre_check: bool = None,
        region_id: str = None,
        sessions: List[main_models.DisconnectDesktopSessionsRequestSessions] = None,
    ):
        # Specifies whether to perform precheck. If you perform precheck, the system does not disconnect from desktop sessions. Only the sessions that do not meet specific conditions are returned.
        self.pre_check = pre_check
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session details.
        # 
        # This parameter is required.
        self.sessions = sessions

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_check is not None:
            result['PreCheck'] = self.pre_check

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheck') is not None:
            self.pre_check = m.get('PreCheck')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DisconnectDesktopSessionsRequestSessions()
                self.sessions.append(temp_model.from_map(k1))

        return self

class DisconnectDesktopSessionsRequestSessions(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_user_id: str = None,
    ):
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The end user ID.
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        return self

