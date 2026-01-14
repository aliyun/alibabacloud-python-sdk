# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddAuthResourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_id: int = None,
        auth_resource_header_list: List[main_models.AddAuthResourceRequestAuthResourceHeaderList] = None,
        domain_id: int = None,
        gateway_unique_id: str = None,
        ignore_case: bool = None,
        match_type: str = None,
        path: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the authorization record.
        self.auth_id = auth_id
        # The authentication resource headers.
        self.auth_resource_header_list = auth_resource_header_list
        # The domain ID.
        self.domain_id = domain_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether the matching is not case-sensitive. Default value: true.
        self.ignore_case = ignore_case
        # The matching type. Valid values:
        # 
        # *   EQUAL
        # *   PRE
        # *   ERGULAR
        self.match_type = match_type
        # The path.
        self.path = path

    def validate(self):
        if self.auth_resource_header_list:
            for v1 in self.auth_resource_header_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        result['AuthResourceHeaderList'] = []
        if self.auth_resource_header_list is not None:
            for k1 in self.auth_resource_header_list:
                result['AuthResourceHeaderList'].append(k1.to_map() if k1 else None)

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        self.auth_resource_header_list = []
        if m.get('AuthResourceHeaderList') is not None:
            for k1 in m.get('AuthResourceHeaderList'):
                temp_model = main_models.AddAuthResourceRequestAuthResourceHeaderList()
                self.auth_resource_header_list.append(temp_model.from_map(k1))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class AddAuthResourceRequestAuthResourceHeaderList(DaraModel):
    def __init__(
        self,
        header_key: str = None,
        header_method: str = None,
        header_value: str = None,
    ):
        # The parameter of the HTTP header.
        self.header_key = header_key
        # The header matching mode.
        # 
        # Valid values:
        # 
        # *   SUFFIX
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   EXIST
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PREFIX
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   EQUAL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   EXCLUDE
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NOT_EQUAL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NOT_EXIST
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REGREX
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   INCLUDE
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.header_method = header_method
        # The parameter value of the HTTP header.
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key

        if self.header_method is not None:
            result['HeaderMethod'] = self.header_method

        if self.header_value is not None:
            result['HeaderValue'] = self.header_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')

        if m.get('HeaderMethod') is not None:
            self.header_method = m.get('HeaderMethod')

        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')

        return self

