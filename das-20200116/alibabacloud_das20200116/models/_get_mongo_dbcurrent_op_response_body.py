# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetMongoDBCurrentOpResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetMongoDBCurrentOpResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The details of the sessions.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. Otherwise, an error message such as an error code is returned.
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
            temp_model = main_models.GetMongoDBCurrentOpResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMongoDBCurrentOpResponseBodyData(DaraModel):
    def __init__(
        self,
        session_list: List[main_models.GetMongoDBCurrentOpResponseBodyDataSessionList] = None,
        session_stat: main_models.GetMongoDBCurrentOpResponseBodyDataSessionStat = None,
        timestamp: int = None,
    ):
        # The sessions.
        self.session_list = session_list
        # The statistics on the sessions.
        self.session_stat = session_stat
        # The time when the database sessions were returned. The value is in the UNIX timestamp format. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        if self.session_list:
            for v1 in self.session_list:
                 if v1:
                    v1.validate()
        if self.session_stat:
            self.session_stat.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SessionList'] = []
        if self.session_list is not None:
            for k1 in self.session_list:
                result['SessionList'].append(k1.to_map() if k1 else None)

        if self.session_stat is not None:
            result['SessionStat'] = self.session_stat.to_map()

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.session_list = []
        if m.get('SessionList') is not None:
            for k1 in m.get('SessionList'):
                temp_model = main_models.GetMongoDBCurrentOpResponseBodyDataSessionList()
                self.session_list.append(temp_model.from_map(k1))

        if m.get('SessionStat') is not None:
            temp_model = main_models.GetMongoDBCurrentOpResponseBodyDataSessionStat()
            self.session_stat = temp_model.from_map(m.get('SessionStat'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMongoDBCurrentOpResponseBodyDataSessionStat(DaraModel):
    def __init__(
        self,
        active_count: int = None,
        client_stats: Dict[str, main_models.DataSessionStatClientStatsValue] = None,
        db_stats: Dict[str, main_models.DataSessionStatDbStatsValue] = None,
        longest_secs_running: int = None,
        total_count: int = None,
    ):
        # The number of active sessions.
        self.active_count = active_count
        # The statistics on the IP addresses of the clients.
        self.client_stats = client_stats
        # The statistics on the namespaces.
        self.db_stats = db_stats
        # The longest duration of a session. Unit: seconds.
        self.longest_secs_running = longest_secs_running
        # The total number of sessions.
        self.total_count = total_count

    def validate(self):
        if self.client_stats:
            for v1 in self.client_stats.values():
                 if v1:
                    v1.validate()
        if self.db_stats:
            for v1 in self.db_stats.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count

        result['ClientStats'] = {}
        if self.client_stats is not None:
            for k1, v1 in self.client_stats.items():
                result['ClientStats'][k1] = v1.to_map() if v1 else None

        result['DbStats'] = {}
        if self.db_stats is not None:
            for k1, v1 in self.db_stats.items():
                result['DbStats'][k1] = v1.to_map() if v1 else None

        if self.longest_secs_running is not None:
            result['LongestSecsRunning'] = self.longest_secs_running

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')

        self.client_stats = {}
        if m.get('ClientStats') is not None:
            for k1, v1 in m.get('ClientStats').items():
                temp_model = main_models.DataSessionStatClientStatsValue()
                self.client_stats[k1] = temp_model.from_map(v1)

        self.db_stats = {}
        if m.get('DbStats') is not None:
            for k1, v1 in m.get('DbStats').items():
                temp_model = main_models.DataSessionStatDbStatsValue()
                self.db_stats[k1] = temp_model.from_map(v1)

        if m.get('LongestSecsRunning') is not None:
            self.longest_secs_running = m.get('LongestSecsRunning')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMongoDBCurrentOpResponseBodyDataSessionList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        client: str = None,
        command: str = None,
        connection_id: int = None,
        desc: str = None,
        driver: str = None,
        host: str = None,
        kill_pending: bool = None,
        ns: str = None,
        op: str = None,
        op_id: str = None,
        os_arch: str = None,
        os_name: str = None,
        os_type: str = None,
        plan_summary: str = None,
        platform: str = None,
        secs_running: int = None,
        shard: str = None,
    ):
        # Indicates whether the operation is active. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.active = active
        # The IP address of the client.
        self.client = client
        # The document that contains the complete command object associated with the operation.
        self.command = command
        # The connection ID.
        self.connection_id = connection_id
        # The description of the connection.
        self.desc = desc
        # The driver for MongoDB.
        self.driver = driver
        # The host.
        self.host = host
        # Indicates whether the operation is marked as terminated.
        # 
        # *   **true**
        # *   **false**
        self.kill_pending = kill_pending
        # The namespace.
        self.ns = ns
        # The type of the operation.
        self.op = op
        # The operation ID.
        self.op_id = op_id
        # The architecture of the operating system.
        self.os_arch = os_arch
        # The name of the operating system.
        self.os_name = os_name
        # The type of the operating system.
        self.os_type = os_type
        # The description of the execution plan.
        self.plan_summary = plan_summary
        # The platform.
        self.platform = platform
        # The duration of the operation. Unit: seconds.
        self.secs_running = secs_running
        # The ID of the data shard.
        # 
        # >  This parameter is returned for sharded cluster instances.
        self.shard = shard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.client is not None:
            result['Client'] = self.client

        if self.command is not None:
            result['Command'] = self.command

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.driver is not None:
            result['Driver'] = self.driver

        if self.host is not None:
            result['Host'] = self.host

        if self.kill_pending is not None:
            result['KillPending'] = self.kill_pending

        if self.ns is not None:
            result['Ns'] = self.ns

        if self.op is not None:
            result['Op'] = self.op

        if self.op_id is not None:
            result['OpId'] = self.op_id

        if self.os_arch is not None:
            result['OsArch'] = self.os_arch

        if self.os_name is not None:
            result['OsName'] = self.os_name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.plan_summary is not None:
            result['PlanSummary'] = self.plan_summary

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.secs_running is not None:
            result['SecsRunning'] = self.secs_running

        if self.shard is not None:
            result['Shard'] = self.shard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Client') is not None:
            self.client = m.get('Client')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('KillPending') is not None:
            self.kill_pending = m.get('KillPending')

        if m.get('Ns') is not None:
            self.ns = m.get('Ns')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('OpId') is not None:
            self.op_id = m.get('OpId')

        if m.get('OsArch') is not None:
            self.os_arch = m.get('OsArch')

        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PlanSummary') is not None:
            self.plan_summary = m.get('PlanSummary')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SecsRunning') is not None:
            self.secs_running = m.get('SecsRunning')

        if m.get('Shard') is not None:
            self.shard = m.get('Shard')

        return self

