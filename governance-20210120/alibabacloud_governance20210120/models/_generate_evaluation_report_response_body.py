# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateEvaluationReportResponseBody(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        evaluation_score: float = None,
        evaluation_time: str = None,
        finished: str = None,
        report_type: str = None,
        report_url: str = None,
        request_id: str = None,
    ):
        self.account_id = account_id
        self.evaluation_score = evaluation_score
        self.evaluation_time = evaluation_time
        self.finished = finished
        self.report_type = report_type
        self.report_url = report_url
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score

        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_url is not None:
            result['ReportUrl'] = self.report_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')

        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

