# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserBuyVersionResponseBody(DaraModel):
    def __init__(
        self,
        ack_cluster_connector_quota: int = None,
        ali_uid: int = None,
        default_bandwidth: int = None,
        expire: int = None,
        extension_bandwidth: int = None,
        general_instance: int = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_bandwidth: int = None,
        ip_number: int = None,
        log_status: bool = None,
        log_storage: int = None,
        major_version: int = None,
        max_overflow: int = None,
        nat_bandwidth: int = None,
        private_dns_connector_quota: int = None,
        request_id: str = None,
        sdl: int = None,
        start_time: int = None,
        temporary_bandwidth: int = None,
        threat_intelligence: int = None,
        user_status: bool = None,
        version: int = None,
        vpc_bandwidth: int = None,
        vpc_number: int = None,
    ):
        self.ack_cluster_connector_quota = ack_cluster_connector_quota
        # The ID of the Alibaba Cloud account that is used to purchase Cloud Firewall.
        self.ali_uid = ali_uid
        self.default_bandwidth = default_bandwidth
        # The time when Cloud Firewall expires.
        # 
        # >  The value is a timestamp in milliseconds.
        # 
        # >  If you use Cloud Firewall that uses the pay-as-you-go billing method, ignore this parameter.
        self.expire = expire
        self.extension_bandwidth = extension_bandwidth
        self.general_instance = general_instance
        # The instance ID of Cloud Firewall.
        # 
        # >  If you use a trial of Cloud Firewall, ignore this parameter.
        self.instance_id = instance_id
        # The status of Cloud Firewall. Valid values:
        # 
        # *   **normal**: Cloud Firewall is running as expected.
        # *   **init**: Cloud Firewall is being initialized.
        # *   **deleting**: Cloud Firewall is being deleted.
        # *   **abnormal**: An exception occurs in Cloud Firewall.
        # *   **free**: Cloud Firewall is invalid.
        self.instance_status = instance_status
        # The peak Internet traffic that can be protected.
        self.internet_bandwidth = internet_bandwidth
        # The number of public IP addresses that can be protected.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.ip_number = ip_number
        # Indicates whether log delivery is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.log_status = log_status
        # The log storage capacity.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.log_storage = log_storage
        self.major_version = major_version
        # The status of the burstable protected traffic feature. Valid values:
        # 
        # *   **1000000**: enabled.
        # *   **0**: disabled.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.max_overflow = max_overflow
        # The peak traffic of NAT private network that can be protected.
        self.nat_bandwidth = nat_bandwidth
        self.private_dns_connector_quota = private_dns_connector_quota
        # The request ID.
        self.request_id = request_id
        self.sdl = sdl
        # The time when Cloud Firewall was activated.
        # 
        # >  The value is a timestamp in milliseconds.
        self.start_time = start_time
        self.temporary_bandwidth = temporary_bandwidth
        self.threat_intelligence = threat_intelligence
        # Indicates whether Cloud Firewall is valid. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.user_status = user_status
        # The edition of Cloud Firewall. Valid values:
        # 
        # *   **2**: Premium Edition.
        # *   **3**: Enterprise Edition.
        # *   **4**: Ultimate Edition.
        # *   **10**: Cloud Firewall that uses the pay-as-you-go billing method.
        self.version = version
        # The peak cross-VPC traffic that can be protected.
        self.vpc_bandwidth = vpc_bandwidth
        # The number of virtual private clouds (VPCs) that can be protected.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.vpc_number = vpc_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_cluster_connector_quota is not None:
            result['AckClusterConnectorQuota'] = self.ack_cluster_connector_quota

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.default_bandwidth is not None:
            result['DefaultBandwidth'] = self.default_bandwidth

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.extension_bandwidth is not None:
            result['ExtensionBandwidth'] = self.extension_bandwidth

        if self.general_instance is not None:
            result['GeneralInstance'] = self.general_instance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth

        if self.ip_number is not None:
            result['IpNumber'] = self.ip_number

        if self.log_status is not None:
            result['LogStatus'] = self.log_status

        if self.log_storage is not None:
            result['LogStorage'] = self.log_storage

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.max_overflow is not None:
            result['MaxOverflow'] = self.max_overflow

        if self.nat_bandwidth is not None:
            result['NatBandwidth'] = self.nat_bandwidth

        if self.private_dns_connector_quota is not None:
            result['PrivateDnsConnectorQuota'] = self.private_dns_connector_quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sdl is not None:
            result['Sdl'] = self.sdl

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.temporary_bandwidth is not None:
            result['TemporaryBandwidth'] = self.temporary_bandwidth

        if self.threat_intelligence is not None:
            result['ThreatIntelligence'] = self.threat_intelligence

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_bandwidth is not None:
            result['VpcBandwidth'] = self.vpc_bandwidth

        if self.vpc_number is not None:
            result['VpcNumber'] = self.vpc_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckClusterConnectorQuota') is not None:
            self.ack_cluster_connector_quota = m.get('AckClusterConnectorQuota')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DefaultBandwidth') is not None:
            self.default_bandwidth = m.get('DefaultBandwidth')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('ExtensionBandwidth') is not None:
            self.extension_bandwidth = m.get('ExtensionBandwidth')

        if m.get('GeneralInstance') is not None:
            self.general_instance = m.get('GeneralInstance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')

        if m.get('IpNumber') is not None:
            self.ip_number = m.get('IpNumber')

        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')

        if m.get('LogStorage') is not None:
            self.log_storage = m.get('LogStorage')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('MaxOverflow') is not None:
            self.max_overflow = m.get('MaxOverflow')

        if m.get('NatBandwidth') is not None:
            self.nat_bandwidth = m.get('NatBandwidth')

        if m.get('PrivateDnsConnectorQuota') is not None:
            self.private_dns_connector_quota = m.get('PrivateDnsConnectorQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sdl') is not None:
            self.sdl = m.get('Sdl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TemporaryBandwidth') is not None:
            self.temporary_bandwidth = m.get('TemporaryBandwidth')

        if m.get('ThreatIntelligence') is not None:
            self.threat_intelligence = m.get('ThreatIntelligence')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcBandwidth') is not None:
            self.vpc_bandwidth = m.get('VpcBandwidth')

        if m.get('VpcNumber') is not None:
            self.vpc_number = m.get('VpcNumber')

        return self

