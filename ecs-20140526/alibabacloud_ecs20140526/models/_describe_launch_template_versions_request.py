# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLaunchTemplateVersionsRequest(DaraModel):
    def __init__(
        self,
        default_version: bool = None,
        detail_flag: bool = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        launch_template_version: List[int] = None,
        max_version: int = None,
        min_version: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to query the default version.
        self.default_version = default_version
        # Specifies whether to query the configurations of the launch template. Valid values:
        # 
        # *   true: queries the basic information and other details of the launch template. The details include the image ID and system disk size.
        # *   false: queries only the basic information of the launch template. The basic information includes the template ID, template name, and default version.
        # 
        # Default value: true.
        self.detail_flag = detail_flag
        # The ID of the launch template.
        # 
        # You must set `LaunchTemplateId` or `LaunchTemplateName` to specify a launch template.
        self.launch_template_id = launch_template_id
        # The name of the launch template.
        # 
        # You must set `LaunchTemplateId` or `LaunchTemplateName` to specify a launch template.
        self.launch_template_name = launch_template_name
        # The versions of the launch template.
        self.launch_template_version = launch_template_version
        # The maximum version number in the version range to query. This parameter is used together with `MinVersion` to specify a version range to query.
        self.max_version = max_version
        # The minimum version number in the version range to query. This parameter is used together with `MaxVersion` to specify a version range to query.
        self.min_version = min_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the launch template.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.detail_flag is not None:
            result['DetailFlag'] = self.detail_flag

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.min_version is not None:
            result['MinVersion'] = self.min_version

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('DetailFlag') is not None:
            self.detail_flag = m.get('DetailFlag')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('MinVersion') is not None:
            self.min_version = m.get('MinVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

