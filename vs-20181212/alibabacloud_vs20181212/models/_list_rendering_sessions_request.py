# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRenderingSessionsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        project_id: str = None,
        rendering_instance_id: str = None,
        session_id: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # Cloud application ID
        self.app_id = app_id
        # Unique ID of the client.
        self.client_id = client_id
        # Time range filter parameter. Represented in ISO8601 standard and must use UTC time, in the format yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # Page number, starting from 1
        self.page_number = page_number
        # The number of rows per page set for paged queries.
        self.page_size = page_size
        # Cloud application patch ID.
        # 
        # 1. When you enter origin, only sessions that started the original version of the app are filtered.
        self.patch_id = patch_id
        # Project ID
        # 
        # This parameter is required.
        self.project_id = project_id
        # Cloud application service instance ID
        self.rendering_instance_id = rendering_instance_id
        # Session ID
        self.session_id = session_id
        # Time range filter parameter. Represented in ISO8601 standard and must use UTC time, in the format yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time
        # Session state. Valid values:
        # 
        # 1. SessionStarting: The session is starting.
        # 
        # 2. SessionStartSuspended: Session startup is paused. Retry by initiating start again.
        # 
        # 3. SessionStarted: The session has started/is in use.
        # 
        # 4. SessionStartFailed: Session startup failed.
        # 
        # 5. SessionAbnormal: The session is abnormal after successful startup.
        # 
        # 6. SessionStopping: The session is stopping.
        # 
        # 7. SessionStopFailed: Session stop failed.
        self.state = state

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

