# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHealthCheckAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        dst_ip_addr: str = None,
        dst_port: int = None,
        fail_count_threshold: int = None,
        hc_instance_id: str = None,
        name: str = None,
        probe_count: int = None,
        probe_interval: int = None,
        probe_timeout: int = None,
        request_id: str = None,
        rtt_fail_threshold: int = None,
        rtt_threshold: int = None,
        smart_agid: str = None,
        src_ip_addr: str = None,
        src_port: int = None,
        type: str = None,
    ):
        # The time when the health check instance was created. This value is a UNIX timestamp.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The description of the health check instance.
        self.description = description
        # The destination IP address of the health check.
        self.dst_ip_addr = dst_ip_addr
        # The destination port of the health check instance.
        # 
        # >  This feature is not supported.
        self.dst_port = dst_port
        # The maximum number of failed probes before the health check is declared failed.
        # 
        # Valid values: **1** to **15**.
        # 
        # Default value: **3**.
        self.fail_count_threshold = fail_count_threshold
        # The ID of the health check instance.
        self.hc_instance_id = hc_instance_id
        # The name of the health check instance.
        self.name = name
        # The number of probes performed per health check.
        # 
        # Valid values: **1** to **20**.
        # 
        # Default value: **1**.
        self.probe_count = probe_count
        # The time interval at which probes are performed. The next probe does not start before the current one is complete.
        # 
        # Valid values: **1000** to **60000**.
        # 
        # Default value: **2000**.
        # 
        # Unit: milliseconds.
        self.probe_interval = probe_interval
        # The timeout period of the probe.
        # 
        # Valid values: **10** to **30000**.
        # 
        # Default value: **1000**.
        # 
        # Unit: milliseconds.
        self.probe_timeout = probe_timeout
        # The ID of the request.
        self.request_id = request_id
        # The number of times that the maximum RTT is exceeded before an alert is triggered.
        # 
        # Valid values: **1** to **15**.
        # 
        # Default value: **3**.
        self.rtt_fail_threshold = rtt_fail_threshold
        # The maximum round-trip time (RTT).
        # 
        # Value values: **-1** and **1** to **5000**.
        # 
        # Default value: **-1**. This value indicates that the RTT threshold is not specified.
        self.rtt_threshold = rtt_threshold
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The source IP address of the health check.
        self.src_ip_addr = src_ip_addr
        # The source port of the health check instance.
        # 
        # >  This feature is not supported.
        self.src_port = src_port
        # The type of packets used in the health check.
        # 
        # Only **ICMP_ECHO** is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

