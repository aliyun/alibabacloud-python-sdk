# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAsynJobsRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        begin_time: int = None,
        end_time: int = None,
        job_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The name of the operation.
        self.api_name = api_name
        # The timestamp that indicates the start time of the task. Unit: milliseconds.
        # 
        # Specify the timestamp in the Unix format to indicate the total amount of time that is from 00:00:00 (UTC+0) on January 1, 1970 to when the status of the asynchronous task is queried.
        self.begin_time = begin_time
        # The timestamp that indicates the end time of the task. Unit: milliseconds.
        # 
        # Specify the timestamp in the Unix format to indicate the total amount of time that is from 00:00:00 (UTC+0) on January 1, 1970 to when the status of the asynchronous task is returned.
        self.end_time = end_time
        # The asynchronous task IDs.
        self.job_ids = job_ids
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The resource IDs.
        self.resource_ids = resource_ids
        # The type of the associated resource. Valid values:
        # 
        # *   **loadbalancer**: an Application Load Balancer (ALB) instance
        # *   **listener**: a listener
        # *   **rule**: a forwarding rule
        # *   **acl**: an access control list (ACL)
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

