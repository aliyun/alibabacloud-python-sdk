# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupDynamicRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resource: main_models.DescribeMonitorGroupDynamicRulesResponseBodyResource = None,
        success: bool = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The resources that are associated with the application group.
        self.resource = resource
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resource') is not None:
            temp_model = main_models.DescribeMonitorGroupDynamicRulesResponseBodyResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMonitorGroupDynamicRulesResponseBodyResource(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupDynamicRulesResponseBodyResourceResource(DaraModel):
    def __init__(
        self,
        category: str = None,
        filter_relation: str = None,
        filters: main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFilters = None,
    ):
        # The type of the cloud service to which the dynamic rule belongs. Valid values:
        # 
        # *   ecs: Elastic Compute Service (ECS)
        # *   rds: ApsaraDB RDS
        # *   slb: Server Load Balancer (SLB)
        self.category = category
        # The filter condition. Valid values:
        # 
        # *   and: queries the instances that meet all alert rules.
        # *   or: queries the instances that meet any alert rule.
        self.filter_relation = filter_relation
        # The dynamic rules of the application group.
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.filter_relation is not None:
            result['FilterRelation'] = self.filter_relation

        if self.filters is not None:
            result['Filters'] = self.filters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('FilterRelation') is not None:
            self.filter_relation = m.get('FilterRelation')

        if m.get('Filters') is not None:
            temp_model = main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        return self

class DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFilters(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFiltersFilter] = None,
    ):
        self.filter = filter

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFiltersFilter()
                self.filter.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupDynamicRulesResponseBodyResourceResourceFiltersFilter(DaraModel):
    def __init__(
        self,
        function: str = None,
        name: str = None,
        value: str = None,
    ):
        # The method that is used to filter the instances. Valid values:
        # 
        # *   contains: contains
        # *   startWith: starts with a prefix
        # *   endWith: ends with a suffix
        self.function = function
        # The instance name.
        self.name = name
        # The value of the dynamic rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

