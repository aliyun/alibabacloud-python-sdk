# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ActiveRightsRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        custom_image_id: str = None,
        data_disk_size: int = None,
        desktop_type: str = None,
        end_time: str = None,
        hibernate: int = None,
        language: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        resource_group_id: str = None,
        rights_assigned_user: List[str] = None,
        rights_gpu_spec: str = None,
        rights_ids: List[str] = None,
        rights_resource_area: str = None,
        rights_resource_image_os: str = None,
        rights_resource_region: str = None,
        rights_resource_type: str = None,
        rights_spec: str = None,
        root_disk_size: int = None,
        start_time: str = None,
        v_switch_id: str = None,
        workspace_ids: List[str] = None,
        wyid_list: List[str] = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip
        # The ID of the image that is available for the specification in the target region.
        self.custom_image_id = custom_image_id
        # The size of the data cloud disk, in GiB. Pass this parameter only when the commodity supports this activation parameter.
        self.data_disk_size = data_disk_size
        # The desktop type. Specify the value based on the types supported by the selected commodity. Omit this parameter if regular cloud desktops do not have this configuration.
        self.desktop_type = desktop_type
        # The end time of the non-hibernation period, in the HH:mm:ss format. This parameter is used together with StartTime.
        self.end_time = end_time
        # The hibernation-related options. The compute plan and existing activation rules corresponding to the right are used.
        self.hibernate = hibernate
        # The display language of the cloud desktop. Valid values: en-US, ja-JP, zh-CN, and zh-HK.
        self.language = language
        # The ID of the office network in the target region. This parameter is required when you activate a cloud desktop.
        self.office_site_id = office_site_id
        # The ID of the policy group. This parameter is optional. If you do not specify this parameter, the default policy of the workspace is used.
        self.policy_group_id = policy_group_id
        # The ID of the resource group. This parameter is optional. The ID is specified by the caller and passed through to the activation request.
        self.resource_group_id = resource_group_id
        # The list of IDs of the assigned end users. The IDs correspond to the rights in this batch by position. For convenience accounts, pass the EndUserId. The number of IDs must be the same as the number of rights.
        self.rights_assigned_user = rights_assigned_user
        # The GPU specification. The value is subject to the return value of the rights details.
        self.rights_gpu_spec = rights_gpu_spec
        # The list of IDs of the rights to be activated. Select the rights accessible to the current identity from ListRights. The parameters in the same batch apply to these rights.
        self.rights_ids = rights_ids
        # The area to which the right belongs. This parameter cannot replace the resource region for a new activation request.
        self.rights_resource_area = rights_resource_area
        # The operating system type of the image used for rights activation.
        self.rights_resource_image_os = rights_resource_image_os
        # The ID of the region where the resource resides. This parameter is configured separately from the routing region of the POP request.
        self.rights_resource_region = rights_resource_region
        # The resource type of the right. For regular cloud desktops, use Desktop. For other commodities, pass the actual type of the right.
        self.rights_resource_type = rights_resource_type
        # The specification code of the right. The value is subject to the rights query result.
        self.rights_spec = rights_spec
        # The size of the system cloud disk, in GiB. Pass this parameter only when the commodity supports this activation parameter.
        self.root_disk_size = root_disk_size
        # The start time of the non-hibernation period, in the HH:mm:ss format. This parameter applies only to the corresponding compute plan.
        self.start_time = start_time
        # The ID of the vSwitch in the target office network. Pass the value based on the network type.
        self.v_switch_id = v_switch_id
        # The list of AD workspace IDs used for BusinessJvsCopilotAgent activation.
        self.workspace_ids = workspace_ids
        # The list of WAIDs used for BusinessJvsCopilotAgent activation. Do not pass this parameter for regular cloud desktop activation.
        self.wyid_list = wyid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.custom_image_id is not None:
            result['CustomImageId'] = self.custom_image_id

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hibernate is not None:
            result['Hibernate'] = self.hibernate

        if self.language is not None:
            result['Language'] = self.language

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rights_assigned_user is not None:
            result['RightsAssignedUser'] = self.rights_assigned_user

        if self.rights_gpu_spec is not None:
            result['RightsGpuSpec'] = self.rights_gpu_spec

        if self.rights_ids is not None:
            result['RightsIds'] = self.rights_ids

        if self.rights_resource_area is not None:
            result['RightsResourceArea'] = self.rights_resource_area

        if self.rights_resource_image_os is not None:
            result['RightsResourceImageOs'] = self.rights_resource_image_os

        if self.rights_resource_region is not None:
            result['RightsResourceRegion'] = self.rights_resource_region

        if self.rights_resource_type is not None:
            result['RightsResourceType'] = self.rights_resource_type

        if self.rights_spec is not None:
            result['RightsSpec'] = self.rights_spec

        if self.root_disk_size is not None:
            result['RootDiskSize'] = self.root_disk_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids

        if self.wyid_list is not None:
            result['WyidList'] = self.wyid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('CustomImageId') is not None:
            self.custom_image_id = m.get('CustomImageId')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Hibernate') is not None:
            self.hibernate = m.get('Hibernate')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RightsAssignedUser') is not None:
            self.rights_assigned_user = m.get('RightsAssignedUser')

        if m.get('RightsGpuSpec') is not None:
            self.rights_gpu_spec = m.get('RightsGpuSpec')

        if m.get('RightsIds') is not None:
            self.rights_ids = m.get('RightsIds')

        if m.get('RightsResourceArea') is not None:
            self.rights_resource_area = m.get('RightsResourceArea')

        if m.get('RightsResourceImageOs') is not None:
            self.rights_resource_image_os = m.get('RightsResourceImageOs')

        if m.get('RightsResourceRegion') is not None:
            self.rights_resource_region = m.get('RightsResourceRegion')

        if m.get('RightsResourceType') is not None:
            self.rights_resource_type = m.get('RightsResourceType')

        if m.get('RightsSpec') is not None:
            self.rights_spec = m.get('RightsSpec')

        if m.get('RootDiskSize') is not None:
            self.root_disk_size = m.get('RootDiskSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        if m.get('WyidList') is not None:
            self.wyid_list = m.get('WyidList')

        return self

