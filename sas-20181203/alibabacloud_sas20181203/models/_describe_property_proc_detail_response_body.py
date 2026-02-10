# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyProcDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyProcDetailResponseBodyPageInfo = None,
        propertys: List[main_models.DescribePropertyProcDetailResponseBodyPropertys] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # An array that consists of the fingerprints of the processes.
        self.propertys = propertys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.propertys:
            for v1 in self.propertys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Propertys'] = []
        if self.propertys is not None:
            for k1 in self.propertys:
                result['Propertys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribePropertyProcDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.propertys = []
        if m.get('Propertys') is not None:
            for k1 in m.get('Propertys'):
                temp_model = main_models.DescribePropertyProcDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyProcDetailResponseBodyPropertys(DaraModel):
    def __init__(
        self,
        cmdline: str = None,
        create_timestamp: int = None,
        euid_name: str = None,
        file_hash: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        is_package: int = None,
        md_5: str = None,
        name: str = None,
        path: str = None,
        pid: str = None,
        pname: str = None,
        start_time: str = None,
        start_time_dt: int = None,
        state: str = None,
        user: str = None,
        uuid: str = None,
    ):
        # The startup parameter of the process.
        self.cmdline = cmdline
        # The timestamp of last data collection. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The permission that is required to run the process.
        self.euid_name = euid_name
        # Process file hash information.
        self.file_hash = file_hash
        # The ID of the server that is associated with the process.
        self.instance_id = instance_id
        # The name of the server that is associated with the process.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # Indicates whether the process is a package installation process. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.is_package = is_package
        # The MD5 hash value of the process file.
        self.md_5 = md_5
        # The name of the process.
        self.name = name
        # The path of the process.
        self.path = path
        # The ID of the process.
        self.pid = pid
        # The name of the parent process to which the process belongs.
        self.pname = pname
        # The time when the process starts.
        self.start_time = start_time
        # The timestamp when the process starts. Unit: milliseconds.
        self.start_time_dt = start_time_dt
        # The status of the process.
        self.state = state
        # The user who runs the process.
        self.user = user
        # The UUID of the server that is associated with the process.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.euid_name is not None:
            result['EuidName'] = self.euid_name

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.is_package is not None:
            result['IsPackage'] = self.is_package

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.pname is not None:
            result['Pname'] = self.pname

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_dt is not None:
            result['StartTimeDt'] = self.start_time_dt

        if self.state is not None:
            result['State'] = self.state

        if self.user is not None:
            result['User'] = self.user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EuidName') is not None:
            self.euid_name = m.get('EuidName')

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('IsPackage') is not None:
            self.is_package = m.get('IsPackage')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Pname') is not None:
            self.pname = m.get('Pname')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeDt') is not None:
            self.start_time_dt = m.get('StartTimeDt')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribePropertyProcDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The value of NextToken that is returned when the NextToken method is used.
        self.next_token = next_token
        # The number of entries returned per page. Default value: **10**.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

