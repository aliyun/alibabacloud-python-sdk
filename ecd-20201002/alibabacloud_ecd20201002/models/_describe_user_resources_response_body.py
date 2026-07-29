# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeUserResourcesResponseBody(DaraModel):
    def __init__(
        self,
        agent_brief_summary: main_models.DescribeUserResourcesResponseBodyAgentBriefSummary = None,
        max_results: int = None,
        next_token: str = None,
        query_failed_resource_types: List[str] = None,
        rank_version: int = None,
        request_id: str = None,
        resources: List[main_models.DescribeUserResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.agent_brief_summary = agent_brief_summary
        # The maximum number of results returned.
        self.max_results = max_results
        # The token used to start the next query. An empty NextToken indicates that there is no next page.
        self.next_token = next_token
        # The list of resource types that failed to be queried.
        self.query_failed_resource_types = query_failed_resource_types
        # The ranking data version number.
        self.rank_version = rank_version
        # The request ID.
        self.request_id = request_id
        # The list of resource details.
        self.resources = resources
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.agent_brief_summary:
            self.agent_brief_summary.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_brief_summary is not None:
            result['AgentBriefSummary'] = self.agent_brief_summary.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.query_failed_resource_types is not None:
            result['QueryFailedResourceTypes'] = self.query_failed_resource_types

        if self.rank_version is not None:
            result['RankVersion'] = self.rank_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentBriefSummary') is not None:
            temp_model = main_models.DescribeUserResourcesResponseBodyAgentBriefSummary()
            self.agent_brief_summary = temp_model.from_map(m.get('AgentBriefSummary'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('QueryFailedResourceTypes') is not None:
            self.query_failed_resource_types = m.get('QueryFailedResourceTypes')

        if m.get('RankVersion') is not None:
            self.rank_version = m.get('RankVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUserResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        agent_im_url: str = None,
        ali_uid: int = None,
        app_id: str = None,
        auth_mode: str = None,
        category_id: int = None,
        category_type: int = None,
        cds_name: str = None,
        center_resource_id: str = None,
        charge_type: str = None,
        clients: List[main_models.DescribeUserResourcesResponseBodyResourcesClients] = None,
        connection_properties: str = None,
        create_time: str = None,
        desktop_duration_list: List[main_models.DescribeUserResourcesResponseBodyResourcesDesktopDurationList] = None,
        desktop_timers: List[main_models.DescribeUserResourcesResponseBodyResourcesDesktopTimers] = None,
        expired_time: str = None,
        external_domain_id: str = None,
        external_user_id: str = None,
        fota_update: main_models.DescribeUserResourcesResponseBodyResourcesFotaUpdate = None,
        global_status: bool = None,
        has_upgrade: bool = None,
        hibernation_beta: bool = None,
        icon: str = None,
        last_start_time: str = None,
        local_name: str = None,
        management_statuses: List[str] = None,
        office_site_id: str = None,
        order_status: str = None,
        os: str = None,
        os_description: str = None,
        os_type: str = None,
        os_update: main_models.DescribeUserResourcesResponseBodyResourcesOsUpdate = None,
        product_type: str = None,
        protocol_type: str = None,
        real_desktop_id: str = None,
        region_id: str = None,
        region_location: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_level: str = None,
        resource_name: str = None,
        resource_session_status: str = None,
        resource_status: str = None,
        resource_type: str = None,
        session_type: str = None,
        sessions: List[main_models.DescribeUserResourcesResponseBodyResourcesSessions] = None,
        sub_pay_type: str = None,
        support_agent_im: bool = None,
        support_hibernation: bool = None,
        supported_actions: List[str] = None,
        theme_color: str = None,
        user_custom_name: str = None,
        version: str = None,
    ):
        # The access type.
        self.access_type = access_type
        self.agent_im_url = agent_im_url
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The application ID. This parameter is specific to resources of the App type.
        self.app_id = app_id
        # The cloud application authorization mode.
        self.auth_mode = auth_mode
        # The secondary category of the resource. This parameter is specific to resources of the App type.
        self.category_id = category_id
        # The primary category of the resource. This parameter is specific to resources of the App type.
        self.category_type = category_type
        # The cloud drive name. This parameter is specific to resources of the CloudDrive type.
        self.cds_name = cds_name
        # The centralized resource ID.
        self.center_resource_id = center_resource_id
        # The billing method.
        self.charge_type = charge_type
        # The list of client types supported by the resource.
        self.clients = clients
        # The connection properties in JSON string format. The client does not need to parse the content. The value is passed directly to the central resource management service when the application resource establishes a connection.
        self.connection_properties = connection_properties
        # The time when the resource was created.
        self.create_time = create_time
        # The list of cloud desktop package information.
        self.desktop_duration_list = desktop_duration_list
        # The list of Cloud Desktop scheduled task settings.
        self.desktop_timers = desktop_timers
        # The expiration time of subscription resources.
        self.expired_time = expired_time
        # The external domain ID. This parameter is specific to resources of the CloudDrive type.
        self.external_domain_id = external_domain_id
        # The external user ID. This parameter is specific to resources of the CloudDrive type.
        self.external_user_id = external_user_id
        # The cloud desktop upgrade information.
        self.fota_update = fota_update
        # Indicates whether cross-region access is supported. This parameter is specific to resources of the CloudDrive type.
        self.global_status = global_status
        # Indicates whether an update is available.
        self.has_upgrade = has_upgrade
        # Indicates whether the resource is a hibernation beta version.
        self.hibernation_beta = hibernation_beta
        # The resource icon URL. This parameter is specific to resources of the App type.
        self.icon = icon
        # The last time the resource was started.
        self.last_start_time = last_start_time
        # The region name.
        self.local_name = local_name
        # The list of management statuses.
        self.management_statuses = management_statuses
        # The office network ID.
        self.office_site_id = office_site_id
        # The order status.
        self.order_status = order_status
        # The operating system platform information.
        self.os = os
        # The operating system platform description.
        self.os_description = os_description
        # The operating system type.
        self.os_type = os_type
        # The operating system upgrade information.
        self.os_update = os_update
        # The product type.
        self.product_type = product_type
        # The protocol type.
        self.protocol_type = protocol_type
        # The real cloud desktop ID of the shared cloud desktop. This value exists only when the shared cloud desktop has an active session.
        self.real_desktop_id = real_desktop_id
        # The region ID.
        self.region_id = region_id
        # The region location.
        self.region_location = region_location
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource level.
        self.resource_level = resource_level
        # The resource name.
        self.resource_name = resource_name
        # The session status.
        self.resource_session_status = resource_session_status
        # The resource status.
        self.resource_status = resource_status
        # The resource type.
        self.resource_type = resource_type
        # The session type.
        self.session_type = session_type
        # The list of resource user session information.
        self.sessions = sessions
        # The sub-billing method.
        self.sub_pay_type = sub_pay_type
        self.support_agent_im = support_agent_im
        # Indicates whether hibernation is supported.
        self.support_hibernation = support_hibernation
        # The list of supported action types. Currently supported only for cloud phones and cloud desktops (including shared cloud desktops).
        self.supported_actions = supported_actions
        # The resource theme color. This parameter is specific to resources of the App type.
        self.theme_color = theme_color
        # The user-defined name.
        self.user_custom_name = user_custom_name
        # The resource version. This parameter is specific to resources of the App type.
        self.version = version

    def validate(self):
        if self.clients:
            for v1 in self.clients:
                 if v1:
                    v1.validate()
        if self.desktop_duration_list:
            for v1 in self.desktop_duration_list:
                 if v1:
                    v1.validate()
        if self.desktop_timers:
            for v1 in self.desktop_timers:
                 if v1:
                    v1.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.os_update:
            self.os_update.validate()
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.agent_im_url is not None:
            result['AgentImUrl'] = self.agent_im_url

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.cds_name is not None:
            result['CdsName'] = self.cds_name

        if self.center_resource_id is not None:
            result['CenterResourceId'] = self.center_resource_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        result['Clients'] = []
        if self.clients is not None:
            for k1 in self.clients:
                result['Clients'].append(k1.to_map() if k1 else None)

        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DesktopDurationList'] = []
        if self.desktop_duration_list is not None:
            for k1 in self.desktop_duration_list:
                result['DesktopDurationList'].append(k1.to_map() if k1 else None)

        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k1 in self.desktop_timers:
                result['DesktopTimers'].append(k1.to_map() if k1 else None)

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()

        if self.global_status is not None:
            result['GlobalStatus'] = self.global_status

        if self.has_upgrade is not None:
            result['HasUpgrade'] = self.has_upgrade

        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.management_statuses is not None:
            result['ManagementStatuses'] = self.management_statuses

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.os is not None:
            result['Os'] = self.os

        if self.os_description is not None:
            result['OsDescription'] = self.os_description

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.os_update is not None:
            result['OsUpdate'] = self.os_update.to_map()

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.real_desktop_id is not None:
            result['RealDesktopId'] = self.real_desktop_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_location is not None:
            result['RegionLocation'] = self.region_location

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_session_status is not None:
            result['ResourceSessionStatus'] = self.resource_session_status

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.support_agent_im is not None:
            result['SupportAgentIm'] = self.support_agent_im

        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation

        if self.supported_actions is not None:
            result['SupportedActions'] = self.supported_actions

        if self.theme_color is not None:
            result['ThemeColor'] = self.theme_color

        if self.user_custom_name is not None:
            result['UserCustomName'] = self.user_custom_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AgentImUrl') is not None:
            self.agent_im_url = m.get('AgentImUrl')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('CdsName') is not None:
            self.cds_name = m.get('CdsName')

        if m.get('CenterResourceId') is not None:
            self.center_resource_id = m.get('CenterResourceId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResourcesClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.desktop_duration_list = []
        if m.get('DesktopDurationList') is not None:
            for k1 in m.get('DesktopDurationList'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResourcesDesktopDurationList()
                self.desktop_duration_list.append(temp_model.from_map(k1))

        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k1 in m.get('DesktopTimers'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResourcesDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k1))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('FotaUpdate') is not None:
            temp_model = main_models.DescribeUserResourcesResponseBodyResourcesFotaUpdate()
            self.fota_update = temp_model.from_map(m.get('FotaUpdate'))

        if m.get('GlobalStatus') is not None:
            self.global_status = m.get('GlobalStatus')

        if m.get('HasUpgrade') is not None:
            self.has_upgrade = m.get('HasUpgrade')

        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ManagementStatuses') is not None:
            self.management_statuses = m.get('ManagementStatuses')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsDescription') is not None:
            self.os_description = m.get('OsDescription')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OsUpdate') is not None:
            temp_model = main_models.DescribeUserResourcesResponseBodyResourcesOsUpdate()
            self.os_update = temp_model.from_map(m.get('OsUpdate'))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RealDesktopId') is not None:
            self.real_desktop_id = m.get('RealDesktopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionLocation') is not None:
            self.region_location = m.get('RegionLocation')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceSessionStatus') is not None:
            self.resource_session_status = m.get('ResourceSessionStatus')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResourcesSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SupportAgentIm') is not None:
            self.support_agent_im = m.get('SupportAgentIm')

        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')

        if m.get('SupportedActions') is not None:
            self.supported_actions = m.get('SupportedActions')

        if m.get('ThemeColor') is not None:
            self.theme_color = m.get('ThemeColor')

        if m.get('UserCustomName') is not None:
            self.user_custom_name = m.get('UserCustomName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeUserResourcesResponseBodyResourcesSessions(DaraModel):
    def __init__(
        self,
        last_client_ip: str = None,
        nick_name: str = None,
        resource_session_start_time: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        self.last_client_ip = last_client_ip
        # The nickname of the user.
        self.nick_name = nick_name
        # The time when the resource session was connected.
        self.resource_session_start_time = resource_session_start_time
        # The username logged on to the resource.
        self.user_id = user_id
        # The User Principal Name (UPN) of the user bound to the resource, if available. This value is populated only for the session of the currently queried user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_client_ip is not None:
            result['LastClientIp'] = self.last_client_ip

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.resource_session_start_time is not None:
            result['ResourceSessionStartTime'] = self.resource_session_start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastClientIp') is not None:
            self.last_client_ip = m.get('LastClientIp')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('ResourceSessionStartTime') is not None:
            self.resource_session_start_time = m.get('ResourceSessionStartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

class DescribeUserResourcesResponseBodyResourcesOsUpdate(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        kb_list_string: str = None,
        package_count: int = None,
        packages: List[main_models.DescribeUserResourcesResponseBodyResourcesOsUpdatePackages] = None,
        update_catalog_url: str = None,
    ):
        # The check ID.
        self.check_id = check_id
        # The patch number list information.
        self.kb_list_string = kb_list_string
        # The number of packages.
        self.package_count = package_count
        # The list of patch package information.
        self.packages = packages
        # The update catalog URL.
        self.update_catalog_url = update_catalog_url

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

        if self.kb_list_string is not None:
            result['KbListString'] = self.kb_list_string

        if self.package_count is not None:
            result['PackageCount'] = self.package_count

        result['Packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['Packages'].append(k1.to_map() if k1 else None)

        if self.update_catalog_url is not None:
            result['UpdateCatalogUrl'] = self.update_catalog_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('KbListString') is not None:
            self.kb_list_string = m.get('KbListString')

        if m.get('PackageCount') is not None:
            self.package_count = m.get('PackageCount')

        self.packages = []
        if m.get('Packages') is not None:
            for k1 in m.get('Packages'):
                temp_model = main_models.DescribeUserResourcesResponseBodyResourcesOsUpdatePackages()
                self.packages.append(temp_model.from_map(k1))

        if m.get('UpdateCatalogUrl') is not None:
            self.update_catalog_url = m.get('UpdateCatalogUrl')

        return self

class DescribeUserResourcesResponseBodyResourcesOsUpdatePackages(DaraModel):
    def __init__(
        self,
        description: str = None,
        kb: str = None,
        title: str = None,
    ):
        # The patch description.
        self.description = description
        # The patch number.
        self.kb = kb
        # The patch title.
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

class DescribeUserResourcesResponseBodyResourcesFotaUpdate(DaraModel):
    def __init__(
        self,
        channel: str = None,
        current_app_version: str = None,
        force: bool = None,
        new_app_version: str = None,
        new_dcd_version: str = None,
        project: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: str = None,
    ):
        # The channel.
        self.channel = channel
        # The version number of the current image on the cloud desktop.
        self.current_app_version = current_app_version
        # Indicates whether the upgrade is mandatory.
        self.force = force
        # The version number available for upgrade on the cloud desktop.
        self.new_app_version = new_app_version
        # The component disk version number available for upgrade.
        self.new_dcd_version = new_dcd_version
        # The project name.
        self.project = project
        # The release note for the available upgrade version.
        self.release_note = release_note
        # The English release note for the available upgrade version.
        self.release_note_en = release_note_en
        # The Japanese release note for the available upgrade version.
        self.release_note_jp = release_note_jp
        # The installation package size of the available upgrade version. Unit: KB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version

        if self.force is not None:
            result['Force'] = self.force

        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version

        if self.new_dcd_version is not None:
            result['NewDcdVersion'] = self.new_dcd_version

        if self.project is not None:
            result['Project'] = self.project

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
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')

        if m.get('NewDcdVersion') is not None:
            self.new_dcd_version = m.get('NewDcdVersion')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')

        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeUserResourcesResponseBodyResourcesDesktopTimers(DaraModel):
    def __init__(
        self,
        allow_client_setting: str = None,
        cron_expression: str = None,
        enforce: bool = None,
        execution_time: str = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        # Indicates whether the client is allowed to configure this setting.
        self.allow_client_setting = allow_client_setting
        # The cron expression of the scheduled task.
        self.cron_expression = cron_expression
        # Indicates whether the task is forcibly executed.
        self.enforce = enforce
        # The execution time.
        self.execution_time = execution_time
        # The interval of the scheduled task.
        self.interval = interval
        # The operation type.
        self.operation_type = operation_type
        # The reset type.
        self.reset_type = reset_type
        # The task type.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class DescribeUserResourcesResponseBodyResourcesDesktopDurationList(DaraModel):
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
        # The order instance ID.
        self.order_instance_id = order_instance_id
        # The creation time.
        self.package_creation_time = package_creation_time
        # The expiration time.
        self.package_expired_time = package_expired_time
        # The package ID.
        self.package_id = package_id
        # The status.
        self.package_status = package_status
        # The duration package type.
        self.package_type = package_type
        # The cloud desktop status policy after the monthly quota of the plan is used up.
        self.package_used_up_strategy = package_used_up_strategy
        # The end time of the current monthly package.
        self.period_end_time = period_end_time
        # The start time of the current monthly package.
        self.period_start_time = period_start_time
        # The cap amount for the second-phase package.
        self.post_paid_limit_fee = post_paid_limit_fee
        # The total duration.
        self.total_duration = total_duration
        # The used duration.
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

class DescribeUserResourcesResponseBodyResourcesClients(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The client type.
        self.client_type = client_type
        # The support status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeUserResourcesResponseBodyAgentBriefSummary(DaraModel):
    def __init__(
        self,
        agent_briefs: List[main_models.DescribeUserResourcesResponseBodyAgentBriefSummaryAgentBriefs] = None,
        total_count: int = None,
    ):
        self.agent_briefs = agent_briefs
        self.total_count = total_count

    def validate(self):
        if self.agent_briefs:
            for v1 in self.agent_briefs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentBriefs'] = []
        if self.agent_briefs is not None:
            for k1 in self.agent_briefs:
                result['AgentBriefs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_briefs = []
        if m.get('AgentBriefs') is not None:
            for k1 in m.get('AgentBriefs'):
                temp_model = main_models.DescribeUserResourcesResponseBodyAgentBriefSummaryAgentBriefs()
                self.agent_briefs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUserResourcesResponseBodyAgentBriefSummaryAgentBriefs(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        avatar_no_resource_url: str = None,
        avatar_url: str = None,
        count: int = None,
        display_name: str = None,
        sub_title: str = None,
        url: str = None,
    ):
        self.agent_platform = agent_platform
        self.agent_provider = agent_provider
        self.avatar_no_resource_url = avatar_no_resource_url
        self.avatar_url = avatar_url
        self.count = count
        self.display_name = display_name
        self.sub_title = sub_title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.avatar_no_resource_url is not None:
            result['AvatarNoResourceUrl'] = self.avatar_no_resource_url

        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.count is not None:
            result['Count'] = self.count

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('AvatarNoResourceUrl') is not None:
            self.avatar_no_resource_url = m.get('AvatarNoResourceUrl')

        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

