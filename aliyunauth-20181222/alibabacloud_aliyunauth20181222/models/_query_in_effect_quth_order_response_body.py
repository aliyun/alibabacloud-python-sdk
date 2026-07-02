# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliyunauth20181222 import models as main_models
from darabonba.model import DaraModel

class QueryInEffectQuthOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryInEffectQuthOrderResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.QueryInEffectQuthOrderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryInEffectQuthOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        list: List[main_models.QueryInEffectQuthOrderResponseBodyDataList] = None,
    ):
        self.count = count
        self.list = list

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
        if self.count is not None:
            result['Count'] = self.count

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryInEffectQuthOrderResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class QueryInEffectQuthOrderResponseBodyDataList(DaraModel):
    def __init__(
        self,
        auth_item_record_group_item_dtos: List[main_models.QueryInEffectQuthOrderResponseBodyDataListAuthItemRecordGroupItemDTOS] = None,
        created_time: str = None,
        last_modify_time: str = None,
        operate_times: List[main_models.QueryInEffectQuthOrderResponseBodyDataListOperateTimes] = None,
        order_vid: str = None,
        status: int = None,
    ):
        self.auth_item_record_group_item_dtos = auth_item_record_group_item_dtos
        self.created_time = created_time
        self.last_modify_time = last_modify_time
        self.operate_times = operate_times
        self.order_vid = order_vid
        self.status = status

    def validate(self):
        if self.auth_item_record_group_item_dtos:
            for v1 in self.auth_item_record_group_item_dtos:
                 if v1:
                    v1.validate()
        if self.operate_times:
            for v1 in self.operate_times:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthItemRecordGroupItemDTOS'] = []
        if self.auth_item_record_group_item_dtos is not None:
            for k1 in self.auth_item_record_group_item_dtos:
                result['AuthItemRecordGroupItemDTOS'].append(k1.to_map() if k1 else None)

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        result['OperateTimes'] = []
        if self.operate_times is not None:
            for k1 in self.operate_times:
                result['OperateTimes'].append(k1.to_map() if k1 else None)

        if self.order_vid is not None:
            result['OrderVid'] = self.order_vid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_item_record_group_item_dtos = []
        if m.get('AuthItemRecordGroupItemDTOS') is not None:
            for k1 in m.get('AuthItemRecordGroupItemDTOS'):
                temp_model = main_models.QueryInEffectQuthOrderResponseBodyDataListAuthItemRecordGroupItemDTOS()
                self.auth_item_record_group_item_dtos.append(temp_model.from_map(k1))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        self.operate_times = []
        if m.get('OperateTimes') is not None:
            for k1 in m.get('OperateTimes'):
                temp_model = main_models.QueryInEffectQuthOrderResponseBodyDataListOperateTimes()
                self.operate_times.append(temp_model.from_map(k1))

        if m.get('OrderVid') is not None:
            self.order_vid = m.get('OrderVid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class QueryInEffectQuthOrderResponseBodyDataListOperateTimes(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryInEffectQuthOrderResponseBodyDataListAuthItemRecordGroupItemDTOS(DaraModel):
    def __init__(
        self,
        authitem_id: str = None,
        gmt_created: str = None,
        msg: str = None,
        name: str = None,
        remark_data_json: str = None,
        status: int = None,
        vid: str = None,
    ):
        self.authitem_id = authitem_id
        self.gmt_created = gmt_created
        self.msg = msg
        self.name = name
        self.remark_data_json = remark_data_json
        self.status = status
        self.vid = vid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authitem_id is not None:
            result['AuthitemID'] = self.authitem_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.name is not None:
            result['Name'] = self.name

        if self.remark_data_json is not None:
            result['RemarkDataJson'] = self.remark_data_json

        if self.status is not None:
            result['Status'] = self.status

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthitemID') is not None:
            self.authitem_id = m.get('AuthitemID')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RemarkDataJson') is not None:
            self.remark_data_json = m.get('RemarkDataJson')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

