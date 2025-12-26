# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class UntagCloudResourcesResponseBody(DaraModel):
    def __init__(
        self,
        failed_resources: List[main_models.UntagCloudResourcesResponseBodyFailedResources] = None,
        request_id: str = None,
    ):
        # The cloud resources whose tags failed to be removed and the corresponding tags.
        self.failed_resources = failed_resources
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            for v1 in self.failed_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedResources'] = []
        if self.failed_resources is not None:
            for k1 in self.failed_resources:
                result['FailedResources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resources = []
        if m.get('FailedResources') is not None:
            for k1 in m.get('FailedResources'):
                temp_model = main_models.UntagCloudResourcesResponseBodyFailedResources()
                self.failed_resources.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UntagCloudResourcesResponseBodyFailedResources(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tags: List[main_models.UntagCloudResourcesResponseBodyFailedResourcesTags] = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The resource IDs.
        self.resource_id = resource_id
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        self.resource_type = resource_type
        # The tags that failed to be removed from the cloud resources.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UntagCloudResourcesResponseBodyFailedResourcesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UntagCloudResourcesResponseBodyFailedResourcesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        # 
        # Valid values:
        # 
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

