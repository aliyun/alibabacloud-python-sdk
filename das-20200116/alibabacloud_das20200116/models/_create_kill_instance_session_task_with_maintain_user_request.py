# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKillInstanceSessionTaskWithMaintainUserRequest(DaraModel):
    def __init__(
        self,
        ignored_users: str = None,
        instance_id: str = None,
        kill_all_sessions: bool = None,
        node_id: str = None,
        session_ids: str = None,
    ):
        self.ignored_users = ignored_users
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.kill_all_sessions = kill_all_sessions
        self.node_id = node_id
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignored_users is not None:
            result['IgnoredUsers'] = self.ignored_users

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kill_all_sessions is not None:
            result['KillAllSessions'] = self.kill_all_sessions

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.session_ids is not None:
            result['SessionIds'] = self.session_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoredUsers') is not None:
            self.ignored_users = m.get('IgnoredUsers')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KillAllSessions') is not None:
            self.kill_all_sessions = m.get('KillAllSessions')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SessionIds') is not None:
            self.session_ids = m.get('SessionIds')

        return self

