# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceDataBackup(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        grafana_workspace_id: str = None,
        id: int = None,
        msg: str = None,
        process_name: str = None,
        process_status: str = None,
        sub_type: str = None,
        user_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grafana_workspace_id = grafana_workspace_id
        self.id = id
        self.msg = msg
        self.process_name = process_name
        self.process_status = process_status
        self.sub_type = sub_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.id is not None:
            result['id'] = self.id

        if self.msg is not None:
            result['msg'] = self.msg

        if self.process_name is not None:
            result['processName'] = self.process_name

        if self.process_status is not None:
            result['processStatus'] = self.process_status

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('processName') is not None:
            self.process_name = m.get('processName')

        if m.get('processStatus') is not None:
            self.process_status = m.get('processStatus')

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

