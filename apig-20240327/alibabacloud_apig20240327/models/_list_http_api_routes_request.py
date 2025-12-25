# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHttpApiRoutesRequest(DaraModel):
    def __init__(
        self,
        consumer_authorization_rule_id: str = None,
        deploy_statuses: str = None,
        domain_id: str = None,
        environment_id: str = None,
        for_deploy: bool = None,
        gateway_id: str = None,
        name: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        path_like: str = None,
        with_auth_policy_info: bool = None,
        with_consumer_info_by_id: str = None,
        with_plugin_attachment_by_plugin_id: str = None,
    ):
        # The string that is used to filter routes based on consumer authentication rules. Only authorized APIs are returned.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        # The deployment state of the route.
        # 
        # Enumerated values:
        # 
        # *   Deploying: The route is being deployed.
        # *   DeployedWithChanges: The route is deployed and modified.
        # *   Undeploying: The route is being undeployed.
        # *   NotDeployed: The route is not deployed.
        # *   Deployed: The route is deployed.
        # *   UndeployFailed: The route failed to be undeployed.
        # *   DeployFailed: The route failed to be deployed.
        self.deploy_statuses = deploy_statuses
        # Specifies to filter routes by domain ID.
        self.domain_id = domain_id
        # The environment ID.
        self.environment_id = environment_id
        self.for_deploy = for_deploy
        # The ID of the Cloud-native API Gateway instance.
        self.gateway_id = gateway_id
        # The route name.
        self.name = name
        # The route name keyword for a fuzzy search.
        self.name_like = name_like
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The route path keyword for a fuzzy search.
        self.path_like = path_like
        # The consumer authorization information in the response.
        self.with_auth_policy_info = with_auth_policy_info
        # The authentication rules of the specified consumer in each route returned.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # The mounting information of the specified plug-in in each route returned.
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

        if self.deploy_statuses is not None:
            result['deployStatuses'] = self.deploy_statuses

        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.for_deploy is not None:
            result['forDeploy'] = self.for_deploy

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

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

        if self.with_auth_policy_info is not None:
            result['withAuthPolicyInfo'] = self.with_auth_policy_info

        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id

        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')

        if m.get('deployStatuses') is not None:
            self.deploy_statuses = m.get('deployStatuses')

        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('forDeploy') is not None:
            self.for_deploy = m.get('forDeploy')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

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

        if m.get('withAuthPolicyInfo') is not None:
            self.with_auth_policy_info = m.get('withAuthPolicyInfo')

        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')

        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')

        return self

