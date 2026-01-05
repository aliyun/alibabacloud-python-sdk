# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListAclsRequest(DaraModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tag: List[main_models.ListAclsRequestTag] = None,
    ):
        # Filter access control lists (ACLs) by ACL ID. You can specify at most 20 ACL IDs in each call.
        self.acl_ids = acl_ids
        # The ACL names. You can specify up to 10 ACL names in each call.
        self.acl_names = acl_names
        # The maximum number of entries to return. This parameter is optional. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the resource group. You can filter the query results based on the specified ID.
        self.resource_group_id = resource_group_id
        # The tags.
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
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.acl_names is not None:
            result['AclNames'] = self.acl_names

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('AclNames') is not None:
            self.acl_names = m.get('AclNames')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListAclsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListAclsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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

