# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alb20200616 import models as alb_20200616_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_entries_to_acl_with_options(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            self.do_rpcrequest('AddEntriesToAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_entries_to_acl_with_options_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            await self.do_rpcrequest_async('AddEntriesToAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_entries_to_acl(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    async def add_entries_to_acl_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_entries_to_acl_with_options_async(request, runtime)

    def add_servers_to_server_group_with_options(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            self.do_rpcrequest('AddServersToServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            await self.do_rpcrequest_async('AddServersToServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def apply_health_check_template_to_server_group_with_options(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            self.do_rpcrequest('ApplyHealthCheckTemplateToServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_health_check_template_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            await self.do_rpcrequest_async('ApplyHealthCheckTemplateToServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_health_check_template_to_server_group(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_health_check_template_to_server_group_with_options(request, runtime)

    async def apply_health_check_template_to_server_group_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_health_check_template_to_server_group_with_options_async(request, runtime)

    def associate_acls_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            self.do_rpcrequest('AssociateAclsWithListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_acls_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            await self.do_rpcrequest_async('AssociateAclsWithListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_acls_with_listener(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    async def associate_acls_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_acls_with_listener_with_options_async(request, runtime)

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.do_rpcrequest('AssociateAdditionalCertificatesWithListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_additional_certificates_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            await self.do_rpcrequest_async('AssociateAdditionalCertificatesWithListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_additional_certificates_with_listener(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    async def associate_additional_certificates_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_additional_certificates_with_listener_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            self.do_rpcrequest('CreateAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            await self.do_rpcrequest_async('CreateAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_health_check_template_with_options(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            self.do_rpcrequest('CreateHealthCheckTemplate', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_health_check_template_with_options_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            await self.do_rpcrequest_async('CreateHealthCheckTemplate', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_health_check_template(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_health_check_template_with_options(request, runtime)

    async def create_health_check_template_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_health_check_template_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            self.do_rpcrequest('CreateListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            await self.do_rpcrequest_async('CreateListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_listener(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            self.do_rpcrequest('CreateLoadBalancer', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            await self.do_rpcrequest_async('CreateLoadBalancer', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            await self.do_rpcrequest_async('CreateRule', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            self.do_rpcrequest('CreateRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            await self.do_rpcrequest_async('CreateRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rules(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            self.do_rpcrequest('CreateSecurityPolicy', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_security_policy_with_options_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            await self.do_rpcrequest_async('CreateSecurityPolicy', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_security_policy(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            self.do_rpcrequest('CreateServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            await self.do_rpcrequest_async('CreateServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_server_group(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            self.do_rpcrequest('DeleteAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            await self.do_rpcrequest_async('DeleteAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_health_check_templates_with_options(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            self.do_rpcrequest('DeleteHealthCheckTemplates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            await self.do_rpcrequest_async('DeleteHealthCheckTemplates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_health_check_templates(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_health_check_templates_with_options(request, runtime)

    async def delete_health_check_templates_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_health_check_templates_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            self.do_rpcrequest('DeleteListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            await self.do_rpcrequest_async('DeleteListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_listener(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            self.do_rpcrequest('DeleteLoadBalancer', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            await self.do_rpcrequest_async('DeleteLoadBalancer', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_load_balancer(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            await self.do_rpcrequest_async('DeleteRule', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            self.do_rpcrequest('DeleteRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            await self.do_rpcrequest_async('DeleteRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rules(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            self.do_rpcrequest('DeleteSecurityPolicy', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_security_policy_with_options_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            await self.do_rpcrequest_async('DeleteSecurityPolicy', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_policy(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            self.do_rpcrequest('DeleteServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            await self.do_rpcrequest_async('DeleteServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_server_group(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            await self.do_rpcrequest_async('DescribeZones', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self) -> alb_20200616_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(runtime)

    async def describe_zones_async(self) -> alb_20200616_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(runtime)

    def disable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            self.do_rpcrequest('DisableDeletionProtection', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            await self.do_rpcrequest_async('DisableDeletionProtection', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_deletion_protection(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_deletion_protection_with_options(request, runtime)

    async def disable_deletion_protection_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_deletion_protection_with_options_async(request, runtime)

    def disable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            self.do_rpcrequest('DisableLoadBalancerAccessLog', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            await self.do_rpcrequest_async('DisableLoadBalancerAccessLog', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_load_balancer_access_log(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_access_log_with_options(request, runtime)

    async def disable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_access_log_with_options_async(request, runtime)

    def dissociate_acls_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            self.do_rpcrequest('DissociateAclsFromListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_acls_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            await self.do_rpcrequest_async('DissociateAclsFromListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_acls_from_listener(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    async def dissociate_acls_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_acls_from_listener_with_options_async(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.do_rpcrequest('DissociateAdditionalCertificatesFromListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_additional_certificates_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            await self.do_rpcrequest_async('DissociateAdditionalCertificatesFromListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_additional_certificates_from_listener(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    async def dissociate_additional_certificates_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_additional_certificates_from_listener_with_options_async(request, runtime)

    def enable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            self.do_rpcrequest('EnableDeletionProtection', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            await self.do_rpcrequest_async('EnableDeletionProtection', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_deletion_protection(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_deletion_protection_with_options(request, runtime)

    async def enable_deletion_protection_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_deletion_protection_with_options_async(request, runtime)

    def enable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            self.do_rpcrequest('EnableLoadBalancerAccessLog', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            await self.do_rpcrequest_async('EnableLoadBalancerAccessLog', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_load_balancer_access_log(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_access_log_with_options(request, runtime)

    async def enable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_access_log_with_options_async(request, runtime)

    def get_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            self.do_rpcrequest('GetHealthCheckTemplateAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            await self.do_rpcrequest_async('GetHealthCheckTemplateAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_health_check_template_attribute(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_health_check_template_attribute_with_options(request, runtime)

    async def get_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_health_check_template_attribute_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            self.do_rpcrequest('GetListenerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            await self.do_rpcrequest_async('GetListenerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_listener_attribute(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            self.do_rpcrequest('GetLoadBalancerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            await self.do_rpcrequest_async('GetLoadBalancerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_acl_entries_with_options(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            self.do_rpcrequest('ListAclEntries', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_acl_entries_with_options_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            await self.do_rpcrequest_async('ListAclEntries', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_acl_entries(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acl_entries_with_options(request, runtime)

    async def list_acl_entries_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_entries_with_options_async(request, runtime)

    def list_acl_relations_with_options(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            self.do_rpcrequest('ListAclRelations', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_acl_relations_with_options_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            await self.do_rpcrequest_async('ListAclRelations', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_acl_relations(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acl_relations_with_options(request, runtime)

    async def list_acl_relations_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_relations_with_options_async(request, runtime)

    def list_acls_with_options(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            self.do_rpcrequest('ListAcls', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_acls_with_options_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            await self.do_rpcrequest_async('ListAcls', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_acls(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    async def list_acls_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acls_with_options_async(request, runtime)

    def list_asyn_jobs_with_options(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            self.do_rpcrequest('ListAsynJobs', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_asyn_jobs_with_options_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            await self.do_rpcrequest_async('ListAsynJobs', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_asyn_jobs(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_asyn_jobs_with_options(request, runtime)

    async def list_asyn_jobs_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_asyn_jobs_with_options_async(request, runtime)

    def list_health_check_templates_with_options(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            self.do_rpcrequest('ListHealthCheckTemplates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            await self.do_rpcrequest_async('ListHealthCheckTemplates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_health_check_templates(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_health_check_templates_with_options(request, runtime)

    async def list_health_check_templates_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_health_check_templates_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            self.do_rpcrequest('ListListenerCertificates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_listener_certificates_with_options_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            await self.do_rpcrequest_async('ListListenerCertificates', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listener_certificates(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            self.do_rpcrequest('ListListeners', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            await self.do_rpcrequest_async('ListListeners', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listeners(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            self.do_rpcrequest('ListLoadBalancers', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            await self.do_rpcrequest_async('ListLoadBalancers', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_load_balancers(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            self.do_rpcrequest('ListRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            await self.do_rpcrequest_async('ListRules', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rules(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_security_policies_with_options(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            self.do_rpcrequest('ListSecurityPolicies', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_security_policies_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            await self.do_rpcrequest_async('ListSecurityPolicies', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_security_policies(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_policies_with_options(request, runtime)

    async def list_security_policies_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policies_with_options_async(request, runtime)

    def list_security_policy_relations_with_options(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            self.do_rpcrequest('ListSecurityPolicyRelations', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_security_policy_relations_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            await self.do_rpcrequest_async('ListSecurityPolicyRelations', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_security_policy_relations(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_policy_relations_with_options(request, runtime)

    async def list_security_policy_relations_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policy_relations_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            self.do_rpcrequest('ListServerGroups', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            await self.do_rpcrequest_async('ListServerGroups', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_server_groups(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            self.do_rpcrequest('ListServerGroupServers', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            await self.do_rpcrequest_async('ListServerGroupServers', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_server_group_servers(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_system_security_policies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            self.do_rpcrequest('ListSystemSecurityPolicies', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_system_security_policies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            await self.do_rpcrequest_async('ListSystemSecurityPolicies', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_security_policies(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policies_with_options(runtime)

    async def list_system_security_policies_async(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_security_policies_with_options_async(runtime)

    def list_tag_keys_with_options(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            await self.do_rpcrequest_async('ListTagValues', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            await self.do_rpcrequest_async('MoveResourceGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_entries_from_acl_with_options(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            self.do_rpcrequest('RemoveEntriesFromAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_entries_from_acl_with_options_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            await self.do_rpcrequest_async('RemoveEntriesFromAcl', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_entries_from_acl(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    async def remove_entries_from_acl_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_entries_from_acl_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            self.do_rpcrequest('RemoveServersFromServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            await self.do_rpcrequest_async('RemoveServersFromServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def replace_servers_in_server_group_with_options(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            self.do_rpcrequest('ReplaceServersInServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_servers_in_server_group_with_options_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            await self.do_rpcrequest_async('ReplaceServersInServerGroup', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_servers_in_server_group(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_servers_in_server_group_with_options(request, runtime)

    async def replace_servers_in_server_group_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_servers_in_server_group_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            self.do_rpcrequest('StartListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_listener_with_options_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            await self.do_rpcrequest_async('StartListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_listener(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            self.do_rpcrequest('StopListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_listener_with_options_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            await self.do_rpcrequest_async('StopListener', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_listener(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            self.do_rpcrequest('UnTagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            await self.do_rpcrequest_async('UnTagResources', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_tag_resources(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_acl_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            self.do_rpcrequest('UpdateAclAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_acl_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            await self.do_rpcrequest_async('UpdateAclAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_acl_attribute(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    async def update_acl_attribute_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_acl_attribute_with_options_async(request, runtime)

    def update_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            self.do_rpcrequest('UpdateHealthCheckTemplateAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            await self.do_rpcrequest_async('UpdateHealthCheckTemplateAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_health_check_template_attribute(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_health_check_template_attribute_with_options(request, runtime)

    async def update_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_health_check_template_attribute_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            self.do_rpcrequest('UpdateListenerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            await self.do_rpcrequest_async('UpdateListenerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_listener_attribute(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_listener_log_config_with_options(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            self.do_rpcrequest('UpdateListenerLogConfig', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_listener_log_config_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            await self.do_rpcrequest_async('UpdateListenerLogConfig', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_listener_log_config(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_listener_log_config_with_options(request, runtime)

    async def update_listener_log_config_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_log_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            self.do_rpcrequest('UpdateLoadBalancerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            await self.do_rpcrequest_async('UpdateLoadBalancerAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_edition_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            self.do_rpcrequest('UpdateLoadBalancerEdition', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_load_balancer_edition_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            await self.do_rpcrequest_async('UpdateLoadBalancerEdition', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_load_balancer_edition(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_edition_with_options(request, runtime)

    async def update_load_balancer_edition_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_edition_with_options_async(request, runtime)

    def update_rule_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            self.do_rpcrequest('UpdateRuleAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rule_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            await self.do_rpcrequest_async('UpdateRuleAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_rule_attribute(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_attribute_with_options(request, runtime)

    async def update_rule_attribute_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_attribute_with_options_async(request, runtime)

    def update_rules_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            self.do_rpcrequest('UpdateRulesAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rules_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            await self.do_rpcrequest_async('UpdateRulesAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_rules_attribute(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rules_attribute_with_options(request, runtime)

    async def update_rules_attribute_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rules_attribute_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            self.do_rpcrequest('UpdateSecurityPolicyAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_security_policy_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            await self.do_rpcrequest_async('UpdateSecurityPolicyAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_security_policy_attribute(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            self.do_rpcrequest('UpdateServerGroupAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            await self.do_rpcrequest_async('UpdateServerGroupAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            self.do_rpcrequest('UpdateServerGroupServersAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_server_group_servers_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            await self.do_rpcrequest_async('UpdateServerGroupServersAttribute', '2020-06-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_server_group_servers_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
