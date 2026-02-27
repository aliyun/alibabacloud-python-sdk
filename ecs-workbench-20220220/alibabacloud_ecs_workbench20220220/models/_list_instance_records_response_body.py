# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs_workbench20220220 import models as main_models
from darabonba.model import DaraModel

class ListInstanceRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: main_models.ListInstanceRecordsResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.ListInstanceRecordsResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstanceRecordsResponseBodyRoot(DaraModel):
    def __init__(
        self,
        record_list: List[main_models.ListInstanceRecordsResponseBodyRootRecordList] = None,
        total_count: int = None,
    ):
        self.record_list = record_list
        self.total_count = total_count

    def validate(self):
        if self.record_list:
            for v1 in self.record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordList'] = []
        if self.record_list is not None:
            for k1 in self.record_list:
                result['RecordList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_list = []
        if m.get('RecordList') is not None:
            for k1 in m.get('RecordList'):
                temp_model = main_models.ListInstanceRecordsResponseBodyRootRecordList()
                self.record_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceRecordsResponseBodyRootRecordList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        expire_time: str = None,
        gmt_create: str = None,
        instance_id: str = None,
        instance_record_url: str = None,
        record_duration_millis: int = None,
        status: str = None,
        terminal_session_token: str = None,
    ):
        self.account_id = account_id
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.instance_record_url = instance_record_url
        self.record_duration_millis = record_duration_millis
        self.status = status
        self.terminal_session_token = terminal_session_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_record_url is not None:
            result['InstanceRecordUrl'] = self.instance_record_url

        if self.record_duration_millis is not None:
            result['RecordDurationMillis'] = self.record_duration_millis

        if self.status is not None:
            result['Status'] = self.status

        if self.terminal_session_token is not None:
            result['TerminalSessionToken'] = self.terminal_session_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRecordUrl') is not None:
            self.instance_record_url = m.get('InstanceRecordUrl')

        if m.get('RecordDurationMillis') is not None:
            self.record_duration_millis = m.get('RecordDurationMillis')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TerminalSessionToken') is not None:
            self.terminal_session_token = m.get('TerminalSessionToken')

        return self

