# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListGreyTagRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The status of the interface or the POP error code. Valid values:
        # 
        # - **2xx**: The request is successful.
        # 
        # - **3xx**: The request is redirected.
        # 
        # - **4xx**: A request error occurs.
        # 
        # - **5xx**: A server error occurs.
        self.code = code
        # The information about the grayscale rule.
        self.data = data
        # The error code. Valid values:
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the query succeeded.
        # 
        # - **true**: The query succeeded.
        # 
        # - **false**: The query failed.
        self.success = success
        # The trace ID, which is used to query the details of a call.
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
            temp_model = main_models.ListGreyTagRouteResponseBodyData()
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

class ListGreyTagRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        result: List[main_models.ListGreyTagRouteResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page in a paged query. The value can only be **1**.
        self.page_size = page_size
        # The returned result.
        self.result = result
        # The total number of entries. The value can only be **1**.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGreyTagRouteResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        alb_rules: List[main_models.ListGreyTagRouteResponseBodyDataResultAlbRules] = None,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[main_models.ListGreyTagRouteResponseBodyDataResultDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[main_models.ListGreyTagRouteResponseBodyDataResultScRules] = None,
        update_time: int = None,
    ):
        # The grayscale rules created for an application for which an Application Load Balancer (ALB) Ingress is configured.
        self.alb_rules = alb_rules
        # The timestamp when the rule was created. Unit: milliseconds.
        self.create_time = create_time
        # The description of the rule.
        self.description = description
        # The grayscale rules for Dubbo services.
        self.dubbo_rules = dubbo_rules
        # The rule ID.
        self.grey_tag_route_id = grey_tag_route_id
        # The rule name.
        self.name = name
        # The grayscale rules for Spring Cloud.
        self.sc_rules = sc_rules
        # The timestamp when the rule was updated. Unit: milliseconds.
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
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultAlbRules()
                self.alb_rules.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k1 in m.get('DubboRules'):
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k1))

        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k1 in m.get('ScRules'):
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultScRules()
                self.sc_rules.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListGreyTagRouteResponseBodyDataResultScRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        items: List[main_models.ListGreyTagRouteResponseBodyDataResultScRulesItems] = None,
        path: str = None,
    ):
        # The conditional pattern of the grayscale rule. Valid values:
        # 
        # - **AND**: All conditions in the list must be met.
        # 
        # - **OR**: Any condition in the list can be met.
        self.condition = condition
        # The list of conditions.
        self.items = items
        # The path that corresponds to the grayscale rule for the Spring Cloud application.
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
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultScRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class ListGreyTagRouteResponseBodyDataResultScRulesItems(DaraModel):
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
        # The comparison operator. Valid values: **>**, **<**, **>=**, **<=**, **==**, and **!=**.
        self.cond = cond
        # This parameter is not applicable to Spring Cloud applications.
        self.expr = expr
        # This parameter is not applicable to Spring Cloud applications.
        self.index = index
        # The parameter name.
        self.name = name
        # The operator. Valid values:
        # 
        # - **rawvalue**: Direct comparison.
        # 
        # - **list**: Whitelist.
        # 
        # - **mod**: Modulo 100 operation.
        # 
        # - **deterministic_proportional_steaming_division**: Percentage.
        self.operator = operator
        # The comparison type. Valid values:
        # 
        # - **param**: Parameter.
        # 
        # - **cookie**: Cookie.
        # 
        # - **header**: Header.
        self.type = type
        # The parameter value. The value obtained based on **type** and **name** is compared with this value.
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

class ListGreyTagRouteResponseBodyDataResultDubboRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[main_models.ListGreyTagRouteResponseBodyDataResultDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        # The conditional pattern of the grayscale rule. Valid values:
        # 
        # - **AND**: All conditions in the list must be met.
        # 
        # - **OR**: Any condition in the list can be met.
        self.condition = condition
        # The group of the Dubbo service that corresponds to the grayscale rule.
        self.group = group
        # The list of conditions.
        self.items = items
        # The method name of the Dubbo service.
        self.method_name = method_name
        # The name of the Dubbo service.
        self.service_name = service_name
        # The version of the Dubbo service.
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
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultDubboRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListGreyTagRouteResponseBodyDataResultDubboRulesItems(DaraModel):
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
        # The comparison operator. Valid values: **>**, **<**, **>=**, **<=**, **==**, and **!=**.
        self.cond = cond
        # The expression that is used to obtain the parameter value. The syntax follows the Spring Expression Language (SpEL). Valid values:
        # 
        # - **Leave it empty**: Obtains the value of the current parameter.
        # 
        # - **.name**: Obtains the name property of the parameter. This is equivalent to args0.getName().
        # 
        # - **.isEnabled()**: Obtains the enabled property of the parameter. This is equivalent to args0.isEnabled().
        # 
        # - **[0]**: Obtains the first value of the array. This is equivalent to args0[0]. Note that the expression does not start with a period (.).
        # 
        # - **.get(0)**: Obtains the first value of the list. This is equivalent to args0.get(0).
        # 
        # - **.get("key")**: Obtains the value that corresponds to the specified key from the map. This is equivalent to args0.get("key").
        self.expr = expr
        # The parameter number. 0 indicates the first parameter.
        self.index = index
        # This parameter is not applicable to Dubbo services.
        self.name = name
        # The operator. Valid values:
        # 
        # - **rawvalue**: Direct comparison.
        # 
        # - **list**: Whitelist.
        # 
        # - **mod**: Modulo 100 operation.
        # 
        # - **deterministic_proportional_steaming_division**: Percentage.
        self.operator = operator
        # This parameter is not applicable to Dubbo services.
        self.type = type
        # The parameter value. The value obtained based on **expr** and **index** is compared with this value.
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

class ListGreyTagRouteResponseBodyDataResultAlbRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        ingress_id: str = None,
        items: List[main_models.ListGreyTagRouteResponseBodyDataResultAlbRulesItems] = None,
        service_name: str = None,
    ):
        # The conditional pattern of the grayscale rule. Only AND is supported, which indicates that all conditions in the list must be met.
        self.condition = condition
        # The Ingress ID.
        self.ingress_id = ingress_id
        # The list of conditions.
        self.items = items
        # The service name.
        self.service_name = service_name

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

        if self.service_name is not None:
            result['serviceName'] = self.service_name

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
                temp_model = main_models.ListGreyTagRouteResponseBodyDataResultAlbRulesItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

class ListGreyTagRouteResponseBodyDataResultAlbRulesItems(DaraModel):
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
        # Only == is supported.
        self.cond = cond
        # This parameter is not applicable to ALB applications.
        self.expr = expr
        # This parameter is not applicable to ALB applications.
        self.index = index
        # The parameter name.
        self.name = name
        # The operator. Valid values: Only rawvalue is supported, which indicates a direct comparison.
        self.operator = operator
        # The comparison type. Valid values:
        # 
        # - **sourceIp**: SourceIp.
        # 
        # - **cookie**: Cookie.
        # 
        # - **header**: Header.
        self.type = type
        # The parameter value. The value obtained based on type and name is compared with this value.
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

