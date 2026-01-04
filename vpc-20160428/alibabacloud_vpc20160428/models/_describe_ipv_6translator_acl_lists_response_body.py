# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIPv6TranslatorAclListsResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6translator_acls: main_models.DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAcls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of network ACLs.
        self.ipv_6translator_acls = ipv_6translator_acls
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6translator_acls:
            self.ipv_6translator_acls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6translator_acls is not None:
            result['Ipv6TranslatorAcls'] = self.ipv_6translator_acls.to_map()

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
        if m.get('Ipv6TranslatorAcls') is not None:
            temp_model = main_models.DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAcls()
            self.ipv_6translator_acls = temp_model.from_map(m.get('Ipv6TranslatorAcls'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAcls(DaraModel):
    def __init__(
        self,
        ipv_6translator_acl: List[main_models.DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAclsIPv6TranslatorAcl] = None,
    ):
        self.ipv_6translator_acl = ipv_6translator_acl

    def validate(self):
        if self.ipv_6translator_acl:
            for v1 in self.ipv_6translator_acl:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IPv6TranslatorAcl'] = []
        if self.ipv_6translator_acl is not None:
            for k1 in self.ipv_6translator_acl:
                result['IPv6TranslatorAcl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6translator_acl = []
        if m.get('IPv6TranslatorAcl') is not None:
            for k1 in m.get('IPv6TranslatorAcl'):
                temp_model = main_models.DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAclsIPv6TranslatorAcl()
                self.ipv_6translator_acl.append(temp_model.from_map(k1))

        return self

class DescribeIPv6TranslatorAclListsResponseBodyIpv6TranslatorAclsIPv6TranslatorAcl(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
    ):
        # The ACL ID.
        self.acl_id = acl_id
        # The ACL name.
        self.acl_name = acl_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        return self

