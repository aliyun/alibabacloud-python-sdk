# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeGreyTagRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The status code of the API call or a POP error code. Valid values:
        # 
        # - **2xx**: The request is successful.
        # 
        # - **3xx**: The request is redirected.
        # 
        # - **4xx**: A client-side error occurred.
        # 
        # - **5xx**: A server-side error occurred.
        self.code = code
        # The details of the canary rule.
        self.data = data
        # The error code. Valid values:
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - If the request fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The message that indicates the result of the call.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID for querying the details of a call.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeGreyTagRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        alb_rules: List[main_models.DescribeGreyTagRouteResponseBodyDataAlbRules] = None,
        app_id: str = None,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[main_models.DescribeGreyTagRouteResponseBodyDataDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[main_models.DescribeGreyTagRouteResponseBodyDataScRules] = None,
        update_time: int = None,
    ):
        # The canary rules for the Application Load Balancer (ALB) instance.
        self.alb_rules = alb_rules
        # The application ID.
        self.app_id = app_id
        # The creation timestamp of the rule, in milliseconds.
        self.create_time = create_time
        # The description of the canary rule.
        self.description = description
        # The canary rules for the Dubbo service.
        self.dubbo_rules = dubbo_rules
        # The globally unique ID of the canary rule.
        self.grey_tag_route_id = grey_tag_route_id
        # The name of the canary rule.
        self.name = name
        # The canary rules for the Spring Cloud application.
        self.sc_rules = sc_rules
        # The timestamp of the rule\\"s last update, in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.alb_rules:
            for v1 in self.alb_rules:
                 if v1:
                    v1.validate()
        if self.dubbo_rules:
            for v1 in self.dubbo_rules:
                 if v1:
                    v1.validate()
        if self.sc_rules:
            for v1 in self.sc_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlbRules'] = []
        if self.alb_rules is not None:
            for k1 in self.alb_rules:
                result['AlbRules'].append(k1.to_map() if k1 else None)

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k1 in self.dubbo_rules:
                result['DubboRules'].append(k1.to_map() if k1 else None)

        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id

        if self.name is not None:
            result['Name'] = self.name

        result['ScRules'] = []
        if self.sc_rules is not None:
            for k1 in self.sc_rules:
                result['ScRules'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_rules = []
        if m.get('AlbRules') is not None:
            for k1 in m.get('AlbRules'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataAlbRules()
                self.alb_rules.append(temp_model.from_map(k1))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k1 in m.get('DubboRules'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k1))

        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k1 in m.get('ScRules'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataScRules()
                self.sc_rules.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeGreyTagRouteResponseBodyDataScRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        items: List[main_models.DescribeGreyTagRouteResponseBodyDataScRulesItems] = None,
        path: str = None,
    ):
        # The relationship between the conditions in the rule. Valid values:
        # 
        # - **AND**: All conditions must be met.
        # 
        # - **OR**: At least one condition must be met.
        self.condition = condition
        # The list of conditions.
        self.items = items
        # The path to which the rule applies.
        self.path = path

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
        if self.condition is not None:
            result['condition'] = self.condition

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataScRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class DescribeGreyTagRouteResponseBodyDataScRulesItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        # The comparison operator. Valid values are **>**, **<**, **>=**, **<=**, **==**, and **!=**.
        self.cond = cond
        # Not used in Spring Cloud applications.
        self.expr = expr
        # Not used in Spring Cloud applications.
        self.index = index
        # The name of the element to match, as specified by the type parameter. For example, a header name or cookie name.
        self.name = name
        # The matching operator. Valid values:
        # 
        # - **rawvalue**: Performs a direct comparison.
        # 
        # - **list**: Matches against an allowlist of values.
        # 
        # - **mod**: Calculates the remainder of a division by 100.
        # 
        # - **deterministic_proportional_steaming_division**: Performs a percentage-based match.
        self.operator = operator
        # The type of request element to match against. Valid values:
        # 
        # - **param**: A request parameter.
        # 
        # - **cookie**: A cookie.
        # 
        # - **header**: A request header.
        self.type = type
        # The value to match. This value is compared with the actual value of the element specified by **type** and **name**.
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

        if self.expr is not None:
            result['expr'] = self.expr

        if self.index is not None:
            result['index'] = self.index

        if self.name is not None:
            result['name'] = self.name

        if self.operator is not None:
            result['operator'] = self.operator

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeGreyTagRouteResponseBodyDataDubboRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[main_models.DescribeGreyTagRouteResponseBodyDataDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        # The relationship between the conditions in the rule. Valid values:
        # 
        # - **AND**: All conditions must be met.
        # 
        # - **OR**: At least one condition must be met.
        self.condition = condition
        # The service group to which the canary rule applies.
        self.group = group
        # The list of conditions.
        self.items = items
        # The method name of the Dubbo service.
        self.method_name = method_name
        # The Dubbo service name.
        self.service_name = service_name
        # The Dubbo service version.
        self.version = version

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
        if self.condition is not None:
            result['condition'] = self.condition

        if self.group is not None:
            result['group'] = self.group

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.method_name is not None:
            result['methodName'] = self.method_name

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('group') is not None:
            self.group = m.get('group')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataDubboRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeGreyTagRouteResponseBodyDataDubboRulesItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        # The comparison operator. Valid values are **>**, **<**, **>=**, **<=**, **==**, and **!=**.
        self.cond = cond
        # The expression that is used to obtain the parameter value. Valid values:
        # 
        # - **Leave empty**: If left empty, the value of the parameter itself is used.
        # 
        # - **.name**: Obtains the value of the `name` attribute of the parameter. This is equivalent to `args0.getName()`.
        # 
        # - **.isEnabled()**: Obtains the value of the `enabled` attribute of the parameter. This is equivalent to `args0.isEnabled()`.
        # 
        # - **[0]**: The parameter must be an array. This expression obtains the first value of the array, which is equivalent to `args0[0]`. Note that the expression does not start with a period (.).
        # 
        # - **.get(0)**: The parameter must be a list. This expression obtains the first value of the list, which is equivalent to `args0.get(0)`.
        # 
        # - **.get("key")**: The parameter must be a map. This expression obtains the value that corresponds to a key. This is equivalent to `args0.get("key")`.
        self.expr = expr
        # The parameter index. `0` indicates the first parameter.
        self.index = index
        # Not used in Dubbo services.
        self.name = name
        # The matching operator. Valid values:
        # 
        # - **rawvalue**: Performs a direct comparison.
        # 
        # - **list**: Matches against an allowlist of values.
        # 
        # - **mod**: Calculates the remainder of a division by 100.
        # 
        # - **deterministic_proportional_steaming_division**: Performs a percentage-based match.
        self.operator = operator
        # Not used in Dubbo services.
        self.type = type
        # The value to match. This value is compared with the actual value retrieved by using the specified **expr** and **index**.
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

        if self.expr is not None:
            result['expr'] = self.expr

        if self.index is not None:
            result['index'] = self.index

        if self.name is not None:
            result['name'] = self.name

        if self.operator is not None:
            result['operator'] = self.operator

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeGreyTagRouteResponseBodyDataAlbRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        ingress_id: str = None,
        items: List[main_models.DescribeGreyTagRouteResponseBodyDataAlbRulesItems] = None,
        service_id: str = None,
    ):
        # The relationship between the conditions in the canary rule. Only **AND** is supported, which indicates that all conditions must be met.
        self.condition = condition
        # The ID of the Ingress.
        self.ingress_id = ingress_id
        # The list of conditions.
        self.items = items
        # The routing service ID.
        self.service_id = service_id

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
        if self.condition is not None:
            result['condition'] = self.condition

        if self.ingress_id is not None:
            result['ingressId'] = self.ingress_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('ingressId') is not None:
            self.ingress_id = m.get('ingressId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeGreyTagRouteResponseBodyDataAlbRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

class DescribeGreyTagRouteResponseBodyDataAlbRulesItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        # Currently supports ==.
        self.cond = cond
        # Not required for ALB applications.
        self.expr = expr
        # Not required for ALB applications.
        self.index = index
        # The name of the element to match, such as a header or cookie name. This parameter is not used if type is set to sourceIp.
        self.name = name
        # The matching operator. Only **rawvalue** is supported, which indicates a direct comparison.
        self.operator = operator
        # The type of request element to match against. Valid values:
        # 
        # - **sourceIp**: The source IP address.
        # 
        # - **cookie**: A cookie.
        # 
        # - **header**: A request header.
        self.type = type
        # The value to match. This value is compared with the actual value of the element specified by **type** and **name**.
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

        if self.expr is not None:
            result['expr'] = self.expr

        if self.index is not None:
            result['index'] = self.index

        if self.name is not None:
            result['name'] = self.name

        if self.operator is not None:
            result['operator'] = self.operator

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

