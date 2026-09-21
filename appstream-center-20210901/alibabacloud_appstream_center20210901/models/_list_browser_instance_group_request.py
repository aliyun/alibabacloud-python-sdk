# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListBrowserInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_set_id: str = None,
        biz_region_id: str = None,
        browser_instance_group_id: str = None,
        browser_instance_group_name: str = None,
        cloud_browser_name: str = None,
        excluded_user_group_ids: List[str] = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: List[str] = None,
        tag: List[main_models.ListBrowserInstanceGroupRequestTag] = None,
        tier: str = None,
        user_group_ids: List[str] = None,
    ):
        # The browser group set ID for exact match queries of active members in the set.
        self.app_instance_group_set_id = app_instance_group_set_id
        # Filters browser groups by business region.
        self.biz_region_id = biz_region_id
        # The cloud browser group ID for exact match queries.
        self.browser_instance_group_id = browser_instance_group_id
        # The browser group name. Fuzzy match is supported.
        self.browser_instance_group_name = browser_instance_group_name
        # Performs a contains match by browser group name or ID.
        self.cloud_browser_name = cloud_browser_name
        # Excludes browser groups that are authorized to the specified user groups.
        self.excluded_user_group_ids = excluded_user_group_ids
        # Filters browser groups by office network ID.
        self.office_site_id = office_site_id
        # The page number, starting from page 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # Filters by browser group status.
        # 
        # **Limit:** Only one status value can be specified at a time.
        self.status = status
        # The tag filter parameters. This parameter is not supported in customer-facing scenarios. Do not specify this parameter.
        self.tag = tag
        # Filters by version of the browser.
        # 
        # - `Basic`: Basic Edition.
        # - `Pro`: Premium Edition.
        # 
        # Use `Pro` to query MAU browser groups.
        self.tier = tier
        # Filters by authorized user group IDs.
        self.user_group_ids = user_group_ids

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
        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        if self.browser_instance_group_name is not None:
            result['BrowserInstanceGroupName'] = self.browser_instance_group_name

        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name

        if self.excluded_user_group_ids is not None:
            result['ExcludedUserGroupIds'] = self.excluded_user_group_ids

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tier is not None:
            result['Tier'] = self.tier

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        if m.get('BrowserInstanceGroupName') is not None:
            self.browser_instance_group_name = m.get('BrowserInstanceGroupName')

        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')

        if m.get('ExcludedUserGroupIds') is not None:
            self.excluded_user_group_ids = m.get('ExcludedUserGroupIds')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListBrowserInstanceGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Tier') is not None:
            self.tier = m.get('Tier')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

class ListBrowserInstanceGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Do not specify this parameter in customer-facing scenarios.
        self.key = key
        # The tag value. Do not specify this parameter in customer-facing scenarios.
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

