# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetReportTemplateResponseBody(DaraModel):
    def __init__(
        self,
        report_template: main_models.GetReportTemplateResponseBodyReportTemplate = None,
        request_id: str = None,
    ):
        # Report template.
        self.report_template = report_template
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.report_template:
            self.report_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_template is not None:
            result['ReportTemplate'] = self.report_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportTemplate') is not None:
            temp_model = main_models.GetReportTemplateResponseBodyReportTemplate()
            self.report_template = temp_model.from_map(m.get('ReportTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetReportTemplateResponseBodyReportTemplate(DaraModel):
    def __init__(
        self,
        report_file_formats: str = None,
        report_granularity: str = None,
        report_language: str = None,
        report_scope: List[main_models.GetReportTemplateResponseBodyReportTemplateReportScope] = None,
        report_template_description: str = None,
        report_template_id: str = None,
        report_template_name: str = None,
        subscription_frequency: str = None,
    ):
        # Report file format.
        self.report_file_formats = report_file_formats
        # Aggregation granularity of the report.
        self.report_granularity = report_granularity
        # Report language. Valid values: zh-CN and en-US. Default is en-US if empty.
        self.report_language = report_language
        # Array of report scopes. Each scope defines a set of rules included in the audit report. Scopes use OR logic. That is, rules from all scopes are combined.
        # 
        # > If the array has two items, and the first specifies RuleId cr-1 while the second specifies RuleId cr-2, then the report covers both cr-1 and cr-2.
        self.report_scope = report_scope
        # Description of the report template.
        self.report_template_description = report_template_description
        # ID of the report template.
        self.report_template_id = report_template_id
        # Name of the report template.
        self.report_template_name = report_template_name
        # Subscription frequency for the report. If this field is not empty, it contains a Quartz-formatted cron expression that triggers notifications.
        # 
        # The format is: seconds minutes hours day-of-month month day-of-week. Common examples include the following:
        # 
        # - Run daily at 00:00: 0 0 0 \\* \\* ?
        # 
        # - Run every Monday at 15:30: 0 30 15 ? \\* MON
        # 
        # - Run on the first day of each month at 02:00: 0 0 2 1 \\* ?
        # 
        # Where:
        # 
        # - "\\*" means any value.
        # 
        # - "?" means no specific value for the day-of-month or day-of-week field.
        # 
        # - MON means Monday.
        # 
        # > Trigger times are in UTC+8. Adjust your cron expression based on your time zone.
        # 
        # > The system tries to trigger notifications as close as possible to the scheduled time. Delays may occur due to report generation status. A single template can trigger at most one notification per day.
        # 
        # > In Quartz, days of the week are numbered: 1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Saturday.
        self.subscription_frequency = subscription_frequency

    def validate(self):
        if self.report_scope:
            for v1 in self.report_scope:
                 if v1:
                    v1.validate()

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

        result['ReportScope'] = []
        if self.report_scope is not None:
            for k1 in self.report_scope:
                result['ReportScope'].append(k1.to_map() if k1 else None)

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

        self.report_scope = []
        if m.get('ReportScope') is not None:
            for k1 in m.get('ReportScope'):
                temp_model = main_models.GetReportTemplateResponseBodyReportTemplateReportScope()
                self.report_scope.append(temp_model.from_map(k1))

        if m.get('ReportTemplateDescription') is not None:
            self.report_template_description = m.get('ReportTemplateDescription')

        if m.get('ReportTemplateId') is not None:
            self.report_template_id = m.get('ReportTemplateId')

        if m.get('ReportTemplateName') is not None:
            self.report_template_name = m.get('ReportTemplateName')

        if m.get('SubscriptionFrequency') is not None:
            self.subscription_frequency = m.get('SubscriptionFrequency')

        return self

class GetReportTemplateResponseBodyReportTemplateReportScope(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: str = None,
    ):
        # Key for the report scope. Supported keys:
        # 
        # - AggregatorId
        # 
        # - CompliancePackId
        # 
        # - RuleId
        self.key = key
        # Matching logic. Only In is supported.
        self.match_type = match_type
        # Value for the report scope. For multiple values of the same type, such as multiple rule IDs, separate them with commas.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

