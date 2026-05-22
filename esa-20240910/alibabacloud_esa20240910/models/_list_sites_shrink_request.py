# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSitesShrinkRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        coverage: str = None,
        only_enterprise: bool = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        plan_subscribe_type: str = None,
        resource_group_id: str = None,
        site_name: str = None,
        site_search_type: str = None,
        status: str = None,
        tag_filter_shrink: str = None,
    ):
        # The DNS setup. Valid values:
        # 
        # *   **NS**
        # *   **CNAME**
        self.access_type = access_type
        # The service location. Valid values:
        # 
        # *   **domestic**: the Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        self.coverage = coverage
        # Specifies whether to query only websites on Enterprise plans. Valid values: **true and false**.
        self.only_enterprise = only_enterprise
        # Sorting field. By default, it sorts by creation time, supporting the following options:
        # - gmtCreate: website creation time
        # - visitTime: website visit time
        self.order_by = order_by
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **500**.
        self.page_size = page_size
        # The plan type. Valid values:
        # 
        # *   **basicplan**: Entrance
        # *   **standardplan**: Pro
        # *   **advancedplan**: Premium
        # *   **enterpriseplan**: Enterprise
        self.plan_subscribe_type = plan_subscribe_type
        # The ID of the resource group. This parameter specifies a filter condition for the query.
        self.resource_group_id = resource_group_id
        # The website name. This parameter specifies a filter condition for the query.
        self.site_name = site_name
        # The match mode to search for the website name. Default value: exact. Valid values:
        # 
        # *   **prefix**: match by prefix.
        # *   **suffix**: match by suffix.
        # *   **exact**: exact match.
        # *   **fuzzy**: fuzzy match.
        self.site_search_type = site_search_type
        # The website status. This parameter specifies a filter condition for the query.
        self.status = status
        # The tag filtering rule.
        self.tag_filter_shrink = tag_filter_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.only_enterprise is not None:
            result['OnlyEnterprise'] = self.only_enterprise

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_subscribe_type is not None:
            result['PlanSubscribeType'] = self.plan_subscribe_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.site_search_type is not None:
            result['SiteSearchType'] = self.site_search_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_filter_shrink is not None:
            result['TagFilter'] = self.tag_filter_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('OnlyEnterprise') is not None:
            self.only_enterprise = m.get('OnlyEnterprise')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanSubscribeType') is not None:
            self.plan_subscribe_type = m.get('PlanSubscribeType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SiteSearchType') is not None:
            self.site_search_type = m.get('SiteSearchType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagFilter') is not None:
            self.tag_filter_shrink = m.get('TagFilter')

        return self

