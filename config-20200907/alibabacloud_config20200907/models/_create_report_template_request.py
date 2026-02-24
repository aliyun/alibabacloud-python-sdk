# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class CreateReportTemplateRequest(DaraModel):
    def __init__(
        self,
        report_file_formats: str = None,
        report_granularity: str = None,
        report_language: str = None,
        report_scope: List[main_models.CreateReportTemplateRequestReportScope] = None,
        report_template_description: str = None,
        report_template_name: str = None,
        subscription_frequency: str = None,
    ):
        # Report format. Currently, only Excel is supported.
        self.report_file_formats = report_file_formats
        # Report aggregation granularity.
        # 
        # Supported for management accounts:
        # 
        # - AllInOne (All accounts within the template scope are aggregated into one report)
        # 
        # - GroupByAggregator (Reports are aggregated by account group, generating a compressed file)
        # 
        # - GroupByAccount (Each account generates a separate report (default), generating a compressed file)
        # 
        # Member accounts only support GroupByAccount.
        self.report_granularity = report_granularity
        # Report language. Supports zh-CN and en-US. If empty, the default is en-US.
        self.report_language = report_language
        # An array of report scopes, used to select the range of rules included in the audit report. The logic between each ReportScope in the array is OR, which means additive logic.
        # 
        # > For example, if the array size is 2, the first ReportScope specifies rule In cr-1, and the second ReportScope specifies rule In cr-2, then the rule scope defined by this report is cr-1 and cr-2.
        self.report_scope = report_scope
        # Report template description
        self.report_template_description = report_template_description
        # Report template name
        # 
        # This parameter is required.
        self.report_template_name = report_template_name
        # Report subscription frequency. If this field is not empty, it is a Quartz-format Cron expression that triggers subscription notifications.
        # 
        # Format: second minute hour day month week. The following are common Cron expression examples:
        # 
        # - Execute at 0:00 every day: 0 0 0 \\* \\* ?
        # 
        # - Execute at 15:30 every Monday: 0 30 15 ? \\* MON
        # 
        # - Execute at 2:00 on the 1st of every month: 0 0 2 1 \\* ?
        # 
        # Where:
        # 
        # - "\\*" indicates any value
        # 
        # - "?" is used for day and week fields, indicating no specific value
        # 
        # - "MON" indicates Monday
        # 
        # > The trigger time is UTC+8. Adjust the Cron expression settings based on your time zone.
        # 
        # > We try to trigger notifications according to the Cron expression time, but there might be delays due to report generation status. A Cron expression limits the same template to trigger notifications at most once per day.
        # 
        # > 1 represents Sunday; 2 represents Monday; 3 represents Tuesday; 4 represents Wednesday; 5 represents Thursday; 6 represents Friday; 7 represents Saturday
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
                temp_model = main_models.CreateReportTemplateRequestReportScope()
                self.report_scope.append(temp_model.from_map(k1))

        if m.get('ReportTemplateDescription') is not None:
            self.report_template_description = m.get('ReportTemplateDescription')

        if m.get('ReportTemplateName') is not None:
            self.report_template_name = m.get('ReportTemplateName')

        if m.get('SubscriptionFrequency') is not None:
            self.subscription_frequency = m.get('SubscriptionFrequency')

        return self

class CreateReportTemplateRequestReportScope(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: str = None,
    ):
        # The key for the report scope. Currently supports:
        # 
        # - AggregatorId
        # 
        # - CompliancePackId
        # 
        # - RuleId
        self.key = key
        # Matching logic. Currently, only In is supported.
        self.match_type = match_type
        # The value for the report scope. Multiple items of the same type, such as multiple Rule IDs, can be separated by English commas (,).
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

