# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAgentlessTaskResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAgentlessTaskResponseBodyList] = None,
        page_info: main_models.ListAgentlessTaskResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The tasks.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListAgentlessTaskResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListAgentlessTaskResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAgentlessTaskResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgentlessTaskResponseBodyList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        measure_space: int = None,
        progress: int = None,
        progress_by_project: str = None,
        report_download_url: str = None,
        report_status: str = None,
        result: str = None,
        start_time: int = None,
        status: int = None,
        target_name: str = None,
        target_type: int = None,
        task_id: str = None,
        task_name: str = None,
        uuid: str = None,
    ):
        # The end timestamp of the task. Unit: milliseconds.
        self.end_time = end_time
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The amount of data detected. Unit: MB.
        self.measure_space = measure_space
        # The progress of the task.
        self.progress = progress
        # The execution progress of the check items.
        self.progress_by_project = progress_by_project
        # The download URL of the report.
        self.report_download_url = report_download_url
        # The status of the report. Valid values:
        # 
        # *   **PREPARED**: preparing
        # *   **RUNNING**: running
        # *   **SUCCESS**: succeeded
        # *   **TIMEOUT**: timed out
        # *   **FAILED**: failed
        self.report_status = report_status
        # The result of the detection.
        self.result = result
        # The start timestamp of the task. Unit: milliseconds.
        self.start_time = start_time
        # The status of the detection task.
        # 
        # *   **1**: The detection task is in progress.
        # *   **2**: The detection task is complete.
        # *   **3**: The detection task fails.
        # *   **4**: The detection task times out.
        self.status = status
        # The name of the asset that is detected.
        self.target_name = target_name
        # The type of the asset that is detected. Valid values:
        # 
        # *   **1**: snapshot
        # *   **2**: image
        self.target_type = target_type
        # The ID of the task.
        self.task_id = task_id
        # The name of the detection task.
        self.task_name = task_name
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.measure_space is not None:
            result['MeasureSpace'] = self.measure_space

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.progress_by_project is not None:
            result['ProgressByProject'] = self.progress_by_project

        if self.report_download_url is not None:
            result['ReportDownloadUrl'] = self.report_download_url

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.result is not None:
            result['Result'] = self.result

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MeasureSpace') is not None:
            self.measure_space = m.get('MeasureSpace')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProgressByProject') is not None:
            self.progress_by_project = m.get('ProgressByProject')

        if m.get('ReportDownloadUrl') is not None:
            self.report_download_url = m.get('ReportDownloadUrl')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

