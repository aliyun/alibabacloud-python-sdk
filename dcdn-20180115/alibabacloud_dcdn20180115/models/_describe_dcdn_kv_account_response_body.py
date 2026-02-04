# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnKvAccountResponseBody(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        namespace_list: List[main_models.DescribeDcdnKvAccountResponseBodyNamespaceList] = None,
        namespace_quota: int = None,
        namespace_used: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.capacity = capacity
        # The available capacity of all namespaces.
        self.capacity_string = capacity_string
        self.capacity_used = capacity_used
        # All namespaces have used capacity.
        self.capacity_used_string = capacity_used_string
        # Details about the namespaces.
        self.namespace_list = namespace_list
        # The maximum number of namespaces that you can apply for by using your account.
        self.namespace_quota = namespace_quota
        # The number of namespaces that you applied for by using your account.
        self.namespace_used = namespace_used
        # The ID of the request.
        self.request_id = request_id
        # The status of the account.
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
        self.status = status

    def validate(self):
        if self.namespace_list:
            for v1 in self.namespace_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string

        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used

        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string

        result['NamespaceList'] = []
        if self.namespace_list is not None:
            for k1 in self.namespace_list:
                result['NamespaceList'].append(k1.to_map() if k1 else None)

        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota

        if self.namespace_used is not None:
            result['NamespaceUsed'] = self.namespace_used

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')

        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')

        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')

        self.namespace_list = []
        if m.get('NamespaceList') is not None:
            for k1 in m.get('NamespaceList'):
                temp_model = main_models.DescribeDcdnKvAccountResponseBodyNamespaceList()
                self.namespace_list.append(temp_model.from_map(k1))

        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')

        if m.get('NamespaceUsed') is not None:
            self.namespace_used = m.get('NamespaceUsed')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDcdnKvAccountResponseBodyNamespaceList(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        status: str = None,
    ):
        self.capacity = capacity
        # The available capacity of the namespace.
        self.capacity_string = capacity_string
        self.capacity_used = capacity_used
        # The namespace has used capacity.
        self.capacity_used_string = capacity_used_string
        # The description of the namespace.
        self.description = description
        # The name of the namespace.
        self.namespace = namespace
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The status of the namespace. Valid values:
        # 
        # *   **online**: normal
        # *   **delete**: pending delete
        # *   **deleting**: being deleted
        # *   **deleted**: deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string

        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used

        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string

        if self.description is not None:
            result['Description'] = self.description

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')

        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')

        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

