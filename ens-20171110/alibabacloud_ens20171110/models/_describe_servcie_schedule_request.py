# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServcieScheduleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        pod_config_name: str = None,
        uuid: str = None,
    ):
        # The application ID.
        # 
        # You can obtain this value after you call the CreateApplication operation to create an application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is invalid.
        self.pod_config_name = pod_config_name
        # The unique ID of the terminal device.
        # 
        # You can obtain this value after you call the RunServiceSchedule operation and set ServiceAction to Start to start service scheduling.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

