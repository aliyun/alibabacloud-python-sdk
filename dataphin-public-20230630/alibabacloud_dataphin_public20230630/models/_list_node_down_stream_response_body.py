# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListNodeDownStreamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_info_list: List[main_models.ListNodeDownStreamResponseBodyNodeInfoList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_info_list = node_info_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_info_list:
            for v1 in self.node_info_list:
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

        if self.message is not None:
            result['Message'] = self.message

        result['NodeInfoList'] = []
        if self.node_info_list is not None:
            for k1 in self.node_info_list:
                result['NodeInfoList'].append(k1.to_map() if k1 else None)

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

        self.node_info_list = []
        if m.get('NodeInfoList') is not None:
            for k1 in m.get('NodeInfoList'):
                temp_model = main_models.ListNodeDownStreamResponseBodyNodeInfoList()
                self.node_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListNodeDownStreamResponseBodyNodeInfoList(DaraModel):
    def __init__(
        self,
        depth: int = None,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.depth = depth
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
        if self.depth is not None:
            result['Depth'] = self.depth

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
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

