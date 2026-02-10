# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20200326 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListProductsResponseBodyData = None,
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
            temp_model = main_models.ListProductsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListProductsResponseBodyData(DaraModel):
    def __init__(
        self,
        consultation_more: List[main_models.ListProductsResponseBodyDataConsultationMore] = None,
        hot_consultation: List[main_models.ListProductsResponseBodyDataHotConsultation] = None,
        hot_tech: List[main_models.ListProductsResponseBodyDataHotTech] = None,
        tech_more: List[main_models.ListProductsResponseBodyDataTechMore] = None,
    ):
        self.consultation_more = consultation_more
        self.hot_consultation = hot_consultation
        self.hot_tech = hot_tech
        self.tech_more = tech_more

    def validate(self):
        if self.consultation_more:
            for v1 in self.consultation_more:
                 if v1:
                    v1.validate()
        if self.hot_consultation:
            for v1 in self.hot_consultation:
                 if v1:
                    v1.validate()
        if self.hot_tech:
            for v1 in self.hot_tech:
                 if v1:
                    v1.validate()
        if self.tech_more:
            for v1 in self.tech_more:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsultationMore'] = []
        if self.consultation_more is not None:
            for k1 in self.consultation_more:
                result['ConsultationMore'].append(k1.to_map() if k1 else None)

        result['HotConsultation'] = []
        if self.hot_consultation is not None:
            for k1 in self.hot_consultation:
                result['HotConsultation'].append(k1.to_map() if k1 else None)

        result['HotTech'] = []
        if self.hot_tech is not None:
            for k1 in self.hot_tech:
                result['HotTech'].append(k1.to_map() if k1 else None)

        result['TechMore'] = []
        if self.tech_more is not None:
            for k1 in self.tech_more:
                result['TechMore'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consultation_more = []
        if m.get('ConsultationMore') is not None:
            for k1 in m.get('ConsultationMore'):
                temp_model = main_models.ListProductsResponseBodyDataConsultationMore()
                self.consultation_more.append(temp_model.from_map(k1))

        self.hot_consultation = []
        if m.get('HotConsultation') is not None:
            for k1 in m.get('HotConsultation'):
                temp_model = main_models.ListProductsResponseBodyDataHotConsultation()
                self.hot_consultation.append(temp_model.from_map(k1))

        self.hot_tech = []
        if m.get('HotTech') is not None:
            for k1 in m.get('HotTech'):
                temp_model = main_models.ListProductsResponseBodyDataHotTech()
                self.hot_tech.append(temp_model.from_map(k1))

        self.tech_more = []
        if m.get('TechMore') is not None:
            for k1 in m.get('TechMore'):
                temp_model = main_models.ListProductsResponseBodyDataTechMore()
                self.tech_more.append(temp_model.from_map(k1))

        return self

class ListProductsResponseBodyDataTechMore(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        product_list: List[main_models.ListProductsResponseBodyDataTechMoreProductList] = None,
    ):
        self.group_name = group_name
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        result['ProductList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['ProductList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        self.product_list = []
        if m.get('ProductList') is not None:
            for k1 in m.get('ProductList'):
                temp_model = main_models.ListProductsResponseBodyDataTechMoreProductList()
                self.product_list.append(temp_model.from_map(k1))

        return self

class ListProductsResponseBodyDataTechMoreProductList(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class ListProductsResponseBodyDataHotTech(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class ListProductsResponseBodyDataHotConsultation(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class ListProductsResponseBodyDataConsultationMore(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_code: str = None,
    ):
        self.description = description
        self.name = name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

