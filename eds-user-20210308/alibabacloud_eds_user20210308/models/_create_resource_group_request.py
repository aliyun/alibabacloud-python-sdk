# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        enable_aliyun_resource_group: bool = None,
        is_resource_group_with_office_site: int = None,
        platform: str = None,
        resource_classification: str = None,
        resource_group_name: str = None,
    ):
        # The business channel.
        self.business_channel = business_channel
        self.enable_aliyun_resource_group = enable_aliyun_resource_group
        # > This parameter is for internal use only.
        self.is_resource_group_with_office_site = is_resource_group_with_office_site
        # Set this parameter to `AliyunConsole` for Wuying Workspace Enterprise Edition.
        self.platform = platform
        self.resource_classification = resource_classification
        # The name of the resource group.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.enable_aliyun_resource_group is not None:
            result['EnableAliyunResourceGroup'] = self.enable_aliyun_resource_group

        if self.is_resource_group_with_office_site is not None:
            result['IsResourceGroupWithOfficeSite'] = self.is_resource_group_with_office_site

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_classification is not None:
            result['ResourceClassification'] = self.resource_classification

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EnableAliyunResourceGroup') is not None:
            self.enable_aliyun_resource_group = m.get('EnableAliyunResourceGroup')

        if m.get('IsResourceGroupWithOfficeSite') is not None:
            self.is_resource_group_with_office_site = m.get('IsResourceGroupWithOfficeSite')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceClassification') is not None:
            self.resource_classification = m.get('ResourceClassification')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

