# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetProductAsAdminResponseBody(DaraModel):
    def __init__(
        self,
        product_detail: main_models.GetProductAsAdminResponseBodyProductDetail = None,
        request_id: str = None,
        tag_options: List[main_models.GetProductAsAdminResponseBodyTagOptions] = None,
    ):
        # The information about the product.
        self.product_detail = product_detail
        # The ID of the request.
        self.request_id = request_id
        # The tag options associated with the product.
        self.tag_options = tag_options

    def validate(self):
        if self.product_detail:
            self.product_detail.validate()
        if self.tag_options:
            for v1 in self.tag_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagOptions'] = []
        if self.tag_options is not None:
            for k1 in self.tag_options:
                result['TagOptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductDetail') is not None:
            temp_model = main_models.GetProductAsAdminResponseBodyProductDetail()
            self.product_detail = temp_model.from_map(m.get('ProductDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_options = []
        if m.get('TagOptions') is not None:
            for k1 in m.get('TagOptions'):
                temp_model = main_models.GetProductAsAdminResponseBodyTagOptions()
                self.tag_options.append(temp_model.from_map(k1))

        return self

class GetProductAsAdminResponseBodyTagOptions(DaraModel):
    def __init__(
        self,
        active: bool = None,
        key: str = None,
        owner: str = None,
        tag_option_id: str = None,
        value: str = None,
    ):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The key of the tag option.
        self.key = key
        # The ID of the owner of the tag option.
        self.owner = owner
        # The ID of the tag option.
        self.tag_option_id = tag_option_id
        # The value of the tag option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.key is not None:
            result['Key'] = self.key

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetProductAsAdminResponseBodyProductDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
        template_type: str = None,
    ):
        # The creation time.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn
        # The ID of the product.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type
        # The provider of the product.
        self.provider_name = provider_name
        # The type of the product template. Valid values:
        # 
        # *   RosTerraformTemplate: the Terraform template that is supported by Resource Orchestration Service (ROS).
        # *   RosStandardTemplate: the standard ROS template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

