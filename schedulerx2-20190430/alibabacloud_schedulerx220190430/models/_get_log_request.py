# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        group_id: str = None,
        job_id: str = None,
        job_instance_id: str = None,
        keyword: str = None,
        line: int = None,
        namespace: str = None,
        namespace_source: str = None,
        offset: int = None,
        region_id: str = None,
        reverse: bool = None,
        start_timestamp: int = None,
    ):
        # The time when the job stops running. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_timestamp = end_timestamp
        # The application group ID. You can obtain the application group ID on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job ID.
        self.job_id = job_id
        # The job instance ID.
        self.job_instance_id = job_instance_id
        # The keyword.
        self.keyword = keyword
        # The number of rows to return. The maximum number is 200.
        self.line = line
        # The namespace ID. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The number of offset rows. This parameter can be used for a paged query.
        self.offset = offset
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to reverse the order. By default, the order is reversed.
        self.reverse = reverse
        # The time when the job starts to run. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_timestamp = start_timestamp

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

        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.line is not None:
            result['Line'] = self.line

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

