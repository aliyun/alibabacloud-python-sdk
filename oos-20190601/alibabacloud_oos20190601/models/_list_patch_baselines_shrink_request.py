# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPatchBaselinesShrinkRequest(DaraModel):
    def __init__(
        self,
        approved_patches_shrink: str = None,
        approved_patches_enable_non_security: bool = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        operation_system: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The approved patches.
        self.approved_patches_shrink = approved_patches_shrink
        # Specifies whether the approved patch involves updates other than security-related updates.
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The number of entries returned per page.
        self.max_results = max_results
        # The name of the patch baseline.
        self.name = name
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        self.operation_system = operation_system
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.share_type = share_type
        # The patch source configurations.
        self.sources_shrink = sources_shrink
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink

        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')

        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

