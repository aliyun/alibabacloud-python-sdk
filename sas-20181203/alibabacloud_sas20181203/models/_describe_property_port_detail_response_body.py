# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyPortDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyPortDetailResponseBodyPageInfo = None,
        propertys: List[main_models.DescribePropertyPortDetailResponseBodyPropertys] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The fingerprints of the ports.
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
            temp_model = main_models.DescribePropertyPortDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.propertys = []
        if m.get('Propertys') is not None:
            for k1 in m.get('Propertys'):
                temp_model = main_models.DescribePropertyPortDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyPortDetailResponseBodyPropertys(DaraModel):
    def __init__(
        self,
        bind_ip: str = None,
        create_timestamp: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        pid: str = None,
        port: str = None,
        proc_name: str = None,
        proto: str = None,
        uuid: str = None,
    ):
        # The IP address bound to the port.
        self.bind_ip = bind_ip
        # The timestamp of the last fingerprint collection. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The instance ID of the server.
        self.instance_id = instance_id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The IP address of the network interface controller (NIC) that is bound to the listening port.
        self.ip = ip
        # The ID of the server process that listens on the port.
        self.pid = pid
        # The listener port.
        self.port = port
        # The name of the server process.
        self.proc_name = proc_name
        # The network protocol that is used by the listening port.
        self.proto = proto
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_ip is not None:
            result['BindIp'] = self.bind_ip

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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.port is not None:
            result['Port'] = self.port

        if self.proc_name is not None:
            result['ProcName'] = self.proc_name

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindIp') is not None:
            self.bind_ip = m.get('BindIp')

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

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProcName') is not None:
            self.proc_name = m.get('ProcName')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribePropertyPortDetailResponseBodyPageInfo(DaraModel):
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

