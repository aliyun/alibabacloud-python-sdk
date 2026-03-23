# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceReplicationResponseBody(DaraModel):
    def __init__(
        self,
        external_replication: str = None,
        gtid_executed: str = None,
        import_status: str = None,
        replication_delay: str = None,
        replication_error_message: str = None,
        replication_ip: str = None,
        replication_port: str = None,
        replication_source: str = None,
        replication_state: str = None,
        request_id: str = None,
        slave_status_list: List[main_models.DescribeDBInstanceReplicationResponseBodySlaveStatusList] = None,
    ):
        # Indicates whether the native replication mods is enabled. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.external_replication = external_replication
        # The executed global transaction identifier.
        self.gtid_executed = gtid_executed
        # Indicates whether full data has been successfully imported.
        self.import_status = import_status
        # The replication latency. Unit: seconds.
        self.replication_delay = replication_delay
        # The replication error message.
        self.replication_error_message = replication_error_message
        # The replication IP address.
        self.replication_ip = replication_ip
        # The replication port.
        self.replication_port = replication_port
        # The source of the native replication.
        self.replication_source = replication_source
        # The current replication status. Valid values:
        # 
        # *   **Running**
        # *   **Connecting**
        # *   **Stopped**
        # *   **Error**
        self.replication_state = replication_state
        # The request ID.
        self.request_id = request_id
        self.slave_status_list = slave_status_list

    def validate(self):
        if self.slave_status_list:
            for v1 in self.slave_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_replication is not None:
            result['ExternalReplication'] = self.external_replication

        if self.gtid_executed is not None:
            result['GtidExecuted'] = self.gtid_executed

        if self.import_status is not None:
            result['ImportStatus'] = self.import_status

        if self.replication_delay is not None:
            result['ReplicationDelay'] = self.replication_delay

        if self.replication_error_message is not None:
            result['ReplicationErrorMessage'] = self.replication_error_message

        if self.replication_ip is not None:
            result['ReplicationIp'] = self.replication_ip

        if self.replication_port is not None:
            result['ReplicationPort'] = self.replication_port

        if self.replication_source is not None:
            result['ReplicationSource'] = self.replication_source

        if self.replication_state is not None:
            result['ReplicationState'] = self.replication_state

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SlaveStatusList'] = []
        if self.slave_status_list is not None:
            for k1 in self.slave_status_list:
                result['SlaveStatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalReplication') is not None:
            self.external_replication = m.get('ExternalReplication')

        if m.get('GtidExecuted') is not None:
            self.gtid_executed = m.get('GtidExecuted')

        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')

        if m.get('ReplicationDelay') is not None:
            self.replication_delay = m.get('ReplicationDelay')

        if m.get('ReplicationErrorMessage') is not None:
            self.replication_error_message = m.get('ReplicationErrorMessage')

        if m.get('ReplicationIp') is not None:
            self.replication_ip = m.get('ReplicationIp')

        if m.get('ReplicationPort') is not None:
            self.replication_port = m.get('ReplicationPort')

        if m.get('ReplicationSource') is not None:
            self.replication_source = m.get('ReplicationSource')

        if m.get('ReplicationState') is not None:
            self.replication_state = m.get('ReplicationState')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.slave_status_list = []
        if m.get('SlaveStatusList') is not None:
            for k1 in m.get('SlaveStatusList'):
                temp_model = main_models.DescribeDBInstanceReplicationResponseBodySlaveStatusList()
                self.slave_status_list.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceReplicationResponseBodySlaveStatusList(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        executed_gtid_set: str = None,
        last_errno: int = None,
        last_io_errno: int = None,
        last_io_error: str = None,
        last_sql_errno: int = None,
        last_sql_error: str = None,
        master_host: str = None,
        master_user: str = None,
        master_uuid: str = None,
        replicate_do_db: str = None,
        replicate_do_table: str = None,
        replicate_ignore_db: str = None,
        replicate_ignore_table: str = None,
        replicate_wild_do_table: str = None,
        replicate_wild_ignore_table: str = None,
        seconds_behind_master: int = None,
        slave_io_running: str = None,
        slave_io_state: str = None,
        slave_sql_running: str = None,
        slave_sql_running_state: str = None,
    ):
        self.channel_name = channel_name
        self.executed_gtid_set = executed_gtid_set
        # 0表示无错误，其他值表示具体的错误代码
        self.last_errno = last_errno
        # 0表示无错误，其他值表示IO线程的错误代码
        self.last_io_errno = last_io_errno
        # IO线程的错误信息描述
        self.last_io_error = last_io_error
        # 0表示无错误，其他值表示SQL线程的错误代码
        self.last_sql_errno = last_sql_errno
        # SQL线程的错误信息描述
        self.last_sql_error = last_sql_error
        self.master_host = master_host
        self.master_user = master_user
        self.master_uuid = master_uuid
        self.replicate_do_db = replicate_do_db
        self.replicate_do_table = replicate_do_table
        self.replicate_ignore_db = replicate_ignore_db
        self.replicate_ignore_table = replicate_ignore_table
        self.replicate_wild_do_table = replicate_wild_do_table
        self.replicate_wild_ignore_table = replicate_wild_ignore_table
        self.seconds_behind_master = seconds_behind_master
        # Yes: 运行中，No: 已停止
        self.slave_io_running = slave_io_running
        self.slave_io_state = slave_io_state
        # Yes: 运行中，No: 已停止
        self.slave_sql_running = slave_sql_running
        self.slave_sql_running_state = slave_sql_running_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.executed_gtid_set is not None:
            result['ExecutedGtidSet'] = self.executed_gtid_set

        if self.last_errno is not None:
            result['LastErrno'] = self.last_errno

        if self.last_io_errno is not None:
            result['LastIoErrno'] = self.last_io_errno

        if self.last_io_error is not None:
            result['LastIoError'] = self.last_io_error

        if self.last_sql_errno is not None:
            result['LastSqlErrno'] = self.last_sql_errno

        if self.last_sql_error is not None:
            result['LastSqlError'] = self.last_sql_error

        if self.master_host is not None:
            result['MasterHost'] = self.master_host

        if self.master_user is not None:
            result['MasterUser'] = self.master_user

        if self.master_uuid is not None:
            result['MasterUuid'] = self.master_uuid

        if self.replicate_do_db is not None:
            result['ReplicateDoDb'] = self.replicate_do_db

        if self.replicate_do_table is not None:
            result['ReplicateDoTable'] = self.replicate_do_table

        if self.replicate_ignore_db is not None:
            result['ReplicateIgnoreDb'] = self.replicate_ignore_db

        if self.replicate_ignore_table is not None:
            result['ReplicateIgnoreTable'] = self.replicate_ignore_table

        if self.replicate_wild_do_table is not None:
            result['ReplicateWildDoTable'] = self.replicate_wild_do_table

        if self.replicate_wild_ignore_table is not None:
            result['ReplicateWildIgnoreTable'] = self.replicate_wild_ignore_table

        if self.seconds_behind_master is not None:
            result['SecondsBehindMaster'] = self.seconds_behind_master

        if self.slave_io_running is not None:
            result['SlaveIoRunning'] = self.slave_io_running

        if self.slave_io_state is not None:
            result['SlaveIoState'] = self.slave_io_state

        if self.slave_sql_running is not None:
            result['SlaveSqlRunning'] = self.slave_sql_running

        if self.slave_sql_running_state is not None:
            result['SlaveSqlRunningState'] = self.slave_sql_running_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ExecutedGtidSet') is not None:
            self.executed_gtid_set = m.get('ExecutedGtidSet')

        if m.get('LastErrno') is not None:
            self.last_errno = m.get('LastErrno')

        if m.get('LastIoErrno') is not None:
            self.last_io_errno = m.get('LastIoErrno')

        if m.get('LastIoError') is not None:
            self.last_io_error = m.get('LastIoError')

        if m.get('LastSqlErrno') is not None:
            self.last_sql_errno = m.get('LastSqlErrno')

        if m.get('LastSqlError') is not None:
            self.last_sql_error = m.get('LastSqlError')

        if m.get('MasterHost') is not None:
            self.master_host = m.get('MasterHost')

        if m.get('MasterUser') is not None:
            self.master_user = m.get('MasterUser')

        if m.get('MasterUuid') is not None:
            self.master_uuid = m.get('MasterUuid')

        if m.get('ReplicateDoDb') is not None:
            self.replicate_do_db = m.get('ReplicateDoDb')

        if m.get('ReplicateDoTable') is not None:
            self.replicate_do_table = m.get('ReplicateDoTable')

        if m.get('ReplicateIgnoreDb') is not None:
            self.replicate_ignore_db = m.get('ReplicateIgnoreDb')

        if m.get('ReplicateIgnoreTable') is not None:
            self.replicate_ignore_table = m.get('ReplicateIgnoreTable')

        if m.get('ReplicateWildDoTable') is not None:
            self.replicate_wild_do_table = m.get('ReplicateWildDoTable')

        if m.get('ReplicateWildIgnoreTable') is not None:
            self.replicate_wild_ignore_table = m.get('ReplicateWildIgnoreTable')

        if m.get('SecondsBehindMaster') is not None:
            self.seconds_behind_master = m.get('SecondsBehindMaster')

        if m.get('SlaveIoRunning') is not None:
            self.slave_io_running = m.get('SlaveIoRunning')

        if m.get('SlaveIoState') is not None:
            self.slave_io_state = m.get('SlaveIoState')

        if m.get('SlaveSqlRunning') is not None:
            self.slave_sql_running = m.get('SlaveSqlRunning')

        if m.get('SlaveSqlRunningState') is not None:
            self.slave_sql_running_state = m.get('SlaveSqlRunningState')

        return self

