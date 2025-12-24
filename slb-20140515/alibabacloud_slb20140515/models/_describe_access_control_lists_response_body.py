# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessControlListsResponseBody(DaraModel):
    def __init__(
        self,
        acls: main_models.DescribeAccessControlListsResponseBodyAcls = None,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of ACLs.
        self.acls = acls
        # The number of ACLs on the current page.
        self.count = count
        # The number of the returned page. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of ACLs.
        self.total_count = total_count

    def validate(self):
        if self.acls:
            self.acls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acls is not None:
            result['Acls'] = self.acls.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acls') is not None:
            temp_model = main_models.DescribeAccessControlListsResponseBodyAcls()
            self.acls = temp_model.from_map(m.get('Acls'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccessControlListsResponseBodyAcls(DaraModel):
    def __init__(
        self,
        acl: List[main_models.DescribeAccessControlListsResponseBodyAclsAcl] = None,
    ):
        self.acl = acl

    def validate(self):
        if self.acl:
            for v1 in self.acl:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Acl'] = []
        if self.acl is not None:
            for k1 in self.acl:
                result['Acl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl = []
        if m.get('Acl') is not None:
            for k1 in m.get('Acl'):
                temp_model = main_models.DescribeAccessControlListsResponseBodyAclsAcl()
                self.acl.append(temp_model.from_map(k1))

        return self

class DescribeAccessControlListsResponseBodyAclsAcl(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        address_ipversion: str = None,
        create_time: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeAccessControlListsResponseBodyAclsAclTags = None,
    ):
        # The ACL ID.
        self.acl_id = acl_id
        # The ACL name.
        self.acl_name = acl_name
        # The IP version that is used by the CLB instance associated with the ACL.
        self.address_ipversion = address_ipversion
        # The time when the CLB instance was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of tags added to the network ACL. The value of this parameter must be a STRING list in the JSON format.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAccessControlListsResponseBodyAclsAclTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeAccessControlListsResponseBodyAclsAclTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAccessControlListsResponseBodyAclsAclTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAccessControlListsResponseBodyAclsAclTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAccessControlListsResponseBodyAclsAclTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

