# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceAlarmStatisticsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        resource_directory_account_id: int = None,
        uuid: str = None,
    ):
        # The data source from which instance alert statistics are collected. Default value: aqs.
        # 
        # Valid values:
        # - **sas**: Threat Detection Service data source.
        # - **aqs**: alert event data.
        # - **honeypot**: cloud honeypot.
        self.from_ = from_
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The UUID of the server to query.
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain this parameter.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

