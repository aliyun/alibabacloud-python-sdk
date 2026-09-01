# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKBSyncLinkResponseBody(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        creation_time: str = None,
        description: str = None,
        im_platform: str = None,
        link_id: str = None,
        link_name: str = None,
        request_id: str = None,
        source_dir: str = None,
        sync_interval_minutes: int = None,
        sync_status: str = None,
    ):
        self.client_id = client_id
        self.creation_time = creation_time
        self.description = description
        self.im_platform = im_platform
        self.link_id = link_id
        self.link_name = link_name
        self.request_id = request_id
        self.source_dir = source_dir
        self.sync_interval_minutes = sync_interval_minutes
        self.sync_status = sync_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.im_platform is not None:
            result['ImPlatform'] = self.im_platform

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.link_name is not None:
            result['LinkName'] = self.link_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_dir is not None:
            result['SourceDir'] = self.source_dir

        if self.sync_interval_minutes is not None:
            result['SyncIntervalMinutes'] = self.sync_interval_minutes

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImPlatform') is not None:
            self.im_platform = m.get('ImPlatform')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('LinkName') is not None:
            self.link_name = m.get('LinkName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceDir') is not None:
            self.source_dir = m.get('SourceDir')

        if m.get('SyncIntervalMinutes') is not None:
            self.sync_interval_minutes = m.get('SyncIntervalMinutes')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        return self

