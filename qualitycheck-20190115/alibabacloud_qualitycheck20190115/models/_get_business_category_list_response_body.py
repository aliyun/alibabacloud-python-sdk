# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetBusinessCategoryListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBusinessCategoryListResponseBodyData = None,
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
            temp_model = main_models.GetBusinessCategoryListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBusinessCategoryListResponseBodyData(DaraModel):
    def __init__(
        self,
        business_category_basic_info: List[main_models.GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo] = None,
    ):
        self.business_category_basic_info = business_category_basic_info

    def validate(self):
        if self.business_category_basic_info:
            for v1 in self.business_category_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k1 in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k1 in m.get('BusinessCategoryBasicInfo'):
                temp_model = main_models.GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k1))

        return self

class GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo(DaraModel):
    def __init__(
        self,
        bid: int = None,
        business_name: str = None,
        service_type: int = None,
    ):
        self.bid = bid
        self.business_name = business_name
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

