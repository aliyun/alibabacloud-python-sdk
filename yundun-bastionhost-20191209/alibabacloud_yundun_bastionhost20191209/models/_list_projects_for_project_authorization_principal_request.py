# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectsForProjectAuthorizationPrincipalRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        skip: int = None,
    ):
        # The instance ID of the Bastionhost instance.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the parameter value.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the project to query. Fuzzy match is supported.
        self.keyword = keyword
        # The maximum number of projects to return per request. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The paging token used to start a paged query. For the first request, do not pass this parameter or pass an empty string of characters.
        self.next_token = next_token
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The number of items to skip.
        # > This parameter takes effect only when NextToken is left empty.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        return self

