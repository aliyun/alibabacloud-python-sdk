# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        desktops: List[main_models.DescribeDesktopsResponseBodyDesktops] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cloud computers.
        self.desktops = desktops
        # The token that is used for the next query. If this parameter is left empty, all results are returned.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of cloud computers.
        self.total_count = total_count

    def validate(self):
        if self.desktops:
            for v1 in self.desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Desktops'] = []
        if self.desktops is not None:
            for k1 in self.desktops:
                result['Desktops'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k1 in m.get('Desktops'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDesktopsResponseBodyDesktops(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        bind_amount: int = None,
        bundle_id: str = None,
        bundle_name: str = None,
        charge_type: str = None,
        connection_status: str = None,
        cpu: int = None,
        creation_time: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_duration_list: List[main_models.DescribeDesktopsResponseBodyDesktopsDesktopDurationList] = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_type: str = None,
        directory_id: str = None,
        directory_type: str = None,
        disks: List[main_models.DescribeDesktopsResponseBodyDesktopsDisks] = None,
        domain_type: str = None,
        downgrade_quota: int = None,
        downgraded_times: int = None,
        end_user_ids: List[str] = None,
        entra_domain_name: str = None,
        expired_time: str = None,
        fota_update: main_models.DescribeDesktopsResponseBodyDesktopsFotaUpdate = None,
        gpu_category: int = None,
        gpu_count: float = None,
        gpu_driver_version: str = None,
        gpu_spec: str = None,
        hibernation_beta: bool = None,
        hibernation_options_configured: bool = None,
        host_name: str = None,
        image_id: str = None,
        is_ldap: bool = None,
        management_flag: str = None,
        management_flags: List[str] = None,
        memory: int = None,
        network_interface_id: str = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        office_site_vpc_type: str = None,
        os_type: str = None,
        os_update: main_models.DescribeDesktopsResponseBodyDesktopsOsUpdate = None,
        platform: str = None,
        policy_group_id: str = None,
        policy_group_id_list: List[str] = None,
        policy_group_name: str = None,
        policy_group_name_list: List[str] = None,
        progress: str = None,
        protocol_type: str = None,
        resource_groups: List[main_models.DescribeDesktopsResponseBodyDesktopsResourceGroups] = None,
        serial_number: str = None,
        session_type: str = None,
        sessions: List[main_models.DescribeDesktopsResponseBodyDesktopsSessions] = None,
        snapshot_policy_id: str = None,
        snapshot_policy_name: str = None,
        standard_start_time: str = None,
        start_time: str = None,
        support_hibernation: bool = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        tags: List[main_models.DescribeDesktopsResponseBodyDesktopsTags] = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        zone_type: str = None,
    ):
        self.account_type = account_type
        # The number of concurrent sessions of each cloud computer in a multi-session cloud computer pool.
        self.bind_amount = bind_amount
        # The ID of the template used to create the cloud computer.
        self.bundle_id = bundle_id
        # The name of the template used to create the cloud computer.
        self.bundle_name = bundle_name
        # The billing method of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Postpaid (default): pay-as-you-go
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The connection status of the end user.
        # 
        # Valid values:
        # 
        # *   Unknown
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Connected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Disconnected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.connection_status = connection_status
        # The number of vCPUs.
        self.cpu = cpu
        # The time when the cloud computer was created.
        self.creation_time = creation_time
        # >  This parameter is in invitational preview and is not publicly available.
        self.data_disk_category = data_disk_category
        # >  This parameter is in invitational preview and is not publicly available.
        self.data_disk_size = data_disk_size
        self.desktop_duration_list = desktop_duration_list
        # The ID of the cloud computer pool to which cloud computers belong. Default value: null.``
        self.desktop_group_id = desktop_group_id
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The cloud computer status.
        self.desktop_status = desktop_status
        # The cloud computer type.
        self.desktop_type = desktop_type
        # The directory ID, which is the same as the office network ID (OfficeSiteId).
        self.directory_id = directory_id
        # >  This parameter is in invitational preview and is not publicly available.
        self.directory_type = directory_type
        # The information about the disks.
        self.disks = disks
        self.domain_type = domain_type
        # The number of times for which the cloud desktop can be downgraded.
        self.downgrade_quota = downgrade_quota
        # The number of times for which the cloud desktop has been downgraded.
        self.downgraded_times = downgraded_times
        # The end user IDs.
        self.end_user_ids = end_user_ids
        self.entra_domain_name = entra_domain_name
        # The time when a subscription cloud computer expired.
        self.expired_time = expired_time
        # The information about the image version of the cloud computer.
        self.fota_update = fota_update
        # Indicates whether the cloud computer uses GPUs.
        self.gpu_category = gpu_category
        # The number of GPU cores.
        self.gpu_count = gpu_count
        # The GPU driver version used by the cloud computer.
        self.gpu_driver_version = gpu_driver_version
        # The GPU Specifications.
        self.gpu_spec = gpu_spec
        # >  This parameter is in invitational preview and is not publicly available.
        self.hibernation_beta = hibernation_beta
        # >  This parameter is in invitational preview and is not publicly available.
        self.hibernation_options_configured = hibernation_options_configured
        # The hostname of the cloud desktop.
        self.host_name = host_name
        # The image ID.
        self.image_id = image_id
        self.is_ldap = is_ldap
        # The flag that is used to manage the cloud computer.
        # 
        # Valid values:
        # 
        # *   Migrating: The cloud computer is being migrated.
        # *   Updating: The configurations of the cloud computer are being updated.
        # *   NoFlag: No flags are available.
        self.management_flag = management_flag
        # The flags that are used to manage the cloud computers.
        self.management_flags = management_flags
        # The memory size. Unit: MiB.
        self.memory = memory
        # The ID of the supplementary network interface controller (NIC) created by EDS within an RAM user or Active Directory (AD) user. You cannot modify the ID.
        self.network_interface_id = network_interface_id
        # The IP address of the supplementary NIC created by EDS within an RAM or AD user.
        self.network_interface_ip = network_interface_ip
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The account type of the office network.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience account
        # *   AD_CONNECTOR: enterprise AD account
        self.office_site_type = office_site_type
        # The VPC type of the office network.
        # 
        # Valid values:
        # 
        # *   standard
        # *   customized
        # *   basic
        self.office_site_vpc_type = office_site_vpc_type
        # The OS that is defined in the desktop template.
        self.os_type = os_type
        self.os_update = os_update
        # The information about the OS platform.
        # 
        # Valid values:
        # 
        # *   Ubuntu
        # *   Windows Server 2022
        # *   UOS
        # *   CentOS
        # *   Windows Server 2019
        # *   Windows Server 2016
        self.platform = platform
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The IDs of the cloud computer policies.
        self.policy_group_id_list = policy_group_id_list
        # The policy name.
        self.policy_group_name = policy_group_name
        # The names of the cloud computer policies.
        self.policy_group_name_list = policy_group_name_list
        # The progress of creating the cloud computer.
        self.progress = progress
        # The protocol.
        # 
        # Valid values:
        # 
        # *   HDX
        # *   ASP
        self.protocol_type = protocol_type
        # The information about the enterprise resource groups.
        self.resource_groups = resource_groups
        self.serial_number = serial_number
        # The type of the session.
        # 
        # Valid values:
        # 
        # *   SINGLE_SESSION
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MULTIPLE_SESSION
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.session_type = session_type
        # The session information about cloud computers connected by end users.
        self.sessions = sessions
        # The snapshot policy ID.
        self.snapshot_policy_id = snapshot_policy_id
        # The name of the snapshot policy.
        self.snapshot_policy_name = snapshot_policy_name
        # The standard start time.
        self.standard_start_time = standard_start_time
        # The time when the cloud computer was first started.
        self.start_time = start_time
        # Indicates whether the cloud desktop supports hibernation.
        self.support_hibernation = support_hibernation
        # >  This parameter is in invitational preview and is not publicly available.
        self.system_disk_category = system_disk_category
        # >  This parameter is in invitational preview and is not publicly available.
        self.system_disk_size = system_disk_size
        # Details about the tags.
        self.tags = tags
        # Indicates whether disk encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to query the list of KMS keys.
        self.volume_encryption_key = volume_encryption_key
        # The zone type. Default value: `AvailabilityZone`. This value indicates Alibaba Cloud zones.
        self.zone_type = zone_type

    def validate(self):
        if self.desktop_duration_list:
            for v1 in self.desktop_duration_list:
                 if v1:
                    v1.validate()
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.os_update:
            self.os_update.validate()
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()
        if self.sessions:
            for v1 in self.sessions:
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
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        result['DesktopDurationList'] = []
        if self.desktop_duration_list is not None:
            for k1 in self.desktop_duration_list:
                result['DesktopDurationList'].append(k1.to_map() if k1 else None)

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.downgrade_quota is not None:
            result['DowngradeQuota'] = self.downgrade_quota

        if self.downgraded_times is not None:
            result['DowngradedTimes'] = self.downgraded_times

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.entra_domain_name is not None:
            result['EntraDomainName'] = self.entra_domain_name

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()

        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta

        if self.hibernation_options_configured is not None:
            result['HibernationOptionsConfigured'] = self.hibernation_options_configured

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.is_ldap is not None:
            result['IsLdap'] = self.is_ldap

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.office_site_vpc_type is not None:
            result['OfficeSiteVpcType'] = self.office_site_vpc_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.os_update is not None:
            result['OsUpdate'] = self.os_update.to_map()

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_id_list is not None:
            result['PolicyGroupIdList'] = self.policy_group_id_list

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.policy_group_name_list is not None:
            result['PolicyGroupNameList'] = self.policy_group_name_list

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        if self.snapshot_policy_name is not None:
            result['SnapshotPolicyName'] = self.snapshot_policy_name

        if self.standard_start_time is not None:
            result['StandardStartTime'] = self.standard_start_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        self.desktop_duration_list = []
        if m.get('DesktopDurationList') is not None:
            for k1 in m.get('DesktopDurationList'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsDesktopDurationList()
                self.desktop_duration_list.append(temp_model.from_map(k1))

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('DowngradeQuota') is not None:
            self.downgrade_quota = m.get('DowngradeQuota')

        if m.get('DowngradedTimes') is not None:
            self.downgraded_times = m.get('DowngradedTimes')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('EntraDomainName') is not None:
            self.entra_domain_name = m.get('EntraDomainName')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FotaUpdate') is not None:
            temp_model = main_models.DescribeDesktopsResponseBodyDesktopsFotaUpdate()
            self.fota_update = temp_model.from_map(m.get('FotaUpdate'))

        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')

        if m.get('HibernationOptionsConfigured') is not None:
            self.hibernation_options_configured = m.get('HibernationOptionsConfigured')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IsLdap') is not None:
            self.is_ldap = m.get('IsLdap')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OfficeSiteVpcType') is not None:
            self.office_site_vpc_type = m.get('OfficeSiteVpcType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OsUpdate') is not None:
            temp_model = main_models.DescribeDesktopsResponseBodyDesktopsOsUpdate()
            self.os_update = temp_model.from_map(m.get('OsUpdate'))

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupIdList') is not None:
            self.policy_group_id_list = m.get('PolicyGroupIdList')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('PolicyGroupNameList') is not None:
            self.policy_group_name_list = m.get('PolicyGroupNameList')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

        if m.get('SnapshotPolicyName') is not None:
            self.snapshot_policy_name = m.get('SnapshotPolicyName')

        if m.get('StandardStartTime') is not None:
            self.standard_start_time = m.get('StandardStartTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeDesktopsResponseBodyDesktopsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeDesktopsResponseBodyDesktopsSessions(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
        external_user_name: str = None,
    ):
        # The ID of the end user that connects to the cloud computer.
        self.end_user_id = end_user_id
        # The time when the cloud computer session was established.
        self.establishment_time = establishment_time
        # The name of the external user.
        self.external_user_name = external_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time

        if self.external_user_name is not None:
            result['ExternalUserName'] = self.external_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')

        if m.get('ExternalUserName') is not None:
            self.external_user_name = m.get('ExternalUserName')

        return self

class DescribeDesktopsResponseBodyDesktopsResourceGroups(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the enterprise resource group.
        self.id = id
        # The name of the enterprise resource group.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDesktopsResponseBodyDesktopsOsUpdate(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        package_count: int = None,
        packages: List[main_models.DescribeDesktopsResponseBodyDesktopsOsUpdatePackages] = None,
    ):
        self.check_id = check_id
        self.package_count = package_count
        self.packages = packages

    def validate(self):
        if self.packages:
            for v1 in self.packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.package_count is not None:
            result['PackageCount'] = self.package_count

        result['Packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['Packages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('PackageCount') is not None:
            self.package_count = m.get('PackageCount')

        self.packages = []
        if m.get('Packages') is not None:
            for k1 in m.get('Packages'):
                temp_model = main_models.DescribeDesktopsResponseBodyDesktopsOsUpdatePackages()
                self.packages.append(temp_model.from_map(k1))

        return self

class DescribeDesktopsResponseBodyDesktopsOsUpdatePackages(DaraModel):
    def __init__(
        self,
        description: str = None,
        kb: str = None,
        title: str = None,
    ):
        self.description = description
        self.kb = kb
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.kb is not None:
            result['Kb'] = self.kb

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Kb') is not None:
            self.kb = m.get('Kb')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeDesktopsResponseBodyDesktopsFotaUpdate(DaraModel):
    def __init__(
        self,
        current_app_version: str = None,
        new_app_version: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: int = None,
    ):
        # The current image version of the cloud computer.
        self.current_app_version = current_app_version
        # The version number to which the image of the cloud computer can be updated.
        self.new_app_version = new_app_version
        # The description of the version to which the image of the cloud computer can be updated.
        self.release_note = release_note
        # The English description of the version to which the image of the cloud computer can be updated.
        self.release_note_en = release_note_en
        # The Japanese description of the image version to which the cloud desktop can be updated.
        self.release_note_jp = release_note_jp
        # The size of the installation package for the image to which the cloud desktop can be updated. Unit: KB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version

        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en

        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')

        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')

        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeDesktopsResponseBodyDesktopsDisks(DaraModel):
    def __init__(
        self,
        disk_category: str = None,
        disk_id: str = None,
        disk_size: int = None,
        disk_type: str = None,
        performance_level: str = None,
    ):
        # The type of the disk. Valid values:
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_auto: standard SSD.
        # *   cloud_essd: enhanced SSD (ESSD).
        self.disk_category = disk_category
        # The disk ID.
        self.disk_id = disk_id
        # The disk size. Unit: GiB.
        self.disk_size = disk_size
        # The type of the disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DATA: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disk_type = disk_type
        # The performance level (PL) of the disk when an enterprise SSD (ESSD) is used.
        # 
        # For more information about the differences among enterprise SSDs (ESSDs) at different PLs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # Valid values:
        # 
        # *   PL1
        # *   PL0
        # *   PL3
        # *   PL2
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        return self

class DescribeDesktopsResponseBodyDesktopsDesktopDurationList(DaraModel):
    def __init__(
        self,
        order_instance_id: str = None,
        package_creation_time: str = None,
        package_expired_time: str = None,
        package_id: str = None,
        package_status: str = None,
        package_type: str = None,
        package_used_up_strategy: str = None,
        period_end_time: str = None,
        period_start_time: str = None,
        post_paid_limit_fee: float = None,
        total_duration: int = None,
        used_duration: int = None,
    ):
        self.order_instance_id = order_instance_id
        self.package_creation_time = package_creation_time
        self.package_expired_time = package_expired_time
        self.package_id = package_id
        self.package_status = package_status
        self.package_type = package_type
        self.package_used_up_strategy = package_used_up_strategy
        self.period_end_time = period_end_time
        self.period_start_time = period_start_time
        self.post_paid_limit_fee = post_paid_limit_fee
        self.total_duration = total_duration
        self.used_duration = used_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.package_creation_time is not None:
            result['PackageCreationTime'] = self.package_creation_time

        if self.package_expired_time is not None:
            result['PackageExpiredTime'] = self.package_expired_time

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.package_status is not None:
            result['PackageStatus'] = self.package_status

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_used_up_strategy is not None:
            result['PackageUsedUpStrategy'] = self.package_used_up_strategy

        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time

        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time

        if self.post_paid_limit_fee is not None:
            result['PostPaidLimitFee'] = self.post_paid_limit_fee

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.used_duration is not None:
            result['UsedDuration'] = self.used_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PackageCreationTime') is not None:
            self.package_creation_time = m.get('PackageCreationTime')

        if m.get('PackageExpiredTime') is not None:
            self.package_expired_time = m.get('PackageExpiredTime')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUsedUpStrategy') is not None:
            self.package_used_up_strategy = m.get('PackageUsedUpStrategy')

        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')

        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')

        if m.get('PostPaidLimitFee') is not None:
            self.post_paid_limit_fee = m.get('PostPaidLimitFee')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('UsedDuration') is not None:
            self.used_duration = m.get('UsedDuration')

        return self

