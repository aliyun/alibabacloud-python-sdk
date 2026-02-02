# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateReportTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        report_file_formats: str = None,
        report_granularity: str = None,
        report_language: str = None,
        report_scope_shrink: str = None,
        report_template_description: str = None,
        report_template_id: str = None,
        report_template_name: str = None,
        subscription_frequency: str = None,
    ):
        self.report_file_formats = report_file_formats
        self.report_granularity = report_granularity
        self.report_language = report_language
        self.report_scope_shrink = report_scope_shrink
        self.report_template_description = report_template_description
        # This parameter is required.
        self.report_template_id = report_template_id
        self.report_template_name = report_template_name
        self.subscription_frequency = subscription_frequency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_file_formats is not None:
            result['ReportFileFormats'] = self.report_file_formats

        if self.report_granularity is not None:
            result['ReportGranularity'] = self.report_granularity

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.report_scope_shrink is not None:
            result['ReportScope'] = self.report_scope_shrink

        if self.report_template_description is not None:
            result['ReportTemplateDescription'] = self.report_template_description

        if self.report_template_id is not None:
            result['ReportTemplateId'] = self.report_template_id

        if self.report_template_name is not None:
            result['ReportTemplateName'] = self.report_template_name

        if self.subscription_frequency is not None:
            result['SubscriptionFrequency'] = self.subscription_frequency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportFileFormats') is not None:
            self.report_file_formats = m.get('ReportFileFormats')

        if m.get('ReportGranularity') is not None:
            self.report_granularity = m.get('ReportGranularity')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ReportScope') is not None:
            self.report_scope_shrink = m.get('ReportScope')

        if m.get('ReportTemplateDescription') is not None:
            self.report_template_description = m.get('ReportTemplateDescription')

        if m.get('ReportTemplateId') is not None:
            self.report_template_id = m.get('ReportTemplateId')

        if m.get('ReportTemplateName') is not None:
            self.report_template_name = m.get('ReportTemplateName')

        if m.get('SubscriptionFrequency') is not None:
            self.subscription_frequency = m.get('SubscriptionFrequency')

        return self

