# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class GetServiceLinkedRoleDeletionStatusResponseBody(DaraModel):
    def __init__(
        self,
        reason: main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReason = None,
        request_id: str = None,
        status: str = None,
    ):
        # The cause for the failure of the deletion task.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The status of the task.
        # 
        # *   SUCCEEDED
        # *   IN_PROGRESS
        # *   FAILED
        # *   NOT_STARTED
        # *   INTERNAL_ERROR
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            temp_model = main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReason()
            self.reason = temp_model.from_map(m.get('Reason'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetServiceLinkedRoleDeletionStatusResponseBodyReason(DaraModel):
    def __init__(
        self,
        message: str = None,
        role_usages: main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages = None,
    ):
        # The failure information.
        self.message = message
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            self.role_usages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.role_usages is not None:
            result['RoleUsages'] = self.role_usages.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RoleUsages') is not None:
            temp_model = main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages()
            self.role_usages = temp_model.from_map(m.get('RoleUsages'))

        return self

class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages(DaraModel):
    def __init__(
        self,
        role_usage: List[main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage] = None,
    ):
        self.role_usage = role_usage

    def validate(self):
        if self.role_usage:
            for v1 in self.role_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RoleUsage'] = []
        if self.role_usage is not None:
            for k1 in self.role_usage:
                result['RoleUsage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_usage = []
        if m.get('RoleUsage') is not None:
            for k1 in m.get('RoleUsage'):
                temp_model = main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage()
                self.role_usage.append(temp_model.from_map(k1))

        return self

class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage(DaraModel):
    def __init__(
        self,
        region: str = None,
        resources: main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Resources') is not None:
            temp_model = main_models.GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        return self

class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources(DaraModel):
    def __init__(
        self,
        resource: List[str] = None,
    ):
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource is not None:
            result['Resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        return self

