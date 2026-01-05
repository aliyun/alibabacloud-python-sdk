# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProductsAsAdminResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_details: List[main_models.ListProductsAsAdminResponseBodyProductDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The products.
        self.product_details = product_details
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.product_details:
            for v1 in self.product_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProductDetails'] = []
        if self.product_details is not None:
            for k1 in self.product_details:
                result['ProductDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.product_details = []
        if m.get('ProductDetails') is not None:
            for k1 in m.get('ProductDetails'):
                temp_model = main_models.ListProductsAsAdminResponseBodyProductDetails()
                self.product_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductsAsAdminResponseBodyProductDetails(DaraModel):
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
        # The time when the product was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn
        # The product ID.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The type of the product.
        # 
        # The value is set to Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type
        # The provider of the product.
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

