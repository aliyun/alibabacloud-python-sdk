# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessControlListsResponseBody(DaraModel):
    def __init__(
        self,
        acls: main_models.DescribeAccessControlListsResponseBodyAcls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ACLs.
        self.acls = acls
        # The page number of the current page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
    ):
        # The ID of the access control policy.
        self.acl_id = acl_id
        # The name of the access control policy.
        self.acl_name = acl_name
        # 访问控制策略组的IP版本。
        # - **IPv4**。
        # - **IPv6**。
        self.address_ipversion = address_ipversion

    def validate(self):
        pass

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        return self

