# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetMemberDeletionPermissionResponseBody(DaraModel):
    def __init__(
        self,
        management_account_id: str = None,
        member_deletion_status: str = None,
        request_id: str = None,
        resource_directory_id: str = None,
    ):
        # The ID of the management account of the resource directory.
        self.management_account_id = management_account_id
        # The status of the member deletion feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   Disabled: The feature is disabled.
        self.member_deletion_status = member_deletion_status
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.management_account_id is not None:
            result['ManagementAccountId'] = self.management_account_id

        if self.member_deletion_status is not None:
            result['MemberDeletionStatus'] = self.member_deletion_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagementAccountId') is not None:
            self.management_account_id = m.get('ManagementAccountId')

        if m.get('MemberDeletionStatus') is not None:
            self.member_deletion_status = m.get('MemberDeletionStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        return self

