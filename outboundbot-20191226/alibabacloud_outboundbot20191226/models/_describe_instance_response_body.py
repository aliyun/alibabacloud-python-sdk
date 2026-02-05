# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance: main_models.DescribeInstanceResponseBodyInstance = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance = instance
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Instance') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        creator_id: int = None,
        creator_name: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        owner_name: str = None,
        resource_group_id: str = None,
    ):
        self.creation_time = creation_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.max_concurrent_conversation = max_concurrent_conversation
        self.owner_name = owner_name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

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

        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

