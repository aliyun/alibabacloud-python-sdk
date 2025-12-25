# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class DescribeNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        namespaces: List[main_models.DescribeNamespacesResponseBodyNamespaces] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.namespaces = namespaces
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['Namespaces'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k1 in m.get('Namespaces'):
                temp_model = main_models.DescribeNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeNamespacesResponseBodyNamespaces(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        ha: bool = None,
        namespace: str = None,
        resource_spec: main_models.DescribeNamespacesResponseBodyNamespacesResourceSpec = None,
        resource_used: main_models.DescribeNamespacesResponseBodyNamespacesResourceUsed = None,
        status: str = None,
        tags: List[main_models.DescribeNamespacesResponseBodyNamespacesTags] = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.ha = ha
        self.namespace = namespace
        self.resource_spec = resource_spec
        self.resource_used = resource_used
        self.status = status
        self.tags = tags

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.resource_used:
            self.resource_used.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.resource_used is not None:
            result['ResourceUsed'] = self.resource_used.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.DescribeNamespacesResponseBodyNamespacesResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('ResourceUsed') is not None:
            temp_model = main_models.DescribeNamespacesResponseBodyNamespacesResourceUsed()
            self.resource_used = temp_model.from_map(m.get('ResourceUsed'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeNamespacesResponseBodyNamespacesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeNamespacesResponseBodyNamespacesTags(DaraModel):
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
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeNamespacesResponseBodyNamespacesResourceUsed(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        cu: float = None,
        memory_gb: float = None,
    ):
        self.cpu = cpu
        self.cu = cu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

class DescribeNamespacesResponseBodyNamespacesResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

