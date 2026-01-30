# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingSessionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sessions: List[main_models.ListRenderingSessionsResponseBodySessions] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sessions = sessions
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.ListRenderingSessionsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingSessionsResponseBodySessions(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        patch_id: str = None,
        rendering_instance_id: str = None,
        session_id: str = None,
        start_time: str = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.patch_id = patch_id
        self.rendering_instance_id = rendering_instance_id
        self.session_id = session_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

