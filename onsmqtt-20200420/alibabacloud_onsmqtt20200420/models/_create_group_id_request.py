# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class CreateGroupIdRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        tag: List[main_models.CreateGroupIdRequestTag] = None,
    ):
        # The group ID to be created. Valid values:
        # 
        # - The value must start with `GID_` or `GID-` and can contain only letters, digits, hyphens (-), and underscores (_). The value must be 7 to 64 characters in length.
        # - A group ID cannot be modified after it is created. For more information, see [Terms](https://help.aliyun.com/document_detail/42420.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance where the group ID resides.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The array of tag key-value pairs.
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateGroupIdRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateGroupIdRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

