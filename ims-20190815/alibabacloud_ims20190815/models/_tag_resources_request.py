# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_principal_name: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The ID of resource N.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource ID is the ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `ResourceId` and `ResourcePrincipalName`.
        self.resource_id = resource_id
        # The name of resource N.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource name is the name of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `ResourceId` and `ResourcePrincipalName`.
        self.resource_principal_name = resource_principal_name
        # The type of the resource. Valid value:
        # 
        # *   user: a Resource Access Management (RAM) user.
        self.resource_type = resource_type
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length. The tag key cannot start with aliyun or acs: and cannot contain `http://` or `https://`.
        self.tag = tag

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class TagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length. The tag key cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

