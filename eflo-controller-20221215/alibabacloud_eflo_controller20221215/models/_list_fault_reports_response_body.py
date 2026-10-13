# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListFaultReportsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        next_token: str = None,
        reports: List[main_models.ListFaultReportsResponseBodyReports] = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The pagination token.
        self.next_token = next_token
        # The fault report details.
        self.reports = reports
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.reports:
            for v1 in self.reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.ListFaultReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFaultReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        diagnosis_type: str = None,
        finish_time: str = None,
        node_id: str = None,
        report_id: str = None,
        status: str = None,
    ):
        # The time when the fault report was created. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # The description of the fault report.
        self.description = description
        # The diagnosis type.
        self.diagnosis_type = diagnosis_type
        # The time when the fault report was resolved. The time is in the YYYY-MM-DD HH:mm:ss format.
        self.finish_time = finish_time
        # The node ID.
        self.node_id = node_id
        # The fault report ID.
        self.report_id = report_id
        # The status of the fault report.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.diagnosis_type is not None:
            result['DiagnosisType'] = self.diagnosis_type

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiagnosisType') is not None:
            self.diagnosis_type = m.get('DiagnosisType')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

