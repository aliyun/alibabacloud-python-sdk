# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeIdcProbeScanResultListResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeIdcProbeScanResultListResponseBodyInstances] = None,
        page_info: main_models.DescribeIdcProbeScanResultListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The instances.
        self.instances = instances
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeIdcProbeScanResultListResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeIdcProbeScanResultListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIdcProbeScanResultListResponseBodyPageInfo(DaraModel):
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
        # The number of entries per page.
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

class DescribeIdcProbeScanResultListResponseBodyInstances(DaraModel):
    def __init__(
        self,
        client_status: str = None,
        idc_name: str = None,
        ip_segment: str = None,
        last_scan_time: int = None,
        os: str = None,
        probe_internet_ip: str = None,
        probe_intranet_ip: str = None,
        probe_machine_name: str = None,
        probe_uuid: str = None,
        scan_result_id: int = None,
        scanned_ip: str = None,
        valid_port: str = None,
    ):
        # The status of the client of the instance on which the probe is installed. Valid values:
        # 
        # *   **online**: The Security Center agent on the asset is **enabled**.
        # *   **offline**: The Security Center agent on the asset is **disabled**.
        self.client_status = client_status
        # The name of the IDC.
        self.idc_name = idc_name
        # The CIDR blocks.
        self.ip_segment = ip_segment
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The operating system type of the asset. Valid values:
        # 
        # *   **windows**
        # *   **linux**
        self.os = os
        # The private IP address of the associated instance.
        self.probe_internet_ip = probe_internet_ip
        # The private IP address of the associated instance.
        self.probe_intranet_ip = probe_intranet_ip
        # The name of the associated instance.
        self.probe_machine_name = probe_machine_name
        # The UUID of the associated instance.
        self.probe_uuid = probe_uuid
        # The ID of the scan result.
        self.scan_result_id = scan_result_id
        # The IP address that is scanned.
        self.scanned_ip = scanned_ip
        # The port that is scanned.
        self.valid_port = valid_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.idc_name is not None:
            result['IdcName'] = self.idc_name

        if self.ip_segment is not None:
            result['IpSegment'] = self.ip_segment

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.os is not None:
            result['Os'] = self.os

        if self.probe_internet_ip is not None:
            result['ProbeInternetIp'] = self.probe_internet_ip

        if self.probe_intranet_ip is not None:
            result['ProbeIntranetIp'] = self.probe_intranet_ip

        if self.probe_machine_name is not None:
            result['ProbeMachineName'] = self.probe_machine_name

        if self.probe_uuid is not None:
            result['ProbeUuid'] = self.probe_uuid

        if self.scan_result_id is not None:
            result['ScanResultId'] = self.scan_result_id

        if self.scanned_ip is not None:
            result['ScannedIp'] = self.scanned_ip

        if self.valid_port is not None:
            result['ValidPort'] = self.valid_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('IdcName') is not None:
            self.idc_name = m.get('IdcName')

        if m.get('IpSegment') is not None:
            self.ip_segment = m.get('IpSegment')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('ProbeInternetIp') is not None:
            self.probe_internet_ip = m.get('ProbeInternetIp')

        if m.get('ProbeIntranetIp') is not None:
            self.probe_intranet_ip = m.get('ProbeIntranetIp')

        if m.get('ProbeMachineName') is not None:
            self.probe_machine_name = m.get('ProbeMachineName')

        if m.get('ProbeUuid') is not None:
            self.probe_uuid = m.get('ProbeUuid')

        if m.get('ScanResultId') is not None:
            self.scan_result_id = m.get('ScanResultId')

        if m.get('ScannedIp') is not None:
            self.scanned_ip = m.get('ScannedIp')

        if m.get('ValidPort') is not None:
            self.valid_port = m.get('ValidPort')

        return self

