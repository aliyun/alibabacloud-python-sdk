# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceLogRequest(DaraModel):
    def __init__(
        self,
        instance_history_id: int = None,
        instance_id: int = None,
        project_env: str = None,
    ):
        # The historical record number of the instance. You can call the ListInstanceHistory operation to query the ID.
        self.instance_history_id = instance_history_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The environment of the workspace. Valid values: PROD and DEV.
        # 
        # This parameter is required.
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_history_id is not None:
            result['InstanceHistoryId'] = self.instance_history_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceHistoryId') is not None:
            self.instance_history_id = m.get('InstanceHistoryId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

