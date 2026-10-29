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
        # The cloud application ID.
        self.app_id = app_id
        # The unique ID of the end client.
        self.client_id = client_id
        # The start time of the time range filter. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries to return on each page during a paging query.
        self.page_size = page_size
        # The ID of the cloud application patch package. If you set this parameter to origin, only sessions that use the original version of the application are returned.
        self.patch_id = patch_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The instance ID of the cloud application service.
        self.rendering_instance_id = rendering_instance_id
        # The session ID.
        self.session_id = session_id
        # The start time of the time range filter. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The session state. Valid values:
        # - SessionStarting: The session is starting.
        # - SessionStartSuspended: The session startup is suspended. You can retry by initiating a start request again.
        # - SessionStarted: The session is started or in use.
        # - SessionStartFailed: The session failed to start.
        # - SessionAbnormal: An exception occurred after the session was successfully started.
        # - SessionStopping: The session is stopping.
        # - SessionStopFailed: The session failed to stop.
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

