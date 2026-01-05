# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UnTagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.UnTagResourcesRequestTag] = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.all = all
        # The IDs of the resources from which you want to remove tags.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   **acl**: an access control list (ACL)
        # *   **loadbalancer**: an Application Load Balancer (ALB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to remove.
        self.tag = tag
        # The keys of the tags that you want to remove.
        self.tag_key = tag_key

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UnTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

class UnTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that you want to remove. The tag key can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of the tag that you want to remove. The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
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

