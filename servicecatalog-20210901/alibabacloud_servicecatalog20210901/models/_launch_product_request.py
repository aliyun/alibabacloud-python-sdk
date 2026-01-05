# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class LaunchProductRequest(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.LaunchProductRequestParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_name: str = None,
        stack_region_id: str = None,
        tags: List[main_models.LaunchProductRequestTags] = None,
    ):
        # The input parameters of the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > This parameter is optional. If you specify the Parameters parameter, you must specify the ParameterKey and ParameterValue parameters.
        self.parameters = parameters
        # The ID of the product portfolio.
        # 
        # > If the PortfolioId parameter is not required, you do not need to specify the PortfolioId parameter. If the PortfolioId parameter is required, you must specify the PortfolioId parameter. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id
        # The ID of the product.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The ID of the product version.
        # 
        # This parameter is required.
        self.product_version_id = product_version_id
        # The name of the product instance.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.provisioned_product_name = provisioned_product_name
        # The ID of the region to which the Resource Orchestration Service (ROS) stack belongs.
        # 
        # For more information about how to obtain the regions that are supported by ROS, see [DescribeRegions](https://help.aliyun.com/document_detail/131035.html).
        # 
        # This parameter is required.
        self.stack_region_id = stack_region_id
        # The custom tags that are specified by the end user.
        # 
        # Maximum value of N: 20.
        # 
        # > 
        # 
        # *   The Tags parameter is optional. If you specify the Tags parameter, you must specify the Tags.N.Key and Tags.N.Value parameters.
        # 
        # *   The tag is propagated to each stack resource that supports the tag feature.
        self.tags = tags

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name

        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.LaunchProductRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')

        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.LaunchProductRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class LaunchProductRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the custom tag.
        # 
        # The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key
        # The tag value of the custom tag.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class LaunchProductRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key
        # The value of the input parameter for the template.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

