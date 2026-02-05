# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instances = instances
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        creator_id: int = None,
        creator_name: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_preset: bool = None,
        max_concurrent_conversation: int = None,
        owner_name: str = None,
        resource_group_id: str = None,
        resource_tags: List[main_models.ListInstancesResponseBodyInstancesResourceTags] = None,
    ):
        self.creation_time = creation_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.is_preset = is_preset
        self.max_concurrent_conversation = max_concurrent_conversation
        self.owner_name = owner_name
        self.resource_group_id = resource_group_id
        self.resource_tags = resource_tags

    def validate(self):
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_preset is not None:
            result['IsPreset'] = self.is_preset

        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ResourceTags'] = []
        if self.resource_tags is not None:
            for k1 in self.resource_tags:
                result['ResourceTags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsPreset') is not None:
            self.is_preset = m.get('IsPreset')

        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resource_tags = []
        if m.get('ResourceTags') is not None:
            for k1 in m.get('ResourceTags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        return self

class ListInstancesResponseBodyInstancesResourceTags(DaraModel):
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

