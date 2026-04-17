# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartInstanceRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        cross_zone: bool = None,
        deploy_module: str = None,
        instance_id: str = None,
        is_eip_inner: bool = None,
        is_force_selected_zones: bool = None,
        is_set_user_and_password: bool = None,
        kmskey_id: str = None,
        name: str = None,
        notifier: str = None,
        password: str = None,
        region_id: str = None,
        security_group: str = None,
        selected_zones: str = None,
        service_version: str = None,
        user_phone_num: str = None,
        username: str = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The initial configurations of the ApsaraMQ for Kafka instance. The values must be valid JSON strings. If you do not specify this parameter, it is left empty.
        # 
        # > - You cannot configure this parameter when you deploy an ApsaraMQ for Confluent instance.
        # > - You cannot configure enable.acl for instances whose versions are earlier than 2.2.0.
        # 
        # The **Config** parameter supports the following parameters:
        # 
        # *   **enable.vpc_sasl_ssl**: specifies whether to enable VPC transmission encryption. Valid values:
        # 
        #     *   **true**: enables VPC transmission encryption. If you enable VPC transmission encryption, you must also enable access control list (ACL).
        #     *   **false**: disables VPC transmission encryption. This is the default value.
        # 
        # *   **enable.acl**: specifies whether to enable ACL. Valid values:
        # 
        #     *   **true**: enables ACL.
        #     *   **false**: disables the ACL feature. This is the default value.
        # 
        # *   **kafka.log.retention.hours**: the maximum message retention period when the disk capacity is sufficient. Unit: hours. Valid values: 24 to 480. Default value: **72**. When the disk usage reaches 85%, the disk capacity is insufficient. In this case, the system deletes the earliest stored messages to ensure service availability.
        # 
        # *   **kafka.message.max.bytes**: the maximum size of a message that can be sent and received by ApsaraMQ for Kafka. Unit: bytes. Valid values: 1048576 to 10485760. Default value: **1048576**. Before you change the maximum message size to a new value, make sure that the new value matches the configurations of the producers and consumers.
        self.config = config
        # Specifies whether cross-zone deployment is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.cross_zone = cross_zone
        # The deployment mode. If the instance is an ApsaraMQ for Kafka V2 instance, this parameter is required. If the instance is an ApsaraMQ for Kafka V3 instance or an ApsaraMQ for Confluent instance, this parameter is optional. Valid values:
        # 
        # *   **vpc**: deploys the instance in a virtual private cloud (VPC).
        # *   **eip**: deploys the instance over the Internet and in the VPC.
        # 
        # The deployment mode of the ApsaraMQ for Kafka instance must be consistent with the instance type. If the instance is a VPC-connected instance, set this parameter to **vpc**. If the instance is an Internet- and VPC-connected instance, set this parameter to **eip**.
        self.deploy_module = deploy_module
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the instance supports elastic IP addresses (EIPs). Valid values:
        # 
        # *   **true**: supports EIPs and allows access from the Internet and a VPC.
        # *   **false**: does not support EIPs and allows access only from a VPC.
        # 
        # The value of this parameter must match the type of the instance. For example, if the instance allows access only from a VPC, set this parameter to **false**.
        self.is_eip_inner = is_eip_inner
        # Specifies whether to forcibly deploy the instance in the selected zones.
        self.is_force_selected_zones = is_force_selected_zones
        # Specifies whether to set a new username and password. Valid values:
        # 
        # *   **true**: sets a new username and password.
        # *   **false**: does not set a new username or password.
        # 
        # This parameter is available only if you deploy an instance that allows access from the Internet and a VPC.
        self.is_set_user_and_password = is_set_user_and_password
        # The ID of the key that is used for disk encryption in the region where the instance is deployed. You can obtain the ID of the key in the [Key Management Service (KMS) console](https://kms.console.aliyun.com/?spm=a2c4g.11186623.2.5.336745b8hfiU21) or create a key. For more information, see [Manage CMKs](https://help.aliyun.com/document_detail/181610.html).
        # 
        # If this parameter is configured, disk encryption is enabled for the instance. You cannot disable disk encryption after disk encryption is enabled. When you call this operation, the system checks whether the AliyunServiceRoleForAlikafkaInstanceEncryption service-linked role is created. If the role is not created, the system automatically creates the role. For more information, see [Service-linked roles](https://help.aliyun.com/document_detail/190460.html).
        # 
        # > When you deploy a serverless ApsaraMQ for Kafka V3 instance, you cannot configure this parameter.
        self.kmskey_id = kmskey_id
        # The name of the instance.
        # 
        # >  If you specify a value for this parameter, make sure that the specified value is unique in the region of the instance.
        self.name = name
        # The alert contact.
        self.notifier = notifier
        # The instance password.
        # 
        # *   This parameter is available only for Internet- and VPC- connected ApsaraMQ for Kafka V2 and V3 instances.
        # *   If the instance is an ApsaraMQ for Confluent instance, this parameter is required. The value of this parameter must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & \\* () _ + - =
        self.password = password
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The security group of the instance.
        # 
        # If you do not specify this parameter, ApsaraMQ for Kafka automatically configures a security group for your instance. If you specify this parameter, you must create a security group in advance. For more information, see [Create a security group](https://help.aliyun.com/document_detail/25468.html).
        self.security_group = security_group
        # The two-dimensional arrays that consist of the candidate set for primary zones and the candidate set for secondary zones. Custom code in the `zone {zone}` format and standard code in the `cn-RegionID-{zone}` format are supported.
        # 
        # *   If you set CrossZone to true and specify Zone H and Zone F as the candidate set for primary zones and Zone K as the candidate set for secondary zones, set this parameter to `[["zoneh","zonef"],["zonek"]]`.
        # 
        # > If you specify multiple zones as the primary or secondary zones, the system deploys the instance in one of the zones without prioritizing them. For example, if you set this parameter to `[["zoneh","zonef"],["zonek"]]`, the primary zone in which the instance is deployed can be Zone H or Zone F, and the secondary zone is Zone K.
        # 
        # *   If you set CrossZone to false and want to deploy the instance in Zone K, set this parameter to `[["zonek"],[]]`. In this case, the value of this parameter must still be two-dimensional arrays, but the array that specifies the candidate for secondary zones is left empty.
        self.selected_zones = selected_zones
        # The version of the ApsaraMQ for Kafka instance. Valid values:
        # 
        # *   ApsaraMQ for Kafka V2 instances: 2.2.0 and 2.6.2.
        # *   ApsaraMQ for Kafka V3 instances: 3.3.1.
        # *   ApsaraMQ for Confluent instances: 7.4.0.
        # 
        # Default value:
        # 
        # *   ApsaraMQ for Kafka V2 instances: 2.2.0.
        # *   ApsaraMQ for Kafka V3 instances: 3.3.1.
        # *   ApsaraMQ for Confluent instances: 7.4.0.
        self.service_version = service_version
        # The mobile phone number of the alert contact.
        self.user_phone_num = user_phone_num
        # The instance username.
        # 
        # *   This parameter is available only for Internet- and VPC- connected ApsaraMQ for Kafka V2 and V3 instances.
        # *   If the instance is an ApsaraMQ for Confluent instance, set this parameter to root or leave this parameter empty.
        # 
        # Default value for ApsaraMQ for Kafka V2 and V3 instances: username. Default value for ApsaraMQ for Confluent instances: root.
        self.username = username
        # The ID of the vSwitch to which you want to connect the instance.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The IDs of the vSwitches with which the instance is associated. If the instance is an ApsaraMQ for Kafka V2 or V3 instance, this parameter is required. If the instance is an ApsaraMQ for Confluent instance, you must configure one of VSwitchIds and VSwitchId. If you configure both of the parameters, the value of VSwitchIds takes effect.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC) in which you want to deploy the instance.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone where you want to deploy the ApsaraMQ for Kafka instance.
        # 
        # *   The zone ID of the ApsaraMQ for Kafka instance must be the same as that of the vSwitch.
        # *   The value must be in the zoneX or Region ID-X format. Examples: zonea and cn-hangzhou-k.
        # 
        # >  If resources in the specified zone is insufficient, the instance may be deployed in another zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.cross_zone is not None:
            result['CrossZone'] = self.cross_zone

        if self.deploy_module is not None:
            result['DeployModule'] = self.deploy_module

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_eip_inner is not None:
            result['IsEipInner'] = self.is_eip_inner

        if self.is_force_selected_zones is not None:
            result['IsForceSelectedZones'] = self.is_force_selected_zones

        if self.is_set_user_and_password is not None:
            result['IsSetUserAndPassword'] = self.is_set_user_and_password

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.name is not None:
            result['Name'] = self.name

        if self.notifier is not None:
            result['Notifier'] = self.notifier

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.selected_zones is not None:
            result['SelectedZones'] = self.selected_zones

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.user_phone_num is not None:
            result['UserPhoneNum'] = self.user_phone_num

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CrossZone') is not None:
            self.cross_zone = m.get('CrossZone')

        if m.get('DeployModule') is not None:
            self.deploy_module = m.get('DeployModule')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsEipInner') is not None:
            self.is_eip_inner = m.get('IsEipInner')

        if m.get('IsForceSelectedZones') is not None:
            self.is_force_selected_zones = m.get('IsForceSelectedZones')

        if m.get('IsSetUserAndPassword') is not None:
            self.is_set_user_and_password = m.get('IsSetUserAndPassword')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notifier') is not None:
            self.notifier = m.get('Notifier')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('SelectedZones') is not None:
            self.selected_zones = m.get('SelectedZones')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('UserPhoneNum') is not None:
            self.user_phone_num = m.get('UserPhoneNum')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

