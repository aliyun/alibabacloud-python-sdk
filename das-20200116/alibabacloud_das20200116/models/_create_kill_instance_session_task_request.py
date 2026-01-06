# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKillInstanceSessionTaskRequest(DaraModel):
    def __init__(
        self,
        db_user: str = None,
        db_user_password: str = None,
        ignored_users: str = None,
        instance_id: str = None,
        kill_all_sessions: bool = None,
        node_id: str = None,
        session_ids: str = None,
    ):
        # The database account that has the permissions to terminate sessions.
        # 
        # This parameter is required.
        self.db_user = db_user
        # The password of the database account.
        # 
        # This parameter is required.
        self.db_user_password = db_user_password
        # The account whose sessions do not need to be terminated.
        # 
        # >  Set this parameter to a JSON array. Separate database accounts with commas (,). Example: [\\"Database account 1\\",\\"Database account 2\\"].
        self.ignored_users = ignored_users
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to terminate all sessions.
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If you set this parameter to **true**, sessions of the accounts that are specified by **IgnoredUsers**, sessions of internal O\\&M accounts of Alibaba Cloud, and **Binlog Dump** sessions are not terminated.
        # 
        # This parameter is required.
        self.kill_all_sessions = kill_all_sessions
        # The node ID.
        # 
        # >  This parameter must be specified if the database instance is a PolarDB for MySQL cluster. If you do not specify a node ID and set **KillAllSessions** to **true**, the system traverses all nodes in the PolarDB for MySQL cluster and terminates the active sessions on each node.
        self.node_id = node_id
        # The IDs of sessions that need to be terminated.
        # 
        # >  Set this parameter to a JSON array. Separate session IDs with commas (,). Example: [\\"Session ID1\\",\\"Session ID2\\"]. If **KillAllSessions** is set to **true**, this parameter does not take effect.
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_user is not None:
            result['DbUser'] = self.db_user

        if self.db_user_password is not None:
            result['DbUserPassword'] = self.db_user_password

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
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')

        if m.get('DbUserPassword') is not None:
            self.db_user_password = m.get('DbUserPassword')

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

