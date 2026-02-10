# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAlarmEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAlarmEventDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the alert event.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAlarmEventDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAlarmEventDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_event_alias_name: str = None,
        alarm_event_desc: str = None,
        alarm_unique_info: str = None,
        app_name: str = None,
        can_be_deal_on_line: bool = None,
        can_cancel_fault: bool = None,
        cause_details: List[main_models.DescribeAlarmEventDetailResponseBodyDataCauseDetails] = None,
        contain_hw_mode: bool = None,
        container_id: str = None,
        container_image_id: str = None,
        container_image_name: str = None,
        data_source: str = None,
        end_time: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        k_8s_cluster_id: str = None,
        k_8s_cluster_name: str = None,
        k_8s_namespace: str = None,
        k_8s_node_id: str = None,
        k_8s_node_name: str = None,
        k_8s_pod_name: str = None,
        level: str = None,
        solution: str = None,
        start_time: int = None,
        type: str = None,
        uuid: str = None,
    ):
        # The name of the alert event.
        self.alarm_event_alias_name = alarm_event_alias_name
        # The description of the alert event.
        self.alarm_event_desc = alarm_event_desc
        # The unique identifier of the alert event.
        # 
        # > To query the details of an alert event, you must provide the unique identifier of the alert event. You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to obtain the identifier.
        self.alarm_unique_info = alarm_unique_info
        # The name of the container application.
        self.app_name = app_name
        # Indicates whether the online handling of the alert event is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.can_be_deal_on_line = can_be_deal_on_line
        # Indicates whether you can cancel marking the alert event as a false positive. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.can_cancel_fault = can_cancel_fault
        # An array consisting of the cause of the alert event, which can be used to trace the alert event.
        self.cause_details = cause_details
        # Indicates whether the Safeguard Mode For Major Activities mode is enabled.
        self.contain_hw_mode = contain_hw_mode
        # The ID of the container application.
        self.container_id = container_id
        # The ID of the image to which the container belongs.
        self.container_image_id = container_image_id
        # The name of the image to which the container belongs.
        self.container_image_name = container_image_name
        # The data source of the alert event.
        self.data_source = data_source
        # The timestamp when the alert event ends. Unit: milliseconds.
        self.end_time = end_time
        # The name of the instance.
        self.instance_name = instance_name
        # The public IP address of the associated instance.
        self.internet_ip = internet_ip
        # The private IP address of the associated instance.
        self.intranet_ip = intranet_ip
        # The ID of the Kubernetes cluster.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The name of the Kubernetes cluster.
        self.k_8s_cluster_name = k_8s_cluster_name
        # The namespace of the Kubernetes cluster.
        self.k_8s_namespace = k_8s_namespace
        # The ID of the Kubernetes cluster node.
        self.k_8s_node_id = k_8s_node_id
        # The name of the Kubernetes cluster node.
        self.k_8s_node_name = k_8s_node_name
        # The name of the Kubernetes pod.
        self.k_8s_pod_name = k_8s_pod_name
        # The severity of the alert event. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The solution to the alert event.
        self.solution = solution
        # The timestamp when the alert event starts. Unit: milliseconds.
        self.start_time = start_time
        # The alert type of the alert event. Valid values:
        # 
        # *   Suspicious process
        # *   Webshell
        # *   Unusual logon
        # *   Exception
        # *   Sensitive file tampering
        # *   Malicious process (cloud threat detection)
        # *   Suspicious network connection
        # *   Other
        # *   Abnormal account
        # *   Application intrusion event
        # *   Cloud threat detection
        # *   Precise defense
        # *   Application whitelist
        # *   Persistent webshell
        # *   Web application threat detection
        # *   Malicious script
        # *   Threat intelligence
        # *   Malicious network activity
        # *   Cluster exception
        # *   Webshell (on-premises threat detection)
        # *   Vulnerability exploitation
        # *   Malicious process (on-premises threat detection)
        # *   Trusted exception
        self.type = type
        # The instance UUID of the asset.
        self.uuid = uuid

    def validate(self):
        if self.cause_details:
            for v1 in self.cause_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_alias_name is not None:
            result['AlarmEventAliasName'] = self.alarm_event_alias_name

        if self.alarm_event_desc is not None:
            result['AlarmEventDesc'] = self.alarm_event_desc

        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line

        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault

        result['CauseDetails'] = []
        if self.cause_details is not None:
            for k1 in self.cause_details:
                result['CauseDetails'].append(k1.to_map() if k1 else None)

        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id

        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id

        if self.k_8s_cluster_name is not None:
            result['K8sClusterName'] = self.k_8s_cluster_name

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id

        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name

        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name

        if self.level is not None:
            result['Level'] = self.level

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventAliasName') is not None:
            self.alarm_event_alias_name = m.get('AlarmEventAliasName')

        if m.get('AlarmEventDesc') is not None:
            self.alarm_event_desc = m.get('AlarmEventDesc')

        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')

        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')

        self.cause_details = []
        if m.get('CauseDetails') is not None:
            for k1 in m.get('CauseDetails'):
                temp_model = main_models.DescribeAlarmEventDetailResponseBodyDataCauseDetails()
                self.cause_details.append(temp_model.from_map(k1))

        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')

        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')

        if m.get('K8sClusterName') is not None:
            self.k_8s_cluster_name = m.get('K8sClusterName')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')

        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')

        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeAlarmEventDetailResponseBodyDataCauseDetails(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[main_models.DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue] = None,
    ):
        # The key that is used to trace the alert event.
        self.key = key
        # The value that is used to trace the alert event.
        self.value = value

    def validate(self):
        if self.value:
            for v1 in self.value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        result['Value'] = []
        if self.value is not None:
            for k1 in self.value:
                result['Value'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.value = []
        if m.get('Value') is not None:
            for k1 in m.get('Value'):
                temp_model = main_models.DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue()
                self.value.append(temp_model.from_map(k1))

        return self

class DescribeAlarmEventDetailResponseBodyDataCauseDetailsValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the field that displays the tracing information.
        self.name = name
        # The type of the field that displays the tracing information. Valid values:
        # 
        # *   **text**
        # *   **html**
        self.type = type
        # The value of the field that displays the tracing information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

