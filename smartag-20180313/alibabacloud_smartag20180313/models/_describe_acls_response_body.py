# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeACLsResponseBody(DaraModel):
    def __init__(
        self,
        acls: main_models.DescribeACLsResponseBodyAcls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.acls = acls
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
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
            temp_model = main_models.DescribeACLsResponseBodyAcls()
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

class DescribeACLsResponseBodyAcls(DaraModel):
    def __init__(
        self,
        acl: List[main_models.DescribeACLsResponseBodyAclsAcl] = None,
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
                temp_model = main_models.DescribeACLsResponseBodyAclsAcl()
                self.acl.append(temp_model.from_map(k1))

        return self

class DescribeACLsResponseBodyAclsAcl(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_type: str = None,
        name: str = None,
        resource_group_id: str = None,
        sag_count: str = None,
    ):
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.name = name
        self.resource_group_id = resource_group_id
        self.sag_count = sag_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sag_count is not None:
            result['SagCount'] = self.sag_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SagCount') is not None:
            self.sag_count = m.get('SagCount')

        return self

