# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetDataSourceOrderConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDataSourceOrderConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetDataSourceOrderConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataSourceOrderConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        total_doc_size: int = None,
        user_config_data_source_list: List[main_models.GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList] = None,
    ):
        self.total_doc_size = total_doc_size
        self.user_config_data_source_list = user_config_data_source_list

    def validate(self):
        if self.user_config_data_source_list:
            for v1 in self.user_config_data_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_doc_size is not None:
            result['TotalDocSize'] = self.total_doc_size

        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k1 in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDocSize') is not None:
            self.total_doc_size = m.get('TotalDocSize')

        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k1 in m.get('UserConfigDataSourceList'):
                temp_model = main_models.GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k1))

        return self

class GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList(DaraModel):
    def __init__(
        self,
        code: str = None,
        enable: bool = None,
        name: str = None,
        number: int = None,
        type: str = None,
    ):
        self.code = code
        self.enable = enable
        self.name = name
        self.number = number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

