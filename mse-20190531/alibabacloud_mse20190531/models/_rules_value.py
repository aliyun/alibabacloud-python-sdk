# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class RulesValue(DaraModel):
    def __init__(
        self,
        status: int = None,
        rate: int = None,
        enable: bool = None,
        tag: str = None,
        name: str = None,
        id: int = None,
        instance_num: int = None,
        rules: main_models.RulesValueRules = None,
    ):
        self.status = status
        self.rate = rate
        self.enable = enable
        self.tag = tag
        self.name = name
        self.id = id
        self.instance_num = instance_num
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.name is not None:
            result['Name'] = self.name

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('Rules') is not None:
            temp_model = main_models.RulesValueRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class RulesValueRules(DaraModel):
    def __init__(
        self,
        springcloud: List[main_models.RulesValueRulesSpringcloud] = None,
        dubbo: List[main_models.RulesValueRulesDubbo] = None,
    ):
        self.springcloud = springcloud
        self.dubbo = dubbo

    def validate(self):
        if self.springcloud:
            for v1 in self.springcloud:
                 if v1:
                    v1.validate()
        if self.dubbo:
            for v1 in self.dubbo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['springcloud'] = []
        if self.springcloud is not None:
            for k1 in self.springcloud:
                result['springcloud'].append(k1.to_map() if k1 else None)

        result['dubbo'] = []
        if self.dubbo is not None:
            for k1 in self.dubbo:
                result['dubbo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.springcloud = []
        if m.get('springcloud') is not None:
            for k1 in m.get('springcloud'):
                temp_model = main_models.RulesValueRulesSpringcloud()
                self.springcloud.append(temp_model.from_map(k1))

        self.dubbo = []
        if m.get('dubbo') is not None:
            for k1 in m.get('dubbo'):
                temp_model = main_models.RulesValueRulesDubbo()
                self.dubbo.append(temp_model.from_map(k1))

        return self

class RulesValueRulesDubbo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        tags: List[str] = None,
        trigger_policy: str = None,
        service_name: str = None,
        group: str = None,
        version: str = None,
        method_name: str = None,
        param_types: List[str] = None,
        condition: str = None,
        argument_items: List[main_models.RulesValueRulesDubboArgumentItems] = None,
    ):
        self.app_id = app_id
        self.tags = tags
        self.trigger_policy = trigger_policy
        self.service_name = service_name
        self.group = group
        self.version = version
        self.method_name = method_name
        self.param_types = param_types
        self.condition = condition
        self.argument_items = argument_items

    def validate(self):
        if self.argument_items:
            for v1 in self.argument_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.tags is not None:
            result['tags'] = self.tags

        if self.trigger_policy is not None:
            result['triggerPolicy'] = self.trigger_policy

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        if self.method_name is not None:
            result['methodName'] = self.method_name

        if self.param_types is not None:
            result['paramTypes'] = self.param_types

        if self.condition is not None:
            result['condition'] = self.condition

        result['argumentItems'] = []
        if self.argument_items is not None:
            for k1 in self.argument_items:
                result['argumentItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('triggerPolicy') is not None:
            self.trigger_policy = m.get('triggerPolicy')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('paramTypes') is not None:
            self.param_types = m.get('paramTypes')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        self.argument_items = []
        if m.get('argumentItems') is not None:
            for k1 in m.get('argumentItems'):
                temp_model = main_models.RulesValueRulesDubboArgumentItems()
                self.argument_items.append(temp_model.from_map(k1))

        return self

class RulesValueRulesDubboArgumentItems(DaraModel):
    def __init__(
        self,
        operator: str = None,
        name_list: List[str] = None,
        datum: str = None,
        cond: str = None,
        divisor: int = None,
        remainder: int = None,
        rate: int = None,
        index: int = None,
        expr: str = None,
        value: Any = None,
    ):
        self.operator = operator
        self.name_list = name_list
        self.datum = datum
        self.cond = cond
        self.divisor = divisor
        self.remainder = remainder
        self.rate = rate
        self.index = index
        self.expr = expr
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['operator'] = self.operator

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.datum is not None:
            result['datum'] = self.datum

        if self.cond is not None:
            result['cond'] = self.cond

        if self.divisor is not None:
            result['divisor'] = self.divisor

        if self.remainder is not None:
            result['remainder'] = self.remainder

        if self.rate is not None:
            result['rate'] = self.rate

        if self.index is not None:
            result['index'] = self.index

        if self.expr is not None:
            result['expr'] = self.expr

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('datum') is not None:
            self.datum = m.get('datum')

        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('divisor') is not None:
            self.divisor = m.get('divisor')

        if m.get('remainder') is not None:
            self.remainder = m.get('remainder')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class RulesValueRulesSpringcloud(DaraModel):
    def __init__(
        self,
        condition: str = None,
        rest_items: List[main_models.RulesValueRulesSpringcloudRestItems] = None,
        trigger_policy: str = None,
        enable: bool = None,
        app_id: str = None,
        priority: int = None,
        tags: List[str] = None,
        paths: List[str] = None,
        path: str = None,
    ):
        self.condition = condition
        self.rest_items = rest_items
        self.trigger_policy = trigger_policy
        self.enable = enable
        self.app_id = app_id
        self.priority = priority
        self.tags = tags
        self.paths = paths
        self.path = path

    def validate(self):
        if self.rest_items:
            for v1 in self.rest_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        result['restItems'] = []
        if self.rest_items is not None:
            for k1 in self.rest_items:
                result['restItems'].append(k1.to_map() if k1 else None)

        if self.trigger_policy is not None:
            result['triggerPolicy'] = self.trigger_policy

        if self.enable is not None:
            result['enable'] = self.enable

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.tags is not None:
            result['tags'] = self.tags

        if self.paths is not None:
            result['paths'] = self.paths

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        self.rest_items = []
        if m.get('restItems') is not None:
            for k1 in m.get('restItems'):
                temp_model = main_models.RulesValueRulesSpringcloudRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        if m.get('triggerPolicy') is not None:
            self.trigger_policy = m.get('triggerPolicy')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('paths') is not None:
            self.paths = m.get('paths')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class RulesValueRulesSpringcloudRestItems(DaraModel):
    def __init__(
        self,
        datum: str = None,
        operator: str = None,
        name_list: List[str] = None,
        cond: str = None,
        divisor: int = None,
        remainder: int = None,
        rate: int = None,
        type: str = None,
        name: str = None,
        value: Any = None,
    ):
        self.datum = datum
        self.operator = operator
        self.name_list = name_list
        self.cond = cond
        self.divisor = divisor
        self.remainder = remainder
        self.rate = rate
        self.type = type
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datum is not None:
            result['datum'] = self.datum

        if self.operator is not None:
            result['operator'] = self.operator

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.cond is not None:
            result['cond'] = self.cond

        if self.divisor is not None:
            result['divisor'] = self.divisor

        if self.remainder is not None:
            result['remainder'] = self.remainder

        if self.rate is not None:
            result['rate'] = self.rate

        if self.type is not None:
            result['type'] = self.type

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datum') is not None:
            self.datum = m.get('datum')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('divisor') is not None:
            self.divisor = m.get('divisor')

        if m.get('remainder') is not None:
            self.remainder = m.get('remainder')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

