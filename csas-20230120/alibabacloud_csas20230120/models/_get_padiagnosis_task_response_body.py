# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetPADiagnosisTaskResponseBody(DaraModel):
    def __init__(
        self,
        diagnosis_task: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTask = None,
        request_id: str = None,
    ):
        self.diagnosis_task = diagnosis_task
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.diagnosis_task:
            self.diagnosis_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis_task is not None:
            result['DiagnosisTask'] = self.diagnosis_task.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisTask') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTask()
            self.diagnosis_task = temp_model.from_map(m.get('DiagnosisTask'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dev_tag: str = None,
        diagnose_id: str = None,
        diagnose_type: str = None,
        host: str = None,
        pop_id: str = None,
        pop_mode: str = None,
        port: str = None,
        protocol: str = None,
        result: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResult = None,
        status: str = None,
        udp_extra_configs: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs = None,
        user_group: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskUserGroup = None,
        username: str = None,
    ):
        self.create_time = create_time
        self.dev_tag = dev_tag
        self.diagnose_id = diagnose_id
        self.diagnose_type = diagnose_type
        self.host = host
        self.pop_id = pop_id
        self.pop_mode = pop_mode
        self.port = port
        self.protocol = protocol
        self.result = result
        self.status = status
        self.udp_extra_configs = udp_extra_configs
        self.user_group = user_group
        self.username = username

    def validate(self):
        if self.result:
            self.result.validate()
        if self.udp_extra_configs:
            self.udp_extra_configs.validate()
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.host is not None:
            result['Host'] = self.host

        if self.pop_id is not None:
            result['PopId'] = self.pop_id

        if self.pop_mode is not None:
            result['PopMode'] = self.pop_mode

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.udp_extra_configs is not None:
            result['UdpExtraConfigs'] = self.udp_extra_configs.to_map()

        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('PopId') is not None:
            self.pop_id = m.get('PopId')

        if m.get('PopMode') is not None:
            self.pop_mode = m.get('PopMode')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Result') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UdpExtraConfigs') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs()
            self.udp_extra_configs = temp_model.from_map(m.get('UdpExtraConfigs'))

        if m.get('UserGroup') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskUserGroup()
            self.user_group = temp_model.from_map(m.get('UserGroup'))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskUserGroup(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs(DaraModel):
    def __init__(
        self,
        expected_response: str = None,
        request_content: str = None,
    ):
        self.expected_response = expected_response
        self.request_content = request_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response

        if self.request_content is not None:
            result['RequestContent'] = self.request_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')

        if m.get('RequestContent') is not None:
            self.request_content = m.get('RequestContent')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResult(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        flow_id: str = None,
        network_link_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfo = None,
        policy_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfo = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.flow_id = flow_id
        self.network_link_info = network_link_info
        self.policy_info = policy_info
        self.success = success

    def validate(self):
        if self.network_link_info:
            self.network_link_info.validate()
        if self.policy_info:
            self.policy_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.network_link_info is not None:
            result['NetworkLinkInfo'] = self.network_link_info.to_map()

        if self.policy_info is not None:
            result['PolicyInfo'] = self.policy_info.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('NetworkLinkInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfo()
            self.network_link_info = temp_model.from_map(m.get('NetworkLinkInfo'))

        if m.get('PolicyInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfo()
            self.policy_info = temp_model.from_map(m.get('PolicyInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfo(DaraModel):
    def __init__(
        self,
        device_attribute_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoDeviceAttributeInfo = None,
        process_time: int = None,
        route_strategy_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoRouteStrategyInfo = None,
        user_group_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoUserGroupInfo = None,
        zero_trust_policy_info: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoZeroTrustPolicyInfo = None,
    ):
        self.device_attribute_info = device_attribute_info
        self.process_time = process_time
        self.route_strategy_info = route_strategy_info
        self.user_group_info = user_group_info
        self.zero_trust_policy_info = zero_trust_policy_info

    def validate(self):
        if self.device_attribute_info:
            self.device_attribute_info.validate()
        if self.route_strategy_info:
            self.route_strategy_info.validate()
        if self.user_group_info:
            self.user_group_info.validate()
        if self.zero_trust_policy_info:
            self.zero_trust_policy_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_attribute_info is not None:
            result['DeviceAttributeInfo'] = self.device_attribute_info.to_map()

        if self.process_time is not None:
            result['ProcessTime'] = self.process_time

        if self.route_strategy_info is not None:
            result['RouteStrategyInfo'] = self.route_strategy_info.to_map()

        if self.user_group_info is not None:
            result['UserGroupInfo'] = self.user_group_info.to_map()

        if self.zero_trust_policy_info is not None:
            result['ZeroTrustPolicyInfo'] = self.zero_trust_policy_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceAttributeInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoDeviceAttributeInfo()
            self.device_attribute_info = temp_model.from_map(m.get('DeviceAttributeInfo'))

        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')

        if m.get('RouteStrategyInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoRouteStrategyInfo()
            self.route_strategy_info = temp_model.from_map(m.get('RouteStrategyInfo'))

        if m.get('UserGroupInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoUserGroupInfo()
            self.user_group_info = temp_model.from_map(m.get('UserGroupInfo'))

        if m.get('ZeroTrustPolicyInfo') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoZeroTrustPolicyInfo()
            self.zero_trust_policy_info = temp_model.from_map(m.get('ZeroTrustPolicyInfo'))

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoZeroTrustPolicyInfo(DaraModel):
    def __init__(
        self,
        action: str = None,
        app_name: str = None,
        block_info: str = None,
        policy_name: str = None,
    ):
        self.action = action
        self.app_name = app_name
        self.block_info = block_info
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.block_info is not None:
            result['BlockInfo'] = self.block_info

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BlockInfo') is not None:
            self.block_info = m.get('BlockInfo')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoUserGroupInfo(DaraModel):
    def __init__(
        self,
        email: str = None,
        group: List[str] = None,
        matched_user_groups: str = None,
        telephone: str = None,
        username: str = None,
    ):
        self.email = email
        self.group = group
        self.matched_user_groups = matched_user_groups
        self.telephone = telephone
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.group is not None:
            result['Group'] = self.group

        if self.matched_user_groups is not None:
            result['MatchedUserGroups'] = self.matched_user_groups

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('MatchedUserGroups') is not None:
            self.matched_user_groups = m.get('MatchedUserGroups')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoRouteStrategyInfo(DaraModel):
    def __init__(
        self,
        route_type: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
    ):
        self.route_type = route_type
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultPolicyInfoDeviceAttributeInfo(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        device_type: str = None,
        file: List[str] = None,
        firewall: str = None,
        hostname: str = None,
        inner_ip: str = None,
        internet_ip: str = None,
        mac: str = None,
        matched_security_baseline: str = None,
        process: List[str] = None,
        ssid: str = None,
    ):
        self.dev_tag = dev_tag
        self.device_type = device_type
        self.file = file
        self.firewall = firewall
        self.hostname = hostname
        self.inner_ip = inner_ip
        self.internet_ip = internet_ip
        self.mac = mac
        self.matched_security_baseline = matched_security_baseline
        self.process = process
        # SSID。
        self.ssid = ssid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.file is not None:
            result['File'] = self.file

        if self.firewall is not None:
            result['Firewall'] = self.firewall

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.matched_security_baseline is not None:
            result['MatchedSecurityBaseline'] = self.matched_security_baseline

        if self.process is not None:
            result['Process'] = self.process

        if self.ssid is not None:
            result['Ssid'] = self.ssid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('Firewall') is not None:
            self.firewall = m.get('Firewall')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('MatchedSecurityBaseline') is not None:
            self.matched_security_baseline = m.get('MatchedSecurityBaseline')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfo(DaraModel):
    def __init__(
        self,
        dns: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDns = None,
        fbt: str = None,
        links: List[main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinks] = None,
        nodes: List[main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodes] = None,
    ):
        self.dns = dns
        self.fbt = fbt
        self.links = links
        self.nodes = nodes

    def validate(self):
        if self.dns:
            self.dns.validate()
        if self.links:
            for v1 in self.links:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns is not None:
            result['Dns'] = self.dns.to_map()

        if self.fbt is not None:
            result['FBT'] = self.fbt

        result['Links'] = []
        if self.links is not None:
            for k1 in self.links:
                result['Links'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDns()
            self.dns = temp_model.from_map(m.get('Dns'))

        if m.get('FBT') is not None:
            self.fbt = m.get('FBT')

        self.links = []
        if m.get('Links') is not None:
            for k1 in m.get('Links'):
                temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinks()
                self.links.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodes(DaraModel):
    def __init__(
        self,
        address: str = None,
        cloud_net_id: str = None,
        error: str = None,
        geo_data: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodesGeoData = None,
        id: int = None,
        name: str = None,
        name_en: str = None,
        node_type: str = None,
        resource_id: str = None,
        success: bool = None,
    ):
        self.address = address
        self.cloud_net_id = cloud_net_id
        self.error = error
        self.geo_data = geo_data
        self.id = id
        self.name = name
        self.name_en = name_en
        self.node_type = node_type
        self.resource_id = resource_id
        self.success = success

    def validate(self):
        if self.geo_data:
            self.geo_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.cloud_net_id is not None:
            result['CloudNetId'] = self.cloud_net_id

        if self.error is not None:
            result['Error'] = self.error

        if self.geo_data is not None:
            result['GeoData'] = self.geo_data.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.name_en is not None:
            result['NameEn'] = self.name_en

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('CloudNetId') is not None:
            self.cloud_net_id = m.get('CloudNetId')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('GeoData') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodesGeoData()
            self.geo_data = temp_model.from_map(m.get('GeoData'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoNodesGeoData(DaraModel):
    def __init__(
        self,
        city: str = None,
        country: str = None,
        isp: str = None,
        prov: str = None,
    ):
        self.city = city
        self.country = country
        self.isp = isp
        self.prov = prov

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.prov is not None:
            result['Prov'] = self.prov

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Prov') is not None:
            self.prov = m.get('Prov')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinks(DaraModel):
    def __init__(
        self,
        error: str = None,
        from_node: int = None,
        hops: List[main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHops] = None,
        latency: str = None,
        success: bool = None,
        to_node: int = None,
    ):
        self.error = error
        self.from_node = from_node
        self.hops = hops
        self.latency = latency
        self.success = success
        self.to_node = to_node

    def validate(self):
        if self.hops:
            for v1 in self.hops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.from_node is not None:
            result['FromNode'] = self.from_node

        result['Hops'] = []
        if self.hops is not None:
            for k1 in self.hops:
                result['Hops'].append(k1.to_map() if k1 else None)

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.success is not None:
            result['Success'] = self.success

        if self.to_node is not None:
            result['ToNode'] = self.to_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('FromNode') is not None:
            self.from_node = m.get('FromNode')

        self.hops = []
        if m.get('Hops') is not None:
            for k1 in m.get('Hops'):
                temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHops()
                self.hops.append(temp_model.from_map(k1))

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('ToNode') is not None:
            self.to_node = m.get('ToNode')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHops(DaraModel):
    def __init__(
        self,
        address: str = None,
        geo_data: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHopsGeoData = None,
        latency: str = None,
        ttl: str = None,
    ):
        self.address = address
        self.geo_data = geo_data
        self.latency = latency
        # TTL。
        self.ttl = ttl

    def validate(self):
        if self.geo_data:
            self.geo_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.geo_data is not None:
            result['GeoData'] = self.geo_data.to_map()

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.ttl is not None:
            result['TTL'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('GeoData') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHopsGeoData()
            self.geo_data = temp_model.from_map(m.get('GeoData'))

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoLinksHopsGeoData(DaraModel):
    def __init__(
        self,
        city: str = None,
        country: str = None,
        isp: str = None,
        prov: str = None,
    ):
        self.city = city
        self.country = country
        self.isp = isp
        self.prov = prov

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.prov is not None:
            result['Prov'] = self.prov

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Prov') is not None:
            self.prov = m.get('Prov')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDns(DaraModel):
    def __init__(
        self,
        dns_server: str = None,
        dns_type: str = None,
        error: str = None,
        from_node: int = None,
        hops: List[List[main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHops]] = None,
        latency: str = None,
        result: str = None,
        success: bool = None,
        to_node: int = None,
    ):
        self.dns_server = dns_server
        self.dns_type = dns_type
        self.error = error
        self.from_node = from_node
        self.hops = hops
        self.latency = latency
        self.result = result
        self.success = success
        self.to_node = to_node

    def validate(self):
        if self.hops:
            for v1 in self.hops:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server

        if self.dns_type is not None:
            result['DnsType'] = self.dns_type

        if self.error is not None:
            result['Error'] = self.error

        if self.from_node is not None:
            result['FromNode'] = self.from_node

        result['Hops'] = []
        if self.hops is not None:
            for k1 in self.hops:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['Hops'].append(l1)

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.result is not None:
            result['Result'] = self.result

        if self.success is not None:
            result['Success'] = self.success

        if self.to_node is not None:
            result['ToNode'] = self.to_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')

        if m.get('DnsType') is not None:
            self.dns_type = m.get('DnsType')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('FromNode') is not None:
            self.from_node = m.get('FromNode')

        self.hops = []
        if m.get('Hops') is not None:
            for k1 in m.get('Hops'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHops()
                    l1.append(temp_model.from_map(k2))
                self.hops.append(l1)

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('ToNode') is not None:
            self.to_node = m.get('ToNode')

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHops(DaraModel):
    def __init__(
        self,
        address: str = None,
        ttl: str = None,
        latency: str = None,
        geo_data: main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHopsGeoData = None,
    ):
        self.address = address
        # TTL。
        self.ttl = ttl
        self.latency = latency
        self.geo_data = geo_data

    def validate(self):
        if self.geo_data:
            self.geo_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.geo_data is not None:
            result['GeoData'] = self.geo_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('GeoData') is not None:
            temp_model = main_models.GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHopsGeoData()
            self.geo_data = temp_model.from_map(m.get('GeoData'))

        return self

class GetPADiagnosisTaskResponseBodyDiagnosisTaskResultNetworkLinkInfoDnsHopsGeoData(DaraModel):
    def __init__(
        self,
        country: str = None,
        prov: str = None,
        city: str = None,
        isp: str = None,
    ):
        self.country = country
        self.prov = prov
        self.city = city
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country is not None:
            result['Country'] = self.country

        if self.prov is not None:
            result['Prov'] = self.prov

        if self.city is not None:
            result['City'] = self.city

        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Prov') is not None:
            self.prov = m.get('Prov')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

