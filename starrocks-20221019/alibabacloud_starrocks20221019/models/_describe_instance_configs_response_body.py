# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceConfigsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.DescribeInstanceConfigsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeInstanceConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstanceConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        allow_modify: str = None,
        config_key: str = None,
        config_type: str = None,
        config_value: str = None,
        custom: bool = None,
        default_node_group: bool = None,
        default_value: str = None,
        description: str = None,
        description_en: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
        restart: bool = None,
        unit: str = None,
        value_range: str = None,
        value_type: str = None,
    ):
        self.allow_modify = allow_modify
        self.config_key = config_key
        self.config_type = config_type
        self.config_value = config_value
        self.custom = custom
        self.default_node_group = default_node_group
        self.default_value = default_value
        self.description = description
        self.description_en = description_en
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.restart = restart
        self.unit = unit
        self.value_range = value_range
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_modify is not None:
            result['AllowModify'] = self.allow_modify

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.custom is not None:
            result['Custom'] = self.custom

        if self.default_node_group is not None:
            result['DefaultNodeGroup'] = self.default_node_group

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value_range is not None:
            result['ValueRange'] = self.value_range

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowModify') is not None:
            self.allow_modify = m.get('AllowModify')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Custom') is not None:
            self.custom = m.get('Custom')

        if m.get('DefaultNodeGroup') is not None:
            self.default_node_group = m.get('DefaultNodeGroup')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('ValueRange') is not None:
            self.value_range = m.get('ValueRange')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

