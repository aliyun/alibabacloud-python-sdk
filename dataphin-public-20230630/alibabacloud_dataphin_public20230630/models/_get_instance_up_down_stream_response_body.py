# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetInstanceUpDownStreamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_dag_info: main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_dag_info = instance_dag_info
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_dag_info:
            self.instance_dag_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_dag_info is not None:
            result['InstanceDagInfo'] = self.instance_dag_info.to_map()

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

        if m.get('InstanceDagInfo') is not None:
            temp_model = main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfo()
            self.instance_dag_info = temp_model.from_map(m.get('InstanceDagInfo'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceUpDownStreamResponseBodyInstanceDagInfo(DaraModel):
    def __init__(
        self,
        down_instance_list: List[main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList] = None,
        start_instance_list: List[main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList] = None,
        up_instance_list: List[main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList] = None,
    ):
        self.down_instance_list = down_instance_list
        self.start_instance_list = start_instance_list
        self.up_instance_list = up_instance_list

    def validate(self):
        if self.down_instance_list:
            for v1 in self.down_instance_list:
                 if v1:
                    v1.validate()
        if self.start_instance_list:
            for v1 in self.start_instance_list:
                 if v1:
                    v1.validate()
        if self.up_instance_list:
            for v1 in self.up_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DownInstanceList'] = []
        if self.down_instance_list is not None:
            for k1 in self.down_instance_list:
                result['DownInstanceList'].append(k1.to_map() if k1 else None)

        result['StartInstanceList'] = []
        if self.start_instance_list is not None:
            for k1 in self.start_instance_list:
                result['StartInstanceList'].append(k1.to_map() if k1 else None)

        result['UpInstanceList'] = []
        if self.up_instance_list is not None:
            for k1 in self.up_instance_list:
                result['UpInstanceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.down_instance_list = []
        if m.get('DownInstanceList') is not None:
            for k1 in m.get('DownInstanceList'):
                temp_model = main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList()
                self.down_instance_list.append(temp_model.from_map(k1))

        self.start_instance_list = []
        if m.get('StartInstanceList') is not None:
            for k1 in m.get('StartInstanceList'):
                temp_model = main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList()
                self.start_instance_list.append(temp_model.from_map(k1))

        self.up_instance_list = []
        if m.get('UpInstanceList') is not None:
            for k1 in m.get('UpInstanceList'):
                temp_model = main_models.GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList()
                self.up_instance_list.append(temp_model.from_map(k1))

        return self

class GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

