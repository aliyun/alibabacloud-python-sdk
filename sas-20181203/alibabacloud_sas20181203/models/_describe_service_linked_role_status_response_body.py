# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceLinkedRoleStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role_status: main_models.DescribeServiceLinkedRoleStatusResponseBodyRoleStatus = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status information about the service-linked role.
        self.role_status = role_status

    def validate(self):
        if self.role_status:
            self.role_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_status is not None:
            result['RoleStatus'] = self.role_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleStatus') is not None:
            temp_model = main_models.DescribeServiceLinkedRoleStatusResponseBodyRoleStatus()
            self.role_status = temp_model.from_map(m.get('RoleStatus'))

        return self

class DescribeServiceLinkedRoleStatusResponseBodyRoleStatus(DaraModel):
    def __init__(
        self,
        status: bool = None,
    ):
        # Indicates whether the service-linked role is created. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

