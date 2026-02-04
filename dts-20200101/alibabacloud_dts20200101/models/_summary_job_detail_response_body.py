# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class SummaryJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_id: str = None,
        progress_summary_details: List[main_models.SummaryJobDetailResponseBodyProgressSummaryDetails] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the data migration or data synchronization task.
        self.job_id = job_id
        # The returned information about the migrated or synchronized objects in arrays.
        # 
        # >  The arrays are in the following format: [{"key":"Function","state":5,"totalCount":22},{"key":"Procedure","state":5,"totalCount":26},{"key":"Table","state":0,"totalCount":68},{"key":"View","state":5,"totalCount":100}].
        self.progress_summary_details = progress_summary_details
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.progress_summary_details:
            for v1 in self.progress_summary_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['ProgressSummaryDetails'] = []
        if self.progress_summary_details is not None:
            for k1 in self.progress_summary_details:
                result['ProgressSummaryDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.progress_summary_details = []
        if m.get('ProgressSummaryDetails') is not None:
            for k1 in m.get('ProgressSummaryDetails'):
                temp_model = main_models.SummaryJobDetailResponseBodyProgressSummaryDetails()
                self.progress_summary_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SummaryJobDetailResponseBodyProgressSummaryDetails(DaraModel):
    def __init__(
        self,
        key: str = None,
        state: int = None,
        total_count: int = None,
    ):
        # The type of migrated or synchronized object. Valid values: **Table**, **Constraint**, **Index**, **View**, **Materialize View**, **Type**, **Synonym**, **Trigger**, **Function**, **Procedure**, **Package**, **Default**, **Rule**, **PlanGuide**, and **Sequence**.
        self.key = key
        # The state of the data migration or data synchronization task. Valid values:
        # 
        # *   **0**: The task was complete.
        # *   **1**: The task was waiting to start.
        # *   **2**: The task was being initialized.
        # *   **3**: The task was in progress.
        # *   **4**: An error occurred.
        # *   **5**: The task failed.
        self.state = state
        # The total number of migrated or synchronized objects.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.state is not None:
            result['State'] = self.state

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

