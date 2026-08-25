# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        provision_type: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # You must specify the value in the `<Attribute> <Operator> <Value>` format. The value is not case-sensitive. You can set `<Attribute>` only to `GroupName` and `<Operator>` only to `eq` or `sw`. The value eq indicates Equals, and the value sw indicates Start With.
        # 
        # For example, if you set Filter to GroupName sw test, the operation queries the groups whose names start with test. If you set Filter to GroupName eq testgroup, the operation queries the group whose name is testgroup.
        self.filter = filter
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        # 
        # When you call this operation for the first time, if the total number of entries to return is larger than the value of the `MaxResults` parameter, the entries are truncated. The system returns entries based on the value of the `MaxResults` parameter, and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and the `NextToken` parameter is returned. In the next call, you can use the value of the `NextToken` parameter and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The type of the group. The type can be used to filter groups. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external IdP.
        self.provision_type = provision_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        return self

