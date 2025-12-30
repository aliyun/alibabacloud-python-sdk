# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_filter: main_models.ListJobsRequestJobFilter = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job filter information.
        self.job_filter = job_filter
        # The page number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Maximum value: 50.
        # *   Default value: 10
        self.page_size = page_size

    def validate(self):
        if self.job_filter:
            self.job_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_filter is not None:
            result['JobFilter'] = self.job_filter.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobFilter') is not None:
            temp_model = main_models.ListJobsRequestJobFilter()
            self.job_filter = temp_model.from_map(m.get('JobFilter'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListJobsRequestJobFilter(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        diagnosis: List[main_models.ListJobsRequestJobFilterDiagnosis] = None,
        job_name: str = None,
        job_status: str = None,
        nodes: List[str] = None,
        queues: List[str] = None,
        sort_by: main_models.ListJobsRequestJobFilterSortBy = None,
        users: List[str] = None,
    ):
        # The time when the job was last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since 1970-01-01T00:00:00Z.
        self.create_time_end = create_time_end
        # The time when the job started. The value is a UNIX timestamp representing the number of seconds that have elapsed since 1970-01-01T00:00:00Z.
        self.create_time_start = create_time_start
        # Job diagnosis and analysis list.
        self.diagnosis = diagnosis
        # The job name. Fuzzy match is supported.
        self.job_name = job_name
        # The job status. Valid values:
        # 
        # *   all: returns all jobs.
        # *   finished: returns completed jobs.
        # *   notfinish: returns uncompleted jobs.
        # 
        # Default value: all.
        self.job_status = job_status
        # The compute nodes that run the jobs.
        self.nodes = nodes
        # The queues to which the jobs belong.
        self.queues = queues
        # The result sorting configurations.
        self.sort_by = sort_by
        # The users that run the jobs.
        self.users = users

    def validate(self):
        if self.diagnosis:
            for v1 in self.diagnosis:
                 if v1:
                    v1.validate()
        if self.sort_by:
            self.sort_by.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        result['Diagnosis'] = []
        if self.diagnosis is not None:
            for k1 in self.diagnosis:
                result['Diagnosis'].append(k1.to_map() if k1 else None)

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.queues is not None:
            result['Queues'] = self.queues

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by.to_map()

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        self.diagnosis = []
        if m.get('Diagnosis') is not None:
            for k1 in m.get('Diagnosis'):
                temp_model = main_models.ListJobsRequestJobFilterDiagnosis()
                self.diagnosis.append(temp_model.from_map(k1))

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('Queues') is not None:
            self.queues = m.get('Queues')

        if m.get('SortBy') is not None:
            temp_model = main_models.ListJobsRequestJobFilterSortBy()
            self.sort_by = temp_model.from_map(m.get('SortBy'))

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

class ListJobsRequestJobFilterSortBy(DaraModel):
    def __init__(
        self,
        execute_order: str = None,
        pend_order: str = None,
        submit_order: str = None,
    ):
        # The order in which jobs are sorted based on their execution time. Valid values:
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        # 
        # Default value: desc.
        self.execute_order = execute_order
        # The order in which jobs are sorted based on their queuing time. Valid values:
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        # 
        # Default value: desc.
        self.pend_order = pend_order
        # The order in which jobs are sorted based on their submitting time. Valid values:
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        # 
        # Default value: desc.
        self.submit_order = submit_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execute_order is not None:
            result['ExecuteOrder'] = self.execute_order

        if self.pend_order is not None:
            result['PendOrder'] = self.pend_order

        if self.submit_order is not None:
            result['SubmitOrder'] = self.submit_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteOrder') is not None:
            self.execute_order = m.get('ExecuteOrder')

        if m.get('PendOrder') is not None:
            self.pend_order = m.get('PendOrder')

        if m.get('SubmitOrder') is not None:
            self.submit_order = m.get('SubmitOrder')

        return self

class ListJobsRequestJobFilterDiagnosis(DaraModel):
    def __init__(
        self,
        operator: str = None,
        option: str = None,
        threshold: str = None,
    ):
        # Job diagnosis threshold comparator.
        self.operator = operator
        # Job diagnosis and analysis metrics
        self.option = option
        # Job diagnosis threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['Operator'] = self.operator

        if self.option is not None:
            result['Option'] = self.option

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

