# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gameshield20180305 import models as gameshield_20180305_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('gameshield', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def clean_flex_acc_fwd_rules_with_options(
        self,
        request: gameshield_20180305_models.CleanFlexAccFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CleanFlexAccFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CleanFlexAccFwdRulesResponse().from_map(
            self.do_rpcrequest('CleanFlexAccFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clean_flex_acc_fwd_rules_with_options_async(
        self,
        request: gameshield_20180305_models.CleanFlexAccFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CleanFlexAccFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CleanFlexAccFwdRulesResponse().from_map(
            await self.do_rpcrequest_async('CleanFlexAccFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clean_flex_acc_fwd_rules(
        self,
        request: gameshield_20180305_models.CleanFlexAccFwdRulesRequest,
    ) -> gameshield_20180305_models.CleanFlexAccFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.clean_flex_acc_fwd_rules_with_options(request, runtime)

    async def clean_flex_acc_fwd_rules_async(
        self,
        request: gameshield_20180305_models.CleanFlexAccFwdRulesRequest,
    ) -> gameshield_20180305_models.CleanFlexAccFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clean_flex_acc_fwd_rules_with_options_async(request, runtime)

    def clean_flex_fwd_rules_with_options(
        self,
        request: gameshield_20180305_models.CleanFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CleanFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CleanFlexFwdRulesResponse().from_map(
            self.do_rpcrequest('CleanFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clean_flex_fwd_rules_with_options_async(
        self,
        request: gameshield_20180305_models.CleanFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CleanFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CleanFlexFwdRulesResponse().from_map(
            await self.do_rpcrequest_async('CleanFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clean_flex_fwd_rules(
        self,
        request: gameshield_20180305_models.CleanFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.CleanFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.clean_flex_fwd_rules_with_options(request, runtime)

    async def clean_flex_fwd_rules_async(
        self,
        request: gameshield_20180305_models.CleanFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.CleanFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clean_flex_fwd_rules_with_options_async(request, runtime)

    def clear_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.ClearCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ClearCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ClearCcRouteRulesResponse().from_map(
            self.do_rpcrequest('ClearCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.ClearCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ClearCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ClearCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('ClearCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_cc_route_rules(
        self,
        request: gameshield_20180305_models.ClearCcRouteRulesRequest,
    ) -> gameshield_20180305_models.ClearCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_cc_route_rules_with_options(request, runtime)

    async def clear_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.ClearCcRouteRulesRequest,
    ) -> gameshield_20180305_models.ClearCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_cc_route_rules_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: gameshield_20180305_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateAppResponse().from_map(
            self.do_rpcrequest('CreateApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: gameshield_20180305_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateAppResponse().from_map(
            await self.do_rpcrequest_async('CreateApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(
        self,
        request: gameshield_20180305_models.CreateAppRequest,
    ) -> gameshield_20180305_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: gameshield_20180305_models.CreateAppRequest,
    ) -> gameshield_20180305_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_key_with_options(
        self,
        request: gameshield_20180305_models.CreateAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateAppKeyResponse().from_map(
            self.do_rpcrequest('CreateAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_key_with_options_async(
        self,
        request: gameshield_20180305_models.CreateAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateAppKeyResponse().from_map(
            await self.do_rpcrequest_async('CreateAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_key(
        self,
        request: gameshield_20180305_models.CreateAppKeyRequest,
    ) -> gameshield_20180305_models.CreateAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_key_with_options(request, runtime)

    async def create_app_key_async(
        self,
        request: gameshield_20180305_models.CreateAppKeyRequest,
    ) -> gameshield_20180305_models.CreateAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_key_with_options_async(request, runtime)

    def create_biz_with_options(
        self,
        request: gameshield_20180305_models.CreateBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateBizResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateBizResponse().from_map(
            self.do_rpcrequest('CreateBiz', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_biz_with_options_async(
        self,
        request: gameshield_20180305_models.CreateBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateBizResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateBizResponse().from_map(
            await self.do_rpcrequest_async('CreateBiz', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_biz(
        self,
        request: gameshield_20180305_models.CreateBizRequest,
    ) -> gameshield_20180305_models.CreateBizResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_biz_with_options(request, runtime)

    async def create_biz_async(
        self,
        request: gameshield_20180305_models.CreateBizRequest,
    ) -> gameshield_20180305_models.CreateBizResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_biz_with_options_async(request, runtime)

    def create_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.CreateCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateCcRouteRulesResponse().from_map(
            self.do_rpcrequest('CreateCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.CreateCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('CreateCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cc_route_rules(
        self,
        request: gameshield_20180305_models.CreateCcRouteRulesRequest,
    ) -> gameshield_20180305_models.CreateCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cc_route_rules_with_options(request, runtime)

    async def create_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.CreateCcRouteRulesRequest,
    ) -> gameshield_20180305_models.CreateCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cc_route_rules_with_options_async(request, runtime)

    def create_flex_acc_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexAccFwdRuleResponse().from_map(
            self.do_rpcrequest('CreateFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flex_acc_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexAccFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flex_acc_fwd_rule(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flex_acc_fwd_rule_with_options(request, runtime)

    async def create_flex_acc_fwd_rule_async(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flex_acc_fwd_rule_with_options_async(request, runtime)

    def create_flex_acc_fwd_rule_list_with_options(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexAccFwdRuleListResponse().from_map(
            self.do_rpcrequest('CreateFlexAccFwdRuleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flex_acc_fwd_rule_list_with_options_async(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexAccFwdRuleListResponse().from_map(
            await self.do_rpcrequest_async('CreateFlexAccFwdRuleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flex_acc_fwd_rule_list(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleListRequest,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flex_acc_fwd_rule_list_with_options(request, runtime)

    async def create_flex_acc_fwd_rule_list_async(
        self,
        request: gameshield_20180305_models.CreateFlexAccFwdRuleListRequest,
    ) -> gameshield_20180305_models.CreateFlexAccFwdRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flex_acc_fwd_rule_list_with_options_async(request, runtime)

    def create_flex_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.CreateFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexFwdRuleResponse().from_map(
            self.do_rpcrequest('CreateFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flex_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.CreateFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateFlexFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flex_fwd_rule(
        self,
        request: gameshield_20180305_models.CreateFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.CreateFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flex_fwd_rule_with_options(request, runtime)

    async def create_flex_fwd_rule_async(
        self,
        request: gameshield_20180305_models.CreateFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.CreateFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flex_fwd_rule_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: gameshield_20180305_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateGroupResponse().from_map(
            self.do_rpcrequest('CreateGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: gameshield_20180305_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(
        self,
        request: gameshield_20180305_models.CreateGroupRequest,
    ) -> gameshield_20180305_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: gameshield_20180305_models.CreateGroupRequest,
    ) -> gameshield_20180305_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_layer_4rule_with_options(
        self,
        request: gameshield_20180305_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateLayer4RuleResponse().from_map(
            self.do_rpcrequest('CreateLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_layer_4rule_with_options_async(
        self,
        request: gameshield_20180305_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('CreateLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_layer_4rule(
        self,
        request: gameshield_20180305_models.CreateLayer4RuleRequest,
    ) -> gameshield_20180305_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    async def create_layer_4rule_async(
        self,
        request: gameshield_20180305_models.CreateLayer4RuleRequest,
    ) -> gameshield_20180305_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_4rule_with_options_async(request, runtime)

    def create_layer_4rules_with_options(
        self,
        request: gameshield_20180305_models.CreateLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateLayer4RulesResponse().from_map(
            self.do_rpcrequest('CreateLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_layer_4rules_with_options_async(
        self,
        request: gameshield_20180305_models.CreateLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.CreateLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.CreateLayer4RulesResponse().from_map(
            await self.do_rpcrequest_async('CreateLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_layer_4rules(
        self,
        request: gameshield_20180305_models.CreateLayer4RulesRequest,
    ) -> gameshield_20180305_models.CreateLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rules_with_options(request, runtime)

    async def create_layer_4rules_async(
        self,
        request: gameshield_20180305_models.CreateLayer4RulesRequest,
    ) -> gameshield_20180305_models.CreateLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_4rules_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: gameshield_20180305_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteAppResponse().from_map(
            self.do_rpcrequest('DeleteApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteAppResponse().from_map(
            await self.do_rpcrequest_async('DeleteApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(
        self,
        request: gameshield_20180305_models.DeleteAppRequest,
    ) -> gameshield_20180305_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: gameshield_20180305_models.DeleteAppRequest,
    ) -> gameshield_20180305_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_key_with_options(
        self,
        request: gameshield_20180305_models.DeleteAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteAppKeyResponse().from_map(
            self.do_rpcrequest('DeleteAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_key_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteAppKeyResponse().from_map(
            await self.do_rpcrequest_async('DeleteAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_key(
        self,
        request: gameshield_20180305_models.DeleteAppKeyRequest,
    ) -> gameshield_20180305_models.DeleteAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_key_with_options(request, runtime)

    async def delete_app_key_async(
        self,
        request: gameshield_20180305_models.DeleteAppKeyRequest,
    ) -> gameshield_20180305_models.DeleteAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_key_with_options_async(request, runtime)

    def delete_biz_with_options(
        self,
        request: gameshield_20180305_models.DeleteBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteBizResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteBizResponse().from_map(
            self.do_rpcrequest('DeleteBiz', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_biz_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteBizResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteBizResponse().from_map(
            await self.do_rpcrequest_async('DeleteBiz', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_biz(
        self,
        request: gameshield_20180305_models.DeleteBizRequest,
    ) -> gameshield_20180305_models.DeleteBizResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_with_options(request, runtime)

    async def delete_biz_async(
        self,
        request: gameshield_20180305_models.DeleteBizRequest,
    ) -> gameshield_20180305_models.DeleteBizResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_with_options_async(request, runtime)

    def delete_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.DeleteCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteCcRouteRulesResponse().from_map(
            self.do_rpcrequest('DeleteCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('DeleteCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cc_route_rules(
        self,
        request: gameshield_20180305_models.DeleteCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DeleteCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cc_route_rules_with_options(request, runtime)

    async def delete_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.DeleteCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DeleteCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cc_route_rules_with_options_async(request, runtime)

    def delete_flex_acc_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.DeleteFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteFlexAccFwdRuleResponse().from_map(
            self.do_rpcrequest('DeleteFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flex_acc_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteFlexAccFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flex_acc_fwd_rule(
        self,
        request: gameshield_20180305_models.DeleteFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.DeleteFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flex_acc_fwd_rule_with_options(request, runtime)

    async def delete_flex_acc_fwd_rule_async(
        self,
        request: gameshield_20180305_models.DeleteFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.DeleteFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flex_acc_fwd_rule_with_options_async(request, runtime)

    def delete_flex_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.DeleteFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteFlexFwdRuleResponse().from_map(
            self.do_rpcrequest('DeleteFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flex_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteFlexFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flex_fwd_rule(
        self,
        request: gameshield_20180305_models.DeleteFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.DeleteFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flex_fwd_rule_with_options(request, runtime)

    async def delete_flex_fwd_rule_async(
        self,
        request: gameshield_20180305_models.DeleteFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.DeleteFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flex_fwd_rule_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: gameshield_20180305_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteGroupResponse().from_map(
            self.do_rpcrequest('DeleteGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group(
        self,
        request: gameshield_20180305_models.DeleteGroupRequest,
    ) -> gameshield_20180305_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: gameshield_20180305_models.DeleteGroupRequest,
    ) -> gameshield_20180305_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_layer_4rule_with_options(
        self,
        request: gameshield_20180305_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteLayer4RuleResponse().from_map(
            self.do_rpcrequest('DeleteLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_layer_4rule_with_options_async(
        self,
        request: gameshield_20180305_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DeleteLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_layer_4rule(
        self,
        request: gameshield_20180305_models.DeleteLayer4RuleRequest,
    ) -> gameshield_20180305_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    async def delete_layer_4rule_async(
        self,
        request: gameshield_20180305_models.DeleteLayer4RuleRequest,
    ) -> gameshield_20180305_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_4rule_with_options_async(request, runtime)

    def describe_acc_res_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeAccResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAccResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAccResSummaryResponse().from_map(
            self.do_rpcrequest('DescribeAccResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_acc_res_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAccResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAccResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAccResSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acc_res_summary(
        self,
        request: gameshield_20180305_models.DescribeAccResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeAccResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_acc_res_summary_with_options(request, runtime)

    async def describe_acc_res_summary_async(
        self,
        request: gameshield_20180305_models.DescribeAccResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeAccResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_acc_res_summary_with_options_async(request, runtime)

    def describe_all_local_ips_with_options(
        self,
        request: gameshield_20180305_models.DescribeAllLocalIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAllLocalIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAllLocalIpsResponse().from_map(
            self.do_rpcrequest('DescribeAllLocalIps', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_local_ips_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAllLocalIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAllLocalIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAllLocalIpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllLocalIps', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_local_ips(
        self,
        request: gameshield_20180305_models.DescribeAllLocalIpsRequest,
    ) -> gameshield_20180305_models.DescribeAllLocalIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_local_ips_with_options(request, runtime)

    async def describe_all_local_ips_async(
        self,
        request: gameshield_20180305_models.DescribeAllLocalIpsRequest,
    ) -> gameshield_20180305_models.DescribeAllLocalIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_local_ips_with_options_async(request, runtime)

    def describe_app_daily_details_with_options(
        self,
        request: gameshield_20180305_models.DescribeAppDailyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppDailyDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppDailyDetailsResponse().from_map(
            self.do_rpcrequest('DescribeAppDailyDetails', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_daily_details_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAppDailyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppDailyDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppDailyDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppDailyDetails', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_daily_details(
        self,
        request: gameshield_20180305_models.DescribeAppDailyDetailsRequest,
    ) -> gameshield_20180305_models.DescribeAppDailyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_daily_details_with_options(request, runtime)

    async def describe_app_daily_details_async(
        self,
        request: gameshield_20180305_models.DescribeAppDailyDetailsRequest,
    ) -> gameshield_20180305_models.DescribeAppDailyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_daily_details_with_options_async(request, runtime)

    def describe_app_daily_sdk_versions_with_options(
        self,
        request: gameshield_20180305_models.DescribeAppDailySdkVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppDailySdkVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppDailySdkVersionsResponse().from_map(
            self.do_rpcrequest('DescribeAppDailySdkVersions', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_daily_sdk_versions_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAppDailySdkVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppDailySdkVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppDailySdkVersionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppDailySdkVersions', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_daily_sdk_versions(
        self,
        request: gameshield_20180305_models.DescribeAppDailySdkVersionsRequest,
    ) -> gameshield_20180305_models.DescribeAppDailySdkVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_daily_sdk_versions_with_options(request, runtime)

    async def describe_app_daily_sdk_versions_async(
        self,
        request: gameshield_20180305_models.DescribeAppDailySdkVersionsRequest,
    ) -> gameshield_20180305_models.DescribeAppDailySdkVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_daily_sdk_versions_with_options_async(request, runtime)

    def describe_app_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppListResponse().from_map(
            self.do_rpcrequest('DescribeAppList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppListResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_list(
        self,
        request: gameshield_20180305_models.DescribeAppListRequest,
    ) -> gameshield_20180305_models.DescribeAppListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_list_with_options(request, runtime)

    async def describe_app_list_async(
        self,
        request: gameshield_20180305_models.DescribeAppListRequest,
    ) -> gameshield_20180305_models.DescribeAppListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_list_with_options_async(request, runtime)

    def describe_app_simple_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeAppSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppSimpleListResponse().from_map(
            self.do_rpcrequest('DescribeAppSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_simple_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAppSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAppSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAppSimpleListResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_simple_list(
        self,
        request: gameshield_20180305_models.DescribeAppSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeAppSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_simple_list_with_options(request, runtime)

    async def describe_app_simple_list_async(
        self,
        request: gameshield_20180305_models.DescribeAppSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeAppSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_simple_list_with_options_async(request, runtime)

    def describe_async_operation_with_options(
        self,
        request: gameshield_20180305_models.DescribeAsyncOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAsyncOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAsyncOperationResponse().from_map(
            self.do_rpcrequest('DescribeAsyncOperation', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_async_operation_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAsyncOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAsyncOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAsyncOperationResponse().from_map(
            await self.do_rpcrequest_async('DescribeAsyncOperation', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_async_operation(
        self,
        request: gameshield_20180305_models.DescribeAsyncOperationRequest,
    ) -> gameshield_20180305_models.DescribeAsyncOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_async_operation_with_options(request, runtime)

    async def describe_async_operation_async(
        self,
        request: gameshield_20180305_models.DescribeAsyncOperationRequest,
    ) -> gameshield_20180305_models.DescribeAsyncOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_async_operation_with_options_async(request, runtime)

    def describe_automatic_traceability_sls_log_with_options(
        self,
        request: gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse().from_map(
            self.do_rpcrequest('DescribeAutomaticTraceabilitySlsLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_automatic_traceability_sls_log_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutomaticTraceabilitySlsLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_automatic_traceability_sls_log(
        self,
        request: gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogRequest,
    ) -> gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_automatic_traceability_sls_log_with_options(request, runtime)

    async def describe_automatic_traceability_sls_log_async(
        self,
        request: gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogRequest,
    ) -> gameshield_20180305_models.DescribeAutomaticTraceabilitySlsLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_automatic_traceability_sls_log_with_options_async(request, runtime)

    def describe_bgp_res_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeBgpResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBgpResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBgpResSummaryResponse().from_map(
            self.do_rpcrequest('DescribeBgpResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_res_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeBgpResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBgpResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBgpResSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_res_summary(
        self,
        request: gameshield_20180305_models.DescribeBgpResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeBgpResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_res_summary_with_options(request, runtime)

    async def describe_bgp_res_summary_async(
        self,
        request: gameshield_20180305_models.DescribeBgpResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeBgpResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_res_summary_with_options_async(request, runtime)

    def describe_biz_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeBizListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBizListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBizListResponse().from_map(
            self.do_rpcrequest('DescribeBizList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeBizListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBizListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBizListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBizList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_list(
        self,
        request: gameshield_20180305_models.DescribeBizListRequest,
    ) -> gameshield_20180305_models.DescribeBizListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_list_with_options(request, runtime)

    async def describe_biz_list_async(
        self,
        request: gameshield_20180305_models.DescribeBizListRequest,
    ) -> gameshield_20180305_models.DescribeBizListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_list_with_options_async(request, runtime)

    def describe_biz_simple_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeBizSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBizSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBizSimpleListResponse().from_map(
            self.do_rpcrequest('DescribeBizSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_simple_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeBizSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBizSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBizSimpleListResponse().from_map(
            await self.do_rpcrequest_async('DescribeBizSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_simple_list(
        self,
        request: gameshield_20180305_models.DescribeBizSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeBizSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_simple_list_with_options(request, runtime)

    async def describe_biz_simple_list_async(
        self,
        request: gameshield_20180305_models.DescribeBizSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeBizSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_simple_list_with_options_async(request, runtime)

    def describe_bps_flow_with_options(
        self,
        request: gameshield_20180305_models.DescribeBpsFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBpsFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBpsFlowResponse().from_map(
            self.do_rpcrequest('DescribeBpsFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bps_flow_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeBpsFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeBpsFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeBpsFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeBpsFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bps_flow(
        self,
        request: gameshield_20180305_models.DescribeBpsFlowRequest,
    ) -> gameshield_20180305_models.DescribeBpsFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bps_flow_with_options(request, runtime)

    async def describe_bps_flow_async(
        self,
        request: gameshield_20180305_models.DescribeBpsFlowRequest,
    ) -> gameshield_20180305_models.DescribeBpsFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bps_flow_with_options_async(request, runtime)

    def describe_cc_black_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcBlackListResponse().from_map(
            self.do_rpcrequest('DescribeCcBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_black_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcBlackListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_black_list(
        self,
        request: gameshield_20180305_models.DescribeCcBlackListRequest,
    ) -> gameshield_20180305_models.DescribeCcBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_black_list_with_options(request, runtime)

    async def describe_cc_black_list_async(
        self,
        request: gameshield_20180305_models.DescribeCcBlackListRequest,
    ) -> gameshield_20180305_models.DescribeCcBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_black_list_with_options_async(request, runtime)

    def describe_cc_devie_ip_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcDevieIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcDevieIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcDevieIpListResponse().from_map(
            self.do_rpcrequest('DescribeCcDevieIpList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_devie_ip_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcDevieIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcDevieIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcDevieIpListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcDevieIpList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_devie_ip_list(
        self,
        request: gameshield_20180305_models.DescribeCcDevieIpListRequest,
    ) -> gameshield_20180305_models.DescribeCcDevieIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_devie_ip_list_with_options(request, runtime)

    async def describe_cc_devie_ip_list_async(
        self,
        request: gameshield_20180305_models.DescribeCcDevieIpListRequest,
    ) -> gameshield_20180305_models.DescribeCcDevieIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_devie_ip_list_with_options_async(request, runtime)

    def describe_cc_flow_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcFlowResponse().from_map(
            self.do_rpcrequest('DescribeCcFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_flow_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_flow(
        self,
        request: gameshield_20180305_models.DescribeCcFlowRequest,
    ) -> gameshield_20180305_models.DescribeCcFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_flow_with_options(request, runtime)

    async def describe_cc_flow_async(
        self,
        request: gameshield_20180305_models.DescribeCcFlowRequest,
    ) -> gameshield_20180305_models.DescribeCcFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_flow_with_options_async(request, runtime)

    def describe_cc_idcblock_switch_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcIDCBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse().from_map(
            self.do_rpcrequest('DescribeCcIDCBlockSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_idcblock_switch_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcIDCBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcIDCBlockSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_idcblock_switch(
        self,
        request: gameshield_20180305_models.DescribeCcIDCBlockSwitchRequest,
    ) -> gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_idcblock_switch_with_options(request, runtime)

    async def describe_cc_idcblock_switch_async(
        self,
        request: gameshield_20180305_models.DescribeCcIDCBlockSwitchRequest,
    ) -> gameshield_20180305_models.DescribeCcIDCBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_idcblock_switch_with_options_async(request, runtime)

    def describe_cc_max_fw_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcMaxFwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcMaxFwResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcMaxFwResponse().from_map(
            self.do_rpcrequest('DescribeCcMaxFw', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_max_fw_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcMaxFwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcMaxFwResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcMaxFwResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcMaxFw', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_max_fw(
        self,
        request: gameshield_20180305_models.DescribeCcMaxFwRequest,
    ) -> gameshield_20180305_models.DescribeCcMaxFwResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_max_fw_with_options(request, runtime)

    async def describe_cc_max_fw_async(
        self,
        request: gameshield_20180305_models.DescribeCcMaxFwRequest,
    ) -> gameshield_20180305_models.DescribeCcMaxFwResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_max_fw_with_options_async(request, runtime)

    def describe_cc_res_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcResSummaryResponse().from_map(
            self.do_rpcrequest('DescribeCcResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_res_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcResSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_res_summary(
        self,
        request: gameshield_20180305_models.DescribeCcResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeCcResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_res_summary_with_options(request, runtime)

    async def describe_cc_res_summary_async(
        self,
        request: gameshield_20180305_models.DescribeCcResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeCcResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_res_summary_with_options_async(request, runtime)

    def describe_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcRouteRulesResponse().from_map(
            self.do_rpcrequest('DescribeCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_route_rules(
        self,
        request: gameshield_20180305_models.DescribeCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DescribeCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_route_rules_with_options(request, runtime)

    async def describe_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.DescribeCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DescribeCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_route_rules_with_options_async(request, runtime)

    def describe_cc_route_switch_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcRouteSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcRouteSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcRouteSwitchResponse().from_map(
            self.do_rpcrequest('DescribeCcRouteSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_route_switch_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcRouteSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcRouteSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcRouteSwitchResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcRouteSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_route_switch(
        self,
        request: gameshield_20180305_models.DescribeCcRouteSwitchRequest,
    ) -> gameshield_20180305_models.DescribeCcRouteSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_route_switch_with_options(request, runtime)

    async def describe_cc_route_switch_async(
        self,
        request: gameshield_20180305_models.DescribeCcRouteSwitchRequest,
    ) -> gameshield_20180305_models.DescribeCcRouteSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_route_switch_with_options_async(request, runtime)

    def describe_cc_socket_detail_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcSocketDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcSocketDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcSocketDetailResponse().from_map(
            self.do_rpcrequest('DescribeCcSocketDetail', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_socket_detail_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcSocketDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcSocketDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcSocketDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcSocketDetail', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_socket_detail(
        self,
        request: gameshield_20180305_models.DescribeCcSocketDetailRequest,
    ) -> gameshield_20180305_models.DescribeCcSocketDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_socket_detail_with_options(request, runtime)

    async def describe_cc_socket_detail_async(
        self,
        request: gameshield_20180305_models.DescribeCcSocketDetailRequest,
    ) -> gameshield_20180305_models.DescribeCcSocketDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_socket_detail_with_options_async(request, runtime)

    def describe_cc_total_fw_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcTotalFwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcTotalFwResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcTotalFwResponse().from_map(
            self.do_rpcrequest('DescribeCcTotalFw', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_total_fw_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcTotalFwRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcTotalFwResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcTotalFwResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcTotalFw', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_total_fw(
        self,
        request: gameshield_20180305_models.DescribeCcTotalFwRequest,
    ) -> gameshield_20180305_models.DescribeCcTotalFwResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_total_fw_with_options(request, runtime)

    async def describe_cc_total_fw_async(
        self,
        request: gameshield_20180305_models.DescribeCcTotalFwRequest,
    ) -> gameshield_20180305_models.DescribeCcTotalFwResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_total_fw_with_options_async(request, runtime)

    def describe_cc_tunnel_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcTunnelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcTunnelResponse().from_map(
            self.do_rpcrequest('DescribeCcTunnel', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_tunnel_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcTunnelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcTunnelResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcTunnel', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_tunnel(
        self,
        request: gameshield_20180305_models.DescribeCcTunnelRequest,
    ) -> gameshield_20180305_models.DescribeCcTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_tunnel_with_options(request, runtime)

    async def describe_cc_tunnel_async(
        self,
        request: gameshield_20180305_models.DescribeCcTunnelRequest,
    ) -> gameshield_20180305_models.DescribeCcTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_tunnel_with_options_async(request, runtime)

    def describe_cc_white_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcWhiteListResponse().from_map(
            self.do_rpcrequest('DescribeCcWhiteList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_white_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcWhiteListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcWhiteList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_white_list(
        self,
        request: gameshield_20180305_models.DescribeCcWhiteListRequest,
    ) -> gameshield_20180305_models.DescribeCcWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_white_list_with_options(request, runtime)

    async def describe_cc_white_list_async(
        self,
        request: gameshield_20180305_models.DescribeCcWhiteListRequest,
    ) -> gameshield_20180305_models.DescribeCcWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_white_list_with_options_async(request, runtime)

    def describe_cc_zone_block_config_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcZoneBlockConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcZoneBlockConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcZoneBlockConfigResponse().from_map(
            self.do_rpcrequest('DescribeCcZoneBlockConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_zone_block_config_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcZoneBlockConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcZoneBlockConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcZoneBlockConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcZoneBlockConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_zone_block_config(
        self,
        request: gameshield_20180305_models.DescribeCcZoneBlockConfigRequest,
    ) -> gameshield_20180305_models.DescribeCcZoneBlockConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_zone_block_config_with_options(request, runtime)

    async def describe_cc_zone_block_config_async(
        self,
        request: gameshield_20180305_models.DescribeCcZoneBlockConfigRequest,
    ) -> gameshield_20180305_models.DescribeCcZoneBlockConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_zone_block_config_with_options_async(request, runtime)

    def describe_cc_zones_with_options(
        self,
        request: gameshield_20180305_models.DescribeCcZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcZonesResponse().from_map(
            self.do_rpcrequest('DescribeCcZones', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cc_zones_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeCcZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeCcZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeCcZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCcZones', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cc_zones(
        self,
        request: gameshield_20180305_models.DescribeCcZonesRequest,
    ) -> gameshield_20180305_models.DescribeCcZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cc_zones_with_options(request, runtime)

    async def describe_cc_zones_async(
        self,
        request: gameshield_20180305_models.DescribeCcZonesRequest,
    ) -> gameshield_20180305_models.DescribeCcZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cc_zones_with_options_async(request, runtime)

    def describe_daily_details_with_options(
        self,
        request: gameshield_20180305_models.DescribeDailyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDailyDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDailyDetailsResponse().from_map(
            self.do_rpcrequest('DescribeDailyDetails', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_daily_details_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeDailyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDailyDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDailyDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDailyDetails', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_daily_details(
        self,
        request: gameshield_20180305_models.DescribeDailyDetailsRequest,
    ) -> gameshield_20180305_models.DescribeDailyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_daily_details_with_options(request, runtime)

    async def describe_daily_details_async(
        self,
        request: gameshield_20180305_models.DescribeDailyDetailsRequest,
    ) -> gameshield_20180305_models.DescribeDailyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_daily_details_with_options_async(request, runtime)

    def describe_download_urls_for_app_key_with_options(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse().from_map(
            self.do_rpcrequest('DescribeDownloadUrlsForAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_download_urls_for_app_key_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDownloadUrlsForAppKey', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_download_urls_for_app_key(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForAppKeyRequest,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_urls_for_app_key_with_options(request, runtime)

    async def describe_download_urls_for_app_key_async(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForAppKeyRequest,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_urls_for_app_key_with_options_async(request, runtime)

    def describe_download_urls_for_sdkwith_options(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse().from_map(
            self.do_rpcrequest('DescribeDownloadUrlsForSDK', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_download_urls_for_sdkwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse().from_map(
            await self.do_rpcrequest_async('DescribeDownloadUrlsForSDK', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_download_urls_for_sdk(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForSDKRequest,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_urls_for_sdkwith_options(request, runtime)

    async def describe_download_urls_for_sdk_async(
        self,
        request: gameshield_20180305_models.DescribeDownloadUrlsForSDKRequest,
    ) -> gameshield_20180305_models.DescribeDownloadUrlsForSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_urls_for_sdkwith_options_async(request, runtime)

    def describe_flex_acc_config_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexAccConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccConfigResponse().from_map(
            self.do_rpcrequest('DescribeFlexAccConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_acc_config_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexAccConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_acc_config(
        self,
        request: gameshield_20180305_models.DescribeFlexAccConfigRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_acc_config_with_options(request, runtime)

    async def describe_flex_acc_config_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccConfigRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_acc_config_with_options_async(request, runtime)

    def describe_flex_acc_flow_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccFlowResponse().from_map(
            self.do_rpcrequest('DescribeFlexAccFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_acc_flow_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexAccFlow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_acc_flow(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFlowRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_acc_flow_with_options(request, runtime)

    async def describe_flex_acc_flow_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFlowRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_acc_flow_with_options_async(request, runtime)

    def describe_flex_acc_fwd_rules_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccFwdRulesResponse().from_map(
            self.do_rpcrequest('DescribeFlexAccFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_acc_fwd_rules_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexAccFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexAccFwdRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexAccFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_acc_fwd_rules(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFwdRulesRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_acc_fwd_rules_with_options(request, runtime)

    async def describe_flex_acc_fwd_rules_async(
        self,
        request: gameshield_20180305_models.DescribeFlexAccFwdRulesRequest,
    ) -> gameshield_20180305_models.DescribeFlexAccFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_acc_fwd_rules_with_options_async(request, runtime)

    def describe_flex_backup_groups_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexBackupGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexBackupGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexBackupGroupsResponse().from_map(
            self.do_rpcrequest('DescribeFlexBackupGroups', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_backup_groups_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexBackupGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexBackupGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexBackupGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexBackupGroups', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_backup_groups(
        self,
        request: gameshield_20180305_models.DescribeFlexBackupGroupsRequest,
    ) -> gameshield_20180305_models.DescribeFlexBackupGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_backup_groups_with_options(request, runtime)

    async def describe_flex_backup_groups_async(
        self,
        request: gameshield_20180305_models.DescribeFlexBackupGroupsRequest,
    ) -> gameshield_20180305_models.DescribeFlexBackupGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_backup_groups_with_options_async(request, runtime)

    def describe_flex_config_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexConfigResponse().from_map(
            self.do_rpcrequest('DescribeFlexConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_config_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_config(
        self,
        request: gameshield_20180305_models.DescribeFlexConfigRequest,
    ) -> gameshield_20180305_models.DescribeFlexConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_config_with_options(request, runtime)

    async def describe_flex_config_async(
        self,
        request: gameshield_20180305_models.DescribeFlexConfigRequest,
    ) -> gameshield_20180305_models.DescribeFlexConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_config_with_options_async(request, runtime)

    def describe_flex_fwd_rules_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexFwdRulesResponse().from_map(
            self.do_rpcrequest('DescribeFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_fwd_rules_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexFwdRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_fwd_rules(
        self,
        request: gameshield_20180305_models.DescribeFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.DescribeFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_fwd_rules_with_options(request, runtime)

    async def describe_flex_fwd_rules_async(
        self,
        request: gameshield_20180305_models.DescribeFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.DescribeFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_fwd_rules_with_options_async(request, runtime)

    def describe_flex_seched_policy_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlexSechedPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexSechedPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexSechedPolicyResponse().from_map(
            self.do_rpcrequest('DescribeFlexSechedPolicy', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flex_seched_policy_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlexSechedPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlexSechedPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlexSechedPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexSechedPolicy', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flex_seched_policy(
        self,
        request: gameshield_20180305_models.DescribeFlexSechedPolicyRequest,
    ) -> gameshield_20180305_models.DescribeFlexSechedPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flex_seched_policy_with_options(request, runtime)

    async def describe_flex_seched_policy_async(
        self,
        request: gameshield_20180305_models.DescribeFlexSechedPolicyRequest,
    ) -> gameshield_20180305_models.DescribeFlexSechedPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flex_seched_policy_with_options_async(request, runtime)

    def describe_flow_report_with_options(
        self,
        request: gameshield_20180305_models.DescribeFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlowReportResponse().from_map(
            self.do_rpcrequest('DescribeFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_report_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFlowReportResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_report(
        self,
        request: gameshield_20180305_models.DescribeFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_report_with_options(request, runtime)

    async def describe_flow_report_async(
        self,
        request: gameshield_20180305_models.DescribeFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_report_with_options_async(request, runtime)

    def describe_full_nodes_with_options(
        self,
        request: gameshield_20180305_models.DescribeFullNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFullNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFullNodesResponse().from_map(
            self.do_rpcrequest('DescribeFullNodes', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_full_nodes_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFullNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFullNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFullNodesResponse().from_map(
            await self.do_rpcrequest_async('DescribeFullNodes', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_full_nodes(
        self,
        request: gameshield_20180305_models.DescribeFullNodesRequest,
    ) -> gameshield_20180305_models.DescribeFullNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_full_nodes_with_options(request, runtime)

    async def describe_full_nodes_async(
        self,
        request: gameshield_20180305_models.DescribeFullNodesRequest,
    ) -> gameshield_20180305_models.DescribeFullNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_full_nodes_with_options_async(request, runtime)

    def describe_full_nodes_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeFullNodesSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFullNodesSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFullNodesSummaryResponse().from_map(
            self.do_rpcrequest('DescribeFullNodesSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_full_nodes_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeFullNodesSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeFullNodesSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeFullNodesSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeFullNodesSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_full_nodes_summary(
        self,
        request: gameshield_20180305_models.DescribeFullNodesSummaryRequest,
    ) -> gameshield_20180305_models.DescribeFullNodesSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_full_nodes_summary_with_options(request, runtime)

    async def describe_full_nodes_summary_async(
        self,
        request: gameshield_20180305_models.DescribeFullNodesSummaryRequest,
    ) -> gameshield_20180305_models.DescribeFullNodesSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_full_nodes_summary_with_options_async(request, runtime)

    def describe_gf_res_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeGfResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGfResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGfResSummaryResponse().from_map(
            self.do_rpcrequest('DescribeGfResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_gf_res_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeGfResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGfResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGfResSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeGfResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_gf_res_summary(
        self,
        request: gameshield_20180305_models.DescribeGfResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeGfResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gf_res_summary_with_options(request, runtime)

    async def describe_gf_res_summary_async(
        self,
        request: gameshield_20180305_models.DescribeGfResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeGfResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gf_res_summary_with_options_async(request, runtime)

    def describe_group_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGroupListResponse().from_map(
            self.do_rpcrequest('DescribeGroupList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_group_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGroupListResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_group_list(
        self,
        request: gameshield_20180305_models.DescribeGroupListRequest,
    ) -> gameshield_20180305_models.DescribeGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_group_list_with_options(request, runtime)

    async def describe_group_list_async(
        self,
        request: gameshield_20180305_models.DescribeGroupListRequest,
    ) -> gameshield_20180305_models.DescribeGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_list_with_options_async(request, runtime)

    def describe_group_simple_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeGroupSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGroupSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGroupSimpleListResponse().from_map(
            self.do_rpcrequest('DescribeGroupSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_group_simple_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeGroupSimpleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeGroupSimpleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeGroupSimpleListResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupSimpleList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_group_simple_list(
        self,
        request: gameshield_20180305_models.DescribeGroupSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeGroupSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_group_simple_list_with_options(request, runtime)

    async def describe_group_simple_list_async(
        self,
        request: gameshield_20180305_models.DescribeGroupSimpleListRequest,
    ) -> gameshield_20180305_models.DescribeGroupSimpleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_simple_list_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: gameshield_20180305_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeInstanceResponse().from_map(
            self.do_rpcrequest('DescribeInstance', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstance', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance(
        self,
        request: gameshield_20180305_models.DescribeInstanceRequest,
    ) -> gameshield_20180305_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: gameshield_20180305_models.DescribeInstanceRequest,
    ) -> gameshield_20180305_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_ip_flow_report_with_options(
        self,
        request: gameshield_20180305_models.DescribeIpFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeIpFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeIpFlowReportResponse().from_map(
            self.do_rpcrequest('DescribeIpFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_flow_report_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeIpFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeIpFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeIpFlowReportResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_flow_report(
        self,
        request: gameshield_20180305_models.DescribeIpFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeIpFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_flow_report_with_options(request, runtime)

    async def describe_ip_flow_report_async(
        self,
        request: gameshield_20180305_models.DescribeIpFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeIpFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_flow_report_with_options_async(request, runtime)

    def describe_jian_yu_test_get_with_options(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestGetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestGetResponse().from_map(
            self.do_rpcrequest('DescribeJianYuTestGet', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_jian_yu_test_get_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestGetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestGetResponse().from_map(
            await self.do_rpcrequest_async('DescribeJianYuTestGet', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_jian_yu_test_get(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestGetRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestGetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_jian_yu_test_get_with_options(request, runtime)

    async def describe_jian_yu_test_get_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestGetRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestGetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_jian_yu_test_get_with_options_async(request, runtime)

    def describe_jian_yu_test_list_with_options(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestListResponse().from_map(
            self.do_rpcrequest('DescribeJianYuTestList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_jian_yu_test_list_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestListResponse().from_map(
            await self.do_rpcrequest_async('DescribeJianYuTestList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_jian_yu_test_list(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestListRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_jian_yu_test_list_with_options(request, runtime)

    async def describe_jian_yu_test_list_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestListRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_jian_yu_test_list_with_options_async(request, runtime)

    def describe_jian_yu_test_pagination_with_options(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestPaginationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestPaginationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestPaginationResponse().from_map(
            self.do_rpcrequest('DescribeJianYuTestPagination', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_jian_yu_test_pagination_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestPaginationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeJianYuTestPaginationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeJianYuTestPaginationResponse().from_map(
            await self.do_rpcrequest_async('DescribeJianYuTestPagination', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_jian_yu_test_pagination(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestPaginationRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestPaginationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_jian_yu_test_pagination_with_options(request, runtime)

    async def describe_jian_yu_test_pagination_async(
        self,
        request: gameshield_20180305_models.DescribeJianYuTestPaginationRequest,
    ) -> gameshield_20180305_models.DescribeJianYuTestPaginationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_jian_yu_test_pagination_with_options_async(request, runtime)

    def describe_l4events_selective_with_options(
        self,
        request: gameshield_20180305_models.DescribeL4EventsSelectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeL4EventsSelectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeL4EventsSelectiveResponse().from_map(
            self.do_rpcrequest('DescribeL4EventsSelective', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_l4events_selective_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeL4EventsSelectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeL4EventsSelectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeL4EventsSelectiveResponse().from_map(
            await self.do_rpcrequest_async('DescribeL4EventsSelective', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_l4events_selective(
        self,
        request: gameshield_20180305_models.DescribeL4EventsSelectiveRequest,
    ) -> gameshield_20180305_models.DescribeL4EventsSelectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_l4events_selective_with_options(request, runtime)

    async def describe_l4events_selective_async(
        self,
        request: gameshield_20180305_models.DescribeL4EventsSelectiveRequest,
    ) -> gameshield_20180305_models.DescribeL4EventsSelectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_l4events_selective_with_options_async(request, runtime)

    def describe_layer_4rules_with_options(
        self,
        request: gameshield_20180305_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeLayer4RulesResponse().from_map(
            self.do_rpcrequest('DescribeLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_layer_4rules_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeLayer4RulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_layer_4rules(
        self,
        request: gameshield_20180305_models.DescribeLayer4RulesRequest,
    ) -> gameshield_20180305_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    async def describe_layer_4rules_async(
        self,
        request: gameshield_20180305_models.DescribeLayer4RulesRequest,
    ) -> gameshield_20180305_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rules_with_options_async(request, runtime)

    def describe_mian_liu_res_summary_with_options(
        self,
        request: gameshield_20180305_models.DescribeMianLiuResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeMianLiuResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeMianLiuResSummaryResponse().from_map(
            self.do_rpcrequest('DescribeMianLiuResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mian_liu_res_summary_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeMianLiuResSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeMianLiuResSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeMianLiuResSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeMianLiuResSummary', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mian_liu_res_summary(
        self,
        request: gameshield_20180305_models.DescribeMianLiuResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeMianLiuResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mian_liu_res_summary_with_options(request, runtime)

    async def describe_mian_liu_res_summary_async(
        self,
        request: gameshield_20180305_models.DescribeMianLiuResSummaryRequest,
    ) -> gameshield_20180305_models.DescribeMianLiuResSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mian_liu_res_summary_with_options_async(request, runtime)

    def describe_ng_source_diagnosis_log_with_options(
        self,
        request: gameshield_20180305_models.DescribeNgSourceDiagnosisLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse().from_map(
            self.do_rpcrequest('DescribeNgSourceDiagnosisLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ng_source_diagnosis_log_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeNgSourceDiagnosisLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeNgSourceDiagnosisLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ng_source_diagnosis_log(
        self,
        request: gameshield_20180305_models.DescribeNgSourceDiagnosisLogRequest,
    ) -> gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ng_source_diagnosis_log_with_options(request, runtime)

    async def describe_ng_source_diagnosis_log_async(
        self,
        request: gameshield_20180305_models.DescribeNgSourceDiagnosisLogRequest,
    ) -> gameshield_20180305_models.DescribeNgSourceDiagnosisLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ng_source_diagnosis_log_with_options_async(request, runtime)

    def describe_remain_qps_with_options(
        self,
        request: gameshield_20180305_models.DescribeRemainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRemainQpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRemainQpsResponse().from_map(
            self.do_rpcrequest('DescribeRemainQps', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_remain_qps_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeRemainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRemainQpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRemainQpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRemainQps', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_remain_qps(
        self,
        request: gameshield_20180305_models.DescribeRemainQpsRequest,
    ) -> gameshield_20180305_models.DescribeRemainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_remain_qps_with_options(request, runtime)

    async def describe_remain_qps_async(
        self,
        request: gameshield_20180305_models.DescribeRemainQpsRequest,
    ) -> gameshield_20180305_models.DescribeRemainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_remain_qps_with_options_async(request, runtime)

    def describe_request_statistic_by_esn_biz_interval_with_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticByEsnBizInterval', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_by_esn_biz_interval_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticByEsnBizInterval', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_by_esn_biz_interval(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_by_esn_biz_interval_with_options(request, runtime)

    async def describe_request_statistic_by_esn_biz_interval_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticByEsnBizIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_by_esn_biz_interval_with_options_async(request, runtime)

    def describe_request_statistic_count_by_esn_biz_1day_with_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticCountByEsnBiz1Day', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_count_by_esn_biz_1day_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticCountByEsnBiz1Day', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_count_by_esn_biz_1day(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_count_by_esn_biz_1day_with_options(request, runtime)

    async def describe_request_statistic_count_by_esn_biz_1day_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_count_by_esn_biz_1day_with_options_async(request, runtime)

    def describe_request_statistic_count_by_esn_biz_1day_province_with_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticCountByEsnBiz1DayProvince', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_count_by_esn_biz_1day_province_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticCountByEsnBiz1DayProvince', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_count_by_esn_biz_1day_province(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_count_by_esn_biz_1day_province_with_options(request, runtime)

    async def describe_request_statistic_count_by_esn_biz_1day_province_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1DayProvinceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_count_by_esn_biz_1day_province_with_options_async(request, runtime)

    def describe_request_statistic_count_by_esn_biz_1m30mwith_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticCountByEsnBiz1M30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_count_by_esn_biz_1m30mwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticCountByEsnBiz1M30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_count_by_esn_biz_1m30m(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_count_by_esn_biz_1m30mwith_options(request, runtime)

    async def describe_request_statistic_count_by_esn_biz_1m30m_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz1M30MResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_count_by_esn_biz_1m30mwith_options_async(request, runtime)

    def describe_request_statistic_count_by_esn_biz_30mwith_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticCountByEsnBiz30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_count_by_esn_biz_30mwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticCountByEsnBiz30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_count_by_esn_biz_30m(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_count_by_esn_biz_30mwith_options(request, runtime)

    async def describe_request_statistic_count_by_esn_biz_30m_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBiz30MResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_count_by_esn_biz_30mwith_options_async(request, runtime)

    def describe_request_statistic_count_by_esn_biz_group_30mwith_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticCountByEsnBizGroup30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_count_by_esn_biz_group_30mwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticCountByEsnBizGroup30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_count_by_esn_biz_group_30m(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_count_by_esn_biz_group_30mwith_options(request, runtime)

    async def describe_request_statistic_count_by_esn_biz_group_30m_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticCountByEsnBizGroup30MResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_count_by_esn_biz_group_30mwith_options_async(request, runtime)

    def describe_request_statistic_log_with_options(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticLogResponse().from_map(
            self.do_rpcrequest('DescribeRequestStatisticLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_statistic_log_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeRequestStatisticLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeRequestStatisticLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestStatisticLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_statistic_log(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticLogRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_statistic_log_with_options(request, runtime)

    async def describe_request_statistic_log_async(
        self,
        request: gameshield_20180305_models.DescribeRequestStatisticLogRequest,
    ) -> gameshield_20180305_models.DescribeRequestStatisticLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_statistic_log_with_options_async(request, runtime)

    def describe_sdkstatistic_log_with_options(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticLogResponse().from_map(
            self.do_rpcrequest('DescribeSDKStatisticLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdkstatistic_log_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeSDKStatisticLog', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdkstatistic_log(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticLogRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkstatistic_log_with_options(request, runtime)

    async def describe_sdkstatistic_log_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticLogRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdkstatistic_log_with_options_async(request, runtime)

    def describe_sdkstatistic_result_by_esn_biz_isp1m30mwith_options(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse().from_map(
            self.do_rpcrequest('DescribeSDKStatisticResultByEsnBizISP1M30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdkstatistic_result_by_esn_biz_isp1m30mwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse().from_map(
            await self.do_rpcrequest_async('DescribeSDKStatisticResultByEsnBizISP1M30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdkstatistic_result_by_esn_biz_isp1m30m(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkstatistic_result_by_esn_biz_isp1m30mwith_options(request, runtime)

    async def describe_sdkstatistic_result_by_esn_biz_isp1m30m_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISP1M30MResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdkstatistic_result_by_esn_biz_isp1m30mwith_options_async(request, runtime)

    def describe_sdkstatistic_result_by_esn_biz_ispinterval_with_options(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse().from_map(
            self.do_rpcrequest('DescribeSDKStatisticResultByEsnBizISPInterval', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdkstatistic_result_by_esn_biz_ispinterval_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse().from_map(
            await self.do_rpcrequest_async('DescribeSDKStatisticResultByEsnBizISPInterval', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdkstatistic_result_by_esn_biz_ispinterval(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkstatistic_result_by_esn_biz_ispinterval_with_options(request, runtime)

    async def describe_sdkstatistic_result_by_esn_biz_ispinterval_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizISPIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdkstatistic_result_by_esn_biz_ispinterval_with_options_async(request, runtime)

    def describe_sdkstatistic_result_by_esn_biz_province_1day_with_options(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse().from_map(
            self.do_rpcrequest('DescribeSDKStatisticResultByEsnBizProvince1Day', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdkstatistic_result_by_esn_biz_province_1day_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse().from_map(
            await self.do_rpcrequest_async('DescribeSDKStatisticResultByEsnBizProvince1Day', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdkstatistic_result_by_esn_biz_province_1day(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkstatistic_result_by_esn_biz_province_1day_with_options(request, runtime)

    async def describe_sdkstatistic_result_by_esn_biz_province_1day_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince1DayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdkstatistic_result_by_esn_biz_province_1day_with_options_async(request, runtime)

    def describe_sdkstatistic_result_by_esn_biz_province_30mwith_options(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse().from_map(
            self.do_rpcrequest('DescribeSDKStatisticResultByEsnBizProvince30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdkstatistic_result_by_esn_biz_province_30mwith_options_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse().from_map(
            await self.do_rpcrequest_async('DescribeSDKStatisticResultByEsnBizProvince30M', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdkstatistic_result_by_esn_biz_province_30m(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkstatistic_result_by_esn_biz_province_30mwith_options(request, runtime)

    async def describe_sdkstatistic_result_by_esn_biz_province_30m_async(
        self,
        request: gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MRequest,
    ) -> gameshield_20180305_models.DescribeSDKStatisticResultByEsnBizProvince30MResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdkstatistic_result_by_esn_biz_province_30mwith_options_async(request, runtime)

    def describe_source_failure_top_ip_with_options(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSourceFailureTopIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSourceFailureTopIpResponse().from_map(
            self.do_rpcrequest('DescribeSourceFailureTopIp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_source_failure_top_ip_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSourceFailureTopIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSourceFailureTopIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeSourceFailureTopIp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_source_failure_top_ip(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTopIpRequest,
    ) -> gameshield_20180305_models.DescribeSourceFailureTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_source_failure_top_ip_with_options(request, runtime)

    async def describe_source_failure_top_ip_async(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTopIpRequest,
    ) -> gameshield_20180305_models.DescribeSourceFailureTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_source_failure_top_ip_with_options_async(request, runtime)

    def describe_source_failure_trend_graph_with_options(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse().from_map(
            self.do_rpcrequest('DescribeSourceFailureTrendGraph', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_source_failure_trend_graph_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse().from_map(
            await self.do_rpcrequest_async('DescribeSourceFailureTrendGraph', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_source_failure_trend_graph(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTrendGraphRequest,
    ) -> gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_source_failure_trend_graph_with_options(request, runtime)

    async def describe_source_failure_trend_graph_async(
        self,
        request: gameshield_20180305_models.DescribeSourceFailureTrendGraphRequest,
    ) -> gameshield_20180305_models.DescribeSourceFailureTrendGraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_source_failure_trend_graph_with_options_async(request, runtime)

    def describe_upload_pre_sign_with_options(
        self,
        request: gameshield_20180305_models.DescribeUploadPreSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUploadPreSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUploadPreSignResponse().from_map(
            self.do_rpcrequest('DescribeUploadPreSign', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_upload_pre_sign_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeUploadPreSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUploadPreSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUploadPreSignResponse().from_map(
            await self.do_rpcrequest_async('DescribeUploadPreSign', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upload_pre_sign(
        self,
        request: gameshield_20180305_models.DescribeUploadPreSignRequest,
    ) -> gameshield_20180305_models.DescribeUploadPreSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_pre_sign_with_options(request, runtime)

    async def describe_upload_pre_sign_async(
        self,
        request: gameshield_20180305_models.DescribeUploadPreSignRequest,
    ) -> gameshield_20180305_models.DescribeUploadPreSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_pre_sign_with_options_async(request, runtime)

    def describe_user_flow_info_with_options(
        self,
        request: gameshield_20180305_models.DescribeUserFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserFlowInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserFlowInfoResponse().from_map(
            self.do_rpcrequest('DescribeUserFlowInfo', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_flow_info_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeUserFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserFlowInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserFlowInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserFlowInfo', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_flow_info(
        self,
        request: gameshield_20180305_models.DescribeUserFlowInfoRequest,
    ) -> gameshield_20180305_models.DescribeUserFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_flow_info_with_options(request, runtime)

    async def describe_user_flow_info_async(
        self,
        request: gameshield_20180305_models.DescribeUserFlowInfoRequest,
    ) -> gameshield_20180305_models.DescribeUserFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_flow_info_with_options_async(request, runtime)

    def describe_user_flow_report_with_options(
        self,
        request: gameshield_20180305_models.DescribeUserFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserFlowReportResponse().from_map(
            self.do_rpcrequest('DescribeUserFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_flow_report_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeUserFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserFlowReportResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_flow_report(
        self,
        request: gameshield_20180305_models.DescribeUserFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeUserFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_flow_report_with_options(request, runtime)

    async def describe_user_flow_report_async(
        self,
        request: gameshield_20180305_models.DescribeUserFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeUserFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_flow_report_with_options_async(request, runtime)

    def describe_user_total_flow_report_with_options(
        self,
        request: gameshield_20180305_models.DescribeUserTotalFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserTotalFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserTotalFlowReportResponse().from_map(
            self.do_rpcrequest('DescribeUserTotalFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_total_flow_report_with_options_async(
        self,
        request: gameshield_20180305_models.DescribeUserTotalFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DescribeUserTotalFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DescribeUserTotalFlowReportResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserTotalFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_total_flow_report(
        self,
        request: gameshield_20180305_models.DescribeUserTotalFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeUserTotalFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_total_flow_report_with_options(request, runtime)

    async def describe_user_total_flow_report_async(
        self,
        request: gameshield_20180305_models.DescribeUserTotalFlowReportRequest,
    ) -> gameshield_20180305_models.DescribeUserTotalFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_total_flow_report_with_options_async(request, runtime)

    def download_app_key_file_with_options(
        self,
        request: gameshield_20180305_models.DownloadAppKeyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadAppKeyFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadAppKeyFileResponse().from_map(
            self.do_rpcrequest('DownloadAppKeyFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_app_key_file_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadAppKeyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadAppKeyFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadAppKeyFileResponse().from_map(
            await self.do_rpcrequest_async('DownloadAppKeyFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_app_key_file(
        self,
        request: gameshield_20180305_models.DownloadAppKeyFileRequest,
    ) -> gameshield_20180305_models.DownloadAppKeyFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_app_key_file_with_options(request, runtime)

    async def download_app_key_file_async(
        self,
        request: gameshield_20180305_models.DownloadAppKeyFileRequest,
    ) -> gameshield_20180305_models.DownloadAppKeyFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_app_key_file_with_options_async(request, runtime)

    def download_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.DownloadCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadCcRouteRulesResponse().from_map(
            self.do_rpcrequest('DownloadCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('DownloadCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_cc_route_rules(
        self,
        request: gameshield_20180305_models.DownloadCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DownloadCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_cc_route_rules_with_options(request, runtime)

    async def download_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.DownloadCcRouteRulesRequest,
    ) -> gameshield_20180305_models.DownloadCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_cc_route_rules_with_options_async(request, runtime)

    def download_flex_acc_rules_file_with_options(
        self,
        request: gameshield_20180305_models.DownloadFlexAccRulesFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadFlexAccRulesFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadFlexAccRulesFileResponse().from_map(
            self.do_rpcrequest('DownloadFlexAccRulesFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_flex_acc_rules_file_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadFlexAccRulesFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadFlexAccRulesFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadFlexAccRulesFileResponse().from_map(
            await self.do_rpcrequest_async('DownloadFlexAccRulesFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_flex_acc_rules_file(
        self,
        request: gameshield_20180305_models.DownloadFlexAccRulesFileRequest,
    ) -> gameshield_20180305_models.DownloadFlexAccRulesFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_flex_acc_rules_file_with_options(request, runtime)

    async def download_flex_acc_rules_file_async(
        self,
        request: gameshield_20180305_models.DownloadFlexAccRulesFileRequest,
    ) -> gameshield_20180305_models.DownloadFlexAccRulesFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_flex_acc_rules_file_with_options_async(request, runtime)

    def download_layer_4rules_with_options(
        self,
        request: gameshield_20180305_models.DownloadLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadLayer4RulesResponse().from_map(
            self.do_rpcrequest('DownloadLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_layer_4rules_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadLayer4RulesResponse().from_map(
            await self.do_rpcrequest_async('DownloadLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_layer_4rules(
        self,
        request: gameshield_20180305_models.DownloadLayer4RulesRequest,
    ) -> gameshield_20180305_models.DownloadLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_layer_4rules_with_options(request, runtime)

    async def download_layer_4rules_async(
        self,
        request: gameshield_20180305_models.DownloadLayer4RulesRequest,
    ) -> gameshield_20180305_models.DownloadLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_layer_4rules_with_options_async(request, runtime)

    def download_sdk_file_with_options(
        self,
        request: gameshield_20180305_models.DownloadSdkFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadSdkFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadSdkFileResponse().from_map(
            self.do_rpcrequest('DownloadSdkFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_sdk_file_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadSdkFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadSdkFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadSdkFileResponse().from_map(
            await self.do_rpcrequest_async('DownloadSdkFile', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_sdk_file(
        self,
        request: gameshield_20180305_models.DownloadSdkFileRequest,
    ) -> gameshield_20180305_models.DownloadSdkFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_sdk_file_with_options(request, runtime)

    async def download_sdk_file_async(
        self,
        request: gameshield_20180305_models.DownloadSdkFileRequest,
    ) -> gameshield_20180305_models.DownloadSdkFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_sdk_file_with_options_async(request, runtime)

    def download_user_total_flow_report_with_options(
        self,
        request: gameshield_20180305_models.DownloadUserTotalFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadUserTotalFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadUserTotalFlowReportResponse().from_map(
            self.do_rpcrequest('DownloadUserTotalFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_user_total_flow_report_with_options_async(
        self,
        request: gameshield_20180305_models.DownloadUserTotalFlowReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.DownloadUserTotalFlowReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.DownloadUserTotalFlowReportResponse().from_map(
            await self.do_rpcrequest_async('DownloadUserTotalFlowReport', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_user_total_flow_report(
        self,
        request: gameshield_20180305_models.DownloadUserTotalFlowReportRequest,
    ) -> gameshield_20180305_models.DownloadUserTotalFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_user_total_flow_report_with_options(request, runtime)

    async def download_user_total_flow_report_async(
        self,
        request: gameshield_20180305_models.DownloadUserTotalFlowReportRequest,
    ) -> gameshield_20180305_models.DownloadUserTotalFlowReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_user_total_flow_report_with_options_async(request, runtime)

    def flush_layer_4rules_with_options(
        self,
        request: gameshield_20180305_models.FlushLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.FlushLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.FlushLayer4RulesResponse().from_map(
            self.do_rpcrequest('FlushLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def flush_layer_4rules_with_options_async(
        self,
        request: gameshield_20180305_models.FlushLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.FlushLayer4RulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.FlushLayer4RulesResponse().from_map(
            await self.do_rpcrequest_async('FlushLayer4Rules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flush_layer_4rules(
        self,
        request: gameshield_20180305_models.FlushLayer4RulesRequest,
    ) -> gameshield_20180305_models.FlushLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.flush_layer_4rules_with_options(request, runtime)

    async def flush_layer_4rules_async(
        self,
        request: gameshield_20180305_models.FlushLayer4RulesRequest,
    ) -> gameshield_20180305_models.FlushLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flush_layer_4rules_with_options_async(request, runtime)

    def realloc_ng_resource_with_options(
        self,
        request: gameshield_20180305_models.ReallocNgResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ReallocNgResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ReallocNgResourceResponse().from_map(
            self.do_rpcrequest('ReallocNgResource', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def realloc_ng_resource_with_options_async(
        self,
        request: gameshield_20180305_models.ReallocNgResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ReallocNgResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ReallocNgResourceResponse().from_map(
            await self.do_rpcrequest_async('ReallocNgResource', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def realloc_ng_resource(
        self,
        request: gameshield_20180305_models.ReallocNgResourceRequest,
    ) -> gameshield_20180305_models.ReallocNgResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.realloc_ng_resource_with_options(request, runtime)

    async def realloc_ng_resource_async(
        self,
        request: gameshield_20180305_models.ReallocNgResourceRequest,
    ) -> gameshield_20180305_models.ReallocNgResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.realloc_ng_resource_with_options_async(request, runtime)

    def replace_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.ReplaceCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ReplaceCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ReplaceCcRouteRulesResponse().from_map(
            self.do_rpcrequest('ReplaceCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.ReplaceCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.ReplaceCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.ReplaceCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('ReplaceCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_cc_route_rules(
        self,
        request: gameshield_20180305_models.ReplaceCcRouteRulesRequest,
    ) -> gameshield_20180305_models.ReplaceCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_cc_route_rules_with_options(request, runtime)

    async def replace_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.ReplaceCcRouteRulesRequest,
    ) -> gameshield_20180305_models.ReplaceCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_cc_route_rules_with_options_async(request, runtime)

    def search_flex_fwd_rules_with_options(
        self,
        request: gameshield_20180305_models.SearchFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.SearchFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.SearchFlexFwdRulesResponse().from_map(
            self.do_rpcrequest('SearchFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_flex_fwd_rules_with_options_async(
        self,
        request: gameshield_20180305_models.SearchFlexFwdRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.SearchFlexFwdRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.SearchFlexFwdRulesResponse().from_map(
            await self.do_rpcrequest_async('SearchFlexFwdRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_flex_fwd_rules(
        self,
        request: gameshield_20180305_models.SearchFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.SearchFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_flex_fwd_rules_with_options(request, runtime)

    async def search_flex_fwd_rules_async(
        self,
        request: gameshield_20180305_models.SearchFlexFwdRulesRequest,
    ) -> gameshield_20180305_models.SearchFlexFwdRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_flex_fwd_rules_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: gameshield_20180305_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateAppResponse().from_map(
            self.do_rpcrequest('UpdateApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateAppResponse().from_map(
            await self.do_rpcrequest_async('UpdateApp', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app(
        self,
        request: gameshield_20180305_models.UpdateAppRequest,
    ) -> gameshield_20180305_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: gameshield_20180305_models.UpdateAppRequest,
    ) -> gameshield_20180305_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_cc_black_list_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcBlackListResponse().from_map(
            self.do_rpcrequest('UpdateCcBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_black_list_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcBlackListResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_black_list(
        self,
        request: gameshield_20180305_models.UpdateCcBlackListRequest,
    ) -> gameshield_20180305_models.UpdateCcBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_black_list_with_options(request, runtime)

    async def update_cc_black_list_async(
        self,
        request: gameshield_20180305_models.UpdateCcBlackListRequest,
    ) -> gameshield_20180305_models.UpdateCcBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_black_list_with_options_async(request, runtime)

    def update_cc_idcblock_switch_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcIDCBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse().from_map(
            self.do_rpcrequest('UpdateCcIDCBlockSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_idcblock_switch_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcIDCBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcIDCBlockSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_idcblock_switch(
        self,
        request: gameshield_20180305_models.UpdateCcIDCBlockSwitchRequest,
    ) -> gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_idcblock_switch_with_options(request, runtime)

    async def update_cc_idcblock_switch_async(
        self,
        request: gameshield_20180305_models.UpdateCcIDCBlockSwitchRequest,
    ) -> gameshield_20180305_models.UpdateCcIDCBlockSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_idcblock_switch_with_options_async(request, runtime)

    def update_cc_route_rules_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcRouteRulesResponse().from_map(
            self.do_rpcrequest('UpdateCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_route_rules_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcRouteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcRouteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcRouteRulesResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcRouteRules', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_route_rules(
        self,
        request: gameshield_20180305_models.UpdateCcRouteRulesRequest,
    ) -> gameshield_20180305_models.UpdateCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_route_rules_with_options(request, runtime)

    async def update_cc_route_rules_async(
        self,
        request: gameshield_20180305_models.UpdateCcRouteRulesRequest,
    ) -> gameshield_20180305_models.UpdateCcRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_route_rules_with_options_async(request, runtime)

    def update_cc_route_switch_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcRouteSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcRouteSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcRouteSwitchResponse().from_map(
            self.do_rpcrequest('UpdateCcRouteSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_route_switch_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcRouteSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcRouteSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcRouteSwitchResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcRouteSwitch', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_route_switch(
        self,
        request: gameshield_20180305_models.UpdateCcRouteSwitchRequest,
    ) -> gameshield_20180305_models.UpdateCcRouteSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_route_switch_with_options(request, runtime)

    async def update_cc_route_switch_async(
        self,
        request: gameshield_20180305_models.UpdateCcRouteSwitchRequest,
    ) -> gameshield_20180305_models.UpdateCcRouteSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_route_switch_with_options_async(request, runtime)

    def update_cc_tunnel_gray_and_only_allow_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse().from_map(
            self.do_rpcrequest('UpdateCcTunnelGrayAndOnlyAllow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_tunnel_gray_and_only_allow_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcTunnelGrayAndOnlyAllow', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_tunnel_gray_and_only_allow(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowRequest,
    ) -> gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_tunnel_gray_and_only_allow_with_options(request, runtime)

    async def update_cc_tunnel_gray_and_only_allow_async(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowRequest,
    ) -> gameshield_20180305_models.UpdateCcTunnelGrayAndOnlyAllowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_tunnel_gray_and_only_allow_with_options_async(request, runtime)

    def update_cc_tunnel_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcTunnelStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcTunnelStatusResponse().from_map(
            self.do_rpcrequest('UpdateCcTunnelStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_tunnel_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcTunnelStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcTunnelStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcTunnelStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_tunnel_status(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelStatusRequest,
    ) -> gameshield_20180305_models.UpdateCcTunnelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_tunnel_status_with_options(request, runtime)

    async def update_cc_tunnel_status_async(
        self,
        request: gameshield_20180305_models.UpdateCcTunnelStatusRequest,
    ) -> gameshield_20180305_models.UpdateCcTunnelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_tunnel_status_with_options_async(request, runtime)

    def update_cc_use_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcUseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcUseResponse().from_map(
            self.do_rpcrequest('UpdateCcUse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_use_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcUseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcUseResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcUse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_use(
        self,
        request: gameshield_20180305_models.UpdateCcUseRequest,
    ) -> gameshield_20180305_models.UpdateCcUseResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_use_with_options(request, runtime)

    async def update_cc_use_async(
        self,
        request: gameshield_20180305_models.UpdateCcUseRequest,
    ) -> gameshield_20180305_models.UpdateCcUseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_use_with_options_async(request, runtime)

    def update_cc_white_list_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcWhiteListResponse().from_map(
            self.do_rpcrequest('UpdateCcWhiteList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_white_list_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcWhiteListResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcWhiteList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_white_list(
        self,
        request: gameshield_20180305_models.UpdateCcWhiteListRequest,
    ) -> gameshield_20180305_models.UpdateCcWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_white_list_with_options(request, runtime)

    async def update_cc_white_list_async(
        self,
        request: gameshield_20180305_models.UpdateCcWhiteListRequest,
    ) -> gameshield_20180305_models.UpdateCcWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_white_list_with_options_async(request, runtime)

    def update_cc_zone_block_config_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcZoneBlockConfigResponse().from_map(
            self.do_rpcrequest('UpdateCcZoneBlockConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_zone_block_config_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcZoneBlockConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcZoneBlockConfig', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_zone_block_config(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockConfigRequest,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_zone_block_config_with_options(request, runtime)

    async def update_cc_zone_block_config_async(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockConfigRequest,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_zone_block_config_with_options_async(request, runtime)

    def update_cc_zone_block_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcZoneBlockStatusResponse().from_map(
            self.do_rpcrequest('UpdateCcZoneBlockStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cc_zone_block_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateCcZoneBlockStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateCcZoneBlockStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cc_zone_block_status(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockStatusRequest,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cc_zone_block_status_with_options(request, runtime)

    async def update_cc_zone_block_status_async(
        self,
        request: gameshield_20180305_models.UpdateCcZoneBlockStatusRequest,
    ) -> gameshield_20180305_models.UpdateCcZoneBlockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cc_zone_block_status_with_options_async(request, runtime)

    def update_flex_acc_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccFwdRuleResponse().from_map(
            self.do_rpcrequest('UpdateFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_acc_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexAccFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_acc_fwd_rule(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_acc_fwd_rule_with_options(request, runtime)

    async def update_flex_acc_fwd_rule_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_acc_fwd_rule_with_options_async(request, runtime)

    def update_flex_acc_fwd_rule_v2with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response().from_map(
            self.do_rpcrequest('UpdateFlexAccFwdRuleV2', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_acc_fwd_rule_v2with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response().from_map(
            await self.do_rpcrequest_async('UpdateFlexAccFwdRuleV2', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_acc_fwd_rule_v2(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleV2Request,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_acc_fwd_rule_v2with_options(request, runtime)

    async def update_flex_acc_fwd_rule_v2_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccFwdRuleV2Request,
    ) -> gameshield_20180305_models.UpdateFlexAccFwdRuleV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_acc_fwd_rule_v2with_options_async(request, runtime)

    def update_flex_acc_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexAccStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccStatusResponse().from_map(
            self.do_rpcrequest('UpdateFlexAccStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_acc_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexAccStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_acc_status(
        self,
        request: gameshield_20180305_models.UpdateFlexAccStatusRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_acc_status_with_options(request, runtime)

    async def update_flex_acc_status_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccStatusRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_acc_status_with_options_async(request, runtime)

    def update_flex_acc_tcp_ports_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexAccTcpPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccTcpPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccTcpPortsResponse().from_map(
            self.do_rpcrequest('UpdateFlexAccTcpPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_acc_tcp_ports_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccTcpPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccTcpPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccTcpPortsResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexAccTcpPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_acc_tcp_ports(
        self,
        request: gameshield_20180305_models.UpdateFlexAccTcpPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccTcpPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_acc_tcp_ports_with_options(request, runtime)

    async def update_flex_acc_tcp_ports_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccTcpPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccTcpPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_acc_tcp_ports_with_options_async(request, runtime)

    def update_flex_acc_udp_ports_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexAccUdpPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccUdpPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccUdpPortsResponse().from_map(
            self.do_rpcrequest('UpdateFlexAccUdpPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_acc_udp_ports_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccUdpPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexAccUdpPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexAccUdpPortsResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexAccUdpPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_acc_udp_ports(
        self,
        request: gameshield_20180305_models.UpdateFlexAccUdpPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccUdpPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_acc_udp_ports_with_options(request, runtime)

    async def update_flex_acc_udp_ports_async(
        self,
        request: gameshield_20180305_models.UpdateFlexAccUdpPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexAccUdpPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_acc_udp_ports_with_options_async(request, runtime)

    def update_flex_backup_groups_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexBackupGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexBackupGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexBackupGroupsResponse().from_map(
            self.do_rpcrequest('UpdateFlexBackupGroups', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_backup_groups_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexBackupGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexBackupGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexBackupGroupsResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexBackupGroups', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_backup_groups(
        self,
        request: gameshield_20180305_models.UpdateFlexBackupGroupsRequest,
    ) -> gameshield_20180305_models.UpdateFlexBackupGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_backup_groups_with_options(request, runtime)

    async def update_flex_backup_groups_async(
        self,
        request: gameshield_20180305_models.UpdateFlexBackupGroupsRequest,
    ) -> gameshield_20180305_models.UpdateFlexBackupGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_backup_groups_with_options_async(request, runtime)

    def update_flex_fwd_rule_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexFwdRuleResponse().from_map(
            self.do_rpcrequest('UpdateFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_fwd_rule_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexFwdRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexFwdRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexFwdRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexFwdRule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_fwd_rule(
        self,
        request: gameshield_20180305_models.UpdateFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.UpdateFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_fwd_rule_with_options(request, runtime)

    async def update_flex_fwd_rule_async(
        self,
        request: gameshield_20180305_models.UpdateFlexFwdRuleRequest,
    ) -> gameshield_20180305_models.UpdateFlexFwdRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_fwd_rule_with_options_async(request, runtime)

    def update_flex_inner_policy_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexInnerPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexInnerPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexInnerPolicyResponse().from_map(
            self.do_rpcrequest('UpdateFlexInnerPolicy', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_inner_policy_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexInnerPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexInnerPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexInnerPolicyResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexInnerPolicy', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_inner_policy(
        self,
        request: gameshield_20180305_models.UpdateFlexInnerPolicyRequest,
    ) -> gameshield_20180305_models.UpdateFlexInnerPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_inner_policy_with_options(request, runtime)

    async def update_flex_inner_policy_async(
        self,
        request: gameshield_20180305_models.UpdateFlexInnerPolicyRequest,
    ) -> gameshield_20180305_models.UpdateFlexInnerPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_inner_policy_with_options_async(request, runtime)

    def update_flex_link_type_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexLinkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexLinkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexLinkTypeResponse().from_map(
            self.do_rpcrequest('UpdateFlexLinkType', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_link_type_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexLinkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexLinkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexLinkTypeResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexLinkType', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_link_type(
        self,
        request: gameshield_20180305_models.UpdateFlexLinkTypeRequest,
    ) -> gameshield_20180305_models.UpdateFlexLinkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_link_type_with_options(request, runtime)

    async def update_flex_link_type_async(
        self,
        request: gameshield_20180305_models.UpdateFlexLinkTypeRequest,
    ) -> gameshield_20180305_models.UpdateFlexLinkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_link_type_with_options_async(request, runtime)

    def update_flex_ports_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexPortsResponse().from_map(
            self.do_rpcrequest('UpdateFlexPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_ports_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexPortsResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexPorts', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_ports(
        self,
        request: gameshield_20180305_models.UpdateFlexPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_ports_with_options(request, runtime)

    async def update_flex_ports_async(
        self,
        request: gameshield_20180305_models.UpdateFlexPortsRequest,
    ) -> gameshield_20180305_models.UpdateFlexPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_ports_with_options_async(request, runtime)

    def update_flex_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateFlexStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexStatusResponse().from_map(
            self.do_rpcrequest('UpdateFlexStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_flex_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateFlexStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateFlexStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateFlexStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateFlexStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flex_status(
        self,
        request: gameshield_20180305_models.UpdateFlexStatusRequest,
    ) -> gameshield_20180305_models.UpdateFlexStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_flex_status_with_options(request, runtime)

    async def update_flex_status_async(
        self,
        request: gameshield_20180305_models.UpdateFlexStatusRequest,
    ) -> gameshield_20180305_models.UpdateFlexStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_flex_status_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: gameshield_20180305_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupResponse().from_map(
            self.do_rpcrequest('UpdateGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateGroup', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group(
        self,
        request: gameshield_20180305_models.UpdateGroupRequest,
    ) -> gameshield_20180305_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: gameshield_20180305_models.UpdateGroupRequest,
    ) -> gameshield_20180305_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_group_dns_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateGroupDnsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupDnsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupDnsStatusResponse().from_map(
            self.do_rpcrequest('UpdateGroupDnsStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_dns_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateGroupDnsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupDnsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupDnsStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateGroupDnsStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_dns_status(
        self,
        request: gameshield_20180305_models.UpdateGroupDnsStatusRequest,
    ) -> gameshield_20180305_models.UpdateGroupDnsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_dns_status_with_options(request, runtime)

    async def update_group_dns_status_async(
        self,
        request: gameshield_20180305_models.UpdateGroupDnsStatusRequest,
    ) -> gameshield_20180305_models.UpdateGroupDnsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_dns_status_with_options_async(request, runtime)

    def update_group_nodes_with_options(
        self,
        request: gameshield_20180305_models.UpdateGroupNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupNodesResponse().from_map(
            self.do_rpcrequest('UpdateGroupNodes', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_nodes_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateGroupNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupNodesResponse().from_map(
            await self.do_rpcrequest_async('UpdateGroupNodes', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_nodes(
        self,
        request: gameshield_20180305_models.UpdateGroupNodesRequest,
    ) -> gameshield_20180305_models.UpdateGroupNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_nodes_with_options(request, runtime)

    async def update_group_nodes_async(
        self,
        request: gameshield_20180305_models.UpdateGroupNodesRequest,
    ) -> gameshield_20180305_models.UpdateGroupNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_nodes_with_options_async(request, runtime)

    def update_group_status_with_options(
        self,
        request: gameshield_20180305_models.UpdateGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupStatusResponse().from_map(
            self.do_rpcrequest('UpdateGroupStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_status_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateGroupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateGroupStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateGroupStatus', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_status(
        self,
        request: gameshield_20180305_models.UpdateGroupStatusRequest,
    ) -> gameshield_20180305_models.UpdateGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_status_with_options(request, runtime)

    async def update_group_status_async(
        self,
        request: gameshield_20180305_models.UpdateGroupStatusRequest,
    ) -> gameshield_20180305_models.UpdateGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_status_with_options_async(request, runtime)

    def update_layer_4rule_with_options(
        self,
        request: gameshield_20180305_models.UpdateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateLayer4RuleResponse().from_map(
            self.do_rpcrequest('UpdateLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_layer_4rule_with_options_async(
        self,
        request: gameshield_20180305_models.UpdateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UpdateLayer4RuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UpdateLayer4RuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateLayer4Rule', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_layer_4rule(
        self,
        request: gameshield_20180305_models.UpdateLayer4RuleRequest,
    ) -> gameshield_20180305_models.UpdateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_layer_4rule_with_options(request, runtime)

    async def update_layer_4rule_async(
        self,
        request: gameshield_20180305_models.UpdateLayer4RuleRequest,
    ) -> gameshield_20180305_models.UpdateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_layer_4rule_with_options_async(request, runtime)

    def upload_cc_route_file_for_parse_with_options(
        self,
        request: gameshield_20180305_models.UploadCcRouteFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadCcRouteFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadCcRouteFileForParseResponse().from_map(
            self.do_rpcrequest('UploadCcRouteFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_cc_route_file_for_parse_with_options_async(
        self,
        request: gameshield_20180305_models.UploadCcRouteFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadCcRouteFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadCcRouteFileForParseResponse().from_map(
            await self.do_rpcrequest_async('UploadCcRouteFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_cc_route_file_for_parse(
        self,
        request: gameshield_20180305_models.UploadCcRouteFileForParseRequest,
    ) -> gameshield_20180305_models.UploadCcRouteFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_cc_route_file_for_parse_with_options(request, runtime)

    async def upload_cc_route_file_for_parse_async(
        self,
        request: gameshield_20180305_models.UploadCcRouteFileForParseRequest,
    ) -> gameshield_20180305_models.UploadCcRouteFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_cc_route_file_for_parse_with_options_async(request, runtime)

    def upload_cc_white_black_list_with_options(
        self,
        request: gameshield_20180305_models.UploadCcWhiteBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadCcWhiteBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadCcWhiteBlackListResponse().from_map(
            self.do_rpcrequest('UploadCcWhiteBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_cc_white_black_list_with_options_async(
        self,
        request: gameshield_20180305_models.UploadCcWhiteBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadCcWhiteBlackListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadCcWhiteBlackListResponse().from_map(
            await self.do_rpcrequest_async('UploadCcWhiteBlackList', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_cc_white_black_list(
        self,
        request: gameshield_20180305_models.UploadCcWhiteBlackListRequest,
    ) -> gameshield_20180305_models.UploadCcWhiteBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_cc_white_black_list_with_options(request, runtime)

    async def upload_cc_white_black_list_async(
        self,
        request: gameshield_20180305_models.UploadCcWhiteBlackListRequest,
    ) -> gameshield_20180305_models.UploadCcWhiteBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_cc_white_black_list_with_options_async(request, runtime)

    def upload_flex_acc_rules_file_for_parse_with_options(
        self,
        request: gameshield_20180305_models.UploadFlexAccRulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse().from_map(
            self.do_rpcrequest('UploadFlexAccRulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_flex_acc_rules_file_for_parse_with_options_async(
        self,
        request: gameshield_20180305_models.UploadFlexAccRulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse().from_map(
            await self.do_rpcrequest_async('UploadFlexAccRulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_flex_acc_rules_file_for_parse(
        self,
        request: gameshield_20180305_models.UploadFlexAccRulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_flex_acc_rules_file_for_parse_with_options(request, runtime)

    async def upload_flex_acc_rules_file_for_parse_async(
        self,
        request: gameshield_20180305_models.UploadFlexAccRulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadFlexAccRulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_flex_acc_rules_file_for_parse_with_options_async(request, runtime)

    def upload_flex_rules_file_for_parse_with_options(
        self,
        request: gameshield_20180305_models.UploadFlexRulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadFlexRulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadFlexRulesFileForParseResponse().from_map(
            self.do_rpcrequest('UploadFlexRulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_flex_rules_file_for_parse_with_options_async(
        self,
        request: gameshield_20180305_models.UploadFlexRulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadFlexRulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadFlexRulesFileForParseResponse().from_map(
            await self.do_rpcrequest_async('UploadFlexRulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_flex_rules_file_for_parse(
        self,
        request: gameshield_20180305_models.UploadFlexRulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadFlexRulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_flex_rules_file_for_parse_with_options(request, runtime)

    async def upload_flex_rules_file_for_parse_async(
        self,
        request: gameshield_20180305_models.UploadFlexRulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadFlexRulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_flex_rules_file_for_parse_with_options_async(request, runtime)

    def upload_l4rules_file_for_parse_with_options(
        self,
        request: gameshield_20180305_models.UploadL4RulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadL4RulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadL4RulesFileForParseResponse().from_map(
            self.do_rpcrequest('UploadL4RulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_l4rules_file_for_parse_with_options_async(
        self,
        request: gameshield_20180305_models.UploadL4RulesFileForParseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gameshield_20180305_models.UploadL4RulesFileForParseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return gameshield_20180305_models.UploadL4RulesFileForParseResponse().from_map(
            await self.do_rpcrequest_async('UploadL4RulesFileForParse', '2018-03-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_l4rules_file_for_parse(
        self,
        request: gameshield_20180305_models.UploadL4RulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadL4RulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_l4rules_file_for_parse_with_options(request, runtime)

    async def upload_l4rules_file_for_parse_async(
        self,
        request: gameshield_20180305_models.UploadL4RulesFileForParseRequest,
    ) -> gameshield_20180305_models.UploadL4RulesFileForParseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_l4rules_file_for_parse_with_options_async(request, runtime)
