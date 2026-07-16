# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
    ):
        # The token for the next query.
        self.next_token = next_token
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource to be tagged. Resource ID rules:
        # 
        # - Instance: instanceId
        # 
        # - Topic: Kafka_alikafka_instanceId_topic
        # 
        # - Group: Kafka_alikafka_instanceId_consumerGroup
        # 
        # For example: If the instance ID is alikafka_post-cn-v0h1fgs2xxxx, the Topic name is test-topic, and the Group name is test-consumer-group, the resource IDs are alikafka_post-cn-v0h1fgs2xxxx, Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-topic, and Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-consumer-group respectively.
        # 
        # > Either the **ResourceId** or **Tag** parameter must be configured to query the tag list bound to resources. Otherwise, the API call fails.
        self.resource_id = resource_id
        # The resource type. Enumeration type. Valid values:
        # 
        # - **INSTANCE**: instance.
        # 
        # - **TOPIC**: topic.
        # 
        # - **CONSUMERGROUP**: consumer group.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag list.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # - If this parameter is empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http\\:// or https\\://.
        self.key = key
        # The tag value of the resource.
        # 
        # - If the tag key is empty, this parameter must be empty. If this parameter is empty, all tag values are matched.
        # 
        # - The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http\\:// or https\\://.
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

