# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationResultsResponseBody(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        request_id: str = None,
        results: main_models.ListEvaluationResultsResponseBodyResults = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The request ID.
        self.request_id = request_id
        # The check results, including the status of the overall check and the results of check items.
        self.results = results

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.ListEvaluationResultsResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        return self

class ListEvaluationResultsResponseBodyResults(DaraModel):
    def __init__(
        self,
        evaluation_time: str = None,
        metric_results: List[main_models.ListEvaluationResultsResponseBodyResultsMetricResults] = None,
        status: str = None,
        total_score: float = None,
    ):
        # The end time of the overall check. The time is displayed in UTC.
        self.evaluation_time = evaluation_time
        # The check result.
        self.metric_results = metric_results
        # The status of the overall check. Valid values:
        # 
        # *   Running: The check is in progress.
        # *   Finished: The check is complete.
        # *   failed: The check fails.
        self.status = status
        # The overall score.
        self.total_score = total_score

    def validate(self):
        if self.metric_results:
            for v1 in self.metric_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time

        result['MetricResults'] = []
        if self.metric_results is not None:
            for k1 in self.metric_results:
                result['MetricResults'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.total_score is not None:
            result['TotalScore'] = self.total_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')

        self.metric_results = []
        if m.get('MetricResults') is not None:
            for k1 in m.get('MetricResults'):
                temp_model = main_models.ListEvaluationResultsResponseBodyResultsMetricResults()
                self.metric_results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')

        return self

class ListEvaluationResultsResponseBodyResultsMetricResults(DaraModel):
    def __init__(
        self,
        account_summary: main_models.ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary = None,
        available_remediation: List[main_models.ListEvaluationResultsResponseBodyResultsMetricResultsAvailableRemediation] = None,
        error_info: main_models.ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo = None,
        evaluation_time: str = None,
        id: str = None,
        potential_score_increase: float = None,
        resources_summary: main_models.ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary = None,
        result: float = None,
        risk: str = None,
        status: str = None,
    ):
        self.account_summary = account_summary
        self.available_remediation = available_remediation
        # The error information.
        # 
        # >  This parameter is returned only if the value of `Status` is `Failed`.
        self.error_info = error_info
        # The end time of the check item. The time is displayed in UTC.
        self.evaluation_time = evaluation_time
        # The ID of the check item.
        self.id = id
        self.potential_score_increase = potential_score_increase
        # The checked resources.
        self.resources_summary = resources_summary
        # The rate of the non-compliant resources.
        self.result = result
        # The risk level. Valid values:
        # 
        # *   Error: high risk
        # *   Warning: medium risk
        # *   None: no risk
        self.risk = risk
        # The status of the check item. Valid values:
        # 
        # *   Running: The check is in progress.
        # *   Finished: The check is complete.
        # *   failed: The check fails.
        self.status = status

    def validate(self):
        if self.account_summary:
            self.account_summary.validate()
        if self.available_remediation:
            for v1 in self.available_remediation:
                 if v1:
                    v1.validate()
        if self.error_info:
            self.error_info.validate()
        if self.resources_summary:
            self.resources_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_summary is not None:
            result['AccountSummary'] = self.account_summary.to_map()

        result['AvailableRemediation'] = []
        if self.available_remediation is not None:
            for k1 in self.available_remediation:
                result['AvailableRemediation'].append(k1.to_map() if k1 else None)

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()

        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time

        if self.id is not None:
            result['Id'] = self.id

        if self.potential_score_increase is not None:
            result['PotentialScoreIncrease'] = self.potential_score_increase

        if self.resources_summary is not None:
            result['ResourcesSummary'] = self.resources_summary.to_map()

        if self.result is not None:
            result['Result'] = self.result

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSummary') is not None:
            temp_model = main_models.ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary()
            self.account_summary = temp_model.from_map(m.get('AccountSummary'))

        self.available_remediation = []
        if m.get('AvailableRemediation') is not None:
            for k1 in m.get('AvailableRemediation'):
                temp_model = main_models.ListEvaluationResultsResponseBodyResultsMetricResultsAvailableRemediation()
                self.available_remediation.append(temp_model.from_map(k1))

        if m.get('ErrorInfo') is not None:
            temp_model = main_models.ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo()
            self.error_info = temp_model.from_map(m.get('ErrorInfo'))

        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PotentialScoreIncrease') is not None:
            self.potential_score_increase = m.get('PotentialScoreIncrease')

        if m.get('ResourcesSummary') is not None:
            temp_model = main_models.ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary()
            self.resources_summary = temp_model.from_map(m.get('ResourcesSummary'))

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary(DaraModel):
    def __init__(
        self,
        non_compliant: int = None,
    ):
        # The number of non-compliant resources.
        self.non_compliant = non_compliant

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_compliant is not None:
            result['NonCompliant'] = self.non_compliant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonCompliant') is not None:
            self.non_compliant = m.get('NonCompliant')

        return self

class ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ListEvaluationResultsResponseBodyResultsMetricResultsAvailableRemediation(DaraModel):
    def __init__(
        self,
        remediation_template_id: str = None,
    ):
        self.remediation_template_id = remediation_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')

        return self

class ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary(DaraModel):
    def __init__(
        self,
        non_compliant: int = None,
    ):
        self.non_compliant = non_compliant

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_compliant is not None:
            result['NonCompliant'] = self.non_compliant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonCompliant') is not None:
            self.non_compliant = m.get('NonCompliant')

        return self

