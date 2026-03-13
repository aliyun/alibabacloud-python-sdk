# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TravelStandardQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TravelStandardQueryResponseBodyModule = None,
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
            temp_model = main_models.TravelStandardQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TravelStandardQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        activated_service_type_list: List[str] = None,
        reserve_rule: main_models.TravelStandardQueryResponseBodyModuleReserveRule = None,
    ):
        self.activated_service_type_list = activated_service_type_list
        self.reserve_rule = reserve_rule

    def validate(self):
        if self.reserve_rule:
            self.reserve_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated_service_type_list is not None:
            result['activated_service_type_list'] = self.activated_service_type_list

        if self.reserve_rule is not None:
            result['reserve_rule'] = self.reserve_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activated_service_type_list') is not None:
            self.activated_service_type_list = m.get('activated_service_type_list')

        if m.get('reserve_rule') is not None:
            temp_model = main_models.TravelStandardQueryResponseBodyModuleReserveRule()
            self.reserve_rule = temp_model.from_map(m.get('reserve_rule'))

        return self

class TravelStandardQueryResponseBodyModuleReserveRule(DaraModel):
    def __init__(
        self,
        main_reserve_rule: main_models.TravelStandardQueryResponseBodyModuleReserveRuleMainReserveRule = None,
        module_config_list: List[main_models.TravelStandardQueryResponseBodyModuleReserveRuleModuleConfigList] = None,
    ):
        self.main_reserve_rule = main_reserve_rule
        self.module_config_list = module_config_list

    def validate(self):
        if self.main_reserve_rule:
            self.main_reserve_rule.validate()
        if self.module_config_list:
            for v1 in self.module_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_reserve_rule is not None:
            result['main_reserve_rule'] = self.main_reserve_rule.to_map()

        result['module_config_list'] = []
        if self.module_config_list is not None:
            for k1 in self.module_config_list:
                result['module_config_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('main_reserve_rule') is not None:
            temp_model = main_models.TravelStandardQueryResponseBodyModuleReserveRuleMainReserveRule()
            self.main_reserve_rule = temp_model.from_map(m.get('main_reserve_rule'))

        self.module_config_list = []
        if m.get('module_config_list') is not None:
            for k1 in m.get('module_config_list'):
                temp_model = main_models.TravelStandardQueryResponseBodyModuleReserveRuleModuleConfigList()
                self.module_config_list.append(temp_model.from_map(k1))

        return self

class TravelStandardQueryResponseBodyModuleReserveRuleModuleConfigList(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class TravelStandardQueryResponseBodyModuleReserveRuleMainReserveRule(DaraModel):
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

