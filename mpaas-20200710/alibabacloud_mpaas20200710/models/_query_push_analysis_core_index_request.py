# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPushAnalysisCoreIndexRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel: str = None,
        end_time: int = None,
        platform: str = None,
        start_time: int = None,
        task_id: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.channel = channel
        # This parameter is required.
        self.end_time = end_time
        self.platform = platform
        # This parameter is required.
        self.start_time = start_time
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

