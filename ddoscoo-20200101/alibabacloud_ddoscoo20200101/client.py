# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ddoscoo20200101 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_auto_cc_blacklist_with_options(
        self,
        request: main_models.AddAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auto_cc_blacklist_with_options_async(
        self,
        request: main_models.AddAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_auto_cc_blacklist(
        self,
        request: main_models.AddAutoCcBlacklistRequest,
    ) -> main_models.AddAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return self.add_auto_cc_blacklist_with_options(request, runtime)

    async def add_auto_cc_blacklist_async(
        self,
        request: main_models.AddAutoCcBlacklistRequest,
    ) -> main_models.AddAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.add_auto_cc_blacklist_with_options_async(request, runtime)

    def add_auto_cc_whitelist_with_options(
        self,
        request: main_models.AddAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_auto_cc_whitelist_with_options_async(
        self,
        request: main_models.AddAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_auto_cc_whitelist(
        self,
        request: main_models.AddAutoCcWhitelistRequest,
    ) -> main_models.AddAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.add_auto_cc_whitelist_with_options(request, runtime)

    async def add_auto_cc_whitelist_async(
        self,
        request: main_models.AddAutoCcWhitelistRequest,
    ) -> main_models.AddAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.add_auto_cc_whitelist_with_options_async(request, runtime)

    def associate_web_cert_with_options(
        self,
        request: main_models.AssociateWebCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateWebCertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert):
            body['Cert'] = request.cert
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_identifier):
            body['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.cert_name):
            body['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            body['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateWebCert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateWebCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_web_cert_with_options_async(
        self,
        request: main_models.AssociateWebCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateWebCertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert):
            body['Cert'] = request.cert
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_identifier):
            body['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.cert_name):
            body['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            body['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.domain):
            body['Domain'] = request.domain
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateWebCert',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateWebCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_web_cert(
        self,
        request: main_models.AssociateWebCertRequest,
    ) -> main_models.AssociateWebCertResponse:
        runtime = RuntimeOptions()
        return self.associate_web_cert_with_options(request, runtime)

    async def associate_web_cert_async(
        self,
        request: main_models.AssociateWebCertRequest,
    ) -> main_models.AssociateWebCertResponse:
        runtime = RuntimeOptions()
        return await self.associate_web_cert_with_options_async(request, runtime)

    def attach_scene_defense_object_with_options(
        self,
        request: main_models.AttachSceneDefenseObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSceneDefenseObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.objects):
            query['Objects'] = request.objects
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSceneDefenseObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_scene_defense_object_with_options_async(
        self,
        request: main_models.AttachSceneDefenseObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSceneDefenseObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.objects):
            query['Objects'] = request.objects
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSceneDefenseObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSceneDefenseObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_scene_defense_object(
        self,
        request: main_models.AttachSceneDefenseObjectRequest,
    ) -> main_models.AttachSceneDefenseObjectResponse:
        runtime = RuntimeOptions()
        return self.attach_scene_defense_object_with_options(request, runtime)

    async def attach_scene_defense_object_async(
        self,
        request: main_models.AttachSceneDefenseObjectRequest,
    ) -> main_models.AttachSceneDefenseObjectResponse:
        runtime = RuntimeOptions()
        return await self.attach_scene_defense_object_with_options_async(request, runtime)

    def config_domain_security_profile_with_options(
        self,
        request: main_models.ConfigDomainSecurityProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigDomainSecurityProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['Cluster'] = request.cluster
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigDomainSecurityProfile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigDomainSecurityProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_domain_security_profile_with_options_async(
        self,
        request: main_models.ConfigDomainSecurityProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigDomainSecurityProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster):
            query['Cluster'] = request.cluster
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigDomainSecurityProfile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigDomainSecurityProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_domain_security_profile(
        self,
        request: main_models.ConfigDomainSecurityProfileRequest,
    ) -> main_models.ConfigDomainSecurityProfileResponse:
        runtime = RuntimeOptions()
        return self.config_domain_security_profile_with_options(request, runtime)

    async def config_domain_security_profile_async(
        self,
        request: main_models.ConfigDomainSecurityProfileRequest,
    ) -> main_models.ConfigDomainSecurityProfileResponse:
        runtime = RuntimeOptions()
        return await self.config_domain_security_profile_with_options_async(request, runtime)

    def config_l7global_rule_with_options(
        self,
        request: main_models.ConfigL7GlobalRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7GlobalRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.rule_attr):
            query['RuleAttr'] = request.rule_attr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7GlobalRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7GlobalRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_l7global_rule_with_options_async(
        self,
        request: main_models.ConfigL7GlobalRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7GlobalRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.rule_attr):
            query['RuleAttr'] = request.rule_attr
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7GlobalRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7GlobalRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_l7global_rule(
        self,
        request: main_models.ConfigL7GlobalRuleRequest,
    ) -> main_models.ConfigL7GlobalRuleResponse:
        runtime = RuntimeOptions()
        return self.config_l7global_rule_with_options(request, runtime)

    async def config_l7global_rule_async(
        self,
        request: main_models.ConfigL7GlobalRuleRequest,
    ) -> main_models.ConfigL7GlobalRuleResponse:
        runtime = RuntimeOptions()
        return await self.config_l7global_rule_with_options_async(request, runtime)

    def config_l7rs_policy_with_options(
        self,
        request: main_models.ConfigL7RsPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7RsPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.upstream_retry):
            query['UpstreamRetry'] = request.upstream_retry
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7RsPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_l7rs_policy_with_options_async(
        self,
        request: main_models.ConfigL7RsPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7RsPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.policy):
            query['Policy'] = request.policy
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.upstream_retry):
            query['UpstreamRetry'] = request.upstream_retry
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7RsPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7RsPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_l7rs_policy(
        self,
        request: main_models.ConfigL7RsPolicyRequest,
    ) -> main_models.ConfigL7RsPolicyResponse:
        runtime = RuntimeOptions()
        return self.config_l7rs_policy_with_options(request, runtime)

    async def config_l7rs_policy_async(
        self,
        request: main_models.ConfigL7RsPolicyRequest,
    ) -> main_models.ConfigL7RsPolicyResponse:
        runtime = RuntimeOptions()
        return await self.config_l7rs_policy_with_options_async(request, runtime)

    def config_l7us_keepalive_with_options(
        self,
        request: main_models.ConfigL7UsKeepaliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7UsKeepaliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.downstream_keepalive):
            query['DownstreamKeepalive'] = request.downstream_keepalive
        if not DaraCore.is_null(request.upstream_keepalive):
            query['UpstreamKeepalive'] = request.upstream_keepalive
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7UsKeepalive',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7UsKeepaliveResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_l7us_keepalive_with_options_async(
        self,
        request: main_models.ConfigL7UsKeepaliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigL7UsKeepaliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.downstream_keepalive):
            query['DownstreamKeepalive'] = request.downstream_keepalive
        if not DaraCore.is_null(request.upstream_keepalive):
            query['UpstreamKeepalive'] = request.upstream_keepalive
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigL7UsKeepalive',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigL7UsKeepaliveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_l7us_keepalive(
        self,
        request: main_models.ConfigL7UsKeepaliveRequest,
    ) -> main_models.ConfigL7UsKeepaliveResponse:
        runtime = RuntimeOptions()
        return self.config_l7us_keepalive_with_options(request, runtime)

    async def config_l7us_keepalive_async(
        self,
        request: main_models.ConfigL7UsKeepaliveRequest,
    ) -> main_models.ConfigL7UsKeepaliveResponse:
        runtime = RuntimeOptions()
        return await self.config_l7us_keepalive_with_options_async(request, runtime)

    def config_layer_4real_limit_with_options(
        self,
        request: main_models.ConfigLayer4RealLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RealLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_value):
            query['LimitValue'] = request.limit_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RealLimit',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RealLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4real_limit_with_options_async(
        self,
        request: main_models.ConfigLayer4RealLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RealLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit_value):
            query['LimitValue'] = request.limit_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RealLimit',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RealLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4real_limit(
        self,
        request: main_models.ConfigLayer4RealLimitRequest,
    ) -> main_models.ConfigLayer4RealLimitResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4real_limit_with_options(request, runtime)

    async def config_layer_4real_limit_async(
        self,
        request: main_models.ConfigLayer4RealLimitRequest,
    ) -> main_models.ConfigLayer4RealLimitResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4real_limit_with_options_async(request, runtime)

    def config_layer_4remark_with_options(
        self,
        request: main_models.ConfigLayer4RemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4Remark',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4remark_with_options_async(
        self,
        request: main_models.ConfigLayer4RemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4Remark',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4remark(
        self,
        request: main_models.ConfigLayer4RemarkRequest,
    ) -> main_models.ConfigLayer4RemarkResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4remark_with_options(request, runtime)

    async def config_layer_4remark_async(
        self,
        request: main_models.ConfigLayer4RemarkRequest,
    ) -> main_models.ConfigLayer4RemarkResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4remark_with_options_async(request, runtime)

    def config_layer_4rule_bak_mode_with_options(
        self,
        request: main_models.ConfigLayer4RuleBakModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleBakModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bak_mode):
            query['BakMode'] = request.bak_mode
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RuleBakMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleBakModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_bak_mode_with_options_async(
        self,
        request: main_models.ConfigLayer4RuleBakModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RuleBakModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bak_mode):
            query['BakMode'] = request.bak_mode
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RuleBakMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RuleBakModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule_bak_mode(
        self,
        request: main_models.ConfigLayer4RuleBakModeRequest,
    ) -> main_models.ConfigLayer4RuleBakModeResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4rule_bak_mode_with_options(request, runtime)

    async def config_layer_4rule_bak_mode_async(
        self,
        request: main_models.ConfigLayer4RuleBakModeRequest,
    ) -> main_models.ConfigLayer4RuleBakModeResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4rule_bak_mode_with_options_async(request, runtime)

    def config_layer_4rule_policy_with_options(
        self,
        request: main_models.ConfigLayer4RulePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RulePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RulePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_policy_with_options_async(
        self,
        request: main_models.ConfigLayer4RulePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigLayer4RulePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigLayer4RulePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigLayer4RulePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule_policy(
        self,
        request: main_models.ConfigLayer4RulePolicyRequest,
    ) -> main_models.ConfigLayer4RulePolicyResponse:
        runtime = RuntimeOptions()
        return self.config_layer_4rule_policy_with_options(request, runtime)

    async def config_layer_4rule_policy_async(
        self,
        request: main_models.ConfigLayer4RulePolicyRequest,
    ) -> main_models.ConfigLayer4RulePolicyResponse:
        runtime = RuntimeOptions()
        return await self.config_layer_4rule_policy_with_options_async(request, runtime)

    def config_network_region_block_with_options(
        self,
        request: main_models.ConfigNetworkRegionBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetworkRegionBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetworkRegionBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_network_region_block_with_options_async(
        self,
        request: main_models.ConfigNetworkRegionBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetworkRegionBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetworkRegionBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetworkRegionBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_network_region_block(
        self,
        request: main_models.ConfigNetworkRegionBlockRequest,
    ) -> main_models.ConfigNetworkRegionBlockResponse:
        runtime = RuntimeOptions()
        return self.config_network_region_block_with_options(request, runtime)

    async def config_network_region_block_async(
        self,
        request: main_models.ConfigNetworkRegionBlockRequest,
    ) -> main_models.ConfigNetworkRegionBlockResponse:
        runtime = RuntimeOptions()
        return await self.config_network_region_block_with_options_async(request, runtime)

    def config_network_rules_with_options(
        self,
        request: main_models.ConfigNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_network_rules_with_options_async(
        self,
        request: main_models.ConfigNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_network_rules(
        self,
        request: main_models.ConfigNetworkRulesRequest,
    ) -> main_models.ConfigNetworkRulesResponse:
        runtime = RuntimeOptions()
        return self.config_network_rules_with_options(request, runtime)

    async def config_network_rules_async(
        self,
        request: main_models.ConfigNetworkRulesRequest,
    ) -> main_models.ConfigNetworkRulesResponse:
        runtime = RuntimeOptions()
        return await self.config_network_rules_with_options_async(request, runtime)

    def config_udp_reflect_with_options(
        self,
        request: main_models.ConfigUdpReflectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigUdpReflectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigUdpReflect',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_udp_reflect_with_options_async(
        self,
        request: main_models.ConfigUdpReflectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigUdpReflectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigUdpReflect',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigUdpReflectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_udp_reflect(
        self,
        request: main_models.ConfigUdpReflectRequest,
    ) -> main_models.ConfigUdpReflectResponse:
        runtime = RuntimeOptions()
        return self.config_udp_reflect_with_options(request, runtime)

    async def config_udp_reflect_async(
        self,
        request: main_models.ConfigUdpReflectRequest,
    ) -> main_models.ConfigUdpReflectResponse:
        runtime = RuntimeOptions()
        return await self.config_udp_reflect_with_options_async(request, runtime)

    def config_web_ccrule_v2with_options(
        self,
        request: main_models.ConfigWebCCRuleV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebCCRuleV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebCCRuleV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebCCRuleV2Response(),
            self.call_api(params, req, runtime)
        )

    async def config_web_ccrule_v2with_options_async(
        self,
        request: main_models.ConfigWebCCRuleV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebCCRuleV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebCCRuleV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebCCRuleV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def config_web_ccrule_v2(
        self,
        request: main_models.ConfigWebCCRuleV2Request,
    ) -> main_models.ConfigWebCCRuleV2Response:
        runtime = RuntimeOptions()
        return self.config_web_ccrule_v2with_options(request, runtime)

    async def config_web_ccrule_v2_async(
        self,
        request: main_models.ConfigWebCCRuleV2Request,
    ) -> main_models.ConfigWebCCRuleV2Response:
        runtime = RuntimeOptions()
        return await self.config_web_ccrule_v2with_options_async(request, runtime)

    def config_web_cctemplate_with_options(
        self,
        request: main_models.ConfigWebCCTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebCCTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebCCTemplate',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebCCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_web_cctemplate_with_options_async(
        self,
        request: main_models.ConfigWebCCTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebCCTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebCCTemplate',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebCCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_web_cctemplate(
        self,
        request: main_models.ConfigWebCCTemplateRequest,
    ) -> main_models.ConfigWebCCTemplateResponse:
        runtime = RuntimeOptions()
        return self.config_web_cctemplate_with_options(request, runtime)

    async def config_web_cctemplate_async(
        self,
        request: main_models.ConfigWebCCTemplateRequest,
    ) -> main_models.ConfigWebCCTemplateResponse:
        runtime = RuntimeOptions()
        return await self.config_web_cctemplate_with_options_async(request, runtime)

    def config_web_ip_set_with_options(
        self,
        request: main_models.ConfigWebIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_list):
            query['BlackList'] = request.black_list
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebIpSet',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_web_ip_set_with_options_async(
        self,
        request: main_models.ConfigWebIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigWebIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_list):
            query['BlackList'] = request.black_list
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigWebIpSet',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigWebIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_web_ip_set(
        self,
        request: main_models.ConfigWebIpSetRequest,
    ) -> main_models.ConfigWebIpSetResponse:
        runtime = RuntimeOptions()
        return self.config_web_ip_set_with_options(request, runtime)

    async def config_web_ip_set_async(
        self,
        request: main_models.ConfigWebIpSetRequest,
    ) -> main_models.ConfigWebIpSetResponse:
        runtime = RuntimeOptions()
        return await self.config_web_ip_set_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: main_models.CreateAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_params):
            query['TaskParams'] = request.task_params
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: main_models.CreateAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_params):
            query['TaskParams'] = request.task_params
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsyncTask',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_async_task(
        self,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: main_models.CreateAsyncTaskRequest,
    ) -> main_models.CreateAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_domain_resource_with_options(
        self,
        request: main_models.CreateDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_resource_with_options_async(
        self,
        request: main_models.CreateDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_resource(
        self,
        request: main_models.CreateDomainResourceRequest,
    ) -> main_models.CreateDomainResourceResponse:
        runtime = RuntimeOptions()
        return self.create_domain_resource_with_options(request, runtime)

    async def create_domain_resource_async(
        self,
        request: main_models.CreateDomainResourceRequest,
    ) -> main_models.CreateDomainResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_resource_with_options_async(request, runtime)

    def create_network_rules_with_options(
        self,
        request: main_models.CreateNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_rules_with_options_async(
        self,
        request: main_models.CreateNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_rules(
        self,
        request: main_models.CreateNetworkRulesRequest,
    ) -> main_models.CreateNetworkRulesResponse:
        runtime = RuntimeOptions()
        return self.create_network_rules_with_options(request, runtime)

    async def create_network_rules_async(
        self,
        request: main_models.CreateNetworkRulesRequest,
    ) -> main_models.CreateNetworkRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_network_rules_with_options_async(request, runtime)

    def create_port_with_options(
        self,
        request: main_models.CreatePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_port_with_options_async(
        self,
        request: main_models.CreatePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_port(
        self,
        request: main_models.CreatePortRequest,
    ) -> main_models.CreatePortResponse:
        runtime = RuntimeOptions()
        return self.create_port_with_options(request, runtime)

    async def create_port_async(
        self,
        request: main_models.CreatePortRequest,
    ) -> main_models.CreatePortResponse:
        runtime = RuntimeOptions()
        return await self.create_port_with_options_async(request, runtime)

    def create_scene_defense_policy_with_options(
        self,
        request: main_models.CreateSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_defense_policy_with_options_async(
        self,
        request: main_models.CreateSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene_defense_policy(
        self,
        request: main_models.CreateSceneDefensePolicyRequest,
    ) -> main_models.CreateSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_scene_defense_policy_with_options(request, runtime)

    async def create_scene_defense_policy_async(
        self,
        request: main_models.CreateSceneDefensePolicyRequest,
    ) -> main_models.CreateSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_scene_defense_policy_with_options_async(request, runtime)

    def create_scheduler_rule_with_options(
        self,
        request: main_models.CreateSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduler_rule_with_options_async(
        self,
        request: main_models.CreateSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduler_rule(
        self,
        request: main_models.CreateSchedulerRuleRequest,
    ) -> main_models.CreateSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return self.create_scheduler_rule_with_options(request, runtime)

    async def create_scheduler_rule_async(
        self,
        request: main_models.CreateSchedulerRuleRequest,
    ) -> main_models.CreateSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_scheduler_rule_with_options_async(request, runtime)

    def create_tag_resources_with_options(
        self,
        request: main_models.CreateTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_resources_with_options_async(
        self,
        request: main_models.CreateTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_resources(
        self,
        request: main_models.CreateTagResourcesRequest,
    ) -> main_models.CreateTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.create_tag_resources_with_options(request, runtime)

    async def create_tag_resources_async(
        self,
        request: main_models.CreateTagResourcesRequest,
    ) -> main_models.CreateTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_resources_with_options_async(request, runtime)

    def create_web_ccrule_with_options(
        self,
        request: main_models.CreateWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_ccrule_with_options_async(
        self,
        request: main_models.CreateWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_ccrule(
        self,
        request: main_models.CreateWebCCRuleRequest,
    ) -> main_models.CreateWebCCRuleResponse:
        runtime = RuntimeOptions()
        return self.create_web_ccrule_with_options(request, runtime)

    async def create_web_ccrule_async(
        self,
        request: main_models.CreateWebCCRuleRequest,
    ) -> main_models.CreateWebCCRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_web_ccrule_with_options_async(request, runtime)

    def create_web_rule_with_options(
        self,
        request: main_models.CreateWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_id):
            query['DefenseId'] = request.defense_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_rule_with_options_async(
        self,
        request: main_models.CreateWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_id):
            query['DefenseId'] = request.defense_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_rule(
        self,
        request: main_models.CreateWebRuleRequest,
    ) -> main_models.CreateWebRuleResponse:
        runtime = RuntimeOptions()
        return self.create_web_rule_with_options(request, runtime)

    async def create_web_rule_async(
        self,
        request: main_models.CreateWebRuleRequest,
    ) -> main_models.CreateWebRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_web_rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: main_models.DeleteAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncTask',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: main_models.DeleteAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsyncTask',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_async_task(
        self,
        request: main_models.DeleteAsyncTaskRequest,
    ) -> main_models.DeleteAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: main_models.DeleteAsyncTaskRequest,
    ) -> main_models.DeleteAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_auto_cc_blacklist_with_options(
        self,
        request: main_models.DeleteAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_cc_blacklist_with_options_async(
        self,
        request: main_models.DeleteAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_cc_blacklist(
        self,
        request: main_models.DeleteAutoCcBlacklistRequest,
    ) -> main_models.DeleteAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_cc_blacklist_with_options(request, runtime)

    async def delete_auto_cc_blacklist_async(
        self,
        request: main_models.DeleteAutoCcBlacklistRequest,
    ) -> main_models.DeleteAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_cc_blacklist_with_options_async(request, runtime)

    def delete_auto_cc_whitelist_with_options(
        self,
        request: main_models.DeleteAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_cc_whitelist_with_options_async(
        self,
        request: main_models.DeleteAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_cc_whitelist(
        self,
        request: main_models.DeleteAutoCcWhitelistRequest,
    ) -> main_models.DeleteAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_cc_whitelist_with_options(request, runtime)

    async def delete_auto_cc_whitelist_async(
        self,
        request: main_models.DeleteAutoCcWhitelistRequest,
    ) -> main_models.DeleteAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_cc_whitelist_with_options_async(request, runtime)

    def delete_domain_resource_with_options(
        self,
        request: main_models.DeleteDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_resource_with_options_async(
        self,
        request: main_models.DeleteDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_resource(
        self,
        request: main_models.DeleteDomainResourceRequest,
    ) -> main_models.DeleteDomainResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_resource_with_options(request, runtime)

    async def delete_domain_resource_async(
        self,
        request: main_models.DeleteDomainResourceRequest,
    ) -> main_models.DeleteDomainResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_resource_with_options_async(request, runtime)

    def delete_network_rule_with_options(
        self,
        request: main_models.DeleteNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rule):
            query['NetworkRule'] = request.network_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_rule_with_options_async(
        self,
        request: main_models.DeleteNetworkRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rule):
            query['NetworkRule'] = request.network_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_rule(
        self,
        request: main_models.DeleteNetworkRuleRequest,
    ) -> main_models.DeleteNetworkRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    async def delete_network_rule_async(
        self,
        request: main_models.DeleteNetworkRuleRequest,
    ) -> main_models.DeleteNetworkRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_rule_with_options_async(request, runtime)

    def delete_port_with_options(
        self,
        request: main_models.DeletePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_port_with_options_async(
        self,
        request: main_models.DeletePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_port(
        self,
        request: main_models.DeletePortRequest,
    ) -> main_models.DeletePortResponse:
        runtime = RuntimeOptions()
        return self.delete_port_with_options(request, runtime)

    async def delete_port_async(
        self,
        request: main_models.DeletePortRequest,
    ) -> main_models.DeletePortResponse:
        runtime = RuntimeOptions()
        return await self.delete_port_with_options_async(request, runtime)

    def delete_scene_defense_policy_with_options(
        self,
        request: main_models.DeleteSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_defense_policy_with_options_async(
        self,
        request: main_models.DeleteSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene_defense_policy(
        self,
        request: main_models.DeleteSceneDefensePolicyRequest,
    ) -> main_models.DeleteSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_scene_defense_policy_with_options(request, runtime)

    async def delete_scene_defense_policy_async(
        self,
        request: main_models.DeleteSceneDefensePolicyRequest,
    ) -> main_models.DeleteSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_scene_defense_policy_with_options_async(request, runtime)

    def delete_scheduler_rule_with_options(
        self,
        request: main_models.DeleteSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduler_rule_with_options_async(
        self,
        request: main_models.DeleteSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduler_rule(
        self,
        request: main_models.DeleteSchedulerRuleRequest,
    ) -> main_models.DeleteSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_scheduler_rule_with_options(request, runtime)

    async def delete_scheduler_rule_async(
        self,
        request: main_models.DeleteSchedulerRuleRequest,
    ) -> main_models.DeleteSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheduler_rule_with_options_async(request, runtime)

    def delete_tag_resources_with_options(
        self,
        request: main_models.DeleteTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_resources_with_options_async(
        self,
        request: main_models.DeleteTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_resources(
        self,
        request: main_models.DeleteTagResourcesRequest,
    ) -> main_models.DeleteTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_resources_with_options(request, runtime)

    async def delete_tag_resources_async(
        self,
        request: main_models.DeleteTagResourcesRequest,
    ) -> main_models.DeleteTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_resources_with_options_async(request, runtime)

    def delete_web_ccrule_with_options(
        self,
        request: main_models.DeleteWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_ccrule_with_options_async(
        self,
        request: main_models.DeleteWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_ccrule(
        self,
        request: main_models.DeleteWebCCRuleRequest,
    ) -> main_models.DeleteWebCCRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_web_ccrule_with_options(request, runtime)

    async def delete_web_ccrule_async(
        self,
        request: main_models.DeleteWebCCRuleRequest,
    ) -> main_models.DeleteWebCCRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_ccrule_with_options_async(request, runtime)

    def delete_web_ccrule_v2with_options(
        self,
        request: main_models.DeleteWebCCRuleV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCCRuleV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCCRuleV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCCRuleV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_ccrule_v2with_options_async(
        self,
        request: main_models.DeleteWebCCRuleV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCCRuleV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCCRuleV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCCRuleV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_ccrule_v2(
        self,
        request: main_models.DeleteWebCCRuleV2Request,
    ) -> main_models.DeleteWebCCRuleV2Response:
        runtime = RuntimeOptions()
        return self.delete_web_ccrule_v2with_options(request, runtime)

    async def delete_web_ccrule_v2_async(
        self,
        request: main_models.DeleteWebCCRuleV2Request,
    ) -> main_models.DeleteWebCCRuleV2Response:
        runtime = RuntimeOptions()
        return await self.delete_web_ccrule_v2with_options_async(request, runtime)

    def delete_web_cache_custom_rule_with_options(
        self,
        request: main_models.DeleteWebCacheCustomRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCacheCustomRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCacheCustomRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_cache_custom_rule_with_options_async(
        self,
        request: main_models.DeleteWebCacheCustomRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCacheCustomRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCacheCustomRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCacheCustomRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_cache_custom_rule(
        self,
        request: main_models.DeleteWebCacheCustomRuleRequest,
    ) -> main_models.DeleteWebCacheCustomRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_web_cache_custom_rule_with_options(request, runtime)

    async def delete_web_cache_custom_rule_async(
        self,
        request: main_models.DeleteWebCacheCustomRuleRequest,
    ) -> main_models.DeleteWebCacheCustomRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_cache_custom_rule_with_options_async(request, runtime)

    def delete_web_precise_access_rule_with_options(
        self,
        request: main_models.DeleteWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_precise_access_rule_with_options_async(
        self,
        request: main_models.DeleteWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_precise_access_rule(
        self,
        request: main_models.DeleteWebPreciseAccessRuleRequest,
    ) -> main_models.DeleteWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_web_precise_access_rule_with_options(request, runtime)

    async def delete_web_precise_access_rule_async(
        self,
        request: main_models.DeleteWebPreciseAccessRuleRequest,
    ) -> main_models.DeleteWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_precise_access_rule_with_options_async(request, runtime)

    def delete_web_rule_with_options(
        self,
        request: main_models.DeleteWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_rule_with_options_async(
        self,
        request: main_models.DeleteWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_rule(
        self,
        request: main_models.DeleteWebRuleRequest,
    ) -> main_models.DeleteWebRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_web_rule_with_options(request, runtime)

    async def delete_web_rule_async(
        self,
        request: main_models.DeleteWebRuleRequest,
    ) -> main_models.DeleteWebRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_rule_with_options_async(request, runtime)

    def describe_async_tasks_with_options(
        self,
        request: main_models.DescribeAsyncTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAsyncTasks',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_async_tasks_with_options_async(
        self,
        request: main_models.DescribeAsyncTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAsyncTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAsyncTasks',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_async_tasks(
        self,
        request: main_models.DescribeAsyncTasksRequest,
    ) -> main_models.DescribeAsyncTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_async_tasks_with_options(request, runtime)

    async def describe_async_tasks_async(
        self,
        request: main_models.DescribeAsyncTasksRequest,
    ) -> main_models.DescribeAsyncTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_async_tasks_with_options_async(request, runtime)

    def describe_attack_analysis_max_qps_with_options(
        self,
        request: main_models.DescribeAttackAnalysisMaxQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackAnalysisMaxQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackAnalysisMaxQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackAnalysisMaxQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_analysis_max_qps_with_options_async(
        self,
        request: main_models.DescribeAttackAnalysisMaxQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackAnalysisMaxQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackAnalysisMaxQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackAnalysisMaxQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_analysis_max_qps(
        self,
        request: main_models.DescribeAttackAnalysisMaxQpsRequest,
    ) -> main_models.DescribeAttackAnalysisMaxQpsResponse:
        runtime = RuntimeOptions()
        return self.describe_attack_analysis_max_qps_with_options(request, runtime)

    async def describe_attack_analysis_max_qps_async(
        self,
        request: main_models.DescribeAttackAnalysisMaxQpsRequest,
    ) -> main_models.DescribeAttackAnalysisMaxQpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_attack_analysis_max_qps_with_options_async(request, runtime)

    def describe_auto_cc_blacklist_with_options(
        self,
        request: main_models.DescribeAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_blacklist_with_options_async(
        self,
        request: main_models.DescribeAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_cc_blacklist(
        self,
        request: main_models.DescribeAutoCcBlacklistRequest,
    ) -> main_models.DescribeAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_cc_blacklist_with_options(request, runtime)

    async def describe_auto_cc_blacklist_async(
        self,
        request: main_models.DescribeAutoCcBlacklistRequest,
    ) -> main_models.DescribeAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_cc_blacklist_with_options_async(request, runtime)

    def describe_auto_cc_list_count_with_options(
        self,
        request: main_models.DescribeAutoCcListCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcListCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcListCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcListCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_list_count_with_options_async(
        self,
        request: main_models.DescribeAutoCcListCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcListCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcListCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcListCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_cc_list_count(
        self,
        request: main_models.DescribeAutoCcListCountRequest,
    ) -> main_models.DescribeAutoCcListCountResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_cc_list_count_with_options(request, runtime)

    async def describe_auto_cc_list_count_async(
        self,
        request: main_models.DescribeAutoCcListCountRequest,
    ) -> main_models.DescribeAutoCcListCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_cc_list_count_with_options_async(request, runtime)

    def describe_auto_cc_whitelist_with_options(
        self,
        request: main_models.DescribeAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_cc_whitelist_with_options_async(
        self,
        request: main_models.DescribeAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_cc_whitelist(
        self,
        request: main_models.DescribeAutoCcWhitelistRequest,
    ) -> main_models.DescribeAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_cc_whitelist_with_options(request, runtime)

    async def describe_auto_cc_whitelist_async(
        self,
        request: main_models.DescribeAutoCcWhitelistRequest,
    ) -> main_models.DescribeAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_cc_whitelist_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackSourceCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackSourceCidr',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackSourceCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackSourceCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.line):
            query['Line'] = request.line
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackSourceCidr',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackSourceCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_back_source_cidr(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
    ) -> main_models.DescribeBackSourceCidrResponse:
        runtime = RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: main_models.DescribeBackSourceCidrRequest,
    ) -> main_models.DescribeBackSourceCidrResponse:
        runtime = RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_blackhole_status_with_options(
        self,
        request: main_models.DescribeBlackholeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlackholeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlackholeStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blackhole_status_with_options_async(
        self,
        request: main_models.DescribeBlackholeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlackholeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlackholeStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlackholeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blackhole_status(
        self,
        request: main_models.DescribeBlackholeStatusRequest,
    ) -> main_models.DescribeBlackholeStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_blackhole_status_with_options(request, runtime)

    async def describe_blackhole_status_async(
        self,
        request: main_models.DescribeBlackholeStatusRequest,
    ) -> main_models.DescribeBlackholeStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_blackhole_status_with_options_async(request, runtime)

    def describe_block_status_with_options(
        self,
        request: main_models.DescribeBlockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlockStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlockStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_block_status_with_options_async(
        self,
        request: main_models.DescribeBlockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlockStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlockStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_block_status(
        self,
        request: main_models.DescribeBlockStatusRequest,
    ) -> main_models.DescribeBlockStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_block_status_with_options(request, runtime)

    async def describe_block_status_async(
        self,
        request: main_models.DescribeBlockStatusRequest,
    ) -> main_models.DescribeBlockStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_block_status_with_options_async(request, runtime)

    def describe_cdn_linkage_rules_with_options(
        self,
        request: main_models.DescribeCdnLinkageRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnLinkageRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnLinkageRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnLinkageRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_linkage_rules_with_options_async(
        self,
        request: main_models.DescribeCdnLinkageRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdnLinkageRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdnLinkageRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdnLinkageRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_linkage_rules(
        self,
        request: main_models.DescribeCdnLinkageRulesRequest,
    ) -> main_models.DescribeCdnLinkageRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_cdn_linkage_rules_with_options(request, runtime)

    async def describe_cdn_linkage_rules_async(
        self,
        request: main_models.DescribeCdnLinkageRulesRequest,
    ) -> main_models.DescribeCdnLinkageRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdn_linkage_rules_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: main_models.DescribeCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCerts',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: main_models.DescribeCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCerts',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certs(
        self,
        request: main_models.DescribeCertsRequest,
    ) -> main_models.DescribeCertsResponse:
        runtime = RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: main_models.DescribeCertsRequest,
    ) -> main_models.DescribeCertsResponse:
        runtime = RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_cname_reuses_with_options(
        self,
        request: main_models.DescribeCnameReusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCnameReusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCnameReuses',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCnameReusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cname_reuses_with_options_async(
        self,
        request: main_models.DescribeCnameReusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCnameReusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCnameReuses',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCnameReusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cname_reuses(
        self,
        request: main_models.DescribeCnameReusesRequest,
    ) -> main_models.DescribeCnameReusesResponse:
        runtime = RuntimeOptions()
        return self.describe_cname_reuses_with_options(request, runtime)

    async def describe_cname_reuses_async(
        self,
        request: main_models.DescribeCnameReusesRequest,
    ) -> main_models.DescribeCnameReusesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cname_reuses_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: main_models.DescribeDDoSEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSEvents',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: main_models.DescribeDDoSEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSEvents',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddo_sevents(
        self,
        request: main_models.DescribeDDoSEventsRequest,
    ) -> main_models.DescribeDDoSEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: main_models.DescribeDDoSEventsRequest,
    ) -> main_models.DescribeDDoSEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddos_all_event_list_with_options(
        self,
        request: main_models.DescribeDDosAllEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosAllEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosAllEventList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosAllEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_all_event_list_with_options_async(
        self,
        request: main_models.DescribeDDosAllEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosAllEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosAllEventList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosAllEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_all_event_list(
        self,
        request: main_models.DescribeDDosAllEventListRequest,
    ) -> main_models.DescribeDDosAllEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    async def describe_ddos_all_event_list_async(
        self,
        request: main_models.DescribeDDosAllEventListRequest,
    ) -> main_models.DescribeDDosAllEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_all_event_list_with_options_async(request, runtime)

    def describe_ddos_event_area_with_options(
        self,
        request: main_models.DescribeDDosEventAreaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventAreaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventArea',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventAreaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_area_with_options_async(
        self,
        request: main_models.DescribeDDosEventAreaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventAreaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventArea',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventAreaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_area(
        self,
        request: main_models.DescribeDDosEventAreaRequest,
    ) -> main_models.DescribeDDosEventAreaResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_area_with_options(request, runtime)

    async def describe_ddos_event_area_async(
        self,
        request: main_models.DescribeDDosEventAreaRequest,
    ) -> main_models.DescribeDDosEventAreaResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_area_with_options_async(request, runtime)

    def describe_ddos_event_attack_type_with_options(
        self,
        request: main_models.DescribeDDosEventAttackTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventAttackTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventAttackType',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventAttackTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_attack_type_with_options_async(
        self,
        request: main_models.DescribeDDosEventAttackTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventAttackTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventAttackType',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventAttackTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_attack_type(
        self,
        request: main_models.DescribeDDosEventAttackTypeRequest,
    ) -> main_models.DescribeDDosEventAttackTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_attack_type_with_options(request, runtime)

    async def describe_ddos_event_attack_type_async(
        self,
        request: main_models.DescribeDDosEventAttackTypeRequest,
    ) -> main_models.DescribeDDosEventAttackTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_attack_type_with_options_async(request, runtime)

    def describe_ddos_event_isp_with_options(
        self,
        request: main_models.DescribeDDosEventIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventIspResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventIsp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_isp_with_options_async(
        self,
        request: main_models.DescribeDDosEventIspRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventIspResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventIsp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventIspResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_isp(
        self,
        request: main_models.DescribeDDosEventIspRequest,
    ) -> main_models.DescribeDDosEventIspResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_isp_with_options(request, runtime)

    async def describe_ddos_event_isp_async(
        self,
        request: main_models.DescribeDDosEventIspRequest,
    ) -> main_models.DescribeDDosEventIspResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_isp_with_options_async(request, runtime)

    def describe_ddos_event_max_with_options(
        self,
        request: main_models.DescribeDDosEventMaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventMaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventMax',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventMaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_max_with_options_async(
        self,
        request: main_models.DescribeDDosEventMaxRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventMaxResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventMax',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventMaxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_max(
        self,
        request: main_models.DescribeDDosEventMaxRequest,
    ) -> main_models.DescribeDDosEventMaxResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_max_with_options(request, runtime)

    async def describe_ddos_event_max_async(
        self,
        request: main_models.DescribeDDosEventMaxRequest,
    ) -> main_models.DescribeDDosEventMaxResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_max_with_options_async(request, runtime)

    def describe_ddos_event_src_ip_with_options(
        self,
        request: main_models.DescribeDDosEventSrcIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventSrcIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventSrcIp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventSrcIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_src_ip_with_options_async(
        self,
        request: main_models.DescribeDDosEventSrcIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDosEventSrcIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDosEventSrcIp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDosEventSrcIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_src_ip(
        self,
        request: main_models.DescribeDDosEventSrcIpRequest,
    ) -> main_models.DescribeDDosEventSrcIpResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_src_ip_with_options(request, runtime)

    async def describe_ddos_event_src_ip_async(
        self,
        request: main_models.DescribeDDosEventSrcIpRequest,
    ) -> main_models.DescribeDDosEventSrcIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_src_ip_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseCountStatistics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseCountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseCountStatistics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseCountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_count_statistics(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: main_models.DescribeDefenseCountStatisticsRequest,
    ) -> main_models.DescribeDefenseCountStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_defense_records_with_options(
        self,
        request: main_models.DescribeDefenseRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRecords',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_records_with_options_async(
        self,
        request: main_models.DescribeDefenseRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRecords',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_records(
        self,
        request: main_models.DescribeDefenseRecordsRequest,
    ) -> main_models.DescribeDefenseRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_records_with_options(request, runtime)

    async def describe_defense_records_async(
        self,
        request: main_models.DescribeDefenseRecordsRequest,
    ) -> main_models.DescribeDefenseRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_records_with_options_async(request, runtime)

    def describe_destination_port_event_with_options(
        self,
        request: main_models.DescribeDestinationPortEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDestinationPortEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDestinationPortEvent',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDestinationPortEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_destination_port_event_with_options_async(
        self,
        request: main_models.DescribeDestinationPortEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDestinationPortEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDestinationPortEvent',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDestinationPortEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_destination_port_event(
        self,
        request: main_models.DescribeDestinationPortEventRequest,
    ) -> main_models.DescribeDestinationPortEventResponse:
        runtime = RuntimeOptions()
        return self.describe_destination_port_event_with_options(request, runtime)

    async def describe_destination_port_event_async(
        self,
        request: main_models.DescribeDestinationPortEventRequest,
    ) -> main_models.DescribeDestinationPortEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_destination_port_event_with_options_async(request, runtime)

    def describe_domain_attack_events_with_options(
        self,
        request: main_models.DescribeDomainAttackEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackEvents',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_attack_events_with_options_async(
        self,
        request: main_models.DescribeDomainAttackEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainAttackEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainAttackEvents',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainAttackEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_attack_events(
        self,
        request: main_models.DescribeDomainAttackEventsRequest,
    ) -> main_models.DescribeDomainAttackEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    async def describe_domain_attack_events_async(
        self,
        request: main_models.DescribeDomainAttackEventsRequest,
    ) -> main_models.DescribeDomainAttackEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_attack_events_with_options_async(request, runtime)

    def describe_domain_bps_with_options(
        self,
        request: main_models.DescribeDomainBpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainBps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_with_options_async(
        self,
        request: main_models.DescribeDomainBpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainBpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainBps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainBpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps(
        self,
        request: main_models.DescribeDomainBpsRequest,
    ) -> main_models.DescribeDomainBpsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_bps_with_options(request, runtime)

    async def describe_domain_bps_async(
        self,
        request: main_models.DescribeDomainBpsRequest,
    ) -> main_models.DescribeDomainBpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_bps_with_options_async(request, runtime)

    def describe_domain_cc_protect_switch_with_options(
        self,
        request: main_models.DescribeDomainCcProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCcProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCcProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCcProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_cc_protect_switch_with_options_async(
        self,
        request: main_models.DescribeDomainCcProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainCcProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainCcProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainCcProtectSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_cc_protect_switch(
        self,
        request: main_models.DescribeDomainCcProtectSwitchRequest,
    ) -> main_models.DescribeDomainCcProtectSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_cc_protect_switch_with_options(request, runtime)

    async def describe_domain_cc_protect_switch_async(
        self,
        request: main_models.DescribeDomainCcProtectSwitchRequest,
    ) -> main_models.DescribeDomainCcProtectSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_cc_protect_switch_with_options_async(request, runtime)

    def describe_domain_h2fingerprint_with_options(
        self,
        request: main_models.DescribeDomainH2FingerprintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainH2FingerprintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainH2Fingerprint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainH2FingerprintResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_h2fingerprint_with_options_async(
        self,
        request: main_models.DescribeDomainH2FingerprintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainH2FingerprintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainH2Fingerprint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainH2FingerprintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_h2fingerprint(
        self,
        request: main_models.DescribeDomainH2FingerprintRequest,
    ) -> main_models.DescribeDomainH2FingerprintResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_h2fingerprint_with_options(request, runtime)

    async def describe_domain_h2fingerprint_async(
        self,
        request: main_models.DescribeDomainH2FingerprintRequest,
    ) -> main_models.DescribeDomainH2FingerprintResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_h2fingerprint_with_options_async(request, runtime)

    def describe_domain_overview_with_options(
        self,
        request: main_models.DescribeDomainOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainOverview',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_overview_with_options_async(
        self,
        request: main_models.DescribeDomainOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainOverview',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_overview(
        self,
        request: main_models.DescribeDomainOverviewRequest,
    ) -> main_models.DescribeDomainOverviewResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    async def describe_domain_overview_async(
        self,
        request: main_models.DescribeDomainOverviewRequest,
    ) -> main_models.DescribeDomainOverviewResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_overview_with_options_async(request, runtime)

    def describe_domain_qpslist_with_options(
        self,
        request: main_models.DescribeDomainQPSListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQPSListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQPSList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQPSListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qpslist_with_options_async(
        self,
        request: main_models.DescribeDomainQPSListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainQPSListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainQPSList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainQPSListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qpslist(
        self,
        request: main_models.DescribeDomainQPSListRequest,
    ) -> main_models.DescribeDomainQPSListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_qpslist_with_options(request, runtime)

    async def describe_domain_qpslist_async(
        self,
        request: main_models.DescribeDomainQPSListRequest,
    ) -> main_models.DescribeDomainQPSListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_qpslist_with_options_async(request, runtime)

    def describe_domain_resource_with_options(
        self,
        request: main_models.DescribeDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resource_with_options_async(
        self,
        request: main_models.DescribeDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resource(
        self,
        request: main_models.DescribeDomainResourceRequest,
    ) -> main_models.DescribeDomainResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_resource_with_options(request, runtime)

    async def describe_domain_resource_async(
        self,
        request: main_models.DescribeDomainResourceRequest,
    ) -> main_models.DescribeDomainResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_resource_with_options_async(request, runtime)

    def describe_domain_security_profile_with_options(
        self,
        request: main_models.DescribeDomainSecurityProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSecurityProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSecurityProfile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSecurityProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_security_profile_with_options_async(
        self,
        request: main_models.DescribeDomainSecurityProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainSecurityProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainSecurityProfile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainSecurityProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_security_profile(
        self,
        request: main_models.DescribeDomainSecurityProfileRequest,
    ) -> main_models.DescribeDomainSecurityProfileResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_security_profile_with_options(request, runtime)

    async def describe_domain_security_profile_async(
        self,
        request: main_models.DescribeDomainSecurityProfileRequest,
    ) -> main_models.DescribeDomainSecurityProfileResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_security_profile_with_options_async(request, runtime)

    def describe_domain_status_code_count_with_options(
        self,
        request: main_models.DescribeDomainStatusCodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_status_code_count_with_options_async(
        self,
        request: main_models.DescribeDomainStatusCodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_status_code_count(
        self,
        request: main_models.DescribeDomainStatusCodeCountRequest,
    ) -> main_models.DescribeDomainStatusCodeCountResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_status_code_count_with_options(request, runtime)

    async def describe_domain_status_code_count_async(
        self,
        request: main_models.DescribeDomainStatusCodeCountRequest,
    ) -> main_models.DescribeDomainStatusCodeCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_status_code_count_with_options_async(request, runtime)

    def describe_domain_status_code_list_with_options(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_status_code_list_with_options_async(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainStatusCodeList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainStatusCodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_status_code_list(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    async def describe_domain_status_code_list_async(
        self,
        request: main_models.DescribeDomainStatusCodeListRequest,
    ) -> main_models.DescribeDomainStatusCodeListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_status_code_list_with_options_async(request, runtime)

    def describe_domain_top_attack_list_with_options(
        self,
        request: main_models.DescribeDomainTopAttackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopAttackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopAttackList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopAttackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_attack_list_with_options_async(
        self,
        request: main_models.DescribeDomainTopAttackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopAttackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopAttackList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopAttackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_attack_list(
        self,
        request: main_models.DescribeDomainTopAttackListRequest,
    ) -> main_models.DescribeDomainTopAttackListResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_attack_list_with_options(request, runtime)

    async def describe_domain_top_attack_list_async(
        self,
        request: main_models.DescribeDomainTopAttackListRequest,
    ) -> main_models.DescribeDomainTopAttackListResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_attack_list_with_options_async(request, runtime)

    def describe_domain_top_fingerprint_with_options(
        self,
        request: main_models.DescribeDomainTopFingerprintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopFingerprintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopFingerprint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopFingerprintResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_fingerprint_with_options_async(
        self,
        request: main_models.DescribeDomainTopFingerprintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopFingerprintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopFingerprint',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopFingerprintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_fingerprint(
        self,
        request: main_models.DescribeDomainTopFingerprintRequest,
    ) -> main_models.DescribeDomainTopFingerprintResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_fingerprint_with_options(request, runtime)

    async def describe_domain_top_fingerprint_async(
        self,
        request: main_models.DescribeDomainTopFingerprintRequest,
    ) -> main_models.DescribeDomainTopFingerprintResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_fingerprint_with_options_async(request, runtime)

    def describe_domain_top_http_method_with_options(
        self,
        request: main_models.DescribeDomainTopHttpMethodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopHttpMethodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopHttpMethod',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopHttpMethodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_http_method_with_options_async(
        self,
        request: main_models.DescribeDomainTopHttpMethodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopHttpMethodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopHttpMethod',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopHttpMethodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_http_method(
        self,
        request: main_models.DescribeDomainTopHttpMethodRequest,
    ) -> main_models.DescribeDomainTopHttpMethodResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_http_method_with_options(request, runtime)

    async def describe_domain_top_http_method_async(
        self,
        request: main_models.DescribeDomainTopHttpMethodRequest,
    ) -> main_models.DescribeDomainTopHttpMethodResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_http_method_with_options_async(request, runtime)

    def describe_domain_top_referer_with_options(
        self,
        request: main_models.DescribeDomainTopRefererRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopRefererResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopReferer',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopRefererResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_referer_with_options_async(
        self,
        request: main_models.DescribeDomainTopRefererRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopRefererResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopReferer',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopRefererResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_referer(
        self,
        request: main_models.DescribeDomainTopRefererRequest,
    ) -> main_models.DescribeDomainTopRefererResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_referer_with_options(request, runtime)

    async def describe_domain_top_referer_async(
        self,
        request: main_models.DescribeDomainTopRefererRequest,
    ) -> main_models.DescribeDomainTopRefererResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_referer_with_options_async(request, runtime)

    def describe_domain_top_user_agent_with_options(
        self,
        request: main_models.DescribeDomainTopUserAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopUserAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopUserAgent',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopUserAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_user_agent_with_options_async(
        self,
        request: main_models.DescribeDomainTopUserAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainTopUserAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainTopUserAgent',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainTopUserAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_user_agent(
        self,
        request: main_models.DescribeDomainTopUserAgentRequest,
    ) -> main_models.DescribeDomainTopUserAgentResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_top_user_agent_with_options(request, runtime)

    async def describe_domain_top_user_agent_async(
        self,
        request: main_models.DescribeDomainTopUserAgentRequest,
    ) -> main_models.DescribeDomainTopUserAgentResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_top_user_agent_with_options_async(request, runtime)

    def describe_domain_view_source_countries_with_options(
        self,
        request: main_models.DescribeDomainViewSourceCountriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewSourceCountriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewSourceCountries',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_source_countries_with_options_async(
        self,
        request: main_models.DescribeDomainViewSourceCountriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewSourceCountriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewSourceCountries',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewSourceCountriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_view_source_countries(
        self,
        request: main_models.DescribeDomainViewSourceCountriesRequest,
    ) -> main_models.DescribeDomainViewSourceCountriesResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_view_source_countries_with_options(request, runtime)

    async def describe_domain_view_source_countries_async(
        self,
        request: main_models.DescribeDomainViewSourceCountriesRequest,
    ) -> main_models.DescribeDomainViewSourceCountriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_view_source_countries_with_options_async(request, runtime)

    def describe_domain_view_source_provinces_with_options(
        self,
        request: main_models.DescribeDomainViewSourceProvincesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewSourceProvincesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewSourceProvinces',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_source_provinces_with_options_async(
        self,
        request: main_models.DescribeDomainViewSourceProvincesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewSourceProvincesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewSourceProvinces',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewSourceProvincesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_view_source_provinces(
        self,
        request: main_models.DescribeDomainViewSourceProvincesRequest,
    ) -> main_models.DescribeDomainViewSourceProvincesResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_view_source_provinces_with_options(request, runtime)

    async def describe_domain_view_source_provinces_async(
        self,
        request: main_models.DescribeDomainViewSourceProvincesRequest,
    ) -> main_models.DescribeDomainViewSourceProvincesResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_view_source_provinces_with_options_async(request, runtime)

    def describe_domain_view_top_cost_time_with_options(
        self,
        request: main_models.DescribeDomainViewTopCostTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewTopCostTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewTopCostTime',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewTopCostTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_top_cost_time_with_options_async(
        self,
        request: main_models.DescribeDomainViewTopCostTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewTopCostTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewTopCostTime',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewTopCostTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_view_top_cost_time(
        self,
        request: main_models.DescribeDomainViewTopCostTimeRequest,
    ) -> main_models.DescribeDomainViewTopCostTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_view_top_cost_time_with_options(request, runtime)

    async def describe_domain_view_top_cost_time_async(
        self,
        request: main_models.DescribeDomainViewTopCostTimeRequest,
    ) -> main_models.DescribeDomainViewTopCostTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_view_top_cost_time_with_options_async(request, runtime)

    def describe_domain_view_top_url_with_options(
        self,
        request: main_models.DescribeDomainViewTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.inerval):
            query['Inerval'] = request.inerval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewTopUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_view_top_url_with_options_async(
        self,
        request: main_models.DescribeDomainViewTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainViewTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.inerval):
            query['Inerval'] = request.inerval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainViewTopUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainViewTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_view_top_url(
        self,
        request: main_models.DescribeDomainViewTopUrlRequest,
    ) -> main_models.DescribeDomainViewTopUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_view_top_url_with_options(request, runtime)

    async def describe_domain_view_top_url_async(
        self,
        request: main_models.DescribeDomainViewTopUrlRequest,
    ) -> main_models.DescribeDomainViewTopUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_view_top_url_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticBandwidthSpec',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticBandwidthSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticBandwidthSpec',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticBandwidthSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_bandwidth_spec(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: main_models.DescribeElasticBandwidthSpecRequest,
    ) -> main_models.DescribeElasticBandwidthSpecResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_elastic_qps_with_options(
        self,
        request: main_models.DescribeElasticQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_qps_with_options_async(
        self,
        request: main_models.DescribeElasticQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_qps(
        self,
        request: main_models.DescribeElasticQpsRequest,
    ) -> main_models.DescribeElasticQpsResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_qps_with_options(request, runtime)

    async def describe_elastic_qps_async(
        self,
        request: main_models.DescribeElasticQpsRequest,
    ) -> main_models.DescribeElasticQpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_qps_with_options_async(request, runtime)

    def describe_elastic_qps_record_with_options(
        self,
        request: main_models.DescribeElasticQpsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticQpsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticQpsRecord',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticQpsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_qps_record_with_options_async(
        self,
        request: main_models.DescribeElasticQpsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticQpsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticQpsRecord',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticQpsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_qps_record(
        self,
        request: main_models.DescribeElasticQpsRecordRequest,
    ) -> main_models.DescribeElasticQpsRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_qps_record_with_options(request, runtime)

    async def describe_elastic_qps_record_async(
        self,
        request: main_models.DescribeElasticQpsRecordRequest,
    ) -> main_models.DescribeElasticQpsRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_qps_record_with_options_async(request, runtime)

    def describe_headers_with_options(
        self,
        request: main_models.DescribeHeadersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHeadersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHeaders',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_headers_with_options_async(
        self,
        request: main_models.DescribeHeadersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHeadersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHeaders',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHeadersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_headers(
        self,
        request: main_models.DescribeHeadersRequest,
    ) -> main_models.DescribeHeadersResponse:
        runtime = RuntimeOptions()
        return self.describe_headers_with_options(request, runtime)

    async def describe_headers_async(
        self,
        request: main_models.DescribeHeadersRequest,
    ) -> main_models.DescribeHeadersResponse:
        runtime = RuntimeOptions()
        return await self.describe_headers_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: main_models.DescribeHealthCheckListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: main_models.DescribeHealthCheckListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_check_list(
        self,
        request: main_models.DescribeHealthCheckListRequest,
    ) -> main_models.DescribeHealthCheckListResponse:
        runtime = RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: main_models.DescribeHealthCheckListRequest,
    ) -> main_models.DescribeHealthCheckListResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_with_options(
        self,
        request: main_models.DescribeHealthCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_check_status_with_options_async(
        self,
        request: main_models.DescribeHealthCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthCheckStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_check_status(
        self,
        request: main_models.DescribeHealthCheckStatusRequest,
    ) -> main_models.DescribeHealthCheckStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_health_check_status_with_options(request, runtime)

    async def describe_health_check_status_async(
        self,
        request: main_models.DescribeHealthCheckStatusRequest,
    ) -> main_models.DescribeHealthCheckStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_check_status_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDetails',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_details(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
    ) -> main_models.DescribeInstanceDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: main_models.DescribeInstanceDetailsRequest,
    ) -> main_models.DescribeInstanceDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instance_ext_with_options(
        self,
        request: main_models.DescribeInstanceExtRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceExtResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceExt',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ext_with_options_async(
        self,
        request: main_models.DescribeInstanceExtRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceExtResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceExt',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ext(
        self,
        request: main_models.DescribeInstanceExtRequest,
    ) -> main_models.DescribeInstanceExtResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_ext_with_options(request, runtime)

    async def describe_instance_ext_async(
        self,
        request: main_models.DescribeInstanceExtRequest,
    ) -> main_models.DescribeInstanceExtResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_ext_with_options_async(request, runtime)

    def describe_instance_ids_with_options(
        self,
        request: main_models.DescribeInstanceIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIds',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ids_with_options_async(
        self,
        request: main_models.DescribeInstanceIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIds',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ids(
        self,
        request: main_models.DescribeInstanceIdsRequest,
    ) -> main_models.DescribeInstanceIdsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_ids_with_options(request, runtime)

    async def describe_instance_ids_async(
        self,
        request: main_models.DescribeInstanceIdsRequest,
    ) -> main_models.DescribeInstanceIdsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_ids_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specs(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
    ) -> main_models.DescribeInstanceSpecsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: main_models.DescribeInstanceSpecsRequest,
    ) -> main_models.DescribeInstanceSpecsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatistics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatistics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: main_models.DescribeInstanceStatisticsRequest,
    ) -> main_models.DescribeInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instance_status_with_options(
        self,
        request: main_models.DescribeInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_status_with_options_async(
        self,
        request: main_models.DescribeInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_status(
        self,
        request: main_models.DescribeInstanceStatusRequest,
    ) -> main_models.DescribeInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    async def describe_instance_status_async(
        self,
        request: main_models.DescribeInstanceStatusRequest,
    ) -> main_models.DescribeInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_status_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not DaraCore.is_null(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not DaraCore.is_null(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_l7global_rule_with_options(
        self,
        request: main_models.DescribeL7GlobalRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7GlobalRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7GlobalRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7GlobalRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l7global_rule_with_options_async(
        self,
        request: main_models.DescribeL7GlobalRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7GlobalRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7GlobalRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7GlobalRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l7global_rule(
        self,
        request: main_models.DescribeL7GlobalRuleRequest,
    ) -> main_models.DescribeL7GlobalRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_l7global_rule_with_options(request, runtime)

    async def describe_l7global_rule_async(
        self,
        request: main_models.DescribeL7GlobalRuleRequest,
    ) -> main_models.DescribeL7GlobalRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_l7global_rule_with_options_async(request, runtime)

    def describe_l7rs_policy_with_options(
        self,
        request: main_models.DescribeL7RsPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7RsPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7RsPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l7rs_policy_with_options_async(
        self,
        request: main_models.DescribeL7RsPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7RsPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7RsPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7RsPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l7rs_policy(
        self,
        request: main_models.DescribeL7RsPolicyRequest,
    ) -> main_models.DescribeL7RsPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_l7rs_policy_with_options(request, runtime)

    async def describe_l7rs_policy_async(
        self,
        request: main_models.DescribeL7RsPolicyRequest,
    ) -> main_models.DescribeL7RsPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_l7rs_policy_with_options_async(request, runtime)

    def describe_l7us_keepalive_with_options(
        self,
        request: main_models.DescribeL7UsKeepaliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7UsKeepaliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7UsKeepalive',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7UsKeepaliveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l7us_keepalive_with_options_async(
        self,
        request: main_models.DescribeL7UsKeepaliveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeL7UsKeepaliveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeL7UsKeepalive',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeL7UsKeepaliveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l7us_keepalive(
        self,
        request: main_models.DescribeL7UsKeepaliveRequest,
    ) -> main_models.DescribeL7UsKeepaliveResponse:
        runtime = RuntimeOptions()
        return self.describe_l7us_keepalive_with_options(request, runtime)

    async def describe_l7us_keepalive_async(
        self,
        request: main_models.DescribeL7UsKeepaliveRequest,
    ) -> main_models.DescribeL7UsKeepaliveResponse:
        runtime = RuntimeOptions()
        return await self.describe_l7us_keepalive_with_options_async(request, runtime)

    def describe_layer_4rule_policy_with_options(
        self,
        request: main_models.DescribeLayer4RulePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RulePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4RulePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_layer_4rule_policy_with_options_async(
        self,
        request: main_models.DescribeLayer4RulePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLayer4RulePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLayer4RulePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLayer4RulePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_layer_4rule_policy(
        self,
        request: main_models.DescribeLayer4RulePolicyRequest,
    ) -> main_models.DescribeLayer4RulePolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_layer_4rule_policy_with_options(request, runtime)

    async def describe_layer_4rule_policy_async(
        self,
        request: main_models.DescribeLayer4RulePolicyRequest,
    ) -> main_models.DescribeLayer4RulePolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_layer_4rule_policy_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreExistStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreExistStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreExistStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreExistStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_exist_status(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: main_models.DescribeLogStoreExistStatusRequest,
    ) -> main_models.DescribeLogStoreExistStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_network_region_block_with_options(
        self,
        request: main_models.DescribeNetworkRegionBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRegionBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRegionBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_region_block_with_options_async(
        self,
        request: main_models.DescribeNetworkRegionBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRegionBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRegionBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRegionBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_region_block(
        self,
        request: main_models.DescribeNetworkRegionBlockRequest,
    ) -> main_models.DescribeNetworkRegionBlockResponse:
        runtime = RuntimeOptions()
        return self.describe_network_region_block_with_options(request, runtime)

    async def describe_network_region_block_async(
        self,
        request: main_models.DescribeNetworkRegionBlockRequest,
    ) -> main_models.DescribeNetworkRegionBlockResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_region_block_with_options_async(request, runtime)

    def describe_network_rule_attributes_with_options(
        self,
        request: main_models.DescribeNetworkRuleAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRuleAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRuleAttributes',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRuleAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rule_attributes_with_options_async(
        self,
        request: main_models.DescribeNetworkRuleAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRuleAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRuleAttributes',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRuleAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_rule_attributes(
        self,
        request: main_models.DescribeNetworkRuleAttributesRequest,
    ) -> main_models.DescribeNetworkRuleAttributesResponse:
        runtime = RuntimeOptions()
        return self.describe_network_rule_attributes_with_options(request, runtime)

    async def describe_network_rule_attributes_async(
        self,
        request: main_models.DescribeNetworkRuleAttributesRequest,
    ) -> main_models.DescribeNetworkRuleAttributesResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_rule_attributes_with_options_async(request, runtime)

    def describe_network_rules_with_options(
        self,
        request: main_models.DescribeNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_rules_with_options_async(
        self,
        request: main_models.DescribeNetworkRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_rules(
        self,
        request: main_models.DescribeNetworkRulesRequest,
    ) -> main_models.DescribeNetworkRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_network_rules_with_options(request, runtime)

    async def describe_network_rules_async(
        self,
        request: main_models.DescribeNetworkRulesRequest,
    ) -> main_models.DescribeNetworkRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_rules_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: main_models.DescribeOpEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: main_models.DescribeOpEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpEntities',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_op_entities(
        self,
        request: main_models.DescribeOpEntitiesRequest,
    ) -> main_models.DescribeOpEntitiesResponse:
        runtime = RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: main_models.DescribeOpEntitiesRequest,
    ) -> main_models.DescribeOpEntitiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_port_with_options(
        self,
        request: main_models.DescribePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_with_options_async(
        self,
        request: main_models.DescribePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port(
        self,
        request: main_models.DescribePortRequest,
    ) -> main_models.DescribePortResponse:
        runtime = RuntimeOptions()
        return self.describe_port_with_options(request, runtime)

    async def describe_port_async(
        self,
        request: main_models.DescribePortRequest,
    ) -> main_models.DescribePortResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_with_options_async(request, runtime)

    def describe_port_attack_max_flow_with_options(
        self,
        request: main_models.DescribePortAttackMaxFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortAttackMaxFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortAttackMaxFlow',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortAttackMaxFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_attack_max_flow_with_options_async(
        self,
        request: main_models.DescribePortAttackMaxFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortAttackMaxFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortAttackMaxFlow',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortAttackMaxFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_attack_max_flow(
        self,
        request: main_models.DescribePortAttackMaxFlowRequest,
    ) -> main_models.DescribePortAttackMaxFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_port_attack_max_flow_with_options(request, runtime)

    async def describe_port_attack_max_flow_async(
        self,
        request: main_models.DescribePortAttackMaxFlowRequest,
    ) -> main_models.DescribePortAttackMaxFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_attack_max_flow_with_options_async(request, runtime)

    def describe_port_auto_cc_status_with_options(
        self,
        request: main_models.DescribePortAutoCcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortAutoCcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortAutoCcStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_auto_cc_status_with_options_async(
        self,
        request: main_models.DescribePortAutoCcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortAutoCcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortAutoCcStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortAutoCcStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_auto_cc_status(
        self,
        request: main_models.DescribePortAutoCcStatusRequest,
    ) -> main_models.DescribePortAutoCcStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_port_auto_cc_status_with_options(request, runtime)

    async def describe_port_auto_cc_status_async(
        self,
        request: main_models.DescribePortAutoCcStatusRequest,
    ) -> main_models.DescribePortAutoCcStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_auto_cc_status_with_options_async(request, runtime)

    def describe_port_cc_attack_top_ipwith_options(
        self,
        request: main_models.DescribePortCcAttackTopIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortCcAttackTopIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortCcAttackTopIP',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortCcAttackTopIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_cc_attack_top_ipwith_options_async(
        self,
        request: main_models.DescribePortCcAttackTopIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortCcAttackTopIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortCcAttackTopIP',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortCcAttackTopIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_cc_attack_top_ip(
        self,
        request: main_models.DescribePortCcAttackTopIPRequest,
    ) -> main_models.DescribePortCcAttackTopIPResponse:
        runtime = RuntimeOptions()
        return self.describe_port_cc_attack_top_ipwith_options(request, runtime)

    async def describe_port_cc_attack_top_ip_async(
        self,
        request: main_models.DescribePortCcAttackTopIPRequest,
    ) -> main_models.DescribePortCcAttackTopIPResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_cc_attack_top_ipwith_options_async(request, runtime)

    def describe_port_conns_count_with_options(
        self,
        request: main_models.DescribePortConnsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortConnsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortConnsCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortConnsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_conns_count_with_options_async(
        self,
        request: main_models.DescribePortConnsCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortConnsCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortConnsCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortConnsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_conns_count(
        self,
        request: main_models.DescribePortConnsCountRequest,
    ) -> main_models.DescribePortConnsCountResponse:
        runtime = RuntimeOptions()
        return self.describe_port_conns_count_with_options(request, runtime)

    async def describe_port_conns_count_async(
        self,
        request: main_models.DescribePortConnsCountRequest,
    ) -> main_models.DescribePortConnsCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_conns_count_with_options_async(request, runtime)

    def describe_port_conns_list_with_options(
        self,
        request: main_models.DescribePortConnsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortConnsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortConnsList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortConnsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_conns_list_with_options_async(
        self,
        request: main_models.DescribePortConnsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortConnsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortConnsList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortConnsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_conns_list(
        self,
        request: main_models.DescribePortConnsListRequest,
    ) -> main_models.DescribePortConnsListResponse:
        runtime = RuntimeOptions()
        return self.describe_port_conns_list_with_options(request, runtime)

    async def describe_port_conns_list_async(
        self,
        request: main_models.DescribePortConnsListRequest,
    ) -> main_models.DescribePortConnsListResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_conns_list_with_options_async(request, runtime)

    def describe_port_flow_list_with_options(
        self,
        request: main_models.DescribePortFlowListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortFlowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortFlowList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_flow_list_with_options_async(
        self,
        request: main_models.DescribePortFlowListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortFlowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortFlowList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortFlowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_flow_list(
        self,
        request: main_models.DescribePortFlowListRequest,
    ) -> main_models.DescribePortFlowListResponse:
        runtime = RuntimeOptions()
        return self.describe_port_flow_list_with_options(request, runtime)

    async def describe_port_flow_list_async(
        self,
        request: main_models.DescribePortFlowListRequest,
    ) -> main_models.DescribePortFlowListResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_flow_list_with_options_async(request, runtime)

    def describe_port_max_conns_with_options(
        self,
        request: main_models.DescribePortMaxConnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortMaxConnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortMaxConns',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortMaxConnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_max_conns_with_options_async(
        self,
        request: main_models.DescribePortMaxConnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortMaxConnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortMaxConns',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortMaxConnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_max_conns(
        self,
        request: main_models.DescribePortMaxConnsRequest,
    ) -> main_models.DescribePortMaxConnsResponse:
        runtime = RuntimeOptions()
        return self.describe_port_max_conns_with_options(request, runtime)

    async def describe_port_max_conns_async(
        self,
        request: main_models.DescribePortMaxConnsRequest,
    ) -> main_models.DescribePortMaxConnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_max_conns_with_options_async(request, runtime)

    def describe_port_view_source_countries_with_options(
        self,
        request: main_models.DescribePortViewSourceCountriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceCountriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceCountries',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_countries_with_options_async(
        self,
        request: main_models.DescribePortViewSourceCountriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceCountriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceCountries',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceCountriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_view_source_countries(
        self,
        request: main_models.DescribePortViewSourceCountriesRequest,
    ) -> main_models.DescribePortViewSourceCountriesResponse:
        runtime = RuntimeOptions()
        return self.describe_port_view_source_countries_with_options(request, runtime)

    async def describe_port_view_source_countries_async(
        self,
        request: main_models.DescribePortViewSourceCountriesRequest,
    ) -> main_models.DescribePortViewSourceCountriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_view_source_countries_with_options_async(request, runtime)

    def describe_port_view_source_isps_with_options(
        self,
        request: main_models.DescribePortViewSourceIspsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceIspsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceIsps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceIspsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_isps_with_options_async(
        self,
        request: main_models.DescribePortViewSourceIspsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceIspsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceIsps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceIspsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_view_source_isps(
        self,
        request: main_models.DescribePortViewSourceIspsRequest,
    ) -> main_models.DescribePortViewSourceIspsResponse:
        runtime = RuntimeOptions()
        return self.describe_port_view_source_isps_with_options(request, runtime)

    async def describe_port_view_source_isps_async(
        self,
        request: main_models.DescribePortViewSourceIspsRequest,
    ) -> main_models.DescribePortViewSourceIspsResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_view_source_isps_with_options_async(request, runtime)

    def describe_port_view_source_provinces_with_options(
        self,
        request: main_models.DescribePortViewSourceProvincesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceProvincesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceProvinces',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_view_source_provinces_with_options_async(
        self,
        request: main_models.DescribePortViewSourceProvincesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePortViewSourceProvincesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePortViewSourceProvinces',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePortViewSourceProvincesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_view_source_provinces(
        self,
        request: main_models.DescribePortViewSourceProvincesRequest,
    ) -> main_models.DescribePortViewSourceProvincesResponse:
        runtime = RuntimeOptions()
        return self.describe_port_view_source_provinces_with_options(request, runtime)

    async def describe_port_view_source_provinces_async(
        self,
        request: main_models.DescribePortViewSourceProvincesRequest,
    ) -> main_models.DescribePortViewSourceProvincesResponse:
        runtime = RuntimeOptions()
        return await self.describe_port_view_source_provinces_with_options_async(request, runtime)

    def describe_scene_defense_objects_with_options(
        self,
        request: main_models.DescribeSceneDefenseObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneDefenseObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneDefenseObjects',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneDefenseObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_defense_objects_with_options_async(
        self,
        request: main_models.DescribeSceneDefenseObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneDefenseObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneDefenseObjects',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneDefenseObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_defense_objects(
        self,
        request: main_models.DescribeSceneDefenseObjectsRequest,
    ) -> main_models.DescribeSceneDefenseObjectsResponse:
        runtime = RuntimeOptions()
        return self.describe_scene_defense_objects_with_options(request, runtime)

    async def describe_scene_defense_objects_async(
        self,
        request: main_models.DescribeSceneDefenseObjectsRequest,
    ) -> main_models.DescribeSceneDefenseObjectsResponse:
        runtime = RuntimeOptions()
        return await self.describe_scene_defense_objects_with_options_async(request, runtime)

    def describe_scene_defense_policies_with_options(
        self,
        request: main_models.DescribeSceneDefensePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneDefensePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneDefensePolicies',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneDefensePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_defense_policies_with_options_async(
        self,
        request: main_models.DescribeSceneDefensePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSceneDefensePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSceneDefensePolicies',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSceneDefensePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_defense_policies(
        self,
        request: main_models.DescribeSceneDefensePoliciesRequest,
    ) -> main_models.DescribeSceneDefensePoliciesResponse:
        runtime = RuntimeOptions()
        return self.describe_scene_defense_policies_with_options(request, runtime)

    async def describe_scene_defense_policies_async(
        self,
        request: main_models.DescribeSceneDefensePoliciesRequest,
    ) -> main_models.DescribeSceneDefensePoliciesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scene_defense_policies_with_options_async(request, runtime)

    def describe_scheduler_rules_with_options(
        self,
        request: main_models.DescribeSchedulerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchedulerRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchedulerRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchedulerRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduler_rules_with_options_async(
        self,
        request: main_models.DescribeSchedulerRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchedulerRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchedulerRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchedulerRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduler_rules(
        self,
        request: main_models.DescribeSchedulerRulesRequest,
    ) -> main_models.DescribeSchedulerRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_scheduler_rules_with_options(request, runtime)

    async def describe_scheduler_rules_async(
        self,
        request: main_models.DescribeSchedulerRulesRequest,
    ) -> main_models.DescribeSchedulerRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_scheduler_rules_with_options_async(request, runtime)

    def describe_sla_event_list_with_options(
        self,
        request: main_models.DescribeSlaEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlaEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlaEventList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlaEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sla_event_list_with_options_async(
        self,
        request: main_models.DescribeSlaEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlaEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlaEventList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlaEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sla_event_list(
        self,
        request: main_models.DescribeSlaEventListRequest,
    ) -> main_models.DescribeSlaEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_sla_event_list_with_options(request, runtime)

    async def describe_sla_event_list_async(
        self,
        request: main_models.DescribeSlaEventListRequest,
    ) -> main_models.DescribeSlaEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sla_event_list_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogstoreInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogstoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogstoreInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogstoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_logstore_info(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: main_models.DescribeSlsLogstoreInfoRequest,
    ) -> main_models.DescribeSlsLogstoreInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsOpenStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsOpenStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_open_status(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: main_models.DescribeSlsOpenStatusRequest,
    ) -> main_models.DescribeSlsOpenStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describe_sts_grant_status_with_options(
        self,
        request: main_models.DescribeStsGrantStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStsGrantStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStsGrantStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStsGrantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sts_grant_status_with_options_async(
        self,
        request: main_models.DescribeStsGrantStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStsGrantStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStsGrantStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStsGrantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sts_grant_status(
        self,
        request: main_models.DescribeStsGrantStatusRequest,
    ) -> main_models.DescribeStsGrantStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sts_grant_status_with_options(request, runtime)

    async def describe_sts_grant_status_async(
        self,
        request: main_models.DescribeStsGrantStatusRequest,
    ) -> main_models.DescribeStsGrantStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sts_grant_status_with_options_async(request, runtime)

    def describe_system_log_with_options(
        self,
        request: main_models.DescribeSystemLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemLog',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_log_with_options_async(
        self,
        request: main_models.DescribeSystemLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemLog',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_log(
        self,
        request: main_models.DescribeSystemLogRequest,
    ) -> main_models.DescribeSystemLogResponse:
        runtime = RuntimeOptions()
        return self.describe_system_log_with_options(request, runtime)

    async def describe_system_log_async(
        self,
        request: main_models.DescribeSystemLogRequest,
    ) -> main_models.DescribeSystemLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_log_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: main_models.DescribeTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeys',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_keys_with_options_async(
        self,
        request: main_models.DescribeTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeys',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_keys(
        self,
        request: main_models.DescribeTagKeysRequest,
    ) -> main_models.DescribeTagKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: main_models.DescribeTagKeysRequest,
    ) -> main_models.DescribeTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_resources_with_options(
        self,
        request: main_models.DescribeTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: main_models.DescribeTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagResources',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_resources(
        self,
        request: main_models.DescribeTagResourcesRequest,
    ) -> main_models.DescribeTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: main_models.DescribeTagResourcesRequest,
    ) -> main_models.DescribeTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_total_attack_max_flow_with_options(
        self,
        request: main_models.DescribeTotalAttackMaxFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTotalAttackMaxFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTotalAttackMaxFlow',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTotalAttackMaxFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_total_attack_max_flow_with_options_async(
        self,
        request: main_models.DescribeTotalAttackMaxFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTotalAttackMaxFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTotalAttackMaxFlow',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTotalAttackMaxFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_total_attack_max_flow(
        self,
        request: main_models.DescribeTotalAttackMaxFlowRequest,
    ) -> main_models.DescribeTotalAttackMaxFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_total_attack_max_flow_with_options(request, runtime)

    async def describe_total_attack_max_flow_async(
        self,
        request: main_models.DescribeTotalAttackMaxFlowRequest,
    ) -> main_models.DescribeTotalAttackMaxFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_total_attack_max_flow_with_options_async(request, runtime)

    def describe_udp_reflect_with_options(
        self,
        request: main_models.DescribeUdpReflectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUdpReflectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUdpReflect',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_udp_reflect_with_options_async(
        self,
        request: main_models.DescribeUdpReflectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUdpReflectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUdpReflect',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUdpReflectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_udp_reflect(
        self,
        request: main_models.DescribeUdpReflectRequest,
    ) -> main_models.DescribeUdpReflectResponse:
        runtime = RuntimeOptions()
        return self.describe_udp_reflect_with_options(request, runtime)

    async def describe_udp_reflect_async(
        self,
        request: main_models.DescribeUdpReflectRequest,
    ) -> main_models.DescribeUdpReflectResponse:
        runtime = RuntimeOptions()
        return await self.describe_udp_reflect_with_options_async(request, runtime)

    def describe_un_blackhole_count_with_options(
        self,
        request: main_models.DescribeUnBlackholeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnBlackholeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnBlackholeCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnBlackholeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_un_blackhole_count_with_options_async(
        self,
        request: main_models.DescribeUnBlackholeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnBlackholeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnBlackholeCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnBlackholeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_un_blackhole_count(
        self,
        request: main_models.DescribeUnBlackholeCountRequest,
    ) -> main_models.DescribeUnBlackholeCountResponse:
        runtime = RuntimeOptions()
        return self.describe_un_blackhole_count_with_options(request, runtime)

    async def describe_un_blackhole_count_async(
        self,
        request: main_models.DescribeUnBlackholeCountRequest,
    ) -> main_models.DescribeUnBlackholeCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_un_blackhole_count_with_options_async(request, runtime)

    def describe_un_block_count_with_options(
        self,
        request: main_models.DescribeUnBlockCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnBlockCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnBlockCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnBlockCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_un_block_count_with_options_async(
        self,
        request: main_models.DescribeUnBlockCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnBlockCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnBlockCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnBlockCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_un_block_count(
        self,
        request: main_models.DescribeUnBlockCountRequest,
    ) -> main_models.DescribeUnBlockCountResponse:
        runtime = RuntimeOptions()
        return self.describe_un_block_count_with_options(request, runtime)

    async def describe_un_block_count_async(
        self,
        request: main_models.DescribeUnBlockCountRequest,
    ) -> main_models.DescribeUnBlockCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_un_block_count_with_options_async(request, runtime)

    def describe_web_access_log_dispatch_status_with_options(
        self,
        request: main_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogDispatchStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_dispatch_status_with_options_async(
        self,
        request: main_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogDispatchStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogDispatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_access_log_dispatch_status(
        self,
        request: main_models.DescribeWebAccessLogDispatchStatusRequest,
    ) -> main_models.DescribeWebAccessLogDispatchStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_web_access_log_dispatch_status_with_options(request, runtime)

    async def describe_web_access_log_dispatch_status_async(
        self,
        request: main_models.DescribeWebAccessLogDispatchStatusRequest,
    ) -> main_models.DescribeWebAccessLogDispatchStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_access_log_dispatch_status_with_options_async(request, runtime)

    def describe_web_access_log_empty_count_with_options(
        self,
        request: main_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogEmptyCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogEmptyCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogEmptyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_empty_count_with_options_async(
        self,
        request: main_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogEmptyCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogEmptyCount',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogEmptyCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_access_log_empty_count(
        self,
        request: main_models.DescribeWebAccessLogEmptyCountRequest,
    ) -> main_models.DescribeWebAccessLogEmptyCountResponse:
        runtime = RuntimeOptions()
        return self.describe_web_access_log_empty_count_with_options(request, runtime)

    async def describe_web_access_log_empty_count_async(
        self,
        request: main_models.DescribeWebAccessLogEmptyCountRequest,
    ) -> main_models.DescribeWebAccessLogEmptyCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_access_log_empty_count_with_options_async(request, runtime)

    def describe_web_access_log_status_with_options(
        self,
        request: main_models.DescribeWebAccessLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_log_status_with_options_async(
        self,
        request: main_models.DescribeWebAccessLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessLogStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_access_log_status(
        self,
        request: main_models.DescribeWebAccessLogStatusRequest,
    ) -> main_models.DescribeWebAccessLogStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_web_access_log_status_with_options(request, runtime)

    async def describe_web_access_log_status_async(
        self,
        request: main_models.DescribeWebAccessLogStatusRequest,
    ) -> main_models.DescribeWebAccessLogStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_access_log_status_with_options_async(request, runtime)

    def describe_web_access_mode_with_options(
        self,
        request: main_models.DescribeWebAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_access_mode_with_options_async(
        self,
        request: main_models.DescribeWebAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAccessMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_access_mode(
        self,
        request: main_models.DescribeWebAccessModeRequest,
    ) -> main_models.DescribeWebAccessModeResponse:
        runtime = RuntimeOptions()
        return self.describe_web_access_mode_with_options(request, runtime)

    async def describe_web_access_mode_async(
        self,
        request: main_models.DescribeWebAccessModeRequest,
    ) -> main_models.DescribeWebAccessModeResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_access_mode_with_options_async(request, runtime)

    def describe_web_area_block_configs_with_options(
        self,
        request: main_models.DescribeWebAreaBlockConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAreaBlockConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAreaBlockConfigs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAreaBlockConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_area_block_configs_with_options_async(
        self,
        request: main_models.DescribeWebAreaBlockConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebAreaBlockConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebAreaBlockConfigs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebAreaBlockConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_area_block_configs(
        self,
        request: main_models.DescribeWebAreaBlockConfigsRequest,
    ) -> main_models.DescribeWebAreaBlockConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_web_area_block_configs_with_options(request, runtime)

    async def describe_web_area_block_configs_async(
        self,
        request: main_models.DescribeWebAreaBlockConfigsRequest,
    ) -> main_models.DescribeWebAreaBlockConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_area_block_configs_with_options_async(request, runtime)

    def describe_web_ccrules_with_options(
        self,
        request: main_models.DescribeWebCCRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCCRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCCRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCCRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_ccrules_with_options_async(
        self,
        request: main_models.DescribeWebCCRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCCRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCCRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCCRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_ccrules(
        self,
        request: main_models.DescribeWebCCRulesRequest,
    ) -> main_models.DescribeWebCCRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_web_ccrules_with_options(request, runtime)

    async def describe_web_ccrules_async(
        self,
        request: main_models.DescribeWebCCRulesRequest,
    ) -> main_models.DescribeWebCCRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_ccrules_with_options_async(request, runtime)

    def describe_web_ccrules_v2with_options(
        self,
        request: main_models.DescribeWebCCRulesV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCCRulesV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCCRulesV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCCRulesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_ccrules_v2with_options_async(
        self,
        request: main_models.DescribeWebCCRulesV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCCRulesV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCCRulesV2',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCCRulesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_ccrules_v2(
        self,
        request: main_models.DescribeWebCCRulesV2Request,
    ) -> main_models.DescribeWebCCRulesV2Response:
        runtime = RuntimeOptions()
        return self.describe_web_ccrules_v2with_options(request, runtime)

    async def describe_web_ccrules_v2_async(
        self,
        request: main_models.DescribeWebCCRulesV2Request,
    ) -> main_models.DescribeWebCCRulesV2Response:
        runtime = RuntimeOptions()
        return await self.describe_web_ccrules_v2with_options_async(request, runtime)

    def describe_web_cache_configs_with_options(
        self,
        request: main_models.DescribeWebCacheConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCacheConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCacheConfigs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCacheConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_cache_configs_with_options_async(
        self,
        request: main_models.DescribeWebCacheConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCacheConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCacheConfigs',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCacheConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_cache_configs(
        self,
        request: main_models.DescribeWebCacheConfigsRequest,
    ) -> main_models.DescribeWebCacheConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_web_cache_configs_with_options(request, runtime)

    async def describe_web_cache_configs_async(
        self,
        request: main_models.DescribeWebCacheConfigsRequest,
    ) -> main_models.DescribeWebCacheConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_cache_configs_with_options_async(request, runtime)

    def describe_web_cc_protect_switch_with_options(
        self,
        request: main_models.DescribeWebCcProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCcProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCcProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCcProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_cc_protect_switch_with_options_async(
        self,
        request: main_models.DescribeWebCcProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCcProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCcProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCcProtectSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_cc_protect_switch(
        self,
        request: main_models.DescribeWebCcProtectSwitchRequest,
    ) -> main_models.DescribeWebCcProtectSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_web_cc_protect_switch_with_options(request, runtime)

    async def describe_web_cc_protect_switch_async(
        self,
        request: main_models.DescribeWebCcProtectSwitchRequest,
    ) -> main_models.DescribeWebCcProtectSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_cc_protect_switch_with_options_async(request, runtime)

    def describe_web_custom_ports_with_options(
        self,
        request: main_models.DescribeWebCustomPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCustomPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCustomPorts',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCustomPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_custom_ports_with_options_async(
        self,
        request: main_models.DescribeWebCustomPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCustomPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCustomPorts',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCustomPortsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_custom_ports(
        self,
        request: main_models.DescribeWebCustomPortsRequest,
    ) -> main_models.DescribeWebCustomPortsResponse:
        runtime = RuntimeOptions()
        return self.describe_web_custom_ports_with_options(request, runtime)

    async def describe_web_custom_ports_async(
        self,
        request: main_models.DescribeWebCustomPortsRequest,
    ) -> main_models.DescribeWebCustomPortsResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_custom_ports_with_options_async(request, runtime)

    def describe_web_instance_relations_with_options(
        self,
        request: main_models.DescribeWebInstanceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebInstanceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebInstanceRelations',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebInstanceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_instance_relations_with_options_async(
        self,
        request: main_models.DescribeWebInstanceRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebInstanceRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebInstanceRelations',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebInstanceRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_instance_relations(
        self,
        request: main_models.DescribeWebInstanceRelationsRequest,
    ) -> main_models.DescribeWebInstanceRelationsResponse:
        runtime = RuntimeOptions()
        return self.describe_web_instance_relations_with_options(request, runtime)

    async def describe_web_instance_relations_async(
        self,
        request: main_models.DescribeWebInstanceRelationsRequest,
    ) -> main_models.DescribeWebInstanceRelationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_instance_relations_with_options_async(request, runtime)

    def describe_web_precise_access_rule_with_options(
        self,
        request: main_models.DescribeWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_precise_access_rule_with_options_async(
        self,
        request: main_models.DescribeWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_precise_access_rule(
        self,
        request: main_models.DescribeWebPreciseAccessRuleRequest,
    ) -> main_models.DescribeWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_web_precise_access_rule_with_options(request, runtime)

    async def describe_web_precise_access_rule_async(
        self,
        request: main_models.DescribeWebPreciseAccessRuleRequest,
    ) -> main_models.DescribeWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_precise_access_rule_with_options_async(request, runtime)

    def describe_web_report_top_ip_with_options(
        self,
        request: main_models.DescribeWebReportTopIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebReportTopIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebReportTopIp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebReportTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_report_top_ip_with_options_async(
        self,
        request: main_models.DescribeWebReportTopIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebReportTopIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebReportTopIp',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebReportTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_report_top_ip(
        self,
        request: main_models.DescribeWebReportTopIpRequest,
    ) -> main_models.DescribeWebReportTopIpResponse:
        runtime = RuntimeOptions()
        return self.describe_web_report_top_ip_with_options(request, runtime)

    async def describe_web_report_top_ip_async(
        self,
        request: main_models.DescribeWebReportTopIpRequest,
    ) -> main_models.DescribeWebReportTopIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_report_top_ip_with_options_async(request, runtime)

    def describe_web_rules_with_options(
        self,
        request: main_models.DescribeWebRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname):
            query['Cname'] = request.cname
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_rules_with_options_async(
        self,
        request: main_models.DescribeWebRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname):
            query['Cname'] = request.cname
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebRules',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_rules(
        self,
        request: main_models.DescribeWebRulesRequest,
    ) -> main_models.DescribeWebRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_web_rules_with_options(request, runtime)

    async def describe_web_rules_async(
        self,
        request: main_models.DescribeWebRulesRequest,
    ) -> main_models.DescribeWebRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_web_rules_with_options_async(request, runtime)

    def detach_scene_defense_object_with_options(
        self,
        request: main_models.DetachSceneDefenseObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSceneDefenseObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.objects):
            query['Objects'] = request.objects
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSceneDefenseObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_scene_defense_object_with_options_async(
        self,
        request: main_models.DetachSceneDefenseObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSceneDefenseObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.objects):
            query['Objects'] = request.objects
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSceneDefenseObject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSceneDefenseObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_scene_defense_object(
        self,
        request: main_models.DetachSceneDefenseObjectRequest,
    ) -> main_models.DetachSceneDefenseObjectResponse:
        runtime = RuntimeOptions()
        return self.detach_scene_defense_object_with_options(request, runtime)

    async def detach_scene_defense_object_async(
        self,
        request: main_models.DetachSceneDefenseObjectRequest,
    ) -> main_models.DetachSceneDefenseObjectResponse:
        runtime = RuntimeOptions()
        return await self.detach_scene_defense_object_with_options_async(request, runtime)

    def disable_scene_defense_policy_with_options(
        self,
        request: main_models.DisableSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scene_defense_policy_with_options_async(
        self,
        request: main_models.DisableSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_scene_defense_policy(
        self,
        request: main_models.DisableSceneDefensePolicyRequest,
    ) -> main_models.DisableSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return self.disable_scene_defense_policy_with_options(request, runtime)

    async def disable_scene_defense_policy_async(
        self,
        request: main_models.DisableSceneDefensePolicyRequest,
    ) -> main_models.DisableSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return await self.disable_scene_defense_policy_with_options_async(request, runtime)

    def disable_web_access_log_config_with_options(
        self,
        request: main_models.DisableWebAccessLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebAccessLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebAccessLogConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_access_log_config_with_options_async(
        self,
        request: main_models.DisableWebAccessLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebAccessLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebAccessLogConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebAccessLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_web_access_log_config(
        self,
        request: main_models.DisableWebAccessLogConfigRequest,
    ) -> main_models.DisableWebAccessLogConfigResponse:
        runtime = RuntimeOptions()
        return self.disable_web_access_log_config_with_options(request, runtime)

    async def disable_web_access_log_config_async(
        self,
        request: main_models.DisableWebAccessLogConfigRequest,
    ) -> main_models.DisableWebAccessLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.disable_web_access_log_config_with_options_async(request, runtime)

    def disable_web_ccwith_options(
        self,
        request: main_models.DisableWebCCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebCCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebCC',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_ccwith_options_async(
        self,
        request: main_models.DisableWebCCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebCCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebCC',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebCCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_web_cc(
        self,
        request: main_models.DisableWebCCRequest,
    ) -> main_models.DisableWebCCResponse:
        runtime = RuntimeOptions()
        return self.disable_web_ccwith_options(request, runtime)

    async def disable_web_cc_async(
        self,
        request: main_models.DisableWebCCRequest,
    ) -> main_models.DisableWebCCResponse:
        runtime = RuntimeOptions()
        return await self.disable_web_ccwith_options_async(request, runtime)

    def disable_web_ccrule_with_options(
        self,
        request: main_models.DisableWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_web_ccrule_with_options_async(
        self,
        request: main_models.DisableWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_web_ccrule(
        self,
        request: main_models.DisableWebCCRuleRequest,
    ) -> main_models.DisableWebCCRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_web_ccrule_with_options(request, runtime)

    async def disable_web_ccrule_async(
        self,
        request: main_models.DisableWebCCRuleRequest,
    ) -> main_models.DisableWebCCRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_web_ccrule_with_options_async(request, runtime)

    def empty_auto_cc_blacklist_with_options(
        self,
        request: main_models.EmptyAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptyAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptyAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptyAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_auto_cc_blacklist_with_options_async(
        self,
        request: main_models.EmptyAutoCcBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptyAutoCcBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptyAutoCcBlacklist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptyAutoCcBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def empty_auto_cc_blacklist(
        self,
        request: main_models.EmptyAutoCcBlacklistRequest,
    ) -> main_models.EmptyAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return self.empty_auto_cc_blacklist_with_options(request, runtime)

    async def empty_auto_cc_blacklist_async(
        self,
        request: main_models.EmptyAutoCcBlacklistRequest,
    ) -> main_models.EmptyAutoCcBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.empty_auto_cc_blacklist_with_options_async(request, runtime)

    def empty_auto_cc_whitelist_with_options(
        self,
        request: main_models.EmptyAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptyAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptyAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptyAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_auto_cc_whitelist_with_options_async(
        self,
        request: main_models.EmptyAutoCcWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptyAutoCcWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptyAutoCcWhitelist',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptyAutoCcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def empty_auto_cc_whitelist(
        self,
        request: main_models.EmptyAutoCcWhitelistRequest,
    ) -> main_models.EmptyAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return self.empty_auto_cc_whitelist_with_options(request, runtime)

    async def empty_auto_cc_whitelist_async(
        self,
        request: main_models.EmptyAutoCcWhitelistRequest,
    ) -> main_models.EmptyAutoCcWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.empty_auto_cc_whitelist_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: main_models.EmptySlsLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptySlsLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptySlsLogstore',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptySlsLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: main_models.EmptySlsLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmptySlsLogstoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmptySlsLogstore',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmptySlsLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def empty_sls_logstore(
        self,
        request: main_models.EmptySlsLogstoreRequest,
    ) -> main_models.EmptySlsLogstoreResponse:
        runtime = RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: main_models.EmptySlsLogstoreRequest,
    ) -> main_models.EmptySlsLogstoreResponse:
        runtime = RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_scene_defense_policy_with_options(
        self,
        request: main_models.EnableSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scene_defense_policy_with_options_async(
        self,
        request: main_models.EnableSceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_scene_defense_policy(
        self,
        request: main_models.EnableSceneDefensePolicyRequest,
    ) -> main_models.EnableSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return self.enable_scene_defense_policy_with_options(request, runtime)

    async def enable_scene_defense_policy_async(
        self,
        request: main_models.EnableSceneDefensePolicyRequest,
    ) -> main_models.EnableSceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return await self.enable_scene_defense_policy_with_options_async(request, runtime)

    def enable_web_access_log_config_with_options(
        self,
        request: main_models.EnableWebAccessLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebAccessLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebAccessLogConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_access_log_config_with_options_async(
        self,
        request: main_models.EnableWebAccessLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebAccessLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebAccessLogConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebAccessLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_web_access_log_config(
        self,
        request: main_models.EnableWebAccessLogConfigRequest,
    ) -> main_models.EnableWebAccessLogConfigResponse:
        runtime = RuntimeOptions()
        return self.enable_web_access_log_config_with_options(request, runtime)

    async def enable_web_access_log_config_async(
        self,
        request: main_models.EnableWebAccessLogConfigRequest,
    ) -> main_models.EnableWebAccessLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.enable_web_access_log_config_with_options_async(request, runtime)

    def enable_web_ccwith_options(
        self,
        request: main_models.EnableWebCCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebCCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebCC',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_ccwith_options_async(
        self,
        request: main_models.EnableWebCCRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebCCResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebCC',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebCCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_web_cc(
        self,
        request: main_models.EnableWebCCRequest,
    ) -> main_models.EnableWebCCResponse:
        runtime = RuntimeOptions()
        return self.enable_web_ccwith_options(request, runtime)

    async def enable_web_cc_async(
        self,
        request: main_models.EnableWebCCRequest,
    ) -> main_models.EnableWebCCResponse:
        runtime = RuntimeOptions()
        return await self.enable_web_ccwith_options_async(request, runtime)

    def enable_web_ccrule_with_options(
        self,
        request: main_models.EnableWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_web_ccrule_with_options_async(
        self,
        request: main_models.EnableWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_web_ccrule(
        self,
        request: main_models.EnableWebCCRuleRequest,
    ) -> main_models.EnableWebCCRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_web_ccrule_with_options(request, runtime)

    async def enable_web_ccrule_async(
        self,
        request: main_models.EnableWebCCRuleRequest,
    ) -> main_models.EnableWebCCRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_web_ccrule_with_options_async(request, runtime)

    def modify_biz_band_width_mode_with_options(
        self,
        request: main_models.ModifyBizBandWidthModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBizBandWidthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBizBandWidthMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBizBandWidthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_biz_band_width_mode_with_options_async(
        self,
        request: main_models.ModifyBizBandWidthModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBizBandWidthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBizBandWidthMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBizBandWidthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_biz_band_width_mode(
        self,
        request: main_models.ModifyBizBandWidthModeRequest,
    ) -> main_models.ModifyBizBandWidthModeResponse:
        runtime = RuntimeOptions()
        return self.modify_biz_band_width_mode_with_options(request, runtime)

    async def modify_biz_band_width_mode_async(
        self,
        request: main_models.ModifyBizBandWidthModeRequest,
    ) -> main_models.ModifyBizBandWidthModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_biz_band_width_mode_with_options_async(request, runtime)

    def modify_blackhole_status_with_options(
        self,
        request: main_models.ModifyBlackholeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlackholeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blackhole_status):
            query['BlackholeStatus'] = request.blackhole_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlackholeStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_blackhole_status_with_options_async(
        self,
        request: main_models.ModifyBlackholeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlackholeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.blackhole_status):
            query['BlackholeStatus'] = request.blackhole_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlackholeStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlackholeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_blackhole_status(
        self,
        request: main_models.ModifyBlackholeStatusRequest,
    ) -> main_models.ModifyBlackholeStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_blackhole_status_with_options(request, runtime)

    async def modify_blackhole_status_async(
        self,
        request: main_models.ModifyBlackholeStatusRequest,
    ) -> main_models.ModifyBlackholeStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_blackhole_status_with_options_async(request, runtime)

    def modify_block_status_with_options(
        self,
        request: main_models.ModifyBlockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlockStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlockStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_block_status_with_options_async(
        self,
        request: main_models.ModifyBlockStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBlockStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lines):
            query['Lines'] = request.lines
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBlockStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBlockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_block_status(
        self,
        request: main_models.ModifyBlockStatusRequest,
    ) -> main_models.ModifyBlockStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_block_status_with_options(request, runtime)

    async def modify_block_status_async(
        self,
        request: main_models.ModifyBlockStatusRequest,
    ) -> main_models.ModifyBlockStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_block_status_with_options_async(request, runtime)

    def modify_cname_reuse_with_options(
        self,
        request: main_models.ModifyCnameReuseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCnameReuseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname):
            query['Cname'] = request.cname
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCnameReuse',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCnameReuseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cname_reuse_with_options_async(
        self,
        request: main_models.ModifyCnameReuseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCnameReuseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cname):
            query['Cname'] = request.cname
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCnameReuse',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCnameReuseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cname_reuse(
        self,
        request: main_models.ModifyCnameReuseRequest,
    ) -> main_models.ModifyCnameReuseResponse:
        runtime = RuntimeOptions()
        return self.modify_cname_reuse_with_options(request, runtime)

    async def modify_cname_reuse_async(
        self,
        request: main_models.ModifyCnameReuseRequest,
    ) -> main_models.ModifyCnameReuseResponse:
        runtime = RuntimeOptions()
        return await self.modify_cname_reuse_with_options_async(request, runtime)

    def modify_domain_resource_with_options(
        self,
        request: main_models.ModifyDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_resource_with_options_async(
        self,
        request: main_models.ModifyDomainResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_resource(
        self,
        request: main_models.ModifyDomainResourceRequest,
    ) -> main_models.ModifyDomainResourceResponse:
        runtime = RuntimeOptions()
        return self.modify_domain_resource_with_options(request, runtime)

    async def modify_domain_resource_async(
        self,
        request: main_models.ModifyDomainResourceRequest,
    ) -> main_models.ModifyDomainResourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_domain_resource_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBandWidth',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBandWidth',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBandWidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_band_width(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
    ) -> main_models.ModifyElasticBandWidthResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: main_models.ModifyElasticBandWidthRequest,
    ) -> main_models.ModifyElasticBandWidthResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_elastic_biz_band_width_with_options(
        self,
        request: main_models.ModifyElasticBizBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBizBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_biz_bandwidth):
            query['ElasticBizBandwidth'] = request.elastic_biz_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBizBandWidth',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBizBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_biz_band_width_with_options_async(
        self,
        request: main_models.ModifyElasticBizBandWidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBizBandWidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.elastic_biz_bandwidth):
            query['ElasticBizBandwidth'] = request.elastic_biz_bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBizBandWidth',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBizBandWidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_biz_band_width(
        self,
        request: main_models.ModifyElasticBizBandWidthRequest,
    ) -> main_models.ModifyElasticBizBandWidthResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_biz_band_width_with_options(request, runtime)

    async def modify_elastic_biz_band_width_async(
        self,
        request: main_models.ModifyElasticBizBandWidthRequest,
    ) -> main_models.ModifyElasticBizBandWidthResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_biz_band_width_with_options_async(request, runtime)

    def modify_elastic_biz_qps_with_options(
        self,
        request: main_models.ModifyElasticBizQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBizQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ops_elastic_qps):
            query['OpsElasticQps'] = request.ops_elastic_qps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBizQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBizQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_biz_qps_with_options_async(
        self,
        request: main_models.ModifyElasticBizQpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticBizQpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ops_elastic_qps):
            query['OpsElasticQps'] = request.ops_elastic_qps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticBizQps',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticBizQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_biz_qps(
        self,
        request: main_models.ModifyElasticBizQpsRequest,
    ) -> main_models.ModifyElasticBizQpsResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_biz_qps_with_options(request, runtime)

    async def modify_elastic_biz_qps_async(
        self,
        request: main_models.ModifyElasticBizQpsRequest,
    ) -> main_models.ModifyElasticBizQpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_biz_qps_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: main_models.ModifyFullLogTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFullLogTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFullLogTtl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFullLogTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: main_models.ModifyFullLogTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFullLogTtlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFullLogTtl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFullLogTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_full_log_ttl(
        self,
        request: main_models.ModifyFullLogTtlRequest,
    ) -> main_models.ModifyFullLogTtlResponse:
        runtime = RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: main_models.ModifyFullLogTtlRequest,
    ) -> main_models.ModifyFullLogTtlResponse:
        runtime = RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_headers_with_options(
        self,
        request: main_models.ModifyHeadersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHeadersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHeaders',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_headers_with_options_async(
        self,
        request: main_models.ModifyHeadersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHeadersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHeaders',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHeadersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_headers(
        self,
        request: main_models.ModifyHeadersRequest,
    ) -> main_models.ModifyHeadersResponse:
        runtime = RuntimeOptions()
        return self.modify_headers_with_options(request, runtime)

    async def modify_headers_async(
        self,
        request: main_models.ModifyHeadersRequest,
    ) -> main_models.ModifyHeadersResponse:
        runtime = RuntimeOptions()
        return await self.modify_headers_with_options_async(request, runtime)

    def modify_health_check_config_with_options(
        self,
        request: main_models.ModifyHealthCheckConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHealthCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHealthCheckConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHealthCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_health_check_config_with_options_async(
        self,
        request: main_models.ModifyHealthCheckConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHealthCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHealthCheckConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHealthCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_health_check_config(
        self,
        request: main_models.ModifyHealthCheckConfigRequest,
    ) -> main_models.ModifyHealthCheckConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    async def modify_health_check_config_async(
        self,
        request: main_models.ModifyHealthCheckConfigRequest,
    ) -> main_models.ModifyHealthCheckConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_health_check_config_with_options_async(request, runtime)

    def modify_http_2enable_with_options(
        self,
        request: main_models.ModifyHttp2EnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHttp2EnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHttp2Enable',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHttp2EnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_http_2enable_with_options_async(
        self,
        request: main_models.ModifyHttp2EnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHttp2EnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHttp2Enable',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHttp2EnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_http_2enable(
        self,
        request: main_models.ModifyHttp2EnableRequest,
    ) -> main_models.ModifyHttp2EnableResponse:
        runtime = RuntimeOptions()
        return self.modify_http_2enable_with_options(request, runtime)

    async def modify_http_2enable_async(
        self,
        request: main_models.ModifyHttp2EnableRequest,
    ) -> main_models.ModifyHttp2EnableResponse:
        runtime = RuntimeOptions()
        return await self.modify_http_2enable_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.base_bandwidth):
            query['BaseBandwidth'] = request.base_bandwidth
        if not DaraCore.is_null(request.domain_count):
            query['DomainCount'] = request.domain_count
        if not DaraCore.is_null(request.edition_sale):
            query['EditionSale'] = request.edition_sale
        if not DaraCore.is_null(request.function_version):
            query['FunctionVersion'] = request.function_version
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.normal_bandwidth):
            query['NormalBandwidth'] = request.normal_bandwidth
        if not DaraCore.is_null(request.normal_qps):
            query['NormalQps'] = request.normal_qps
        if not DaraCore.is_null(request.port_count):
            query['PortCount'] = request.port_count
        if not DaraCore.is_null(request.product_plan):
            query['ProductPlan'] = request.product_plan
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.service_bandwidth):
            query['ServiceBandwidth'] = request.service_bandwidth
        if not DaraCore.is_null(request.service_partner):
            query['ServicePartner'] = request.service_partner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.base_bandwidth):
            query['BaseBandwidth'] = request.base_bandwidth
        if not DaraCore.is_null(request.domain_count):
            query['DomainCount'] = request.domain_count
        if not DaraCore.is_null(request.edition_sale):
            query['EditionSale'] = request.edition_sale
        if not DaraCore.is_null(request.function_version):
            query['FunctionVersion'] = request.function_version
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.normal_bandwidth):
            query['NormalBandwidth'] = request.normal_bandwidth
        if not DaraCore.is_null(request.normal_qps):
            query['NormalQps'] = request.normal_qps
        if not DaraCore.is_null(request.port_count):
            query['PortCount'] = request.port_count
        if not DaraCore.is_null(request.product_plan):
            query['ProductPlan'] = request.product_plan
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.service_bandwidth):
            query['ServiceBandwidth'] = request.service_bandwidth
        if not DaraCore.is_null(request.service_partner):
            query['ServicePartner'] = request.service_partner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRemark',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceRemark',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_remark(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
    ) -> main_models.ModifyInstanceRemarkResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: main_models.ModifyInstanceRemarkRequest,
    ) -> main_models.ModifyInstanceRemarkResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def modify_network_rule_attribute_with_options(
        self,
        request: main_models.ModifyNetworkRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNetworkRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNetworkRuleAttribute',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNetworkRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_rule_attribute_with_options_async(
        self,
        request: main_models.ModifyNetworkRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNetworkRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNetworkRuleAttribute',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNetworkRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_rule_attribute(
        self,
        request: main_models.ModifyNetworkRuleAttributeRequest,
    ) -> main_models.ModifyNetworkRuleAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_network_rule_attribute_with_options(request, runtime)

    async def modify_network_rule_attribute_async(
        self,
        request: main_models.ModifyNetworkRuleAttributeRequest,
    ) -> main_models.ModifyNetworkRuleAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_network_rule_attribute_with_options_async(request, runtime)

    def modify_ocsp_status_with_options(
        self,
        request: main_models.ModifyOcspStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOcspStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOcspStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOcspStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ocsp_status_with_options_async(
        self,
        request: main_models.ModifyOcspStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOcspStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOcspStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOcspStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ocsp_status(
        self,
        request: main_models.ModifyOcspStatusRequest,
    ) -> main_models.ModifyOcspStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_ocsp_status_with_options(request, runtime)

    async def modify_ocsp_status_async(
        self,
        request: main_models.ModifyOcspStatusRequest,
    ) -> main_models.ModifyOcspStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_ocsp_status_with_options_async(request, runtime)

    def modify_port_with_options(
        self,
        request: main_models.ModifyPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_port_with_options_async(
        self,
        request: main_models.ModifyPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not DaraCore.is_null(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not DaraCore.is_null(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.proxy_enable):
            query['ProxyEnable'] = request.proxy_enable
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPort',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_port(
        self,
        request: main_models.ModifyPortRequest,
    ) -> main_models.ModifyPortResponse:
        runtime = RuntimeOptions()
        return self.modify_port_with_options(request, runtime)

    async def modify_port_async(
        self,
        request: main_models.ModifyPortRequest,
    ) -> main_models.ModifyPortResponse:
        runtime = RuntimeOptions()
        return await self.modify_port_with_options_async(request, runtime)

    def modify_port_auto_cc_status_with_options(
        self,
        request: main_models.ModifyPortAutoCcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPortAutoCcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.switch):
            query['Switch'] = request.switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPortAutoCcStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_port_auto_cc_status_with_options_async(
        self,
        request: main_models.ModifyPortAutoCcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPortAutoCcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.switch):
            query['Switch'] = request.switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPortAutoCcStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPortAutoCcStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_port_auto_cc_status(
        self,
        request: main_models.ModifyPortAutoCcStatusRequest,
    ) -> main_models.ModifyPortAutoCcStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_port_auto_cc_status_with_options(request, runtime)

    async def modify_port_auto_cc_status_async(
        self,
        request: main_models.ModifyPortAutoCcStatusRequest,
    ) -> main_models.ModifyPortAutoCcStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_port_auto_cc_status_with_options_async(request, runtime)

    def modify_qps_mode_with_options(
        self,
        request: main_models.ModifyQpsModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQpsModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQpsMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQpsModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qps_mode_with_options_async(
        self,
        request: main_models.ModifyQpsModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQpsModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQpsMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQpsModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qps_mode(
        self,
        request: main_models.ModifyQpsModeRequest,
    ) -> main_models.ModifyQpsModeResponse:
        runtime = RuntimeOptions()
        return self.modify_qps_mode_with_options(request, runtime)

    async def modify_qps_mode_async(
        self,
        request: main_models.ModifyQpsModeRequest,
    ) -> main_models.ModifyQpsModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_qps_mode_with_options_async(request, runtime)

    def modify_scene_defense_policy_with_options(
        self,
        request: main_models.ModifySceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scene_defense_policy_with_options_async(
        self,
        request: main_models.ModifySceneDefensePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySceneDefensePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySceneDefensePolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySceneDefensePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scene_defense_policy(
        self,
        request: main_models.ModifySceneDefensePolicyRequest,
    ) -> main_models.ModifySceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_scene_defense_policy_with_options(request, runtime)

    async def modify_scene_defense_policy_async(
        self,
        request: main_models.ModifySceneDefensePolicyRequest,
    ) -> main_models.ModifySceneDefensePolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_scene_defense_policy_with_options_async(request, runtime)

    def modify_scheduler_rule_with_options(
        self,
        request: main_models.ModifySchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduler_rule_with_options_async(
        self,
        request: main_models.ModifySchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduler_rule(
        self,
        request: main_models.ModifySchedulerRuleRequest,
    ) -> main_models.ModifySchedulerRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_scheduler_rule_with_options(request, runtime)

    async def modify_scheduler_rule_async(
        self,
        request: main_models.ModifySchedulerRuleRequest,
    ) -> main_models.ModifySchedulerRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_scheduler_rule_with_options_async(request, runtime)

    def modify_tls_config_with_options(
        self,
        request: main_models.ModifyTlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTlsConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTlsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tls_config_with_options_async(
        self,
        request: main_models.ModifyTlsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTlsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTlsConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTlsConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tls_config(
        self,
        request: main_models.ModifyTlsConfigRequest,
    ) -> main_models.ModifyTlsConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_tls_config_with_options(request, runtime)

    async def modify_tls_config_async(
        self,
        request: main_models.ModifyTlsConfigRequest,
    ) -> main_models.ModifyTlsConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_tls_config_with_options_async(request, runtime)

    def modify_web_aiprotect_mode_with_options(
        self,
        request: main_models.ModifyWebAIProtectModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAIProtectModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAIProtectMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAIProtectModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_aiprotect_mode_with_options_async(
        self,
        request: main_models.ModifyWebAIProtectModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAIProtectModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAIProtectMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAIProtectModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_aiprotect_mode(
        self,
        request: main_models.ModifyWebAIProtectModeRequest,
    ) -> main_models.ModifyWebAIProtectModeResponse:
        runtime = RuntimeOptions()
        return self.modify_web_aiprotect_mode_with_options(request, runtime)

    async def modify_web_aiprotect_mode_async(
        self,
        request: main_models.ModifyWebAIProtectModeRequest,
    ) -> main_models.ModifyWebAIProtectModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_aiprotect_mode_with_options_async(request, runtime)

    def modify_web_aiprotect_switch_with_options(
        self,
        request: main_models.ModifyWebAIProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAIProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAIProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAIProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_aiprotect_switch_with_options_async(
        self,
        request: main_models.ModifyWebAIProtectSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAIProtectSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAIProtectSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAIProtectSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_aiprotect_switch(
        self,
        request: main_models.ModifyWebAIProtectSwitchRequest,
    ) -> main_models.ModifyWebAIProtectSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_aiprotect_switch_with_options(request, runtime)

    async def modify_web_aiprotect_switch_async(
        self,
        request: main_models.ModifyWebAIProtectSwitchRequest,
    ) -> main_models.ModifyWebAIProtectSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_aiprotect_switch_with_options_async(request, runtime)

    def modify_web_access_mode_with_options(
        self,
        request: main_models.ModifyWebAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAccessMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_access_mode_with_options_async(
        self,
        request: main_models.ModifyWebAccessModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAccessModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAccessMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAccessModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_access_mode(
        self,
        request: main_models.ModifyWebAccessModeRequest,
    ) -> main_models.ModifyWebAccessModeResponse:
        runtime = RuntimeOptions()
        return self.modify_web_access_mode_with_options(request, runtime)

    async def modify_web_access_mode_async(
        self,
        request: main_models.ModifyWebAccessModeRequest,
    ) -> main_models.ModifyWebAccessModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_access_mode_with_options_async(request, runtime)

    def modify_web_area_block_with_options(
        self,
        request: main_models.ModifyWebAreaBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAreaBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAreaBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAreaBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_area_block_with_options_async(
        self,
        request: main_models.ModifyWebAreaBlockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAreaBlockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAreaBlock',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAreaBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_area_block(
        self,
        request: main_models.ModifyWebAreaBlockRequest,
    ) -> main_models.ModifyWebAreaBlockResponse:
        runtime = RuntimeOptions()
        return self.modify_web_area_block_with_options(request, runtime)

    async def modify_web_area_block_async(
        self,
        request: main_models.ModifyWebAreaBlockRequest,
    ) -> main_models.ModifyWebAreaBlockResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_area_block_with_options_async(request, runtime)

    def modify_web_area_block_switch_with_options(
        self,
        request: main_models.ModifyWebAreaBlockSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAreaBlockSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAreaBlockSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAreaBlockSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_area_block_switch_with_options_async(
        self,
        request: main_models.ModifyWebAreaBlockSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebAreaBlockSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebAreaBlockSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebAreaBlockSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_area_block_switch(
        self,
        request: main_models.ModifyWebAreaBlockSwitchRequest,
    ) -> main_models.ModifyWebAreaBlockSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_area_block_switch_with_options(request, runtime)

    async def modify_web_area_block_switch_async(
        self,
        request: main_models.ModifyWebAreaBlockSwitchRequest,
    ) -> main_models.ModifyWebAreaBlockSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_area_block_switch_with_options_async(request, runtime)

    def modify_web_ccglobal_switch_with_options(
        self,
        request: main_models.ModifyWebCCGlobalSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCCGlobalSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cc_global_switch):
            query['CcGlobalSwitch'] = request.cc_global_switch
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCCGlobalSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCCGlobalSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ccglobal_switch_with_options_async(
        self,
        request: main_models.ModifyWebCCGlobalSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCCGlobalSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cc_global_switch):
            query['CcGlobalSwitch'] = request.cc_global_switch
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCCGlobalSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCCGlobalSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_ccglobal_switch(
        self,
        request: main_models.ModifyWebCCGlobalSwitchRequest,
    ) -> main_models.ModifyWebCCGlobalSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_ccglobal_switch_with_options(request, runtime)

    async def modify_web_ccglobal_switch_async(
        self,
        request: main_models.ModifyWebCCGlobalSwitchRequest,
    ) -> main_models.ModifyWebCCGlobalSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_ccglobal_switch_with_options_async(request, runtime)

    def modify_web_ccrule_with_options(
        self,
        request: main_models.ModifyWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ccrule_with_options_async(
        self,
        request: main_models.ModifyWebCCRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCCRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.uri):
            query['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCCRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCCRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_ccrule(
        self,
        request: main_models.ModifyWebCCRuleRequest,
    ) -> main_models.ModifyWebCCRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_web_ccrule_with_options(request, runtime)

    async def modify_web_ccrule_async(
        self,
        request: main_models.ModifyWebCCRuleRequest,
    ) -> main_models.ModifyWebCCRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_ccrule_with_options_async(request, runtime)

    def modify_web_cache_custom_rule_with_options(
        self,
        request: main_models.ModifyWebCacheCustomRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheCustomRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheCustomRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_custom_rule_with_options_async(
        self,
        request: main_models.ModifyWebCacheCustomRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheCustomRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheCustomRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheCustomRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_cache_custom_rule(
        self,
        request: main_models.ModifyWebCacheCustomRuleRequest,
    ) -> main_models.ModifyWebCacheCustomRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_web_cache_custom_rule_with_options(request, runtime)

    async def modify_web_cache_custom_rule_async(
        self,
        request: main_models.ModifyWebCacheCustomRuleRequest,
    ) -> main_models.ModifyWebCacheCustomRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_cache_custom_rule_with_options_async(request, runtime)

    def modify_web_cache_mode_with_options(
        self,
        request: main_models.ModifyWebCacheModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_mode_with_options_async(
        self,
        request: main_models.ModifyWebCacheModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheMode',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_cache_mode(
        self,
        request: main_models.ModifyWebCacheModeRequest,
    ) -> main_models.ModifyWebCacheModeResponse:
        runtime = RuntimeOptions()
        return self.modify_web_cache_mode_with_options(request, runtime)

    async def modify_web_cache_mode_async(
        self,
        request: main_models.ModifyWebCacheModeRequest,
    ) -> main_models.ModifyWebCacheModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_cache_mode_with_options_async(request, runtime)

    def modify_web_cache_switch_with_options(
        self,
        request: main_models.ModifyWebCacheSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_cache_switch_with_options_async(
        self,
        request: main_models.ModifyWebCacheSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebCacheSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebCacheSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebCacheSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_cache_switch(
        self,
        request: main_models.ModifyWebCacheSwitchRequest,
    ) -> main_models.ModifyWebCacheSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_cache_switch_with_options(request, runtime)

    async def modify_web_cache_switch_async(
        self,
        request: main_models.ModifyWebCacheSwitchRequest,
    ) -> main_models.ModifyWebCacheSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_cache_switch_with_options_async(request, runtime)

    def modify_web_ip_set_switch_with_options(
        self,
        request: main_models.ModifyWebIpSetSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebIpSetSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebIpSetSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebIpSetSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ip_set_switch_with_options_async(
        self,
        request: main_models.ModifyWebIpSetSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebIpSetSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebIpSetSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebIpSetSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_ip_set_switch(
        self,
        request: main_models.ModifyWebIpSetSwitchRequest,
    ) -> main_models.ModifyWebIpSetSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_ip_set_switch_with_options(request, runtime)

    async def modify_web_ip_set_switch_async(
        self,
        request: main_models.ModifyWebIpSetSwitchRequest,
    ) -> main_models.ModifyWebIpSetSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_ip_set_switch_with_options_async(request, runtime)

    def modify_web_precise_access_rule_with_options(
        self,
        request: main_models.ModifyWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_precise_access_rule_with_options_async(
        self,
        request: main_models.ModifyWebPreciseAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebPreciseAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebPreciseAccessRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebPreciseAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_precise_access_rule(
        self,
        request: main_models.ModifyWebPreciseAccessRuleRequest,
    ) -> main_models.ModifyWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_web_precise_access_rule_with_options(request, runtime)

    async def modify_web_precise_access_rule_async(
        self,
        request: main_models.ModifyWebPreciseAccessRuleRequest,
    ) -> main_models.ModifyWebPreciseAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_precise_access_rule_with_options_async(request, runtime)

    def modify_web_precise_access_switch_with_options(
        self,
        request: main_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebPreciseAccessSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebPreciseAccessSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebPreciseAccessSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_precise_access_switch_with_options_async(
        self,
        request: main_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebPreciseAccessSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebPreciseAccessSwitch',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebPreciseAccessSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_precise_access_switch(
        self,
        request: main_models.ModifyWebPreciseAccessSwitchRequest,
    ) -> main_models.ModifyWebPreciseAccessSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_web_precise_access_switch_with_options(request, runtime)

    async def modify_web_precise_access_switch_async(
        self,
        request: main_models.ModifyWebPreciseAccessSwitchRequest,
    ) -> main_models.ModifyWebPreciseAccessSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_precise_access_switch_with_options_async(request, runtime)

    def modify_web_rule_with_options(
        self,
        request: main_models.ModifyWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_rule_with_options_async(
        self,
        request: main_models.ModifyWebRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWebRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not DaraCore.is_null(request.real_servers):
            query['RealServers'] = request.real_servers
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWebRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWebRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_rule(
        self,
        request: main_models.ModifyWebRuleRequest,
    ) -> main_models.ModifyWebRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_web_rule_with_options(request, runtime)

    async def modify_web_rule_async(
        self,
        request: main_models.ModifyWebRuleRequest,
    ) -> main_models.ModifyWebRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_web_rule_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def switch_scheduler_rule_with_options(
        self,
        request: main_models.SwitchSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.switch_data):
            query['SwitchData'] = request.switch_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_scheduler_rule_with_options_async(
        self,
        request: main_models.SwitchSchedulerRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSchedulerRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.switch_data):
            query['SwitchData'] = request.switch_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSchedulerRule',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSchedulerRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_scheduler_rule(
        self,
        request: main_models.SwitchSchedulerRuleRequest,
    ) -> main_models.SwitchSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return self.switch_scheduler_rule_with_options(request, runtime)

    async def switch_scheduler_rule_async(
        self,
        request: main_models.SwitchSchedulerRuleRequest,
    ) -> main_models.SwitchSchedulerRuleResponse:
        runtime = RuntimeOptions()
        return await self.switch_scheduler_rule_with_options_async(request, runtime)
