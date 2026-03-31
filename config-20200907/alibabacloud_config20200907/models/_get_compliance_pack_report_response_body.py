# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetCompliancePackReportResponseBody(DaraModel):
    def __init__(
        self,
        compliance_pack_report: main_models.GetCompliancePackReportResponseBodyCompliancePackReport = None,
        request_id: str = None,
    ):
        # The information about the compliance evaluation report.
        self.compliance_pack_report = compliance_pack_report
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_report:
            self.compliance_pack_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_report is not None:
            result['CompliancePackReport'] = self.compliance_pack_report.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackReport') is not None:
            temp_model = main_models.GetCompliancePackReportResponseBodyCompliancePackReport()
            self.compliance_pack_report = temp_model.from_map(m.get('CompliancePackReport'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCompliancePackReportResponseBodyCompliancePackReport(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        report_create_timestamp: int = None,
        report_status: str = None,
        report_url: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the compliance package belongs.
        self.account_id = account_id
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The timestamp when the compliance evaluation report was generated. Unit: milliseconds.
        self.report_create_timestamp = report_create_timestamp
        # The status of the compliance evaluation report. Valid values:
        # 
        # *   NONE: The compliance evaluation report is not generated.
        # *   CREATING: The compliance evaluation report is being generated.
        # *   COMPLETE: The compliance evaluation report is generated.
        self.report_status = report_status
        # The URL that is used to download the compliance evaluation report.
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

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_url is not None:
            result['ReportUrl'] = self.report_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')

        return self

