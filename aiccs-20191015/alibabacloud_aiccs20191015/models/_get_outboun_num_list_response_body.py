# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetOutbounNumListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetOutbounNumListResponseBodyData = None,
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
            temp_model = main_models.GetOutbounNumListResponseBodyData()
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

class GetOutbounNumListResponseBodyData(DaraModel):
    def __init__(
        self,
        num: List[main_models.GetOutbounNumListResponseBodyDataNum] = None,
        num_group: List[main_models.GetOutbounNumListResponseBodyDataNumGroup] = None,
    ):
        self.num = num
        self.num_group = num_group

    def validate(self):
        if self.num:
            for v1 in self.num:
                 if v1:
                    v1.validate()
        if self.num_group:
            for v1 in self.num_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Num'] = []
        if self.num is not None:
            for k1 in self.num:
                result['Num'].append(k1.to_map() if k1 else None)

        result['NumGroup'] = []
        if self.num_group is not None:
            for k1 in self.num_group:
                result['NumGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.num = []
        if m.get('Num') is not None:
            for k1 in m.get('Num'):
                temp_model = main_models.GetOutbounNumListResponseBodyDataNum()
                self.num.append(temp_model.from_map(k1))

        self.num_group = []
        if m.get('NumGroup') is not None:
            for k1 in m.get('NumGroup'):
                temp_model = main_models.GetOutbounNumListResponseBodyDataNumGroup()
                self.num_group.append(temp_model.from_map(k1))

        return self

class GetOutbounNumListResponseBodyDataNumGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        type: int = None,
        value: str = None,
    ):
        self.description = description
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetOutbounNumListResponseBodyDataNum(DaraModel):
    def __init__(
        self,
        description: str = None,
        type: int = None,
        value: str = None,
    ):
        self.description = description
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

