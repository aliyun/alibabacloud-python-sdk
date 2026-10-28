# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSynchronizationJobsRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_job_name: str = None,
        tag: List[main_models.DescribeSynchronizationJobsRequestTag] = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because it is about to be deprecated.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, and you must ensure that the token is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_id = owner_id
        # The page number. The value must be an integer greater than **0** and less than or equal to the maximum value of the Integer data type. Default value: **1**.
        self.page_num = page_num
        # The number of entries per page. Valid values: **10**, **20**, and **30**. Default value: **30**. Maximum value: **30**.
        self.page_size = page_size
        # The ID of the region where the data synchronization instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the synchronization instance. Fuzzy matching is supported.
        self.synchronization_job_name = synchronization_job_name
        # The tags of the data synchronization instance, which are used as a filter. If this parameter is not empty, only the instances that have the specified tags are returned.
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSynchronizationJobsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSynchronizationJobsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can call the [ListTagResources](https://help.aliyun.com/document_detail/191187.html) operation to query tag keys.
        # > - N indicates the sequence number of the tag. For example, Tag.1.Key indicates the key of the first tag, and Tag.2.Key indicates the key of the second tag. You can specify 1 to 20 tag keys at a time.
        # - Empty strings are not allowed.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. You can call the [ListTagResources](https://help.aliyun.com/document_detail/191187.html) operation to query tag values.
        # >- N indicates the sequence number of the tag. For example, Tag.1.Value indicates the value of the first tag, and Tag.2.Value indicates the value of the second tag. You can specify 1 to 20 tag values at a time.
        # - Empty strings are allowed.
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

