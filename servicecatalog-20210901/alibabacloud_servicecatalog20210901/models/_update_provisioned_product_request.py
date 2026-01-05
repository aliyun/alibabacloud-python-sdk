# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class UpdateProvisionedProductRequest(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.UpdateProvisionedProductRequestParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_id: str = None,
        tags: List[main_models.UpdateProvisionedProductRequestTags] = None,
    ):
        # The input parameters of the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > - This parameter is optional. If you specify the Parameters parameter, you must specify the ParameterKey and ParameterValue parameters.
        # > - If the values of the ProductVersionId and Parameters parameters are not changed, you are not allowed to update the information about the product instance.
        self.parameters = parameters
        # The ID of the product portfolio.
        # 
        # > The PortfolioId parameter is not required if the default launch option exists. The PortfolioId parameter is required if the default launch option does not exist. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id
        # The ID of the product.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The ID of the product version.
        # 
        # > If the values of the ProductVersionId and Parameters parameters are not changed, the information about the product instance cannot be updated.
        # 
        # This parameter is required.
        self.product_version_id = product_version_id
        # The ID of the product instance.
        # 
        # This parameter is required.
        self.provisioned_product_id = provisioned_product_id
        # The input custom tags.
        # 
        # Maximum value of N: 20.
        # 
        # > - The Tags parameter is optional. If you need to specify the Tags parameter, you must specify the Tags.N.Key and Tags.N.Value parameters.
        # > - The tag is propagated to each stack resource that supports the tag feature.
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

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

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
                temp_model = main_models.UpdateProvisionedProductRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateProvisionedProductRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UpdateProvisionedProductRequestTags(DaraModel):
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

class UpdateProvisionedProductRequestParameters(DaraModel):
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

