# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormInstanceListRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_str: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        service_type: str = None,
        support_engine: int = None,
        tag: List[main_models.GetLindormInstanceListRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of instances to return on each page.
        self.page_size = page_size
        # The keyword contained in the names of Lindorm instances you want to query. Fuzzy queries based on the keyword is supported.
        self.query_str = query_str
        # The ID of the region in which the instances that you want to query is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The series of instances that you want to query. Valid values:
        # 
        # *   **lindorm**: The instance is a single-zone Lindorm instance.
        # *   **lindorm_multizone**: The instance is a multi-zone Lindorm instance.
        # *   **serverless_lindorm**: The instance is a Lindorm Serverless instance.
        # *   **lindorm_standalone**: The instance is a single-node Lindorm instance.
        # *   **lts**: The instance is an LTS instance.
        self.service_type = service_type
        # The engine supported by the instances that you want to query. The engines are indicated by different numbers:
        # 
        # *   **1**: LindormSearch.
        # *   **2**: LindormTSDB
        # *   **4**: LindormTable
        # *   **8**: LindormDFS
        # 
        # >  The value of this parameter is the sum of all numbers that indicate the engines supported by the instance. For example, if you set the value of this parameter to 15, which is the sum of 1, 2, 4, and 8, this operation queries instances that support all four engines. If you set the value of this parameter to 6, which is the sum of 2 and 4, this operation queries instances that support LindormTSDB and LindormTable.
        self.support_engine = support_engine
        # The list of tags associated with the specified instances.
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_str is not None:
            result['QueryStr'] = self.query_str

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.support_engine is not None:
            result['SupportEngine'] = self.support_engine

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('SupportEngine') is not None:
            self.support_engine = m.get('SupportEngine')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.GetLindormInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class GetLindormInstanceListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the instances you want to query. You can specify 1 to 20 tag keys.
        # 
        # > You can specify the keys of multiple tags. For example, you can specify the key of the first tag in the first key-value pair contained in the value of this parameter and specify the key of the second tag in the second key-value pair.
        self.key = key
        # The value of tag N of the instances you want to query. You can specify 1 to 20 tag values.
        # 
        # > You can specify the values of multiple tags. For example, you can specify the value of the first tag in the first key-value pair contained in the value of this parameter and specify the value of the second tag in the second key-value pair.
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

