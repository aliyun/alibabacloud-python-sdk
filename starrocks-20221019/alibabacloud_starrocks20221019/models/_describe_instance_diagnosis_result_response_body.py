# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceDiagnosisResultResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.DescribeInstanceDiagnosisResultResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeInstanceDiagnosisResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstanceDiagnosisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        best_practice: str = None,
        description: str = None,
        dimension: str = None,
        evaluation_time: int = None,
        full_score: float = None,
        instance_id: str = None,
        introduction: str = None,
        item_id: str = None,
        item_name: str = None,
        report_date: str = None,
        score: float = None,
        status: str = None,
        suggestion: str = None,
    ):
        self.best_practice = best_practice
        self.description = description
        self.dimension = dimension
        self.evaluation_time = evaluation_time
        self.full_score = full_score
        self.instance_id = instance_id
        self.introduction = introduction
        self.item_id = item_id
        self.item_name = item_name
        self.report_date = report_date
        self.score = score
        self.status = status
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.best_practice is not None:
            result['BestPractice'] = self.best_practice

        if self.description is not None:
            result['Description'] = self.description

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time

        if self.full_score is not None:
            result['FullScore'] = self.full_score

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.score is not None:
            result['Score'] = self.score

        if self.status is not None:
            result['Status'] = self.status

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BestPractice') is not None:
            self.best_practice = m.get('BestPractice')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')

        if m.get('FullScore') is not None:
            self.full_score = m.get('FullScore')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

