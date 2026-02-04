# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnIpaUserDomainsRequest(DaraModel):
    def __init__(
        self,
        check_domain_show: bool = None,
        domain_name: str = None,
        domain_search_type: str = None,
        domain_status: str = None,
        func_filter: str = None,
        func_id: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeDcdnIpaUserDomainsRequestTag] = None,
    ):
        # Specifies whether to display domain names that are under review, failed the review, or failed to be configured. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.check_domain_show = check_domain_show
        # The domain name that is used as a keyword to filter domain names. Fuzzy match is supported.
        self.domain_name = domain_name
        # The search method. Default value: full_match. Valid values:
        # 
        # *   **fuzzy_match**: fuzzy match
        # *   **pre_match**: prefix match
        # *   **suf_match**: suffix match
        # *   **full_match**: exact match
        self.domain_search_type = domain_search_type
        # The status of the domain name. Valid values:
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
        # *   **configuring**: configuring
        # *   **configure_failed**: configuration failed
        # *   **checking**: reviewing
        # *   **check_failed:** review failed
        self.domain_status = domain_status
        # The status of the feature.
        # 
        # *   config: The feature is enabled.
        # *   unconfig: The feature is not enabled.
        self.func_filter = func_filter
        # The ID of the feature. For example, a value of 7 specifies the feature of configuring an expiration rule for a specific directory. For more information about feature IDs, see [Parameters for configuring features for domain names](https://help.aliyun.com/document_detail/410622.html).
        self.func_id = func_id
        self.owner_id = owner_id
        # The page number. Valid values: **1** to **100000**. Default value: **1**.
        self.page_number = page_number
        # The number of domain names per page. Default value: **20**.**** Valid values: **1** to **500**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the command.
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
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter

        if self.func_id is not None:
            result['FuncId'] = self.func_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')

        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDcdnIpaUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDcdnIpaUserDomainsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Valid values of N: 1 to 20. You can call the TagDcdnResources operation to set a tag for a domain name.
        self.key = key
        # The tag value. Valid values of N: 1 to 20.
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

