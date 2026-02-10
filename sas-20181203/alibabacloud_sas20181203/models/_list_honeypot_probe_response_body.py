# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotProbeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListHoneypotProbeResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListHoneypotProbeResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code that is returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code that is returned.
        self.http_status_code = http_status_code
        # An array that consists of the details about the probe.
        self.list = list
        # The message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListHoneypotProbeResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotProbeResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHoneypotProbeResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
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

class ListHoneypotProbeResponseBodyList(DaraModel):
    def __init__(
        self,
        control_node: main_models.ListHoneypotProbeResponseBodyListControlNode = None,
        deploy_time: int = None,
        display_name: str = None,
        host_ip: str = None,
        os_type: str = None,
        probe_id: str = None,
        probe_type: str = None,
        probe_version: str = None,
        status: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        # The information about the management node.
        self.control_node = control_node
        # The time when the probe was deployed.
        self.deploy_time = deploy_time
        # The name of the probe.
        self.display_name = display_name
        # The IP address of the server on which the probe is installed.
        self.host_ip = host_ip
        # The operating system of the server on which the probe is deployed. Valid values:
        # 
        # *   windows
        # *   linux
        self.os_type = os_type
        # The ID of the probe.
        self.probe_id = probe_id
        # The type of the probe. Valid values:
        # 
        # *   **host_probe**: host probe
        # *   **vpc_black_hole_probe**: VPC probe
        self.probe_type = probe_type
        # The version of the probe.
        self.probe_version = probe_version
        # The status of the probe. Valid values:
        # 
        # *   **installed**: installed
        # *   **install_failed**: installation failed
        # *   **online**: online
        # *   **offline**: offline
        # *   **unnormal**: abnormal
        # *   **unprobe**: unauthorized
        # *   **uninstalling**: being uninstalled
        # *   **uninstalled**: uninstalled
        # *   **uninstall_failed**: uninstallation failed
        # *   **not_exist**: not installed
        self.status = status
        # The UUID of the server to which the host probe is deployed.
        self.uuid = uuid
        # The ID of the VPC in which the VPC probe is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.control_node:
            self.control_node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_node is not None:
            result['ControlNode'] = self.control_node.to_map()

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        if self.probe_version is not None:
            result['ProbeVersion'] = self.probe_version

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlNode') is not None:
            temp_model = main_models.ListHoneypotProbeResponseBodyListControlNode()
            self.control_node = temp_model.from_map(m.get('ControlNode'))

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('ProbeVersion') is not None:
            self.probe_version = m.get('ProbeVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListHoneypotProbeResponseBodyListControlNode(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        node_id: str = None,
        node_name: str = None,
    ):
        # The ID of the Elastic Compute Service (ECS) instance.
        self.ecs_instance_id = ecs_instance_id
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

