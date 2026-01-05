# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProductVersionRequest(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # Specifies whether the product version is active. Valid values:
        # 
        # *   true: The product version is active. This is the default value.
        # *   false: The product version is inactive.
        self.active = active
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommendation version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance
        # The ID of the product to which the product version belongs.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.product_version_name = product_version_name
        # The type of the product template. Valid values:
        # 
        # *   RosTerraformTemplate: the Terraform template that is supported by Resource Orchestration Service (ROS).
        # *   RosStandardTemplate: the standard ROS template.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The URL of the template.
        # 
        # For more information about how to obtain the URL of a template, see [CreateTemplate](~~CreateTemplate~~).
        # 
        # This parameter is required.
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

        if self.product_id is not None:
            result['ProductId'] = self.product_id

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

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        return self

