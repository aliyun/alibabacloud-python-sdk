# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetEndpointSwitchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEndpointSwitchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetEndpointSwitchTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class GetEndpointSwitchTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        db_link_id: int = None,
        err_msg: str = None,
        ori_uuid: str = None,
        status: str = None,
        task_id: str = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_link_id = db_link_id
        self.err_msg = err_msg
        self.ori_uuid = ori_uuid
        self.status = status
        self.task_id = task_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DbLinkId') is not None:
            self.db_link_id = m.get('DbLinkId')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('OriUuid') is not None:
            self.ori_uuid = m.get('OriUuid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

