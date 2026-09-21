# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticFSVolumeConfig(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        agentic_space_id: str = None,
        file_system_id: str = None,
        group_id: int = None,
        server_addr: str = None,
        user_id: int = None,
    ):
        # The access point ID.
        self.access_point_id = access_point_id
        # The workspace ID.
        self.agentic_space_id = agentic_space_id
        # The file system ID.
        self.file_system_id = file_system_id
        # The group ID for local mounting.
        self.group_id = group_id
        # The AgenticFS access point address.
        self.server_addr = server_addr
        # The user ID for local mounting.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['accessPointID'] = self.access_point_id

        if self.agentic_space_id is not None:
            result['agenticSpaceID'] = self.agentic_space_id

        if self.file_system_id is not None:
            result['fileSystemID'] = self.file_system_id

        if self.group_id is not None:
            result['groupID'] = self.group_id

        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessPointID') is not None:
            self.access_point_id = m.get('accessPointID')

        if m.get('agenticSpaceID') is not None:
            self.agentic_space_id = m.get('agenticSpaceID')

        if m.get('fileSystemID') is not None:
            self.file_system_id = m.get('fileSystemID')

        if m.get('groupID') is not None:
            self.group_id = m.get('groupID')

        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

