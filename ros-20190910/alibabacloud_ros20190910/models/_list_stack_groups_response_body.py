# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_groups: List[main_models.ListStackGroupsResponseBodyStackGroups] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stack groups.
        self.stack_groups = stack_groups
        # The total number of stack groups.
        self.total_count = total_count

    def validate(self):
        if self.stack_groups:
            for v1 in self.stack_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StackGroups'] = []
        if self.stack_groups is not None:
            for k1 in self.stack_groups:
                result['StackGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stack_groups = []
        if m.get('StackGroups') is not None:
            for k1 in m.get('StackGroups'):
                temp_model = main_models.ListStackGroupsResponseBodyStackGroups()
                self.stack_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStackGroupsResponseBodyStackGroups(DaraModel):
    def __init__(
        self,
        auto_deployment: main_models.ListStackGroupsResponseBodyStackGroupsAutoDeployment = None,
        create_time: str = None,
        description: str = None,
        drift_detection_time: str = None,
        permission_model: str = None,
        resource_group_id: str = None,
        stack_group_drift_status: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
        tags: List[main_models.ListStackGroupsResponseBodyStackGroupsTags] = None,
        update_time: str = None,
    ):
        # The information about automatic deployment settings.
        self.auto_deployment = auto_deployment
        self.create_time = create_time
        # The description of the stack group.
        self.description = description
        # The time when the most recent successful drift detection was performed on the stack group.
        self.drift_detection_time = drift_detection_time
        # The permission model of the stack group.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED
        # *   SERVICE_MANAGED
        # 
        # > For more information about the permission models of stack groups, see [Overview](https://help.aliyun.com/document_detail/154578.html).
        self.permission_model = permission_model
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The drift state of the stack group on which the most recent successful drift detection was performed.
        # 
        # Valid values:
        # 
        # *   DRIFTED: The stack group has drifted.
        # *   NOT_CHECKED: No drift detection is performed on the stack group.
        # *   IN_SYNC: No drifts are detected on the stack group.
        self.stack_group_drift_status = stack_group_drift_status
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the stack group.
        # 
        # Valid values:
        # 
        # *   ACTIVE
        # *   DELETED
        self.status = status
        # The tags that are added to the stack group.
        self.tags = tags
        self.update_time = update_time

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time

        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeployment') is not None:
            temp_model = main_models.ListStackGroupsResponseBodyStackGroupsAutoDeployment()
            self.auto_deployment = temp_model.from_map(m.get('AutoDeployment'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')

        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListStackGroupsResponseBodyStackGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListStackGroupsResponseBodyStackGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is added to the stack group.
        self.key = key
        # The value of the tag that is added to the stack group.
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

class ListStackGroupsResponseBodyStackGroupsAutoDeployment(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If you add a member to the folder to which the stack group belongs after automatic deployment is enabled, Resource Orchestration Service (ROS) automatically adds the stack instances in the stack group to the specified region of the member. If you delete the member from the folder, ROS automatically deletes the stack instances in the stack group from the specified region of the member.
        # *   false: Automatic deployment is disabled. After you disable automatic deployment, the stack instances remain unchanged when you change the member in the folder.
        self.enabled = enabled
        # Indicates whether the stacks within a member are retained when you delete the member from the folder.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # > This parameter is returned only if Enabled is set to true.
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')

        return self

