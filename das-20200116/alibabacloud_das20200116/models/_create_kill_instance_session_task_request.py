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
        # The database account that has the permission to terminate sessions.
        # 
        # This parameter is required.
        self.db_user = db_user
        # The password of the database account.
        # 
        # This parameter is required.
        self.db_user_password = db_user_password
        # The list of accounts whose sessions will not be terminated.
        # 
        # > The data is in JSONArray format, such as [\\"DatabaseAccount1\\",\\"DatabaseAccount2\\"\\]. Separate multiple database accounts with commas (,).
        self.ignored_users = ignored_users
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to terminate all sessions.
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        # 
        # > When this parameter is set to **true**, sessions of accounts specified in the **IgnoredUsers** request parameter, sessions of Alibaba Cloud internal operations accounts, and **Binlog Dump** sessions are not terminated.
        # 
        # This parameter is required.
        self.kill_all_sessions = kill_all_sessions
        # The node ID.
        # 
        # > For PolarDB for MySQL instances, provide the node ID. If no node ID is provided and the **KillAllSessions** request parameter is set to **true** (terminate all sessions), the system traverses all nodes of the PolarDB for MySQL instance and terminates ongoing sessions on each node.
        self.node_id = node_id
        # The list of session IDs to be terminated.
        # 
        # > The data is in JSONArray format, such as [SessionID1,SessionID2\\]. Separate multiple session IDs with commas (,). If the **KillAllSessions** request parameter is set to **true** (terminate all sessions), this list is ignored.
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

