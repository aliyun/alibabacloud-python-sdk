# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateBootAndAntiUninstallPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        allow_report: bool = None,
        block_content_shrink: str = None,
        is_anti_uninstall: bool = None,
        is_boot: bool = None,
        user_group_ids: List[str] = None,
        whitelist_users: List[str] = None,
    ):
        self.allow_report = allow_report
        self.block_content_shrink = block_content_shrink
        self.is_anti_uninstall = is_anti_uninstall
        self.is_boot = is_boot
        self.user_group_ids = user_group_ids
        self.whitelist_users = whitelist_users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_report is not None:
            result['AllowReport'] = self.allow_report

        if self.block_content_shrink is not None:
            result['BlockContent'] = self.block_content_shrink

        if self.is_anti_uninstall is not None:
            result['IsAntiUninstall'] = self.is_anti_uninstall

        if self.is_boot is not None:
            result['IsBoot'] = self.is_boot

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist_users is not None:
            result['WhitelistUsers'] = self.whitelist_users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowReport') is not None:
            self.allow_report = m.get('AllowReport')

        if m.get('BlockContent') is not None:
            self.block_content_shrink = m.get('BlockContent')

        if m.get('IsAntiUninstall') is not None:
            self.is_anti_uninstall = m.get('IsAntiUninstall')

        if m.get('IsBoot') is not None:
            self.is_boot = m.get('IsBoot')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('WhitelistUsers') is not None:
            self.whitelist_users = m.get('WhitelistUsers')

        return self

