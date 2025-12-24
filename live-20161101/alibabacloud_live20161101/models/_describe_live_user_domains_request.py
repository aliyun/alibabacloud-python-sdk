# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUserDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_search_type: str = None,
        domain_status: str = None,
        live_domain_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_name: str = None,
        resource_group_id: str = None,
        security_token: str = None,
        tag: List[main_models.DescribeLiveUserDomainsRequestTag] = None,
    ):
        # The domain name that is used as a keyword to filter domain names. Fuzzy match is supported.
        # 
        # > 
        # 
        # *   If you set LiveDomainType to liveVideo and leave this parameter empty, the streaming domains are queried. - If you set LiveDomainType to liveEdge and leave this parameter empty, the ingest domains are queried.
        self.domain_name = domain_name
        # The search mode. Valid values:
        # 
        # *   **fuzzy_match** (default): fuzzy match
        # *   **pre_match**: prefix match
        # *   **suf_match**: suffix match
        # *   **full_match**: exact match
        self.domain_search_type = domain_search_type
        # The status of the domain name. Valid values:
        # 
        # *   **online**
        # *   **offline**
        # *   **configuring**
        self.domain_status = domain_status
        # The type of the domain name. Valid values:
        # 
        # *   **liveVideo**: streaming domain
        # *   **liveEdge**: ingest domain
        # 
        # >  If you leave this parameter empty, all ingest domains and streaming domains within your Alibaba Cloud account are queried by default.
        self.live_domain_type = live_domain_type
        self.owner_id = owner_id
        # The page number. Valid values: **1 to 100000**.
        self.page_number = page_number
        # The number of entries per page. Default value: **20**. Maximum value: **50**.
        self.page_size = page_size
        # The ID of the region in which the domain name resides.
        self.region_name = region_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
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

        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeLiveUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLiveUserDomainsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

