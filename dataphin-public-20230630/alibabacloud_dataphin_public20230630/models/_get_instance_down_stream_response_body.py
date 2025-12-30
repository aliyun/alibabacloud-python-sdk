# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetInstanceDownStreamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_relation_list: List[main_models.GetInstanceDownStreamResponseBodyInstanceRelationList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_relation_list = instance_relation_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_relation_list:
            for v1 in self.instance_relation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['InstanceRelationList'] = []
        if self.instance_relation_list is not None:
            for k1 in self.instance_relation_list:
                result['InstanceRelationList'].append(k1.to_map() if k1 else None)

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.instance_relation_list = []
        if m.get('InstanceRelationList') is not None:
            for k1 in m.get('InstanceRelationList'):
                temp_model = main_models.GetInstanceDownStreamResponseBodyInstanceRelationList()
                self.instance_relation_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceDownStreamResponseBodyInstanceRelationList(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        extend_info: str = None,
        field_instance_list: List[main_models.GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList] = None,
        instance_info: main_models.GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo = None,
        run_status: str = None,
        select_status: str = None,
        select_status_cause: str = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.extend_info = extend_info
        self.field_instance_list = field_instance_list
        self.instance_info = instance_info
        self.run_status = run_status
        self.select_status = select_status
        self.select_status_cause = select_status_cause

    def validate(self):
        if self.field_instance_list:
            for v1 in self.field_instance_list:
                 if v1:
                    v1.validate()
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        result['FieldInstanceList'] = []
        if self.field_instance_list is not None:
            for k1 in self.field_instance_list:
                result['FieldInstanceList'].append(k1.to_map() if k1 else None)

        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        if self.select_status is not None:
            result['SelectStatus'] = self.select_status

        if self.select_status_cause is not None:
            result['SelectStatusCause'] = self.select_status_cause

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        self.field_instance_list = []
        if m.get('FieldInstanceList') is not None:
            for k1 in m.get('FieldInstanceList'):
                temp_model = main_models.GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList()
                self.field_instance_list.append(temp_model.from_map(k1))

        if m.get('InstanceInfo') is not None:
            temp_model = main_models.GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo()
            self.instance_info = temp_model.from_map(m.get('InstanceInfo'))

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        if m.get('SelectStatus') is not None:
            self.select_status = m.get('SelectStatus')

        if m.get('SelectStatusCause') is not None:
            self.select_status_cause = m.get('SelectStatusCause')

        return self

class GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList(DaraModel):
    def __init__(
        self,
        field_instance_id: str = None,
        run_status: str = None,
        select_status: str = None,
    ):
        self.field_instance_id = field_instance_id
        self.run_status = run_status
        self.select_status = select_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id is not None:
            result['FieldInstanceId'] = self.field_instance_id

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        if self.select_status is not None:
            result['SelectStatus'] = self.select_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceId') is not None:
            self.field_instance_id = m.get('FieldInstanceId')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        if m.get('SelectStatus') is not None:
            self.select_status = m.get('SelectStatus')

        return self

