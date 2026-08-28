# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpDubboTranscoder(DaraModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        method_map_list: List[main_models.HttpDubboTranscoderMethodMapList] = None,
    ):
        # The Dubbo service group.
        self.dubbo_service_group = dubbo_service_group
        # The Dubbo service name.
        self.dubbo_service_name = dubbo_service_name
        # The Dubbo service version.
        self.dubbo_service_version = dubbo_service_version
        # The method mapping list.
        self.method_map_list = method_map_list

    def validate(self):
        if self.method_map_list:
            for v1 in self.method_map_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dubbo_service_group is not None:
            result['dubboServiceGroup'] = self.dubbo_service_group

        if self.dubbo_service_name is not None:
            result['dubboServiceName'] = self.dubbo_service_name

        if self.dubbo_service_version is not None:
            result['dubboServiceVersion'] = self.dubbo_service_version

        result['methodMapList'] = []
        if self.method_map_list is not None:
            for k1 in self.method_map_list:
                result['methodMapList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboServiceGroup') is not None:
            self.dubbo_service_group = m.get('dubboServiceGroup')

        if m.get('dubboServiceName') is not None:
            self.dubbo_service_name = m.get('dubboServiceName')

        if m.get('dubboServiceVersion') is not None:
            self.dubbo_service_version = m.get('dubboServiceVersion')

        self.method_map_list = []
        if m.get('methodMapList') is not None:
            for k1 in m.get('methodMapList'):
                temp_model = main_models.HttpDubboTranscoderMethodMapList()
                self.method_map_list.append(temp_model.from_map(k1))

        return self

class HttpDubboTranscoderMethodMapList(DaraModel):
    def __init__(
        self,
        dubbo_method_name: str = None,
        http_method: str = None,
        method_path: str = None,
        param_maps_list: List[main_models.HttpDubboTranscoderMethodMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        # The Dubbo method name.
        self.dubbo_method_name = dubbo_method_name
        # The HTTP method. Valid values: ALL_GET. ALL_POST. ALL_PUT. ALL_DELETE. ALL_PATCH.
        self.http_method = http_method
        # The method matching path.
        self.method_path = method_path
        # The parameter mapping list.
        self.param_maps_list = param_maps_list
        # The header pass-through type. Valid values:
        # - PASS_ALL: Pass through all headers.
        # - PASS_NOT: Do not pass through headers.
        # - PASS_ASSIGN: Pass through specified headers.
        self.pass_through_all_headers = pass_through_all_headers
        # The list of specified pass-through headers.
        self.pass_through_list = pass_through_list

    def validate(self):
        if self.param_maps_list:
            for v1 in self.param_maps_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dubbo_method_name is not None:
            result['dubboMethodName'] = self.dubbo_method_name

        if self.http_method is not None:
            result['httpMethod'] = self.http_method

        if self.method_path is not None:
            result['methodPath'] = self.method_path

        result['paramMapsList'] = []
        if self.param_maps_list is not None:
            for k1 in self.param_maps_list:
                result['paramMapsList'].append(k1.to_map() if k1 else None)

        if self.pass_through_all_headers is not None:
            result['passThroughAllHeaders'] = self.pass_through_all_headers

        if self.pass_through_list is not None:
            result['passThroughList'] = self.pass_through_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboMethodName') is not None:
            self.dubbo_method_name = m.get('dubboMethodName')

        if m.get('httpMethod') is not None:
            self.http_method = m.get('httpMethod')

        if m.get('methodPath') is not None:
            self.method_path = m.get('methodPath')

        self.param_maps_list = []
        if m.get('paramMapsList') is not None:
            for k1 in m.get('paramMapsList'):
                temp_model = main_models.HttpDubboTranscoderMethodMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k1))

        if m.get('passThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('passThroughAllHeaders')

        if m.get('passThroughList') is not None:
            self.pass_through_list = m.get('passThroughList')

        return self

class HttpDubboTranscoderMethodMapListParamMapsList(DaraModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        # The key used to extract the input parameter.
        self.extract_key = extract_key
        # The input parameter location. Valid values:
        # - ALL_QUERY_PARAMETER: Request parameter.
        # - ALL_HEADER: Request header.
        # - ALL_PATH: URI of the request.
        # - ALL_BODY: Request body.
        self.extract_key_spec = extract_key_spec
        # The backend parameter type.
        self.mapping_type = mapping_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extract_key is not None:
            result['extractKey'] = self.extract_key

        if self.extract_key_spec is not None:
            result['extractKeySpec'] = self.extract_key_spec

        if self.mapping_type is not None:
            result['mappingType'] = self.mapping_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extractKey') is not None:
            self.extract_key = m.get('extractKey')

        if m.get('extractKeySpec') is not None:
            self.extract_key_spec = m.get('extractKeySpec')

        if m.get('mappingType') is not None:
            self.mapping_type = m.get('mappingType')

        return self

