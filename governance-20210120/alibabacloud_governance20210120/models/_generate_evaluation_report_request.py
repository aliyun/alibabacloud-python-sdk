# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GenerateEvaluationReportRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_ids: List[int] = None,
        evaluation_domain: str = None,
        region_id: str = None,
        report_type: str = None,
    ):
        # The account ID. If this parameter is not specified, the report is generated for the current account by default. A management account (MA) can pass in a member account ID to generate a report for the member account.
        self.account_id = account_id
        # The list of member account IDs for which to generate reports.
        # Note: This parameter is required only when you generate a multi-account report and want to specify the scope of accounts.
        self.account_ids = account_ids
        self.evaluation_domain = evaluation_domain
        # RegionId
        self.region_id = region_id
        # The report type. Valid values:
        # - EvaluationAccountHtmlReport: single-account HTML report.
        # - EvaluationAccountExcelReport: single-account Excel report.
        # - EvaluationMultiAccountExcelReport: multi-account Excel report.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.evaluation_domain is not None:
            result['EvaluationDomain'] = self.evaluation_domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EvaluationDomain') is not None:
            self.evaluation_domain = m.get('EvaluationDomain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

