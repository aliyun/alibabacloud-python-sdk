# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainGroupsResponseBody(DaraModel):
    def __init__(
        self,
        domain_groups: main_models.DescribeDomainGroupsResponseBodyDomainGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain name groups.
        self.domain_groups = domain_groups
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domain_groups:
            self.domain_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_groups is not None:
            result['DomainGroups'] = self.domain_groups.to_map()

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
        if m.get('DomainGroups') is not None:
            temp_model = main_models.DescribeDomainGroupsResponseBodyDomainGroups()
            self.domain_groups = temp_model.from_map(m.get('DomainGroups'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainGroupsResponseBodyDomainGroups(DaraModel):
    def __init__(
        self,
        domain_group: List[main_models.DescribeDomainGroupsResponseBodyDomainGroupsDomainGroup] = None,
    ):
        self.domain_group = domain_group

    def validate(self):
        if self.domain_group:
            for v1 in self.domain_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainGroup'] = []
        if self.domain_group is not None:
            for k1 in self.domain_group:
                result['DomainGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_group = []
        if m.get('DomainGroup') is not None:
            for k1 in m.get('DomainGroup'):
                temp_model = main_models.DescribeDomainGroupsResponseBodyDomainGroupsDomainGroup()
                self.domain_group.append(temp_model.from_map(k1))

        return self

class DescribeDomainGroupsResponseBodyDomainGroupsDomainGroup(DaraModel):
    def __init__(
        self,
        domain_count: int = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The number of domain name groups.
        self.domain_count = domain_count
        # The ID of the domain name group. Valid values:
        # 
        # *   defaultGroup: the default group
        # *   If an empty string is returned, it indicates the group that contains all domain names.
        self.group_id = group_id
        # The name of the domain name group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

