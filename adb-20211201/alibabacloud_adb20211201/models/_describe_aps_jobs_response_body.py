# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsJobsResponseBody(DaraModel):
    def __init__(
        self,
        apsjobs: List[main_models.DescribeApsJobsResponseBodyAPSJobs] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        # The queried APS jobs.
        self.apsjobs = apsjobs
        # The HTTP status code.
        self.code = code
        # The status code. A value of 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.apsjobs:
            for v1 in self.apsjobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['APSJobs'] = []
        if self.apsjobs is not None:
            for k1 in self.apsjobs:
                result['APSJobs'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apsjobs = []
        if m.get('APSJobs') is not None:
            for k1 in m.get('APSJobs'):
                temp_model = main_models.DescribeApsJobsResponseBodyAPSJobs()
                self.apsjobs.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApsJobsResponseBodyAPSJobs(DaraModel):
    def __init__(
        self,
        aps_job_id: str = None,
        aps_job_name: str = None,
        create_time: str = None,
        delay: int = None,
        destination_instance_id: str = None,
        err_message: str = None,
        projress: str = None,
        source_instance_id: str = None,
        status: str = None,
        sub_status: str = None,
    ):
        # The job ID.
        self.aps_job_id = aps_job_id
        # The name of the APS job.
        self.aps_job_name = aps_job_name
        # The time when the APS job was created.
        self.create_time = create_time
        # The synchronization latency.
        self.delay = delay
        # The destination cluster ID.
        self.destination_instance_id = destination_instance_id
        # The error message.
        self.err_message = err_message
        # The progress.
        self.projress = projress
        # The ID of the source instance or cluster.
        self.source_instance_id = source_instance_id
        # The status of the APS job.
        self.status = status
        # The status of the task.
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_job_id is not None:
            result['ApsJobId'] = self.aps_job_id

        if self.aps_job_name is not None:
            result['ApsJobName'] = self.aps_job_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.destination_instance_id is not None:
            result['DestinationInstanceID'] = self.destination_instance_id

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.projress is not None:
            result['Projress'] = self.projress

        if self.source_instance_id is not None:
            result['SourceInstanceID'] = self.source_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobId') is not None:
            self.aps_job_id = m.get('ApsJobId')

        if m.get('ApsJobName') is not None:
            self.aps_job_name = m.get('ApsJobName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationInstanceID') is not None:
            self.destination_instance_id = m.get('DestinationInstanceID')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('Projress') is not None:
            self.projress = m.get('Projress')

        if m.get('SourceInstanceID') is not None:
            self.source_instance_id = m.get('SourceInstanceID')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        return self

