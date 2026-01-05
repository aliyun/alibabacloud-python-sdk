# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeAndroidInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_model: List[main_models.DescribeAndroidInstancesResponseBodyInstanceModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cloud phone instances.
        self.instance_model = instance_model
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_model:
            for v1 in self.instance_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceModel'] = []
        if self.instance_model is not None:
            for k1 in self.instance_model:
                result['InstanceModel'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_model = []
        if m.get('InstanceModel') is not None:
            for k1 in m.get('InstanceModel'):
                temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModel()
                self.instance_model.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModel(DaraModel):
    def __init__(
        self,
        android_instance_group_id: str = None,
        android_instance_group_name: str = None,
        android_instance_id: str = None,
        android_instance_name: str = None,
        android_instance_status: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_manage_policy: main_models.DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy = None,
        authorized_user_id: str = None,
        bandwidth_package_id: str = None,
        bandwidth_package_type: str = None,
        bind_user_id: str = None,
        biz_image_type: str = None,
        biz_tags: List[main_models.DescribeAndroidInstancesResponseBodyInstanceModelBizTags] = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[main_models.DescribeAndroidInstancesResponseBodyInstanceModelDisks] = None,
        display_config: main_models.DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig = None,
        down_bandwidth_limit: int = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_version: str = None,
        instance_type: str = None,
        internet_status: str = None,
        key_pair_id: str = None,
        memory: int = None,
        network_interface_ip: str = None,
        network_interface_ipv_6address: str = None,
        network_type: str = None,
        office_site_id: str = None,
        persistent_app_instance_id: str = None,
        phone_data_info: main_models.DescribeAndroidInstancesResponseBodyInstanceModelPhoneDataInfo = None,
        policy_group_id: str = None,
        public_ip_address: str = None,
        public_ipv_6address: str = None,
        qos_rule_id: str = None,
        rate: int = None,
        region_id: str = None,
        rendering_type: str = None,
        server_status: str = None,
        server_type: str = None,
        session_status: str = None,
        stream_mode: int = None,
        system_version: str = None,
        tags: List[main_models.DescribeAndroidInstancesResponseBodyInstanceModelTags] = None,
        up_bandwidth_limit: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance group.
        self.android_instance_group_id = android_instance_group_id
        # The name of the instance group.
        self.android_instance_group_name = android_instance_group_name
        # The ID of the instance.
        self.android_instance_id = android_instance_id
        # The name of the instance.
        self.android_instance_name = android_instance_name
        # The state of the instance.
        self.android_instance_status = android_instance_status
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the physical instance.
        self.app_instance_id = app_instance_id
        self.app_manage_policy = app_manage_policy
        # The ID of the user to whom the instance is assigned.
        self.authorized_user_id = authorized_user_id
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        # The ID of the bound user.
        self.bind_user_id = bind_user_id
        self.biz_image_type = biz_image_type
        self.biz_tags = biz_tags
        # The billing method of the instance.
        self.charge_type = charge_type
        # The number of vCPUs.
        self.cpu = cpu
        # The disks.
        self.disks = disks
        self.display_config = display_config
        self.down_bandwidth_limit = down_bandwidth_limit
        # The cause of the instance data backup failure or restoration failure.
        self.error_code = error_code
        # The time when the instance was created.
        self.gmt_create = gmt_create
        # The time when the subscription instance group expires.
        self.gmt_expired = gmt_expired
        # The time when the instance was modified.
        self.gmt_modified = gmt_modified
        self.image_id = image_id
        # The version of the image.
        self.image_version = image_version
        # The type of the instance.
        self.instance_type = instance_type
        self.internet_status = internet_status
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The memory size.
        self.memory = memory
        # The IP address of the ENI.
        self.network_interface_ip = network_interface_ip
        # >  This parameter is not publicly available.
        self.network_interface_ipv_6address = network_interface_ipv_6address
        self.network_type = network_type
        # The office network ID.
        self.office_site_id = office_site_id
        # The ID of the persistent session.
        self.persistent_app_instance_id = persistent_app_instance_id
        self.phone_data_info = phone_data_info
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The public IP address.
        self.public_ip_address = public_ip_address
        # >  This parameter is not publicly available.
        self.public_ipv_6address = public_ipv_6address
        self.qos_rule_id = qos_rule_id
        # The progress of instance data backup or restoration.
        self.rate = rate
        # The region ID of the instance.
        self.region_id = region_id
        # The rendering type.
        self.rendering_type = rendering_type
        self.server_status = server_status
        self.server_type = server_type
        # The session status.
        # 
        # Valid values:
        # 
        # *   disConnect: The session is disconnected.
        # *   connect: The session is connected.
        self.session_status = session_status
        self.stream_mode = stream_mode
        self.system_version = system_version
        # The tags.
        self.tags = tags
        self.up_bandwidth_limit = up_bandwidth_limit
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.app_manage_policy:
            self.app_manage_policy.validate()
        if self.biz_tags:
            for v1 in self.biz_tags:
                 if v1:
                    v1.validate()
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.display_config:
            self.display_config.validate()
        if self.phone_data_info:
            self.phone_data_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_group_id is not None:
            result['AndroidInstanceGroupId'] = self.android_instance_group_id

        if self.android_instance_group_name is not None:
            result['AndroidInstanceGroupName'] = self.android_instance_group_name

        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name

        if self.android_instance_status is not None:
            result['AndroidInstanceStatus'] = self.android_instance_status

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_manage_policy is not None:
            result['AppManagePolicy'] = self.app_manage_policy.to_map()

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id

        if self.biz_image_type is not None:
            result['BizImageType'] = self.biz_image_type

        result['BizTags'] = []
        if self.biz_tags is not None:
            for k1 in self.biz_tags:
                result['BizTags'].append(k1.to_map() if k1 else None)

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config.to_map()

        if self.down_bandwidth_limit is not None:
            result['DownBandwidthLimit'] = self.down_bandwidth_limit

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_status is not None:
            result['InternetStatus'] = self.internet_status

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.network_interface_ipv_6address is not None:
            result['NetworkInterfaceIpv6Address'] = self.network_interface_ipv_6address

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.persistent_app_instance_id is not None:
            result['PersistentAppInstanceId'] = self.persistent_app_instance_id

        if self.phone_data_info is not None:
            result['PhoneDataInfo'] = self.phone_data_info.to_map()

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.public_ipv_6address is not None:
            result['PublicIpv6Address'] = self.public_ipv_6address

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type

        if self.server_status is not None:
            result['ServerStatus'] = self.server_status

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.stream_mode is not None:
            result['StreamMode'] = self.stream_mode

        if self.system_version is not None:
            result['SystemVersion'] = self.system_version

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.up_bandwidth_limit is not None:
            result['UpBandwidthLimit'] = self.up_bandwidth_limit

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceGroupId') is not None:
            self.android_instance_group_id = m.get('AndroidInstanceGroupId')

        if m.get('AndroidInstanceGroupName') is not None:
            self.android_instance_group_name = m.get('AndroidInstanceGroupName')

        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')

        if m.get('AndroidInstanceStatus') is not None:
            self.android_instance_status = m.get('AndroidInstanceStatus')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppManagePolicy') is not None:
            temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy()
            self.app_manage_policy = temp_model.from_map(m.get('AppManagePolicy'))

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')

        if m.get('BizImageType') is not None:
            self.biz_image_type = m.get('BizImageType')

        self.biz_tags = []
        if m.get('BizTags') is not None:
            for k1 in m.get('BizTags'):
                temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelBizTags()
                self.biz_tags.append(temp_model.from_map(k1))

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('DisplayConfig') is not None:
            temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig()
            self.display_config = temp_model.from_map(m.get('DisplayConfig'))

        if m.get('DownBandwidthLimit') is not None:
            self.down_bandwidth_limit = m.get('DownBandwidthLimit')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetStatus') is not None:
            self.internet_status = m.get('InternetStatus')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('NetworkInterfaceIpv6Address') is not None:
            self.network_interface_ipv_6address = m.get('NetworkInterfaceIpv6Address')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PersistentAppInstanceId') is not None:
            self.persistent_app_instance_id = m.get('PersistentAppInstanceId')

        if m.get('PhoneDataInfo') is not None:
            temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelPhoneDataInfo()
            self.phone_data_info = temp_model.from_map(m.get('PhoneDataInfo'))

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('PublicIpv6Address') is not None:
            self.public_ipv_6address = m.get('PublicIpv6Address')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')

        if m.get('ServerStatus') is not None:
            self.server_status = m.get('ServerStatus')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('StreamMode') is not None:
            self.stream_mode = m.get('StreamMode')

        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAndroidInstancesResponseBodyInstanceModelTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpBandwidthLimit') is not None:
            self.up_bandwidth_limit = m.get('UpBandwidthLimit')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelPhoneDataInfo(DaraModel):
    def __init__(
        self,
        phone_data_id: str = None,
        phone_data_volume: int = None,
    ):
        self.phone_data_id = phone_data_id
        self.phone_data_volume = phone_data_volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_data_id is not None:
            result['PhoneDataId'] = self.phone_data_id

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneDataId') is not None:
            self.phone_data_id = m.get('PhoneDataId')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelDisplayConfig(DaraModel):
    def __init__(
        self,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi is not None:
            result['Dpi'] = self.dpi

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelDisks(DaraModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # The type of the disk.
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelBizTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeAndroidInstancesResponseBodyInstanceModelAppManagePolicy(DaraModel):
    def __init__(
        self,
        app_manage_policy_id: str = None,
        app_manage_policy_name: str = None,
    ):
        self.app_manage_policy_id = app_manage_policy_id
        self.app_manage_policy_name = app_manage_policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_manage_policy_id is not None:
            result['AppManagePolicyId'] = self.app_manage_policy_id

        if self.app_manage_policy_name is not None:
            result['AppManagePolicyName'] = self.app_manage_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppManagePolicyId') is not None:
            self.app_manage_policy_id = m.get('AppManagePolicyId')

        if m.get('AppManagePolicyName') is not None:
            self.app_manage_policy_name = m.get('AppManagePolicyName')

        return self

