# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVulStatisticsRequest(DaraModel):
    def __init__(
        self,
        group_id_list: str = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
        type_list: str = None,
    ):
        # The ID of the asset group. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of asset groups.
        # 
        # This parameter is required.
        self.group_id_list = group_id_list
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the vulnerability whose statistics you want to query. Separate multiple types with commas (,). Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **emg**: urgent vulnerability
        # *   **app**: vulnerability detected by using a web scanner
        # *   **sca**: vulnerability detected based on software component analysis
        # 
        # This parameter is required.
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

