# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeAndroidInstanceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        instance_group_model: List[main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instance group.
        self.instance_group_model = instance_group_model
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_group_model:
            for v1 in self.instance_group_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceGroupModel'] = []
        if self.instance_group_model is not None:
            for k1 in self.instance_group_model:
                result['InstanceGroupModel'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_group_model = []
        if m.get('InstanceGroupModel') is not None:
            for k1 in m.get('InstanceGroupModel'):
                temp_model = main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel()
                self.instance_group_model.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        architecture_type: str = None,
        available_instance_amount: int = None,
        bandwidth_package_id: str = None,
        bandwidth_package_status: str = None,
        bandwidth_package_type: str = None,
        bind_qos_rules: main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRules = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks] = None,
        enable_ipv_6: bool = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_version: str = None,
        installed_app_list: str = None,
        instance_group_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        instance_group_spec_describe: str = None,
        instance_group_status: str = None,
        ipv_6bandwidth: int = None,
        memory: int = None,
        network_type: str = None,
        number_of_instances: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        rendering_type: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        sale_mode: str = None,
        system_version: str = None,
        tags: List[main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelTags] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The type of the architecture.
        self.architecture_type = architecture_type
        # The number of available instances.
        # 
        # >  Available instances are those not in the Deleting or Deleted state.
        self.available_instance_amount = available_instance_amount
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_status = bandwidth_package_status
        self.bandwidth_package_type = bandwidth_package_type
        self.bind_qos_rules = bind_qos_rules
        # The billing method.
        self.charge_type = charge_type
        # The number of vCPUs.
        self.cpu = cpu
        # The disks.
        self.disks = disks
        self.enable_ipv_6 = enable_ipv_6
        # The cause of the creation failure.
        self.error_code = error_code
        # The time when the instance group was created.
        self.gmt_create = gmt_create
        # The time when the subscription instance group expires.
        self.gmt_expired = gmt_expired
        # The time when the instance group was updated.
        self.gmt_modified = gmt_modified
        # The ID of the image.
        self.image_id = image_id
        self.image_version = image_version
        # The list of installed applications.
        self.installed_app_list = installed_app_list
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The name of the instance group.
        self.instance_group_name = instance_group_name
        # The specifications of the instance group.
        self.instance_group_spec = instance_group_spec
        # The description of the instance group specifications.
        self.instance_group_spec_describe = instance_group_spec_describe
        # The status of the instance group.
        self.instance_group_status = instance_group_status
        self.ipv_6bandwidth = ipv_6bandwidth
        # The memory size.
        self.memory = memory
        self.network_type = network_type
        # The number of instances in the instance group.
        self.number_of_instances = number_of_instances
        # The ID of the network.
        self.office_site_id = office_site_id
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The ID of the region.
        self.region_id = region_id
        # The rendering mode of the instance group.
        # 
        # Valid values:
        # 
        # *   GPURemote: GPU remote rendering.
        # *   CPU: CPU rendering.
        # *   GPUocal: GPU local rendering.
        self.rendering_type = rendering_type
        # The height of the resolution.
        self.resolution_height = resolution_height
        # The width of the resolution.
        self.resolution_width = resolution_width
        # The sales mode.
        self.sale_mode = sale_mode
        # The version of the operating system.
        self.system_version = system_version
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.bind_qos_rules:
            self.bind_qos_rules.validate()
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.available_instance_amount is not None:
            result['AvailableInstanceAmount'] = self.available_instance_amount

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_status is not None:
            result['BandwidthPackageStatus'] = self.bandwidth_package_status

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.bind_qos_rules is not None:
            result['BindQosRules'] = self.bind_qos_rules.to_map()

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

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

        if self.installed_app_list is not None:
            result['InstalledAppList'] = self.installed_app_list

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name

        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec

        if self.instance_group_spec_describe is not None:
            result['InstanceGroupSpecDescribe'] = self.instance_group_spec_describe

        if self.instance_group_status is not None:
            result['InstanceGroupStatus'] = self.instance_group_status

        if self.ipv_6bandwidth is not None:
            result['Ipv6Bandwidth'] = self.ipv_6bandwidth

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.system_version is not None:
            result['SystemVersion'] = self.system_version

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AvailableInstanceAmount') is not None:
            self.available_instance_amount = m.get('AvailableInstanceAmount')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageStatus') is not None:
            self.bandwidth_package_status = m.get('BandwidthPackageStatus')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('BindQosRules') is not None:
            temp_model = main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRules()
            self.bind_qos_rules = temp_model.from_map(m.get('BindQosRules'))

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

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

        if m.get('InstalledAppList') is not None:
            self.installed_app_list = m.get('InstalledAppList')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')

        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')

        if m.get('InstanceGroupSpecDescribe') is not None:
            self.instance_group_spec_describe = m.get('InstanceGroupSpecDescribe')

        if m.get('InstanceGroupStatus') is not None:
            self.instance_group_status = m.get('InstanceGroupStatus')

        if m.get('Ipv6Bandwidth') is not None:
            self.ipv_6bandwidth = m.get('Ipv6Bandwidth')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelTags(DaraModel):
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

class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks(DaraModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The size of the disk. Unit: GB.
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

class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRules(DaraModel):
    def __init__(
        self,
        instance_qos_rule: List[main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRulesInstanceQosRule] = None,
        total_count: int = None,
    ):
        self.instance_qos_rule = instance_qos_rule
        self.total_count = total_count

    def validate(self):
        if self.instance_qos_rule:
            for v1 in self.instance_qos_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceQosRule'] = []
        if self.instance_qos_rule is not None:
            for k1 in self.instance_qos_rule:
                result['InstanceQosRule'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_qos_rule = []
        if m.get('InstanceQosRule') is not None:
            for k1 in m.get('InstanceQosRule'):
                temp_model = main_models.DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRulesInstanceQosRule()
                self.instance_qos_rule.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelBindQosRulesInstanceQosRule(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        qos_rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.qos_rule_id = qos_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        return self

