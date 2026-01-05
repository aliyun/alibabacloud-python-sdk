# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class CreateProvisionedProductPlanRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        operation_type: str = None,
        parameters: List[main_models.CreateProvisionedProductPlanRequestParameters] = None,
        plan_name: str = None,
        plan_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_name: str = None,
        stack_region_id: str = None,
        tags: List[main_models.CreateProvisionedProductPlanRequestTags] = None,
    ):
        # The description of the plan.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The type of the operation that you want the plan to perform. Valid values:
        # 
        # *   LaunchProduct: launches the product. This is the default value.
        # *   UpdateProvisionedProduct: updates the information about the product instance.
        # *   TerminateProvisionedProduct: terminates the product instance.
        self.operation_type = operation_type
        # An array that consists of the parameters in the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > If you specify Parameters, you must specify ParameterKey and ParameterValue.
        self.parameters = parameters
        # The plan name.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.plan_name = plan_name
        # The plan type.
        # 
        # Set the value to Ros, which specifies Resource Orchestration Service (ROS).
        # 
        # This parameter is required.
        self.plan_type = plan_type
        # The product portfolio ID.
        # 
        # > If PortfolioId is not required, you do not need to specify PortfolioId. If PortfolioId is required, you must specify PortfolioId. For more information about how to obtain the value of PortfolioId, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id
        # The product ID.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The product version ID.
        # 
        # This parameter is required.
        self.product_version_id = product_version_id
        # The product instance name.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.provisioned_product_name = provisioned_product_name
        # The ID of the region to which the ROS stack belongs.
        # 
        # For more information about how to obtain the regions that are supported by ROS, see [DescribeRegions](https://help.aliyun.com/document_detail/131035.html).
        # 
        # This parameter is required.
        self.stack_region_id = stack_region_id
        # An array that consists of custom tags.
        # 
        # Maximum value of N: 20.
        # 
        # > 
        # *   If you specify Tags, you must specify Tags.N.Key and Tags.N.Value.
        # *   The tag of a stack is propagated to each resource that supports the tag feature in the stack.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateProvisionedProductPlanRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

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
                temp_model = main_models.CreateProvisionedProductPlanRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateProvisionedProductPlanRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom tag.
        # 
        # The key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the custom tag.
        # 
        # The value can be up to 128 characters in length, and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
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

class CreateProvisionedProductPlanRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key
        # The value of the parameter in the template.
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

