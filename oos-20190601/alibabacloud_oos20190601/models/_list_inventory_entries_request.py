# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListInventoryEntriesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListInventoryEntriesRequestFilter] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type_name: str = None,
    ):
        # The filter rules for the component.
        self.filter = filter
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The name of the component. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsRegistry
        # *   ACS:WindowsUpdate
        # 
        # This parameter is required.
        self.type_name = type_name

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListInventoryEntriesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class ListInventoryEntriesRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # The name of the component property. Valid values of N: 1 to 5.
        self.name = name
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator
        # The values of properties. Valid values of the first N: 1 to 5. Valid values of the second N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

