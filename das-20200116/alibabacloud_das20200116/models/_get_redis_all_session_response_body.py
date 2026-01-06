# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetRedisAllSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetRedisAllSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The session data.
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
            temp_model = main_models.GetRedisAllSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRedisAllSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        sessions: List[main_models.GetRedisAllSessionResponseBodyDataSessions] = None,
        source_stats: List[main_models.GetRedisAllSessionResponseBodyDataSourceStats] = None,
        timestamp: int = None,
        total: int = None,
    ):
        # The information about the sessions.
        self.sessions = sessions
        # The statistics on the access source.
        self.source_stats = source_stats
        # The time when the instance sessions were returned. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The total number of sessions.
        self.total = total

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()
        if self.source_stats:
            for v1 in self.source_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        result['SourceStats'] = []
        if self.source_stats is not None:
            for k1 in self.source_stats:
                result['SourceStats'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.GetRedisAllSessionResponseBodyDataSessions()
                self.sessions.append(temp_model.from_map(k1))

        self.source_stats = []
        if m.get('SourceStats') is not None:
            for k1 in m.get('SourceStats'):
                temp_model = main_models.GetRedisAllSessionResponseBodyDataSourceStats()
                self.source_stats.append(temp_model.from_map(k1))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetRedisAllSessionResponseBodyDataSourceStats(DaraModel):
    def __init__(
        self,
        count: str = None,
        ids: List[int] = None,
        key: str = None,
    ):
        # The total number of sessions from the access source.
        self.count = count
        # The client IDs.
        self.ids = ids
        # The access source.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class GetRedisAllSessionResponseBodyDataSessions(DaraModel):
    def __init__(
        self,
        addr: str = None,
        age: str = None,
        client: str = None,
        client_desc: str = None,
        cmd: str = None,
        db: int = None,
        events: str = None,
        fd: int = None,
        flags: str = None,
        id: int = None,
        idle: int = None,
        multi: int = None,
        name: str = None,
        node_id: str = None,
        obl: int = None,
        oll: int = None,
        omem: int = None,
        psub: int = None,
        qbuf: int = None,
        qbuf_free: int = None,
        sub: int = None,
    ):
        # The IP address and port number of the client.
        self.addr = addr
        # The connection duration of the session. Unit: seconds.
        self.age = age
        # The IP address of the client.
        self.client = client
        # The alias of the client.
        self.client_desc = client_desc
        # The command that was last run.
        self.cmd = cmd
        # The ID of the database that the client is using.
        self.db = db
        # The file descriptor event. Valid values:
        # 
        # *   **r**: Client sockets are readable in the event loop.
        # *   **w**: Client sockets are writable in the event loop.
        self.events = events
        # The file descriptor that is used by sockets.
        self.fd = fd
        # The client flag. Valid values:
        # 
        # *   **A**: The connection needs to be closed at the earliest opportunity.
        # *   **b**: The client is waiting for blocked events.
        # *   **c**: The connection is closed after all replies are written.
        # *   **d**: The monitored keys have been modified, and the `EXEC` command is about to fail.
        # *   **i**: The client is waiting for VM I/O operations. This value is no longer used.
        # *   **M**: The client is the primary node.
        # *   **N**: No special flags are configured.
        # *   **O**: The client is in monitor mode.
        # *   **r**: The client is a cluster node in read-only mode.
        # *   **S**: The client is a replica node in normal mode.
        # *   **u**: The client is not blocked.
        # *   **U**: The client is connected by using UNIX domain sockets.
        # *   **x**: The client is executing a transaction.
        self.flags = flags
        # The client ID.
        self.id = id
        # The duration during which the session is in the idle state. Unit: seconds.
        self.idle = idle
        # The number of commands in `MULTI` or `EXEC`.
        self.multi = multi
        # The name of the client.
        self.name = name
        # The node ID.
        self.node_id = node_id
        # The size of the fixed output buffer. Unit: bytes.
        self.obl = obl
        # The number of objects contained in the output list.
        self.oll = oll
        # The size of the output buffer. Unit: bytes.
        self.omem = omem
        # The number of subscriptions that match the pattern.
        self.psub = psub
        # The size of the input buffer. Unit: bytes.
        self.qbuf = qbuf
        # The remaining size of the input buffer. Unit: bytes.
        self.qbuf_free = qbuf_free
        # The number of subscribed channels.
        self.sub = sub

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.age is not None:
            result['Age'] = self.age

        if self.client is not None:
            result['Client'] = self.client

        if self.client_desc is not None:
            result['ClientDesc'] = self.client_desc

        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.db is not None:
            result['Db'] = self.db

        if self.events is not None:
            result['Events'] = self.events

        if self.fd is not None:
            result['Fd'] = self.fd

        if self.flags is not None:
            result['Flags'] = self.flags

        if self.id is not None:
            result['Id'] = self.id

        if self.idle is not None:
            result['Idle'] = self.idle

        if self.multi is not None:
            result['Multi'] = self.multi

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.obl is not None:
            result['Obl'] = self.obl

        if self.oll is not None:
            result['Oll'] = self.oll

        if self.omem is not None:
            result['Omem'] = self.omem

        if self.psub is not None:
            result['Psub'] = self.psub

        if self.qbuf is not None:
            result['Qbuf'] = self.qbuf

        if self.qbuf_free is not None:
            result['QbufFree'] = self.qbuf_free

        if self.sub is not None:
            result['Sub'] = self.sub

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('Age') is not None:
            self.age = m.get('Age')

        if m.get('Client') is not None:
            self.client = m.get('Client')

        if m.get('ClientDesc') is not None:
            self.client_desc = m.get('ClientDesc')

        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('Fd') is not None:
            self.fd = m.get('Fd')

        if m.get('Flags') is not None:
            self.flags = m.get('Flags')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Idle') is not None:
            self.idle = m.get('Idle')

        if m.get('Multi') is not None:
            self.multi = m.get('Multi')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Obl') is not None:
            self.obl = m.get('Obl')

        if m.get('Oll') is not None:
            self.oll = m.get('Oll')

        if m.get('Omem') is not None:
            self.omem = m.get('Omem')

        if m.get('Psub') is not None:
            self.psub = m.get('Psub')

        if m.get('Qbuf') is not None:
            self.qbuf = m.get('Qbuf')

        if m.get('QbufFree') is not None:
            self.qbuf_free = m.get('QbufFree')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        return self

