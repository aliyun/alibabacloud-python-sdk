# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class DedicatedIpListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        ips: List[main_models.DedicatedIpListResponseBodyIps] = None,
        page_size: int = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # Current page
        self.current_page = current_page
        # Whether there is a next page
        self.has_more = has_more
        # IP list
        self.ips = ips
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total amount of purchased IP data
        self.total_counts = total_counts

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.DedicatedIpListResponseBodyIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class DedicatedIpListResponseBodyIps(DaraModel):
    def __init__(
        self,
        expired_time: str = None,
        id: str = None,
        instance_id: str = None,
        ip: str = None,
        ip_ext: main_models.DedicatedIpListResponseBodyIpsIpExt = None,
        ip_pool_name: str = None,
        start_time: str = None,
        status: str = None,
        warmup_status: str = None,
        warmup_type: str = None,
        zone_id: str = None,
    ):
        # Expiration time
        self.expired_time = expired_time
        # IP ID, consistent with the purchased instance ID
        self.id = id
        # Purchased instance ID
        self.instance_id = instance_id
        # IP address
        self.ip = ip
        # Extended information
        self.ip_ext = ip_ext
        # Name of the IP pool
        self.ip_pool_name = ip_pool_name
        # Purchase time
        self.start_time = start_time
        # IP status
        self.status = status
        # Warm-up status
        self.warmup_status = warmup_status
        # Warm-up method
        self.warmup_type = warmup_type
        self.zone_id = zone_id

    def validate(self):
        if self.ip_ext:
            self.ip_ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_ext is not None:
            result['IpExt'] = self.ip_ext.to_map()

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.warmup_status is not None:
            result['WarmupStatus'] = self.warmup_status

        if self.warmup_type is not None:
            result['WarmupType'] = self.warmup_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpExt') is not None:
            temp_model = main_models.DedicatedIpListResponseBodyIpsIpExt()
            self.ip_ext = temp_model.from_map(m.get('IpExt'))

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WarmupStatus') is not None:
            self.warmup_status = m.get('WarmupStatus')

        if m.get('WarmupType') is not None:
            self.warmup_type = m.get('WarmupType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DedicatedIpListResponseBodyIpsIpExt(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        has_send_mail: bool = None,
        last_warm_up_type_changed_time: str = None,
    ):
        # Whether auto-renewal is enabled
        self.auto_renewal = auto_renewal
        # Whether an email has been sent
        self.has_send_mail = has_send_mail
        self.last_warm_up_type_changed_time = last_warm_up_type_changed_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.has_send_mail is not None:
            result['HasSendMail'] = self.has_send_mail

        if self.last_warm_up_type_changed_time is not None:
            result['LastWarmUpTypeChangedTime'] = self.last_warm_up_type_changed_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('HasSendMail') is not None:
            self.has_send_mail = m.get('HasSendMail')

        if m.get('LastWarmUpTypeChangedTime') is not None:
            self.last_warm_up_type_changed_time = m.get('LastWarmUpTypeChangedTime')

        return self

