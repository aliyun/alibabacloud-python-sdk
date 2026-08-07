# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHttpApisRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        types: str = None,
        with_apis_published_to_environment: bool = None,
        with_auth_policy_in_environment_id: str = None,
        with_auth_policy_list: bool = None,
        with_consumer_info_by_id: str = None,
        with_environment_info: bool = None,
        with_environment_info_by_id: str = None,
        with_ingress_info: bool = None,
        with_plugin_attachment_by_plugin_id: str = None,
        with_policy_configs: bool = None,
    ):
        # The ID of the cloud-native API gateway.
        self.gateway_id = gateway_id
        # The gateway type associated with the HTTP API. Valid values:
        # - API: cloud-native API gateway.
        # - AI: AI gateway.
        self.gateway_type = gateway_type
        # The search keyword. Supports fuzzy match by API name or exact search by API ID.
        self.keyword = keyword
        # Searches by exact name match.
        self.name = name
        # The page number, starting from 1. Default value: 1.
        self.page_number = page_number
        # The page size. Valid range: [1, 100]. Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of the HTTP API. You can specify multiple types separated by commas (,). Valid values:
        # - Http
        # - Rest
        # - WebSocket
        # - HttpIngress
        self.types = types
        # Specifies whether to return API information that has been published to the specified environment.
        self.with_apis_published_to_environment = with_apis_published_to_environment
        # Specifies the environment ID. The response includes consumer authentication policy information for each API in the specified environment.
        self.with_auth_policy_in_environment_id = with_auth_policy_in_environment_id
        # Specifies whether permission authentication policies are enabled.
        self.with_auth_policy_list = with_auth_policy_list
        # Specifies the consumer ID. The response includes the authorization rule list for the specified consumer for each API.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # The environment context.
        self.with_environment_info = with_environment_info
        # The environment ID.
        self.with_environment_info_by_id = with_environment_info_by_id
        # Specifies whether to include ingress information.
        self.with_ingress_info = with_ingress_info
        # The plug-in ID. Used to retrieve plug-in publishing information based on this plug-in ID.
        self.with_plugin_attachment_by_plugin_id = with_plugin_attachment_by_plugin_id
        # Specifies whether to include policy information.
        self.with_policy_configs = with_policy_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.types is not None:
            result['types'] = self.types

        if self.with_apis_published_to_environment is not None:
            result['withAPIsPublishedToEnvironment'] = self.with_apis_published_to_environment

        if self.with_auth_policy_in_environment_id is not None:
            result['withAuthPolicyInEnvironmentId'] = self.with_auth_policy_in_environment_id

        if self.with_auth_policy_list is not None:
            result['withAuthPolicyList'] = self.with_auth_policy_list

        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id

        if self.with_environment_info is not None:
            result['withEnvironmentInfo'] = self.with_environment_info

        if self.with_environment_info_by_id is not None:
            result['withEnvironmentInfoById'] = self.with_environment_info_by_id

        if self.with_ingress_info is not None:
            result['withIngressInfo'] = self.with_ingress_info

        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id

        if self.with_policy_configs is not None:
            result['withPolicyConfigs'] = self.with_policy_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('types') is not None:
            self.types = m.get('types')

        if m.get('withAPIsPublishedToEnvironment') is not None:
            self.with_apis_published_to_environment = m.get('withAPIsPublishedToEnvironment')

        if m.get('withAuthPolicyInEnvironmentId') is not None:
            self.with_auth_policy_in_environment_id = m.get('withAuthPolicyInEnvironmentId')

        if m.get('withAuthPolicyList') is not None:
            self.with_auth_policy_list = m.get('withAuthPolicyList')

        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')

        if m.get('withEnvironmentInfo') is not None:
            self.with_environment_info = m.get('withEnvironmentInfo')

        if m.get('withEnvironmentInfoById') is not None:
            self.with_environment_info_by_id = m.get('withEnvironmentInfoById')

        if m.get('withIngressInfo') is not None:
            self.with_ingress_info = m.get('withIngressInfo')

        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')

        if m.get('withPolicyConfigs') is not None:
            self.with_policy_configs = m.get('withPolicyConfigs')

        return self

