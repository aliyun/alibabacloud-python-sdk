# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsWithTagRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListApplicationsWithTagRulesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data overview.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        # 
        # - If the request is successful, a success message is returned.
        # - If the request fails, the cause of the failure is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - `true`: The request is successful.
        # - `false`: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListApplicationsWithTagRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApplicationsWithTagRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The data structure.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        namespace: str = None,
        route_rules: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRules] = None,
        route_status: int = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The MSE namespace to which the application belongs.
        self.namespace = namespace
        # The list of rules.
        self.route_rules = route_rules
        # The routing status. Valid values:
        # 
        # - 0: Disabled.
        # 
        # - 1: Enabled.
        self.route_status = route_status

    def validate(self):
        if self.route_rules:
            for v1 in self.route_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        result['RouteRules'] = []
        if self.route_rules is not None:
            for k1 in self.route_rules:
                result['RouteRules'].append(k1.to_map() if k1 else None)

        if self.route_status is not None:
            result['RouteStatus'] = self.route_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        self.route_rules = []
        if m.get('RouteRules') is not None:
            for k1 in m.get('RouteRules'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRules()
                self.route_rules.append(temp_model.from_map(k1))

        if m.get('RouteStatus') is not None:
            self.route_status = m.get('RouteStatus')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRules(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        id: int = None,
        instance_num: int = None,
        name: str = None,
        rate: int = None,
        rules: main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRules = None,
        status: int = None,
        tag: str = None,
    ):
        # The enabling status of the alert rule. Valid values:
        # 
        # - `true`: Enabled.
        # - `false`: Disabled.
        self.enable = enable
        # The rule ID.
        self.id = id
        # The number of instances.
        self.instance_num = instance_num
        # The rule name.
        self.name = name
        # The proportion.
        self.rate = rate
        # The applicable routes of the rule.
        self.rules = rules
        # The status.
        self.status = status
        # The tag.
        self.tag = tag

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.name is not None:
            result['Name'] = self.name

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Rules') is not None:
            temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRules(DaraModel):
    def __init__(
        self,
        dubbo: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubbo] = None,
        springcloud: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloud] = None,
    ):
        # The Dubbo rule.
        self.dubbo = dubbo
        # The Spring Cloud rule.
        self.springcloud = springcloud

    def validate(self):
        if self.dubbo:
            for v1 in self.dubbo:
                 if v1:
                    v1.validate()
        if self.springcloud:
            for v1 in self.springcloud:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dubbo'] = []
        if self.dubbo is not None:
            for k1 in self.dubbo:
                result['dubbo'].append(k1.to_map() if k1 else None)

        result['springcloud'] = []
        if self.springcloud is not None:
            for k1 in self.springcloud:
                result['springcloud'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dubbo = []
        if m.get('dubbo') is not None:
            for k1 in m.get('dubbo'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubbo()
                self.dubbo.append(temp_model.from_map(k1))

        self.springcloud = []
        if m.get('springcloud') is not None:
            for k1 in m.get('springcloud'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloud()
                self.springcloud.append(temp_model.from_map(k1))

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloud(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        condition: str = None,
        enable: bool = None,
        path: str = None,
        paths: List[str] = None,
        priority: int = None,
        rest_items: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloudRestItems] = None,
        tags: List[str] = None,
        trigger_policy: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The logical relationship among the following items. Valid values: AND and OR.
        self.condition = condition
        # Specifies whether the feature is enabled.
        self.enable = enable
        # The path.
        self.path = path
        # The list of paths.
        self.paths = paths
        # The priority.
        self.priority = priority
        # The list of matching conditions for REST requests.
        self.rest_items = rest_items
        # The list of tags.
        self.tags = tags
        # The policy type.
        self.trigger_policy = trigger_policy

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
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.condition is not None:
            result['condition'] = self.condition

        if self.enable is not None:
            result['enable'] = self.enable

        if self.path is not None:
            result['path'] = self.path

        if self.paths is not None:
            result['paths'] = self.paths

        if self.priority is not None:
            result['priority'] = self.priority

        result['restItems'] = []
        if self.rest_items is not None:
            for k1 in self.rest_items:
                result['restItems'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['tags'] = self.tags

        if self.trigger_policy is not None:
            result['triggerPolicy'] = self.trigger_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('paths') is not None:
            self.paths = m.get('paths')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        self.rest_items = []
        if m.get('restItems') is not None:
            for k1 in m.get('restItems'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloudRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('triggerPolicy') is not None:
            self.trigger_policy = m.get('triggerPolicy')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesSpringcloudRestItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        datum: str = None,
        divisor: int = None,
        name: str = None,
        name_list: List[str] = None,
        operator: str = None,
        rate: int = None,
        remainder: int = None,
        type: str = None,
        value: str = None,
    ):
        # The comparison operator. Valid values: >=, <=, >, <, and ==.
        self.cond = cond
        # The value to be compared for operators such as rawvalue.
        self.datum = datum
        # The field required for the mod operator, which is the divisor.
        self.divisor = divisor
        # The name.
        self.name = name
        # The field required for the list operator.
        self.name_list = name_list
        # The operator. A value of rawvalue indicates direct comparison, mode indicates modulo operation, and list indicates a whitelist.
        self.operator = operator
        # The proportion rule, where 20% of traffic is routed to the node corresponding to this tag.
        self.rate = rate
        # The field required for the percentage operation, which is the percentage value.
        self.remainder = remainder
        # The type.
        self.type = type
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cond is not None:
            result['cond'] = self.cond

        if self.datum is not None:
            result['datum'] = self.datum

        if self.divisor is not None:
            result['divisor'] = self.divisor

        if self.name is not None:
            result['name'] = self.name

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.operator is not None:
            result['operator'] = self.operator

        if self.rate is not None:
            result['rate'] = self.rate

        if self.remainder is not None:
            result['remainder'] = self.remainder

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('datum') is not None:
            self.datum = m.get('datum')

        if m.get('divisor') is not None:
            self.divisor = m.get('divisor')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('remainder') is not None:
            self.remainder = m.get('remainder')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubbo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        argument_items: List[main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubboArgumentItems] = None,
        condition: str = None,
        group: str = None,
        method_name: str = None,
        param_types: List[str] = None,
        service_name: str = None,
        tags: List[str] = None,
        trigger_policy: str = None,
        version: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The list of parameter arguments.
        self.argument_items = argument_items
        # The logical relationship among the following items. Valid values: AND and OR.
        self.condition = condition
        # The Dubbo service group.
        self.group = group
        # The Dubbo service method name.
        self.method_name = method_name
        # The list of parameter types.
        self.param_types = param_types
        # The service name (interface).
        self.service_name = service_name
        # The list of tags.
        self.tags = tags
        # The policy type.
        self.trigger_policy = trigger_policy
        # The Dubbo service version.
        self.version = version

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

        result['argumentItems'] = []
        if self.argument_items is not None:
            for k1 in self.argument_items:
                result['argumentItems'].append(k1.to_map() if k1 else None)

        if self.condition is not None:
            result['condition'] = self.condition

        if self.group is not None:
            result['group'] = self.group

        if self.method_name is not None:
            result['methodName'] = self.method_name

        if self.param_types is not None:
            result['paramTypes'] = self.param_types

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.tags is not None:
            result['tags'] = self.tags

        if self.trigger_policy is not None:
            result['triggerPolicy'] = self.trigger_policy

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        self.argument_items = []
        if m.get('argumentItems') is not None:
            for k1 in m.get('argumentItems'):
                temp_model = main_models.ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubboArgumentItems()
                self.argument_items.append(temp_model.from_map(k1))

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('paramTypes') is not None:
            self.param_types = m.get('paramTypes')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('triggerPolicy') is not None:
            self.trigger_policy = m.get('triggerPolicy')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListApplicationsWithTagRulesResponseBodyDataResultRouteRulesRulesDubboArgumentItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        datum: str = None,
        divisor: int = None,
        expr: str = None,
        index: int = None,
        name_list: List[str] = None,
        operator: str = None,
        rate: int = None,
        remainder: int = None,
        value: str = None,
    ):
        # The comparison operator. Valid values: >=, <=, >, <, and ==.
        self.cond = cond
        # The value to be compared for operators such as rawvalue.
        self.datum = datum
        # The field required for the mod operator, which is the divisor.
        self.divisor = divisor
        # The expression. For more information, see the descriptions of other fields.
        self.expr = expr
        # The parameter position, starting from 0.
        self.index = index
        # The list of names.
        self.name_list = name_list
        # The operator. A value of rawvalue indicates direct comparison, mode indicates modulo operation, and list indicates a whitelist.
        self.operator = operator
        # The proportion rule, where 20% of traffic is routed to the node corresponding to this tag.
        self.rate = rate
        # The field required for the percentage operation, which is the percentage value.
        self.remainder = remainder
        # The value used for comparison. The value obtained from the expression is compared with this value. If the operator is a list whitelist, separate multiple values with commas (,), such as 1,2,3.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cond is not None:
            result['cond'] = self.cond

        if self.datum is not None:
            result['datum'] = self.datum

        if self.divisor is not None:
            result['divisor'] = self.divisor

        if self.expr is not None:
            result['expr'] = self.expr

        if self.index is not None:
            result['index'] = self.index

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.operator is not None:
            result['operator'] = self.operator

        if self.rate is not None:
            result['rate'] = self.rate

        if self.remainder is not None:
            result['remainder'] = self.remainder

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('datum') is not None:
            self.datum = m.get('datum')

        if m.get('divisor') is not None:
            self.divisor = m.get('divisor')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('remainder') is not None:
            self.remainder = m.get('remainder')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

