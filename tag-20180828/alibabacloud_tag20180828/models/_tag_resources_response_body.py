# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class TagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        failed_resources: main_models.TagResourcesResponseBodyFailedResources = None,
        request_id: str = None,
    ):
        self.failed_resources = failed_resources
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            temp_model = main_models.TagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m.get('FailedResources'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TagResourcesResponseBodyFailedResources(DaraModel):
    def __init__(
        self,
        failed_resource: List[main_models.TagResourcesResponseBodyFailedResourcesFailedResource] = None,
    ):
        self.failed_resource = failed_resource

    def validate(self):
        if self.failed_resource:
            for v1 in self.failed_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedResource'] = []
        if self.failed_resource is not None:
            for k1 in self.failed_resource:
                result['FailedResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resource = []
        if m.get('FailedResource') is not None:
            for k1 in m.get('FailedResource'):
                temp_model = main_models.TagResourcesResponseBodyFailedResourcesFailedResource()
                self.failed_resource.append(temp_model.from_map(k1))

        return self

class TagResourcesResponseBodyFailedResourcesFailedResource(DaraModel):
    def __init__(
        self,
        resource_arn: str = None,
        result: main_models.TagResourcesResponseBodyFailedResourcesFailedResourceResult = None,
    ):
        self.resource_arn = resource_arn
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')

        if m.get('Result') is not None:
            temp_model = main_models.TagResourcesResponseBodyFailedResourcesFailedResourceResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class TagResourcesResponseBodyFailedResourcesFailedResourceResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

