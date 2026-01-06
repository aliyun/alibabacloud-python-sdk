# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetMySQLAllSessionAsyncResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetMySQLAllSessionAsyncResponseBodyData = None,
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
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
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
            temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMySQLAllSessionAsyncResponseBodyData(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        fail: bool = None,
        is_finish: bool = None,
        result_id: str = None,
        session_data: main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionData = None,
        state: str = None,
        timestamp: int = None,
    ):
        # Indicates whether the asynchronous request was complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.complete = complete
        # Indicates whether the asynchronous request failed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fail = fail
        # Indicates whether the asynchronous request was complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_finish = is_finish
        # The ID of the asynchronous request.
        self.result_id = result_id
        # The session data.
        self.session_data = session_data
        # The state of the asynchronous request. Valid values:
        # 
        # *   **RUNNING**
        # *   **SUCCESS**
        # *   **FAIL**
        self.state = state
        # The time when the asynchronous request was made. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        if self.session_data:
            self.session_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['Complete'] = self.complete

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.session_data is not None:
            result['SessionData'] = self.session_data.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('SessionData') is not None:
            temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionData()
            self.session_data = temp_model.from_map(m.get('SessionData'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMySQLAllSessionAsyncResponseBodyDataSessionData(DaraModel):
    def __init__(
        self,
        active_session_count: int = None,
        client_stats: List[main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataClientStats] = None,
        db_stats: List[main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataDbStats] = None,
        max_active_time: int = None,
        session_list: List[main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataSessionList] = None,
        time_stamp: int = None,
        total_session_count: int = None,
        user_stats: List[main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataUserStats] = None,
    ):
        # The total number of active sessions.
        self.active_session_count = active_session_count
        # The sessions that are counted by client IP address.
        self.client_stats = client_stats
        # The sessions that are counted by database.
        self.db_stats = db_stats
        # The maximum execution duration of an active session. Unit: seconds.
        self.max_active_time = max_active_time
        # The sessions.
        self.session_list = session_list
        # The time when the session was queried. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.time_stamp = time_stamp
        # The total number of sessions.
        self.total_session_count = total_session_count
        # The sessions that are counted by database account.
        self.user_stats = user_stats

    def validate(self):
        if self.client_stats:
            for v1 in self.client_stats:
                 if v1:
                    v1.validate()
        if self.db_stats:
            for v1 in self.db_stats:
                 if v1:
                    v1.validate()
        if self.session_list:
            for v1 in self.session_list:
                 if v1:
                    v1.validate()
        if self.user_stats:
            for v1 in self.user_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count

        result['ClientStats'] = []
        if self.client_stats is not None:
            for k1 in self.client_stats:
                result['ClientStats'].append(k1.to_map() if k1 else None)

        result['DbStats'] = []
        if self.db_stats is not None:
            for k1 in self.db_stats:
                result['DbStats'].append(k1.to_map() if k1 else None)

        if self.max_active_time is not None:
            result['MaxActiveTime'] = self.max_active_time

        result['SessionList'] = []
        if self.session_list is not None:
            for k1 in self.session_list:
                result['SessionList'].append(k1.to_map() if k1 else None)

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_session_count is not None:
            result['TotalSessionCount'] = self.total_session_count

        result['UserStats'] = []
        if self.user_stats is not None:
            for k1 in self.user_stats:
                result['UserStats'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')

        self.client_stats = []
        if m.get('ClientStats') is not None:
            for k1 in m.get('ClientStats'):
                temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataClientStats()
                self.client_stats.append(temp_model.from_map(k1))

        self.db_stats = []
        if m.get('DbStats') is not None:
            for k1 in m.get('DbStats'):
                temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataDbStats()
                self.db_stats.append(temp_model.from_map(k1))

        if m.get('MaxActiveTime') is not None:
            self.max_active_time = m.get('MaxActiveTime')

        self.session_list = []
        if m.get('SessionList') is not None:
            for k1 in m.get('SessionList'):
                temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataSessionList()
                self.session_list.append(temp_model.from_map(k1))

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalSessionCount') is not None:
            self.total_session_count = m.get('TotalSessionCount')

        self.user_stats = []
        if m.get('UserStats') is not None:
            for k1 in m.get('UserStats'):
                temp_model = main_models.GetMySQLAllSessionAsyncResponseBodyDataSessionDataUserStats()
                self.user_stats.append(temp_model.from_map(k1))

        return self

class GetMySQLAllSessionAsyncResponseBodyDataSessionDataUserStats(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        key: str = None,
        thread_id_list: List[int] = None,
        total_count: int = None,
        user_list: List[str] = None,
    ):
        # The number of active sessions within the account.
        # 
        # >  If the type of the command executed in the session is Query or Execute and the session in the transaction is not terminated, the session is active.
        self.active_count = active_count
        # The database account.
        self.key = key
        # The IDs of the sessions within the account.
        self.thread_id_list = thread_id_list
        # The total number of sessions within the account.
        self.total_count = total_count
        # The database accounts to which the sessions belong.
        self.user_list = user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.key is not None:
            result['Key'] = self.key

        if self.thread_id_list is not None:
            result['ThreadIdList'] = self.thread_id_list

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_list is not None:
            result['UserList'] = self.user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ThreadIdList') is not None:
            self.thread_id_list = m.get('ThreadIdList')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')

        return self

class GetMySQLAllSessionAsyncResponseBodyDataSessionDataSessionList(DaraModel):
    def __init__(
        self,
        client: str = None,
        command: str = None,
        db_name: str = None,
        session_id: int = None,
        sql_template_id: str = None,
        sql_text: str = None,
        state: str = None,
        time: int = None,
        trx_duration: int = None,
        trx_id: str = None,
        user: str = None,
        user_client_alias: str = None,
    ):
        # The IP address of the client.
        self.client = client
        # The type of the command executed in the session.
        self.command = command
        # The database name.
        self.db_name = db_name
        # The session ID.
        self.session_id = session_id
        # The SQL template ID.
        # 
        # >  This parameter is returned only when you use a PolarDB-X 2.0 instance.
        self.sql_template_id = sql_template_id
        # The SQL statement executed in the session.
        self.sql_text = sql_text
        # The status of the session.
        self.state = state
        # The execution duration of the session. Unit: seconds.
        self.time = time
        # The duration of the transaction. Unit: seconds.
        self.trx_duration = trx_duration
        # The ID of the transaction to which the session belongs.
        self.trx_id = trx_id
        # The username of the database account.
        self.user = user
        # The alias of the IP address of the client.
        self.user_client_alias = user_client_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client is not None:
            result['Client'] = self.client

        if self.command is not None:
            result['Command'] = self.command

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sql_template_id is not None:
            result['SqlTemplateId'] = self.sql_template_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.state is not None:
            result['State'] = self.state

        if self.time is not None:
            result['Time'] = self.time

        if self.trx_duration is not None:
            result['TrxDuration'] = self.trx_duration

        if self.trx_id is not None:
            result['TrxId'] = self.trx_id

        if self.user is not None:
            result['User'] = self.user

        if self.user_client_alias is not None:
            result['UserClientAlias'] = self.user_client_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Client') is not None:
            self.client = m.get('Client')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SqlTemplateId') is not None:
            self.sql_template_id = m.get('SqlTemplateId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TrxDuration') is not None:
            self.trx_duration = m.get('TrxDuration')

        if m.get('TrxId') is not None:
            self.trx_id = m.get('TrxId')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('UserClientAlias') is not None:
            self.user_client_alias = m.get('UserClientAlias')

        return self

class GetMySQLAllSessionAsyncResponseBodyDataSessionDataDbStats(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        key: str = None,
        thread_id_list: List[int] = None,
        total_count: int = None,
        user_list: List[str] = None,
    ):
        # The number of active sessions of the database.
        # 
        # >  If the type of the command executed in the session is Query or Execute and the session in the transaction is not terminated, the session is active.
        self.active_count = active_count
        # The database name.
        self.key = key
        # The IDs of the sessions of the database.
        self.thread_id_list = thread_id_list
        # The total number of sessions of the database.
        self.total_count = total_count
        # The database accounts to which the sessions belong.
        self.user_list = user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.key is not None:
            result['Key'] = self.key

        if self.thread_id_list is not None:
            result['ThreadIdList'] = self.thread_id_list

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_list is not None:
            result['UserList'] = self.user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ThreadIdList') is not None:
            self.thread_id_list = m.get('ThreadIdList')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')

        return self

class GetMySQLAllSessionAsyncResponseBodyDataSessionDataClientStats(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        key: str = None,
        thread_id_list: List[int] = None,
        total_count: int = None,
        user_list: List[str] = None,
    ):
        # The number of active sessions that belong to the client IP address.
        # 
        # >  If the type of the command executed in the session is Query or Execute and the session in the transaction is not terminated, the session is active.
        self.active_count = active_count
        # The IP address of the client.
        self.key = key
        # The IDs of the sessions that belong to the client IP address.
        self.thread_id_list = thread_id_list
        # The total number of sessions that belong to the client IP address.
        self.total_count = total_count
        # The database accounts to which the sessions belong.
        self.user_list = user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        if self.key is not None:
            result['Key'] = self.key

        if self.thread_id_list is not None:
            result['ThreadIdList'] = self.thread_id_list

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_list is not None:
            result['UserList'] = self.user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ThreadIdList') is not None:
            self.thread_id_list = m.get('ThreadIdList')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')

        return self

