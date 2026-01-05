# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class CreateProductRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        product_name: str = None,
        product_type: str = None,
        product_version_parameters: main_models.CreateProductRequestProductVersionParameters = None,
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
        self.product_version_parameters = product_version_parameters
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
        if self.product_version_parameters:
            self.product_version_parameters.validate()

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

        if self.product_version_parameters is not None:
            result['ProductVersionParameters'] = self.product_version_parameters.to_map()

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
            temp_model = main_models.CreateProductRequestProductVersionParameters()
            self.product_version_parameters = temp_model.from_map(m.get('ProductVersionParameters'))

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self



class CreateProductRequestProductVersionParameters(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # Specifies whether to enable the product version. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The recommended product version. Valid values:
        # 
        # *   Default (default): No product version is recommended.
        # *   Recommended: the stable version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be deprecated.
        self.guidance = guidance
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_version_name = product_version_name
        # The type of the template.
        # 
        # Set the value to RosTerraformTemplate, which indicates the Terraform template that is supported by Resource Orchestration Service (ROS).
        self.template_type = template_type
        # The URL of the template.
        # 
        # To obtain the URL of a template, you can call the [CreateTemplate](~~CreateTemplate~~) operation.
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.description is not None:
            result['Description'] = self.description

        if self.guidance is not None:
            result['Guidance'] = self.guidance

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        return self

