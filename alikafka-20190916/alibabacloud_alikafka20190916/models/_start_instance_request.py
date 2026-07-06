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
        # The initial configurations of the ApsaraMQ for Kafka instance. The value must be a valid JSON string. If you do not specify this parameter, the default value is empty.
        # 
        # > - You cannot specify the Config parameter when you deploy a Confluent instance.
        # >
        # > - The enable.acl configuration is not supported for instances of versions earlier than 2.2.0. Only Professional Edition and Serverless instances support access control lists (ACLs).
        # 
        # The following parameters of **Config** are supported for reserved instances:
        # 
        # - **enable.vpc_sasl_ssl**
        # 
        # - **enable.acl**
        # 
        # - **kafka.log.retention.hours**
        # 
        # - **kafka.message.max.bytes**
        # 
        # The following parameters of **Config** are supported for Serverless instances:
        # 
        # - **enable.vpc_sasl_ssl**
        # 
        # - **enable.acl**
        # 
        # - **log.retention.hours**
        # 
        # - **offsets.retention.minutes**
        # 
        # - **message.max.bytes**
        # 
        # - **auto.create.topics.enable**
        # 
        # - **num.partitions**
        # 
        # <props="china">
        # 
        # For more information, see [UpdateInstanceConfig](https://help.aliyun.com/zh/apsaramq-for-kafka/cloud-message-queue-for-kafka/developer-reference/api-alikafka-2019-09-16-updateinstanceconfig?spm=a2c4g.11186623.0.0.3e9e2a04vLr5nF).
        # 
        # 
        # 
        # <props="intl">
        # 
        # For more information, see [UpdateInstanceConfig](https://www.alibabacloud.com/help/zh/apsaramq-for-kafka/cloud-message-queue-for-kafka/developer-reference/api-alikafka-2019-09-16-updateinstanceconfig?spm=a2c63.p38356.0.i1).
        self.config = config
        # Specifies whether to deploy the instance across zones.
        # 
        # - true: Deploy the instance across zones.
        # 
        # - false: Do not deploy the instance across zones.
        # 
        # Default value: true.
        self.cross_zone = cross_zone
        # The deployment mode of the instance. This parameter is required for provisioned instances. This parameter is not required for Serverless and Confluent instances. Valid values:
        # 
        # - **vpc**: VPC instance
        # 
        # - **eip**: Internet/VPC instance
        # 
        # The deployment mode of the instance must be consistent with the instance type. If the instance is a VPC instance, set this parameter to **vpc**. If the instance is an Internet/VPC instance, set this parameter to **eip**.
        self.deploy_module = deploy_module
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable elastic IP addresses (EIPs). Valid values:
        # 
        # - **true**: The instance is an Internet/VPC instance.
        # 
        # - **false**: The instance is a VPC instance.
        # 
        # The value of this parameter must be consistent with the instance type. For example, if the instance is a VPC instance, you must set this parameter to **false**.
        self.is_eip_inner = is_eip_inner
        # Specifies whether to forcibly deploy the instance in the selected zones.
        self.is_force_selected_zones = is_force_selected_zones
        # Specifies whether to set a new username and password. Valid values:
        # 
        # - **true**: Set a new username and password.
        # 
        # - **false**: Do not set a new username and password.
        # 
        # This parameter is supported only for Internet/VPC instances.
        self.is_set_user_and_password = is_set_user_and_password
        # The ID of the key that is used for disk encryption in the same region. You can view the key ID in the [Key Management Service (KMS) console](https://kms.console.aliyun.com/?spm=a2c4g.11186623.2.5.336745b8hfiU21) or create a key. For more information, see [Manage keys](https://help.aliyun.com/document_detail/181610.html).
        # 
        # If you specify this parameter, disk encryption is enabled. You cannot disable disk encryption after it is enabled. When you call this operation, the system checks whether the AliyunServiceRoleForAlikafkaInstanceEncryption service-linked role is created. If the role is not created, the system automatically creates the role. For more information, see [Service-linked Role](https://help.aliyun.com/document_detail/190460.html).
        # 
        # > - You cannot specify the KMSKeyId parameter when you deploy a Serverless instance.
        self.kmskey_id = kmskey_id
        # The name of the instance.
        # 
        # This parameter is not supported for Serverless and Confluent instances.
        # 
        # > If you specify this parameter, make sure that the value is unique in the same region.
        self.name = name
        # The alert contact.
        self.notifier = notifier
        # The password.
        # 
        # - For provisioned and Serverless instances, this parameter is supported only for Internet/VPC instances.
        # 
        # - This parameter is required for Confluent instances. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters are !@#$%^&\\*()_+-=.
        self.password = password
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The security group of the instance.
        # 
        # If you do not specify this parameter, ApsaraMQ for Kafka automatically configures a security group for your instance. If you want to specify this parameter, you must create a security group for the instance in advance. For more information, see [Create a security group](https://help.aliyun.com/document_detail/25468.html).
        self.security_group = security_group
        # A two-dimensional array that consists of the candidate set of the primary zone and the candidate set of the secondary zone. The values can be custom codes (`zone{zone}`) or standard codes (`cn-RegionID-{zone}`).
        # 
        # - If you want to deploy the instance across zones (isCrossZone=true), the candidate set of the primary zone is Zone H or Zone F, and the candidate set of the secondary zone is Zone K, set this parameter to `[[\\"zoneh\\",\\"zonef\\"],[\\"zonek\\"]]`. This example uses custom codes.
        # 
        #   > If you specify multiple zones for the primary or secondary zone, the system selects one of the zones for deployment without a priority. For example, if you set the parameter to `[[\\"zoneh\\",\\"zonef\\"],[\\"zonek\\"]]`, the primary zone of the deployed instance is Zone H or Zone F, and the secondary zone is Zone K.
        # 
        # - If you do not want to deploy the instance across zones (isCrossZone=false) and want to deploy the instance in Zone K, set this parameter to `[[\\"zonek\\"],[]]`. This example uses a custom code. Note that you must still specify two arrays. The second array, which represents the candidate set of the secondary zone, can be empty [].
        # 
        # > Relationship between the SelectedZones and VSwitchIds parameters for provisioned instances
        # >
        # > - If you specify only VSwitchIds and do not specify SelectedZones, the system preferentially selects the zones that correspond to the vSwitches in VSwitchIds.
        self.selected_zones = selected_zones
        # The version of the ApsaraMQ for Kafka instance that you want to deploy.
        # 
        # - For provisioned instances, valid values are 2.2.0 and 2.6.2.
        # 
        # - For Serverless instances, the valid value is 3.3.1.
        # 
        # - For Confluent instances, the valid value is 7.4.0.
        # 
        # Default value:
        # 
        # - Provisioned instances: 2.2.0
        # 
        # - Serverless instances: 3.3.1
        # 
        # - Confluent instances: 7.4.0
        self.service_version = service_version
        # The mobile phone number of the alert contact.
        self.user_phone_num = user_phone_num
        # The username.
        # 
        # - For provisioned and Serverless instances, this parameter is supported only for Internet/VPC instances.
        # 
        # - For Confluent instances, you can set this parameter only to root or leave it empty.
        # 
        # Default value: For provisioned and Serverless instances, the default value is username. For Confluent instances, the default value is root.
        self.username = username
        # The ID of the vSwitch to which the instance is deployed.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The list of vSwitch IDs. This parameter is required for provisioned and Serverless instances. This parameter is supported for Confluent instances. You must specify at least one of VSwitchIds and VSwitchId. If you specify both, VSwitchIds takes precedence.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC in which the instance is deployed.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone in which the instance is deployed.
        # 
        # - The value must be the zone ID of the vSwitch.
        # 
        # - The value can be in the zoneX or RegionId-X format. For example, you can set the value to zonea or cn-hangzhou-k.
        # 
        # > If resources in the specified zone are insufficient, the instance may be deployed in another zone.
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

