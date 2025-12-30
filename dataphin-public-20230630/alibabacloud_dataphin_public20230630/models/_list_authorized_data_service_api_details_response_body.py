# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedDataServiceApiDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAuthorizedDataServiceApiDetailsResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizedDataServiceApiDetailsResponseBodyResultData(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        app_id: int = None,
        auth_type: str = None,
        authorized_dev_return_parameters: List[main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedDevReturnParameters] = None,
        authorized_prod_return_parameters: List[main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedProdReturnParameters] = None,
        description: str = None,
        dev_auth_period: str = None,
        prod_auth_period: str = None,
        project_id: int = None,
    ):
        # API_ID
        self.api_id = api_id
        self.api_name = api_name
        self.app_id = app_id
        self.auth_type = auth_type
        self.authorized_dev_return_parameters = authorized_dev_return_parameters
        self.authorized_prod_return_parameters = authorized_prod_return_parameters
        self.description = description
        self.dev_auth_period = dev_auth_period
        self.prod_auth_period = prod_auth_period
        self.project_id = project_id

    def validate(self):
        if self.authorized_dev_return_parameters:
            for v1 in self.authorized_dev_return_parameters:
                 if v1:
                    v1.validate()
        if self.authorized_prod_return_parameters:
            for v1 in self.authorized_prod_return_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        result['AuthorizedDevReturnParameters'] = []
        if self.authorized_dev_return_parameters is not None:
            for k1 in self.authorized_dev_return_parameters:
                result['AuthorizedDevReturnParameters'].append(k1.to_map() if k1 else None)

        result['AuthorizedProdReturnParameters'] = []
        if self.authorized_prod_return_parameters is not None:
            for k1 in self.authorized_prod_return_parameters:
                result['AuthorizedProdReturnParameters'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_auth_period is not None:
            result['DevAuthPeriod'] = self.dev_auth_period

        if self.prod_auth_period is not None:
            result['ProdAuthPeriod'] = self.prod_auth_period

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        self.authorized_dev_return_parameters = []
        if m.get('AuthorizedDevReturnParameters') is not None:
            for k1 in m.get('AuthorizedDevReturnParameters'):
                temp_model = main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedDevReturnParameters()
                self.authorized_dev_return_parameters.append(temp_model.from_map(k1))

        self.authorized_prod_return_parameters = []
        if m.get('AuthorizedProdReturnParameters') is not None:
            for k1 in m.get('AuthorizedProdReturnParameters'):
                temp_model = main_models.ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedProdReturnParameters()
                self.authorized_prod_return_parameters.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevAuthPeriod') is not None:
            self.dev_auth_period = m.get('DevAuthPeriod')

        if m.get('ProdAuthPeriod') is not None:
            self.prod_auth_period = m.get('ProdAuthPeriod')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedProdReturnParameters(DaraModel):
    def __init__(
        self,
        example_value: str = None,
        is_authorized: int = None,
        parameter_data_type: int = None,
        parameter_description: str = None,
        parameter_name: str = None,
    ):
        self.example_value = example_value
        self.is_authorized = is_authorized
        self.parameter_data_type = parameter_data_type
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value

        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized

        if self.parameter_data_type is not None:
            result['ParameterDataType'] = self.parameter_data_type

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')

        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')

        if m.get('ParameterDataType') is not None:
            self.parameter_data_type = m.get('ParameterDataType')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class ListAuthorizedDataServiceApiDetailsResponseBodyResultDataAuthorizedDevReturnParameters(DaraModel):
    def __init__(
        self,
        example_value: str = None,
        is_authorized: int = None,
        parameter_data_type: int = None,
        parameter_description: str = None,
        parameter_name: str = None,
    ):
        self.example_value = example_value
        self.is_authorized = is_authorized
        self.parameter_data_type = parameter_data_type
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value

        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized

        if self.parameter_data_type is not None:
            result['ParameterDataType'] = self.parameter_data_type

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')

        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')

        if m.get('ParameterDataType') is not None:
            self.parameter_data_type = m.get('ParameterDataType')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

