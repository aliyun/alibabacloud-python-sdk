# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20200101 import models as ddoscoo_20200101_models
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
        self._endpoint = self.get_endpoint('ddoscoo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('AddAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcBlacklistResponse().from_map(
            await self.do_rpcrequest_async('AddAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_auto_cc_blacklist(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_blacklist_with_options(request, runtime)

    async def add_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_auto_cc_blacklist_with_options_async(request, runtime)

    def add_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('AddAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcWhitelistResponse().from_map(
            await self.do_rpcrequest_async('AddAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_auto_cc_whitelist(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_whitelist_with_options(request, runtime)

    async def add_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_auto_cc_whitelist_with_options_async(request, runtime)

    def associate_web_cert_with_options(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AssociateWebCertResponse().from_map(
            self.do_rpcrequest('AssociateWebCert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_web_cert_with_options_async(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AssociateWebCertResponse().from_map(
            await self.do_rpcrequest_async('AssociateWebCert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_web_cert(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_web_cert_with_options(request, runtime)

    async def associate_web_cert_async(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_web_cert_with_options_async(request, runtime)

    def attach_scene_defense_object_with_options(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AttachSceneDefenseObjectResponse().from_map(
            self.do_rpcrequest('AttachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_scene_defense_object_with_options_async(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AttachSceneDefenseObjectResponse().from_map(
            await self.do_rpcrequest_async('AttachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_scene_defense_object(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_scene_defense_object_with_options(request, runtime)

    async def attach_scene_defense_object_async(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_scene_defense_object_with_options_async(request, runtime)

    def config_l7rs_policy_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigL7RsPolicyResponse().from_map(
            self.do_rpcrequest('ConfigL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_l7rs_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigL7RsPolicyResponse().from_map(
            await self.do_rpcrequest_async('ConfigL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_l7rs_policy(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_l7rs_policy_with_options(request, runtime)

    async def config_l7rs_policy_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_l7rs_policy_with_options_async(request, runtime)

    def config_network_region_block_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse().from_map(
            self.do_rpcrequest('ConfigNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_network_region_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse().from_map(
            await self.do_rpcrequest_async('ConfigNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_network_region_block(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_network_region_block_with_options(request, runtime)

    async def config_network_region_block_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_network_region_block_with_options_async(request, runtime)

    def config_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRulesResponse().from_map(
            self.do_rpcrequest('ConfigNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRulesResponse().from_map(
            await self.do_rpcrequest_async('ConfigNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_network_rules(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_network_rules_with_options(request, runtime)

    async def config_network_rules_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_network_rules_with_options_async(request, runtime)

    def config_web_cctemplate_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebCCTemplateResponse().from_map(
            self.do_rpcrequest('ConfigWebCCTemplate', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_web_cctemplate_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebCCTemplateResponse().from_map(
            await self.do_rpcrequest_async('ConfigWebCCTemplate', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_web_cctemplate(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_web_cctemplate_with_options(request, runtime)

    async def config_web_cctemplate_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_web_cctemplate_with_options_async(request, runtime)

    def config_web_ip_set_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebIpSetResponse().from_map(
            self.do_rpcrequest('ConfigWebIpSet', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_web_ip_set_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebIpSetResponse().from_map(
            await self.do_rpcrequest_async('ConfigWebIpSet', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_web_ip_set(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_web_ip_set_with_options(request, runtime)

    async def config_web_ip_set_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_web_ip_set_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateAsyncTaskResponse().from_map(
            self.do_rpcrequest('CreateAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateAsyncTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_async_task(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateNetworkRulesResponse().from_map(
            self.do_rpcrequest('CreateNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateNetworkRulesResponse().from_map(
            await self.do_rpcrequest_async('CreateNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_rules(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_rules_with_options(request, runtime)

    async def create_network_rules_async(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_rules_with_options_async(request, runtime)

    def create_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('CreateSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSceneDefensePolicyResponse().from_map(
            await self.do_rpcrequest_async('CreateSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scene_defense_policy(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_defense_policy_with_options(request, runtime)

    async def create_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_defense_policy_with_options_async(request, runtime)

    def create_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSchedulerRuleResponse().from_map(
            self.do_rpcrequest('CreateSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSchedulerRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scheduler_rule(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scheduler_rule_with_options(request, runtime)

    async def create_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduler_rule_with_options_async(request, runtime)

    def create_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateTagResourcesResponse().from_map(
            self.do_rpcrequest('CreateTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('CreateTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tag_resources(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_resources_with_options(request, runtime)

    async def create_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_resources_with_options_async(request, runtime)

    def create_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebCCRuleResponse().from_map(
            self.do_rpcrequest('CreateWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebCCRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_web_ccrule(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_web_ccrule_with_options(request, runtime)

    async def create_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_web_ccrule_with_options_async(request, runtime)

    def create_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebRuleResponse().from_map(
            self.do_rpcrequest('CreateWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_web_rule(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_web_rule_with_options(request, runtime)

    async def create_web_rule_async(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_web_rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAsyncTaskResponse().from_map(
            self.do_rpcrequest('DeleteAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAsyncTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_async_task(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('DeleteAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse().from_map(
            await self.do_rpcrequest_async('DeleteAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_cc_blacklist(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_blacklist_with_options(request, runtime)

    async def delete_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_cc_blacklist_with_options_async(request, runtime)

    def delete_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('DeleteAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DeleteAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_cc_whitelist(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_whitelist_with_options(request, runtime)

    async def delete_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_cc_whitelist_with_options_async(request, runtime)

    def delete_network_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteNetworkRuleResponse().from_map(
            self.do_rpcrequest('DeleteNetworkRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteNetworkRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_rule(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    async def delete_network_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_rule_with_options_async(request, runtime)

    def delete_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('DeleteSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse().from_map(
            await self.do_rpcrequest_async('DeleteSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scene_defense_policy(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_defense_policy_with_options(request, runtime)

    async def delete_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_defense_policy_with_options_async(request, runtime)

    def delete_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSchedulerRuleResponse().from_map(
            self.do_rpcrequest('DeleteSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSchedulerRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scheduler_rule(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduler_rule_with_options(request, runtime)

    async def delete_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduler_rule_with_options_async(request, runtime)

    def delete_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteTagResourcesResponse().from_map(
            self.do_rpcrequest('DeleteTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('DeleteTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tag_resources(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_resources_with_options(request, runtime)

    async def delete_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_resources_with_options_async(request, runtime)

    def delete_web_cache_custom_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_cache_custom_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_cache_custom_rule(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_cache_custom_rule_with_options(request, runtime)

    async def delete_web_cache_custom_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_cache_custom_rule_with_options_async(request, runtime)

    def delete_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCCRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCCRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_ccrule(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_ccrule_with_options(request, runtime)

    async def delete_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_ccrule_with_options_async(request, runtime)

    def delete_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_precise_access_rule(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_precise_access_rule_with_options(request, runtime)

    async def delete_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_precise_access_rule_with_options_async(request, runtime)

    def delete_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_rule(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_web_rule_with_options(request, runtime)

    async def delete_web_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_rule_with_options_async(request, runtime)

    def describe_async_tasks_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAsyncTasksResponse().from_map(
            self.do_rpcrequest('DescribeAsyncTasks', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_async_tasks_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAsyncTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeAsyncTasks', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_async_tasks(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_async_tasks_with_options(request, runtime)

    async def describe_async_tasks_async(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_async_tasks_with_options_async(request, runtime)

    def describe_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_blacklist(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_blacklist_with_options(request, runtime)

    async def describe_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_blacklist_with_options_async(request, runtime)

    def describe_auto_cc_list_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcListCountResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcListCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_cc_list_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcListCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoCcListCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_list_count(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_list_count_with_options(request, runtime)

    async def describe_auto_cc_list_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_list_count_with_options_async(request, runtime)

    def describe_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_whitelist(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_whitelist_with_options(request, runtime)

    async def describe_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_whitelist_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBackSourceCidrResponse().from_map(
            self.do_rpcrequest('DescribeBackSourceCidr', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBackSourceCidrResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackSourceCidr', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_source_cidr(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_blackhole_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlackholeStatusResponse().from_map(
            self.do_rpcrequest('DescribeBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_blackhole_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlackholeStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_blackhole_status(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blackhole_status_with_options(request, runtime)

    async def describe_blackhole_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blackhole_status_with_options_async(request, runtime)

    def describe_block_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlockStatusResponse().from_map(
            self.do_rpcrequest('DescribeBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_block_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlockStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_block_status(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_block_status_with_options(request, runtime)

    async def describe_block_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_block_status_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCertsResponse().from_map(
            self.do_rpcrequest('DescribeCerts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCertsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCerts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certs(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_cname_reuses_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCnameReusesResponse().from_map(
            self.do_rpcrequest('DescribeCnameReuses', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cname_reuses_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCnameReusesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCnameReuses', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cname_reuses(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cname_reuses_with_options(request, runtime)

    async def describe_cname_reuses_async(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cname_reuses_with_options_async(request, runtime)

    def describe_ddos_all_event_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosAllEventListResponse().from_map(
            self.do_rpcrequest('DescribeDDosAllEventList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_all_event_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosAllEventListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosAllEventList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_all_event_list(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    async def describe_ddos_all_event_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_all_event_list_with_options_async(request, runtime)

    def describe_ddos_event_area_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAreaResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventArea', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_area_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAreaResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosEventArea', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_area(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_area_with_options(request, runtime)

    async def describe_ddos_event_area_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_area_with_options_async(request, runtime)

    def describe_ddos_event_attack_type_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventAttackType', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_attack_type_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosEventAttackType', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_attack_type(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_attack_type_with_options(request, runtime)

    async def describe_ddos_event_attack_type_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_attack_type_with_options_async(request, runtime)

    def describe_ddos_event_isp_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventIspResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventIsp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_isp_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventIspResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosEventIsp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_isp(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_isp_with_options(request, runtime)

    async def describe_ddos_event_isp_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_isp_with_options_async(request, runtime)

    def describe_ddos_event_max_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventMaxResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventMax', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_max_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventMaxResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosEventMax', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_max(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_max_with_options(request, runtime)

    async def describe_ddos_event_max_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_max_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDoSEventsResponse().from_map(
            self.do_rpcrequest('DescribeDDoSEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDoSEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDoSEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddo_sevents(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddos_event_src_ip_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventSrcIp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_src_ip_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeDDosEventSrcIp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_src_ip(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_src_ip_with_options(request, runtime)

    async def describe_ddos_event_src_ip_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_src_ip_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDefenseCountStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDefenseCountStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_defense_count_statistics(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_defense_records_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseRecordsResponse().from_map(
            self.do_rpcrequest('DescribeDefenseRecords', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_defense_records_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDefenseRecords', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_defense_records(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_records_with_options(request, runtime)

    async def describe_defense_records_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_records_with_options_async(request, runtime)

    def describe_domain_attack_events_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainAttackEventsResponse().from_map(
            self.do_rpcrequest('DescribeDomainAttackEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_attack_events_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainAttackEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAttackEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_attack_events(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    async def describe_domain_attack_events_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_events_with_options_async(request, runtime)

    def describe_domain_overview_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainOverviewResponse().from_map(
            self.do_rpcrequest('DescribeDomainOverview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_overview_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainOverviewResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainOverview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_overview(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    async def describe_domain_overview_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_overview_with_options_async(request, runtime)

    def describe_domain_qpslist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQPSListResponse().from_map(
            self.do_rpcrequest('DescribeDomainQPSList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qpslist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQPSListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQPSList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qpslist(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qpslist_with_options(request, runtime)

    async def describe_domain_qpslist_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qpslist_with_options_async(request, runtime)

    def describe_domain_qps_with_cache_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse().from_map(
            self.do_rpcrequest('DescribeDomainQpsWithCache', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQpsWithCache', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qps_with_cache(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    async def describe_domain_qps_with_cache_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_cache_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDomains', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomains', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domains(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_domain_status_code_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatusCodeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_status_code_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainStatusCodeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_status_code_count(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_count_with_options(request, runtime)

    async def describe_domain_status_code_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_status_code_count_with_options_async(request, runtime)

    def describe_domain_status_code_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatusCodeList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_status_code_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainStatusCodeList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_status_code_list(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    async def describe_domain_status_code_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_status_code_list_with_options_async(request, runtime)

    def describe_domain_top_attack_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainTopAttackListResponse().from_map(
            self.do_rpcrequest('DescribeDomainTopAttackList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_top_attack_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainTopAttackListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainTopAttackList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_top_attack_list(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_attack_list_with_options(request, runtime)

    async def describe_domain_top_attack_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_attack_list_with_options_async(request, runtime)

    def describe_domain_view_source_countries_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_view_source_countries_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_source_countries(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_countries_with_options(request, runtime)

    async def describe_domain_view_source_countries_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_source_countries_with_options_async(request, runtime)

    def describe_domain_view_source_provinces_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_view_source_provinces_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_source_provinces(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_provinces_with_options(request, runtime)

    async def describe_domain_view_source_provinces_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_source_provinces_with_options_async(request, runtime)

    def describe_domain_view_top_cost_time_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewTopCostTime', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_view_top_cost_time_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainViewTopCostTime', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_top_cost_time(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_cost_time_with_options(request, runtime)

    async def describe_domain_view_top_cost_time_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_top_cost_time_with_options_async(request, runtime)

    def describe_domain_view_top_url_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewTopUrl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_view_top_url_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainViewTopUrl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_top_url(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_url_with_options(request, runtime)

    async def describe_domain_view_top_url_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_top_url_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse().from_map(
            self.do_rpcrequest('DescribeElasticBandwidthSpec', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse().from_map(
            await self.do_rpcrequest_async('DescribeElasticBandwidthSpec', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elastic_bandwidth_spec(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckListResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckListResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_list(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckStatusResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_check_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthCheckStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_status(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_with_options(request, runtime)

    async def describe_health_check_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_status_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceDetailsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceDetails', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceDetails', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_details(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instance_ids_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceIdsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceIds', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_ids_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceIdsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceIds', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ids(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ids_with_options(request, runtime)

    async def describe_instance_ids_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ids_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceSpecsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSpecs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceSpecsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceSpecs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_specs(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instance_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_status(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    async def describe_instance_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_status_with_options_async(request, runtime)

    def describe_l7rs_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeL7RsPolicyResponse().from_map(
            self.do_rpcrequest('DescribeL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_l7rs_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeL7RsPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_l7rs_policy(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_l7rs_policy_with_options(request, runtime)

    async def describe_l7rs_policy_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_l7rs_policy_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse().from_map(
            self.do_rpcrequest('DescribeLogStoreExistStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeLogStoreExistStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_store_exist_status(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_network_region_block_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_region_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_region_block(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_region_block_with_options(request, runtime)

    async def describe_network_region_block_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_region_block_with_options_async(request, runtime)

    def describe_network_rule_attributes_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRuleAttributes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_rule_attributes_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkRuleAttributes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_rule_attributes(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rule_attributes_with_options(request, runtime)

    async def describe_network_rule_attributes_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_rule_attributes_with_options_async(request, runtime)

    def describe_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRulesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_rules(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rules_with_options(request, runtime)

    async def describe_network_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_rules_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeOpEntitiesResponse().from_map(
            self.do_rpcrequest('DescribeOpEntities', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeOpEntitiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeOpEntities', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_op_entities(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_port_attack_max_flow_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse().from_map(
            self.do_rpcrequest('DescribePortAttackMaxFlow', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_attack_max_flow_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribePortAttackMaxFlow', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_attack_max_flow(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_attack_max_flow_with_options(request, runtime)

    async def describe_port_attack_max_flow_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_attack_max_flow_with_options_async(request, runtime)

    def describe_port_auto_cc_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAutoCcStatusResponse().from_map(
            self.do_rpcrequest('DescribePortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_auto_cc_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAutoCcStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribePortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_auto_cc_status(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_auto_cc_status_with_options(request, runtime)

    async def describe_port_auto_cc_status_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_auto_cc_status_with_options_async(request, runtime)

    def describe_port_conns_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsCountResponse().from_map(
            self.do_rpcrequest('DescribePortConnsCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_conns_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsCountResponse().from_map(
            await self.do_rpcrequest_async('DescribePortConnsCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_conns_count(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_count_with_options(request, runtime)

    async def describe_port_conns_count_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_conns_count_with_options_async(request, runtime)

    def describe_port_conns_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsListResponse().from_map(
            self.do_rpcrequest('DescribePortConnsList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_conns_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsListResponse().from_map(
            await self.do_rpcrequest_async('DescribePortConnsList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_conns_list(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_list_with_options(request, runtime)

    async def describe_port_conns_list_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_conns_list_with_options_async(request, runtime)

    def describe_port_flow_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortFlowListResponse().from_map(
            self.do_rpcrequest('DescribePortFlowList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_flow_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortFlowListResponse().from_map(
            await self.do_rpcrequest_async('DescribePortFlowList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_flow_list(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_flow_list_with_options(request, runtime)

    async def describe_port_flow_list_async(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_flow_list_with_options_async(request, runtime)

    def describe_port_max_conns_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortMaxConnsResponse().from_map(
            self.do_rpcrequest('DescribePortMaxConns', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_max_conns_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortMaxConnsResponse().from_map(
            await self.do_rpcrequest_async('DescribePortMaxConns', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_max_conns(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_max_conns_with_options(request, runtime)

    async def describe_port_max_conns_async(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_max_conns_with_options_async(request, runtime)

    def describe_port_view_source_countries_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_view_source_countries_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse().from_map(
            await self.do_rpcrequest_async('DescribePortViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_countries(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_countries_with_options(request, runtime)

    async def describe_port_view_source_countries_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_countries_with_options_async(request, runtime)

    def describe_port_view_source_isps_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceIspsResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceIsps', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_view_source_isps_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceIspsResponse().from_map(
            await self.do_rpcrequest_async('DescribePortViewSourceIsps', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_isps(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_isps_with_options(request, runtime)

    async def describe_port_view_source_isps_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_isps_with_options_async(request, runtime)

    def describe_port_view_source_provinces_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_port_view_source_provinces_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse().from_map(
            await self.do_rpcrequest_async('DescribePortViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_provinces(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_provinces_with_options(request, runtime)

    async def describe_port_view_source_provinces_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_provinces_with_options_async(request, runtime)

    def describe_scene_defense_objects_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse().from_map(
            self.do_rpcrequest('DescribeSceneDefenseObjects', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scene_defense_objects_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSceneDefenseObjects', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scene_defense_objects(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_objects_with_options(request, runtime)

    async def describe_scene_defense_objects_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_defense_objects_with_options_async(request, runtime)

    def describe_scene_defense_policies_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse().from_map(
            self.do_rpcrequest('DescribeSceneDefensePolicies', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scene_defense_policies_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSceneDefensePolicies', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scene_defense_policies(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_policies_with_options(request, runtime)

    async def describe_scene_defense_policies_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_defense_policies_with_options_async(request, runtime)

    def describe_scheduler_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSchedulerRulesResponse().from_map(
            self.do_rpcrequest('DescribeSchedulerRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scheduler_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSchedulerRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSchedulerRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scheduler_rules(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduler_rules_with_options(request, runtime)

    async def describe_scheduler_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduler_rules_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsAuthStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsAuthStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsAuthStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsAuthStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse().from_map(
            self.do_rpcrequest('DescribeSlsLogstoreInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsLogstoreInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_logstore_info(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsOpenStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsOpenStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsOpenStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlsOpenStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_open_status(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describe_sts_grant_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeStsGrantStatusResponse().from_map(
            self.do_rpcrequest('DescribeStsGrantStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sts_grant_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeStsGrantStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeStsGrantStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sts_grant_status(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sts_grant_status_with_options(request, runtime)

    async def describe_sts_grant_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sts_grant_status_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagKeysResponse().from_map(
            self.do_rpcrequest('DescribeTagKeys', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_keys_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagKeysResponse().from_map(
            await self.do_rpcrequest_async('DescribeTagKeys', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_keys(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagResourcesResponse().from_map(
            self.do_rpcrequest('DescribeTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('DescribeTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_resources(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_un_blackhole_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlackholeCountResponse().from_map(
            self.do_rpcrequest('DescribeUnBlackholeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_un_blackhole_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlackholeCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeUnBlackholeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_un_blackhole_count(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_un_blackhole_count_with_options(request, runtime)

    async def describe_un_blackhole_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_un_blackhole_count_with_options_async(request, runtime)

    def describe_un_block_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlockCountResponse().from_map(
            self.do_rpcrequest('DescribeUnBlockCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_un_block_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlockCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeUnBlockCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_un_block_count(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_un_block_count_with_options(request, runtime)

    async def describe_un_block_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_un_block_count_with_options_async(request, runtime)

    def describe_web_access_log_dispatch_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogDispatchStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_access_log_dispatch_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebAccessLogDispatchStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_dispatch_status(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_dispatch_status_with_options(request, runtime)

    async def describe_web_access_log_dispatch_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_dispatch_status_with_options_async(request, runtime)

    def describe_web_access_log_empty_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogEmptyCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_access_log_empty_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebAccessLogEmptyCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_empty_count(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_empty_count_with_options(request, runtime)

    async def describe_web_access_log_empty_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_empty_count_with_options_async(request, runtime)

    def describe_web_access_log_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_access_log_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebAccessLogStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_status(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_status_with_options(request, runtime)

    async def describe_web_access_log_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_status_with_options_async(request, runtime)

    def describe_web_access_mode_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessModeResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_access_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessModeResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_mode(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_mode_with_options(request, runtime)

    async def describe_web_access_mode_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_mode_with_options_async(request, runtime)

    def describe_web_area_block_configs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse().from_map(
            self.do_rpcrequest('DescribeWebAreaBlockConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_area_block_configs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebAreaBlockConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_area_block_configs(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_area_block_configs_with_options(request, runtime)

    async def describe_web_area_block_configs_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_area_block_configs_with_options_async(request, runtime)

    def describe_web_cache_configs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCacheConfigsResponse().from_map(
            self.do_rpcrequest('DescribeWebCacheConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_cache_configs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCacheConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebCacheConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_cache_configs(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cache_configs_with_options(request, runtime)

    async def describe_web_cache_configs_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_cache_configs_with_options_async(request, runtime)

    def describe_web_cc_protect_switch_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse().from_map(
            self.do_rpcrequest('DescribeWebCcProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_cc_protect_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebCcProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_cc_protect_switch(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cc_protect_switch_with_options(request, runtime)

    async def describe_web_cc_protect_switch_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_cc_protect_switch_with_options_async(request, runtime)

    def describe_web_ccrules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCCRulesResponse().from_map(
            self.do_rpcrequest('DescribeWebCCRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_ccrules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCCRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebCCRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_ccrules(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_ccrules_with_options(request, runtime)

    async def describe_web_ccrules_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_ccrules_with_options_async(request, runtime)

    def describe_web_custom_ports_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCustomPortsResponse().from_map(
            self.do_rpcrequest('DescribeWebCustomPorts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_custom_ports_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCustomPortsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebCustomPorts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_custom_ports(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_custom_ports_with_options(request, runtime)

    async def describe_web_custom_ports_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_custom_ports_with_options_async(request, runtime)

    def describe_web_instance_relations_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse().from_map(
            self.do_rpcrequest('DescribeWebInstanceRelations', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_instance_relations_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebInstanceRelations', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_instance_relations(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_instance_relations_with_options(request, runtime)

    async def describe_web_instance_relations_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_instance_relations_with_options_async(request, runtime)

    def describe_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('DescribeWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_precise_access_rule(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_precise_access_rule_with_options(request, runtime)

    async def describe_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_precise_access_rule_with_options_async(request, runtime)

    def describe_web_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebRulesResponse().from_map(
            self.do_rpcrequest('DescribeWebRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_rules(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_rules_with_options(request, runtime)

    async def describe_web_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_rules_with_options_async(request, runtime)

    def detach_scene_defense_object_with_options(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DetachSceneDefenseObjectResponse().from_map(
            self.do_rpcrequest('DetachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_scene_defense_object_with_options_async(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DetachSceneDefenseObjectResponse().from_map(
            await self.do_rpcrequest_async('DetachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_scene_defense_object(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_scene_defense_object_with_options(request, runtime)

    async def detach_scene_defense_object_async(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_scene_defense_object_with_options_async(request, runtime)

    def disable_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('DisableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableSceneDefensePolicyResponse().from_map(
            await self.do_rpcrequest_async('DisableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_scene_defense_policy(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_defense_policy_with_options(request, runtime)

    async def disable_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_scene_defense_policy_with_options_async(request, runtime)

    def disable_web_access_log_config_with_options(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebAccessLogConfigResponse().from_map(
            self.do_rpcrequest('DisableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_web_access_log_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebAccessLogConfigResponse().from_map(
            await self.do_rpcrequest_async('DisableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_access_log_config(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_web_access_log_config_with_options(request, runtime)

    async def disable_web_access_log_config_async(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_access_log_config_with_options_async(request, runtime)

    def disable_web_ccwith_options(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCResponse().from_map(
            self.do_rpcrequest('DisableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_web_ccwith_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCResponse().from_map(
            await self.do_rpcrequest_async('DisableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_cc(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccwith_options(request, runtime)

    async def disable_web_cc_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_ccwith_options_async(request, runtime)

    def disable_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCRuleResponse().from_map(
            self.do_rpcrequest('DisableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCRuleResponse().from_map(
            await self.do_rpcrequest_async('DisableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_ccrule(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccrule_with_options(request, runtime)

    async def disable_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_ccrule_with_options_async(request, runtime)

    def empty_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('EmptyAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def empty_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse().from_map(
            await self.do_rpcrequest_async('EmptyAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_auto_cc_blacklist(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_blacklist_with_options(request, runtime)

    async def empty_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.empty_auto_cc_blacklist_with_options_async(request, runtime)

    def empty_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('EmptyAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def empty_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse().from_map(
            await self.do_rpcrequest_async('EmptyAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_auto_cc_whitelist(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_whitelist_with_options(request, runtime)

    async def empty_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.empty_auto_cc_whitelist_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptySlsLogstoreResponse().from_map(
            self.do_rpcrequest('EmptySlsLogstore', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptySlsLogstoreResponse().from_map(
            await self.do_rpcrequest_async('EmptySlsLogstore', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_sls_logstore(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('EnableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableSceneDefensePolicyResponse().from_map(
            await self.do_rpcrequest_async('EnableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_scene_defense_policy(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_defense_policy_with_options(request, runtime)

    async def enable_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_scene_defense_policy_with_options_async(request, runtime)

    def enable_web_access_log_config_with_options(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebAccessLogConfigResponse().from_map(
            self.do_rpcrequest('EnableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_web_access_log_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebAccessLogConfigResponse().from_map(
            await self.do_rpcrequest_async('EnableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_access_log_config(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_web_access_log_config_with_options(request, runtime)

    async def enable_web_access_log_config_async(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_access_log_config_with_options_async(request, runtime)

    def enable_web_ccwith_options(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCResponse().from_map(
            self.do_rpcrequest('EnableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_web_ccwith_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCResponse().from_map(
            await self.do_rpcrequest_async('EnableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_cc(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccwith_options(request, runtime)

    async def enable_web_cc_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_ccwith_options_async(request, runtime)

    def enable_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCRuleResponse().from_map(
            self.do_rpcrequest('EnableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCRuleResponse().from_map(
            await self.do_rpcrequest_async('EnableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_ccrule(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccrule_with_options(request, runtime)

    async def enable_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_ccrule_with_options_async(request, runtime)

    def modify_blackhole_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlackholeStatusResponse().from_map(
            self.do_rpcrequest('ModifyBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_blackhole_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlackholeStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_blackhole_status(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_blackhole_status_with_options(request, runtime)

    async def modify_blackhole_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_blackhole_status_with_options_async(request, runtime)

    def modify_block_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlockStatusResponse().from_map(
            self.do_rpcrequest('ModifyBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_block_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlockStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_block_status(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_block_status_with_options(request, runtime)

    async def modify_block_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_block_status_with_options_async(request, runtime)

    def modify_cname_reuse_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyCnameReuseResponse().from_map(
            self.do_rpcrequest('ModifyCnameReuse', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cname_reuse_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyCnameReuseResponse().from_map(
            await self.do_rpcrequest_async('ModifyCnameReuse', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cname_reuse(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cname_reuse_with_options(request, runtime)

    async def modify_cname_reuse_async(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cname_reuse_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyElasticBandWidthResponse().from_map(
            self.do_rpcrequest('ModifyElasticBandWidth', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyElasticBandWidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyElasticBandWidth', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elastic_band_width(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyFullLogTtlResponse().from_map(
            self.do_rpcrequest('ModifyFullLogTtl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyFullLogTtlResponse().from_map(
            await self.do_rpcrequest_async('ModifyFullLogTtl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_full_log_ttl(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_health_check_config_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHealthCheckConfigResponse().from_map(
            self.do_rpcrequest('ModifyHealthCheckConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_health_check_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHealthCheckConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyHealthCheckConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_health_check_config(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    async def modify_health_check_config_async(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_health_check_config_with_options_async(request, runtime)

    def modify_http_2enable_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHttp2EnableResponse().from_map(
            self.do_rpcrequest('ModifyHttp2Enable', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_http_2enable_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHttp2EnableResponse().from_map(
            await self.do_rpcrequest_async('ModifyHttp2Enable', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_http_2enable(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_http_2enable_with_options(request, runtime)

    async def modify_http_2enable_async(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_http_2enable_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyInstanceRemarkResponse().from_map(
            self.do_rpcrequest('ModifyInstanceRemark', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyInstanceRemarkResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceRemark', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_remark(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def modify_network_rule_attribute_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse().from_map(
            self.do_rpcrequest('ModifyNetworkRuleAttribute', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_rule_attribute_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyNetworkRuleAttribute', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_rule_attribute(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_rule_attribute_with_options(request, runtime)

    async def modify_network_rule_attribute_async(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_rule_attribute_with_options_async(request, runtime)

    def modify_port_auto_cc_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse().from_map(
            self.do_rpcrequest('ModifyPortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_port_auto_cc_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyPortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_port_auto_cc_status(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_port_auto_cc_status_with_options(request, runtime)

    async def modify_port_auto_cc_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_port_auto_cc_status_with_options_async(request, runtime)

    def modify_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('ModifySceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySceneDefensePolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifySceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scene_defense_policy(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scene_defense_policy_with_options(request, runtime)

    async def modify_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scene_defense_policy_with_options_async(request, runtime)

    def modify_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySchedulerRuleResponse().from_map(
            self.do_rpcrequest('ModifySchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySchedulerRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scheduler_rule(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduler_rule_with_options(request, runtime)

    async def modify_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduler_rule_with_options_async(request, runtime)

    def modify_tls_config_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyTlsConfigResponse().from_map(
            self.do_rpcrequest('ModifyTlsConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_tls_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyTlsConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyTlsConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_tls_config(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tls_config_with_options(request, runtime)

    async def modify_tls_config_async(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tls_config_with_options_async(request, runtime)

    def modify_web_access_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAccessModeResponse().from_map(
            self.do_rpcrequest('ModifyWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_access_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAccessModeResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_access_mode(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_access_mode_with_options(request, runtime)

    async def modify_web_access_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_access_mode_with_options_async(request, runtime)

    def modify_web_aiprotect_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectModeResponse().from_map(
            self.do_rpcrequest('ModifyWebAIProtectMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_aiprotect_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectModeResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebAIProtectMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_aiprotect_mode(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_mode_with_options(request, runtime)

    async def modify_web_aiprotect_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_aiprotect_mode_with_options_async(request, runtime)

    def modify_web_aiprotect_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebAIProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_aiprotect_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebAIProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_aiprotect_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_switch_with_options(request, runtime)

    async def modify_web_aiprotect_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_aiprotect_switch_with_options_async(request, runtime)

    def modify_web_area_block_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockResponse().from_map(
            self.do_rpcrequest('ModifyWebAreaBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_area_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebAreaBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_area_block(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_with_options(request, runtime)

    async def modify_web_area_block_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_area_block_with_options_async(request, runtime)

    def modify_web_area_block_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebAreaBlockSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_area_block_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebAreaBlockSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_area_block_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_switch_with_options(request, runtime)

    async def modify_web_area_block_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_area_block_switch_with_options_async(request, runtime)

    def modify_web_cache_custom_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_cache_custom_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_custom_rule(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_custom_rule_with_options(request, runtime)

    async def modify_web_cache_custom_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_custom_rule_with_options_async(request, runtime)

    def modify_web_cache_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheModeResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_cache_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheModeResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebCacheMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_mode(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_mode_with_options(request, runtime)

    async def modify_web_cache_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_mode_with_options_async(request, runtime)

    def modify_web_cache_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_cache_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebCacheSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_switch_with_options(request, runtime)

    async def modify_web_cache_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_switch_with_options_async(request, runtime)

    def modify_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCCRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCCRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_ccrule(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ccrule_with_options(request, runtime)

    async def modify_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_ccrule_with_options_async(request, runtime)

    def modify_web_ip_set_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebIpSetSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_ip_set_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebIpSetSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_ip_set_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ip_set_switch_with_options(request, runtime)

    async def modify_web_ip_set_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_ip_set_switch_with_options_async(request, runtime)

    def modify_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_precise_access_rule(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_rule_with_options(request, runtime)

    async def modify_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_precise_access_rule_with_options_async(request, runtime)

    def modify_web_precise_access_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebPreciseAccessSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_precise_access_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebPreciseAccessSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_precise_access_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_switch_with_options(request, runtime)

    async def modify_web_precise_access_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_precise_access_switch_with_options_async(request, runtime)

    def modify_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_rule(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_rule_with_options(request, runtime)

    async def modify_web_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_rule_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ReleaseInstanceResponse().from_map(
            self.do_rpcrequest('ReleaseInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ReleaseInstanceResponse().from_map(
            await self.do_rpcrequest_async('ReleaseInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def switch_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.SwitchSchedulerRuleResponse().from_map(
            self.do_rpcrequest('SwitchSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.SwitchSchedulerRuleResponse().from_map(
            await self.do_rpcrequest_async('SwitchSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_scheduler_rule(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_scheduler_rule_with_options(request, runtime)

    async def switch_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_scheduler_rule_with_options_async(request, runtime)
