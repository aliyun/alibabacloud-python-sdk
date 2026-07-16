# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListResourcesByTagRequest(DaraModel):
    def __init__(
        self,
        tag_filter: main_models.ListResourcesByTagRequestTagFilter = None,
        fuzzy_type: str = None,
        include_all_tags: bool = None,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.tag_filter = tag_filter
        # The type of the query. Valid values:
        # 
        # *   EQUAL: exact match for resources to which the specified tag is added. This is the default value.
        # *   NOT: exact match for resources to which the specified tag is not added.
        self.fuzzy_type = fuzzy_type
        # Specifies whether to return the information of tags added to the resources. Valid values:
        # 
        # *   False: does not return the information of tags added to the resources. This is the default value.
        # *   True: returns the information of all tags added to the resources.
        self.include_all_tags = include_all_tags
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result
        # The token that is used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](https://help.aliyun.com/document_detail/2330902.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # *   If you set the FuzzyType parameter to EQUAL, you can set this parameter to a value obtained from the response of the [ListSupportResourceTypes](https://help.aliyun.com/document_detail/2330915.html) operation.
        # *   If you set the FuzzyType parameter to NOT, you can set this parameter to a resource type provided in **Types of resources that support queries based on the NOT operator**.
        # 
        # This parameter is required.
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

        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type

        if self.include_all_tags is not None:
            result['IncludeAllTags'] = self.include_all_tags

        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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
            temp_model = main_models.ListResourcesByTagRequestTagFilter()
            self.tag_filter = temp_model.from_map(m.get('TagFilter'))

        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')

        if m.get('IncludeAllTags') is not None:
            self.include_all_tags = m.get('IncludeAllTags')

        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ListResourcesByTagRequestTagFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. This parameter specifies a filter condition for the query.
        # 
        # The tag key can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. This parameter specifies a filter condition for the query.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

