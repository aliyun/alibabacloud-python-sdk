# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysRequest(DaraModel):
    def __init__(
        self,
        tag_filter: main_models.ListTagKeysRequestTagFilter = None,
        category: str = None,
        fuzzy_type: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.tag_filter = tag_filter
        # The type of the resource tags. This parameter specifies a filter condition for the query. Valid values:
        # 
        # - all (default value)
        # 
        # - custom
        # 
        # - system
        # 
        # > The value of this parameter is not case-sensitive.
        self.category = category
        # The type of the query. Valid values:
        # 
        # - EQUAL (default): exact match
        # 
        # - PREFIX: prefix-based fuzzy match
        self.fuzzy_type = fuzzy_type
        # The token that is used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of tag keys to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.page_size = page_size
        # The category of the tags. This parameter specifies a filter condition for the query. Valid values:
        # 
        # - ResourceTag: resource tags, including custom and system tags. This is the default value.
        # 
        # - MetaTag: preset tags.
        # 
        # > The value of this parameter is not case-sensitive.
        self.query_type = query_type
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](https://help.aliyun.com/document_detail/2330902.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # Format: `ALIYUN::${ProductCode}::${ResourceType}`. All letters in the value of this parameter must be in uppercase.
        # 
        # - `ProductCode`: the service code. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](https://help.aliyun.com/document_detail/2330915.html) operation.
        # 
        # - `ResourceType`: the resource type. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](https://help.aliyun.com/document_detail/2330915.html) operation.
        self.resource_type = resource_type

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()

        if self.category is not None:
            result['Category'] = self.category

        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = main_models.ListTagKeysRequestTagFilter()
            self.tag_filter = temp_model.from_map(m.get('TagFilter'))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ListTagKeysRequestTagFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The tag key for a fuzzy query.
        # 
        # This parameter is used together with the `FuzzyType` parameter.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

