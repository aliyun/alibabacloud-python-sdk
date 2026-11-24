# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeVulDesktopsRequest(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        cve_id: str = None,
        desktop_id_list: List[str] = None,
        desktop_status: str = None,
        include_fix_result: bool = None,
        include_patch_task: bool = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        only_current_month_fix_attempted: bool = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        search_region_id: str = None,
        status_list: List[str] = None,
        vul_level: str = None,
    ):
        # The connection status of the cloud desktop.
        self.connection_status = connection_status
        # The vulnerability ID.
        self.cve_id = cve_id
        # The list of cloud desktop IDs.
        self.desktop_id_list = desktop_id_list
        # The running status of the cloud desktop.
        self.desktop_status = desktop_status
        # Specifies whether to include the patch update results.
        self.include_fix_result = include_fix_result
        # Specifies whether to include cloud desktops that have scheduled patch tasks.
        self.include_patch_task = include_patch_task
        # The language of the response.
        self.language = language
        # The number of entries per page for a paging query.
        # Maximum value: 100.
        # Default value: 10.
        self.max_results = max_results
        # The token for the next page.
        self.next_token = next_token
        # Specifies whether to include only cloud desktops for which fix tasks have been executed in the current month.
        self.only_current_month_fix_attempted = only_current_month_fix_attempted
        # The page number of the current page for a paging query.
        self.page_number = page_number
        # The page size for a paging query.
        self.page_size = page_size
        # The patch ID.
        self.patch_id = patch_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions supported by WUYING Workspace.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The search region ID. This parameter is used to filter cloud desktop information for a specified region.
        self.search_region_id = search_region_id
        # The list of vulnerability status details.
        self.status_list = status_list
        # The security level of the intrusion prevention event. Valid values:
        # - **low**: low-risk.
        # - **medium**: medium-risk.
        # - **critical**: high-risk.
        # 
        # > If you do not specify this parameter, vulnerabilities of all security levels are queried.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.desktop_id_list is not None:
            result['DesktopIdList'] = self.desktop_id_list

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.include_fix_result is not None:
            result['IncludeFixResult'] = self.include_fix_result

        if self.include_patch_task is not None:
            result['IncludePatchTask'] = self.include_patch_task

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.only_current_month_fix_attempted is not None:
            result['OnlyCurrentMonthFixAttempted'] = self.only_current_month_fix_attempted

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('DesktopIdList') is not None:
            self.desktop_id_list = m.get('DesktopIdList')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('IncludeFixResult') is not None:
            self.include_fix_result = m.get('IncludeFixResult')

        if m.get('IncludePatchTask') is not None:
            self.include_patch_task = m.get('IncludePatchTask')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OnlyCurrentMonthFixAttempted') is not None:
            self.only_current_month_fix_attempted = m.get('OnlyCurrentMonthFixAttempted')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

