# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateBootAndAntiUninstallPolicyRequest(DaraModel):
    def __init__(
        self,
        allow_report: bool = None,
        block_content: main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContent = None,
        is_anti_uninstall: bool = None,
        is_boot: bool = None,
        user_group_ids: List[str] = None,
        whitelist_users: List[str] = None,
    ):
        self.allow_report = allow_report
        self.block_content = block_content
        self.is_anti_uninstall = is_anti_uninstall
        self.is_boot = is_boot
        self.user_group_ids = user_group_ids
        self.whitelist_users = whitelist_users

    def validate(self):
        if self.block_content:
            self.block_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_report is not None:
            result['AllowReport'] = self.allow_report

        if self.block_content is not None:
            result['BlockContent'] = self.block_content.to_map()

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
            temp_model = main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContent()
            self.block_content = temp_model.from_map(m.get('BlockContent'))

        if m.get('IsAntiUninstall') is not None:
            self.is_anti_uninstall = m.get('IsAntiUninstall')

        if m.get('IsBoot') is not None:
            self.is_boot = m.get('IsBoot')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('WhitelistUsers') is not None:
            self.whitelist_users = m.get('WhitelistUsers')

        return self

class UpdateBootAndAntiUninstallPolicyRequestBlockContent(DaraModel):
    def __init__(
        self,
        block_text_en: main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextEn = None,
        block_text_zh: main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextZh = None,
    ):
        self.block_text_en = block_text_en
        self.block_text_zh = block_text_zh

    def validate(self):
        if self.block_text_en:
            self.block_text_en.validate()
        if self.block_text_zh:
            self.block_text_zh.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_text_en is not None:
            result['BlockTextEn'] = self.block_text_en.to_map()

        if self.block_text_zh is not None:
            result['BlockTextZh'] = self.block_text_zh.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockTextEn') is not None:
            temp_model = main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextEn()
            self.block_text_en = temp_model.from_map(m.get('BlockTextEn'))

        if m.get('BlockTextZh') is not None:
            temp_model = main_models.UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextZh()
            self.block_text_zh = temp_model.from_map(m.get('BlockTextZh'))

        return self

class UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextZh(DaraModel):
    def __init__(
        self,
        content: str = None,
        main_button_text: str = None,
        minor_button_text: str = None,
        title: str = None,
    ):
        self.content = content
        self.main_button_text = main_button_text
        self.minor_button_text = minor_button_text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.main_button_text is not None:
            result['MainButtonText'] = self.main_button_text

        if self.minor_button_text is not None:
            result['MinorButtonText'] = self.minor_button_text

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('MainButtonText') is not None:
            self.main_button_text = m.get('MainButtonText')

        if m.get('MinorButtonText') is not None:
            self.minor_button_text = m.get('MinorButtonText')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class UpdateBootAndAntiUninstallPolicyRequestBlockContentBlockTextEn(DaraModel):
    def __init__(
        self,
        content: str = None,
        main_button_text: str = None,
        minor_button_text: str = None,
        title: str = None,
    ):
        self.content = content
        self.main_button_text = main_button_text
        self.minor_button_text = minor_button_text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.main_button_text is not None:
            result['MainButtonText'] = self.main_button_text

        if self.minor_button_text is not None:
            result['MinorButtonText'] = self.minor_button_text

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('MainButtonText') is not None:
            self.main_button_text = m.get('MainButtonText')

        if m.get('MinorButtonText') is not None:
            self.minor_button_text = m.get('MinorButtonText')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

