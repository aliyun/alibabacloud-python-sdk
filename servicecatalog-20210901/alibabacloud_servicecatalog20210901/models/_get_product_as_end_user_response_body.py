# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetProductAsEndUserResponseBody(DaraModel):
    def __init__(
        self,
        product_summary: main_models.GetProductAsEndUserResponseBodyProductSummary = None,
        request_id: str = None,
    ):
        # The information about the product.
        self.product_summary = product_summary
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.product_summary:
            self.product_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_summary is not None:
            result['ProductSummary'] = self.product_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductSummary') is not None:
            temp_model = main_models.GetProductAsEndUserResponseBodyProductSummary()
            self.product_summary = temp_model.from_map(m.get('ProductSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProductAsEndUserResponseBodyProductSummary(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        has_default_launch_option: bool = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
        template_type: str = None,
    ):
        # The time when the product was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product.
        self.description = description
        # Indicates whether the default launch option exists. Valid values:
        # 
        # *   true: The default launch option exists. In this case, the PortfolioId parameter is not required when the product is launched or when the information about the product instance is updated.
        # *   false: The default launch option does not exist. In this case, the PortfolioId parameter is required when the product is launched or when the information about the product instance is updated. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        # 
        # > If the product is added to only one product portfolio, the default launch option exists. If the product is added to multiple product portfolios, multiple launch options exist at the same time. However, no default launch options exist.
        self.has_default_launch_option = has_default_launch_option
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
        # *   RosTerraformTemplate: The Terraform template that is supported by Resource Orchestration Service (ROS).
        # *   RosStandardTemplate: The standard ROS template.
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

        if self.has_default_launch_option is not None:
            result['HasDefaultLaunchOption'] = self.has_default_launch_option

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

        if m.get('HasDefaultLaunchOption') is not None:
            self.has_default_launch_option = m.get('HasDefaultLaunchOption')

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

