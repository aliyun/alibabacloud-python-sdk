# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImportableKMSSecretsForHostRequest(DaraModel):
    def __init__(
        self,
        host_id: int = None,
        instance_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The ID of the host.
        # 
        # > Call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to get this ID.
        # 
        # This parameter is required.
        self.host_id = host_id
        # The ID of the bastion host instance.
        # 
        # > Call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to get this ID.
        self.instance_id = instance_id
        # The name of the secret to search for. Fuzzy matching is supported.
        self.keyword = keyword
        # The number of entries to return on each page. Default value: 20.
        self.max_results = max_results
        # The token to retrieve the next page of results.
        # 
        # > You do not need to specify this parameter for the first request. For subsequent requests, use the `NextToken` value from the previous response.
        self.next_token = next_token
        # The region ID of the bastion host.
        # 
        # > For details about the mapping between region IDs and region names, see [Regions and availability zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

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

        return self

