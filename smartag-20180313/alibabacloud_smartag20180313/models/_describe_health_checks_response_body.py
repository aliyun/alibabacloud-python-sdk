# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthChecksResponseBody(DaraModel):
    def __init__(
        self,
        health_checks: main_models.DescribeHealthChecksResponseBodyHealthChecks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.health_checks = health_checks
        # The page number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Default value: **10**. Maximum value: **50**.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.health_checks:
            self.health_checks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_checks is not None:
            result['HealthChecks'] = self.health_checks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthChecks') is not None:
            temp_model = main_models.DescribeHealthChecksResponseBodyHealthChecks()
            self.health_checks = temp_model.from_map(m.get('HealthChecks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHealthChecksResponseBodyHealthChecks(DaraModel):
    def __init__(
        self,
        health_check: List[main_models.DescribeHealthChecksResponseBodyHealthChecksHealthCheck] = None,
    ):
        self.health_check = health_check

    def validate(self):
        if self.health_check:
            for v1 in self.health_check:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HealthCheck'] = []
        if self.health_check is not None:
            for k1 in self.health_check:
                result['HealthCheck'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check = []
        if m.get('HealthCheck') is not None:
            for k1 in m.get('HealthCheck'):
                temp_model = main_models.DescribeHealthChecksResponseBodyHealthChecksHealthCheck()
                self.health_check.append(temp_model.from_map(k1))

        return self

class DescribeHealthChecksResponseBodyHealthChecksHealthCheck(DaraModel):
    def __init__(
        self,
        description: str = None,
        dst_ip_addr: str = None,
        dst_port: int = None,
        fail_count_threshold: int = None,
        hc_instance_id: str = None,
        name: str = None,
        probe_count: int = None,
        probe_interval: int = None,
        probe_timeout: int = None,
        relation_count: int = None,
        rtt_fail_threshold: int = None,
        rtt_threshold: int = None,
        smart_agid: str = None,
        src_ip_addr: str = None,
        src_port: int = None,
        status: str = None,
        type: str = None,
    ):
        self.description = description
        self.dst_ip_addr = dst_ip_addr
        self.dst_port = dst_port
        self.fail_count_threshold = fail_count_threshold
        self.hc_instance_id = hc_instance_id
        self.name = name
        self.probe_count = probe_count
        self.probe_interval = probe_interval
        self.probe_timeout = probe_timeout
        self.relation_count = relation_count
        self.rtt_fail_threshold = rtt_fail_threshold
        self.rtt_threshold = rtt_threshold
        self.smart_agid = smart_agid
        self.src_ip_addr = src_ip_addr
        self.src_port = src_port
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dst_ip_addr is not None:
            result['DstIpAddr'] = self.dst_ip_addr

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.fail_count_threshold is not None:
            result['FailCountThreshold'] = self.fail_count_threshold

        if self.hc_instance_id is not None:
            result['HcInstanceId'] = self.hc_instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.probe_count is not None:
            result['ProbeCount'] = self.probe_count

        if self.probe_interval is not None:
            result['ProbeInterval'] = self.probe_interval

        if self.probe_timeout is not None:
            result['ProbeTimeout'] = self.probe_timeout

        if self.relation_count is not None:
            result['RelationCount'] = self.relation_count

        if self.rtt_fail_threshold is not None:
            result['RttFailThreshold'] = self.rtt_fail_threshold

        if self.rtt_threshold is not None:
            result['RttThreshold'] = self.rtt_threshold

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.src_ip_addr is not None:
            result['SrcIpAddr'] = self.src_ip_addr

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DstIpAddr') is not None:
            self.dst_ip_addr = m.get('DstIpAddr')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('FailCountThreshold') is not None:
            self.fail_count_threshold = m.get('FailCountThreshold')

        if m.get('HcInstanceId') is not None:
            self.hc_instance_id = m.get('HcInstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProbeCount') is not None:
            self.probe_count = m.get('ProbeCount')

        if m.get('ProbeInterval') is not None:
            self.probe_interval = m.get('ProbeInterval')

        if m.get('ProbeTimeout') is not None:
            self.probe_timeout = m.get('ProbeTimeout')

        if m.get('RelationCount') is not None:
            self.relation_count = m.get('RelationCount')

        if m.get('RttFailThreshold') is not None:
            self.rtt_fail_threshold = m.get('RttFailThreshold')

        if m.get('RttThreshold') is not None:
            self.rtt_threshold = m.get('RttThreshold')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SrcIpAddr') is not None:
            self.src_ip_addr = m.get('SrcIpAddr')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

