# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEdsAgentReportConfigRequest(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        desktop_id: str = None,
        ecs_instance_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.desktop_id = desktop_id
        self.ecs_instance_id = ecs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        return self

