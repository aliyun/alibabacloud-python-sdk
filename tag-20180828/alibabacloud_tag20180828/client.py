# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tag20180828 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'us-west-1': 'tag.us-east-1.aliyuncs.com',
            'cn-hangzhou-finance': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'tag.aliyuncs.com',
            'ap-northeast-2-pop': 'tag.aliyuncs.com',
            'cn-beijing-finance-pop': 'tag.aliyuncs.com',
            'cn-beijing-gov-1': 'tag.aliyuncs.com',
            'cn-beijing-nu16-b01': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-edge-1': 'tag.aliyuncs.com',
            'cn-fujian': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-haidian-cm12-c01': 'tag.cn-north-2-gov-1.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'tag.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-test-306': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-hongkong-finance-pop': 'tag.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'tag.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tag.aliyuncs.com',
            'cn-shanghai-inner': 'tag.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'tag.aliyuncs.com',
            'cn-shenzhen-inner': 'tag.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'tag.aliyuncs.com',
            'cn-wuhan': 'tag.aliyuncs.com',
            'cn-yushanfang': 'tag.aliyuncs.com',
            'cn-zhangbei': 'tag.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'tag.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'tag.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'tag.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'tag.aliyuncs.com',
            'us-east-1': 'tag.us-east-1.aliyuncs.com',
            'me-east-1': 'tag.me-east-1.aliyuncs.com',
            'me-central-1': 'tag.me-central-1.aliyuncs.com',
            'eu-west-1': 'tag.eu-west-1.aliyuncs.com',
            'eu-central-1': 'tag.eu-central-1.aliyuncs.com',
            'cn-zhengzhou-jva': 'tag.cn-zhengzhou-jva.aliyuncs.com',
            'cn-zhangjiakou': 'tag.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'tag.cn-wulanchabu.aliyuncs.com',
            'cn-shenzhen-finance-1': 'tag.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen': 'tag.cn-shenzhen.aliyuncs.com',
            'cn-shanghai': 'tag.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'tag.cn-qingdao.aliyuncs.com',
            'cn-nanjing': 'tag.cn-nanjing.aliyuncs.com',
            'cn-huhehaote': 'tag.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'tag.cn-hongkong.aliyuncs.com',
            'cn-heyuan': 'tag.cn-heyuan.aliyuncs.com',
            'cn-hangzhou': 'tag.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'tag.cn-guangzhou.aliyuncs.com',
            'cn-fuzhou': 'tag.cn-fuzhou.aliyuncs.com',
            'cn-chengdu': 'tag.cn-chengdu.aliyuncs.com',
            'cn-beijing-finance-1': 'tag.cn-beijing-finance-1.aliyuncs.com',
            'cn-beijing': 'tag.cn-beijing.aliyuncs.com',
            'ap-southeast-7': 'tag.ap-southeast-7.aliyuncs.com',
            'ap-southeast-6': 'tag.ap-southeast-6.aliyuncs.com',
            'ap-southeast-5': 'tag.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'tag.ap-southeast-3.aliyuncs.com',
            'ap-southeast-1': 'tag.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'tag.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'tag.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_policy_with_options(
        self,
        request: main_models.AttachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: main_models.AttachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy(
        self,
        request: main_models.AttachPolicyRequest,
    ) -> main_models.AttachPolicyResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: main_models.AttachPolicyRequest,
    ) -> main_models.AttachPolicyResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def check_created_by_enabled_with_options(
        self,
        request: main_models.CheckCreatedByEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCreatedByEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCreatedByEnabled',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCreatedByEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_created_by_enabled_with_options_async(
        self,
        request: main_models.CheckCreatedByEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCreatedByEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCreatedByEnabled',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCreatedByEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_created_by_enabled(
        self,
        request: main_models.CheckCreatedByEnabledRequest,
    ) -> main_models.CheckCreatedByEnabledResponse:
        runtime = RuntimeOptions()
        return self.check_created_by_enabled_with_options(request, runtime)

    async def check_created_by_enabled_async(
        self,
        request: main_models.CheckCreatedByEnabledRequest,
    ) -> main_models.CheckCreatedByEnabledResponse:
        runtime = RuntimeOptions()
        return await self.check_created_by_enabled_with_options_async(request, runtime)

    def close_created_by_with_options(
        self,
        request: main_models.CloseCreatedByRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseCreatedByResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseCreatedBy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseCreatedByResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_created_by_with_options_async(
        self,
        request: main_models.CloseCreatedByRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseCreatedByResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseCreatedBy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseCreatedByResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_created_by(
        self,
        request: main_models.CloseCreatedByRequest,
    ) -> main_models.CloseCreatedByResponse:
        runtime = RuntimeOptions()
        return self.close_created_by_with_options(request, runtime)

    async def close_created_by_async(
        self,
        request: main_models.CloseCreatedByRequest,
    ) -> main_models.CloseCreatedByResponse:
        runtime = RuntimeOptions()
        return await self.close_created_by_with_options_async(request, runtime)

    def create_associated_resource_rules_with_options(
        self,
        request: main_models.CreateAssociatedResourceRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssociatedResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_rules_list):
            query['CreateRulesList'] = request.create_rules_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssociatedResourceRules',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssociatedResourceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_associated_resource_rules_with_options_async(
        self,
        request: main_models.CreateAssociatedResourceRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssociatedResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_rules_list):
            query['CreateRulesList'] = request.create_rules_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssociatedResourceRules',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssociatedResourceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_associated_resource_rules(
        self,
        request: main_models.CreateAssociatedResourceRulesRequest,
    ) -> main_models.CreateAssociatedResourceRulesResponse:
        runtime = RuntimeOptions()
        return self.create_associated_resource_rules_with_options(request, runtime)

    async def create_associated_resource_rules_async(
        self,
        request: main_models.CreateAssociatedResourceRulesRequest,
    ) -> main_models.CreateAssociatedResourceRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_associated_resource_rules_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not DaraCore.is_null(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not DaraCore.is_null(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_tags_with_options(
        self,
        request: main_models.CreateTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key_value_param_list):
            query['TagKeyValueParamList'] = request.tag_key_value_param_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTags',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tags_with_options_async(
        self,
        request: main_models.CreateTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key_value_param_list):
            query['TagKeyValueParamList'] = request.tag_key_value_param_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTags',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tags(
        self,
        request: main_models.CreateTagsRequest,
    ) -> main_models.CreateTagsResponse:
        runtime = RuntimeOptions()
        return self.create_tags_with_options(request, runtime)

    async def create_tags_async(
        self,
        request: main_models.CreateTagsRequest,
    ) -> main_models.CreateTagsResponse:
        runtime = RuntimeOptions()
        return await self.create_tags_with_options_async(request, runtime)

    def delete_associated_resource_rule_with_options(
        self,
        request: main_models.DeleteAssociatedResourceRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAssociatedResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAssociatedResourceRule',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAssociatedResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_associated_resource_rule_with_options_async(
        self,
        request: main_models.DeleteAssociatedResourceRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAssociatedResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAssociatedResourceRule',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAssociatedResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_associated_resource_rule(
        self,
        request: main_models.DeleteAssociatedResourceRuleRequest,
    ) -> main_models.DeleteAssociatedResourceRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_associated_resource_rule_with_options(request, runtime)

    async def delete_associated_resource_rule_async(
        self,
        request: main_models.DeleteAssociatedResourceRuleRequest,
    ) -> main_models.DeleteAssociatedResourceRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_associated_resource_rule_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: main_models.DeleteTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_policy_with_options(
        self,
        request: main_models.DetachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: main_models.DetachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy(
        self,
        request: main_models.DetachPolicyRequest,
    ) -> main_models.DetachPolicyResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: main_models.DetachPolicyRequest,
    ) -> main_models.DetachPolicyResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_policy_type_with_options(
        self,
        request: main_models.DisablePolicyTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisablePolicyTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisablePolicyType',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisablePolicyTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_policy_type_with_options_async(
        self,
        request: main_models.DisablePolicyTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisablePolicyTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisablePolicyType',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisablePolicyTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_policy_type(
        self,
        request: main_models.DisablePolicyTypeRequest,
    ) -> main_models.DisablePolicyTypeResponse:
        runtime = RuntimeOptions()
        return self.disable_policy_type_with_options(request, runtime)

    async def disable_policy_type_async(
        self,
        request: main_models.DisablePolicyTypeRequest,
    ) -> main_models.DisablePolicyTypeResponse:
        runtime = RuntimeOptions()
        return await self.disable_policy_type_with_options_async(request, runtime)

    def enable_policy_type_with_options(
        self,
        request: main_models.EnablePolicyTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnablePolicyTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnablePolicyType',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnablePolicyTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_policy_type_with_options_async(
        self,
        request: main_models.EnablePolicyTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnablePolicyTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnablePolicyType',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnablePolicyTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_policy_type(
        self,
        request: main_models.EnablePolicyTypeRequest,
    ) -> main_models.EnablePolicyTypeResponse:
        runtime = RuntimeOptions()
        return self.enable_policy_type_with_options(request, runtime)

    async def enable_policy_type_async(
        self,
        request: main_models.EnablePolicyTypeRequest,
    ) -> main_models.EnablePolicyTypeResponse:
        runtime = RuntimeOptions()
        return await self.enable_policy_type_with_options_async(request, runtime)

    def generate_config_rule_report_with_options(
        self,
        request: main_models.GenerateConfigRuleReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateConfigRuleReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateConfigRuleReport',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateConfigRuleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_config_rule_report_with_options_async(
        self,
        request: main_models.GenerateConfigRuleReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateConfigRuleReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateConfigRuleReport',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateConfigRuleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_config_rule_report(
        self,
        request: main_models.GenerateConfigRuleReportRequest,
    ) -> main_models.GenerateConfigRuleReportResponse:
        runtime = RuntimeOptions()
        return self.generate_config_rule_report_with_options(request, runtime)

    async def generate_config_rule_report_async(
        self,
        request: main_models.GenerateConfigRuleReportRequest,
    ) -> main_models.GenerateConfigRuleReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_config_rule_report_with_options_async(request, runtime)

    def get_config_rule_report_with_options(
        self,
        request: main_models.GetConfigRuleReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRuleReport',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_rule_report_with_options_async(
        self,
        request: main_models.GetConfigRuleReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigRuleReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConfigRuleReport',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigRuleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_rule_report(
        self,
        request: main_models.GetConfigRuleReportRequest,
    ) -> main_models.GetConfigRuleReportResponse:
        runtime = RuntimeOptions()
        return self.get_config_rule_report_with_options(request, runtime)

    async def get_config_rule_report_async(
        self,
        request: main_models.GetConfigRuleReportRequest,
    ) -> main_models.GetConfigRuleReportResponse:
        runtime = RuntimeOptions()
        return await self.get_config_rule_report_with_options_async(request, runtime)

    def get_effective_policy_with_options(
        self,
        request: main_models.GetEffectivePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEffectivePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEffectivePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEffectivePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_effective_policy_with_options_async(
        self,
        request: main_models.GetEffectivePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEffectivePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEffectivePolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEffectivePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_effective_policy(
        self,
        request: main_models.GetEffectivePolicyRequest,
    ) -> main_models.GetEffectivePolicyResponse:
        runtime = RuntimeOptions()
        return self.get_effective_policy_with_options(request, runtime)

    async def get_effective_policy_async(
        self,
        request: main_models.GetEffectivePolicyRequest,
    ) -> main_models.GetEffectivePolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_effective_policy_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_enable_status_with_options(
        self,
        request: main_models.GetPolicyEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyEnableStatus',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_enable_status_with_options_async(
        self,
        request: main_models.GetPolicyEnableStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyEnableStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.open_type):
            query['OpenType'] = request.open_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyEnableStatus',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_enable_status(
        self,
        request: main_models.GetPolicyEnableStatusRequest,
    ) -> main_models.GetPolicyEnableStatusResponse:
        runtime = RuntimeOptions()
        return self.get_policy_enable_status_with_options(request, runtime)

    async def get_policy_enable_status_async(
        self,
        request: main_models.GetPolicyEnableStatusRequest,
    ) -> main_models.GetPolicyEnableStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_enable_status_with_options_async(request, runtime)

    def list_associated_resource_rules_with_options(
        self,
        request: main_models.ListAssociatedResourceRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssociatedResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAssociatedResourceRules',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssociatedResourceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_associated_resource_rules_with_options_async(
        self,
        request: main_models.ListAssociatedResourceRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssociatedResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAssociatedResourceRules',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssociatedResourceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_associated_resource_rules(
        self,
        request: main_models.ListAssociatedResourceRulesRequest,
    ) -> main_models.ListAssociatedResourceRulesResponse:
        runtime = RuntimeOptions()
        return self.list_associated_resource_rules_with_options(request, runtime)

    async def list_associated_resource_rules_async(
        self,
        request: main_models.ListAssociatedResourceRulesRequest,
    ) -> main_models.ListAssociatedResourceRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_associated_resource_rules_with_options_async(request, runtime)

    def list_config_rules_for_target_with_options(
        self,
        request: main_models.ListConfigRulesForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRulesForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRulesForTarget',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRulesForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rules_for_target_with_options_async(
        self,
        request: main_models.ListConfigRulesForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigRulesForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigRulesForTarget',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigRulesForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rules_for_target(
        self,
        request: main_models.ListConfigRulesForTargetRequest,
    ) -> main_models.ListConfigRulesForTargetResponse:
        runtime = RuntimeOptions()
        return self.list_config_rules_for_target_with_options(request, runtime)

    async def list_config_rules_for_target_async(
        self,
        request: main_models.ListConfigRulesForTargetRequest,
    ) -> main_models.ListConfigRulesForTargetResponse:
        runtime = RuntimeOptions()
        return await self.list_config_rules_for_target_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policies_for_target_with_options(
        self,
        request: main_models.ListPoliciesForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForTarget',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_target_with_options_async(
        self,
        request: main_models.ListPoliciesForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForTarget',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_target(
        self,
        request: main_models.ListPoliciesForTargetRequest,
    ) -> main_models.ListPoliciesForTargetResponse:
        runtime = RuntimeOptions()
        return self.list_policies_for_target_with_options(request, runtime)

    async def list_policies_for_target_async(
        self,
        request: main_models.ListPoliciesForTargetRequest,
    ) -> main_models.ListPoliciesForTargetResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_for_target_with_options_async(request, runtime)

    def list_resources_by_tag_with_options(
        self,
        request: main_models.ListResourcesByTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesByTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.include_all_tags):
            query['IncludeAllTags'] = request.include_all_tags
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesByTag',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesByTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_by_tag_with_options_async(
        self,
        request: main_models.ListResourcesByTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesByTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.include_all_tags):
            query['IncludeAllTags'] = request.include_all_tags
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesByTag',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesByTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_by_tag(
        self,
        request: main_models.ListResourcesByTagRequest,
    ) -> main_models.ListResourcesByTagResponse:
        runtime = RuntimeOptions()
        return self.list_resources_by_tag_with_options(request, runtime)

    async def list_resources_by_tag_async(
        self,
        request: main_models.ListResourcesByTagRequest,
    ) -> main_models.ListResourcesByTagResponse:
        runtime = RuntimeOptions()
        return await self.list_resources_by_tag_with_options_async(request, runtime)

    def list_support_resource_types_with_options(
        self,
        request: main_models.ListSupportResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_tye):
            query['ResourceTye'] = request.resource_tye
        if not DaraCore.is_null(request.show_items):
            query['ShowItems'] = request.show_items
        if not DaraCore.is_null(request.support_code):
            query['SupportCode'] = request.support_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportResourceTypes',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_support_resource_types_with_options_async(
        self,
        request: main_models.ListSupportResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_tye):
            query['ResourceTye'] = request.resource_tye
        if not DaraCore.is_null(request.show_items):
            query['ShowItems'] = request.show_items
        if not DaraCore.is_null(request.support_code):
            query['SupportCode'] = request.support_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportResourceTypes',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_support_resource_types(
        self,
        request: main_models.ListSupportResourceTypesRequest,
    ) -> main_models.ListSupportResourceTypesResponse:
        runtime = RuntimeOptions()
        return self.list_support_resource_types_with_options(request, runtime)

    async def list_support_resource_types_async(
        self,
        request: main_models.ListSupportResourceTypesRequest,
    ) -> main_models.ListSupportResourceTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_support_resource_types_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fuzzy_type):
            query['FuzzyType'] = request.fuzzy_type
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_targets_for_policy_with_options(
        self,
        request: main_models.ListTargetsForPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetsForPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargetsForPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetsForPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_targets_for_policy_with_options_async(
        self,
        request: main_models.ListTargetsForPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetsForPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargetsForPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetsForPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_targets_for_policy(
        self,
        request: main_models.ListTargetsForPolicyRequest,
    ) -> main_models.ListTargetsForPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_targets_for_policy_with_options(request, runtime)

    async def list_targets_for_policy_async(
        self,
        request: main_models.ListTargetsForPolicyRequest,
    ) -> main_models.ListTargetsForPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_targets_for_policy_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not DaraCore.is_null(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        request: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.policy_content):
            query['PolicyContent'] = request.policy_content
        if not DaraCore.is_null(request.policy_desc):
            query['PolicyDesc'] = request.policy_desc
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def open_created_by_with_options(
        self,
        request: main_models.OpenCreatedByRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCreatedByResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCreatedBy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCreatedByResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_created_by_with_options_async(
        self,
        request: main_models.OpenCreatedByRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCreatedByResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCreatedBy',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCreatedByResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_created_by(
        self,
        request: main_models.OpenCreatedByRequest,
    ) -> main_models.OpenCreatedByResponse:
        runtime = RuntimeOptions()
        return self.open_created_by_with_options(request, runtime)

    async def open_created_by_async(
        self,
        request: main_models.OpenCreatedByRequest,
    ) -> main_models.OpenCreatedByResponse:
        runtime = RuntimeOptions()
        return await self.open_created_by_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_associated_resource_rule_with_options(
        self,
        request: main_models.UpdateAssociatedResourceRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssociatedResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.existing_status):
            query['ExistingStatus'] = request.existing_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssociatedResourceRule',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssociatedResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_associated_resource_rule_with_options_async(
        self,
        request: main_models.UpdateAssociatedResourceRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssociatedResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.existing_status):
            query['ExistingStatus'] = request.existing_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.setting_name):
            query['SettingName'] = request.setting_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssociatedResourceRule',
            version = '2018-08-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssociatedResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_associated_resource_rule(
        self,
        request: main_models.UpdateAssociatedResourceRuleRequest,
    ) -> main_models.UpdateAssociatedResourceRuleResponse:
        runtime = RuntimeOptions()
        return self.update_associated_resource_rule_with_options(request, runtime)

    async def update_associated_resource_rule_async(
        self,
        request: main_models.UpdateAssociatedResourceRuleRequest,
    ) -> main_models.UpdateAssociatedResourceRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_associated_resource_rule_with_options_async(request, runtime)
