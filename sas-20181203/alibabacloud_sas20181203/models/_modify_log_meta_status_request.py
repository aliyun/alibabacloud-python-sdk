# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLogMetaStatusRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        log_store: str = None,
        project: str = None,
        resource_directory_account_id: int = None,
        status: str = None,
    ):
        # The ID of the request source. Set the value to **sas**.
        self.from_ = from_
        # The name of the dedicated Logstore in which logs are stored.
        # 
        # >  You can call the [DescribeLogMeta](~~DescribeLogMeta~~) operation to query the names of Logstores.
        # 
        # This parameter is required.
        self.log_store = log_store
        # The name of the project.
        # 
        # >  You can call the [DescribeLogMeta](~~DescribeLogMeta~~) operation to query the names of projects.
        self.project = project
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The status of the log analysis feature. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

