# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetNodeUpDownStreamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_dag_info: main_models.GetNodeUpDownStreamResponseBodyNodeDagInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_dag_info = node_dag_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_dag_info:
            self.node_dag_info.validate()

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

        if self.node_dag_info is not None:
            result['NodeDagInfo'] = self.node_dag_info.to_map()

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

        if m.get('NodeDagInfo') is not None:
            temp_model = main_models.GetNodeUpDownStreamResponseBodyNodeDagInfo()
            self.node_dag_info = temp_model.from_map(m.get('NodeDagInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNodeUpDownStreamResponseBodyNodeDagInfo(DaraModel):
    def __init__(
        self,
        down_stream_node_list: List[main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList] = None,
        start_node_list: List[main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList] = None,
        up_stream_node_list: List[main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList] = None,
    ):
        self.down_stream_node_list = down_stream_node_list
        self.start_node_list = start_node_list
        self.up_stream_node_list = up_stream_node_list

    def validate(self):
        if self.down_stream_node_list:
            for v1 in self.down_stream_node_list:
                 if v1:
                    v1.validate()
        if self.start_node_list:
            for v1 in self.start_node_list:
                 if v1:
                    v1.validate()
        if self.up_stream_node_list:
            for v1 in self.up_stream_node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DownStreamNodeList'] = []
        if self.down_stream_node_list is not None:
            for k1 in self.down_stream_node_list:
                result['DownStreamNodeList'].append(k1.to_map() if k1 else None)

        result['StartNodeList'] = []
        if self.start_node_list is not None:
            for k1 in self.start_node_list:
                result['StartNodeList'].append(k1.to_map() if k1 else None)

        result['UpStreamNodeList'] = []
        if self.up_stream_node_list is not None:
            for k1 in self.up_stream_node_list:
                result['UpStreamNodeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.down_stream_node_list = []
        if m.get('DownStreamNodeList') is not None:
            for k1 in m.get('DownStreamNodeList'):
                temp_model = main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList()
                self.down_stream_node_list.append(temp_model.from_map(k1))

        self.start_node_list = []
        if m.get('StartNodeList') is not None:
            for k1 in m.get('StartNodeList'):
                temp_model = main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList()
                self.start_node_list.append(temp_model.from_map(k1))

        self.up_stream_node_list = []
        if m.get('UpStreamNodeList') is not None:
            for k1 in m.get('UpStreamNodeList'):
                temp_model = main_models.GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList()
                self.up_stream_node_list.append(temp_model.from_map(k1))

        return self

class GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
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
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
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
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
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
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

