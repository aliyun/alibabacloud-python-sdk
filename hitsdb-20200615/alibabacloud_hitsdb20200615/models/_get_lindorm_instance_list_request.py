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
        # The page number to return.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query.
        self.page_size = page_size
        # A keyword for a fuzzy search on instance names.
        self.query_str = query_str
        # The ID of the region where the instance is located. Call [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) to obtain the region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The type of the instance. Valid values:
        # 
        # - **lindorm**: a single-zone Lindorm instance.
        # 
        # - **lindorm_multizone**: a multi-zone Lindorm instance.
        # 
        # - **serverless_lindorm**: a Lindorm Serverless instance.
        # 
        # - **lindorm_standalone**: a Lindorm standalone instance.
        # 
        # - **lts**: the Lindorm Tunnel Service (LTS) type.
        self.service_type = service_type
        # The type of the engine supported by the instance that you want to query. Valid values:
        # 
        # - **1**: search engine.
        # 
        # - **2**: LindormTSDB.
        # 
        # - **4**: LindormTable.
        # 
        # - **8**: file engine.
        # 
        # > For example, a value of 15 (8 + 4 + 2 + 1) indicates that the instance supports the file engine, LindormTable, LindormTSDB, and the search engine. A value of 6 (4 + 2) indicates that the instance supports LindormTSDB and LindormTable.
        self.support_engine = support_engine
        # A list of tags. You can specify up to 20 tags.
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
        # The key of the tag.
        # 
        # > You can pass in keys for multiple tags. For example, the Key in the first pair represents the key for the first tag. The Key in the second pair represents the key for the second tag.
        self.key = key
        # The value of the tag.
        # 
        # > You can provide values for multiple tags. For example, the Value in the first pair is the value for the first tag. The Value in the second pair is the value for the second tag.
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

