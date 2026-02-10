# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAgentlessRiskUuidResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAgentlessRiskUuidResponseBodyList] = None,
        page_info: main_models.ListAgentlessRiskUuidResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the hosts.
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
                temp_model = main_models.ListAgentlessRiskUuidResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListAgentlessRiskUuidResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAgentlessRiskUuidResponseBodyPageInfo(DaraModel):
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

class ListAgentlessRiskUuidResponseBodyList(DaraModel):
    def __init__(
        self,
        baseline_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        malicious_count: int = None,
        scan_time: int = None,
        target_id: str = None,
        target_name: str = None,
        uuid: str = None,
        vul_count: int = None,
    ):
        # The number of baseline risks.
        self.baseline_count = baseline_count
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The number of malicious samples.
        self.malicious_count = malicious_count
        # The timestamp of the detection. Unit: milliseconds.
        self.scan_time = scan_time
        # The ID of the asset that is detected.
        self.target_id = target_id
        # The name of the asset that is detected.
        self.target_name = target_name
        # The UUID of the server.
        self.uuid = uuid
        # The number of detected vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_count is not None:
            result['BaselineCount'] = self.baseline_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.malicious_count is not None:
            result['MaliciousCount'] = self.malicious_count

        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineCount') is not None:
            self.baseline_count = m.get('BaselineCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MaliciousCount') is not None:
            self.malicious_count = m.get('MaliciousCount')

        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

