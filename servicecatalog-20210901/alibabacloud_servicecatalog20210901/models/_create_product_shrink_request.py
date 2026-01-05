# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProductShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        product_name: str = None,
        product_type: str = None,
        product_version_parameters_shrink: str = None,
        provider_name: str = None,
        template_type: str = None,
    ):
        # The description of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The name of the product.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The type of the product.
        # 
        # Set the value to Ros, which specifies Resource Orchestration Service (ROS).
        # 
        # This parameter is required.
        self.product_type = product_type
        # The information about the product version.
        self.product_version_parameters_shrink = product_version_parameters_shrink
        # The provider of the product.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.provider_name = provider_name
        # The type of the product template. Valid values:
        # 
        # *   RosTerraformTemplate: the Terraform template that is supported by ROS.
        # *   RosStandardTemplate: the standard ROS template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.product_version_parameters_shrink is not None:
            result['ProductVersionParameters'] = self.product_version_parameters_shrink

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProductVersionParameters') is not None:
            self.product_version_parameters_shrink = m.get('ProductVersionParameters')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

