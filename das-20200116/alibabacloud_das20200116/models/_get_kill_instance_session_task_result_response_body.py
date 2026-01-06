# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetKillInstanceSessionTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetKillInstanceSessionTaskResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, Successful is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetKillInstanceSessionTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKillInstanceSessionTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        ignored_user_session_count: int = None,
        instance_id: str = None,
        kill_fail_count: int = None,
        kill_success_count: int = None,
        node_id: str = None,
        result: List[main_models.GetKillInstanceSessionTaskResultResponseBodyDataResult] = None,
        sessions: List[int] = None,
        task_id: str = None,
        task_state: str = None,
        user_id: str = None,
    ):
        # The number of ignored sessions, including sessions of the accounts that are specified by IgnoredUsers, sessions of internal O\\&M accounts of Alibaba Cloud, and **Binlog Dump** sessions.
        self.ignored_user_session_count = ignored_user_session_count
        # The instance ID.
        self.instance_id = instance_id
        # The number of sessions that failed to be terminated.
        self.kill_fail_count = kill_fail_count
        # The number of sessions that were terminated.
        self.kill_success_count = kill_success_count
        # The node ID.
        # 
        # >  This parameter is returned only if the instance is a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The details of the task that terminated sessions.
        self.result = result
        # The session IDs.
        # 
        # >  If all sessions are terminated, the IDs of all sessions on the instance or node are returned.
        self.sessions = sessions
        # The task ID.
        self.task_id = task_id
        # The state of the task that terminates sessions.
        # 
        # *   **RUNNING**: The task is in progress.
        # *   **SUCCESS**: The task is successful.
        # *   **FAILURE**: The task failed.
        # *   **ERROR**: Other errors occur.
        self.task_state = task_state
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignored_user_session_count is not None:
            result['IgnoredUserSessionCount'] = self.ignored_user_session_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kill_fail_count is not None:
            result['KillFailCount'] = self.kill_fail_count

        if self.kill_success_count is not None:
            result['KillSuccessCount'] = self.kill_success_count

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.sessions is not None:
            result['Sessions'] = self.sessions

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoredUserSessionCount') is not None:
            self.ignored_user_session_count = m.get('IgnoredUserSessionCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KillFailCount') is not None:
            self.kill_fail_count = m.get('KillFailCount')

        if m.get('KillSuccessCount') is not None:
            self.kill_success_count = m.get('KillSuccessCount')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetKillInstanceSessionTaskResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Sessions') is not None:
            self.sessions = m.get('Sessions')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetKillInstanceSessionTaskResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        command: str = None,
        db: str = None,
        host: str = None,
        id: int = None,
        info: str = None,
        reason: str = None,
        state: str = None,
        task_id: str = None,
        time: int = None,
        user: str = None,
    ):
        # Indicates whether the session is active.
        # 
        # > If the type of the command is Query or Execute and the session in the transaction is not terminated, the session is active.
        self.active = active
        # The type of the command executed in the session.
        self.command = command
        # The name of the database.
        self.db = db
        # The IP address and port number of the host that initiated the session.
        self.host = host
        # The session ID.
        self.id = id
        # The SQL statement executed in the session.
        self.info = info
        # The description of the session when the session was terminated.
        # 
        # *   **SESSION_KILLED**: The session is terminated.
        # *   **SESSION_EXPIRED**: The session has expired.
        # *   **SESSION_NO_PERMISSION**: The account used to terminate the session has insufficient permissions.
        # *   **SESSION_ACCOUNT_ERROR**: The account or password used to terminate the session is invalid.
        # *   **SESSION_IGNORED_USER**: The session of the account does not need to be terminated.
        # *   **SESSION_INTERNAL_USER_OR_COMMAND**: The session is a session initiated by or a command run by an Alibaba Cloud O\\&M account.
        # *   **SESSION_KILL_TASK_TIMEOUT**: Timeout occurs when the session is terminated.
        # *   **SESSION_OTHER_ERROR**: Other errors occurred.
        self.reason = reason
        # The status of the session.
        self.state = state
        # The ID of the subtask that terminates the session.
        self.task_id = task_id
        # The execution duration. Unit: seconds.
        self.time = time
        # The account of the database.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.command is not None:
            result['Command'] = self.command

        if self.db is not None:
            result['Db'] = self.db

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

        if self.info is not None:
            result['Info'] = self.info

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.time is not None:
            result['Time'] = self.time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

