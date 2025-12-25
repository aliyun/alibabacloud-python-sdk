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
        mothed_map_list: List[main_models.HttpDubboTranscoderMothedMapList] = None,
    ):
        self.dubbo_service_group = dubbo_service_group
        self.dubbo_service_name = dubbo_service_name
        self.dubbo_service_version = dubbo_service_version
        self.mothed_map_list = mothed_map_list

    def validate(self):
        if self.mothed_map_list:
            for v1 in self.mothed_map_list:
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

        result['mothedMapList'] = []
        if self.mothed_map_list is not None:
            for k1 in self.mothed_map_list:
                result['mothedMapList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboServiceGroup') is not None:
            self.dubbo_service_group = m.get('dubboServiceGroup')

        if m.get('dubboServiceName') is not None:
            self.dubbo_service_name = m.get('dubboServiceName')

        if m.get('dubboServiceVersion') is not None:
            self.dubbo_service_version = m.get('dubboServiceVersion')

        self.mothed_map_list = []
        if m.get('mothedMapList') is not None:
            for k1 in m.get('mothedMapList'):
                temp_model = main_models.HttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k1))

        return self

class HttpDubboTranscoderMothedMapList(DaraModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[main_models.HttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        self.dubbo_mothed_name = dubbo_mothed_name
        self.http_mothed = http_mothed
        self.mothedpath = mothedpath
        self.param_maps_list = param_maps_list
        self.pass_through_all_headers = pass_through_all_headers
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
        if self.dubbo_mothed_name is not None:
            result['dubboMothedName'] = self.dubbo_mothed_name

        if self.http_mothed is not None:
            result['httpMothed'] = self.http_mothed

        if self.mothedpath is not None:
            result['mothedpath'] = self.mothedpath

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
        if m.get('dubboMothedName') is not None:
            self.dubbo_mothed_name = m.get('dubboMothedName')

        if m.get('httpMothed') is not None:
            self.http_mothed = m.get('httpMothed')

        if m.get('mothedpath') is not None:
            self.mothedpath = m.get('mothedpath')

        self.param_maps_list = []
        if m.get('paramMapsList') is not None:
            for k1 in m.get('paramMapsList'):
                temp_model = main_models.HttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k1))

        if m.get('passThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('passThroughAllHeaders')

        if m.get('passThroughList') is not None:
            self.pass_through_list = m.get('passThroughList')

        return self

class HttpDubboTranscoderMothedMapListParamMapsList(DaraModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        self.extract_key = extract_key
        self.extract_key_spec = extract_key_spec
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

