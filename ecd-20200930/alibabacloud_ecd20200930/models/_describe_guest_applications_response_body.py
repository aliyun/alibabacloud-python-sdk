# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeGuestApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.DescribeGuestApplicationsResponseBodyApplications] = None,
        request_id: str = None,
    ):
        # The applications.
        self.applications = applications
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.DescribeGuestApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGuestApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        application_version: str = None,
        cpu_percent: float = None,
        gpu_percent: float = None,
        icon_url: str = None,
        io_speed: float = None,
        mem_percent: float = None,
        pid: int = None,
        process_data: List[main_models.DescribeGuestApplicationsResponseBodyApplicationsProcessData] = None,
        process_path: str = None,
        status: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The application version.
        self.application_version = application_version
        # The CPU utilization (%).
        self.cpu_percent = cpu_percent
        # The GPU utilization (%).
        self.gpu_percent = gpu_percent
        # The icon URL of the application.
        self.icon_url = icon_url
        # The I/O read and write performance. Unit: byte/s.
        self.io_speed = io_speed
        # The memory utilization (%).
        self.mem_percent = mem_percent
        # The process ID (PID).
        self.pid = pid
        # The processes.
        self.process_data = process_data
        # The path to the process.
        self.process_path = process_path
        # The status of the application.
        # 
        # Valid value:
        # 
        # *   Idle: The application is installed in the cloud computer but is not running.
        # *   Running: The application has been installed in the cloud computer and is running.
        self.status = status

    def validate(self):
        if self.process_data:
            for v1 in self.process_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_version is not None:
            result['ApplicationVersion'] = self.application_version

        if self.cpu_percent is not None:
            result['CpuPercent'] = self.cpu_percent

        if self.gpu_percent is not None:
            result['GpuPercent'] = self.gpu_percent

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.io_speed is not None:
            result['IoSpeed'] = self.io_speed

        if self.mem_percent is not None:
            result['MemPercent'] = self.mem_percent

        if self.pid is not None:
            result['Pid'] = self.pid

        result['ProcessData'] = []
        if self.process_data is not None:
            for k1 in self.process_data:
                result['ProcessData'].append(k1.to_map() if k1 else None)

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationVersion') is not None:
            self.application_version = m.get('ApplicationVersion')

        if m.get('CpuPercent') is not None:
            self.cpu_percent = m.get('CpuPercent')

        if m.get('GpuPercent') is not None:
            self.gpu_percent = m.get('GpuPercent')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('IoSpeed') is not None:
            self.io_speed = m.get('IoSpeed')

        if m.get('MemPercent') is not None:
            self.mem_percent = m.get('MemPercent')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        self.process_data = []
        if m.get('ProcessData') is not None:
            for k1 in m.get('ProcessData'):
                temp_model = main_models.DescribeGuestApplicationsResponseBodyApplicationsProcessData()
                self.process_data.append(temp_model.from_map(k1))

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGuestApplicationsResponseBodyApplicationsProcessData(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        application_version: str = None,
        cpu_percent: float = None,
        gpu_percent: float = None,
        iospeed: float = None,
        mem_percent: float = None,
        pid: int = None,
        process_path: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The application version.
        self.application_version = application_version
        # The CPU utilization (%).
        self.cpu_percent = cpu_percent
        # The GPU usage (%).
        self.gpu_percent = gpu_percent
        # The I/O read and write performance. Unit: byte/s.
        self.iospeed = iospeed
        # The memory usage (%).
        self.mem_percent = mem_percent
        # The PID.
        self.pid = pid
        # The path to the process.
        self.process_path = process_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_version is not None:
            result['ApplicationVersion'] = self.application_version

        if self.cpu_percent is not None:
            result['CpuPercent'] = self.cpu_percent

        if self.gpu_percent is not None:
            result['GpuPercent'] = self.gpu_percent

        if self.iospeed is not None:
            result['Iospeed'] = self.iospeed

        if self.mem_percent is not None:
            result['MemPercent'] = self.mem_percent

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationVersion') is not None:
            self.application_version = m.get('ApplicationVersion')

        if m.get('CpuPercent') is not None:
            self.cpu_percent = m.get('CpuPercent')

        if m.get('GpuPercent') is not None:
            self.gpu_percent = m.get('GpuPercent')

        if m.get('Iospeed') is not None:
            self.iospeed = m.get('Iospeed')

        if m.get('MemPercent') is not None:
            self.mem_percent = m.get('MemPercent')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        return self

