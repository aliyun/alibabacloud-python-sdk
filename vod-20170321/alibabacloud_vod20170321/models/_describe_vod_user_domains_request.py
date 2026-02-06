# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodUserDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_search_type: str = None,
        domain_status: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        tag: List[main_models.DescribeVodUserDomainsRequestTag] = None,
    ):
        # The domain name. The value of this parameter is used as a filter condition for a fuzzy match.
        self.domain_name = domain_name
        # The search method. Valid values:
        # 
        # *   **fuzzy_match** (default): fuzzy match.
        # *   **pre_match**: prefix match
        # *   **suf_match**: suffix match
        # *   **full_match**: exact match
        self.domain_search_type = domain_search_type
        # The status of the domain name. Value values:
        # 
        # *   **online**: indicates that the domain name is enabled.
        # *   **offline**: indicates that the domain name is disabled.
        # *   **configuring**: indicates that the domain name is being configured.
        # *   **configure_failed**: indicates that the domain name failed to be configured.
        # *   **checking**: indicates that the domain name is under review.
        # *   **check_failed**: indicates that the domain name failed the review.
        self.domain_status = domain_status
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: **20**. Maximum value: **50**. Valid values: **1** to **50**.
        self.page_size = page_size
        self.security_token = security_token
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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVodUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVodUserDomainsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: **1** to **20**.
        # 
        # By default, all tag keys are queried.
        self.key = key
        # The value of tag N. Valid values of N: **1** to **20**.
        # 
        # By default, all tag values are queried.
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

