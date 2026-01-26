# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGrafanaWorkspaceShrinkRequest(DaraModel):
    def __init__(
        self,
        account_number: str = None,
        aliyun_lang: str = None,
        auto_renew: str = None,
        custom_account_number: str = None,
        description: str = None,
        duration: str = None,
        grafana_version: str = None,
        grafana_workspace_edition: str = None,
        grafana_workspace_name: str = None,
        password: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        self.account_number = account_number
        # The language. Default value: zh. Valid values:
        # 
        # *   zh
        # *   en
        self.aliyun_lang = aliyun_lang
        self.auto_renew = auto_renew
        self.custom_account_number = custom_account_number
        # The description of the workspace
        self.description = description
        self.duration = duration
        # This parameter is required.
        self.grafana_version = grafana_version
        # The edition.
        # 
        # **Valid values:**
        # 
        # *   standard: `Beta Edition or Standard Edition`
        # *   personal_edition: Developer Edition
        # *   experts_edition: Pro Edition
        # *   advanced_edition: Advanced Edition
        # 
        # This parameter is required.
        self.grafana_workspace_edition = grafana_workspace_edition
        # The name of the Grafana workspace.
        # 
        # This parameter is required.
        self.grafana_workspace_name = grafana_workspace_name
        # The password of the workspace. The password must be 8 to 30 characters in length. It must include at least three of the following characters types: uppercase letter, lowercase letter, digit, and special character. Special characters include () \\" ~ ! @ # $ % ^ & \\* - _ + =.
        self.password = password
        # 包年包月的计费周期，取值： Month（默认值）：按月购买。                                 Year：按年购买。
        self.pricing_cycle = pricing_cycle
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_number is not None:
            result['AccountNumber'] = self.account_number

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.custom_account_number is not None:
            result['CustomAccountNumber'] = self.custom_account_number

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.grafana_version is not None:
            result['GrafanaVersion'] = self.grafana_version

        if self.grafana_workspace_edition is not None:
            result['GrafanaWorkspaceEdition'] = self.grafana_workspace_edition

        if self.grafana_workspace_name is not None:
            result['GrafanaWorkspaceName'] = self.grafana_workspace_name

        if self.password is not None:
            result['Password'] = self.password

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNumber') is not None:
            self.account_number = m.get('AccountNumber')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('CustomAccountNumber') is not None:
            self.custom_account_number = m.get('CustomAccountNumber')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GrafanaVersion') is not None:
            self.grafana_version = m.get('GrafanaVersion')

        if m.get('GrafanaWorkspaceEdition') is not None:
            self.grafana_workspace_edition = m.get('GrafanaWorkspaceEdition')

        if m.get('GrafanaWorkspaceName') is not None:
            self.grafana_workspace_name = m.get('GrafanaWorkspaceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

