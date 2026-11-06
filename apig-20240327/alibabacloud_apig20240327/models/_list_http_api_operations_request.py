# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHttpApiOperationsRequest(DaraModel):
    def __init__(
        self,
        consumer_authorization_rule_id: str = None,
        enable_auth: bool = None,
        for_deploy: bool = None,
        gateway_id: str = None,
        method: str = None,
        name: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        path_like: str = None,
        with_consumer_in_environment_id: str = None,
        with_consumer_info_by_id: str = None,
        with_plugin_attachment_by_plugin_id: str = None,
    ):
        # Filters API operations by a specific consumer authorization rule ID. The response includes only authorized API operations.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        # Specifies whether to enable the authentication filter.
        self.enable_auth = enable_auth
        # Specifies whether the request is for a deployment scenario.
        self.for_deploy = for_deploy
        # The ID of the gateway used to filter API operations.
        self.gateway_id = gateway_id
        # Filters API operations by HTTP method.
        self.method = method
        # Searches for API operations by exact name.
        self.name = name
        # Searches for API operations by name prefix.
        self.name_like = name_like
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # Searches for API operations by path prefix.
        self.path_like = path_like
        # The ID of the environment. The response includes the list of authorization rules for the specified consumer in this environment for each API operation. You must also specify the withConsumerInfoById parameter.
        self.with_consumer_in_environment_id = with_consumer_in_environment_id
        # The ID of the consumer. The response includes the list of authorization rules for this consumer in the specified environment for each API operation. You must also specify the withConsumerInEnvironmentId parameter.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # The ID of the plugin. Retrieves the plugin release information based on this plugin ID.
        self.with_plugin_attachment_by_plugin_id = with_plugin_attachment_by_plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_authorization_rule_id is not None:
            result['consumerAuthorizationRuleId'] = self.consumer_authorization_rule_id

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.for_deploy is not None:
            result['forDeploy'] = self.for_deploy

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.path_like is not None:
            result['pathLike'] = self.path_like

        if self.with_consumer_in_environment_id is not None:
            result['withConsumerInEnvironmentId'] = self.with_consumer_in_environment_id

        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id

        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('forDeploy') is not None:
            self.for_deploy = m.get('forDeploy')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pathLike') is not None:
            self.path_like = m.get('pathLike')

        if m.get('withConsumerInEnvironmentId') is not None:
            self.with_consumer_in_environment_id = m.get('withConsumerInEnvironmentId')

        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')

        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')

        return self

