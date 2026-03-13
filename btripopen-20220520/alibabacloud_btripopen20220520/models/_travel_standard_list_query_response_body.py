# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TravelStandardListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: main_models.TravelStandardListQueryResponseBodyModule = None,
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
            temp_model = main_models.TravelStandardListQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TravelStandardListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        items: List[main_models.TravelStandardListQueryResponseBodyModuleItems] = None,
        total_size: int = None,
    ):
        self.items = items
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.TravelStandardListQueryResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

class TravelStandardListQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        main_reserve_rule: main_models.TravelStandardListQueryResponseBodyModuleItemsMainReserveRule = None,
        reserve_rule_desc: List[main_models.TravelStandardListQueryResponseBodyModuleItemsReserveRuleDesc] = None,
        scope: int = None,
    ):
        self.main_reserve_rule = main_reserve_rule
        self.reserve_rule_desc = reserve_rule_desc
        self.scope = scope

    def validate(self):
        if self.main_reserve_rule:
            self.main_reserve_rule.validate()
        if self.reserve_rule_desc:
            for v1 in self.reserve_rule_desc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_reserve_rule is not None:
            result['main_reserve_rule'] = self.main_reserve_rule.to_map()

        result['reserve_rule_desc'] = []
        if self.reserve_rule_desc is not None:
            for k1 in self.reserve_rule_desc:
                result['reserve_rule_desc'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('main_reserve_rule') is not None:
            temp_model = main_models.TravelStandardListQueryResponseBodyModuleItemsMainReserveRule()
            self.main_reserve_rule = temp_model.from_map(m.get('main_reserve_rule'))

        self.reserve_rule_desc = []
        if m.get('reserve_rule_desc') is not None:
            for k1 in m.get('reserve_rule_desc'):
                temp_model = main_models.TravelStandardListQueryResponseBodyModuleItemsReserveRuleDesc()
                self.reserve_rule_desc.append(temp_model.from_map(k1))

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

class TravelStandardListQueryResponseBodyModuleItemsReserveRuleDesc(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.TravelStandardListQueryResponseBodyModuleItemsReserveRuleDescDataList] = None,
        title: str = None,
        type: str = None,
    ):
        self.data_list = data_list
        self.title = title
        self.type = type

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data_list'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['data_list'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('data_list') is not None:
            for k1 in m.get('data_list'):
                temp_model = main_models.TravelStandardListQueryResponseBodyModuleItemsReserveRuleDescDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TravelStandardListQueryResponseBodyModuleItemsReserveRuleDescDataList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class TravelStandardListQueryResponseBodyModuleItemsMainReserveRule(DaraModel):
    def __init__(
        self,
        open_service_type_list: List[str] = None,
        rule_code: int = None,
        rule_desc: str = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.open_service_type_list = open_service_type_list
        self.rule_code = rule_code
        self.rule_desc = rule_desc
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_service_type_list is not None:
            result['open_service_type_list'] = self.open_service_type_list

        if self.rule_code is not None:
            result['rule_code'] = self.rule_code

        if self.rule_desc is not None:
            result['rule_desc'] = self.rule_desc

        if self.rule_id is not None:
            result['rule_id'] = self.rule_id

        if self.rule_name is not None:
            result['rule_name'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('open_service_type_list') is not None:
            self.open_service_type_list = m.get('open_service_type_list')

        if m.get('rule_code') is not None:
            self.rule_code = m.get('rule_code')

        if m.get('rule_desc') is not None:
            self.rule_desc = m.get('rule_desc')

        if m.get('rule_id') is not None:
            self.rule_id = m.get('rule_id')

        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')

        return self

