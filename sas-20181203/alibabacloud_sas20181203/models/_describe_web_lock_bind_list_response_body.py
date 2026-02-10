# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWebLockBindListResponseBody(DaraModel):
    def __init__(
        self,
        bind_list: List[main_models.DescribeWebLockBindListResponseBodyBindList] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the servers that have web tamper proofing enabled.
        self.bind_list = bind_list
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The number of entries returned per page. Default value: 20.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of servers that have web tamper proofing enabled.
        self.total_count = total_count

    def validate(self):
        if self.bind_list:
            for v1 in self.bind_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindList'] = []
        if self.bind_list is not None:
            for k1 in self.bind_list:
                result['BindList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_list = []
        if m.get('BindList') is not None:
            for k1 in m.get('BindList'):
                temp_model = main_models.DescribeWebLockBindListResponseBodyBindList()
                self.bind_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebLockBindListResponseBodyBindList(DaraModel):
    def __init__(
        self,
        audit_count: str = None,
        block_count: str = None,
        dir_count: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        os: str = None,
        percent: int = None,
        service_code: str = None,
        service_detail: str = None,
        service_status: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The number of alerts.
        self.audit_count = audit_count
        # The number of blocked tampering events.
        self.block_count = block_count
        # The number of protected directories.
        self.dir_count = dir_count
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The operating system that the server runs.
        self.os = os
        # The percentage of the starting progress of web tamper proofing. Valid values: 0 to 100.
        self.percent = percent
        # The error code for web tamper proofing. Valid values:
        # 
        # *   **2001**: The Security Center agent is offline.
        # *   **9999**: The connection timed out.
        self.service_code = service_code
        # The exception details of web tamper proofing. Valid values:
        # 
        # *   **client offline**: The Security Center agent is offline.
        # *   **timeout**: The connection timed out.
        self.service_detail = service_detail
        # The status of web tamper proofing on the server. Valid values:
        # 
        # *   **stop**: Web tamper proofing is disabled.
        # *   **initializing**: Web tamper proofing is being enabled.
        # *   **exception**: Web tamper proofing is not running as expected.
        # *   **running**: Web tamper proofing is running.
        # *   **closing**: Web tamper proofing is being disabled.
        self.service_status = service_status
        # The protection status of the server. Valid values:
        # 
        # *   **on**: The server is protected.
        # *   **off**: The server is not protected.
        self.status = status
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_count is not None:
            result['AuditCount'] = self.audit_count

        if self.block_count is not None:
            result['BlockCount'] = self.block_count

        if self.dir_count is not None:
            result['DirCount'] = self.dir_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.os is not None:
            result['Os'] = self.os

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_detail is not None:
            result['ServiceDetail'] = self.service_detail

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditCount') is not None:
            self.audit_count = m.get('AuditCount')

        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')

        if m.get('DirCount') is not None:
            self.dir_count = m.get('DirCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceDetail') is not None:
            self.service_detail = m.get('ServiceDetail')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

