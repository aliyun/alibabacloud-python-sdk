# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotEventFlowsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        honeypot_event_flows: List[main_models.ListHoneypotEventFlowsResponseBodyHoneypotEventFlows] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: main_models.ListHoneypotEventFlowsResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The attack timelines.
        self.honeypot_event_flows = honeypot_event_flows
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.honeypot_event_flows:
            for v1 in self.honeypot_event_flows:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['HoneypotEventFlows'] = []
        if self.honeypot_event_flows is not None:
            for k1 in self.honeypot_event_flows:
                result['HoneypotEventFlows'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.honeypot_event_flows = []
        if m.get('HoneypotEventFlows') is not None:
            for k1 in m.get('HoneypotEventFlows'):
                temp_model = main_models.ListHoneypotEventFlowsResponseBodyHoneypotEventFlows()
                self.honeypot_event_flows.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotEventFlowsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHoneypotEventFlowsResponseBodyPageInfo(DaraModel):
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

class ListHoneypotEventFlowsResponseBodyHoneypotEventFlows(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        docker_id: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        event_connection: str = None,
        extra: str = None,
        extra_1: str = None,
        file_oss_url: str = None,
        first_time: int = None,
        honeypot_event_id: str = None,
        honeypot_id: str = None,
        honeypot_name: str = None,
        last_time: int = None,
        risk_level: str = None,
        security_event_id: int = None,
        src_ip: str = None,
        src_mac: str = None,
        src_port: int = None,
        status: int = None,
        type_id: str = None,
        uid: str = None,
    ):
        # The ID of the probe.
        self.agent_id = agent_id
        # The name of the probe.
        self.agent_name = agent_name
        # The ID of the container.
        self.docker_id = docker_id
        # The destination IP address.
        self.dst_ip = dst_ip
        # The destination port.
        self.dst_port = dst_port
        # The UUID of the connection in the attack.
        self.event_connection = event_connection
        # The extended information about the attack payload.
        self.extra = extra
        # The extension information about the virtual private cloud (VPC).
        self.extra_1 = extra_1
        # The Object Storage Service (OSS) URL of the file.
        self.file_oss_url = file_oss_url
        # The timestamp when the intrusion event was first occurred.
        self.first_time = first_time
        # The ID of the intrusion event. The value is a string.
        self.honeypot_event_id = honeypot_event_id
        # The ID of the honeypot.
        self.honeypot_id = honeypot_id
        # The name of the honeypot.
        self.honeypot_name = honeypot_name
        # The timestamp when the intrusion event was last occurred.
        self.last_time = last_time
        # The risk level. Valid values:
        # 
        # *   **2**: low
        # *   **3**: medium
        # *   **4**: high
        self.risk_level = risk_level
        # The ID of the intrusion event.
        self.security_event_id = security_event_id
        # The source IP address.
        self.src_ip = src_ip
        # The source media access control (MAC) address.
        self.src_mac = src_mac
        # The source port number.
        self.src_port = src_port
        # The handling status of the intrusion event. Valid values:
        # 
        # *   **1**: pending handling
        # *   **2**: ignored
        # *   **4**: confirmed
        self.status = status
        # The ID of the attack type.
        self.type_id = type_id
        # The UUID of an attack in the intrusion event.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.docker_id is not None:
            result['DockerId'] = self.docker_id

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.event_connection is not None:
            result['EventConnection'] = self.event_connection

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.extra_1 is not None:
            result['Extra1'] = self.extra_1

        if self.file_oss_url is not None:
            result['FileOssUrl'] = self.file_oss_url

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.honeypot_event_id is not None:
            result['HoneypotEventId'] = self.honeypot_event_id

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.src_mac is not None:
            result['SrcMac'] = self.src_mac

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.status is not None:
            result['Status'] = self.status

        if self.type_id is not None:
            result['TypeId'] = self.type_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('DockerId') is not None:
            self.docker_id = m.get('DockerId')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('EventConnection') is not None:
            self.event_connection = m.get('EventConnection')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Extra1') is not None:
            self.extra_1 = m.get('Extra1')

        if m.get('FileOssUrl') is not None:
            self.file_oss_url = m.get('FileOssUrl')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('HoneypotEventId') is not None:
            self.honeypot_event_id = m.get('HoneypotEventId')

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('SrcMac') is not None:
            self.src_mac = m.get('SrcMac')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

