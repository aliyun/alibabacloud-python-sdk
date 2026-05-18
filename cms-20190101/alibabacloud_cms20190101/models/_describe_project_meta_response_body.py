# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeProjectMetaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        resources: main_models.DescribeProjectMetaResponseBodyResources = None,
        success: bool = None,
        total: str = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.resources = resources
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeProjectMetaResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeProjectMetaResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeProjectMetaResponseBodyResourcesResource] = None,
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
                temp_model = main_models.DescribeProjectMetaResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeProjectMetaResponseBodyResourcesResource(DaraModel):
    def __init__(
        self,
        description: str = None,
        labels: str = None,
        namespace: str = None,
    ):
        self.description = description
        self.labels = labels
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

