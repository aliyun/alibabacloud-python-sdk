# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyScaProcessDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyScaProcessDetailResponseBodyPageInfo = None,
        propertys: List[main_models.DescribePropertyScaProcessDetailResponseBodyPropertys] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The processes collected by the asset fingerprints feature.
        self.propertys = propertys
        # The request ID.
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
            temp_model = main_models.DescribePropertyScaProcessDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.propertys = []
        if m.get('Propertys') is not None:
            for k1 in m.get('Propertys'):
                temp_model = main_models.DescribePropertyScaProcessDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyScaProcessDetailResponseBodyPropertys(DaraModel):
    def __init__(
        self,
        cmdline: str = None,
        create_timestamp: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        name: str = None,
        pid: str = None,
        uuid: str = None,
        version: str = None,
    ):
        # The command line of the process.
        self.cmdline = cmdline
        # The timestamp at which the last asset fingerprint collection is performed. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The instance ID of the server.
        self.instance_id = instance_id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The name of the process.
        self.name = name
        # The ID of the process.
        self.pid = pid
        # The UUID of the server.
        self.uuid = uuid
        # The version of web application service.
        self.version = version

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribePropertyScaProcessDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page. Default value: **10**.
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

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

