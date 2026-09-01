# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCheckProcessRequest(DaraModel):
    def __init__(
        self,
        resource_directory_account_id: int = None,
        task_id: str = None,
    ):
        # The ID of the member accounts in the resource folder (Alibaba Cloud account).
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The ID of the cloud service configuration check task that you want to query.
        # > You can call the [SubmitCheck](~~SubmitCheck~~) operation to obtain this parameter.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

