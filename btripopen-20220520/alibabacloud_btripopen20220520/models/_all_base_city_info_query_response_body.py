# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class AllBaseCityInfoQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.AllBaseCityInfoQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.AllBaseCityInfoQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class AllBaseCityInfoQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        all_city_base_info_list: List[main_models.AllBaseCityInfoQueryResponseBodyModuleAllCityBaseInfoList] = None,
    ):
        self.all_city_base_info_list = all_city_base_info_list

    def validate(self):
        if self.all_city_base_info_list:
            for v1 in self.all_city_base_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['all_city_base_info_list'] = []
        if self.all_city_base_info_list is not None:
            for k1 in self.all_city_base_info_list:
                result['all_city_base_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_city_base_info_list = []
        if m.get('all_city_base_info_list') is not None:
            for k1 in m.get('all_city_base_info_list'):
                temp_model = main_models.AllBaseCityInfoQueryResponseBodyModuleAllCityBaseInfoList()
                self.all_city_base_info_list.append(temp_model.from_map(k1))

        return self

class AllBaseCityInfoQueryResponseBodyModuleAllCityBaseInfoList(DaraModel):
    def __init__(
        self,
        adcode: str = None,
        city_code: str = None,
        city_level: str = None,
        city_name: str = None,
        cn_name_tree: str = None,
        id: int = None,
        other_name_list: List[str] = None,
    ):
        self.adcode = adcode
        self.city_code = city_code
        self.city_level = city_level
        self.city_name = city_name
        self.cn_name_tree = cn_name_tree
        self.id = id
        self.other_name_list = other_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adcode is not None:
            result['adcode'] = self.adcode

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_level is not None:
            result['city_level'] = self.city_level

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.cn_name_tree is not None:
            result['cn_name_tree'] = self.cn_name_tree

        if self.id is not None:
            result['id'] = self.id

        if self.other_name_list is not None:
            result['other_name_list'] = self.other_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_level') is not None:
            self.city_level = m.get('city_level')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('cn_name_tree') is not None:
            self.cn_name_tree = m.get('cn_name_tree')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('other_name_list') is not None:
            self.other_name_list = m.get('other_name_list')

        return self

