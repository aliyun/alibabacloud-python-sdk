# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetBootAndAntiUninstallPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategy: main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategy = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The auto-start and anti-uninstall policy.
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategy') is not None:
            temp_model = main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class GetBootAndAntiUninstallPolicyResponseBodyStrategy(DaraModel):
    def __init__(
        self,
        allow_report: bool = None,
        block_content: main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContent = None,
        create_time: str = None,
        is_anti_uninstall: bool = None,
        is_boot: bool = None,
        policy_id: str = None,
        report_process_id: str = None,
        update_time: str = None,
        user_group_ids: List[str] = None,
        whitelist_users: List[str] = None,
    ):
        # Indicates whether end users are allowed to submit approval requests.
        self.allow_report = allow_report
        # The content displayed in the client interception pop-up window.
        self.block_content = block_content
        # The time when the policy was created.
        self.create_time = create_time
        # Indicates whether the anti-uninstall feature is enabled.
        self.is_anti_uninstall = is_anti_uninstall
        # Indicates whether the auto-start feature is enabled.
        self.is_boot = is_boot
        # The policy ID.
        self.policy_id = policy_id
        # The ID of the approval process associated with the policy.
        self.report_process_id = report_process_id
        # The time when the policy was updated.
        self.update_time = update_time
        # The list of user group IDs to which the policy applies.
        self.user_group_ids = user_group_ids
        # The list of whitelist users.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.is_anti_uninstall is not None:
            result['IsAntiUninstall'] = self.is_anti_uninstall

        if self.is_boot is not None:
            result['IsBoot'] = self.is_boot

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.report_process_id is not None:
            result['ReportProcessId'] = self.report_process_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

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
            temp_model = main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContent()
            self.block_content = temp_model.from_map(m.get('BlockContent'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IsAntiUninstall') is not None:
            self.is_anti_uninstall = m.get('IsAntiUninstall')

        if m.get('IsBoot') is not None:
            self.is_boot = m.get('IsBoot')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ReportProcessId') is not None:
            self.report_process_id = m.get('ReportProcessId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('WhitelistUsers') is not None:
            self.whitelist_users = m.get('WhitelistUsers')

        return self

class GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContent(DaraModel):
    def __init__(
        self,
        block_text_en: main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextEn = None,
        block_text_zh: main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextZh = None,
    ):
        # The English content.
        self.block_text_en = block_text_en
        # The Chinese content.
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
            temp_model = main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextEn()
            self.block_text_en = temp_model.from_map(m.get('BlockTextEn'))

        if m.get('BlockTextZh') is not None:
            temp_model = main_models.GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextZh()
            self.block_text_zh = temp_model.from_map(m.get('BlockTextZh'))

        return self

class GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextZh(DaraModel):
    def __init__(
        self,
        content: str = None,
        main_button_text: str = None,
        minor_button_text: str = None,
        title: str = None,
    ):
        # The pop-up window content.
        self.content = content
        # The text of the primary button in the pop-up window.
        self.main_button_text = main_button_text
        # The text of the secondary button in the pop-up window.
        self.minor_button_text = minor_button_text
        # The pop-up window title.
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

class GetBootAndAntiUninstallPolicyResponseBodyStrategyBlockContentBlockTextEn(DaraModel):
    def __init__(
        self,
        content: str = None,
        main_button_text: str = None,
        minor_button_text: str = None,
        title: str = None,
    ):
        # The pop-up window content.
        self.content = content
        # The text of the primary button in the pop-up window.
        self.main_button_text = main_button_text
        # The text of the secondary button in the pop-up window.
        self.minor_button_text = minor_button_text
        # The pop-up window title.
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

