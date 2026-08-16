# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDesktopAgentRuntimeRequest(DaraModel):
    def __init__(
        self,
        agent_im_online_status: str = None,
        agent_instance_statuses: List[str] = None,
        agent_instance_versions: List[str] = None,
        agent_platform: str = None,
        agent_platform_list: List[str] = None,
        agent_provider: str = None,
        agent_provider_list: List[str] = None,
        agent_template_ids: List[str] = None,
        auth_users: List[str] = None,
        biz_region_id: str = None,
        biz_type: int = None,
        channel_configure: bool = None,
        deployment_source: str = None,
        desktop_ids: List[str] = None,
        desktop_names: List[str] = None,
        desktop_statuses: List[str] = None,
        has_auth_user: bool = None,
        has_risk: bool = None,
        include_risk_info: bool = None,
        management_status: str = None,
        model_configure: bool = None,
        model_template_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_ids: List[str] = None,
    ):
        # The agent IM online status filter.
        self.agent_im_online_status = agent_im_online_status
        # The list of agent instance statuses.
        self.agent_instance_statuses = agent_instance_statuses
        # The list of agent instance versions.
        self.agent_instance_versions = agent_instance_versions
        # The agent platform.
        self.agent_platform = agent_platform
        # The list of agent platforms. If AgentPlatform is also specified, AgentPlatform takes precedence and this list is ignored.
        self.agent_platform_list = agent_platform_list
        # The agent provider name.
        self.agent_provider = agent_provider
        # The list of agent providers. If AgentProvider is also specified, AgentProvider takes precedence and this list is ignored.
        self.agent_provider_list = agent_provider_list
        # The list of agent template IDs. A match occurs only when all valid templates are assigned.
        self.agent_template_ids = agent_template_ids
        # The list of authorized users.
        self.auth_users = auth_users
        # The business region ID.
        self.biz_region_id = biz_region_id
        # The business type.
        self.biz_type = biz_type
        # Specifies whether a third-party channel is configured.
        self.channel_configure = channel_configure
        # The deployment source.
        self.deployment_source = deployment_source
        # The list of agent runtime IDs.
        self.desktop_ids = desktop_ids
        # The list of agent runtime names.
        self.desktop_names = desktop_names
        # The list of Cloud Desktop statuses.
        self.desktop_statuses = desktop_statuses
        # Indicates whether an authorized user exists for authorization.
        self.has_auth_user = has_auth_user
        # Specifies whether a risk exists. This parameter is used to filter Cloud Desktops with or without risks and takes effect only when IncludeRiskInfo is set to true.
        # 
        # Set this parameter to true to return only records with risks. Set this parameter to false to return only records without risks. If you do not specify this parameter, no filtering is applied.
        self.has_risk = has_risk
        # Specifies whether to query and return risk information. Default value: false. If set to true, the response includes the RiskInfo field, and the HasRisk filter takes effect.
        self.include_risk_info = include_risk_info
        # The management status filter, such as Hibernated.
        self.management_status = management_status
        # Specifies whether a model is configured.
        self.model_configure = model_configure
        # The model group ID.
        self.model_template_id = model_template_id
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number. Starts from 1. Values 0 and 1 return the same result.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of resource IDs (underlying actual resource IDs).
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_im_online_status is not None:
            result['AgentImOnlineStatus'] = self.agent_im_online_status

        if self.agent_instance_statuses is not None:
            result['AgentInstanceStatuses'] = self.agent_instance_statuses

        if self.agent_instance_versions is not None:
            result['AgentInstanceVersions'] = self.agent_instance_versions

        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_platform_list is not None:
            result['AgentPlatformList'] = self.agent_platform_list

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.agent_provider_list is not None:
            result['AgentProviderList'] = self.agent_provider_list

        if self.agent_template_ids is not None:
            result['AgentTemplateIds'] = self.agent_template_ids

        if self.auth_users is not None:
            result['AuthUsers'] = self.auth_users

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.channel_configure is not None:
            result['ChannelConfigure'] = self.channel_configure

        if self.deployment_source is not None:
            result['DeploymentSource'] = self.deployment_source

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.desktop_names is not None:
            result['DesktopNames'] = self.desktop_names

        if self.desktop_statuses is not None:
            result['DesktopStatuses'] = self.desktop_statuses

        if self.has_auth_user is not None:
            result['HasAuthUser'] = self.has_auth_user

        if self.has_risk is not None:
            result['HasRisk'] = self.has_risk

        if self.include_risk_info is not None:
            result['IncludeRiskInfo'] = self.include_risk_info

        if self.management_status is not None:
            result['ManagementStatus'] = self.management_status

        if self.model_configure is not None:
            result['ModelConfigure'] = self.model_configure

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentImOnlineStatus') is not None:
            self.agent_im_online_status = m.get('AgentImOnlineStatus')

        if m.get('AgentInstanceStatuses') is not None:
            self.agent_instance_statuses = m.get('AgentInstanceStatuses')

        if m.get('AgentInstanceVersions') is not None:
            self.agent_instance_versions = m.get('AgentInstanceVersions')

        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentPlatformList') is not None:
            self.agent_platform_list = m.get('AgentPlatformList')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('AgentProviderList') is not None:
            self.agent_provider_list = m.get('AgentProviderList')

        if m.get('AgentTemplateIds') is not None:
            self.agent_template_ids = m.get('AgentTemplateIds')

        if m.get('AuthUsers') is not None:
            self.auth_users = m.get('AuthUsers')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ChannelConfigure') is not None:
            self.channel_configure = m.get('ChannelConfigure')

        if m.get('DeploymentSource') is not None:
            self.deployment_source = m.get('DeploymentSource')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('DesktopNames') is not None:
            self.desktop_names = m.get('DesktopNames')

        if m.get('DesktopStatuses') is not None:
            self.desktop_statuses = m.get('DesktopStatuses')

        if m.get('HasAuthUser') is not None:
            self.has_auth_user = m.get('HasAuthUser')

        if m.get('HasRisk') is not None:
            self.has_risk = m.get('HasRisk')

        if m.get('IncludeRiskInfo') is not None:
            self.include_risk_info = m.get('IncludeRiskInfo')

        if m.get('ManagementStatus') is not None:
            self.management_status = m.get('ManagementStatus')

        if m.get('ModelConfigure') is not None:
            self.model_configure = m.get('ModelConfigure')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        return self

