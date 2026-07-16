# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDoctorApplicationsRequest(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        cluster_id: str = None,
        date_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        queues: List[str] = None,
        region_id: str = None,
        types: List[str] = None,
        users: List[str] = None,
    ):
        # The IDs of jobs that are submitted to YARN.
        self.app_ids = app_ids
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specify the date in the ISO 8601 standard. For example, 2023-01-01 represents January 1, 2023.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The field that you use to sort the query results. Valid values:
        # 
        # 1. startTime: the time when the job starts
        # 
        # 2. endTime: the time when the job ends
        # 
        # 3. vcoreUtilization: the vCPU utilization of the job
        # 
        # 4. memUtilization: the memory usage of the job
        # 
        # 5. vcoreSeconds: the aggregated number of vCPUs that are allocated to the job multiplied by the number of seconds the job has been running
        # 
        # 6. memSeconds: the aggregated amount of memory that is allocated to the job multiplied by the number of seconds the job has been running
        # 
        # 7. score: the score of the job
        self.order_by = order_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # - ASC: the ascending order
        # 
        # - DESC: the descending order
        self.order_type = order_type
        # The YARN queues to which the jobs are submitted.
        self.queues = queues
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The YARN engines to which the jobs are submitted.
        self.types = types
        # The users who submit the jobs.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.queues is not None:
            result['Queues'] = self.queues

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.types is not None:
            result['Types'] = self.types

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Queues') is not None:
            self.queues = m.get('Queues')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

