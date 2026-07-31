# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class DownloadSemanticResultsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DownloadSemanticResultsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The collection of result files for the specified node run. Multiple items are returned if a single run generates multiple files.
        self.data = data
        # The request ID. Used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DownloadSemanticResultsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DownloadSemanticResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        results: List[main_models.DownloadSemanticResultsResponseBodyDataResults] = None,
    ):
        # The list of result files. Each item contains the associated node name, the associated run ID, and a short-lived download URL.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DownloadSemanticResultsResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DownloadSemanticResultsResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        job_name: str = None,
        job_run_id: str = None,
    ):
        # The temporary pre-signed download URL of the result file. Download the file by using an HTTP GET request as soon as possible. Do not log, share, or treat the full URL as a long-term address.
        self.download_url = download_url
        # The node name to which the artifact belongs. This value is the same as the JobName value in the request.
        self.job_name = job_name
        # The run ID to which the artifact belongs. You can compare this value with the Data.JobRunId value from the RunSemanticJob response or the JobRunId value from ListSemanticJobRuns.
        self.job_run_id = job_run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_run_id is not None:
            result['JobRunId'] = self.job_run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobRunId') is not None:
            self.job_run_id = m.get('JobRunId')

        return self

