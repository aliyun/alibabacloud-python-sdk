# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddIdcProbeResponseBody(DaraModel):
    def __init__(
        self,
        add_idc_probe_failed_list: List[main_models.AddIdcProbeResponseBodyAddIdcProbeFailedList] = None,
        count: str = None,
        request_id: str = None,
    ):
        # The records of failure.
        self.add_idc_probe_failed_list = add_idc_probe_failed_list
        # The total number of entries returned.
        self.count = count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.add_idc_probe_failed_list:
            for v1 in self.add_idc_probe_failed_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddIdcProbeFailedList'] = []
        if self.add_idc_probe_failed_list is not None:
            for k1 in self.add_idc_probe_failed_list:
                result['AddIdcProbeFailedList'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_idc_probe_failed_list = []
        if m.get('AddIdcProbeFailedList') is not None:
            for k1 in m.get('AddIdcProbeFailedList'):
                temp_model = main_models.AddIdcProbeResponseBodyAddIdcProbeFailedList()
                self.add_idc_probe_failed_list.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddIdcProbeResponseBodyAddIdcProbeFailedList(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        idc_name: str = None,
        idc_region: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip_segments: str = None,
        uuid: str = None,
    ):
        # The error message that is returned.
        self.error_msg = error_msg
        # The name of the data center.
        self.idc_name = idc_name
        # The region ID.
        self.idc_region = idc_region
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The settings of the CIDR block.
        self.ip_segments = ip_segments
        # The UUID of the server. Multiple UUIDs are separated by commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.idc_name is not None:
            result['IdcName'] = self.idc_name

        if self.idc_region is not None:
            result['IdcRegion'] = self.idc_region

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip_segments is not None:
            result['IpSegments'] = self.ip_segments

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('IdcName') is not None:
            self.idc_name = m.get('IdcName')

        if m.get('IdcRegion') is not None:
            self.idc_region = m.get('IdcRegion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('IpSegments') is not None:
            self.ip_segments = m.get('IpSegments')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

