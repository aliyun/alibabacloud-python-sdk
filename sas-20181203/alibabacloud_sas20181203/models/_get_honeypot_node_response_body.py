# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetHoneypotNodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        honeypot_node: main_models.GetHoneypotNodeResponseBodyHoneypotNode = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The details of the management node.
        self.honeypot_node = honeypot_node
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.honeypot_node:
            self.honeypot_node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.honeypot_node is not None:
            result['HoneypotNode'] = self.honeypot_node.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HoneypotNode') is not None:
            temp_model = main_models.GetHoneypotNodeResponseBodyHoneypotNode()
            self.honeypot_node = temp_model.from_map(m.get('HoneypotNode'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHoneypotNodeResponseBodyHoneypotNode(DaraModel):
    def __init__(
        self,
        allow_honeypot_access_internet: bool = None,
        create_time: str = None,
        ecs_instance_id: str = None,
        honeypot_total_count: int = None,
        honeypot_used_count: int = None,
        node_id: str = None,
        node_ip: str = None,
        node_name: str = None,
        probe_total_count: int = None,
        probe_used_count: int = None,
        security_group_probe_ip_list: List[str] = None,
        total_status: int = None,
        upgrade_available: bool = None,
    ):
        # Indicates whether a honeypot is allowed to access the Internet. Valid values:
        # 
        # *   **true**: The honeypot is allowed to access the Internet.
        # *   **false**: The honeypot is not allowed to access the Internet.
        self.allow_honeypot_access_internet = allow_honeypot_access_internet
        # The time when the management node was created.
        self.create_time = create_time
        # The ID of the instance.
        self.ecs_instance_id = ecs_instance_id
        # The maximum number of honeypots that can be deployed to the management node.
        self.honeypot_total_count = honeypot_total_count
        # The number of honeypots that are deployed to the management node.
        self.honeypot_used_count = honeypot_used_count
        # The ID of the management node.
        self.node_id = node_id
        # The IP address of the management node.
        self.node_ip = node_ip
        # The name of the management node.
        self.node_name = node_name
        # The maximum number of probes that can be deployed for the management node.
        self.probe_total_count = probe_total_count
        # The number of probes that are deployed for the management node.
        self.probe_used_count = probe_used_count
        # An array consisting of the CIDR blocks that are allowed to access the management node.
        self.security_group_probe_ip_list = security_group_probe_ip_list
        # The status of the management node. Valid values:
        # 
        # *   **0**: preparing
        # *   **1**: normal
        # *   **2**: abnormal
        # *   **4**: starting
        # *   **5**: upgrading
        self.total_status = total_status
        # Indicates whether the management node can be upgraded. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.upgrade_available = upgrade_available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_honeypot_access_internet is not None:
            result['AllowHoneypotAccessInternet'] = self.allow_honeypot_access_internet

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.honeypot_total_count is not None:
            result['HoneypotTotalCount'] = self.honeypot_total_count

        if self.honeypot_used_count is not None:
            result['HoneypotUsedCount'] = self.honeypot_used_count

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.probe_total_count is not None:
            result['ProbeTotalCount'] = self.probe_total_count

        if self.probe_used_count is not None:
            result['ProbeUsedCount'] = self.probe_used_count

        if self.security_group_probe_ip_list is not None:
            result['SecurityGroupProbeIpList'] = self.security_group_probe_ip_list

        if self.total_status is not None:
            result['TotalStatus'] = self.total_status

        if self.upgrade_available is not None:
            result['UpgradeAvailable'] = self.upgrade_available

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowHoneypotAccessInternet') is not None:
            self.allow_honeypot_access_internet = m.get('AllowHoneypotAccessInternet')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('HoneypotTotalCount') is not None:
            self.honeypot_total_count = m.get('HoneypotTotalCount')

        if m.get('HoneypotUsedCount') is not None:
            self.honeypot_used_count = m.get('HoneypotUsedCount')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ProbeTotalCount') is not None:
            self.probe_total_count = m.get('ProbeTotalCount')

        if m.get('ProbeUsedCount') is not None:
            self.probe_used_count = m.get('ProbeUsedCount')

        if m.get('SecurityGroupProbeIpList') is not None:
            self.security_group_probe_ip_list = m.get('SecurityGroupProbeIpList')

        if m.get('TotalStatus') is not None:
            self.total_status = m.get('TotalStatus')

        if m.get('UpgradeAvailable') is not None:
            self.upgrade_available = m.get('UpgradeAvailable')

        return self

