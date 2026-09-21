# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeadLockDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        # The returned status code.
        self.code = code
        # The returned data in JSON format:
        # 
        # - accountId: the user ID.
        # 
        # - textId: the deadlock text ID.
        # 
        # - gmtModified: the time when the diagnosis was generated.
        # 
        # - originText: the original deadlock text of LATEST DETECTED DEADLOCK or the original deadlock text in the error log.
        # 
        # - deadlock: the deadlock details:
        # 
        #   - occurTime: the time when the deadlock occurred.
        # 
        #   - originTextId: the deadlock text ID.
        # 
        #   - rollbackTrxId: the ID of the rolled back transaction.
        # 
        #   - transactions:
        # 
        #     - deadlockIdInDB: the deadlock ID in the database.
        # 
        #     - ip: the access IP address.
        # 
        #     - queryId: the query ID.
        # 
        #     - queryType: the query type.
        # 
        #     - relatedTables: the related tables.
        # 
        #     - tableNamesString: the related tables.
        # 
        #     - sqlText: the SQL text.
        # 
        #     - threadId: the thread ID.
        # 
        #     - transactionId: the transaction ID.
        # 
        #     - trxIdInLock: the transaction ID in the deadlock.
        # 
        #     - userName: the database username.
        # 
        #     - waitLockIndexName: the name of the index for which the lock is waiting.
        # 
        #     - waitLockMode: the type of the lock that is waiting.
        # 
        #     - lockWait: the waiting lock.
        # 
        #     - holdLockIndexName: the name of the index for which the lock is held.
        # 
        #     - holdLockMode: the type of the lock that is held.
        # 
        #     - lockHold: the held lock.
        # 
        #   - trxNum: the number of transactions.
        # 
        # - gmtCreate: the time when the diagnosis was created.
        # 
        # - nodeId: the node ID.
        # 
        # - uuid: the instance ID.
        self.data = data
        # The response message.
        # 
        # > - When the request is successful, **Successful** is returned.
        # >
        # > - When the request fails, error information (such as error codes) is returned.
        self.message = message
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The reserved parameter.
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

