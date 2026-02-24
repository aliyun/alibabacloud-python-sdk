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
        # The format of the report.
        self.report_file_formats = report_file_formats
        # The aggregation granularity of the report.
        # 
        # For a management account, the following values are supported:
        # 
        # - AllInOne: A single report is generated for all accounts within the template scope.
        # 
        # - GroupByAggregator: Reports are aggregated by account group. A compressed file is generated.
        # 
        # - GroupByAccount: A separate report is generated for each account. This is the default value. A compressed file is generated.
        # 
        # For a member account, only GroupByAccount is supported.
        self.report_granularity = report_granularity
        # The language of the report. Valid values: zh-CN and en-US. If you leave this parameter empty, the default value en-US is used.
        self.report_language = report_language
        # An array that specifies the report scope. It is used to select the range of rules to include in the audit report. The logical relationship between multiple ReportScope objects in the array is OR. This means the scopes are added together.
        # 
        # > For example, if the array contains two ReportScope objects, where the first specifies the rule In cr-1 and the second specifies the rule In cr-2, the report scope includes both cr-1 and cr-2.
        self.report_scope_shrink = report_scope_shrink
        # The description of the report template.
        self.report_template_description = report_template_description
        # The ID of the report template.
        # 
        # This parameter is required.
        self.report_template_id = report_template_id
        # The name of the report template.
        self.report_template_name = report_template_name
        # The frequency for subscribing to the report. If this parameter is not empty, it specifies a cron expression in the Quartz format that triggers a subscription notification.
        # 
        # The format is: Second Minute Hour Day Month Week. The following list provides common examples of cron expressions:
        # 
        # - To run at 00:00 every day: 0 0 0 \\* \\* ?
        # 
        # - To run at 15:30 every Monday: 0 30 15 ? \\* MON
        # 
        # - To run at 02:00 on the first day of every month: 0 0 2 1 \\* ?
        # 
        # Where:
        # 
        # - "\\*" indicates any value.
        # 
        # - ? is used in the Day and Week fields and indicates that no specific value is specified.
        # 
        # - MON indicates Monday.
        # 
        # > The trigger time is in UTC+8. You can convert the cron expression based on your time zone.
        # 
        # > The system attempts to trigger the notification at the time specified by the cron expression. However, a delay may occur due to the report generation status. The cron expression limits the notification for the same template to a maximum of once per day.
        # 
        # > In addition to using MON for Monday, you can also use numbers. In the Quartz framework, 1 represents Sunday, 2 represents Monday, 3 represents Tuesday, 4 represents Wednesday, 5 represents Thursday, 6 represents Friday, and 7 represents Saturday.
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

