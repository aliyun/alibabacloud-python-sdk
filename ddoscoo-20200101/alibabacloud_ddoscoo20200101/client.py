# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20200101 import models as ddoscoo_20200101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Blacklist'] = request.blacklist
        query['ExpireTime'] = request.expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Blacklist'] = request.blacklist
        query['ExpireTime'] = request.expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Whitelist'] = request.whitelist
        query['ExpireTime'] = request.expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Whitelist'] = request.whitelist
        query['ExpireTime'] = request.expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['CertId'] = request.cert_id
        query['CertName'] = request.cert_name
        query['Cert'] = request.cert
        query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociateWebCert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AssociateWebCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_web_cert_with_options_async(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['CertId'] = request.cert_id
        query['CertName'] = request.cert_name
        query['Cert'] = request.cert
        query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociateWebCert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AssociateWebCertResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        query['ObjectType'] = request.object_type
        query['Objects'] = request.objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AttachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_scene_defense_object_with_options_async(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        query['ObjectType'] = request.object_type
        query['Objects'] = request.objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AttachSceneDefenseObjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_l7rs_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigL7RsPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_network_region_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigWebCCTemplate',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebCCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_web_cctemplate_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigWebCCTemplate',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebCCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['BlackList'] = request.black_list
        query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigWebIpSet',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_web_ip_set_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['BlackList'] = request.black_list
        query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigWebIpSet',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebIpSetResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['TaskType'] = request.task_type
        query['TaskParams'] = request.task_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['TaskType'] = request.task_type
        query['TaskParams'] = request.task_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['Template'] = request.template
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['Template'] = request.template
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Rules'] = request.rules
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Rules'] = request.rules
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['ResourceIds'] = request.resource_ids
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['ResourceIds'] = request.resource_ids
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        query['Act'] = request.act
        query['Count'] = request.count
        query['Interval'] = request.interval
        query['Mode'] = request.mode
        query['Ttl'] = request.ttl
        query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        query['Act'] = request.act
        query['Count'] = request.count
        query['Interval'] = request.interval
        query['Mode'] = request.mode
        query['Ttl'] = request.ttl
        query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RsType'] = request.rs_type
        query['Rules'] = request.rules
        query['HttpsExt'] = request.https_ext
        query['DefenseId'] = request.defense_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RsType'] = request.rs_type
        query['Rules'] = request.rules
        query['HttpsExt'] = request.https_ext
        query['DefenseId'] = request.defense_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Blacklist'] = request.blacklist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Blacklist'] = request.blacklist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRule'] = request.network_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRule'] = request.network_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceIds'] = request.resource_ids
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceIds'] = request.resource_ids
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_cache_custom_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAsyncTasks',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_async_tasks_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAsyncTasks',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcListCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcListCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_list_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcListCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcListCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['KeyWord'] = request.key_word
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBackSourceCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Line'] = request.line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBackSourceCidrResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blackhole_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlackholeStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_block_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlockStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCertsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCnameReuses',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCnameReusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cname_reuses_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCnameReuses',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCnameReusesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosAllEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosAllEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_all_event_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosAllEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosAllEventListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventArea',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAreaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_area_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventArea',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAreaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventAttackType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_attack_type_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventAttackType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventIsp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_isp_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventIsp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventIspResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventMax',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventMaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_max_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        UtilClient.validate_model(request)
        query = {}
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventMax',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventMaxResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDoSEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDoSEventsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        query['Range'] = request.range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventSrcIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_src_ip_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EventType'] = request.event_type
        query['StartTime'] = request.start_time
        query['Ip'] = request.ip
        query['Range'] = request.range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventSrcIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRecords',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_records_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceId'] = request.instance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRecords',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseRecordsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainAttackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_attack_events_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainAttackEventsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_overview_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainOverviewResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainQPSList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQPSListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qpslist_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainQPSList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQPSListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsWithCache',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsWithCache',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_status_code_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['Domain'] = request.domain
        query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_status_code_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['Domain'] = request.domain
        query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopAttackList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainTopAttackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_attack_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopAttackList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainTopAttackListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_source_countries_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_source_provinces_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopCostTime',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_top_cost_time_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopCostTime',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_top_url_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Domain'] = request.domain
        query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceDetailsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Edition'] = request.edition
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIds',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ids_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Edition'] = request.edition
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIds',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Ip'] = request.ip
        query['Remark'] = request.remark
        query['Edition'] = request.edition
        query['Enabled'] = request.enabled
        query['ExpireStartTime'] = request.expire_start_time
        query['ExpireEndTime'] = request.expire_end_time
        query['InstanceIds'] = request.instance_ids
        query['Status'] = request.status
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Ip'] = request.ip
        query['Remark'] = request.remark
        query['Edition'] = request.edition
        query['Enabled'] = request.enabled
        query['ExpireStartTime'] = request.expire_start_time
        query['ExpireEndTime'] = request.expire_end_time
        query['InstanceIds'] = request.instance_ids
        query['Status'] = request.status
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceSpecsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l7rs_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeL7RsPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_region_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRuleAttributes',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rule_attributes_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRuleAttributes',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EntityType'] = request.entity_type
        query['EntityObject'] = request.entity_object
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EntityType'] = request.entity_type
        query['EntityObject'] = request.entity_object
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeOpEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_attack_max_flow_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_auto_cc_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAutoCcStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Port'] = request.port
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortConnsCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_conns_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Port'] = request.port
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortConnsCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Interval'] = request.interval
        query['Port'] = request.port
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortConnsList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_conns_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Interval'] = request.interval
        query['Port'] = request.port
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortConnsList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Interval'] = request.interval
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortFlowList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_flow_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['Interval'] = request.interval
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortFlowList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortFlowListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortMaxConns',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortMaxConnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_max_conns_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortMaxConns',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortMaxConnsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_countries_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceIsps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceIspsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_isps_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceIsps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceIspsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_provinces_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefenseObjects',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_defense_objects_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefenseObjects',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Template'] = request.template
        query['Status'] = request.status
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefensePolicies',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_defense_policies_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Template'] = request.template
        query['Status'] = request.status
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefensePolicies',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['RuleName'] = request.rule_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSchedulerRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSchedulerRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduler_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['RuleName'] = request.rule_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSchedulerRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSchedulerRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStsGrantStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeStsGrantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sts_grant_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStsGrantStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeStsGrantStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_keys_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceIds'] = request.resource_ids
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceIds'] = request.resource_ids
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUnBlackholeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlackholeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_un_blackhole_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUnBlackholeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlackholeCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUnBlockCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlockCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_un_block_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUnBlockCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlockCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogDispatchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_dispatch_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogDispatchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogEmptyCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_empty_count_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogEmptyCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAreaBlockConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_area_block_configs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebAreaBlockConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCacheConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCacheConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_cache_configs_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCacheConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCacheConfigsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCcProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_cc_protect_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCcProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCCRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_ccrules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCCRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomPorts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCustomPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_custom_ports_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomPorts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCustomPortsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceRelations',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_instance_relations_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceRelations',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['QueryDomainPattern'] = request.query_domain_pattern
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_rules_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['QueryDomainPattern'] = request.query_domain_pattern
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWebRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        query['ObjectType'] = request.object_type
        query['Objects'] = request.objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DetachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_scene_defense_object_with_options_async(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        query['ObjectType'] = request.object_type
        query['Objects'] = request.objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DetachSceneDefenseObjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_access_log_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebAccessLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_ccwith_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_auto_cc_blacklist_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_auto_cc_whitelist_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptySlsLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptySlsLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_access_log_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebAccessLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_ccwith_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BlackholeStatus'] = request.blackhole_status
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_blackhole_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BlackholeStatus'] = request.blackhole_status
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlackholeStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Status'] = request.status
        query['Duration'] = request.duration
        query['InstanceId'] = request.instance_id
        query['Lines'] = request.lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_block_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Status'] = request.status
        query['Duration'] = request.duration
        query['InstanceId'] = request.instance_id
        query['Lines'] = request.lines
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlockStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Cname'] = request.cname
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyCnameReuse',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyCnameReuseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cname_reuse_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Cname'] = request.cname
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyCnameReuse',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyCnameReuseResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ElasticBandwidth'] = request.elastic_bandwidth
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ElasticBandwidth'] = request.elastic_bandwidth
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBandWidthResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Ttl'] = request.ttl
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyFullLogTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Ttl'] = request.ttl
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyFullLogTtlResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['HealthCheck'] = request.health_check
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheckConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHealthCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_health_check_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['HealthCheck'] = request.health_check
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheckConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHealthCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHttp2Enable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHttp2EnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_http_2enable_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHttp2Enable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHttp2EnableResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyInstanceRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyInstanceRemarkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyNetworkRuleAttribute',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_rule_attribute_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ForwardProtocol'] = request.forward_protocol
        query['FrontendPort'] = request.frontend_port
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyNetworkRuleAttribute',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['Switch'] = request.switch
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_port_auto_cc_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Switch'] = request.switch
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PolicyId'] = request.policy_id
        query['Name'] = request.name
        query['Template'] = request.template
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scene_defense_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyId'] = request.policy_id
        query['Name'] = request.name
        query['Template'] = request.template
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Rules'] = request.rules
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Rules'] = request.rules
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyTlsConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyTlsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tls_config_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyTlsConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyTlsConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Domain'] = request.domain
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_access_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['AccessMode'] = request.access_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_aiprotect_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_aiprotect_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_area_block_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlockSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_area_block_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlockSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_custom_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        query['Act'] = request.act
        query['Count'] = request.count
        query['Interval'] = request.interval
        query['Mode'] = request.mode
        query['Ttl'] = request.ttl
        query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ccrule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Name'] = request.name
        query['Act'] = request.act
        query['Count'] = request.count
        query['Interval'] = request.interval
        query['Mode'] = request.mode
        query['Ttl'] = request.ttl
        query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebIpSetSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ip_set_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebIpSetSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Rules'] = request.rules
        query['Expires'] = request.expires
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_precise_access_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Rules'] = request.rules
        query['Expires'] = request.expires
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_precise_access_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['ProxyTypes'] = request.proxy_types
        query['RsType'] = request.rs_type
        query['HttpsExt'] = request.https_ext
        query['RealServers'] = request.real_servers
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['Domain'] = request.domain
        query['ProxyTypes'] = request.proxy_types
        query['RsType'] = request.rs_type
        query['HttpsExt'] = request.https_ext
        query['RealServers'] = request.real_servers
        query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['SwitchData'] = request.switch_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.SwitchSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_scheduler_rule_with_options_async(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RuleName'] = request.rule_name
        query['RuleType'] = request.rule_type
        query['SwitchData'] = request.switch_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.SwitchSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
