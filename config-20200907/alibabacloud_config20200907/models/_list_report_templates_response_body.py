# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListReportTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        report_template_list: List[main_models.ListReportTemplatesResponseBodyReportTemplateList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries to return per page. Valid values: 1 to 50. Default value: 20.
        self.max_results = max_results
        # If the response is truncated, use NextToken to send another request and get results after the truncation point.
        self.next_token = next_token
        # The list of report templates.
        self.report_template_list = report_template_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of templates.
        self.total_count = total_count

    def validate(self):
        if self.report_template_list:
            for v1 in self.report_template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ReportTemplateList'] = []
        if self.report_template_list is not None:
            for k1 in self.report_template_list:
                result['ReportTemplateList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.report_template_list = []
        if m.get('ReportTemplateList') is not None:
            for k1 in m.get('ReportTemplateList'):
                temp_model = main_models.ListReportTemplatesResponseBodyReportTemplateList()
                self.report_template_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListReportTemplatesResponseBodyReportTemplateList(DaraModel):
    def __init__(
        self,
        report_file_formats: str = None,
        report_granularity: str = None,
        report_language: str = None,
        report_scope: List[main_models.ListReportTemplatesResponseBodyReportTemplateListReportScope] = None,
        report_template_description: str = None,
        report_template_id: str = None,
        report_template_name: str = None,
        subscription_frequency: str = None,
    ):
        # The format of the report. Only Excel is supported.
        self.report_file_formats = report_file_formats
        # The aggregation granularity of the report.
        # 
        # From the management account perspective, the following options are supported:
        # 
        # - AllInOne: Aggregate all accounts in the template scope into one report.
        # 
        # - GroupByAggregator: Generate reports by aggregator group. Output as one compressed file.
        # 
        # - GroupByAccount: Generate separate reports for each account (default). Output as one compressed file.
        # 
        # Member accounts support only GroupByAccount.
        self.report_granularity = report_granularity
        # The language of the report. Valid values: zh-CN and en-US. Default value: en-US.
        self.report_language = report_language
        # An array that defines which rules appear in the audit report. Each ReportScope object uses OR logic (additive logic).
        # 
        # > For example, if the array has two items — the first specifies RuleId cr-1 and the second specifies RuleId cr-2 — then the report covers both cr-1 and cr-2.
        self.report_scope = report_scope
        # The description of the report template.
        self.report_template_description = report_template_description
        # The ID of the report template.
        self.report_template_id = report_template_id
        # The name of the report template.
        self.report_template_name = report_template_name
        # The subscription frequency of the report. If this parameter is specified, it must be a Quartz-formatted cron expression.
        # 
        # The format is: second minute hour day month weekday. Common examples:
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
        # - "?" means no specific value for day or weekday.
        # 
        # - "MON" means Monday.
        # 
        # > Times are in UTC+8. Adjust your cron expression based on your local time zone.
        # 
        # > The system tries to run reports at the scheduled time, but delays may occur due to report generation. Each template can trigger at most one notification per day.
        # 
        # > In Quartz, weekdays are numbered starting from Sunday: 1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Saturday.
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
                temp_model = main_models.ListReportTemplatesResponseBodyReportTemplateListReportScope()
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

class ListReportTemplatesResponseBodyReportTemplateListReportScope(DaraModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: str = None,
    ):
        # The key for the report scope. Supported values:
        # 
        # - AggregatorId
        # 
        # - CompliancePackId
        # 
        # - RuleId
        self.key = key
        # The matching logic. Only In is supported.
        self.match_type = match_type
        # The value for the report scope. For multiple values of the same type — such as multiple rule IDs — separate them with commas (,).
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

