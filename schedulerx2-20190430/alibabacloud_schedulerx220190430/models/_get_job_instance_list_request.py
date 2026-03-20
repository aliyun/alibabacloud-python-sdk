# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobInstanceListRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        start_timestamp: int = None,
        status: int = None,
    ):
        # The end of the time range to query. Specify a UNIX timestamp.
        self.end_timestamp = end_timestamp
        # The application group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job ID.
        self.job_id = job_id
        # The namespace ID. You can obtain the namespace ID on the **Namespace** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Specify a UNIX timestamp.
        self.start_timestamp = start_timestamp
        # The status of the job instance. Valid values:
        # 
        # 1: The job instance is pending. 3: The job instance is running. 4: The job instance is run. 5: The job instance fails. 9: The request for running the job instance is rejected. To specify this parameter, you must declare the following enumeration class: com.alibaba.schedulerx.common.domain.InstanceStatus.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

