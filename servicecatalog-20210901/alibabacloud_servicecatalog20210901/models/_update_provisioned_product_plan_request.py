# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class UpdateProvisionedProductPlanRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        parameters: List[main_models.UpdateProvisionedProductPlanRequestParameters] = None,
        plan_id: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        tags: List[main_models.UpdateProvisionedProductPlanRequestTags] = None,
    ):
        # The description of the plan.
        self.description = description
        # An array that consists of the parameters in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify ParameterKey and ParameterValue.
        self.parameters = parameters
        # The ID of the plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the product portfolio.
        # 
        # > If the default launch option exists, you do not need to specify PortfolioId. If the default launch option does not exist, you must specify PortfolioId. For more information about how to obtain the value of PortfolioId, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id
        # The ID of the product.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The ID of the product version.
        # 
        # This parameter is required.
        self.product_version_id = product_version_id
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

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.UpdateProvisionedProductPlanRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateProvisionedProductPlanRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UpdateProvisionedProductPlanRequestTags(DaraModel):
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

class UpdateProvisionedProductPlanRequestParameters(DaraModel):
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

