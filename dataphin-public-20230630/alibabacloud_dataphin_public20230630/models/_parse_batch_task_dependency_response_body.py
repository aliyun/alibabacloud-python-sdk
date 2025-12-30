# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ParseBatchTaskDependencyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        parse_result: main_models.ParseBatchTaskDependencyResponseBodyParseResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.parse_result = parse_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.parse_result:
            self.parse_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.parse_result is not None:
            result['ParseResult'] = self.parse_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ParseResult') is not None:
            temp_model = main_models.ParseBatchTaskDependencyResponseBodyParseResult()
            self.parse_result = temp_model.from_map(m.get('ParseResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ParseBatchTaskDependencyResponseBodyParseResult(DaraModel):
    def __init__(
        self,
        depend_node_list: List[main_models.ParseBatchTaskDependencyResponseBodyParseResultDependNodeList] = None,
    ):
        self.depend_node_list = depend_node_list

    def validate(self):
        if self.depend_node_list:
            for v1 in self.depend_node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DependNodeList'] = []
        if self.depend_node_list is not None:
            for k1 in self.depend_node_list:
                result['DependNodeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.depend_node_list = []
        if m.get('DependNodeList') is not None:
            for k1 in m.get('DependNodeList'):
                temp_model = main_models.ParseBatchTaskDependencyResponseBodyParseResultDependNodeList()
                self.depend_node_list.append(temp_model.from_map(k1))

        return self

class ParseBatchTaskDependencyResponseBodyParseResultDependNodeList(DaraModel):
    def __init__(
        self,
        node_io_type: str = None,
        schedule_node_info_list: List[main_models.ParseBatchTaskDependencyResponseBodyParseResultDependNodeListScheduleNodeInfoList] = None,
    ):
        self.node_io_type = node_io_type
        self.schedule_node_info_list = schedule_node_info_list

    def validate(self):
        if self.schedule_node_info_list:
            for v1 in self.schedule_node_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_io_type is not None:
            result['NodeIoType'] = self.node_io_type

        result['ScheduleNodeInfoList'] = []
        if self.schedule_node_info_list is not None:
            for k1 in self.schedule_node_info_list:
                result['ScheduleNodeInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIoType') is not None:
            self.node_io_type = m.get('NodeIoType')

        self.schedule_node_info_list = []
        if m.get('ScheduleNodeInfoList') is not None:
            for k1 in m.get('ScheduleNodeInfoList'):
                temp_model = main_models.ParseBatchTaskDependencyResponseBodyParseResultDependNodeListScheduleNodeInfoList()
                self.schedule_node_info_list.append(temp_model.from_map(k1))

        return self

class ParseBatchTaskDependencyResponseBodyParseResultDependNodeListScheduleNodeInfoList(DaraModel):
    def __init__(
        self,
        field_list: List[str] = None,
        node_id: str = None,
        node_name: str = None,
        output_name: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        table_name: str = None,
    ):
        self.field_list = field_list
        self.node_id = node_id
        self.node_name = node_name
        self.output_name = output_name
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_list is not None:
            result['FieldList'] = self.field_list

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.output_name is not None:
            result['OutputName'] = self.output_name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OutputName') is not None:
            self.output_name = m.get('OutputName')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

