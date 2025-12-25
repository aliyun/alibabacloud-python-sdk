# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class DescribeNamespacesRequest(DaraModel):
    def __init__(
        self,
        describe_namespaces_request: main_models.DescribeNamespacesRequestDescribeNamespacesRequest = None,
    ):
        # This parameter is required.
        self.describe_namespaces_request = describe_namespaces_request

    def validate(self):
        if self.describe_namespaces_request:
            self.describe_namespaces_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe_namespaces_request is not None:
            result['DescribeNamespacesRequest'] = self.describe_namespaces_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeNamespacesRequest') is not None:
            temp_model = main_models.DescribeNamespacesRequestDescribeNamespacesRequest()
            self.describe_namespaces_request = temp_model.from_map(m.get('DescribeNamespacesRequest'))

        return self

class DescribeNamespacesRequestDescribeNamespacesRequest(DaraModel):
    def __init__(
        self,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
        region: str = None,
        tags: List[main_models.DescribeNamespacesRequestDescribeNamespacesRequestTags] = None,
    ):
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.region = region
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha is not None:
            result['Ha'] = self.ha

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeNamespacesRequestDescribeNamespacesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeNamespacesRequestDescribeNamespacesRequestTags(DaraModel):
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

