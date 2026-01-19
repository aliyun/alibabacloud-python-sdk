# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateConfigRulesReportResponseBody(DaraModel):
    def __init__(
        self,
        config_rules_report: main_models.GetAggregateConfigRulesReportResponseBodyConfigRulesReport = None,
        request_id: str = None,
    ):
        # The compliance evaluation report.
        self.config_rules_report = config_rules_report
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_rules_report:
            self.config_rules_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rules_report is not None:
            result['ConfigRulesReport'] = self.config_rules_report.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRulesReport') is not None:
            temp_model = main_models.GetAggregateConfigRulesReportResponseBodyConfigRulesReport()
            self.config_rules_report = temp_model.from_map(m.get('ConfigRulesReport'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateConfigRulesReportResponseBodyConfigRulesReport(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        report_create_timestamp: int = None,
        report_id: str = None,
        report_status: str = None,
        report_url: str = None,
    ):
        # The ID of the management account to which the rules belong.
        self.account_id = account_id
        # The ID of the account group.
        self.aggregator_id = aggregator_id
        # The timestamp when the compliance evaluation report was generated. Unit: milliseconds.
        self.report_create_timestamp = report_create_timestamp
        # The ID of the compliance evaluation report.
        self.report_id = report_id
        # The status of the compliance evaluation report. Valid values:
        # 
        # *   NONE: The compliance evaluation report is not generated.
        # *   CREATING: The compliance evaluation report is being generated.
        # *   COMPLETE: The compliance evaluation report was generated.
        self.report_status = report_status
        # The URL used to download the compliance evaluation report.
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_url is not None:
            result['ReportUrl'] = self.report_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')

        return self

