# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetProductVersionResponseBody(DaraModel):
    def __init__(
        self,
        product_version_detail: main_models.GetProductVersionResponseBodyProductVersionDetail = None,
        request_id: str = None,
    ):
        # The details of the product version.
        self.product_version_detail = product_version_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.product_version_detail:
            self.product_version_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_version_detail is not None:
            result['ProductVersionDetail'] = self.product_version_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionDetail') is not None:
            temp_model = main_models.GetProductVersionResponseBodyProductVersionDetail()
            self.product_version_detail = temp_model.from_map(m.get('ProductVersionDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProductVersionResponseBodyProductVersionDetail(DaraModel):
    def __init__(
        self,
        active: bool = None,
        create_time: str = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # Indicates whether the product version is visible to end users. Valid values:
        # - true: The product version is visible to end users. This is the default value.
        # - false: The product version is invisible to end users.
        self.active = active
        # The time when the product version was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product version.
        self.description = description
        # The recommendation information. Valid values:
        # 
        # - Default: No recommendation information is provided. This is the default value.
        # - Recommended: the recommendation version.
        # - Latest: the latest version.
        # - Deprecated: the version that is about to be deprecated.
        self.guidance = guidance
        # The ID of the product to which the product version belongs.
        self.product_id = product_id
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The name of the product version.
        self.product_version_name = product_version_name
        # The type of the product template. Valid values:
        # 
        # *   RosTerraformTemplate: The Terraform template that is supported by Resource Orchestration Service (ROS).
        # *   RosStandardTemplate: The standard ROS template.
        self.template_type = template_type
        # The URL of the template.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.guidance is not None:
            result['Guidance'] = self.guidance

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        return self

