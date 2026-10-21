# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class ListSupportedPricingApisResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        supported_apis: List[main_models.ListSupportedPricingApisResponseBodySupportedApis] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The array of OpenAPI triplets that support price inquiry. The triplets are sorted in alphabetical order by popCode, popVersion, and apiName.
        self.supported_apis = supported_apis

    def validate(self):
        if self.supported_apis:
            for v1 in self.supported_apis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['supportedApis'] = []
        if self.supported_apis is not None:
            for k1 in self.supported_apis:
                result['supportedApis'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.supported_apis = []
        if m.get('supportedApis') is not None:
            for k1 in m.get('supportedApis'):
                temp_model = main_models.ListSupportedPricingApisResponseBodySupportedApis()
                self.supported_apis.append(temp_model.from_map(k1))

        return self

class ListSupportedPricingApisResponseBodySupportedApis(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        pop_code: str = None,
        pop_version: str = None,
    ):
        # The OpenAPI name in PascalCase, such as RunInstances.
        self.api_name = api_name
        # The POP product code, such as Ecs, Rds, or Alb. This value corresponds to the popCode field used in price inquiry requests.
        self.pop_code = pop_code
        # The OpenAPI version number, such as 2014-05-26.
        self.pop_version = pop_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.pop_code is not None:
            result['popCode'] = self.pop_code

        if self.pop_version is not None:
            result['popVersion'] = self.pop_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('popCode') is not None:
            self.pop_code = m.get('popCode')

        if m.get('popVersion') is not None:
            self.pop_version = m.get('popVersion')

        return self

