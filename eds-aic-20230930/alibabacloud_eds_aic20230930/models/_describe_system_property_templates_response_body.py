# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemPropertyTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        system_property_template_model: List[main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModel] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.system_property_template_model = system_property_template_model
        self.total_count = total_count

    def validate(self):
        if self.system_property_template_model:
            for v1 in self.system_property_template_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SystemPropertyTemplateModel'] = []
        if self.system_property_template_model is not None:
            for k1 in self.system_property_template_model:
                result['SystemPropertyTemplateModel'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.system_property_template_model = []
        if m.get('SystemPropertyTemplateModel') is not None:
            for k1 in m.get('SystemPropertyTemplateModel'):
                temp_model = main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModel()
                self.system_property_template_model.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModel(DaraModel):
    def __init__(
        self,
        enable_auto: bool = None,
        file_path: str = None,
        status: str = None,
        system_property_info: main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfo = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.enable_auto = enable_auto
        self.file_path = file_path
        self.status = status
        self.system_property_info = system_property_info
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.system_property_info:
            self.system_property_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto is not None:
            result['EnableAuto'] = self.enable_auto

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.status is not None:
            result['Status'] = self.status

        if self.system_property_info is not None:
            result['SystemPropertyInfo'] = self.system_property_info.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAuto') is not None:
            self.enable_auto = m.get('EnableAuto')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemPropertyInfo') is not None:
            temp_model = main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfo()
            self.system_property_info = temp_model.from_map(m.get('SystemPropertyInfo'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfo(DaraModel):
    def __init__(
        self,
        custom_property_infos: List[main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfoCustomPropertyInfos] = None,
        ro_product_device: str = None,
    ):
        self.custom_property_infos = custom_property_infos
        self.ro_product_device = ro_product_device

    def validate(self):
        if self.custom_property_infos:
            for v1 in self.custom_property_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPropertyInfos'] = []
        if self.custom_property_infos is not None:
            for k1 in self.custom_property_infos:
                result['CustomPropertyInfos'].append(k1.to_map() if k1 else None)

        if self.ro_product_device is not None:
            result['RoProductDevice'] = self.ro_product_device

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_property_infos = []
        if m.get('CustomPropertyInfos') is not None:
            for k1 in m.get('CustomPropertyInfos'):
                temp_model = main_models.DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfoCustomPropertyInfos()
                self.custom_property_infos.append(temp_model.from_map(k1))

        if m.get('RoProductDevice') is not None:
            self.ro_product_device = m.get('RoProductDevice')

        return self

class DescribeSystemPropertyTemplatesResponseBodySystemPropertyTemplateModelSystemPropertyInfoCustomPropertyInfos(DaraModel):
    def __init__(
        self,
        property_name: str = None,
        property_value: str = None,
    ):
        self.property_name = property_name
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        return self

