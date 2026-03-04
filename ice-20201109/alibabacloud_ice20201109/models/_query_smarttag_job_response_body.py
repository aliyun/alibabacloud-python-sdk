# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QuerySmarttagJobResponseBody(DaraModel):
    def __init__(
        self,
        job_status: str = None,
        request_id: str = None,
        results: main_models.QuerySmarttagJobResponseBodyResults = None,
        usages: main_models.QuerySmarttagJobResponseBodyUsages = None,
        user_data: str = None,
    ):
        # The status of the job. Valid values:
        # 
        # *   **Success**: The job was successful.
        # *   **Fail**: The job failed.
        # *   **Processing**: The job is in progress.
        # *   **Submitted**: The job is submitted and waiting to be processed.
        self.job_status = job_status
        # The request ID.
        self.request_id = request_id
        self.results = results
        self.usages = usages
        # The content of callback messages that are sent to Simple Message Queue (SMQ) when the information of the smart tagging job changes. For more information about the parameters contained in the callback message, see the "Callback parameters" section of this topic.
        self.user_data = user_data

    def validate(self):
        if self.results:
            self.results.validate()
        if self.usages:
            self.usages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.usages is not None:
            result['Usages'] = self.usages.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.QuerySmarttagJobResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Usages') is not None:
            temp_model = main_models.QuerySmarttagJobResponseBodyUsages()
            self.usages = temp_model.from_map(m.get('Usages'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QuerySmarttagJobResponseBodyUsages(DaraModel):
    def __init__(
        self,
        usage: List[main_models.QuerySmarttagJobResponseBodyUsagesUsage] = None,
    ):
        self.usage = usage

    def validate(self):
        if self.usage:
            for v1 in self.usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Usage'] = []
        if self.usage is not None:
            for k1 in self.usage:
                result['Usage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage = []
        if m.get('Usage') is not None:
            for k1 in m.get('Usage'):
                temp_model = main_models.QuerySmarttagJobResponseBodyUsagesUsage()
                self.usage.append(temp_model.from_map(k1))

        return self

class QuerySmarttagJobResponseBodyUsagesUsage(DaraModel):
    def __init__(
        self,
        quota: int = None,
        type: str = None,
    ):
        self.quota = quota
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QuerySmarttagJobResponseBodyResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.QuerySmarttagJobResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QuerySmarttagJobResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QuerySmarttagJobResponseBodyResultsResult(DaraModel):
    def __init__(
        self,
        data: str = None,
        type: str = None,
    ):
        self.data = data
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

