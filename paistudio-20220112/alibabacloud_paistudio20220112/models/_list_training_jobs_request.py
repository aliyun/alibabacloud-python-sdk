# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListTrainingJobsRequest(DaraModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        end_time: str = None,
        is_temp_algo: bool = None,
        labels: Dict[str, Any] = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        training_job_id: str = None,
        training_job_name: str = None,
        workspace_id: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.end_time = end_time
        self.is_temp_algo = is_temp_algo
        self.labels = labels
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.start_time = start_time
        self.status = status
        self.training_job_id = training_job_id
        self.training_job_name = training_job_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_temp_algo is not None:
            result['IsTempAlgo'] = self.is_temp_algo

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id

        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsTempAlgo') is not None:
            self.is_temp_algo = m.get('IsTempAlgo')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')

        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

