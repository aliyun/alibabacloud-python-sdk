# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsGroupListRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_type: str = None,
        instance_id: str = None,
        tag: List[main_models.OnsGroupListRequestTag] = None,
    ):
        # This parameter is required only when you query specific consumer groups by using the fuzzy search method. If this parameter is not configured, the system queries all consumer groups that can be accessed by the current account.
        # 
        # If you set this parameter to GID_ABC, the information about the consumer groups whose IDs contain GID_ABC is returned. For example, the information about the GID_test_GID_ABC_123 and GID_ABC_356 consumer groups is returned.
        self.group_id = group_id
        # The protocol over which the queried consumer group publishes and subscribes to messages. All clients in a consumer group communicate with the ApsaraMQ for RocketMQ broker over the same protocol. You must create different consumer groups for TCP clients and HTTP clients. Valid values:
        # 
        # *   **tcp**: specifies that the consumer group publishes or subscribes to messages over TCP. This value is the default value.
        # *   **http**: specifies that the consumer group publishes or subscribes to messages over HTTP.
        self.group_type = group_type
        # The ID of the instance to which the consumer group you want to query belongs.
        self.instance_id = instance_id
        # The list of tags that are attached to the consumer group. A maximum of 20 tags can be included in the list.
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

        if self.group_type is not None:
            result['GroupType'] = self.group_type

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

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.OnsGroupListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class OnsGroupListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is attached to the consumer group. This parameter is not required. If you configure this parameter, you must configure the **Key** parameter.**** If you configure both the Key and Value parameters, the consumer groups are filtered based on the specified tag. If you do not configure these parameters, all consumer groups are queried.
        # 
        # *   The value of this parameter cannot be an empty string.
        # *   The tag value must be 1 to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that is attached to the group. This parameter is not required. If you configure this parameter, you must configure the **Key** parameter.**** If you configure both the Key and Value parameters, the consumer groups are filtered based on the specified tag. If you do not configure these parameters, all consumer groups are queried.
        # 
        # *   The value of this parameter can be an empty string.
        # *   The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
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

