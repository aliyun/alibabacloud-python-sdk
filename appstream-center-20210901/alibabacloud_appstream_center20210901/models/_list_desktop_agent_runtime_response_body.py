# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListDesktopAgentRuntimeResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDesktopAgentRuntimeResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of returned result objects.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDesktopAgentRuntimeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDesktopAgentRuntimeResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_im_info: main_models.ListDesktopAgentRuntimeResponseBodyDataAgentImInfo = None,
        agent_instance_info_list: List[main_models.ListDesktopAgentRuntimeResponseBodyDataAgentInstanceInfoList] = None,
        auth_users: List[str] = None,
        channel_configure: bool = None,
        channel_configured_list: List[str] = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        has_auth_user: bool = None,
        management_statuses: List[str] = None,
        model_configure: bool = None,
        model_template_id: str = None,
        model_template_name: str = None,
        os_type: str = None,
        qr_code_configuring_list: List[str] = None,
        region_id: str = None,
        region_location: str = None,
        resource_group: main_models.ListDesktopAgentRuntimeResponseBodyDataResourceGroup = None,
        resource_id: str = None,
        risk_info: main_models.ListDesktopAgentRuntimeResponseBodyDataRiskInfo = None,
    ):
        # The agent IM information.
        self.agent_im_info = agent_im_info
        # The list of agent instance information.
        self.agent_instance_info_list = agent_instance_info_list
        # The list of authorized users.
        self.auth_users = auth_users
        # Indicates whether the agent runtime has a configured third-party channel.
        self.channel_configure = channel_configure
        # The list of third-party channels configured for the agent runtime.
        self.channel_configured_list = channel_configured_list
        # The agent runtime ID.
        self.desktop_id = desktop_id
        # The agent runtime name.
        self.desktop_name = desktop_name
        # The cloud computer status.
        self.desktop_status = desktop_status
        # Indicates whether authorized users exist.
        self.has_auth_user = has_auth_user
        self.management_statuses = management_statuses
        # Indicates whether the agent runtime has a configured model.
        self.model_configure = model_configure
        # The effective model template ID (returned only when modelConfigure=true).
        self.model_template_id = model_template_id
        # The effective model template name (returned only when modelConfigure=true).
        self.model_template_name = model_template_name
        # The operating system type.
        self.os_type = os_type
        # The list of channels in QR code configuration.
        self.qr_code_configuring_list = qr_code_configuring_list
        # The region ID.
        self.region_id = region_id
        # The region location (domestic/overseas).
        self.region_location = region_location
        # The resource group information.
        self.resource_group = resource_group
        # The resource ID, which is the cloud computer ID.
        self.resource_id = resource_id
        # The risk information (returned only when the request parameter IncludeRiskInfo is set to true, otherwise null).
        self.risk_info = risk_info

    def validate(self):
        if self.agent_im_info:
            self.agent_im_info.validate()
        if self.agent_instance_info_list:
            for v1 in self.agent_instance_info_list:
                 if v1:
                    v1.validate()
        if self.resource_group:
            self.resource_group.validate()
        if self.risk_info:
            self.risk_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_im_info is not None:
            result['AgentImInfo'] = self.agent_im_info.to_map()

        result['AgentInstanceInfoList'] = []
        if self.agent_instance_info_list is not None:
            for k1 in self.agent_instance_info_list:
                result['AgentInstanceInfoList'].append(k1.to_map() if k1 else None)

        if self.auth_users is not None:
            result['AuthUsers'] = self.auth_users

        if self.channel_configure is not None:
            result['ChannelConfigure'] = self.channel_configure

        if self.channel_configured_list is not None:
            result['ChannelConfiguredList'] = self.channel_configured_list

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.has_auth_user is not None:
            result['HasAuthUser'] = self.has_auth_user

        if self.management_statuses is not None:
            result['ManagementStatuses'] = self.management_statuses

        if self.model_configure is not None:
            result['ModelConfigure'] = self.model_configure

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.model_template_name is not None:
            result['ModelTemplateName'] = self.model_template_name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.qr_code_configuring_list is not None:
            result['QrCodeConfiguringList'] = self.qr_code_configuring_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_location is not None:
            result['RegionLocation'] = self.region_location

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentImInfo') is not None:
            temp_model = main_models.ListDesktopAgentRuntimeResponseBodyDataAgentImInfo()
            self.agent_im_info = temp_model.from_map(m.get('AgentImInfo'))

        self.agent_instance_info_list = []
        if m.get('AgentInstanceInfoList') is not None:
            for k1 in m.get('AgentInstanceInfoList'):
                temp_model = main_models.ListDesktopAgentRuntimeResponseBodyDataAgentInstanceInfoList()
                self.agent_instance_info_list.append(temp_model.from_map(k1))

        if m.get('AuthUsers') is not None:
            self.auth_users = m.get('AuthUsers')

        if m.get('ChannelConfigure') is not None:
            self.channel_configure = m.get('ChannelConfigure')

        if m.get('ChannelConfiguredList') is not None:
            self.channel_configured_list = m.get('ChannelConfiguredList')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('HasAuthUser') is not None:
            self.has_auth_user = m.get('HasAuthUser')

        if m.get('ManagementStatuses') is not None:
            self.management_statuses = m.get('ManagementStatuses')

        if m.get('ModelConfigure') is not None:
            self.model_configure = m.get('ModelConfigure')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('ModelTemplateName') is not None:
            self.model_template_name = m.get('ModelTemplateName')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('QrCodeConfiguringList') is not None:
            self.qr_code_configuring_list = m.get('QrCodeConfiguringList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionLocation') is not None:
            self.region_location = m.get('RegionLocation')

        if m.get('ResourceGroup') is not None:
            temp_model = main_models.ListDesktopAgentRuntimeResponseBodyDataResourceGroup()
            self.resource_group = temp_model.from_map(m.get('ResourceGroup'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RiskInfo') is not None:
            temp_model = main_models.ListDesktopAgentRuntimeResponseBodyDataRiskInfo()
            self.risk_info = temp_model.from_map(m.get('RiskInfo'))

        return self

class ListDesktopAgentRuntimeResponseBodyDataRiskInfo(DaraModel):
    def __init__(
        self,
        agent_uninstalled: bool = None,
        channel_modified: bool = None,
        model_modified: bool = None,
    ):
        # Indicates whether the agent is uninstalled.
        self.agent_uninstalled = agent_uninstalled
        # Indicates whether the third-party channel configuration is modified (inconsistent with the admin-distributed configuration).
        self.channel_modified = channel_modified
        # Indicates whether the model configuration is modified (inconsistent with the admin-distributed configuration).
        self.model_modified = model_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_uninstalled is not None:
            result['AgentUninstalled'] = self.agent_uninstalled

        if self.channel_modified is not None:
            result['ChannelModified'] = self.channel_modified

        if self.model_modified is not None:
            result['ModelModified'] = self.model_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUninstalled') is not None:
            self.agent_uninstalled = m.get('AgentUninstalled')

        if m.get('ChannelModified') is not None:
            self.channel_modified = m.get('ChannelModified')

        if m.get('ModelModified') is not None:
            self.model_modified = m.get('ModelModified')

        return self

class ListDesktopAgentRuntimeResponseBodyDataResourceGroup(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_group_name: str = None,
    ):
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource group name.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

class ListDesktopAgentRuntimeResponseBodyDataAgentInstanceInfoList(DaraModel):
    def __init__(
        self,
        agent_instance_status: str = None,
        agent_instance_version: str = None,
        agent_platform: str = None,
        agent_provider: str = None,
        channel_configure: bool = None,
        channel_configured_list: List[str] = None,
        deployment_source: str = None,
        model_configure: bool = None,
        model_template_id: str = None,
    ):
        # The agent instance status.
        self.agent_instance_status = agent_instance_status
        # The agent instance version.
        self.agent_instance_version = agent_instance_version
        self.agent_platform = agent_platform
        self.agent_provider = agent_provider
        # Indicates whether the agent instance has a configured third-party channel.
        self.channel_configure = channel_configure
        # The list of third-party channels configured for the agent instance.
        self.channel_configured_list = channel_configured_list
        # The deployment source.
        self.deployment_source = deployment_source
        # Indicates whether the agent instance has a configured model.
        self.model_configure = model_configure
        # The configured model group ID.
        self.model_template_id = model_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_instance_status is not None:
            result['AgentInstanceStatus'] = self.agent_instance_status

        if self.agent_instance_version is not None:
            result['AgentInstanceVersion'] = self.agent_instance_version

        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.channel_configure is not None:
            result['ChannelConfigure'] = self.channel_configure

        if self.channel_configured_list is not None:
            result['ChannelConfiguredList'] = self.channel_configured_list

        if self.deployment_source is not None:
            result['DeploymentSource'] = self.deployment_source

        if self.model_configure is not None:
            result['ModelConfigure'] = self.model_configure

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstanceStatus') is not None:
            self.agent_instance_status = m.get('AgentInstanceStatus')

        if m.get('AgentInstanceVersion') is not None:
            self.agent_instance_version = m.get('AgentInstanceVersion')

        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('ChannelConfigure') is not None:
            self.channel_configure = m.get('ChannelConfigure')

        if m.get('ChannelConfiguredList') is not None:
            self.channel_configured_list = m.get('ChannelConfiguredList')

        if m.get('DeploymentSource') is not None:
            self.deployment_source = m.get('DeploymentSource')

        if m.get('ModelConfigure') is not None:
            self.model_configure = m.get('ModelConfigure')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        return self

class ListDesktopAgentRuntimeResponseBodyDataAgentImInfo(DaraModel):
    def __init__(
        self,
        agent_im_status: str = None,
        cloud_space_status: str = None,
    ):
        # The agent IM status.
        self.agent_im_status = agent_im_status
        # The CloudSpace status.
        self.cloud_space_status = cloud_space_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_im_status is not None:
            result['AgentImStatus'] = self.agent_im_status

        if self.cloud_space_status is not None:
            result['CloudSpaceStatus'] = self.cloud_space_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentImStatus') is not None:
            self.agent_im_status = m.get('AgentImStatus')

        if m.get('CloudSpaceStatus') is not None:
            self.cloud_space_status = m.get('CloudSpaceStatus')

        return self

