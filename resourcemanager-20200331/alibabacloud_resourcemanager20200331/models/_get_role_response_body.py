# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class GetRoleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role: main_models.GetRoleResponseBodyRole = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the role.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            temp_model = main_models.GetRoleResponseBodyRole()
            self.role = temp_model.from_map(m.get('Role'))

        return self

class GetRoleResponseBodyRole(DaraModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: main_models.GetRoleResponseBodyRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the role.
        self.arn = arn
        # The document of the policy in which the identity that can assume the role is specified.
        self.assume_role_policy_document = assume_role_policy_document
        # The time when the role was created.
        self.create_date = create_date
        # The description of the role.
        self.description = description
        # Indicates whether the role is a service-linked role.
        self.is_service_linked_role = is_service_linked_role
        # The information of the most recent deletion task.
        self.latest_deletion_task = latest_deletion_task
        # The maximum session duration of the role.
        self.max_session_duration = max_session_duration
        # The ID of the role.
        self.role_id = role_id
        # The name of the role.
        self.role_name = role_name
        # The name of the role after authorization.
        self.role_principal_name = role_principal_name
        # The time when the role was updated.
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role

        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()

        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')

        if m.get('LatestDeletionTask') is not None:
            temp_model = main_models.GetRoleResponseBodyRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m.get('LatestDeletionTask'))

        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class GetRoleResponseBodyRoleLatestDeletionTask(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        # The time when the deletion task was created.
        self.create_date = create_date
        # The ID of the deletion task.
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')

        return self

