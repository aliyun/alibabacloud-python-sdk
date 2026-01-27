# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskReplicaPairsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        pair_ids: str = None,
        region_id: str = None,
        replica_group_id: str = None,
        resource_group_id: str = None,
        site: str = None,
        tag: List[main_models.DescribeDiskReplicaPairsRequestTag] = None,
    ):
        # The maximum number of entries per page. You can use this parameter together with NextToken.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The name of the replication pair. Fuzzy search is supported.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. If you specify NextToken, the PageSize and PageNumber request parameters do not take effect, and the TotalCount response parameter is invalid.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The IDs of replication pairs. You can specify the IDs of one or more replication pairs and separate the IDs with commas (,). Example: `pair-cn-dsa****,pair-cn-asd****`.
        # 
        # This parameter is empty by default, which indicates that all replication pairs in the specified region are queried. You can specify a maximum of 100 replication pair IDs.
        self.pair_ids = pair_ids
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which async replication is supported.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair-consistent group. You can specify the ID of a replication pair-consistent group to query the replication pairs in the group. Example: `pg-****`.
        # 
        # This parameter is empty by default, which indicates that all replication pairs in the specified region are queried.
        # 
        # >  If this parameter is set to`-`, replication pairs that are not added to any replication pair-consistent groups are returned.
        self.replica_group_id = replica_group_id
        # The ID of the resource group to which the replication pair belongs.
        self.resource_group_id = resource_group_id
        # The type of the site from which the information of replication pairs is retrieved. Valid value:
        # 
        # *   production: primary site
        # *   backup: secondary site
        # 
        # Default value: production.
        self.site = site
        # The tags. Up to 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pair_ids is not None:
            result['PairIds'] = self.pair_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site is not None:
            result['Site'] = self.site

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PairIds') is not None:
            self.pair_ids = m.get('PairIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDiskReplicaPairsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDiskReplicaPairsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

