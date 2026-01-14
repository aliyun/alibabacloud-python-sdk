# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCommodityResponseBody(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
        components: List[main_models.DescribeCommodityResponseBodyComponents] = None,
        request_id: str = None,
    ):
        # The commodity code.
        # 
        # Examples for the China site (aliyun.com):
        # 
        # *   **ga_gapluspre_public_cn**: GA instance.
        # *   **ga_plusbwppre_public_cn**: basic bandwidth plan.
        # 
        # Examples for the international site (alibabacloud.com):
        # 
        # *   **ga_pluspre_public_intl**: GA instance.
        # *   **ga_bwppreintl_public_intl**: basic bandwidth plan.
        self.commodity_code = commodity_code
        # The name of the commodity.
        self.commodity_name = commodity_name
        # The information about the commodity modules.
        # 
        # The returned information varies based on the commodity.
        self.components = components
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeCommodityResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCommodityResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        component_name: str = None,
        properties: List[main_models.DescribeCommodityResponseBodyComponentsProperties] = None,
    ):
        # The code of the commodity module.
        # 
        # The returned information varies based on the commodity module.
        self.component_code = component_code
        # The name of the commodity module.
        # 
        # The returned information varies based on the commodity module.
        self.component_name = component_name
        # The attributes of the commodity module.
        # 
        # The returned information varies based on the commodity module.
        self.properties = properties

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.DescribeCommodityResponseBodyComponentsProperties()
                self.properties.append(temp_model.from_map(k1))

        return self

class DescribeCommodityResponseBodyComponentsProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        property_value_list: List[main_models.DescribeCommodityResponseBodyComponentsPropertiesPropertyValueList] = None,
    ):
        # The code of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.code = code
        # The name of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.name = name
        # The list of attribute values of the commodity module.
        # 
        # The returned information varies based on the commodity module.
        self.property_value_list = property_value_list

    def validate(self):
        if self.property_value_list:
            for v1 in self.property_value_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        result['PropertyValueList'] = []
        if self.property_value_list is not None:
            for k1 in self.property_value_list:
                result['PropertyValueList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.property_value_list = []
        if m.get('PropertyValueList') is not None:
            for k1 in m.get('PropertyValueList'):
                temp_model = main_models.DescribeCommodityResponseBodyComponentsPropertiesPropertyValueList()
                self.property_value_list.append(temp_model.from_map(k1))

        return self

class DescribeCommodityResponseBodyComponentsPropertiesPropertyValueList(DaraModel):
    def __init__(
        self,
        order_index: int = None,
        text: str = None,
        tips: str = None,
        value: str = None,
    ):
        # The sequence number of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.order_index = order_index
        # The content of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.text = text
        # The message of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.tips = tips
        # The value of the attribute.
        # 
        # The returned information varies based on the commodity module.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.text is not None:
            result['Text'] = self.text

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

