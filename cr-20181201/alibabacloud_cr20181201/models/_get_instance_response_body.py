# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        instance_issue: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        is_success: bool = None,
        modified_time: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.GetInstanceResponseBodyTags] = None,
    ):
        self.code = code
        # The time when the instance was created.
        self.create_time = create_time
        # The ID of the Container Registry instance.
        self.instance_id = instance_id
        # The issue occurs on the instance.
        self.instance_issue = instance_issue
        # The name of the instance.
        self.instance_name = instance_name
        # The edition of the instance. Valid values: Enterprise_Basic: Basic Edition instances Enterprise_Standard: Standard Edition instances Enterprise_Advanced: Advanced Edition instances
        self.instance_specification = instance_specification
        # The status of the instance. Valid values:
        # 
        # *   `PENDING`: The instance is being initialized.
        # *   `INIT_ERROR`: The instance failed to be initialized.
        # *   `STARTING`: The instance is being started.
        # *   `RUNNING`: The instance is running.
        # *   `STOPPING`: The instance is being stopped.
        # *   `STOPPED`: The instance is stopped.
        # *   `DELETING`: The instance is being deleted.
        # *   `DELETED`: The instance is deleted.
        self.instance_status = instance_status
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the instance was last modified.
        self.modified_time = modified_time
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the instance.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_issue is not None:
            result['InstanceIssue'] = self.instance_issue

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIssue') is not None:
            self.instance_issue = m.get('InstanceIssue')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetInstanceResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

