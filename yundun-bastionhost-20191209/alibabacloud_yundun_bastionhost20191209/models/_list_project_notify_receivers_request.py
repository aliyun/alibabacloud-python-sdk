# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectNotifyReceiversRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        project_id: int = None,
        region_id: str = None,
        skip: int = None,
    ):
        # The instance ID of the bastion host. 
        # > You can invoke [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) to obtain this parameter.
        self.instance_id = instance_id
        # The name, phone number, or email address of the notification recipient to query. Fuzzy match is supported.
        self.keyword = keyword
        # The number of entries to query. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The request token. Leave this parameter empty or set it to an empty string for the first request.
        self.next_token = next_token
        # The project ID.
        # > You can call ListProjects to obtain this parameter.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The number of entries to skip.
        # > This parameter takes effect only when NextToken is empty.
        self.skip = skip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skip is not None:
            result['Skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        return self

