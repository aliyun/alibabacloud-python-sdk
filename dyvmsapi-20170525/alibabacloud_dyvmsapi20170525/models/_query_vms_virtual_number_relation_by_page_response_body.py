# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryVmsVirtualNumberRelationByPageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.QueryVmsVirtualNumberRelationByPageResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.QueryVmsVirtualNumberRelationByPageResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryVmsVirtualNumberRelationByPageResponseBodyModel(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryVmsVirtualNumberRelationByPageResponseBodyModelData] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_no = page_no
        self.page_size = page_size
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryVmsVirtualNumberRelationByPageResponseBodyModelData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryVmsVirtualNumberRelationByPageResponseBodyModelData(DaraModel):
    def __init__(
        self,
        number_city: str = None,
        number_province: str = None,
        real_number: str = None,
        state: int = None,
        virtual_number: str = None,
    ):
        # 号码归属地--城市
        self.number_city = number_city
        # 号码归属地--省
        self.number_province = number_province
        # 真实号码
        self.real_number = real_number
        # 状态 1:有效；0:无效；-1:注销
        self.state = state
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number_city is not None:
            result['NumberCity'] = self.number_city

        if self.number_province is not None:
            result['NumberProvince'] = self.number_province

        if self.real_number is not None:
            result['RealNumber'] = self.real_number

        if self.state is not None:
            result['State'] = self.state

        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumberCity') is not None:
            self.number_city = m.get('NumberCity')

        if m.get('NumberProvince') is not None:
            self.number_province = m.get('NumberProvince')

        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')

        return self

