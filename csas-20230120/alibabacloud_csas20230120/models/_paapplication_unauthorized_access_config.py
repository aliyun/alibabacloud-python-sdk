# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class PAApplicationUnauthorizedAccessConfig(DaraModel):
    def __init__(
        self,
        allow_report: bool = None,
        block_content: main_models.PAApplicationUnauthorizedAccessConfigBlockContent = None,
        enabled: bool = None,
        report_process_id: str = None,
    ):
        # Specifies whether end users are allowed to submit approval requests.
        self.allow_report = allow_report
        # The content displayed in the client interception pop-up window.
        self.block_content = block_content
        # Specifies whether the feature is enabled. Valid values:
        # - **true**: Enabled. Users are redirected to an interception page when they access an unauthorized application.
        # - **false**: Disabled. An error message is returned by default when users access an unauthorized application.
        self.enabled = enabled
        # The ID of the approval flow associated with the policy.
        self.report_process_id = report_process_id

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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.report_process_id is not None:
            result['ReportProcessId'] = self.report_process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowReport') is not None:
            self.allow_report = m.get('AllowReport')

        if m.get('BlockContent') is not None:
            temp_model = main_models.PAApplicationUnauthorizedAccessConfigBlockContent()
            self.block_content = temp_model.from_map(m.get('BlockContent'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ReportProcessId') is not None:
            self.report_process_id = m.get('ReportProcessId')

        return self

class PAApplicationUnauthorizedAccessConfigBlockContent(DaraModel):
    def __init__(
        self,
        block_text_en: main_models.PAApplicationUnauthorizedAccessConfigBlockContentBlockTextEn = None,
        block_text_zh: main_models.PAApplicationUnauthorizedAccessConfigBlockContentBlockTextZh = None,
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
            temp_model = main_models.PAApplicationUnauthorizedAccessConfigBlockContentBlockTextEn()
            self.block_text_en = temp_model.from_map(m.get('BlockTextEn'))

        if m.get('BlockTextZh') is not None:
            temp_model = main_models.PAApplicationUnauthorizedAccessConfigBlockContentBlockTextZh()
            self.block_text_zh = temp_model.from_map(m.get('BlockTextZh'))

        return self

class PAApplicationUnauthorizedAccessConfigBlockContentBlockTextZh(DaraModel):
    def __init__(
        self,
        browser_alert_content: str = None,
        browser_alert_style: str = None,
        browser_alert_title: str = None,
        report_button_text: str = None,
    ):
        # The prompt content of the block page.
        self.browser_alert_content = browser_alert_content
        # The background pattern of the block page.
        self.browser_alert_style = browser_alert_style
        # The title of the block page.
        self.browser_alert_title = browser_alert_title
        # The text of the report approval button.
        self.report_button_text = report_button_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_alert_content is not None:
            result['BrowserAlertContent'] = self.browser_alert_content

        if self.browser_alert_style is not None:
            result['BrowserAlertStyle'] = self.browser_alert_style

        if self.browser_alert_title is not None:
            result['BrowserAlertTitle'] = self.browser_alert_title

        if self.report_button_text is not None:
            result['ReportButtonText'] = self.report_button_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserAlertContent') is not None:
            self.browser_alert_content = m.get('BrowserAlertContent')

        if m.get('BrowserAlertStyle') is not None:
            self.browser_alert_style = m.get('BrowserAlertStyle')

        if m.get('BrowserAlertTitle') is not None:
            self.browser_alert_title = m.get('BrowserAlertTitle')

        if m.get('ReportButtonText') is not None:
            self.report_button_text = m.get('ReportButtonText')

        return self

class PAApplicationUnauthorizedAccessConfigBlockContentBlockTextEn(DaraModel):
    def __init__(
        self,
        browser_alert_content: str = None,
        browser_alert_style: str = None,
        browser_alert_title: str = None,
        report_button_text: str = None,
    ):
        # The prompt content of the English block page.
        self.browser_alert_content = browser_alert_content
        # The background pattern of the English block page.
        self.browser_alert_style = browser_alert_style
        # The title of the English block page.
        self.browser_alert_title = browser_alert_title
        # The text of the English report approval button.
        self.report_button_text = report_button_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_alert_content is not None:
            result['BrowserAlertContent'] = self.browser_alert_content

        if self.browser_alert_style is not None:
            result['BrowserAlertStyle'] = self.browser_alert_style

        if self.browser_alert_title is not None:
            result['BrowserAlertTitle'] = self.browser_alert_title

        if self.report_button_text is not None:
            result['ReportButtonText'] = self.report_button_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserAlertContent') is not None:
            self.browser_alert_content = m.get('BrowserAlertContent')

        if m.get('BrowserAlertStyle') is not None:
            self.browser_alert_style = m.get('BrowserAlertStyle')

        if m.get('BrowserAlertTitle') is not None:
            self.browser_alert_title = m.get('BrowserAlertTitle')

        if m.get('ReportButtonText') is not None:
            self.report_button_text = m.get('ReportButtonText')

        return self

