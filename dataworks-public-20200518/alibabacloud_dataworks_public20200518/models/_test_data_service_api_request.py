# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class TestDataServiceApiRequest(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        body_content: str = None,
        body_params: List[main_models.TestDataServiceApiRequestBodyParams] = None,
        head_params: List[main_models.TestDataServiceApiRequestHeadParams] = None,
        path_params: List[main_models.TestDataServiceApiRequestPathParams] = None,
        query_param: List[main_models.TestDataServiceApiRequestQueryParam] = None,
    ):
        # The ID of the DataService Studio API on which the test is performed.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The data of the request body.
        self.body_content = body_content
        # The request parameters that are contained in the request body.
        self.body_params = body_params
        # The request parameters that are contained in the request header.
        self.head_params = head_params
        # The request parameters that are contained in the request path.
        self.path_params = path_params
        # The request parameters that are contained in the query.
        self.query_param = query_param

    def validate(self):
        if self.body_params:
            for v1 in self.body_params:
                 if v1:
                    v1.validate()
        if self.head_params:
            for v1 in self.head_params:
                 if v1:
                    v1.validate()
        if self.path_params:
            for v1 in self.path_params:
                 if v1:
                    v1.validate()
        if self.query_param:
            for v1 in self.query_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.body_content is not None:
            result['BodyContent'] = self.body_content

        result['BodyParams'] = []
        if self.body_params is not None:
            for k1 in self.body_params:
                result['BodyParams'].append(k1.to_map() if k1 else None)

        result['HeadParams'] = []
        if self.head_params is not None:
            for k1 in self.head_params:
                result['HeadParams'].append(k1.to_map() if k1 else None)

        result['PathParams'] = []
        if self.path_params is not None:
            for k1 in self.path_params:
                result['PathParams'].append(k1.to_map() if k1 else None)

        result['QueryParam'] = []
        if self.query_param is not None:
            for k1 in self.query_param:
                result['QueryParam'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('BodyContent') is not None:
            self.body_content = m.get('BodyContent')

        self.body_params = []
        if m.get('BodyParams') is not None:
            for k1 in m.get('BodyParams'):
                temp_model = main_models.TestDataServiceApiRequestBodyParams()
                self.body_params.append(temp_model.from_map(k1))

        self.head_params = []
        if m.get('HeadParams') is not None:
            for k1 in m.get('HeadParams'):
                temp_model = main_models.TestDataServiceApiRequestHeadParams()
                self.head_params.append(temp_model.from_map(k1))

        self.path_params = []
        if m.get('PathParams') is not None:
            for k1 in m.get('PathParams'):
                temp_model = main_models.TestDataServiceApiRequestPathParams()
                self.path_params.append(temp_model.from_map(k1))

        self.query_param = []
        if m.get('QueryParam') is not None:
            for k1 in m.get('QueryParam'):
                temp_model = main_models.TestDataServiceApiRequestQueryParam()
                self.query_param.append(temp_model.from_map(k1))

        return self

class TestDataServiceApiRequestQueryParam(DaraModel):
    def __init__(
        self,
        param_key: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_key = param_key
        # The value of the parameter.
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        return self

class TestDataServiceApiRequestPathParams(DaraModel):
    def __init__(
        self,
        param_key: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_key = param_key
        # The value of the parameter.
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        return self

class TestDataServiceApiRequestHeadParams(DaraModel):
    def __init__(
        self,
        param_key: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_key = param_key
        # The value of the parameter.
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        return self

class TestDataServiceApiRequestBodyParams(DaraModel):
    def __init__(
        self,
        param_key: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_key = param_key
        # The value of the parameter.
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        return self

