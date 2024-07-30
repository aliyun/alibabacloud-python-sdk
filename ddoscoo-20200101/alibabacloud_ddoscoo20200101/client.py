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
        """
        @param request: AddAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: AddAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: AddAutoCcBlacklistRequest
        @return: AddAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_blacklist_with_options(request, runtime)

    async def add_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcBlacklistResponse:
        """
        @param request: AddAutoCcBlacklistRequest
        @return: AddAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_auto_cc_blacklist_with_options_async(request, runtime)

    def add_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        """
        @summary Adds IP addresses to the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call the AddAutoCcWhitelist operation to add IP addresses to the whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance. This way, the Anti-DDoS Pro or Anti-DDoS Premium instance allows traffic from the IP addresses.
        By default, the traffic from the IP addresses that you add to the whitelist is always allowed. If you no longer use the whitelist, you can call the [EmptyAutoCcWhitelist](https://help.aliyun.com/document_detail/157505.html) operation to remove the IP addresses from the whitelist.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds IP addresses to the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call the AddAutoCcWhitelist operation to add IP addresses to the whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance. This way, the Anti-DDoS Pro or Anti-DDoS Premium instance allows traffic from the IP addresses.
        By default, the traffic from the IP addresses that you add to the whitelist is always allowed. If you no longer use the whitelist, you can call the [EmptyAutoCcWhitelist](https://help.aliyun.com/document_detail/157505.html) operation to remove the IP addresses from the whitelist.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds IP addresses to the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call the AddAutoCcWhitelist operation to add IP addresses to the whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance. This way, the Anti-DDoS Pro or Anti-DDoS Premium instance allows traffic from the IP addresses.
        By default, the traffic from the IP addresses that you add to the whitelist is always allowed. If you no longer use the whitelist, you can call the [EmptyAutoCcWhitelist](https://help.aliyun.com/document_detail/157505.html) operation to remove the IP addresses from the whitelist.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAutoCcWhitelistRequest
        @return: AddAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_whitelist_with_options(request, runtime)

    async def add_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.AddAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.AddAutoCcWhitelistResponse:
        """
        @summary Adds IP addresses to the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call the AddAutoCcWhitelist operation to add IP addresses to the whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance. This way, the Anti-DDoS Pro or Anti-DDoS Premium instance allows traffic from the IP addresses.
        By default, the traffic from the IP addresses that you add to the whitelist is always allowed. If you no longer use the whitelist, you can call the [EmptyAutoCcWhitelist](https://help.aliyun.com/document_detail/157505.html) operation to remove the IP addresses from the whitelist.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAutoCcWhitelistRequest
        @return: AddAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_auto_cc_whitelist_with_options_async(request, runtime)

    def associate_web_cert_with_options(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        """
        @summary Associates an SSL certificate with the forwarding rule of a website.
        
        @param request: AssociateWebCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateWebCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_identifier):
            body['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            body['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateWebCert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Associates an SSL certificate with the forwarding rule of a website.
        
        @param request: AssociateWebCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateWebCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_identifier):
            body['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            body['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateWebCert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Associates an SSL certificate with the forwarding rule of a website.
        
        @param request: AssociateWebCertRequest
        @return: AssociateWebCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_web_cert_with_options(request, runtime)

    async def associate_web_cert_async(
        self,
        request: ddoscoo_20200101_models.AssociateWebCertRequest,
    ) -> ddoscoo_20200101_models.AssociateWebCertResponse:
        """
        @summary Associates an SSL certificate with the forwarding rule of a website.
        
        @param request: AssociateWebCertRequest
        @return: AssociateWebCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_web_cert_with_options_async(request, runtime)

    def attach_scene_defense_object_with_options(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        """
        @summary Adds an object to a scenario-specific custom policy for protection.
        
        @param request: AttachSceneDefenseObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachSceneDefenseObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds an object to a scenario-specific custom policy for protection.
        
        @param request: AttachSceneDefenseObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachSceneDefenseObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds an object to a scenario-specific custom policy for protection.
        
        @param request: AttachSceneDefenseObjectRequest
        @return: AttachSceneDefenseObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_scene_defense_object_with_options(request, runtime)

    async def attach_scene_defense_object_async(
        self,
        request: ddoscoo_20200101_models.AttachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.AttachSceneDefenseObjectResponse:
        """
        @summary Adds an object to a scenario-specific custom policy for protection.
        
        @param request: AttachSceneDefenseObjectRequest
        @return: AttachSceneDefenseObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_scene_defense_object_with_options_async(request, runtime)

    def config_domain_security_profile_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigDomainSecurityProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse:
        """
        @summary Configures the global mitigation policy feature, including the feature status and settings.
        
        @param request: ConfigDomainSecurityProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigDomainSecurityProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigDomainSecurityProfile',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_domain_security_profile_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigDomainSecurityProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse:
        """
        @summary Configures the global mitigation policy feature, including the feature status and settings.
        
        @param request: ConfigDomainSecurityProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigDomainSecurityProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigDomainSecurityProfile',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_domain_security_profile(
        self,
        request: ddoscoo_20200101_models.ConfigDomainSecurityProfileRequest,
    ) -> ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse:
        """
        @summary Configures the global mitigation policy feature, including the feature status and settings.
        
        @param request: ConfigDomainSecurityProfileRequest
        @return: ConfigDomainSecurityProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_domain_security_profile_with_options(request, runtime)

    async def config_domain_security_profile_async(
        self,
        request: ddoscoo_20200101_models.ConfigDomainSecurityProfileRequest,
    ) -> ddoscoo_20200101_models.ConfigDomainSecurityProfileResponse:
        """
        @summary Configures the global mitigation policy feature, including the feature status and settings.
        
        @param request: ConfigDomainSecurityProfileRequest
        @return: ConfigDomainSecurityProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_domain_security_profile_with_options_async(request, runtime)

    def config_l7rs_policy_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        """
        @summary Configures a back-to-origin policy for the forwarding rule of a website.
        
        @description If multiple origin servers are configured for a website that is added to Anti-DDoS Pro or Anti-DDoS Premium, you can modify the load balancing algorithms for back-to-origin traffic based on back-to-origin policies. The IP hash algorithm is used by default. You can change the algorithm to the round-robin or least response time algorithm. For more information, see the description of the *Policy** parameter in the "Request parameters" section of this topic.
        
        @param request: ConfigL7RsPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigL7RsPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.upstream_retry):
            query['UpstreamRetry'] = request.upstream_retry
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures a back-to-origin policy for the forwarding rule of a website.
        
        @description If multiple origin servers are configured for a website that is added to Anti-DDoS Pro or Anti-DDoS Premium, you can modify the load balancing algorithms for back-to-origin traffic based on back-to-origin policies. The IP hash algorithm is used by default. You can change the algorithm to the round-robin or least response time algorithm. For more information, see the description of the *Policy** parameter in the "Request parameters" section of this topic.
        
        @param request: ConfigL7RsPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigL7RsPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.upstream_retry):
            query['UpstreamRetry'] = request.upstream_retry
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures a back-to-origin policy for the forwarding rule of a website.
        
        @description If multiple origin servers are configured for a website that is added to Anti-DDoS Pro or Anti-DDoS Premium, you can modify the load balancing algorithms for back-to-origin traffic based on back-to-origin policies. The IP hash algorithm is used by default. You can change the algorithm to the round-robin or least response time algorithm. For more information, see the description of the *Policy** parameter in the "Request parameters" section of this topic.
        
        @param request: ConfigL7RsPolicyRequest
        @return: ConfigL7RsPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_l7rs_policy_with_options(request, runtime)

    async def config_l7rs_policy_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.ConfigL7RsPolicyResponse:
        """
        @summary Configures a back-to-origin policy for the forwarding rule of a website.
        
        @description If multiple origin servers are configured for a website that is added to Anti-DDoS Pro or Anti-DDoS Premium, you can modify the load balancing algorithms for back-to-origin traffic based on back-to-origin policies. The IP hash algorithm is used by default. You can change the algorithm to the round-robin or least response time algorithm. For more information, see the description of the *Policy** parameter in the "Request parameters" section of this topic.
        
        @param request: ConfigL7RsPolicyRequest
        @return: ConfigL7RsPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_l7rs_policy_with_options_async(request, runtime)

    def config_l7us_keepalive_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigL7UsKeepaliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse:
        """
        @summary Configures the settings for back-to-origin persistent connections for a domain name.
        
        @param request: ConfigL7UsKeepaliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigL7UsKeepaliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.upstream_keepalive):
            query['UpstreamKeepalive'] = request.upstream_keepalive
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigL7UsKeepalive',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_l7us_keepalive_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7UsKeepaliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse:
        """
        @summary Configures the settings for back-to-origin persistent connections for a domain name.
        
        @param request: ConfigL7UsKeepaliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigL7UsKeepaliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.upstream_keepalive):
            query['UpstreamKeepalive'] = request.upstream_keepalive
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigL7UsKeepalive',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_l7us_keepalive(
        self,
        request: ddoscoo_20200101_models.ConfigL7UsKeepaliveRequest,
    ) -> ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse:
        """
        @summary Configures the settings for back-to-origin persistent connections for a domain name.
        
        @param request: ConfigL7UsKeepaliveRequest
        @return: ConfigL7UsKeepaliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_l7us_keepalive_with_options(request, runtime)

    async def config_l7us_keepalive_async(
        self,
        request: ddoscoo_20200101_models.ConfigL7UsKeepaliveRequest,
    ) -> ddoscoo_20200101_models.ConfigL7UsKeepaliveResponse:
        """
        @summary Configures the settings for back-to-origin persistent connections for a domain name.
        
        @param request: ConfigL7UsKeepaliveRequest
        @return: ConfigL7UsKeepaliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_l7us_keepalive_with_options_async(request, runtime)

    def config_layer_4real_limit_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RealLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RealLimitResponse:
        """
        @summary Specifies a threshold for the clean bandwidth of an Anti-DDoS Pro or Anti-DDoS premium instance. If the threshold is reached, rate limiting is triggered.
        
        @param request: ConfigLayer4RealLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RealLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.limit_value):
            query['LimitValue'] = request.limit_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RealLimit',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RealLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4real_limit_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RealLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RealLimitResponse:
        """
        @summary Specifies a threshold for the clean bandwidth of an Anti-DDoS Pro or Anti-DDoS premium instance. If the threshold is reached, rate limiting is triggered.
        
        @param request: ConfigLayer4RealLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RealLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.limit_value):
            query['LimitValue'] = request.limit_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RealLimit',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RealLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4real_limit(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RealLimitRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RealLimitResponse:
        """
        @summary Specifies a threshold for the clean bandwidth of an Anti-DDoS Pro or Anti-DDoS premium instance. If the threshold is reached, rate limiting is triggered.
        
        @param request: ConfigLayer4RealLimitRequest
        @return: ConfigLayer4RealLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4real_limit_with_options(request, runtime)

    async def config_layer_4real_limit_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RealLimitRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RealLimitResponse:
        """
        @summary Specifies a threshold for the clean bandwidth of an Anti-DDoS Pro or Anti-DDoS premium instance. If the threshold is reached, rate limiting is triggered.
        
        @param request: ConfigLayer4RealLimitRequest
        @return: ConfigLayer4RealLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4real_limit_with_options_async(request, runtime)

    def config_layer_4remark_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RemarkResponse:
        """
        @summary Adds a description to a port forwarding rule.
        
        @param request: ConfigLayer4RemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4Remark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4remark_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RemarkResponse:
        """
        @summary Adds a description to a port forwarding rule.
        
        @param request: ConfigLayer4RemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4Remark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4remark(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RemarkRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RemarkResponse:
        """
        @summary Adds a description to a port forwarding rule.
        
        @param request: ConfigLayer4RemarkRequest
        @return: ConfigLayer4RemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4remark_with_options(request, runtime)

    async def config_layer_4remark_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RemarkRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RemarkResponse:
        """
        @summary Adds a description to a port forwarding rule.
        
        @param request: ConfigLayer4RemarkRequest
        @return: ConfigLayer4RemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4remark_with_options_async(request, runtime)

    def config_layer_4rule_bak_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RuleBakModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse:
        """
        @summary Enables or disables the origin redundancy mode for a port forwarding rule.
        
        @param request: ConfigLayer4RuleBakModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleBakModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bak_mode):
            query['BakMode'] = request.bak_mode
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RuleBakMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_bak_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RuleBakModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse:
        """
        @summary Enables or disables the origin redundancy mode for a port forwarding rule.
        
        @param request: ConfigLayer4RuleBakModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RuleBakModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bak_mode):
            query['BakMode'] = request.bak_mode
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RuleBakMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule_bak_mode(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RuleBakModeRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse:
        """
        @summary Enables or disables the origin redundancy mode for a port forwarding rule.
        
        @param request: ConfigLayer4RuleBakModeRequest
        @return: ConfigLayer4RuleBakModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_bak_mode_with_options(request, runtime)

    async def config_layer_4rule_bak_mode_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RuleBakModeRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse:
        """
        @summary Enables or disables the origin redundancy mode for a port forwarding rule.
        
        @param request: ConfigLayer4RuleBakModeRequest
        @return: ConfigLayer4RuleBakModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_bak_mode_with_options_async(request, runtime)

    def config_layer_4rule_policy_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RulePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse:
        """
        @summary Configures the IP addresses of the primary and secondary origin servers for a port forwarding rule.
        
        @param request: ConfigLayer4RulePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RulePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_layer_4rule_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RulePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse:
        """
        @summary Configures the IP addresses of the primary and secondary origin servers for a port forwarding rule.
        
        @param request: ConfigLayer4RulePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigLayer4RulePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_layer_4rule_policy(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RulePolicyRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse:
        """
        @summary Configures the IP addresses of the primary and secondary origin servers for a port forwarding rule.
        
        @param request: ConfigLayer4RulePolicyRequest
        @return: ConfigLayer4RulePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_policy_with_options(request, runtime)

    async def config_layer_4rule_policy_async(
        self,
        request: ddoscoo_20200101_models.ConfigLayer4RulePolicyRequest,
    ) -> ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse:
        """
        @summary Configures the IP addresses of the primary and secondary origin servers for a port forwarding rule.
        
        @param request: ConfigLayer4RulePolicyRequest
        @return: ConfigLayer4RulePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_policy_with_options_async(request, runtime)

    def config_network_region_block_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        """
        @summary Configures blocked locations for an Anti-DDoS Proxy instance.
        
        @param request: ConfigNetworkRegionBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetworkRegionBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures blocked locations for an Anti-DDoS Proxy instance.
        
        @param request: ConfigNetworkRegionBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetworkRegionBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures blocked locations for an Anti-DDoS Proxy instance.
        
        @param request: ConfigNetworkRegionBlockRequest
        @return: ConfigNetworkRegionBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_network_region_block_with_options(request, runtime)

    async def config_network_region_block_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse:
        """
        @summary Configures blocked locations for an Anti-DDoS Proxy instance.
        
        @param request: ConfigNetworkRegionBlockRequest
        @return: ConfigNetworkRegionBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_network_region_block_with_options_async(request, runtime)

    def config_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        """
        @summary Modifies the IP addresses of the origin server that is configured in a port forwarding rule.
        
        @param request: ConfigNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the IP addresses of the origin server that is configured in a port forwarding rule.
        
        @param request: ConfigNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the IP addresses of the origin server that is configured in a port forwarding rule.
        
        @param request: ConfigNetworkRulesRequest
        @return: ConfigNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_network_rules_with_options(request, runtime)

    async def config_network_rules_async(
        self,
        request: ddoscoo_20200101_models.ConfigNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.ConfigNetworkRulesResponse:
        """
        @summary Modifies the IP addresses of the origin server that is configured in a port forwarding rule.
        
        @param request: ConfigNetworkRulesRequest
        @return: ConfigNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_network_rules_with_options_async(request, runtime)

    def config_udp_reflect_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigUdpReflectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigUdpReflectResponse:
        """
        @summary Adds the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance to filter out the source ports of UDP traffic.
        
        @description You can call this operation to configure filtering policies to filter out UDP traffic from specific ports. This helps defend against UDP reflection attacks.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigUdpReflectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigUdpReflectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_udp_reflect_with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigUdpReflectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigUdpReflectResponse:
        """
        @summary Adds the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance to filter out the source ports of UDP traffic.
        
        @description You can call this operation to configure filtering policies to filter out UDP traffic from specific ports. This helps defend against UDP reflection attacks.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigUdpReflectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigUdpReflectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigUdpReflectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_udp_reflect(
        self,
        request: ddoscoo_20200101_models.ConfigUdpReflectRequest,
    ) -> ddoscoo_20200101_models.ConfigUdpReflectResponse:
        """
        @summary Adds the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance to filter out the source ports of UDP traffic.
        
        @description You can call this operation to configure filtering policies to filter out UDP traffic from specific ports. This helps defend against UDP reflection attacks.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigUdpReflectRequest
        @return: ConfigUdpReflectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_udp_reflect_with_options(request, runtime)

    async def config_udp_reflect_async(
        self,
        request: ddoscoo_20200101_models.ConfigUdpReflectRequest,
    ) -> ddoscoo_20200101_models.ConfigUdpReflectResponse:
        """
        @summary Adds the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance to filter out the source ports of UDP traffic.
        
        @description You can call this operation to configure filtering policies to filter out UDP traffic from specific ports. This helps defend against UDP reflection attacks.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigUdpReflectRequest
        @return: ConfigUdpReflectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_udp_reflect_with_options_async(request, runtime)

    def config_web_ccrule_v2with_options(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCRuleV2Response:
        """
        @summary 配置新版基于匹配条件的cc规则
        
        @param request: ConfigWebCCRuleV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebCCRuleV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.expires):
            query['Expires'] = request.expires
        if not UtilClient.is_unset(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebCCRuleV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebCCRuleV2Response(),
            self.call_api(params, req, runtime)
        )

    async def config_web_ccrule_v2with_options_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCRuleV2Response:
        """
        @summary 配置新版基于匹配条件的cc规则
        
        @param request: ConfigWebCCRuleV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebCCRuleV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.expires):
            query['Expires'] = request.expires
        if not UtilClient.is_unset(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebCCRuleV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebCCRuleV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def config_web_ccrule_v2(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCRuleV2Request,
    ) -> ddoscoo_20200101_models.ConfigWebCCRuleV2Response:
        """
        @summary 配置新版基于匹配条件的cc规则
        
        @param request: ConfigWebCCRuleV2Request
        @return: ConfigWebCCRuleV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.config_web_ccrule_v2with_options(request, runtime)

    async def config_web_ccrule_v2_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCRuleV2Request,
    ) -> ddoscoo_20200101_models.ConfigWebCCRuleV2Response:
        """
        @summary 配置新版基于匹配条件的cc规则
        
        @param request: ConfigWebCCRuleV2Request
        @return: ConfigWebCCRuleV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_web_ccrule_v2with_options_async(request, runtime)

    def config_web_cctemplate_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        """
        @summary Configures the mode of the Frequency Control policy for a website.
        
        @param request: ConfigWebCCTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebCCTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebCCTemplate',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures the mode of the Frequency Control policy for a website.
        
        @param request: ConfigWebCCTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebCCTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebCCTemplate',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures the mode of the Frequency Control policy for a website.
        
        @param request: ConfigWebCCTemplateRequest
        @return: ConfigWebCCTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_web_cctemplate_with_options(request, runtime)

    async def config_web_cctemplate_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebCCTemplateRequest,
    ) -> ddoscoo_20200101_models.ConfigWebCCTemplateResponse:
        """
        @summary Configures the mode of the Frequency Control policy for a website.
        
        @param request: ConfigWebCCTemplateRequest
        @return: ConfigWebCCTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_web_cctemplate_with_options_async(request, runtime)

    def config_web_ip_set_with_options(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        """
        @summary Configures the IP address whitelist and blacklist for a website.
        
        @param request: ConfigWebIpSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_list):
            query['BlackList'] = request.black_list
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebIpSet',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures the IP address whitelist and blacklist for a website.
        
        @param request: ConfigWebIpSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigWebIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_list):
            query['BlackList'] = request.black_list
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebIpSet',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Configures the IP address whitelist and blacklist for a website.
        
        @param request: ConfigWebIpSetRequest
        @return: ConfigWebIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_web_ip_set_with_options(request, runtime)

    async def config_web_ip_set_async(
        self,
        request: ddoscoo_20200101_models.ConfigWebIpSetRequest,
    ) -> ddoscoo_20200101_models.ConfigWebIpSetResponse:
        """
        @summary Configures the IP address whitelist and blacklist for a website.
        
        @param request: ConfigWebIpSetRequest
        @return: ConfigWebIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_web_ip_set_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        """
        @summary Creates an asynchronous export task to export forwarding rules for websites, port forwarding rules, session persistence and health check settings, DDoS mitigation policies, the IP address blacklist, or the IP address whitelist.
        
        @param request: CreateAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_params):
            query['TaskParams'] = request.task_params
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates an asynchronous export task to export forwarding rules for websites, port forwarding rules, session persistence and health check settings, DDoS mitigation policies, the IP address blacklist, or the IP address whitelist.
        
        @param request: CreateAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_params):
            query['TaskParams'] = request.task_params
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates an asynchronous export task to export forwarding rules for websites, port forwarding rules, session persistence and health check settings, DDoS mitigation policies, the IP address blacklist, or the IP address whitelist.
        
        @param request: CreateAsyncTaskRequest
        @return: CreateAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: ddoscoo_20200101_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.CreateAsyncTaskResponse:
        """
        @summary Creates an asynchronous export task to export forwarding rules for websites, port forwarding rules, session persistence and health check settings, DDoS mitigation policies, the IP address blacklist, or the IP address whitelist.
        
        @param request: CreateAsyncTaskRequest
        @return: CreateAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def create_domain_resource_with_options(
        self,
        request: ddoscoo_20200101_models.CreateDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateDomainResourceResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_resource_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreateDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateDomainResourceResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_resource(
        self,
        request: ddoscoo_20200101_models.CreateDomainResourceRequest,
    ) -> ddoscoo_20200101_models.CreateDomainResourceResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateDomainResourceRequest
        @return: CreateDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_resource_with_options(request, runtime)

    async def create_domain_resource_async(
        self,
        request: ddoscoo_20200101_models.CreateDomainResourceRequest,
    ) -> ddoscoo_20200101_models.CreateDomainResourceResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateDomainResourceRequest
        @return: CreateDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_resource_with_options_async(request, runtime)

    def create_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        """
        @summary Creates a port forwarding rule.
        
        @param request: CreateNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a port forwarding rule.
        
        @param request: CreateNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a port forwarding rule.
        
        @param request: CreateNetworkRulesRequest
        @return: CreateNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_rules_with_options(request, runtime)

    async def create_network_rules_async(
        self,
        request: ddoscoo_20200101_models.CreateNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.CreateNetworkRulesResponse:
        """
        @summary Creates a port forwarding rule.
        
        @param request: CreateNetworkRulesRequest
        @return: CreateNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_rules_with_options_async(request, runtime)

    def create_port_with_options(
        self,
        request: ddoscoo_20200101_models.CreatePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreatePortResponse:
        """
        @summary Creates a port forwarding rule.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: CreatePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreatePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_port_with_options_async(
        self,
        request: ddoscoo_20200101_models.CreatePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreatePortResponse:
        """
        @summary Creates a port forwarding rule.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: CreatePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreatePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_port(
        self,
        request: ddoscoo_20200101_models.CreatePortRequest,
    ) -> ddoscoo_20200101_models.CreatePortResponse:
        """
        @summary Creates a port forwarding rule.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: CreatePortRequest
        @return: CreatePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_port_with_options(request, runtime)

    async def create_port_async(
        self,
        request: ddoscoo_20200101_models.CreatePortRequest,
    ) -> ddoscoo_20200101_models.CreatePortResponse:
        """
        @summary Creates a port forwarding rule.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: CreatePortRequest
        @return: CreatePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_port_with_options_async(request, runtime)

    def create_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        """
        @summary Creates a scenario-specific custom policy.
        
        @param request: CreateSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a scenario-specific custom policy.
        
        @param request: CreateSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a scenario-specific custom policy.
        
        @param request: CreateSceneDefensePolicyRequest
        @return: CreateSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scene_defense_policy_with_options(request, runtime)

    async def create_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.CreateSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.CreateSceneDefensePolicyResponse:
        """
        @summary Creates a scenario-specific custom policy.
        
        @param request: CreateSceneDefensePolicyRequest
        @return: CreateSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_defense_policy_with_options_async(request, runtime)

    def create_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        """
        @summary Creates a scheduling rule for Sec-Traffic Manager.
        
        @param request: CreateSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a scheduling rule for Sec-Traffic Manager.
        
        @param request: CreateSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a scheduling rule for Sec-Traffic Manager.
        
        @param request: CreateSchedulerRuleRequest
        @return: CreateSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduler_rule_with_options(request, runtime)

    async def create_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.CreateSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.CreateSchedulerRuleResponse:
        """
        @summary Creates a scheduling rule for Sec-Traffic Manager.
        
        @param request: CreateSchedulerRuleRequest
        @return: CreateSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduler_rule_with_options_async(request, runtime)

    def create_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        """
        @summary Adds tags to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        
        @description You can call the CreateTagResources operation to add a tag to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        >  Anti-DDoS Proxy (Outside Chinese Mainland) does not support the tag feature.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds tags to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        
        @description You can call the CreateTagResources operation to add a tag to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        >  Anti-DDoS Proxy (Outside Chinese Mainland) does not support the tag feature.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Adds tags to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        
        @description You can call the CreateTagResources operation to add a tag to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        >  Anti-DDoS Proxy (Outside Chinese Mainland) does not support the tag feature.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateTagResourcesRequest
        @return: CreateTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_resources_with_options(request, runtime)

    async def create_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.CreateTagResourcesRequest,
    ) -> ddoscoo_20200101_models.CreateTagResourcesResponse:
        """
        @summary Adds tags to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        
        @description You can call the CreateTagResources operation to add a tag to multiple Anti-DDoS Proxy (Chinese Mainland) instances at a time.
        >  Anti-DDoS Proxy (Outside Chinese Mainland) does not support the tag feature.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateTagResourcesRequest
        @return: CreateTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_resources_with_options_async(request, runtime)

    def create_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        """
        @deprecated OpenAPI CreateWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Creates a custom frequency control rule for a website.
        
        @param request: CreateWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI CreateWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Creates a custom frequency control rule for a website.
        
        @param request: CreateWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI CreateWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Creates a custom frequency control rule for a website.
        
        @param request: CreateWebCCRuleRequest
        @return: CreateWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_web_ccrule_with_options(request, runtime)

    async def create_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.CreateWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebCCRuleResponse:
        """
        @deprecated OpenAPI CreateWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Creates a custom frequency control rule for a website.
        
        @param request: CreateWebCCRuleRequest
        @return: CreateWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_web_ccrule_with_options_async(request, runtime)

    def create_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_id):
            query['DefenseId'] = request.defense_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_id):
            query['DefenseId'] = request.defense_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateWebRuleRequest
        @return: CreateWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_web_rule_with_options(request, runtime)

    async def create_web_rule_async(
        self,
        request: ddoscoo_20200101_models.CreateWebRuleRequest,
    ) -> ddoscoo_20200101_models.CreateWebRuleResponse:
        """
        @summary Creates a forwarding rule for a website.
        
        @param request: CreateWebRuleRequest
        @return: CreateWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_web_rule_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        """
        @summary Deletes an asynchronous export task.
        
        @param request: DeleteAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes an asynchronous export task.
        
        @param request: DeleteAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes an asynchronous export task.
        
        @param request: DeleteAsyncTaskRequest
        @return: DeleteAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: ddoscoo_20200101_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20200101_models.DeleteAsyncTaskResponse:
        """
        @summary Deletes an asynchronous export task.
        
        @param request: DeleteAsyncTaskRequest
        @return: DeleteAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def delete_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        """
        @summary Removes IP addresses from the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes IP addresses from the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes IP addresses from the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcBlacklistRequest
        @return: DeleteAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_blacklist_with_options(request, runtime)

    async def delete_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse:
        """
        @summary Removes IP addresses from the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcBlacklistRequest
        @return: DeleteAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_cc_blacklist_with_options_async(request, runtime)

    def delete_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        """
        @summary Removes IP addresses from the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes IP addresses from the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes IP addresses from the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcWhitelistRequest
        @return: DeleteAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_whitelist_with_options(request, runtime)

    async def delete_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.DeleteAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse:
        """
        @summary Removes IP addresses from the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DeleteAutoCcWhitelistRequest
        @return: DeleteAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_cc_whitelist_with_options_async(request, runtime)

    def delete_domain_resource_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteDomainResourceResponse:
        """
        @summary Deletes a specified forwarding rule of a website.
        
        @param request: DeleteDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_resource_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteDomainResourceResponse:
        """
        @summary Deletes a specified forwarding rule of a website.
        
        @param request: DeleteDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_resource(
        self,
        request: ddoscoo_20200101_models.DeleteDomainResourceRequest,
    ) -> ddoscoo_20200101_models.DeleteDomainResourceResponse:
        """
        @summary Deletes a specified forwarding rule of a website.
        
        @param request: DeleteDomainResourceRequest
        @return: DeleteDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_resource_with_options(request, runtime)

    async def delete_domain_resource_async(
        self,
        request: ddoscoo_20200101_models.DeleteDomainResourceRequest,
    ) -> ddoscoo_20200101_models.DeleteDomainResourceResponse:
        """
        @summary Deletes a specified forwarding rule of a website.
        
        @param request: DeleteDomainResourceRequest
        @return: DeleteDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_resource_with_options_async(request, runtime)

    def delete_network_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a port forwarding rule. You can delete only one port forwarding rule at a time.
        
        @param request: DeleteNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rule):
            query['NetworkRule'] = request.network_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a port forwarding rule. You can delete only one port forwarding rule at a time.
        
        @param request: DeleteNetworkRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rule):
            query['NetworkRule'] = request.network_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a port forwarding rule. You can delete only one port forwarding rule at a time.
        
        @param request: DeleteNetworkRuleRequest
        @return: DeleteNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    async def delete_network_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteNetworkRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteNetworkRuleResponse:
        """
        @summary Deletes a port forwarding rule. You can delete only one port forwarding rule at a time.
        
        @param request: DeleteNetworkRuleRequest
        @return: DeleteNetworkRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_rule_with_options_async(request, runtime)

    def delete_port_with_options(
        self,
        request: ddoscoo_20200101_models.DeletePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeletePortResponse:
        """
        @summary Deletes the specified port forwarding rule.
        
        @description After you delete a port forwarding rule, the Anti-DDoS Pro or Anti-DDoS Premium instance no longer forwards service traffic on the Layer 4 port. Before you delete a specific port forwarding rule, make sure that the service traffic destined for the Layer 4 port is redirected to the origin server. This can prevent negative impacts on your services.
        > You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DeletePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeletePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_port_with_options_async(
        self,
        request: ddoscoo_20200101_models.DeletePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeletePortResponse:
        """
        @summary Deletes the specified port forwarding rule.
        
        @description After you delete a port forwarding rule, the Anti-DDoS Pro or Anti-DDoS Premium instance no longer forwards service traffic on the Layer 4 port. Before you delete a specific port forwarding rule, make sure that the service traffic destined for the Layer 4 port is redirected to the origin server. This can prevent negative impacts on your services.
        > You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DeletePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeletePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_port(
        self,
        request: ddoscoo_20200101_models.DeletePortRequest,
    ) -> ddoscoo_20200101_models.DeletePortResponse:
        """
        @summary Deletes the specified port forwarding rule.
        
        @description After you delete a port forwarding rule, the Anti-DDoS Pro or Anti-DDoS Premium instance no longer forwards service traffic on the Layer 4 port. Before you delete a specific port forwarding rule, make sure that the service traffic destined for the Layer 4 port is redirected to the origin server. This can prevent negative impacts on your services.
        > You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DeletePortRequest
        @return: DeletePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_port_with_options(request, runtime)

    async def delete_port_async(
        self,
        request: ddoscoo_20200101_models.DeletePortRequest,
    ) -> ddoscoo_20200101_models.DeletePortResponse:
        """
        @summary Deletes the specified port forwarding rule.
        
        @description After you delete a port forwarding rule, the Anti-DDoS Pro or Anti-DDoS Premium instance no longer forwards service traffic on the Layer 4 port. Before you delete a specific port forwarding rule, make sure that the service traffic destined for the Layer 4 port is redirected to the origin server. This can prevent negative impacts on your services.
        > You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DeletePortRequest
        @return: DeletePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_port_with_options_async(request, runtime)

    def delete_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        """
        @summary Deletes a scenario-specific custom policy.
        
        @param request: DeleteSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a scenario-specific custom policy.
        
        @param request: DeleteSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a scenario-specific custom policy.
        
        @param request: DeleteSceneDefensePolicyRequest
        @return: DeleteSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_defense_policy_with_options(request, runtime)

    async def delete_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.DeleteSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse:
        """
        @summary Deletes a scenario-specific custom policy.
        
        @param request: DeleteSceneDefensePolicyRequest
        @return: DeleteSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_defense_policy_with_options_async(request, runtime)

    def delete_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        """
        @summary Deletes a scheduling rule of Sec-Traffic Manager.
        
        @param request: DeleteSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a scheduling rule of Sec-Traffic Manager.
        
        @param request: DeleteSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a scheduling rule of Sec-Traffic Manager.
        
        @param request: DeleteSchedulerRuleRequest
        @return: DeleteSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduler_rule_with_options(request, runtime)

    async def delete_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteSchedulerRuleResponse:
        """
        @summary Deletes a scheduling rule of Sec-Traffic Manager.
        
        @param request: DeleteSchedulerRuleRequest
        @return: DeleteSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduler_rule_with_options_async(request, runtime)

    def delete_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call the DeleteTagResources operation to remove tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call the DeleteTagResources operation to remove tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call the DeleteTagResources operation to remove tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteTagResourcesRequest
        @return: DeleteTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_resources_with_options(request, runtime)

    async def delete_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.DeleteTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DeleteTagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call the DeleteTagResources operation to remove tags from Anti-DDoS Proxy (Chinese Mainland) instances.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteTagResourcesRequest
        @return: DeleteTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_resources_with_options_async(request, runtime)

    def delete_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        """
        @deprecated OpenAPI DeleteWebCCRule is deprecated, please use ddoscoo::2020-01-01::DeleteWebCCRuleV2 instead.
        
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI DeleteWebCCRule is deprecated, please use ddoscoo::2020-01-01::DeleteWebCCRuleV2 instead.
        
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI DeleteWebCCRule is deprecated, please use ddoscoo::2020-01-01::DeleteWebCCRuleV2 instead.
        
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleRequest
        @return: DeleteWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_web_ccrule_with_options(request, runtime)

    async def delete_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleResponse:
        """
        @deprecated OpenAPI DeleteWebCCRule is deprecated, please use ddoscoo::2020-01-01::DeleteWebCCRuleV2 instead.
        
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleRequest
        @return: DeleteWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_ccrule_with_options_async(request, runtime)

    def delete_web_ccrule_v2with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleV2Response:
        """
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCCRuleV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRuleV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCCRuleV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_ccrule_v2with_options_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleV2Response:
        """
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCCRuleV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRuleV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCCRuleV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_ccrule_v2(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleV2Request,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleV2Response:
        """
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleV2Request
        @return: DeleteWebCCRuleV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_web_ccrule_v2with_options(request, runtime)

    async def delete_web_ccrule_v2_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCCRuleV2Request,
    ) -> ddoscoo_20200101_models.DeleteWebCCRuleV2Response:
        """
        @summary Deletes custom frequency control rules of a website.
        
        @param request: DeleteWebCCRuleV2Request
        @return: DeleteWebCCRuleV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_ccrule_v2with_options_async(request, runtime)

    def delete_web_cache_custom_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        """
        @summary Deletes the custom rules of the Static Page Caching policy for a website.
        
        @description You can call the DeleteWebCacheCustomRule operation to delete the custom rules of the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteWebCacheCustomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCacheCustomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes the custom rules of the Static Page Caching policy for a website.
        
        @description You can call the DeleteWebCacheCustomRule operation to delete the custom rules of the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteWebCacheCustomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCacheCustomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes the custom rules of the Static Page Caching policy for a website.
        
        @description You can call the DeleteWebCacheCustomRule operation to delete the custom rules of the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteWebCacheCustomRuleRequest
        @return: DeleteWebCacheCustomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_web_cache_custom_rule_with_options(request, runtime)

    async def delete_web_cache_custom_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse:
        """
        @summary Deletes the custom rules of the Static Page Caching policy for a website.
        
        @description You can call the DeleteWebCacheCustomRule operation to delete the custom rules of the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteWebCacheCustomRuleRequest
        @return: DeleteWebCacheCustomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_cache_custom_rule_with_options_async(request, runtime)

    def delete_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        """
        @summary Deletes the accurate access control rules that are created for a website.
        
        @param request: DeleteWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes the accurate access control rules that are created for a website.
        
        @param request: DeleteWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes the accurate access control rules that are created for a website.
        
        @param request: DeleteWebPreciseAccessRuleRequest
        @return: DeleteWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_web_precise_access_rule_with_options(request, runtime)

    async def delete_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse:
        """
        @summary Deletes the accurate access control rules that are created for a website.
        
        @param request: DeleteWebPreciseAccessRuleRequest
        @return: DeleteWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_precise_access_rule_with_options_async(request, runtime)

    def delete_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        """
        @summary Deletes a forwarding rule of a website.
        
        @param request: DeleteWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a forwarding rule of a website.
        
        @param request: DeleteWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a forwarding rule of a website.
        
        @param request: DeleteWebRuleRequest
        @return: DeleteWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_web_rule_with_options(request, runtime)

    async def delete_web_rule_async(
        self,
        request: ddoscoo_20200101_models.DeleteWebRuleRequest,
    ) -> ddoscoo_20200101_models.DeleteWebRuleResponse:
        """
        @summary Deletes a forwarding rule of a website.
        
        @param request: DeleteWebRuleRequest
        @return: DeleteWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_web_rule_with_options_async(request, runtime)

    def describe_async_tasks_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        """
        @summary Queries the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        
        @description You can call the DescribeAsyncTasks operation to query the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAsyncTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAsyncTasks',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        
        @description You can call the DescribeAsyncTasks operation to query the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAsyncTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAsyncTasks',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        
        @description You can call the DescribeAsyncTasks operation to query the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAsyncTasksRequest
        @return: DescribeAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_async_tasks_with_options(request, runtime)

    async def describe_async_tasks_async(
        self,
        request: ddoscoo_20200101_models.DescribeAsyncTasksRequest,
    ) -> ddoscoo_20200101_models.DescribeAsyncTasksResponse:
        """
        @summary Queries the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        
        @description You can call the DescribeAsyncTasks operation to query the details of asynchronous export tasks, such as the IDs, start time, end time, status, parameters, and results.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAsyncTasksRequest
        @return: DescribeAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_async_tasks_with_options_async(request, runtime)

    def describe_attack_analysis_max_qps_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse:
        """
        @summary Queries the peak QPS of DDoS attacks within the specific period of time.
        
        @param request: DescribeAttackAnalysisMaxQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttackAnalysisMaxQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisMaxQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_analysis_max_qps_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse:
        """
        @summary Queries the peak QPS of DDoS attacks within the specific period of time.
        
        @param request: DescribeAttackAnalysisMaxQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttackAnalysisMaxQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisMaxQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_analysis_max_qps(
        self,
        request: ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsRequest,
    ) -> ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse:
        """
        @summary Queries the peak QPS of DDoS attacks within the specific period of time.
        
        @param request: DescribeAttackAnalysisMaxQpsRequest
        @return: DescribeAttackAnalysisMaxQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_analysis_max_qps_with_options(request, runtime)

    async def describe_attack_analysis_max_qps_async(
        self,
        request: ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsRequest,
    ) -> ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse:
        """
        @summary Queries the peak QPS of DDoS attacks within the specific period of time.
        
        @param request: DescribeAttackAnalysisMaxQpsRequest
        @return: DescribeAttackAnalysisMaxQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_analysis_max_qps_with_options_async(request, runtime)

    def describe_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        """
        @summary Queries IP addresses in the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries IP addresses in the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries IP addresses in the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcBlacklistRequest
        @return: DescribeAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_blacklist_with_options(request, runtime)

    async def describe_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse:
        """
        @summary Queries IP addresses in the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcBlacklistRequest
        @return: DescribeAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_blacklist_with_options_async(request, runtime)

    def describe_auto_cc_list_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        """
        @summary Queries the numbers of IP addresses in the IP address whitelist and IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcListCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcListCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcListCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the numbers of IP addresses in the IP address whitelist and IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcListCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcListCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcListCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the numbers of IP addresses in the IP address whitelist and IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcListCountRequest
        @return: DescribeAutoCcListCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_list_count_with_options(request, runtime)

    async def describe_auto_cc_list_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcListCountRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcListCountResponse:
        """
        @summary Queries the numbers of IP addresses in the IP address whitelist and IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcListCountRequest
        @return: DescribeAutoCcListCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_list_count_with_options_async(request, runtime)

    def describe_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        """
        @summary Queries IP addresses in the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries IP addresses in the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries IP addresses in the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcWhitelistRequest
        @return: DescribeAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_whitelist_with_options(request, runtime)

    async def describe_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.DescribeAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse:
        """
        @summary Queries IP addresses in the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeAutoCcWhitelistRequest
        @return: DescribeAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_cc_whitelist_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeBackSourceCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackSourceCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the back-to-origin CIDR blocks of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeBackSourceCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackSourceCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the back-to-origin CIDR blocks of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeBackSourceCidrRequest
        @return: DescribeBackSourceCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddoscoo_20200101_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20200101_models.DescribeBackSourceCidrResponse:
        """
        @summary Queries the back-to-origin CIDR blocks of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeBackSourceCidrRequest
        @return: DescribeBackSourceCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def describe_blackhole_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        """
        @summary Queries the blackhole filtering status of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribeBlackholeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlackholeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the blackhole filtering status of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribeBlackholeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlackholeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the blackhole filtering status of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribeBlackholeStatusRequest
        @return: DescribeBlackholeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_blackhole_status_with_options(request, runtime)

    async def describe_blackhole_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlackholeStatusResponse:
        """
        @summary Queries the blackhole filtering status of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribeBlackholeStatusRequest
        @return: DescribeBlackholeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_blackhole_status_with_options_async(request, runtime)

    def describe_block_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        """
        @summary Queries the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call this operation to query the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBlockStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlockStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call this operation to query the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBlockStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlockStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call this operation to query the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBlockStatusRequest
        @return: DescribeBlockStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_block_status_with_options(request, runtime)

    async def describe_block_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeBlockStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeBlockStatusResponse:
        """
        @summary Queries the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        
        @description You can call this operation to query the Diversion from Origin Server configurations of one or more Anti-DDoS Proxy (Chinese Mainland) instances.
        >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBlockStatusRequest
        @return: DescribeBlockStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_block_status_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        """
        @summary Queries information about all certificates that can be associated with the current domain name instead of the certificate currently in use. To query the information about the certificate that is currently in use, you can call the DescribeWebRules operation and view the values of the CertName and CertRegion response parameters.
        
        @param request: DescribeCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries information about all certificates that can be associated with the current domain name instead of the certificate currently in use. To query the information about the certificate that is currently in use, you can call the DescribeWebRules operation and view the values of the CertName and CertRegion response parameters.
        
        @param request: DescribeCertsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries information about all certificates that can be associated with the current domain name instead of the certificate currently in use. To query the information about the certificate that is currently in use, you can call the DescribeWebRules operation and view the values of the CertName and CertRegion response parameters.
        
        @param request: DescribeCertsRequest
        @return: DescribeCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: ddoscoo_20200101_models.DescribeCertsRequest,
    ) -> ddoscoo_20200101_models.DescribeCertsResponse:
        """
        @summary Queries information about all certificates that can be associated with the current domain name instead of the certificate currently in use. To query the information about the certificate that is currently in use, you can call the DescribeWebRules operation and view the values of the CertName and CertRegion response parameters.
        
        @param request: DescribeCertsRequest
        @return: DescribeCertsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_cname_reuses_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        """
        @param request: DescribeCnameReusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCnameReusesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCnameReuses',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: DescribeCnameReusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCnameReusesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCnameReuses',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: DescribeCnameReusesRequest
        @return: DescribeCnameReusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cname_reuses_with_options(request, runtime)

    async def describe_cname_reuses_async(
        self,
        request: ddoscoo_20200101_models.DescribeCnameReusesRequest,
    ) -> ddoscoo_20200101_models.DescribeCnameReusesResponse:
        """
        @param request: DescribeCnameReusesRequest
        @return: DescribeCnameReusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cname_reuses_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        """
        @summary Queries the attack events launched against one or more Anti-DDoS Proxy instances.
        
        @param request: DescribeDDoSEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack events launched against one or more Anti-DDoS Proxy instances.
        
        @param request: DescribeDDoSEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack events launched against one or more Anti-DDoS Proxy instances.
        
        @param request: DescribeDDoSEventsRequest
        @return: DescribeDDoSEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDDoSEventsResponse:
        """
        @summary Queries the attack events launched against one or more Anti-DDoS Proxy instances.
        
        @param request: DescribeDDoSEventsRequest
        @return: DescribeDDoSEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def describe_ddos_all_event_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        """
        @summary Query DDoS attacks by IP address.
        
        @description You can call the DescribeDDosAllEventList operation to query DDoS attack events within a specific time range by page. The information about a DDoS attack event includes the start time and end time of the attack, attack event type, attacked object, peak bandwidth of attack traffic, and peak packet forwarding rate.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDDosAllEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosAllEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosAllEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Query DDoS attacks by IP address.
        
        @description You can call the DescribeDDosAllEventList operation to query DDoS attack events within a specific time range by page. The information about a DDoS attack event includes the start time and end time of the attack, attack event type, attacked object, peak bandwidth of attack traffic, and peak packet forwarding rate.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDDosAllEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosAllEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosAllEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Query DDoS attacks by IP address.
        
        @description You can call the DescribeDDosAllEventList operation to query DDoS attack events within a specific time range by page. The information about a DDoS attack event includes the start time and end time of the attack, attack event type, attacked object, peak bandwidth of attack traffic, and peak packet forwarding rate.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDDosAllEventListRequest
        @return: DescribeDDosAllEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    async def describe_ddos_all_event_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosAllEventListRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosAllEventListResponse:
        """
        @summary Query DDoS attacks by IP address.
        
        @description You can call the DescribeDDosAllEventList operation to query DDoS attack events within a specific time range by page. The information about a DDoS attack event includes the start time and end time of the attack, attack event type, attacked object, peak bandwidth of attack traffic, and peak packet forwarding rate.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDDosAllEventListRequest
        @return: DescribeDDosAllEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_all_event_list_with_options_async(request, runtime)

    def describe_ddos_event_area_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        """
        @summary Queries the source region from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAreaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventAreaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventArea',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the source region from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAreaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventAreaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventArea',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the source region from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAreaRequest
        @return: DescribeDDosEventAreaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_area_with_options(request, runtime)

    async def describe_ddos_event_area_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAreaRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAreaResponse:
        """
        @summary Queries the source region from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAreaRequest
        @return: DescribeDDosEventAreaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_area_with_options_async(request, runtime)

    def describe_ddos_event_attack_type_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        """
        @summary Queries the attack type details of a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAttackTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventAttackTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventAttackType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack type details of a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAttackTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventAttackTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventAttackType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack type details of a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAttackTypeRequest
        @return: DescribeDDosEventAttackTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_attack_type_with_options(request, runtime)

    async def describe_ddos_event_attack_type_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventAttackTypeRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse:
        """
        @summary Queries the attack type details of a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventAttackTypeRequest
        @return: DescribeDDosEventAttackTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_attack_type_with_options_async(request, runtime)

    def describe_ddos_event_isp_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        """
        @summary Queries the Internet service provider (ISP) information about a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventIspResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventIsp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Internet service provider (ISP) information about a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventIspResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventIsp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Internet service provider (ISP) information about a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventIspRequest
        @return: DescribeDDosEventIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_isp_with_options(request, runtime)

    async def describe_ddos_event_isp_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventIspRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventIspResponse:
        """
        @summary Queries the Internet service provider (ISP) information about a volumetric attack.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventIspRequest
        @return: DescribeDDosEventIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_isp_with_options_async(request, runtime)

    def describe_ddos_event_max_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        """
        @summary Queries the peaks of volumetric attacks (bit/s), connection flood attacks (CPS), and resource exhaustion attacks on websites (QPS).
        
        @param request: DescribeDDosEventMaxRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventMaxResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventMax',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peaks of volumetric attacks (bit/s), connection flood attacks (CPS), and resource exhaustion attacks on websites (QPS).
        
        @param request: DescribeDDosEventMaxRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventMaxResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventMax',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peaks of volumetric attacks (bit/s), connection flood attacks (CPS), and resource exhaustion attacks on websites (QPS).
        
        @param request: DescribeDDosEventMaxRequest
        @return: DescribeDDosEventMaxResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_max_with_options(request, runtime)

    async def describe_ddos_event_max_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventMaxRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventMaxResponse:
        """
        @summary Queries the peaks of volumetric attacks (bit/s), connection flood attacks (CPS), and resource exhaustion attacks on websites (QPS).
        
        @param request: DescribeDDosEventMaxRequest
        @return: DescribeDDosEventMaxResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_max_with_options_async(request, runtime)

    def describe_ddos_event_src_ip_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        """
        @summary Queries the source IP address from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventSrcIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventSrcIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventSrcIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the source IP address from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventSrcIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDosEventSrcIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventSrcIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the source IP address from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventSrcIpRequest
        @return: DescribeDDosEventSrcIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_src_ip_with_options(request, runtime)

    async def describe_ddos_event_src_ip_async(
        self,
        request: ddoscoo_20200101_models.DescribeDDosEventSrcIpRequest,
    ) -> ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse:
        """
        @summary Queries the source IP address from which a volumetric attack is initiated.
        
        @description > This operation is suitable only for volumetric attacks.
        
        @param request: DescribeDDosEventSrcIpRequest
        @return: DescribeDDosEventSrcIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_src_ip_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        """
        @summary Queries the statistics on advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance.
        
        @description You can call the DescribeDefenseCountStatistics operation to query the information about advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance. For example, you can query the number of advanced mitigation sessions that are used within the current calendar month and the number of remaining advanced mitigation sessions.
        >  This operation is suitable only for Anti-DDoS Proxy (Outside Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDefenseCountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseCountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance.
        
        @description You can call the DescribeDefenseCountStatistics operation to query the information about advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance. For example, you can query the number of advanced mitigation sessions that are used within the current calendar month and the number of remaining advanced mitigation sessions.
        >  This operation is suitable only for Anti-DDoS Proxy (Outside Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDefenseCountStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseCountStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance.
        
        @description You can call the DescribeDefenseCountStatistics operation to query the information about advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance. For example, you can query the number of advanced mitigation sessions that are used within the current calendar month and the number of remaining advanced mitigation sessions.
        >  This operation is suitable only for Anti-DDoS Proxy (Outside Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDefenseCountStatisticsRequest
        @return: DescribeDefenseCountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse:
        """
        @summary Queries the statistics on advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance.
        
        @description You can call the DescribeDefenseCountStatistics operation to query the information about advanced mitigation sessions of an Anti-DDoS Proxy (Outside Chinese Mainland) instance. For example, you can query the number of advanced mitigation sessions that are used within the current calendar month and the number of remaining advanced mitigation sessions.
        >  This operation is suitable only for Anti-DDoS Proxy (Outside Chinese Mainland).
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDefenseCountStatisticsRequest
        @return: DescribeDefenseCountStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def describe_defense_records_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        """
        @summary Queries the advanced mitigation logs of Anti-DDoS Premium.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: DescribeDefenseRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRecords',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the advanced mitigation logs of Anti-DDoS Premium.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: DescribeDefenseRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefenseRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRecords',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the advanced mitigation logs of Anti-DDoS Premium.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: DescribeDefenseRecordsRequest
        @return: DescribeDefenseRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_records_with_options(request, runtime)

    async def describe_defense_records_async(
        self,
        request: ddoscoo_20200101_models.DescribeDefenseRecordsRequest,
    ) -> ddoscoo_20200101_models.DescribeDefenseRecordsResponse:
        """
        @summary Queries the advanced mitigation logs of Anti-DDoS Premium.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: DescribeDefenseRecordsRequest
        @return: DescribeDefenseRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_records_with_options_async(request, runtime)

    def describe_destination_port_event_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDestinationPortEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDestinationPortEventResponse:
        """
        @summary Queries the number of request packets received by the destination ports of the attacked IP address that is protected by Anti-DDoS Proxy.
        
        @param request: DescribeDestinationPortEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDestinationPortEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDestinationPortEvent',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDestinationPortEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_destination_port_event_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDestinationPortEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDestinationPortEventResponse:
        """
        @summary Queries the number of request packets received by the destination ports of the attacked IP address that is protected by Anti-DDoS Proxy.
        
        @param request: DescribeDestinationPortEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDestinationPortEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDestinationPortEvent',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDestinationPortEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_destination_port_event(
        self,
        request: ddoscoo_20200101_models.DescribeDestinationPortEventRequest,
    ) -> ddoscoo_20200101_models.DescribeDestinationPortEventResponse:
        """
        @summary Queries the number of request packets received by the destination ports of the attacked IP address that is protected by Anti-DDoS Proxy.
        
        @param request: DescribeDestinationPortEventRequest
        @return: DescribeDestinationPortEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_destination_port_event_with_options(request, runtime)

    async def describe_destination_port_event_async(
        self,
        request: ddoscoo_20200101_models.DescribeDestinationPortEventRequest,
    ) -> ddoscoo_20200101_models.DescribeDestinationPortEventResponse:
        """
        @summary Queries the number of request packets received by the destination ports of the attacked IP address that is protected by Anti-DDoS Proxy.
        
        @param request: DescribeDestinationPortEventRequest
        @return: DescribeDestinationPortEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_destination_port_event_with_options_async(request, runtime)

    def describe_domain_attack_events_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        """
        @summary Queries the attack events launched against a website.
        
        @param request: DescribeDomainAttackEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack events launched against a website.
        
        @param request: DescribeDomainAttackEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAttackEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack events launched against a website.
        
        @param request: DescribeDomainAttackEventsRequest
        @return: DescribeDomainAttackEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    async def describe_domain_attack_events_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainAttackEventsResponse:
        """
        @summary Queries the attack events launched against a website.
        
        @param request: DescribeDomainAttackEventsRequest
        @return: DescribeDomainAttackEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_events_with_options_async(request, runtime)

    def describe_domain_overview_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        """
        @summary Queries the attack overview of a website, such as the peak HTTP and HTTPS traffic.
        
        @param request: DescribeDomainOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack overview of a website, such as the peak HTTP and HTTPS traffic.
        
        @param request: DescribeDomainOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the attack overview of a website, such as the peak HTTP and HTTPS traffic.
        
        @param request: DescribeDomainOverviewRequest
        @return: DescribeDomainOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    async def describe_domain_overview_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainOverviewRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainOverviewResponse:
        """
        @summary Queries the attack overview of a website, such as the peak HTTP and HTTPS traffic.
        
        @param request: DescribeDomainOverviewRequest
        @return: DescribeDomainOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_overview_with_options_async(request, runtime)

    def describe_domain_qpslist_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        """
        @summary Queries the statistics on the queries per second (QPS) of a website.
        
        @param request: DescribeDomainQPSListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQPSListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQPSList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on the queries per second (QPS) of a website.
        
        @param request: DescribeDomainQPSListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQPSListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQPSList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on the queries per second (QPS) of a website.
        
        @param request: DescribeDomainQPSListRequest
        @return: DescribeDomainQPSListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qpslist_with_options(request, runtime)

    async def describe_domain_qpslist_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainQPSListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainQPSListResponse:
        """
        @summary Queries the statistics on the queries per second (QPS) of a website.
        
        @param request: DescribeDomainQPSListRequest
        @return: DescribeDomainQPSListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qpslist_with_options_async(request, runtime)

    def describe_domain_resource_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainResourceResponse:
        """
        @summary Queries the configurations of a forwarding rule.
        
        @description You can call the DescribeDomainResource operation to query the configurations of the forwarding rules that you create for a website by page. The configurations include the domain name-related configurations, protocol-related configurations, HTTPS-related configurations, and configurations that are used to mitigate HTTP flood attacks.
        You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        ### Limits
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resource_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainResourceResponse:
        """
        @summary Queries the configurations of a forwarding rule.
        
        @description You can call the DescribeDomainResource operation to query the configurations of the forwarding rules that you create for a website by page. The configurations include the domain name-related configurations, protocol-related configurations, HTTPS-related configurations, and configurations that are used to mitigate HTTP flood attacks.
        You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        ### Limits
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resource(
        self,
        request: ddoscoo_20200101_models.DescribeDomainResourceRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainResourceResponse:
        """
        @summary Queries the configurations of a forwarding rule.
        
        @description You can call the DescribeDomainResource operation to query the configurations of the forwarding rules that you create for a website by page. The configurations include the domain name-related configurations, protocol-related configurations, HTTPS-related configurations, and configurations that are used to mitigate HTTP flood attacks.
        You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        ### Limits
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResourceRequest
        @return: DescribeDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resource_with_options(request, runtime)

    async def describe_domain_resource_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainResourceRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainResourceResponse:
        """
        @summary Queries the configurations of a forwarding rule.
        
        @description You can call the DescribeDomainResource operation to query the configurations of the forwarding rules that you create for a website by page. The configurations include the domain name-related configurations, protocol-related configurations, HTTPS-related configurations, and configurations that are used to mitigate HTTP flood attacks.
        You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        ### Limits
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResourceRequest
        @return: DescribeDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resource_with_options_async(request, runtime)

    def describe_domain_security_profile_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainSecurityProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse:
        """
        @summary Queries the global mitigation policy for a domain name.
        
        @param request: DescribeDomainSecurityProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSecurityProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSecurityProfile',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_security_profile_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainSecurityProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse:
        """
        @summary Queries the global mitigation policy for a domain name.
        
        @param request: DescribeDomainSecurityProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSecurityProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSecurityProfile',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_security_profile(
        self,
        request: ddoscoo_20200101_models.DescribeDomainSecurityProfileRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse:
        """
        @summary Queries the global mitigation policy for a domain name.
        
        @param request: DescribeDomainSecurityProfileRequest
        @return: DescribeDomainSecurityProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_security_profile_with_options(request, runtime)

    async def describe_domain_security_profile_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainSecurityProfileRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainSecurityProfileResponse:
        """
        @summary Queries the global mitigation policy for a domain name.
        
        @param request: DescribeDomainSecurityProfileRequest
        @return: DescribeDomainSecurityProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_security_profile_with_options_async(request, runtime)

    def describe_domain_status_code_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        """
        @summary Queries the statistics on HTTP status codes of a website within a specified period of time.
        
        @param request: DescribeDomainStatusCodeCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on HTTP status codes of a website within a specified period of time.
        
        @param request: DescribeDomainStatusCodeCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on HTTP status codes of a website within a specified period of time.
        
        @param request: DescribeDomainStatusCodeCountRequest
        @return: DescribeDomainStatusCodeCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_count_with_options(request, runtime)

    async def describe_domain_status_code_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse:
        """
        @summary Queries the statistics on HTTP status codes of a website within a specified period of time.
        
        @param request: DescribeDomainStatusCodeCountRequest
        @return: DescribeDomainStatusCodeCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_status_code_count_with_options_async(request, runtime)

    def describe_domain_status_code_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        """
        @summary Queries the statistics on HTTP status codes of a website.
        
        @param request: DescribeDomainStatusCodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on HTTP status codes of a website.
        
        @param request: DescribeDomainStatusCodeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainStatusCodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on HTTP status codes of a website.
        
        @param request: DescribeDomainStatusCodeListRequest
        @return: DescribeDomainStatusCodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    async def describe_domain_status_code_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainStatusCodeListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse:
        """
        @summary Queries the statistics on HTTP status codes of a website.
        
        @param request: DescribeDomainStatusCodeListRequest
        @return: DescribeDomainStatusCodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_status_code_list_with_options_async(request, runtime)

    def describe_domain_top_attack_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        """
        @summary Queries the peak queries per second (QPS) information about a website, such as the attack QPS and total QPS, within a specific period of time.
        
        @param request: DescribeDomainTopAttackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopAttackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopAttackList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peak queries per second (QPS) information about a website, such as the attack QPS and total QPS, within a specific period of time.
        
        @param request: DescribeDomainTopAttackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopAttackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopAttackList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peak queries per second (QPS) information about a website, such as the attack QPS and total QPS, within a specific period of time.
        
        @param request: DescribeDomainTopAttackListRequest
        @return: DescribeDomainTopAttackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_attack_list_with_options(request, runtime)

    async def describe_domain_top_attack_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainTopAttackListRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainTopAttackListResponse:
        """
        @summary Queries the peak queries per second (QPS) information about a website, such as the attack QPS and total QPS, within a specific period of time.
        
        @param request: DescribeDomainTopAttackListRequest
        @return: DescribeDomainTopAttackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_attack_list_with_options_async(request, runtime)

    def describe_domain_view_source_countries_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        """
        @summary Queries the areas and countries from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceCountriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewSourceCountriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the areas and countries from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceCountriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewSourceCountriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the areas and countries from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceCountriesRequest
        @return: DescribeDomainViewSourceCountriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_countries_with_options(request, runtime)

    async def describe_domain_view_source_countries_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse:
        """
        @summary Queries the areas and countries from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceCountriesRequest
        @return: DescribeDomainViewSourceCountriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_source_countries_with_options_async(request, runtime)

    def describe_domain_view_source_provinces_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        """
        @summary Queries the administrative regions in China from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceProvincesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewSourceProvincesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the administrative regions in China from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceProvincesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewSourceProvincesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the administrative regions in China from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceProvincesRequest
        @return: DescribeDomainViewSourceProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_provinces_with_options(request, runtime)

    async def describe_domain_view_source_provinces_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse:
        """
        @summary Queries the administrative regions in China from which requests are sent to a website within a specified period of time.
        
        @param request: DescribeDomainViewSourceProvincesRequest
        @return: DescribeDomainViewSourceProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_source_provinces_with_options_async(request, runtime)

    def describe_domain_view_top_cost_time_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        """
        @summary Queries the top N URLs that require the longest time to respond to requests within a specified period of time.
        
        @param request: DescribeDomainViewTopCostTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewTopCostTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopCostTime',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the top N URLs that require the longest time to respond to requests within a specified period of time.
        
        @param request: DescribeDomainViewTopCostTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewTopCostTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopCostTime',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the top N URLs that require the longest time to respond to requests within a specified period of time.
        
        @param request: DescribeDomainViewTopCostTimeRequest
        @return: DescribeDomainViewTopCostTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_cost_time_with_options(request, runtime)

    async def describe_domain_view_top_cost_time_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopCostTimeRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse:
        """
        @summary Queries the top N URLs that require the longest time to respond to requests within a specified period of time.
        
        @param request: DescribeDomainViewTopCostTimeRequest
        @return: DescribeDomainViewTopCostTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_top_cost_time_with_options_async(request, runtime)

    def describe_domain_view_top_url_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        """
        @summary Queries the top N URLs that receive the most requests within a specified period of time.
        
        @param request: DescribeDomainViewTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the top N URLs that receive the most requests within a specified period of time.
        
        @param request: DescribeDomainViewTopUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainViewTopUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the top N URLs that receive the most requests within a specified period of time.
        
        @param request: DescribeDomainViewTopUrlRequest
        @return: DescribeDomainViewTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_url_with_options(request, runtime)

    async def describe_domain_view_top_url_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainViewTopUrlRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse:
        """
        @summary Queries the top N URLs that receive the most requests within a specified period of time.
        
        @param request: DescribeDomainViewTopUrlRequest
        @return: DescribeDomainViewTopUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_view_top_url_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        """
        @summary Queries domain names for which forwarding rules are created.
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries domain names for which forwarding rules are created.
        
        @param request: DescribeDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries domain names for which forwarding rules are created.
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: ddoscoo_20200101_models.DescribeDomainsRequest,
    ) -> ddoscoo_20200101_models.DescribeDomainsResponse:
        """
        @summary Queries domain names for which forwarding rules are created.
        
        @param request: DescribeDomainsRequest
        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        """
        @summary Queries the available burstable protection bandwidths of an Anti-DDoS Pro instance.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeElasticBandwidthSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticBandwidthSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the available burstable protection bandwidths of an Anti-DDoS Pro instance.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeElasticBandwidthSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticBandwidthSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the available burstable protection bandwidths of an Anti-DDoS Pro instance.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeElasticBandwidthSpecRequest
        @return: DescribeElasticBandwidthSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse:
        """
        @summary Queries the available burstable protection bandwidths of an Anti-DDoS Pro instance.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeElasticBandwidthSpecRequest
        @return: DescribeElasticBandwidthSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_elastic_qps_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsResponse:
        """
        @summary Queries the line chart of the bills for the burstable QPS of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_qps_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsResponse:
        """
        @summary Queries the line chart of the bills for the burstable QPS of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_qps(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsResponse:
        """
        @summary Queries the line chart of the bills for the burstable QPS of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRequest
        @return: DescribeElasticQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_qps_with_options(request, runtime)

    async def describe_elastic_qps_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsResponse:
        """
        @summary Queries the line chart of the bills for the burstable QPS of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRequest
        @return: DescribeElasticQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_qps_with_options_async(request, runtime)

    def describe_elastic_qps_record_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsRecordResponse:
        """
        @summary Queries the burstable QPS details of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticQpsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticQpsRecord',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticQpsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_qps_record_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsRecordResponse:
        """
        @summary Queries the burstable QPS details of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticQpsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticQpsRecord',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticQpsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_qps_record(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRecordRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsRecordResponse:
        """
        @summary Queries the burstable QPS details of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRecordRequest
        @return: DescribeElasticQpsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_qps_record_with_options(request, runtime)

    async def describe_elastic_qps_record_async(
        self,
        request: ddoscoo_20200101_models.DescribeElasticQpsRecordRequest,
    ) -> ddoscoo_20200101_models.DescribeElasticQpsRecordResponse:
        """
        @summary Queries the burstable QPS details of an Anti-DDoS Proxy instance.
        
        @param request: DescribeElasticQpsRecordRequest
        @return: DescribeElasticQpsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_qps_record_with_options_async(request, runtime)

    def describe_headers_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeHeadersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHeadersResponse:
        """
        @summary Queries the custom header that is specified for a domain name.
        
        @param request: DescribeHeadersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHeadersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHeaders',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_headers_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeHeadersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHeadersResponse:
        """
        @summary Queries the custom header that is specified for a domain name.
        
        @param request: DescribeHeadersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHeadersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHeaders',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHeadersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_headers(
        self,
        request: ddoscoo_20200101_models.DescribeHeadersRequest,
    ) -> ddoscoo_20200101_models.DescribeHeadersResponse:
        """
        @summary Queries the custom header that is specified for a domain name.
        
        @param request: DescribeHeadersRequest
        @return: DescribeHeadersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_headers_with_options(request, runtime)

    async def describe_headers_async(
        self,
        request: ddoscoo_20200101_models.DescribeHeadersRequest,
    ) -> ddoscoo_20200101_models.DescribeHeadersResponse:
        """
        @summary Queries the custom header that is specified for a domain name.
        
        @param request: DescribeHeadersRequest
        @return: DescribeHeadersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_headers_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        """
        @summary Queries the Layer 4 or Layer 7 health check configurations of a port forwarding rule.
        
        @param request: DescribeHealthCheckListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Layer 4 or Layer 7 health check configurations of a port forwarding rule.
        
        @param request: DescribeHealthCheckListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Layer 4 or Layer 7 health check configurations of a port forwarding rule.
        
        @param request: DescribeHealthCheckListRequest
        @return: DescribeHealthCheckListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckListResponse:
        """
        @summary Queries the Layer 4 or Layer 7 health check configurations of a port forwarding rule.
        
        @param request: DescribeHealthCheckListRequest
        @return: DescribeHealthCheckListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_health_check_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        """
        @summary Queries the health status of an origin server.
        
        @param request: DescribeHealthCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the health status of an origin server.
        
        @param request: DescribeHealthCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the health status of an origin server.
        
        @param request: DescribeHealthCheckStatusRequest
        @return: DescribeHealthCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_with_options(request, runtime)

    async def describe_health_check_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeHealthCheckStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeHealthCheckStatusResponse:
        """
        @summary Queries the health status of an origin server.
        
        @param request: DescribeHealthCheckStatusRequest
        @return: DescribeHealthCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_status_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        """
        @summary Queries the IP addresses and Internet service provider (ISP) lines of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceDetails operation to query the information about the IP addresses and ISP lines of the instances. The information includes the IP address, status, and protection line.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the IP addresses and Internet service provider (ISP) lines of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceDetails operation to query the information about the IP addresses and ISP lines of the instances. The information includes the IP address, status, and protection line.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the IP addresses and Internet service provider (ISP) lines of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceDetails operation to query the information about the IP addresses and ISP lines of the instances. The information includes the IP address, status, and protection line.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceDetailsRequest
        @return: DescribeInstanceDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceDetailsResponse:
        """
        @summary Queries the IP addresses and Internet service provider (ISP) lines of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceDetails operation to query the information about the IP addresses and ISP lines of the instances. The information includes the IP address, status, and protection line.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceDetailsRequest
        @return: DescribeInstanceDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_instance_ext_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceExtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceExtResponse:
        """
        @summary Queries the information about Anti-DDoS Pro and Anti-DDoS Premium instances.
        
        @param request: DescribeInstanceExtRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceExtResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceExt',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceExtResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ext_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceExtRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceExtResponse:
        """
        @summary Queries the information about Anti-DDoS Pro and Anti-DDoS Premium instances.
        
        @param request: DescribeInstanceExtRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceExtResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceExt',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceExtResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ext(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceExtRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceExtResponse:
        """
        @summary Queries the information about Anti-DDoS Pro and Anti-DDoS Premium instances.
        
        @param request: DescribeInstanceExtRequest
        @return: DescribeInstanceExtResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ext_with_options(request, runtime)

    async def describe_instance_ext_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceExtRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceExtResponse:
        """
        @summary Queries the information about Anti-DDoS Pro and Anti-DDoS Premium instances.
        
        @param request: DescribeInstanceExtRequest
        @return: DescribeInstanceExtResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ext_with_options_async(request, runtime)

    def describe_instance_ids_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        """
        @summary The description of the instance.
        
        @param request: DescribeInstanceIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIds',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The description of the instance.
        
        @param request: DescribeInstanceIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIds',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The description of the instance.
        
        @param request: DescribeInstanceIdsRequest
        @return: DescribeInstanceIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ids_with_options(request, runtime)

    async def describe_instance_ids_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceIdsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceIdsResponse:
        """
        @summary The description of the instance.
        
        @param request: DescribeInstanceIdsRequest
        @return: DescribeInstanceIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ids_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        """
        @summary Queries the specifications of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceSpecs operation to query the specifications of multiple Anti-DDoS Pro or Anti-DDoS Premium instances at a time. The specifications include the clean bandwidth, protection bandwidth, function plan, and the numbers of domain names and ports that can be protected.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the specifications of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceSpecs operation to query the specifications of multiple Anti-DDoS Pro or Anti-DDoS Premium instances at a time. The specifications include the clean bandwidth, protection bandwidth, function plan, and the numbers of domain names and ports that can be protected.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the specifications of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceSpecs operation to query the specifications of multiple Anti-DDoS Pro or Anti-DDoS Premium instances at a time. The specifications include the clean bandwidth, protection bandwidth, function plan, and the numbers of domain names and ports that can be protected.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceSpecsResponse:
        """
        @summary Queries the specifications of Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @description You can call the DescribeInstanceSpecs operation to query the specifications of multiple Anti-DDoS Pro or Anti-DDoS Premium instances at a time. The specifications include the clean bandwidth, protection bandwidth, function plan, and the numbers of domain names and ports that can be protected.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        """
        @summary Queries the statistics on one or more Anti-DDoS Proxy instances, such as the numbers of protected domain names and ports.
        
        @param request: DescribeInstanceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on one or more Anti-DDoS Proxy instances, such as the numbers of protected domain names and ports.
        
        @param request: DescribeInstanceStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the statistics on one or more Anti-DDoS Proxy instances, such as the numbers of protected domain names and ports.
        
        @param request: DescribeInstanceStatisticsRequest
        @return: DescribeInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatisticsResponse:
        """
        @summary Queries the statistics on one or more Anti-DDoS Proxy instances, such as the numbers of protected domain names and ports.
        
        @param request: DescribeInstanceStatisticsRequest
        @return: DescribeInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instance_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        """
        @summary Queries the status of a specified Anti-DDoS Proxy instance.
        
        @param request: DescribeInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status of a specified Anti-DDoS Proxy instance.
        
        @param request: DescribeInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status of a specified Anti-DDoS Proxy instance.
        
        @param request: DescribeInstanceStatusRequest
        @return: DescribeInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    async def describe_instance_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstanceStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeInstanceStatusResponse:
        """
        @summary Queries the status of a specified Anti-DDoS Proxy instance.
        
        @param request: DescribeInstanceStatusRequest
        @return: DescribeInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_status_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        """
        @description You can call the DescribeInstances operation to query the details of Anti-DDoS Pro or Anti-DDoS Premium instances within the Alibaba Cloud account by page. The details include the ID, mitigation plan, expiration time, and forwarding status.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not UtilClient.is_unset(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @description You can call the DescribeInstances operation to query the details of Anti-DDoS Pro or Anti-DDoS Premium instances within the Alibaba Cloud account by page. The details include the ID, mitigation plan, expiration time, and forwarding status.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not UtilClient.is_unset(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @description You can call the DescribeInstances operation to query the details of Anti-DDoS Pro or Anti-DDoS Premium instances within the Alibaba Cloud account by page. The details include the ID, mitigation plan, expiration time, and forwarding status.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ddoscoo_20200101_models.DescribeInstancesRequest,
    ) -> ddoscoo_20200101_models.DescribeInstancesResponse:
        """
        @description You can call the DescribeInstances operation to query the details of Anti-DDoS Pro or Anti-DDoS Premium instances within the Alibaba Cloud account by page. The details include the ID, mitigation plan, expiration time, and forwarding status.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_l7rs_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        """
        @summary Queries the back-to-origin policies for the forwarding rule of a website.
        
        @param request: DescribeL7RsPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL7RsPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the back-to-origin policies for the forwarding rule of a website.
        
        @param request: DescribeL7RsPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL7RsPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the back-to-origin policies for the forwarding rule of a website.
        
        @param request: DescribeL7RsPolicyRequest
        @return: DescribeL7RsPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_l7rs_policy_with_options(request, runtime)

    async def describe_l7rs_policy_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7RsPolicyRequest,
    ) -> ddoscoo_20200101_models.DescribeL7RsPolicyResponse:
        """
        @summary Queries the back-to-origin policies for the forwarding rule of a website.
        
        @param request: DescribeL7RsPolicyRequest
        @return: DescribeL7RsPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_l7rs_policy_with_options_async(request, runtime)

    def describe_l7us_keepalive_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeL7UsKeepaliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse:
        """
        @summary Queries the configuration of back-to-origin persistent connections of a domain name.
        
        @param request: DescribeL7UsKeepaliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL7UsKeepaliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeL7UsKeepalive',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l7us_keepalive_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7UsKeepaliveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse:
        """
        @summary Queries the configuration of back-to-origin persistent connections of a domain name.
        
        @param request: DescribeL7UsKeepaliveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL7UsKeepaliveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeL7UsKeepalive',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l7us_keepalive(
        self,
        request: ddoscoo_20200101_models.DescribeL7UsKeepaliveRequest,
    ) -> ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse:
        """
        @summary Queries the configuration of back-to-origin persistent connections of a domain name.
        
        @param request: DescribeL7UsKeepaliveRequest
        @return: DescribeL7UsKeepaliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_l7us_keepalive_with_options(request, runtime)

    async def describe_l7us_keepalive_async(
        self,
        request: ddoscoo_20200101_models.DescribeL7UsKeepaliveRequest,
    ) -> ddoscoo_20200101_models.DescribeL7UsKeepaliveResponse:
        """
        @summary Queries the configuration of back-to-origin persistent connections of a domain name.
        
        @param request: DescribeL7UsKeepaliveRequest
        @return: DescribeL7UsKeepaliveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_l7us_keepalive_with_options_async(request, runtime)

    def describe_layer_4rule_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeLayer4RulePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse:
        """
        @summary Queries the back-to-origin settings of a port forwarding rule.
        
        @param request: DescribeLayer4RulePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RulePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_layer_4rule_policy_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeLayer4RulePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse:
        """
        @summary Queries the back-to-origin settings of a port forwarding rule.
        
        @param request: DescribeLayer4RulePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLayer4RulePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_layer_4rule_policy(
        self,
        request: ddoscoo_20200101_models.DescribeLayer4RulePolicyRequest,
    ) -> ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse:
        """
        @summary Queries the back-to-origin settings of a port forwarding rule.
        
        @param request: DescribeLayer4RulePolicyRequest
        @return: DescribeLayer4RulePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_policy_with_options(request, runtime)

    async def describe_layer_4rule_policy_async(
        self,
        request: ddoscoo_20200101_models.DescribeLayer4RulePolicyRequest,
    ) -> ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse:
        """
        @summary Queries the back-to-origin settings of a port forwarding rule.
        
        @param request: DescribeLayer4RulePolicyRequest
        @return: DescribeLayer4RulePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rule_policy_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        """
        @summary Checks whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeLogStoreExistStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreExistStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeLogStoreExistStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogStoreExistStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeLogStoreExistStatusRequest
        @return: DescribeLogStoreExistStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse:
        """
        @summary Checks whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeLogStoreExistStatusRequest
        @return: DescribeLogStoreExistStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_network_region_block_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        """
        @summary Queries the blocked locations that are configured for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeNetworkRegionBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRegionBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the blocked locations that are configured for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeNetworkRegionBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRegionBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the blocked locations that are configured for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeNetworkRegionBlockRequest
        @return: DescribeNetworkRegionBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_network_region_block_with_options(request, runtime)

    async def describe_network_region_block_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRegionBlockRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse:
        """
        @summary Queries the blocked locations that are configured for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeNetworkRegionBlockRequest
        @return: DescribeNetworkRegionBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_region_block_with_options_async(request, runtime)

    def describe_network_rule_attributes_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        """
        @summary Queries the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        
        @param request: DescribeNetworkRuleAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRuleAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRuleAttributes',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        
        @param request: DescribeNetworkRuleAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRuleAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRuleAttributes',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        
        @param request: DescribeNetworkRuleAttributesRequest
        @return: DescribeNetworkRuleAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rule_attributes_with_options(request, runtime)

    async def describe_network_rule_attributes_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRuleAttributesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse:
        """
        @summary Queries the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        
        @param request: DescribeNetworkRuleAttributesRequest
        @return: DescribeNetworkRuleAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_rule_attributes_with_options_async(request, runtime)

    def describe_network_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        """
        @summary Queries port forwarding rules.
        
        @param request: DescribeNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries port forwarding rules.
        
        @param request: DescribeNetworkRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries port forwarding rules.
        
        @param request: DescribeNetworkRulesRequest
        @return: DescribeNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rules_with_options(request, runtime)

    async def describe_network_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeNetworkRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeNetworkRulesResponse:
        """
        @summary Queries port forwarding rules.
        
        @param request: DescribeNetworkRulesRequest
        @return: DescribeNetworkRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_rules_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        """
        @summary Queries the operation logs of Anti-DDoS Pro.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        You can query operations performed on Anti-DDoS Pro, such as configuring burstable protection bandwidth, deactivating blackhole filtering, configuring the Diversion from Origin Server policy, using Anti-DDoS plans, changing the IP addresses of Elastic Compute Service (ECS) instances, and clearing all logs.
        
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the operation logs of Anti-DDoS Pro.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        You can query operations performed on Anti-DDoS Pro, such as configuring burstable protection bandwidth, deactivating blackhole filtering, configuring the Diversion from Origin Server policy, using Anti-DDoS plans, changing the IP addresses of Elastic Compute Service (ECS) instances, and clearing all logs.
        
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the operation logs of Anti-DDoS Pro.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        You can query operations performed on Anti-DDoS Pro, such as configuring burstable protection bandwidth, deactivating blackhole filtering, configuring the Diversion from Origin Server policy, using Anti-DDoS plans, changing the IP addresses of Elastic Compute Service (ECS) instances, and clearing all logs.
        
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddoscoo_20200101_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20200101_models.DescribeOpEntitiesResponse:
        """
        @summary Queries the operation logs of Anti-DDoS Pro.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        You can query operations performed on Anti-DDoS Pro, such as configuring burstable protection bandwidth, deactivating blackhole filtering, configuring the Diversion from Origin Server policy, using Anti-DDoS plans, changing the IP addresses of Elastic Compute Service (ECS) instances, and clearing all logs.
        
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_port_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortResponse:
        """
        @summary Queries the port forwarding rules that are created for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DescribePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortResponse:
        """
        @summary Queries the port forwarding rules that are created for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DescribePortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port(
        self,
        request: ddoscoo_20200101_models.DescribePortRequest,
    ) -> ddoscoo_20200101_models.DescribePortResponse:
        """
        @summary Queries the port forwarding rules that are created for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DescribePortRequest
        @return: DescribePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_with_options(request, runtime)

    async def describe_port_async(
        self,
        request: ddoscoo_20200101_models.DescribePortRequest,
    ) -> ddoscoo_20200101_models.DescribePortResponse:
        """
        @summary Queries the port forwarding rules that are created for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description You can call this operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: DescribePortRequest
        @return: DescribePortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_with_options_async(request, runtime)

    def describe_port_attack_max_flow_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        """
        @summary Queries the peak attack traffic bandwidth and peak attack traffic packet rates of one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @description You can call this operation to query the peak bandwidth and peak packet rate of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortAttackMaxFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortAttackMaxFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peak attack traffic bandwidth and peak attack traffic packet rates of one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @description You can call this operation to query the peak bandwidth and peak packet rate of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortAttackMaxFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortAttackMaxFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the peak attack traffic bandwidth and peak attack traffic packet rates of one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @description You can call this operation to query the peak bandwidth and peak packet rate of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortAttackMaxFlowRequest
        @return: DescribePortAttackMaxFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_attack_max_flow_with_options(request, runtime)

    async def describe_port_attack_max_flow_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAttackMaxFlowRequest,
    ) -> ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse:
        """
        @summary Queries the peak attack traffic bandwidth and peak attack traffic packet rates of one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @description You can call this operation to query the peak bandwidth and peak packet rate of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortAttackMaxFlowRequest
        @return: DescribePortAttackMaxFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_attack_max_flow_with_options_async(request, runtime)

    def describe_port_auto_cc_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        """
        @summary Queries the configurations of the Intelligent Protection policy for non-website services.
        
        @param request: DescribePortAutoCcStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortAutoCcStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the configurations of the Intelligent Protection policy for non-website services.
        
        @param request: DescribePortAutoCcStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortAutoCcStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the configurations of the Intelligent Protection policy for non-website services.
        
        @param request: DescribePortAutoCcStatusRequest
        @return: DescribePortAutoCcStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_auto_cc_status_with_options(request, runtime)

    async def describe_port_auto_cc_status_async(
        self,
        request: ddoscoo_20200101_models.DescribePortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.DescribePortAutoCcStatusResponse:
        """
        @summary Queries the configurations of the Intelligent Protection policy for non-website services.
        
        @param request: DescribePortAutoCcStatusRequest
        @return: DescribePortAutoCcStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_auto_cc_status_with_options_async(request, runtime)

    def describe_port_cc_attack_top_ipwith_options(
        self,
        request: ddoscoo_20200101_models.DescribePortCcAttackTopIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse:
        """
        @summary Queries the top source IP addresses of the volumetric attack events for the Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribePortCcAttackTopIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortCcAttackTopIPResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortCcAttackTopIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_port_cc_attack_top_ipwith_options_async(
        self,
        request: ddoscoo_20200101_models.DescribePortCcAttackTopIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse:
        """
        @summary Queries the top source IP addresses of the volumetric attack events for the Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribePortCcAttackTopIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortCcAttackTopIPResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortCcAttackTopIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_port_cc_attack_top_ip(
        self,
        request: ddoscoo_20200101_models.DescribePortCcAttackTopIPRequest,
    ) -> ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse:
        """
        @summary Queries the top source IP addresses of the volumetric attack events for the Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribePortCcAttackTopIPRequest
        @return: DescribePortCcAttackTopIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_cc_attack_top_ipwith_options(request, runtime)

    async def describe_port_cc_attack_top_ip_async(
        self,
        request: ddoscoo_20200101_models.DescribePortCcAttackTopIPRequest,
    ) -> ddoscoo_20200101_models.DescribePortCcAttackTopIPResponse:
        """
        @summary Queries the top source IP addresses of the volumetric attack events for the Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribePortCcAttackTopIPRequest
        @return: DescribePortCcAttackTopIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_cc_attack_top_ipwith_options_async(request, runtime)

    def describe_port_conns_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        """
        @summary The statistics on the connections established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances are queried.
        
        @param request: DescribePortConnsCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortConnsCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The statistics on the connections established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances are queried.
        
        @param request: DescribePortConnsCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortConnsCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The statistics on the connections established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances are queried.
        
        @param request: DescribePortConnsCountRequest
        @return: DescribePortConnsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_count_with_options(request, runtime)

    async def describe_port_conns_count_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsCountRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsCountResponse:
        """
        @summary The statistics on the connections established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances are queried.
        
        @param request: DescribePortConnsCountRequest
        @return: DescribePortConnsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_conns_count_with_options_async(request, runtime)

    def describe_port_conns_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        """
        @summary Queries the connections established over the ports of one or more Anti-DDoS Proxy instances.
        
        @param request: DescribePortConnsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortConnsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the connections established over the ports of one or more Anti-DDoS Proxy instances.
        
        @param request: DescribePortConnsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortConnsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the connections established over the ports of one or more Anti-DDoS Proxy instances.
        
        @param request: DescribePortConnsListRequest
        @return: DescribePortConnsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_list_with_options(request, runtime)

    async def describe_port_conns_list_async(
        self,
        request: ddoscoo_20200101_models.DescribePortConnsListRequest,
    ) -> ddoscoo_20200101_models.DescribePortConnsListResponse:
        """
        @summary Queries the connections established over the ports of one or more Anti-DDoS Proxy instances.
        
        @param request: DescribePortConnsListRequest
        @return: DescribePortConnsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_conns_list_with_options_async(request, runtime)

    def describe_port_flow_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        """
        @summary Queries the traffic data of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortFlowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortFlowListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortFlowList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the traffic data of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortFlowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortFlowListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortFlowList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the traffic data of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortFlowListRequest
        @return: DescribePortFlowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_flow_list_with_options(request, runtime)

    async def describe_port_flow_list_async(
        self,
        request: ddoscoo_20200101_models.DescribePortFlowListRequest,
    ) -> ddoscoo_20200101_models.DescribePortFlowListResponse:
        """
        @summary Queries the traffic data of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortFlowListRequest
        @return: DescribePortFlowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_flow_list_with_options_async(request, runtime)

    def describe_port_max_conns_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        """
        @summary Queries the maximum number of connections that can be established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortMaxConnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortMaxConnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortMaxConns',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the maximum number of connections that can be established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortMaxConnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortMaxConnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortMaxConns',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the maximum number of connections that can be established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortMaxConnsRequest
        @return: DescribePortMaxConnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_max_conns_with_options(request, runtime)

    async def describe_port_max_conns_async(
        self,
        request: ddoscoo_20200101_models.DescribePortMaxConnsRequest,
    ) -> ddoscoo_20200101_models.DescribePortMaxConnsResponse:
        """
        @summary Queries the maximum number of connections that can be established over the ports of one or more Anti-DDoS Pro or Anti-DDoS Premium instances.
        
        @param request: DescribePortMaxConnsRequest
        @return: DescribePortMaxConnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_max_conns_with_options_async(request, runtime)

    def describe_port_view_source_countries_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        """
        @summary Queries the areas and countries from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @param request: DescribePortViewSourceCountriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceCountriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the areas and countries from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @param request: DescribePortViewSourceCountriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceCountriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the areas and countries from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @param request: DescribePortViewSourceCountriesRequest
        @return: DescribePortViewSourceCountriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_countries_with_options(request, runtime)

    async def describe_port_view_source_countries_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceCountriesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse:
        """
        @summary Queries the areas and countries from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @param request: DescribePortViewSourceCountriesRequest
        @return: DescribePortViewSourceCountriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_countries_with_options_async(request, runtime)

    def describe_port_view_source_isps_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        """
        @summary Queries the Internet service providers (ISPs) from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @description You can call the DescribePortViewSourceIsps operation to query the ISPs from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        > The data returned for this operation cannot reflect the actual traffic volume because Layer 4 identity authentication algorithms are updated for Anti-DDoS Pro and Anti-DDoS Premium. You can call this operation to calculate only the proportion of requests sent from different ISPs. If you want to query the request traffic volume, we recommend that you call the [DescribePortFlowList](https://help.aliyun.com/document_detail/157460.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortViewSourceIspsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceIspsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceIsps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Internet service providers (ISPs) from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @description You can call the DescribePortViewSourceIsps operation to query the ISPs from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        > The data returned for this operation cannot reflect the actual traffic volume because Layer 4 identity authentication algorithms are updated for Anti-DDoS Pro and Anti-DDoS Premium. You can call this operation to calculate only the proportion of requests sent from different ISPs. If you want to query the request traffic volume, we recommend that you call the [DescribePortFlowList](https://help.aliyun.com/document_detail/157460.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortViewSourceIspsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceIspsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceIsps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Internet service providers (ISPs) from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @description You can call the DescribePortViewSourceIsps operation to query the ISPs from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        > The data returned for this operation cannot reflect the actual traffic volume because Layer 4 identity authentication algorithms are updated for Anti-DDoS Pro and Anti-DDoS Premium. You can call this operation to calculate only the proportion of requests sent from different ISPs. If you want to query the request traffic volume, we recommend that you call the [DescribePortFlowList](https://help.aliyun.com/document_detail/157460.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortViewSourceIspsRequest
        @return: DescribePortViewSourceIspsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_isps_with_options(request, runtime)

    async def describe_port_view_source_isps_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceIspsRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceIspsResponse:
        """
        @summary Queries the Internet service providers (ISPs) from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within the specified period of time.
        
        @description You can call the DescribePortViewSourceIsps operation to query the ISPs from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        > The data returned for this operation cannot reflect the actual traffic volume because Layer 4 identity authentication algorithms are updated for Anti-DDoS Pro and Anti-DDoS Premium. You can call this operation to calculate only the proportion of requests sent from different ISPs. If you want to query the request traffic volume, we recommend that you call the [DescribePortFlowList](https://help.aliyun.com/document_detail/157460.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePortViewSourceIspsRequest
        @return: DescribePortViewSourceIspsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_isps_with_options_async(request, runtime)

    def describe_port_view_source_provinces_with_options(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        """
        @summary Queries the administrative regions in China from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @param request: DescribePortViewSourceProvincesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceProvincesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the administrative regions in China from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @param request: DescribePortViewSourceProvincesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePortViewSourceProvincesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the administrative regions in China from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @param request: DescribePortViewSourceProvincesRequest
        @return: DescribePortViewSourceProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_provinces_with_options(request, runtime)

    async def describe_port_view_source_provinces_async(
        self,
        request: ddoscoo_20200101_models.DescribePortViewSourceProvincesRequest,
    ) -> ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse:
        """
        @summary Queries the administrative regions in China from which requests are sent to one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specified period of time.
        
        @param request: DescribePortViewSourceProvincesRequest
        @return: DescribePortViewSourceProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_port_view_source_provinces_with_options_async(request, runtime)

    def describe_scene_defense_objects_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        """
        @summary Queries the protected objects of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefenseObjects operation to query the protected objects of a scenario-specific custom policy.
        Before you call this operation, make sure that you have created a scenario-specific custom policy by calling the [CreateSceneDefensePolicy](https://help.aliyun.com/document_detail/159779.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefenseObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneDefenseObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefenseObjects',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the protected objects of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefenseObjects operation to query the protected objects of a scenario-specific custom policy.
        Before you call this operation, make sure that you have created a scenario-specific custom policy by calling the [CreateSceneDefensePolicy](https://help.aliyun.com/document_detail/159779.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefenseObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneDefenseObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefenseObjects',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the protected objects of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefenseObjects operation to query the protected objects of a scenario-specific custom policy.
        Before you call this operation, make sure that you have created a scenario-specific custom policy by calling the [CreateSceneDefensePolicy](https://help.aliyun.com/document_detail/159779.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefenseObjectsRequest
        @return: DescribeSceneDefenseObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_objects_with_options(request, runtime)

    async def describe_scene_defense_objects_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefenseObjectsRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse:
        """
        @summary Queries the protected objects of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefenseObjects operation to query the protected objects of a scenario-specific custom policy.
        Before you call this operation, make sure that you have created a scenario-specific custom policy by calling the [CreateSceneDefensePolicy](https://help.aliyun.com/document_detail/159779.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefenseObjectsRequest
        @return: DescribeSceneDefenseObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_defense_objects_with_options_async(request, runtime)

    def describe_scene_defense_policies_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        """
        @summary Queries the configurations of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefensePolicies operation to query the configurations of a scenario-specific custom policy that is created. For example, you can query the status, protected objects, and protection rules of the policy.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefensePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneDefensePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefensePolicies',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the configurations of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefensePolicies operation to query the configurations of a scenario-specific custom policy that is created. For example, you can query the status, protected objects, and protection rules of the policy.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefensePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneDefensePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefensePolicies',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the configurations of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefensePolicies operation to query the configurations of a scenario-specific custom policy that is created. For example, you can query the status, protected objects, and protection rules of the policy.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefensePoliciesRequest
        @return: DescribeSceneDefensePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_policies_with_options(request, runtime)

    async def describe_scene_defense_policies_async(
        self,
        request: ddoscoo_20200101_models.DescribeSceneDefensePoliciesRequest,
    ) -> ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse:
        """
        @summary Queries the configurations of a scenario-specific custom policy.
        
        @description You can call the DescribeSceneDefensePolicies operation to query the configurations of a scenario-specific custom policy that is created. For example, you can query the status, protected objects, and protection rules of the policy.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSceneDefensePoliciesRequest
        @return: DescribeSceneDefensePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_defense_policies_with_options_async(request, runtime)

    def describe_scheduler_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        """
        @param request: DescribeSchedulerRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchedulerRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedulerRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: DescribeSchedulerRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchedulerRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedulerRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: DescribeSchedulerRulesRequest
        @return: DescribeSchedulerRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduler_rules_with_options(request, runtime)

    async def describe_scheduler_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeSchedulerRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeSchedulerRulesResponse:
        """
        @param request: DescribeSchedulerRulesRequest
        @return: DescribeSchedulerRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduler_rules_with_options_async(request, runtime)

    def describe_sla_event_list_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlaEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlaEventListResponse:
        """
        @summary Queries the destination rate limit events.
        
        @param request: DescribeSlaEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlaEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlaEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlaEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sla_event_list_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlaEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlaEventListResponse:
        """
        @summary Queries the destination rate limit events.
        
        @param request: DescribeSlaEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlaEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlaEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlaEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sla_event_list(
        self,
        request: ddoscoo_20200101_models.DescribeSlaEventListRequest,
    ) -> ddoscoo_20200101_models.DescribeSlaEventListResponse:
        """
        @summary Queries the destination rate limit events.
        
        @param request: DescribeSlaEventListRequest
        @return: DescribeSlaEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sla_event_list_with_options(request, runtime)

    async def describe_sla_event_list_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlaEventListRequest,
    ) -> ddoscoo_20200101_models.DescribeSlaEventListResponse:
        """
        @summary Queries the destination rate limit events.
        
        @param request: DescribeSlaEventListRequest
        @return: DescribeSlaEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sla_event_list_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service.
        
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service.
        
        @param request: DescribeSlsAuthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service.
        
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsAuthStatusResponse:
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service.
        
        @param request: DescribeSlsAuthStatusRequest
        @return: DescribeSlsAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        """
        @summary Queries the information about the Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance, such as the log storage capacity and log storage duration.
        
        @param request: DescribeSlsLogstoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogstoreInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance, such as the log storage capacity and log storage duration.
        
        @param request: DescribeSlsLogstoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsLogstoreInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance, such as the log storage capacity and log storage duration.
        
        @param request: DescribeSlsLogstoreInfoRequest
        @return: DescribeSlsLogstoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse:
        """
        @summary Queries the information about the Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance, such as the log storage capacity and log storage duration.
        
        @param request: DescribeSlsLogstoreInfoRequest
        @return: DescribeSlsLogstoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: DescribeSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether Log Service is activated.
        
        @param request: DescribeSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether Log Service is activated.
        
        @param request: DescribeSlsOpenStatusRequest
        @return: DescribeSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: DescribeSlsOpenStatusRequest
        @return: DescribeSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describe_sts_grant_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        
        @description You can call the DescribeStsGrantStatus operation to query whether Anti-DDoS Pro or Anti-DDoS Premium of the current Alibaba Cloud account is authorized to access other cloud services.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeStsGrantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStsGrantStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStsGrantStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        
        @description You can call the DescribeStsGrantStatus operation to query whether Anti-DDoS Pro or Anti-DDoS Premium of the current Alibaba Cloud account is authorized to access other cloud services.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeStsGrantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStsGrantStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStsGrantStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        
        @description You can call the DescribeStsGrantStatus operation to query whether Anti-DDoS Pro or Anti-DDoS Premium of the current Alibaba Cloud account is authorized to access other cloud services.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeStsGrantStatusRequest
        @return: DescribeStsGrantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sts_grant_status_with_options(request, runtime)

    async def describe_sts_grant_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeStsGrantStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeStsGrantStatusResponse:
        """
        @summary Queries whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        
        @description You can call the DescribeStsGrantStatus operation to query whether Anti-DDoS Pro or Anti-DDoS Premium of the current Alibaba Cloud account is authorized to access other cloud services.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeStsGrantStatusRequest
        @return: DescribeStsGrantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sts_grant_status_with_options_async(request, runtime)

    def describe_system_log_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeSystemLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSystemLogResponse:
        """
        @summary Queries the details of the bills for the burstable clean bandwidth.
        
        @description You can call the DescribeSystemLog operation to query the system logs of Anti-DDoS Pro or Anti-DDoS Premium. The system logs contain only billing logs for the burstable clean bandwidth.
        If you have enabled the burstable clean bandwidth feature, you can call this operation to query the details of the bills of the burstable clean bandwidth.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSystemLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSystemLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_log_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeSystemLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeSystemLogResponse:
        """
        @summary Queries the details of the bills for the burstable clean bandwidth.
        
        @description You can call the DescribeSystemLog operation to query the system logs of Anti-DDoS Pro or Anti-DDoS Premium. The system logs contain only billing logs for the burstable clean bandwidth.
        If you have enabled the burstable clean bandwidth feature, you can call this operation to query the details of the bills of the burstable clean bandwidth.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSystemLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSystemLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_log(
        self,
        request: ddoscoo_20200101_models.DescribeSystemLogRequest,
    ) -> ddoscoo_20200101_models.DescribeSystemLogResponse:
        """
        @summary Queries the details of the bills for the burstable clean bandwidth.
        
        @description You can call the DescribeSystemLog operation to query the system logs of Anti-DDoS Pro or Anti-DDoS Premium. The system logs contain only billing logs for the burstable clean bandwidth.
        If you have enabled the burstable clean bandwidth feature, you can call this operation to query the details of the bills of the burstable clean bandwidth.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSystemLogRequest
        @return: DescribeSystemLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_system_log_with_options(request, runtime)

    async def describe_system_log_async(
        self,
        request: ddoscoo_20200101_models.DescribeSystemLogRequest,
    ) -> ddoscoo_20200101_models.DescribeSystemLogResponse:
        """
        @summary Queries the details of the bills for the burstable clean bandwidth.
        
        @description You can call the DescribeSystemLog operation to query the system logs of Anti-DDoS Pro or Anti-DDoS Premium. The system logs contain only billing logs for the burstable clean bandwidth.
        If you have enabled the burstable clean bandwidth feature, you can call this operation to query the details of the bills of the burstable clean bandwidth.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSystemLogRequest
        @return: DescribeSystemLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_log_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added.
        
        @description You can call this operation to query all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added by page.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added.
        
        @description You can call this operation to query all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added by page.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added.
        
        @description You can call this operation to query all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added by page.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagKeysRequest
        @return: DescribeTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagKeysRequest,
    ) -> ddoscoo_20200101_models.DescribeTagKeysResponse:
        """
        @summary Queries all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added.
        
        @description You can call this operation to query all tag keys and the number of Anti-DDoS Proxy (Chinese Mainland) instances to which each tag key is added by page.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagKeysRequest
        @return: DescribeTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_resources_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        """
        @summary Queries the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description You can call the DescribeTagResources operation to query the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description You can call the DescribeTagResources operation to query the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description You can call the DescribeTagResources operation to query the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagResourcesRequest
        @return: DescribeTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: ddoscoo_20200101_models.DescribeTagResourcesRequest,
    ) -> ddoscoo_20200101_models.DescribeTagResourcesResponse:
        """
        @summary Queries the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description You can call the DescribeTagResources operation to query the information about the tags that are added to an Anti-DDoS Proxy (Chinese Mainland) instance.
        >  Only Anti-DDoS Proxy (Chinese Mainland) supports tags.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTagResourcesRequest
        @return: DescribeTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_total_attack_max_flow_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeTotalAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse:
        """
        @summary Queries the peak bandwidth and peak packet rates of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        
        @param request: DescribeTotalAttackMaxFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTotalAttackMaxFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTotalAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_total_attack_max_flow_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeTotalAttackMaxFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse:
        """
        @summary Queries the peak bandwidth and peak packet rates of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        
        @param request: DescribeTotalAttackMaxFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTotalAttackMaxFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTotalAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_total_attack_max_flow(
        self,
        request: ddoscoo_20200101_models.DescribeTotalAttackMaxFlowRequest,
    ) -> ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse:
        """
        @summary Queries the peak bandwidth and peak packet rates of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        
        @param request: DescribeTotalAttackMaxFlowRequest
        @return: DescribeTotalAttackMaxFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_total_attack_max_flow_with_options(request, runtime)

    async def describe_total_attack_max_flow_async(
        self,
        request: ddoscoo_20200101_models.DescribeTotalAttackMaxFlowRequest,
    ) -> ddoscoo_20200101_models.DescribeTotalAttackMaxFlowResponse:
        """
        @summary Queries the peak bandwidth and peak packet rates of attack traffic on one or more Anti-DDoS Pro or Anti-DDoS Premium instances within a specific period of time.
        
        @param request: DescribeTotalAttackMaxFlowRequest
        @return: DescribeTotalAttackMaxFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_total_attack_max_flow_with_options_async(request, runtime)

    def describe_udp_reflect_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeUdpReflectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUdpReflectResponse:
        """
        @summary Queries the source ports of UDP traffic that are filtered out by the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeUdpReflectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUdpReflectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_udp_reflect_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeUdpReflectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUdpReflectResponse:
        """
        @summary Queries the source ports of UDP traffic that are filtered out by the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeUdpReflectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUdpReflectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUdpReflectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_udp_reflect(
        self,
        request: ddoscoo_20200101_models.DescribeUdpReflectRequest,
    ) -> ddoscoo_20200101_models.DescribeUdpReflectResponse:
        """
        @summary Queries the source ports of UDP traffic that are filtered out by the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeUdpReflectRequest
        @return: DescribeUdpReflectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_udp_reflect_with_options(request, runtime)

    async def describe_udp_reflect_async(
        self,
        request: ddoscoo_20200101_models.DescribeUdpReflectRequest,
    ) -> ddoscoo_20200101_models.DescribeUdpReflectResponse:
        """
        @summary Queries the source ports of UDP traffic that are filtered out by the filtering policies for UDP reflection attacks on an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: DescribeUdpReflectRequest
        @return: DescribeUdpReflectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_udp_reflect_with_options_async(request, runtime)

    def describe_un_blackhole_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        """
        @summary Queries the total quota and remaining quota that allow you to deactivate blackhole filtering.
        
        @param request: DescribeUnBlackholeCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUnBlackholeCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlackholeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the total quota and remaining quota that allow you to deactivate blackhole filtering.
        
        @param request: DescribeUnBlackholeCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUnBlackholeCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlackholeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the total quota and remaining quota that allow you to deactivate blackhole filtering.
        
        @param request: DescribeUnBlackholeCountRequest
        @return: DescribeUnBlackholeCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_un_blackhole_count_with_options(request, runtime)

    async def describe_un_blackhole_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlackholeCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlackholeCountResponse:
        """
        @summary Queries the total quota and remaining quota that allow you to deactivate blackhole filtering.
        
        @param request: DescribeUnBlackholeCountRequest
        @return: DescribeUnBlackholeCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_un_blackhole_count_with_options_async(request, runtime)

    def describe_un_block_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        """
        @summary Queries the remaining quota that allows you to use the Diversion from Origin Server policy.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeUnBlockCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUnBlockCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlockCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the remaining quota that allows you to use the Diversion from Origin Server policy.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeUnBlockCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUnBlockCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlockCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the remaining quota that allows you to use the Diversion from Origin Server policy.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeUnBlockCountRequest
        @return: DescribeUnBlockCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_un_block_count_with_options(request, runtime)

    async def describe_un_block_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeUnBlockCountRequest,
    ) -> ddoscoo_20200101_models.DescribeUnBlockCountResponse:
        """
        @summary Queries the remaining quota that allows you to use the Diversion from Origin Server policy.
        
        @description > This operation is suitable only for Anti-DDoS Pro.
        
        @param request: DescribeUnBlockCountRequest
        @return: DescribeUnBlockCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_un_block_count_with_options_async(request, runtime)

    def describe_web_access_log_dispatch_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        """
        @summary Checks whether the log analysis feature is enabled for all domain names.
        
        @description You can call the DescribeWebAccessLogDispatchStatus operation to check whether the log analysis feature is enabled for all domain names that are added to your Anti-DDoS Pro or Anti-DDoS Premium instance.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebAccessLogDispatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogDispatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogDispatchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether the log analysis feature is enabled for all domain names.
        
        @description You can call the DescribeWebAccessLogDispatchStatus operation to check whether the log analysis feature is enabled for all domain names that are added to your Anti-DDoS Pro or Anti-DDoS Premium instance.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebAccessLogDispatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogDispatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogDispatchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Checks whether the log analysis feature is enabled for all domain names.
        
        @description You can call the DescribeWebAccessLogDispatchStatus operation to check whether the log analysis feature is enabled for all domain names that are added to your Anti-DDoS Pro or Anti-DDoS Premium instance.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebAccessLogDispatchStatusRequest
        @return: DescribeWebAccessLogDispatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_dispatch_status_with_options(request, runtime)

    async def describe_web_access_log_dispatch_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse:
        """
        @summary Checks whether the log analysis feature is enabled for all domain names.
        
        @description You can call the DescribeWebAccessLogDispatchStatus operation to check whether the log analysis feature is enabled for all domain names that are added to your Anti-DDoS Pro or Anti-DDoS Premium instance.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebAccessLogDispatchStatusRequest
        @return: DescribeWebAccessLogDispatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_dispatch_status_with_options_async(request, runtime)

    def describe_web_access_log_empty_count_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        """
        @summary Queries the remaining quota that allows you to clear the Logstore.
        
        @param request: DescribeWebAccessLogEmptyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogEmptyCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogEmptyCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the remaining quota that allows you to clear the Logstore.
        
        @param request: DescribeWebAccessLogEmptyCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogEmptyCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogEmptyCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the remaining quota that allows you to clear the Logstore.
        
        @param request: DescribeWebAccessLogEmptyCountRequest
        @return: DescribeWebAccessLogEmptyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_empty_count_with_options(request, runtime)

    async def describe_web_access_log_empty_count_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse:
        """
        @summary Queries the remaining quota that allows you to clear the Logstore.
        
        @param request: DescribeWebAccessLogEmptyCountRequest
        @return: DescribeWebAccessLogEmptyCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_empty_count_with_options_async(request, runtime)

    def describe_web_access_log_status_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        """
        @summary Queries the information about the Log Analysis feature for a website, such as the feature status and the Log Service project and Logstore that are used.
        
        @param request: DescribeWebAccessLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the Log Analysis feature for a website, such as the feature status and the Log Service project and Logstore that are used.
        
        @param request: DescribeWebAccessLogStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessLogStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about the Log Analysis feature for a website, such as the feature status and the Log Service project and Logstore that are used.
        
        @param request: DescribeWebAccessLogStatusRequest
        @return: DescribeWebAccessLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_status_with_options(request, runtime)

    async def describe_web_access_log_status_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessLogStatusRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse:
        """
        @summary Queries the information about the Log Analysis feature for a website, such as the feature status and the Log Service project and Logstore that are used.
        
        @param request: DescribeWebAccessLogStatusRequest
        @return: DescribeWebAccessLogStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_log_status_with_options_async(request, runtime)

    def describe_web_access_mode_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        """
        @summary Queries the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeWebAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeWebAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeWebAccessModeRequest
        @return: DescribeWebAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_mode_with_options(request, runtime)

    async def describe_web_access_mode_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAccessModeResponse:
        """
        @summary Queries the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: DescribeWebAccessModeRequest
        @return: DescribeWebAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_access_mode_with_options_async(request, runtime)

    def describe_web_area_block_configs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        """
        @summary Queries the Location Blacklist (Domain Names) configurations for websites.
        
        @param request: DescribeWebAreaBlockConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAreaBlockConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAreaBlockConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Location Blacklist (Domain Names) configurations for websites.
        
        @param request: DescribeWebAreaBlockConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebAreaBlockConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAreaBlockConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Location Blacklist (Domain Names) configurations for websites.
        
        @param request: DescribeWebAreaBlockConfigsRequest
        @return: DescribeWebAreaBlockConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_area_block_configs_with_options(request, runtime)

    async def describe_web_area_block_configs_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebAreaBlockConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse:
        """
        @summary Queries the Location Blacklist (Domain Names) configurations for websites.
        
        @param request: DescribeWebAreaBlockConfigsRequest
        @return: DescribeWebAreaBlockConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_area_block_configs_with_options_async(request, runtime)

    def describe_web_ccrules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        """
        @deprecated OpenAPI DescribeWebCCRules is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCCRulesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI DescribeWebCCRules is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCCRulesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI DescribeWebCCRules is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesRequest
        @return: DescribeWebCCRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_ccrules_with_options(request, runtime)

    async def describe_web_ccrules_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesResponse:
        """
        @deprecated OpenAPI DescribeWebCCRules is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesRequest
        @return: DescribeWebCCRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_ccrules_with_options_async(request, runtime)

    def describe_web_ccrules_v2with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesV2Response:
        """
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCCRulesV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRulesV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCCRulesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_ccrules_v2with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesV2Response:
        """
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCCRulesV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRulesV2',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCCRulesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_ccrules_v2(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesV2Request,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesV2Response:
        """
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesV2Request
        @return: DescribeWebCCRulesV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_ccrules_v2with_options(request, runtime)

    async def describe_web_ccrules_v2_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCCRulesV2Request,
    ) -> ddoscoo_20200101_models.DescribeWebCCRulesV2Response:
        """
        @summary Queries the custom frequency control rules that are created for a website.
        
        @param request: DescribeWebCCRulesV2Request
        @return: DescribeWebCCRulesV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_ccrules_v2with_options_async(request, runtime)

    def describe_web_cache_configs_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        """
        @summary Queries the Static Page Caching configuration of websites.
        
        @description You can call the DescribeWebCacheConfigs operation to query the Static Page Caching configurations of websites. The configurations include cache modes and custom caching rules.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebCacheConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCacheConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCacheConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Static Page Caching configuration of websites.
        
        @description You can call the DescribeWebCacheConfigs operation to query the Static Page Caching configurations of websites. The configurations include cache modes and custom caching rules.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebCacheConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCacheConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCacheConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the Static Page Caching configuration of websites.
        
        @description You can call the DescribeWebCacheConfigs operation to query the Static Page Caching configurations of websites. The configurations include cache modes and custom caching rules.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebCacheConfigsRequest
        @return: DescribeWebCacheConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cache_configs_with_options(request, runtime)

    async def describe_web_cache_configs_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCacheConfigsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCacheConfigsResponse:
        """
        @summary Queries the Static Page Caching configuration of websites.
        
        @description You can call the DescribeWebCacheConfigs operation to query the Static Page Caching configurations of websites. The configurations include cache modes and custom caching rules.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWebCacheConfigsRequest
        @return: DescribeWebCacheConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_cache_configs_with_options_async(request, runtime)

    def describe_web_cc_protect_switch_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        """
        @summary Queries the status of each mitigation policy for a website.
        
        @param request: DescribeWebCcProtectSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCcProtectSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCcProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status of each mitigation policy for a website.
        
        @param request: DescribeWebCcProtectSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCcProtectSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCcProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status of each mitigation policy for a website.
        
        @param request: DescribeWebCcProtectSwitchRequest
        @return: DescribeWebCcProtectSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cc_protect_switch_with_options(request, runtime)

    async def describe_web_cc_protect_switch_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCcProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse:
        """
        @summary Queries the status of each mitigation policy for a website.
        
        @param request: DescribeWebCcProtectSwitchRequest
        @return: DescribeWebCcProtectSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_cc_protect_switch_with_options_async(request, runtime)

    def describe_web_custom_ports_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        """
        @summary Queries the supported custom ports of a website.
        
        @param request: DescribeWebCustomPortsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCustomPortsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomPorts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the supported custom ports of a website.
        
        @param request: DescribeWebCustomPortsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCustomPortsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomPorts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the supported custom ports of a website.
        
        @param request: DescribeWebCustomPortsRequest
        @return: DescribeWebCustomPortsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_custom_ports_with_options(request, runtime)

    async def describe_web_custom_ports_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebCustomPortsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebCustomPortsResponse:
        """
        @summary Queries the supported custom ports of a website.
        
        @param request: DescribeWebCustomPortsRequest
        @return: DescribeWebCustomPortsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_custom_ports_with_options_async(request, runtime)

    def describe_web_instance_relations_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        """
        @summary Queries the information about Anti-DDoS Pro or Anti-DDoS Premium instances to which a website service is added.
        
        @param request: DescribeWebInstanceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebInstanceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceRelations',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about Anti-DDoS Pro or Anti-DDoS Premium instances to which a website service is added.
        
        @param request: DescribeWebInstanceRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebInstanceRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceRelations',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the information about Anti-DDoS Pro or Anti-DDoS Premium instances to which a website service is added.
        
        @param request: DescribeWebInstanceRelationsRequest
        @return: DescribeWebInstanceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_instance_relations_with_options(request, runtime)

    async def describe_web_instance_relations_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebInstanceRelationsRequest,
    ) -> ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse:
        """
        @summary Queries the information about Anti-DDoS Pro or Anti-DDoS Premium instances to which a website service is added.
        
        @param request: DescribeWebInstanceRelationsRequest
        @return: DescribeWebInstanceRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_instance_relations_with_options_async(request, runtime)

    def describe_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        """
        @summary Queries the accurate access control rules that are created for websites.
        
        @param request: DescribeWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the accurate access control rules that are created for websites.
        
        @param request: DescribeWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the accurate access control rules that are created for websites.
        
        @param request: DescribeWebPreciseAccessRuleRequest
        @return: DescribeWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_precise_access_rule_with_options(request, runtime)

    async def describe_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse:
        """
        @summary Queries the accurate access control rules that are created for websites.
        
        @param request: DescribeWebPreciseAccessRuleRequest
        @return: DescribeWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_precise_access_rule_with_options_async(request, runtime)

    def describe_web_report_top_ip_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebReportTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebReportTopIpResponse:
        """
        @summary Queries the top source IP addresses of the web resource exhaustion attacks for the Anti-DDoS Proxy instance.
        
        @param request: DescribeWebReportTopIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebReportTopIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebReportTopIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebReportTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_report_top_ip_with_options_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebReportTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebReportTopIpResponse:
        """
        @summary Queries the top source IP addresses of the web resource exhaustion attacks for the Anti-DDoS Proxy instance.
        
        @param request: DescribeWebReportTopIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebReportTopIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebReportTopIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebReportTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_report_top_ip(
        self,
        request: ddoscoo_20200101_models.DescribeWebReportTopIpRequest,
    ) -> ddoscoo_20200101_models.DescribeWebReportTopIpResponse:
        """
        @summary Queries the top source IP addresses of the web resource exhaustion attacks for the Anti-DDoS Proxy instance.
        
        @param request: DescribeWebReportTopIpRequest
        @return: DescribeWebReportTopIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_report_top_ip_with_options(request, runtime)

    async def describe_web_report_top_ip_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebReportTopIpRequest,
    ) -> ddoscoo_20200101_models.DescribeWebReportTopIpResponse:
        """
        @summary Queries the top source IP addresses of the web resource exhaustion attacks for the Anti-DDoS Proxy instance.
        
        @param request: DescribeWebReportTopIpRequest
        @return: DescribeWebReportTopIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_report_top_ip_with_options_async(request, runtime)

    def describe_web_rules_with_options(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        """
        @summary Indicates whether Allow Access Only from SM Certificates-based Clients is turned on.
        0: no
        1: yes
        
        @param request: DescribeWebRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Indicates whether Allow Access Only from SM Certificates-based Clients is turned on.
        0: no
        1: yes
        
        @param request: DescribeWebRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Indicates whether Allow Access Only from SM Certificates-based Clients is turned on.
        0: no
        1: yes
        
        @param request: DescribeWebRulesRequest
        @return: DescribeWebRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_web_rules_with_options(request, runtime)

    async def describe_web_rules_async(
        self,
        request: ddoscoo_20200101_models.DescribeWebRulesRequest,
    ) -> ddoscoo_20200101_models.DescribeWebRulesResponse:
        """
        @summary Indicates whether Allow Access Only from SM Certificates-based Clients is turned on.
        0: no
        1: yes
        
        @param request: DescribeWebRulesRequest
        @return: DescribeWebRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_rules_with_options_async(request, runtime)

    def detach_scene_defense_object_with_options(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        """
        @summary Removes a protected object from a scenario-specific custom policy.
        
        @param request: DetachSceneDefenseObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachSceneDefenseObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes a protected object from a scenario-specific custom policy.
        
        @param request: DetachSceneDefenseObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachSceneDefenseObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Removes a protected object from a scenario-specific custom policy.
        
        @param request: DetachSceneDefenseObjectRequest
        @return: DetachSceneDefenseObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_scene_defense_object_with_options(request, runtime)

    async def detach_scene_defense_object_async(
        self,
        request: ddoscoo_20200101_models.DetachSceneDefenseObjectRequest,
    ) -> ddoscoo_20200101_models.DetachSceneDefenseObjectResponse:
        """
        @summary Removes a protected object from a scenario-specific custom policy.
        
        @param request: DetachSceneDefenseObjectRequest
        @return: DetachSceneDefenseObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_scene_defense_object_with_options_async(request, runtime)

    def disable_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        """
        @summary Disables a scenario-specific custom policy.
        
        @param request: DisableSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables a scenario-specific custom policy.
        
        @param request: DisableSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables a scenario-specific custom policy.
        
        @param request: DisableSceneDefensePolicyRequest
        @return: DisableSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_defense_policy_with_options(request, runtime)

    async def disable_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.DisableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.DisableSceneDefensePolicyResponse:
        """
        @summary Disables a scenario-specific custom policy.
        
        @param request: DisableSceneDefensePolicyRequest
        @return: DisableSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_scene_defense_policy_with_options_async(request, runtime)

    def disable_web_access_log_config_with_options(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        """
        @summary Disables the log analysis feature for a website.
        
        @param request: DisableWebAccessLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebAccessLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables the log analysis feature for a website.
        
        @param request: DisableWebAccessLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebAccessLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables the log analysis feature for a website.
        
        @param request: DisableWebAccessLogConfigRequest
        @return: DisableWebAccessLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_web_access_log_config_with_options(request, runtime)

    async def disable_web_access_log_config_async(
        self,
        request: ddoscoo_20200101_models.DisableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.DisableWebAccessLogConfigResponse:
        """
        @summary Disables the log analysis feature for a website.
        
        @param request: DisableWebAccessLogConfigRequest
        @return: DisableWebAccessLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_access_log_config_with_options_async(request, runtime)

    def disable_web_ccwith_options(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        """
        @summary Disables the Frequency Control policy for a website.
        
        @param request: DisableWebCCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebCCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables the Frequency Control policy for a website.
        
        @param request: DisableWebCCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebCCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Disables the Frequency Control policy for a website.
        
        @param request: DisableWebCCRequest
        @return: DisableWebCCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccwith_options(request, runtime)

    async def disable_web_cc_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCResponse:
        """
        @summary Disables the Frequency Control policy for a website.
        
        @param request: DisableWebCCRequest
        @return: DisableWebCCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_ccwith_options_async(request, runtime)

    def disable_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        """
        @summary Turns off the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: DisableWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebCCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Turns off the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: DisableWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWebCCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Turns off the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: DisableWebCCRuleRequest
        @return: DisableWebCCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccrule_with_options(request, runtime)

    async def disable_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.DisableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.DisableWebCCRuleResponse:
        """
        @summary Turns off the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: DisableWebCCRuleRequest
        @return: DisableWebCCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_web_ccrule_with_options_async(request, runtime)

    def empty_auto_cc_blacklist_with_options(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        """
        @summary Clears the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptyAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptyAutoCcBlacklistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcBlacklistRequest
        @return: EmptyAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_blacklist_with_options(request, runtime)

    async def empty_auto_cc_blacklist_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcBlacklistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse:
        """
        @summary Clears the IP address blacklist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcBlacklistRequest
        @return: EmptyAutoCcBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.empty_auto_cc_blacklist_with_options_async(request, runtime)

    def empty_auto_cc_whitelist_with_options(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        """
        @summary Clears the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptyAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptyAutoCcWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcWhitelistRequest
        @return: EmptyAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_whitelist_with_options(request, runtime)

    async def empty_auto_cc_whitelist_async(
        self,
        request: ddoscoo_20200101_models.EmptyAutoCcWhitelistRequest,
    ) -> ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse:
        """
        @summary Clears the IP address whitelist of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: EmptyAutoCcWhitelistRequest
        @return: EmptyAutoCcWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.empty_auto_cc_whitelist_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        """
        @summary Clears the Logstore of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: EmptySlsLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptySlsLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the Logstore of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: EmptySlsLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmptySlsLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Clears the Logstore of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: EmptySlsLogstoreRequest
        @return: EmptySlsLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: ddoscoo_20200101_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20200101_models.EmptySlsLogstoreResponse:
        """
        @summary Clears the Logstore of Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: EmptySlsLogstoreRequest
        @return: EmptySlsLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def enable_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        """
        @summary Enables a scenario-specific custom policy.
        
        @param request: EnableSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables a scenario-specific custom policy.
        
        @param request: EnableSceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables a scenario-specific custom policy.
        
        @param request: EnableSceneDefensePolicyRequest
        @return: EnableSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_defense_policy_with_options(request, runtime)

    async def enable_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.EnableSceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.EnableSceneDefensePolicyResponse:
        """
        @summary Enables a scenario-specific custom policy.
        
        @param request: EnableSceneDefensePolicyRequest
        @return: EnableSceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_scene_defense_policy_with_options_async(request, runtime)

    def enable_web_access_log_config_with_options(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        """
        @summary Enables the log analysis feature for a website.
        
        @param request: EnableWebAccessLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebAccessLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables the log analysis feature for a website.
        
        @param request: EnableWebAccessLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebAccessLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables the log analysis feature for a website.
        
        @param request: EnableWebAccessLogConfigRequest
        @return: EnableWebAccessLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_web_access_log_config_with_options(request, runtime)

    async def enable_web_access_log_config_async(
        self,
        request: ddoscoo_20200101_models.EnableWebAccessLogConfigRequest,
    ) -> ddoscoo_20200101_models.EnableWebAccessLogConfigResponse:
        """
        @summary Enables the log analysis feature for a website.
        
        @param request: EnableWebAccessLogConfigRequest
        @return: EnableWebAccessLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_access_log_config_with_options_async(request, runtime)

    def enable_web_ccwith_options(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        """
        @summary Enables the Frequency Control policy for a website.
        
        @param request: EnableWebCCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebCCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables the Frequency Control policy for a website.
        
        @param request: EnableWebCCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebCCResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables the Frequency Control policy for a website.
        
        @param request: EnableWebCCRequest
        @return: EnableWebCCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccwith_options(request, runtime)

    async def enable_web_cc_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCResponse:
        """
        @summary Enables the Frequency Control policy for a website.
        
        @param request: EnableWebCCRequest
        @return: EnableWebCCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_ccwith_options_async(request, runtime)

    def enable_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        """
        @summary Turns on the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: EnableWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebCCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Turns on the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: EnableWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWebCCRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Turns on the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: EnableWebCCRuleRequest
        @return: EnableWebCCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccrule_with_options(request, runtime)

    async def enable_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.EnableWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.EnableWebCCRuleResponse:
        """
        @summary Turns on the Custom Rule switch of the Frequency Control policy for a website.
        
        @param request: EnableWebCCRuleRequest
        @return: EnableWebCCRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_web_ccrule_with_options_async(request, runtime)

    def modify_biz_band_width_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyBizBandWidthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBizBandWidthModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @description You can switch between the metering methods of the burstable clean bandwidth feature. The new metering method takes effect from 00:00 on the first day of the next month. You can change the metering method up to three times each calendar month. The most recent metering method that you select takes effect in the next month. You cannot change the metering method on the last day of each calendar month.
        
        @param request: ModifyBizBandWidthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBizBandWidthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBizBandWidthMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBizBandWidthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_biz_band_width_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyBizBandWidthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBizBandWidthModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @description You can switch between the metering methods of the burstable clean bandwidth feature. The new metering method takes effect from 00:00 on the first day of the next month. You can change the metering method up to three times each calendar month. The most recent metering method that you select takes effect in the next month. You cannot change the metering method on the last day of each calendar month.
        
        @param request: ModifyBizBandWidthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBizBandWidthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBizBandWidthMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBizBandWidthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_biz_band_width_mode(
        self,
        request: ddoscoo_20200101_models.ModifyBizBandWidthModeRequest,
    ) -> ddoscoo_20200101_models.ModifyBizBandWidthModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @description You can switch between the metering methods of the burstable clean bandwidth feature. The new metering method takes effect from 00:00 on the first day of the next month. You can change the metering method up to three times each calendar month. The most recent metering method that you select takes effect in the next month. You cannot change the metering method on the last day of each calendar month.
        
        @param request: ModifyBizBandWidthModeRequest
        @return: ModifyBizBandWidthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_biz_band_width_mode_with_options(request, runtime)

    async def modify_biz_band_width_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyBizBandWidthModeRequest,
    ) -> ddoscoo_20200101_models.ModifyBizBandWidthModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @description You can switch between the metering methods of the burstable clean bandwidth feature. The new metering method takes effect from 00:00 on the first day of the next month. You can change the metering method up to three times each calendar month. The most recent metering method that you select takes effect in the next month. You cannot change the metering method on the last day of each calendar month.
        
        @param request: ModifyBizBandWidthModeRequest
        @return: ModifyBizBandWidthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_biz_band_width_mode_with_options_async(request, runtime)

    def modify_blackhole_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        """
        @summary Deactivates blackhole filtering that is triggered on an instance.
        
        @param request: ModifyBlackholeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBlackholeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blackhole_status):
            query['BlackholeStatus'] = request.blackhole_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deactivates blackhole filtering that is triggered on an instance.
        
        @param request: ModifyBlackholeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBlackholeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blackhole_status):
            query['BlackholeStatus'] = request.blackhole_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deactivates blackhole filtering that is triggered on an instance.
        
        @param request: ModifyBlackholeStatusRequest
        @return: ModifyBlackholeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_blackhole_status_with_options(request, runtime)

    async def modify_blackhole_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlackholeStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlackholeStatusResponse:
        """
        @summary Deactivates blackhole filtering that is triggered on an instance.
        
        @param request: ModifyBlackholeStatusRequest
        @return: ModifyBlackholeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_blackhole_status_with_options_async(request, runtime)

    def modify_block_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        """
        @summary Modifies the Diversion from Origin Server configuration of an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyBlockStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBlockStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Diversion from Origin Server configuration of an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyBlockStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBlockStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Diversion from Origin Server configuration of an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyBlockStatusRequest
        @return: ModifyBlockStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_block_status_with_options(request, runtime)

    async def modify_block_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyBlockStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyBlockStatusResponse:
        """
        @summary Modifies the Diversion from Origin Server configuration of an Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyBlockStatusRequest
        @return: ModifyBlockStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_block_status_with_options_async(request, runtime)

    def modify_cname_reuse_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        """
        @summary Enables or disables CNAME reuse for a website.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: ModifyCnameReuseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCnameReuseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCnameReuse',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables CNAME reuse for a website.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: ModifyCnameReuseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCnameReuseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCnameReuse',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables CNAME reuse for a website.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: ModifyCnameReuseRequest
        @return: ModifyCnameReuseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cname_reuse_with_options(request, runtime)

    async def modify_cname_reuse_async(
        self,
        request: ddoscoo_20200101_models.ModifyCnameReuseRequest,
    ) -> ddoscoo_20200101_models.ModifyCnameReuseResponse:
        """
        @summary Enables or disables CNAME reuse for a website.
        
        @description > This operation is suitable only for Anti-DDoS Premium.
        
        @param request: ModifyCnameReuseRequest
        @return: ModifyCnameReuseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cname_reuse_with_options_async(request, runtime)

    def modify_domain_resource_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyDomainResourceResponse:
        """
        @summary Modifies the forwarding rule of a website.
        
        @param request: ModifyDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_resource_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyDomainResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyDomainResourceResponse:
        """
        @summary Modifies the forwarding rule of a website.
        
        @param request: ModifyDomainResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyDomainResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_resource(
        self,
        request: ddoscoo_20200101_models.ModifyDomainResourceRequest,
    ) -> ddoscoo_20200101_models.ModifyDomainResourceResponse:
        """
        @summary Modifies the forwarding rule of a website.
        
        @param request: ModifyDomainResourceRequest
        @return: ModifyDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_resource_with_options(request, runtime)

    async def modify_domain_resource_async(
        self,
        request: ddoscoo_20200101_models.ModifyDomainResourceRequest,
    ) -> ddoscoo_20200101_models.ModifyDomainResourceResponse:
        """
        @summary Modifies the forwarding rule of a website.
        
        @param request: ModifyDomainResourceRequest
        @return: ModifyDomainResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_resource_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        """
        @summary Modifies the burstable protection bandwidth of a specified Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyElasticBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the burstable protection bandwidth of a specified Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyElasticBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the burstable protection bandwidth of a specified Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyElasticBandWidthRequest
        @return: ModifyElasticBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBandWidthResponse:
        """
        @summary Modifies the burstable protection bandwidth of a specified Anti-DDoS Proxy (Chinese Mainland) instance.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyElasticBandWidthRequest
        @return: ModifyElasticBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def modify_elastic_biz_band_width_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse:
        """
        @summary Modifies the burstable clean bandwidth for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description Before you call this operation, make sure that you have fully understood the billing method and [pricing](https://help.aliyun.com/document_detail/283754.html) of the burstable clean bandwidth feature. After you call this operation for the first time, the modification immediately takes effect.
        
        @param request: ModifyElasticBizBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBizBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_biz_bandwidth):
            query['ElasticBizBandwidth'] = request.elastic_biz_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBizBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_biz_band_width_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse:
        """
        @summary Modifies the burstable clean bandwidth for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description Before you call this operation, make sure that you have fully understood the billing method and [pricing](https://help.aliyun.com/document_detail/283754.html) of the burstable clean bandwidth feature. After you call this operation for the first time, the modification immediately takes effect.
        
        @param request: ModifyElasticBizBandWidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBizBandWidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_biz_bandwidth):
            query['ElasticBizBandwidth'] = request.elastic_biz_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBizBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_biz_band_width(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizBandWidthRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse:
        """
        @summary Modifies the burstable clean bandwidth for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description Before you call this operation, make sure that you have fully understood the billing method and [pricing](https://help.aliyun.com/document_detail/283754.html) of the burstable clean bandwidth feature. After you call this operation for the first time, the modification immediately takes effect.
        
        @param request: ModifyElasticBizBandWidthRequest
        @return: ModifyElasticBizBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_biz_band_width_with_options(request, runtime)

    async def modify_elastic_biz_band_width_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizBandWidthRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBizBandWidthResponse:
        """
        @summary Modifies the burstable clean bandwidth for an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @description Before you call this operation, make sure that you have fully understood the billing method and [pricing](https://help.aliyun.com/document_detail/283754.html) of the burstable clean bandwidth feature. After you call this operation for the first time, the modification immediately takes effect.
        
        @param request: ModifyElasticBizBandWidthRequest
        @return: ModifyElasticBizBandWidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_biz_band_width_with_options_async(request, runtime)

    def modify_elastic_biz_qps_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBizQpsResponse:
        """
        @summary Configures the burstable QPS and mode of an Anti-DDoS Proxy instance.
        
        @description You can enable burstable QPS only for IPv4 instances.
        
        @param request: ModifyElasticBizQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBizQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ops_elastic_qps):
            query['OpsElasticQps'] = request.ops_elastic_qps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBizQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBizQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_biz_qps_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyElasticBizQpsResponse:
        """
        @summary Configures the burstable QPS and mode of an Anti-DDoS Proxy instance.
        
        @description You can enable burstable QPS only for IPv4 instances.
        
        @param request: ModifyElasticBizQpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticBizQpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ops_elastic_qps):
            query['OpsElasticQps'] = request.ops_elastic_qps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBizQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBizQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_biz_qps(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizQpsRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBizQpsResponse:
        """
        @summary Configures the burstable QPS and mode of an Anti-DDoS Proxy instance.
        
        @description You can enable burstable QPS only for IPv4 instances.
        
        @param request: ModifyElasticBizQpsRequest
        @return: ModifyElasticBizQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_biz_qps_with_options(request, runtime)

    async def modify_elastic_biz_qps_async(
        self,
        request: ddoscoo_20200101_models.ModifyElasticBizQpsRequest,
    ) -> ddoscoo_20200101_models.ModifyElasticBizQpsResponse:
        """
        @summary Configures the burstable QPS and mode of an Anti-DDoS Proxy instance.
        
        @description You can enable burstable QPS only for IPv4 instances.
        
        @param request: ModifyElasticBizQpsRequest
        @return: ModifyElasticBizQpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_biz_qps_with_options_async(request, runtime)

    def modify_full_log_ttl_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        """
        @summary Modifies the log storage duration for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyFullLogTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFullLogTtlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the log storage duration for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyFullLogTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFullLogTtlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the log storage duration for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyFullLogTtlRequest
        @return: ModifyFullLogTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: ddoscoo_20200101_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20200101_models.ModifyFullLogTtlResponse:
        """
        @summary Modifies the log storage duration for Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyFullLogTtlRequest
        @return: ModifyFullLogTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def modify_headers_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyHeadersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHeadersResponse:
        """
        @summary Modifies the custom header of a domain name that is added to an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyHeadersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHeadersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHeaders',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_headers_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyHeadersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHeadersResponse:
        """
        @summary Modifies the custom header of a domain name that is added to an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyHeadersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHeadersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHeaders',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHeadersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_headers(
        self,
        request: ddoscoo_20200101_models.ModifyHeadersRequest,
    ) -> ddoscoo_20200101_models.ModifyHeadersResponse:
        """
        @summary Modifies the custom header of a domain name that is added to an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyHeadersRequest
        @return: ModifyHeadersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_headers_with_options(request, runtime)

    async def modify_headers_async(
        self,
        request: ddoscoo_20200101_models.ModifyHeadersRequest,
    ) -> ddoscoo_20200101_models.ModifyHeadersResponse:
        """
        @summary Modifies the custom header of a domain name that is added to an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyHeadersRequest
        @return: ModifyHeadersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_headers_with_options_async(request, runtime)

    def modify_health_check_config_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        """
        @summary Modifies the Layer 4 or Layer 7 health check configuration of a port forwarding rule.
        
        @param request: ModifyHealthCheckConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHealthCheckConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheckConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Layer 4 or Layer 7 health check configuration of a port forwarding rule.
        
        @param request: ModifyHealthCheckConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHealthCheckConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheckConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Layer 4 or Layer 7 health check configuration of a port forwarding rule.
        
        @param request: ModifyHealthCheckConfigRequest
        @return: ModifyHealthCheckConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    async def modify_health_check_config_async(
        self,
        request: ddoscoo_20200101_models.ModifyHealthCheckConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyHealthCheckConfigResponse:
        """
        @summary Modifies the Layer 4 or Layer 7 health check configuration of a port forwarding rule.
        
        @param request: ModifyHealthCheckConfigRequest
        @return: ModifyHealthCheckConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_health_check_config_with_options_async(request, runtime)

    def modify_http_2enable_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        """
        @summary Enables or disables HTTP/2 for the forwarding rule of a website.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyHttp2EnableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHttp2EnableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHttp2Enable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables HTTP/2 for the forwarding rule of a website.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyHttp2EnableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHttp2EnableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHttp2Enable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables HTTP/2 for the forwarding rule of a website.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyHttp2EnableRequest
        @return: ModifyHttp2EnableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_http_2enable_with_options(request, runtime)

    async def modify_http_2enable_async(
        self,
        request: ddoscoo_20200101_models.ModifyHttp2EnableRequest,
    ) -> ddoscoo_20200101_models.ModifyHttp2EnableResponse:
        """
        @summary Enables or disables HTTP/2 for the forwarding rule of a website.
        
        @description >  This operation is suitable only for Anti-DDoS Proxy (Chinese Mainland).
        
        @param request: ModifyHttp2EnableRequest
        @return: ModifyHttp2EnableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_http_2enable_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        """
        @summary Modifies the description of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the description of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyInstanceRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the description of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyInstanceRemarkRequest
        @return: ModifyInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: ddoscoo_20200101_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20200101_models.ModifyInstanceRemarkResponse:
        """
        @summary Modifies the description of an Anti-DDoS Pro or Anti-DDoS Premium instance.
        
        @param request: ModifyInstanceRemarkRequest
        @return: ModifyInstanceRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def modify_network_rule_attribute_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        """
        @summary Modifies the session persistence settings of a port forwarding rule.
        
        @param request: ModifyNetworkRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkRuleAttribute',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the session persistence settings of a port forwarding rule.
        
        @param request: ModifyNetworkRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkRuleAttribute',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the session persistence settings of a port forwarding rule.
        
        @param request: ModifyNetworkRuleAttributeRequest
        @return: ModifyNetworkRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_network_rule_attribute_with_options(request, runtime)

    async def modify_network_rule_attribute_async(
        self,
        request: ddoscoo_20200101_models.ModifyNetworkRuleAttributeRequest,
    ) -> ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse:
        """
        @summary Modifies the session persistence settings of a port forwarding rule.
        
        @param request: ModifyNetworkRuleAttributeRequest
        @return: ModifyNetworkRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_rule_attribute_with_options_async(request, runtime)

    def modify_ocsp_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyOcspStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyOcspStatusResponse:
        """
        @summary Specifies whether to enable the Online Certificate Status Protocol (OCSP) feature.
        
        @description This feature is available only for a website that supports HTTPS. If HTTPS is selected for Protocol, we recommend that you enable this feature.
        
        @param request: ModifyOcspStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOcspStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOcspStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyOcspStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ocsp_status_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyOcspStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyOcspStatusResponse:
        """
        @summary Specifies whether to enable the Online Certificate Status Protocol (OCSP) feature.
        
        @description This feature is available only for a website that supports HTTPS. If HTTPS is selected for Protocol, we recommend that you enable this feature.
        
        @param request: ModifyOcspStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOcspStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOcspStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyOcspStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ocsp_status(
        self,
        request: ddoscoo_20200101_models.ModifyOcspStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyOcspStatusResponse:
        """
        @summary Specifies whether to enable the Online Certificate Status Protocol (OCSP) feature.
        
        @description This feature is available only for a website that supports HTTPS. If HTTPS is selected for Protocol, we recommend that you enable this feature.
        
        @param request: ModifyOcspStatusRequest
        @return: ModifyOcspStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ocsp_status_with_options(request, runtime)

    async def modify_ocsp_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyOcspStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyOcspStatusResponse:
        """
        @summary Specifies whether to enable the Online Certificate Status Protocol (OCSP) feature.
        
        @description This feature is available only for a website that supports HTTPS. If HTTPS is selected for Protocol, we recommend that you enable this feature.
        
        @param request: ModifyOcspStatusRequest
        @return: ModifyOcspStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_ocsp_status_with_options_async(request, runtime)

    def modify_port_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortResponse:
        """
        @summary Modifies a port forwarding rule.
        
        @description You can call the ModifyPort operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: ModifyPortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_port_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortResponse:
        """
        @summary Modifies a port forwarding rule.
        
        @description You can call the ModifyPort operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: ModifyPortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_port(
        self,
        request: ddoscoo_20200101_models.ModifyPortRequest,
    ) -> ddoscoo_20200101_models.ModifyPortResponse:
        """
        @summary Modifies a port forwarding rule.
        
        @description You can call the ModifyPort operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: ModifyPortRequest
        @return: ModifyPortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_port_with_options(request, runtime)

    async def modify_port_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortRequest,
    ) -> ddoscoo_20200101_models.ModifyPortResponse:
        """
        @summary Modifies a port forwarding rule.
        
        @description You can call the ModifyPort operation by using Terraform. For more information about Terraform, see [What is Terraform?](https://help.aliyun.com/document_detail/95820.html).
        
        @param request: ModifyPortRequest
        @return: ModifyPortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_port_with_options_async(request, runtime)

    def modify_port_auto_cc_status_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        """
        @summary Modifies the Intelligent Protection configuration of a non-website service.
        
        @param request: ModifyPortAutoCcStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPortAutoCcStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.switch):
            query['Switch'] = request.switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Intelligent Protection configuration of a non-website service.
        
        @param request: ModifyPortAutoCcStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPortAutoCcStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.switch):
            query['Switch'] = request.switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Intelligent Protection configuration of a non-website service.
        
        @param request: ModifyPortAutoCcStatusRequest
        @return: ModifyPortAutoCcStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_port_auto_cc_status_with_options(request, runtime)

    async def modify_port_auto_cc_status_async(
        self,
        request: ddoscoo_20200101_models.ModifyPortAutoCcStatusRequest,
    ) -> ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse:
        """
        @summary Modifies the Intelligent Protection configuration of a non-website service.
        
        @param request: ModifyPortAutoCcStatusRequest
        @return: ModifyPortAutoCcStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_port_auto_cc_status_with_options_async(request, runtime)

    def modify_qps_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyQpsModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyQpsModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @param request: ModifyQpsModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQpsModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQpsMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyQpsModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qps_mode_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyQpsModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyQpsModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @param request: ModifyQpsModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQpsModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQpsMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyQpsModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qps_mode(
        self,
        request: ddoscoo_20200101_models.ModifyQpsModeRequest,
    ) -> ddoscoo_20200101_models.ModifyQpsModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @param request: ModifyQpsModeRequest
        @return: ModifyQpsModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_qps_mode_with_options(request, runtime)

    async def modify_qps_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyQpsModeRequest,
    ) -> ddoscoo_20200101_models.ModifyQpsModeResponse:
        """
        @summary Switches between the metering methods of the burstable clean bandwidth feature.
        
        @param request: ModifyQpsModeRequest
        @return: ModifyQpsModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_qps_mode_with_options_async(request, runtime)

    def modify_scene_defense_policy_with_options(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        """
        @summary Modifies a scenario-specific custom policy.
        
        @param request: ModifySceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies a scenario-specific custom policy.
        
        @param request: ModifySceneDefensePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySceneDefensePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies a scenario-specific custom policy.
        
        @param request: ModifySceneDefensePolicyRequest
        @return: ModifySceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scene_defense_policy_with_options(request, runtime)

    async def modify_scene_defense_policy_async(
        self,
        request: ddoscoo_20200101_models.ModifySceneDefensePolicyRequest,
    ) -> ddoscoo_20200101_models.ModifySceneDefensePolicyResponse:
        """
        @summary Modifies a scenario-specific custom policy.
        
        @param request: ModifySceneDefensePolicyRequest
        @return: ModifySceneDefensePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scene_defense_policy_with_options_async(request, runtime)

    def modify_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        """
        @summary Modifies the scheduling rule of Sec-Traffic Manager.
        
        @param request: ModifySchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the scheduling rule of Sec-Traffic Manager.
        
        @param request: ModifySchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the scheduling rule of Sec-Traffic Manager.
        
        @param request: ModifySchedulerRuleRequest
        @return: ModifySchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduler_rule_with_options(request, runtime)

    async def modify_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifySchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.ModifySchedulerRuleResponse:
        """
        @summary Modifies the scheduling rule of Sec-Traffic Manager.
        
        @param request: ModifySchedulerRuleRequest
        @return: ModifySchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduler_rule_with_options_async(request, runtime)

    def modify_tls_config_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        """
        @summary Modifies the Transport Layer Security (TLS) policy configuration for the forwarding rule of a website.
        
        @param request: ModifyTlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTlsConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Transport Layer Security (TLS) policy configuration for the forwarding rule of a website.
        
        @param request: ModifyTlsConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTlsConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTlsConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the Transport Layer Security (TLS) policy configuration for the forwarding rule of a website.
        
        @param request: ModifyTlsConfigRequest
        @return: ModifyTlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tls_config_with_options(request, runtime)

    async def modify_tls_config_async(
        self,
        request: ddoscoo_20200101_models.ModifyTlsConfigRequest,
    ) -> ddoscoo_20200101_models.ModifyTlsConfigResponse:
        """
        @summary Modifies the Transport Layer Security (TLS) policy configuration for the forwarding rule of a website.
        
        @param request: ModifyTlsConfigRequest
        @return: ModifyTlsConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tls_config_with_options_async(request, runtime)

    def modify_web_aiprotect_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        """
        @summary Changes the mode of the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAIProtectModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the mode of the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAIProtectModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the mode of the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectModeRequest
        @return: ModifyWebAIProtectModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_mode_with_options(request, runtime)

    async def modify_web_aiprotect_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectModeResponse:
        """
        @summary Changes the mode of the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectModeRequest
        @return: ModifyWebAIProtectModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_aiprotect_mode_with_options_async(request, runtime)

    def modify_web_aiprotect_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        """
        @summary Enables or disables the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAIProtectSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAIProtectSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectSwitchRequest
        @return: ModifyWebAIProtectSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_switch_with_options(request, runtime)

    async def modify_web_aiprotect_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAIProtectSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse:
        """
        @summary Enables or disables the Intelligent Protection policy for a website.
        
        @param request: ModifyWebAIProtectSwitchRequest
        @return: ModifyWebAIProtectSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_aiprotect_switch_with_options_async(request, runtime)

    def modify_web_access_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        """
        @summary Changes the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyWebAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyWebAccessModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyWebAccessModeRequest
        @return: ModifyWebAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_access_mode_with_options(request, runtime)

    async def modify_web_access_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAccessModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAccessModeResponse:
        """
        @summary Changes the mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium.
        
        @param request: ModifyWebAccessModeRequest
        @return: ModifyWebAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_access_mode_with_options_async(request, runtime)

    def modify_web_area_block_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        """
        @summary Modifies the blocked locations that are configured in the Location Blacklist (Domain Names) policy for a website.
        
        @param request: ModifyWebAreaBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAreaBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the blocked locations that are configured in the Location Blacklist (Domain Names) policy for a website.
        
        @param request: ModifyWebAreaBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAreaBlockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the blocked locations that are configured in the Location Blacklist (Domain Names) policy for a website.
        
        @param request: ModifyWebAreaBlockRequest
        @return: ModifyWebAreaBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_with_options(request, runtime)

    async def modify_web_area_block_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockResponse:
        """
        @summary Modifies the blocked locations that are configured in the Location Blacklist (Domain Names) policy for a website.
        
        @param request: ModifyWebAreaBlockRequest
        @return: ModifyWebAreaBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_area_block_with_options_async(request, runtime)

    def modify_web_area_block_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        """
        @summary Enables or disables the Location Blacklist (Domain Names) policy for a domain name.
        
        @description You can call the ModifyWebAreaBlockSwitch operation to enable or disable the Location Blacklist (Domain Names) policy for a domain name.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebAreaBlockSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAreaBlockSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlockSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Location Blacklist (Domain Names) policy for a domain name.
        
        @description You can call the ModifyWebAreaBlockSwitch operation to enable or disable the Location Blacklist (Domain Names) policy for a domain name.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebAreaBlockSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebAreaBlockSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlockSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Location Blacklist (Domain Names) policy for a domain name.
        
        @description You can call the ModifyWebAreaBlockSwitch operation to enable or disable the Location Blacklist (Domain Names) policy for a domain name.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebAreaBlockSwitchRequest
        @return: ModifyWebAreaBlockSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_switch_with_options(request, runtime)

    async def modify_web_area_block_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebAreaBlockSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse:
        """
        @summary Enables or disables the Location Blacklist (Domain Names) policy for a domain name.
        
        @description You can call the ModifyWebAreaBlockSwitch operation to enable or disable the Location Blacklist (Domain Names) policy for a domain name.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebAreaBlockSwitchRequest
        @return: ModifyWebAreaBlockSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_area_block_switch_with_options_async(request, runtime)

    def modify_web_ccglobal_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCGlobalSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse:
        """
        @summary Enables or disables the HTTP flood mitigation feature for a website.
        
        @param request: ModifyWebCCGlobalSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCCGlobalSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cc_global_switch):
            query['CcGlobalSwitch'] = request.cc_global_switch
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCCGlobalSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_ccglobal_switch_with_options_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCGlobalSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse:
        """
        @summary Enables or disables the HTTP flood mitigation feature for a website.
        
        @param request: ModifyWebCCGlobalSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCCGlobalSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cc_global_switch):
            query['CcGlobalSwitch'] = request.cc_global_switch
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCCGlobalSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_ccglobal_switch(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCGlobalSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse:
        """
        @summary Enables or disables the HTTP flood mitigation feature for a website.
        
        @param request: ModifyWebCCGlobalSwitchRequest
        @return: ModifyWebCCGlobalSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ccglobal_switch_with_options(request, runtime)

    async def modify_web_ccglobal_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCGlobalSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCCGlobalSwitchResponse:
        """
        @summary Enables or disables the HTTP flood mitigation feature for a website.
        
        @param request: ModifyWebCCGlobalSwitchRequest
        @return: ModifyWebCCGlobalSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_ccglobal_switch_with_options_async(request, runtime)

    def modify_web_ccrule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        """
        @deprecated OpenAPI ModifyWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Modifies the custom frequency control rule of a website.
        
        @param request: ModifyWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI ModifyWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Modifies the custom frequency control rule of a website.
        
        @param request: ModifyWebCCRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCCRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @deprecated OpenAPI ModifyWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Modifies the custom frequency control rule of a website.
        
        @param request: ModifyWebCCRuleRequest
        @return: ModifyWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ccrule_with_options(request, runtime)

    async def modify_web_ccrule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCCRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCCRuleResponse:
        """
        @deprecated OpenAPI ModifyWebCCRule is deprecated, please use ddoscoo::2020-01-01::ConfigWebCCRuleV2 instead.
        
        @summary Modifies the custom frequency control rule of a website.
        
        @param request: ModifyWebCCRuleRequest
        @return: ModifyWebCCRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_ccrule_with_options_async(request, runtime)

    def modify_web_cache_custom_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        """
        @summary Modifies the custom rule of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheCustomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheCustomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the custom rule of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheCustomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheCustomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the custom rule of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheCustomRuleRequest
        @return: ModifyWebCacheCustomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_custom_rule_with_options(request, runtime)

    async def modify_web_cache_custom_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheCustomRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse:
        """
        @summary Modifies the custom rule of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheCustomRuleRequest
        @return: ModifyWebCacheCustomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_custom_rule_with_options_async(request, runtime)

    def modify_web_cache_mode_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        """
        @summary Changes the cache mode of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the cache mode of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the cache mode of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheModeRequest
        @return: ModifyWebCacheModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_mode_with_options(request, runtime)

    async def modify_web_cache_mode_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheModeRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheModeResponse:
        """
        @summary Changes the cache mode of the Static Page Caching policy for a website.
        
        @param request: ModifyWebCacheModeRequest
        @return: ModifyWebCacheModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_mode_with_options_async(request, runtime)

    def modify_web_cache_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        """
        @summary Enables or disables the Static Page Caching policy for a website.
        
        @description You can call the ModifyWebCacheSwitch operation to enable or disable the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebCacheSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Static Page Caching policy for a website.
        
        @description You can call the ModifyWebCacheSwitch operation to enable or disable the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebCacheSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebCacheSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Static Page Caching policy for a website.
        
        @description You can call the ModifyWebCacheSwitch operation to enable or disable the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebCacheSwitchRequest
        @return: ModifyWebCacheSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_switch_with_options(request, runtime)

    async def modify_web_cache_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebCacheSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebCacheSwitchResponse:
        """
        @summary Enables or disables the Static Page Caching policy for a website.
        
        @description You can call the ModifyWebCacheSwitch operation to enable or disable the Static Page Caching policy for a website.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyWebCacheSwitchRequest
        @return: ModifyWebCacheSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_cache_switch_with_options_async(request, runtime)

    def modify_web_ip_set_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        """
        @summary Enables or disables the Black Lists and White Lists (Domain Names) policy for a domain name.
        
        @param request: ModifyWebIpSetSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebIpSetSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebIpSetSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Black Lists and White Lists (Domain Names) policy for a domain name.
        
        @param request: ModifyWebIpSetSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebIpSetSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebIpSetSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Black Lists and White Lists (Domain Names) policy for a domain name.
        
        @param request: ModifyWebIpSetSwitchRequest
        @return: ModifyWebIpSetSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ip_set_switch_with_options(request, runtime)

    async def modify_web_ip_set_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebIpSetSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse:
        """
        @summary Enables or disables the Black Lists and White Lists (Domain Names) policy for a domain name.
        
        @param request: ModifyWebIpSetSwitchRequest
        @return: ModifyWebIpSetSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_ip_set_switch_with_options_async(request, runtime)

    def modify_web_precise_access_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        """
        @summary Modifies the accurate access control rule of a website.
        
        @param request: ModifyWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.expires):
            query['Expires'] = request.expires
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the accurate access control rule of a website.
        
        @param request: ModifyWebPreciseAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebPreciseAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.expires):
            query['Expires'] = request.expires
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Modifies the accurate access control rule of a website.
        
        @param request: ModifyWebPreciseAccessRuleRequest
        @return: ModifyWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_rule_with_options(request, runtime)

    async def modify_web_precise_access_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse:
        """
        @summary Modifies the accurate access control rule of a website.
        
        @param request: ModifyWebPreciseAccessRuleRequest
        @return: ModifyWebPreciseAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_precise_access_rule_with_options_async(request, runtime)

    def modify_web_precise_access_switch_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        """
        @summary Enables or disables the Accurate Access Control policy for a website.
        
        @param request: ModifyWebPreciseAccessSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebPreciseAccessSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Accurate Access Control policy for a website.
        
        @param request: ModifyWebPreciseAccessSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebPreciseAccessSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Enables or disables the Accurate Access Control policy for a website.
        
        @param request: ModifyWebPreciseAccessSwitchRequest
        @return: ModifyWebPreciseAccessSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_switch_with_options(request, runtime)

    async def modify_web_precise_access_switch_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchRequest,
    ) -> ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse:
        """
        @summary Enables or disables the Accurate Access Control policy for a website.
        
        @param request: ModifyWebPreciseAccessSwitchRequest
        @return: ModifyWebPreciseAccessSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_precise_access_switch_with_options_async(request, runtime)

    def modify_web_rule_with_options(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        """
        @param request: ModifyWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: ModifyWebRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyWebRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @param request: ModifyWebRuleRequest
        @return: ModifyWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_rule_with_options(request, runtime)

    async def modify_web_rule_async(
        self,
        request: ddoscoo_20200101_models.ModifyWebRuleRequest,
    ) -> ddoscoo_20200101_models.ModifyWebRuleResponse:
        """
        @param request: ModifyWebRuleRequest
        @return: ModifyWebRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_rule_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        """
        @summary The ID of the instance that you want to release.
        > You can release only expired instances. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) operation to query the IDs and expiration status of all instances.
        
        @description The ID of the request, which is used to locate and troubleshoot issues.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The ID of the instance that you want to release.
        > You can release only expired instances. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) operation to query the IDs and expiration status of all instances.
        
        @description The ID of the request, which is used to locate and troubleshoot issues.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary The ID of the instance that you want to release.
        > You can release only expired instances. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) operation to query the IDs and expiration status of all instances.
        
        @description The ID of the request, which is used to locate and troubleshoot issues.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ddoscoo_20200101_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20200101_models.ReleaseInstanceResponse:
        """
        @summary The ID of the instance that you want to release.
        > You can release only expired instances. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) operation to query the IDs and expiration status of all instances.
        
        @description The ID of the request, which is used to locate and troubleshoot issues.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def switch_scheduler_rule_with_options(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        """
        @summary Switches service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switches service traffic back to the associated cloud resources.
        
        @description You can call the SwitchSchedulerRule operation to modify the resources to which service traffic is switched for a scheduling rule. For example, you can switch service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switch the service traffic back to the associated cloud resources.
        Before you call this operation, you must have created a scheduling rule by calling the [CreateSchedulerRule](https://help.aliyun.com/document_detail/157479.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SwitchSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.switch_data):
            query['SwitchData'] = request.switch_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Switches service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switches service traffic back to the associated cloud resources.
        
        @description You can call the SwitchSchedulerRule operation to modify the resources to which service traffic is switched for a scheduling rule. For example, you can switch service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switch the service traffic back to the associated cloud resources.
        Before you call this operation, you must have created a scheduling rule by calling the [CreateSchedulerRule](https://help.aliyun.com/document_detail/157479.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SwitchSchedulerRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSchedulerRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.switch_data):
            query['SwitchData'] = request.switch_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Switches service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switches service traffic back to the associated cloud resources.
        
        @description You can call the SwitchSchedulerRule operation to modify the resources to which service traffic is switched for a scheduling rule. For example, you can switch service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switch the service traffic back to the associated cloud resources.
        Before you call this operation, you must have created a scheduling rule by calling the [CreateSchedulerRule](https://help.aliyun.com/document_detail/157479.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SwitchSchedulerRuleRequest
        @return: SwitchSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_scheduler_rule_with_options(request, runtime)

    async def switch_scheduler_rule_async(
        self,
        request: ddoscoo_20200101_models.SwitchSchedulerRuleRequest,
    ) -> ddoscoo_20200101_models.SwitchSchedulerRuleResponse:
        """
        @summary Switches service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switches service traffic back to the associated cloud resources.
        
        @description You can call the SwitchSchedulerRule operation to modify the resources to which service traffic is switched for a scheduling rule. For example, you can switch service traffic to an Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing or switch the service traffic back to the associated cloud resources.
        Before you call this operation, you must have created a scheduling rule by calling the [CreateSchedulerRule](https://help.aliyun.com/document_detail/157479.html) operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SwitchSchedulerRuleRequest
        @return: SwitchSchedulerRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_scheduler_rule_with_options_async(request, runtime)
