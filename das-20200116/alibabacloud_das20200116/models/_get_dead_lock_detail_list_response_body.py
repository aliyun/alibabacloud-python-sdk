# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetDeadLockDetailListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDeadLockDetailListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request is successful, **Successful** is returned. Otherwise, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
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
            temp_model = main_models.GetDeadLockDetailListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDeadLockDetailListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetDeadLockDetailListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The details of the data returned.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetDeadLockDetailListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetDeadLockDetailListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        block_process_list: List[main_models.GetDeadLockDetailListResponseBodyDataListBlockProcessList] = None,
        client_app: str = None,
        database_name: str = None,
        host_name: str = None,
        last_tran_started: int = None,
        lock_mode: str = None,
        log_used: int = None,
        login_name: str = None,
        object_owned: str = None,
        object_requested: str = None,
        own_mode: str = None,
        spid: int = None,
        sql_text: str = None,
        status: str = None,
        victim: int = None,
        wait_mode: str = None,
        wait_resource: str = None,
        wait_resource_description: str = None,
    ):
        # The time when the data was collected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.batch_id = batch_id
        # The blocking details of the instance. The details are information about the session that caused the lock.
        self.block_process_list = block_process_list
        # The name of the client.
        self.client_app = client_app
        # The name of the database.
        self.database_name = database_name
        # The hostname.
        self.host_name = host_name
        # The time when the transaction was started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_tran_started = last_tran_started
        # The mode of the lock. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.lock_mode = lock_mode
        # The size of the logs generated in the session. Unit: bytes.
        self.log_used = log_used
        # The logon name of the user.
        self.login_name = login_name
        # The locked object.
        self.object_owned = object_owned
        # The object that the transaction requested to lock.
        self.object_requested = object_requested
        # The lock mode held by the session. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.own_mode = own_mode
        # The ID of the session in which the transaction is started.
        self.spid = spid
        # The SQL statement.
        self.sql_text = sql_text
        # The status of the transaction.
        self.status = status
        # Indicates whether the session is the victim of the deadlock. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.victim = victim
        # The lock mode requested by the session. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.wait_mode = wait_mode
        # The resources requested by the transaction.
        self.wait_resource = wait_resource
        # The details of the resources requested by the transaction.
        self.wait_resource_description = wait_resource_description

    def validate(self):
        if self.block_process_list:
            for v1 in self.block_process_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        result['BlockProcessList'] = []
        if self.block_process_list is not None:
            for k1 in self.block_process_list:
                result['BlockProcessList'].append(k1.to_map() if k1 else None)

        if self.client_app is not None:
            result['ClientApp'] = self.client_app

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.last_tran_started is not None:
            result['LastTranStarted'] = self.last_tran_started

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.log_used is not None:
            result['LogUsed'] = self.log_used

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.object_owned is not None:
            result['ObjectOwned'] = self.object_owned

        if self.object_requested is not None:
            result['ObjectRequested'] = self.object_requested

        if self.own_mode is not None:
            result['OwnMode'] = self.own_mode

        if self.spid is not None:
            result['Spid'] = self.spid

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.status is not None:
            result['Status'] = self.status

        if self.victim is not None:
            result['Victim'] = self.victim

        if self.wait_mode is not None:
            result['WaitMode'] = self.wait_mode

        if self.wait_resource is not None:
            result['WaitResource'] = self.wait_resource

        if self.wait_resource_description is not None:
            result['WaitResourceDescription'] = self.wait_resource_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        self.block_process_list = []
        if m.get('BlockProcessList') is not None:
            for k1 in m.get('BlockProcessList'):
                temp_model = main_models.GetDeadLockDetailListResponseBodyDataListBlockProcessList()
                self.block_process_list.append(temp_model.from_map(k1))

        if m.get('ClientApp') is not None:
            self.client_app = m.get('ClientApp')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('LastTranStarted') is not None:
            self.last_tran_started = m.get('LastTranStarted')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LogUsed') is not None:
            self.log_used = m.get('LogUsed')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('ObjectOwned') is not None:
            self.object_owned = m.get('ObjectOwned')

        if m.get('ObjectRequested') is not None:
            self.object_requested = m.get('ObjectRequested')

        if m.get('OwnMode') is not None:
            self.own_mode = m.get('OwnMode')

        if m.get('Spid') is not None:
            self.spid = m.get('Spid')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Victim') is not None:
            self.victim = m.get('Victim')

        if m.get('WaitMode') is not None:
            self.wait_mode = m.get('WaitMode')

        if m.get('WaitResource') is not None:
            self.wait_resource = m.get('WaitResource')

        if m.get('WaitResourceDescription') is not None:
            self.wait_resource_description = m.get('WaitResourceDescription')

        return self

class GetDeadLockDetailListResponseBodyDataListBlockProcessList(DaraModel):
    def __init__(
        self,
        client_app: str = None,
        database_name: str = None,
        host_name: str = None,
        last_tran_started: int = None,
        lock_mode: str = None,
        log_used: int = None,
        login_name: str = None,
        object_owned: str = None,
        object_requested: str = None,
        own_mode: str = None,
        spid: int = None,
        sql_text: str = None,
        status: str = None,
        victim: int = None,
        wait_mode: str = None,
        wait_resource: str = None,
        wait_resource_description: str = None,
    ):
        # The name of the client that initiates the transaction in the session.
        self.client_app = client_app
        # The name of the database.
        self.database_name = database_name
        # The hostname.
        self.host_name = host_name
        # The time when the transaction was started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_tran_started = last_tran_started
        # The mode of the lock. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.lock_mode = lock_mode
        # The size of the logs generated in the session. Unit: bytes.
        self.log_used = log_used
        # The logon name of the user.
        self.login_name = login_name
        # The locked object.
        self.object_owned = object_owned
        # The object that the transaction requested to lock.
        self.object_requested = object_requested
        # The lock mode held by the session. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.own_mode = own_mode
        # The ID of the session in which the transaction is started.
        self.spid = spid
        # The SQL statement.
        self.sql_text = sql_text
        # The status of the transaction.
        self.status = status
        # Indicates whether the session is the victim of the deadlock. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.victim = victim
        # The lock mode requested by the session. For more information, see [Lock modes](https://help.aliyun.com/document_detail/2362804.html).
        self.wait_mode = wait_mode
        # The resources requested by the transaction.
        self.wait_resource = wait_resource
        # The details of the resources requested by the transaction.
        self.wait_resource_description = wait_resource_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_app is not None:
            result['ClientApp'] = self.client_app

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.last_tran_started is not None:
            result['LastTranStarted'] = self.last_tran_started

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.log_used is not None:
            result['LogUsed'] = self.log_used

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.object_owned is not None:
            result['ObjectOwned'] = self.object_owned

        if self.object_requested is not None:
            result['ObjectRequested'] = self.object_requested

        if self.own_mode is not None:
            result['OwnMode'] = self.own_mode

        if self.spid is not None:
            result['Spid'] = self.spid

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.status is not None:
            result['Status'] = self.status

        if self.victim is not None:
            result['Victim'] = self.victim

        if self.wait_mode is not None:
            result['WaitMode'] = self.wait_mode

        if self.wait_resource is not None:
            result['WaitResource'] = self.wait_resource

        if self.wait_resource_description is not None:
            result['WaitResourceDescription'] = self.wait_resource_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientApp') is not None:
            self.client_app = m.get('ClientApp')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('LastTranStarted') is not None:
            self.last_tran_started = m.get('LastTranStarted')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LogUsed') is not None:
            self.log_used = m.get('LogUsed')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('ObjectOwned') is not None:
            self.object_owned = m.get('ObjectOwned')

        if m.get('ObjectRequested') is not None:
            self.object_requested = m.get('ObjectRequested')

        if m.get('OwnMode') is not None:
            self.own_mode = m.get('OwnMode')

        if m.get('Spid') is not None:
            self.spid = m.get('Spid')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Victim') is not None:
            self.victim = m.get('Victim')

        if m.get('WaitMode') is not None:
            self.wait_mode = m.get('WaitMode')

        if m.get('WaitResource') is not None:
            self.wait_resource = m.get('WaitResource')

        if m.get('WaitResourceDescription') is not None:
            self.wait_resource_description = m.get('WaitResourceDescription')

        return self

