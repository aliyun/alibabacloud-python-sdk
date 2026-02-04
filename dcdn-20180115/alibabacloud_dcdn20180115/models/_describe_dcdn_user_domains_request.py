# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserDomainsRequest(DaraModel):
    def __init__(
        self,
        change_end_time: str = None,
        change_start_time: str = None,
        check_domain_show: bool = None,
        coverage: str = None,
        domain_name: str = None,
        domain_search_type: str = None,
        domain_status: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        tag: List[main_models.DescribeDcdnUserDomainsRequestTag] = None,
        web_site_type: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # 
        # > The end time must be later than the start time.
        self.change_end_time = change_end_time
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        self.change_start_time = change_start_time
        # Specifies whether to display domain names that are under review, failed the review, or failed to be configured. Valid values:
        # 
        # *   true: displays domain names.
        # *   false: does not display detailed information.
        self.check_domain_show = check_domain_show
        # The acceleration region. By default, all acceleration regions are queried.
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: outside the Chinese mainland
        # *   **global**: global
        self.coverage = coverage
        # The accelerated domain names. If you do not set this parameter, configurations of all domain names that match the conditions are returned.
        self.domain_name = domain_name
        # The search method. Default value: full_match. Valid values:
        # 
        # *   **fuzzy_match**: fuzzy match
        # *   **pre_match**: prefix match
        # *   **suf_match**: suffix match
        # *   **full_match** (default): exact match
        # 
        # > If you specify the domain names to query but do not set the DomainSearchType parameter, the exact match mode is used.
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
        self.owner_id = owner_id
        # The number of returned pages. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**. Valid values: **1** to **500**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The list of tags.
        self.tag = tag
        # The business type of the domain. Separate multiple values with commas (,). Default value: **dynamic**. To query common domains, keep the default value. To query domains of the computing business type, enter **computing_routine** or **computing_image**.
        self.web_site_type = web_site_type

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
        if self.change_end_time is not None:
            result['ChangeEndTime'] = self.change_end_time

        if self.change_start_time is not None:
            result['ChangeStartTime'] = self.change_start_time

        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show

        if self.coverage is not None:
            result['Coverage'] = self.coverage

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.web_site_type is not None:
            result['WebSiteType'] = self.web_site_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeEndTime') is not None:
            self.change_end_time = m.get('ChangeEndTime')

        if m.get('ChangeStartTime') is not None:
            self.change_start_time = m.get('ChangeStartTime')

        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDcdnUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('WebSiteType') is not None:
            self.web_site_type = m.get('WebSiteType')

        return self

class DescribeDcdnUserDomainsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Valid values of N: **1** to **20**. You can call the TagDcdnResources operation to set a tag for a domain name.
        self.key = key
        # The tag value. Valid values of N: **1** to **20**.
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

