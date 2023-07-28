# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'dcdn.aliyuncs.com',
            'ap-northeast-2-pop': 'dcdn.aliyuncs.com',
            'ap-south-1': 'dcdn.aliyuncs.com',
            'ap-southeast-1': 'dcdn.aliyuncs.com',
            'ap-southeast-2': 'dcdn.aliyuncs.com',
            'ap-southeast-3': 'dcdn.aliyuncs.com',
            'ap-southeast-5': 'dcdn.aliyuncs.com',
            'cn-beijing': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-1': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'dcdn.aliyuncs.com',
            'cn-beijing-gov-1': 'dcdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dcdn.aliyuncs.com',
            'cn-chengdu': 'dcdn.aliyuncs.com',
            'cn-edge-1': 'dcdn.aliyuncs.com',
            'cn-fujian': 'dcdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dcdn.aliyuncs.com',
            'cn-hangzhou': 'dcdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dcdn.aliyuncs.com',
            'cn-hangzhou-finance': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dcdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'dcdn.aliyuncs.com',
            'cn-hongkong': 'dcdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dcdn.aliyuncs.com',
            'cn-huhehaote': 'dcdn.aliyuncs.com',
            'cn-north-2-gov-1': 'dcdn.aliyuncs.com',
            'cn-qingdao': 'dcdn.aliyuncs.com',
            'cn-qingdao-nebula': 'dcdn.aliyuncs.com',
            'cn-shanghai': 'dcdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'dcdn.aliyuncs.com',
            'cn-shanghai-inner': 'dcdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen': 'dcdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen-inner': 'dcdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dcdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dcdn.aliyuncs.com',
            'cn-wuhan': 'dcdn.aliyuncs.com',
            'cn-yushanfang': 'dcdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dcdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dcdn.aliyuncs.com',
            'eu-central-1': 'dcdn.aliyuncs.com',
            'eu-west-1': 'dcdn.aliyuncs.com',
            'eu-west-1-oxs': 'dcdn.aliyuncs.com',
            'me-east-1': 'dcdn.aliyuncs.com',
            'rus-west-1-pop': 'dcdn.aliyuncs.com',
            'us-east-1': 'dcdn.aliyuncs.com',
            'us-west-1': 'dcdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        """
        >
        *   Dynamic Content Delivery Network (DCDN) is activated.
        *   Internet content provider (ICP) filing is complete for the accelerated domain name.
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: AddDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        """
        >
        *   Dynamic Content Delivery Network (DCDN) is activated.
        *   Internet content provider (ICP) filing is complete for the accelerated domain name.
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: AddDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dcdn_domain(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        """
        >
        *   Dynamic Content Delivery Network (DCDN) is activated.
        *   Internet content provider (ICP) filing is complete for the accelerated domain name.
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: AddDcdnDomainRequest
        @return: AddDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    async def add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        """
        >
        *   Dynamic Content Delivery Network (DCDN) is activated.
        *   Internet content provider (ICP) filing is complete for the accelerated domain name.
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: AddDcdnDomainRequest
        @return: AddDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_domain_with_options_async(request, runtime)

    def add_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        """
        >
        *   Make sure that the IPA service is activated before you add a domain name to accelerate.
        *   Make sure that the Internet content provider (ICP) filling is complete for the domain name to accelerate.
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review is complete by the end of the next business day after you submit the request.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: AddDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        """
        >
        *   Make sure that the IPA service is activated before you add a domain name to accelerate.
        *   Make sure that the Internet content provider (ICP) filling is complete for the domain name to accelerate.
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review is complete by the end of the next business day after you submit the request.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: AddDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        """
        >
        *   Make sure that the IPA service is activated before you add a domain name to accelerate.
        *   Make sure that the Internet content provider (ICP) filling is complete for the domain name to accelerate.
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review is complete by the end of the next business day after you submit the request.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: AddDcdnIpaDomainRequest
        @return: AddDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    async def add_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        """
        >
        *   Make sure that the IPA service is activated before you add a domain name to accelerate.
        *   Make sure that the Internet content provider (ICP) filling is complete for the domain name to accelerate.
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review is complete by the end of the next business day after you submit the request.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: AddDcdnIpaDomainRequest
        @return: AddDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_ipa_domain_with_options_async(request, runtime)

    def batch_add_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        """
        *Prerequisites**:
        *   The [DCDN service is activated](~~64926~~).
        *   Internet content provider (ICP) filing is complete for the accelerated domain names.
        >
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        """
        *Prerequisites**:
        *   The [DCDN service is activated](~~64926~~).
        *   Internet content provider (ICP) filing is complete for the accelerated domain names.
        >
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        """
        *Prerequisites**:
        *   The [DCDN service is activated](~~64926~~).
        *   Internet content provider (ICP) filing is complete for the accelerated domain names.
        >
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddDcdnDomainRequest
        @return: BatchAddDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    async def batch_add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        """
        *Prerequisites**:
        *   The [DCDN service is activated](~~64926~~).
        *   Internet content provider (ICP) filing is complete for the accelerated domain names.
        >
        *   If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. After you submit the request, the review is complete by the end of the following business day.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddDcdnDomainRequest
        @return: BatchAddDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_dcdn_domain_with_options_async(request, runtime)

    def batch_create_dcdn_waf_rules_with_options(
        self,
        request: dcdn_20180115_models.BatchCreateDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchCreateDcdnWafRulesResponse:
        """
        The ID of the request.
        
        @param request: BatchCreateDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchCreateDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_dcdn_waf_rules_with_options_async(
        self,
        request: dcdn_20180115_models.BatchCreateDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchCreateDcdnWafRulesResponse:
        """
        The ID of the request.
        
        @param request: BatchCreateDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchCreateDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_dcdn_waf_rules(
        self,
        request: dcdn_20180115_models.BatchCreateDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchCreateDcdnWafRulesResponse:
        """
        The ID of the request.
        
        @param request: BatchCreateDcdnWafRulesRequest
        @return: BatchCreateDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_dcdn_waf_rules_with_options(request, runtime)

    async def batch_create_dcdn_waf_rules_async(
        self,
        request: dcdn_20180115_models.BatchCreateDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchCreateDcdnWafRulesResponse:
        """
        The ID of the request.
        
        @param request: BatchCreateDcdnWafRulesRequest
        @return: BatchCreateDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        """
        > - You can specify up to 50 domain names in each request.
        > - You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        """
        > - You can specify up to 50 domain names in each request.
        > - You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        """
        > - You can specify up to 50 domain names in each request.
        > - You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteDcdnDomainConfigsRequest
        @return: BatchDeleteDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    async def batch_delete_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        """
        > - You can specify up to 50 domain names in each request.
        > - You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteDcdnDomainConfigsRequest
        @return: BatchDeleteDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_delete_dcdn_waf_rules_with_options(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchDeleteDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_ids):
            body['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_dcdn_waf_rules_with_options_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchDeleteDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_ids):
            body['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_dcdn_waf_rules(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchDeleteDcdnWafRulesRequest
        @return: BatchDeleteDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_waf_rules_with_options(request, runtime)

    async def batch_delete_dcdn_waf_rules_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnWafRulesResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchDeleteDcdnWafRulesRequest
        @return: BatchDeleteDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_modify_dcdn_waf_rules_with_options(
        self,
        request: dcdn_20180115_models.BatchModifyDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchModifyDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: BatchModifyDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchModifyDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchModifyDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_modify_dcdn_waf_rules_with_options_async(
        self,
        request: dcdn_20180115_models.BatchModifyDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchModifyDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: BatchModifyDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchModifyDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.rule_configs):
            body['RuleConfigs'] = request.rule_configs
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchModifyDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_modify_dcdn_waf_rules(
        self,
        request: dcdn_20180115_models.BatchModifyDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchModifyDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: BatchModifyDcdnWafRulesRequest
        @return: BatchModifyDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_modify_dcdn_waf_rules_with_options(request, runtime)

    async def batch_modify_dcdn_waf_rules_async(
        self,
        request: dcdn_20180115_models.BatchModifyDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.BatchModifyDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: BatchModifyDcdnWafRulesRequest
        @return: BatchModifyDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_modify_dcdn_waf_rules_with_options_async(request, runtime)

    def batch_set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: BatchSetDcdnDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: BatchSetDcdnDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_domain_certificate(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: BatchSetDcdnDomainCertificateRequest
        @return: BatchSetDcdnDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_certificate_with_options(request, runtime)

    async def batch_set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: BatchSetDcdnDomainCertificateRequest
        @return: BatchSetDcdnDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_certificate_with_options_async(request, runtime)

    def batch_set_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        """
        >  You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,)
        > * You can call this operation up to 30 times per second per account.
        
        @param request: BatchSetDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        """
        >  You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,)
        > * You can call this operation up to 30 times per second per account.
        
        @param request: BatchSetDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        """
        >  You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,)
        > * You can call this operation up to 30 times per second per account.
        
        @param request: BatchSetDcdnDomainConfigsRequest
        @return: BatchSetDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        """
        >  You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,)
        > * You can call this operation up to 30 times per second per account.
        
        @param request: BatchSetDcdnDomainConfigsRequest
        @return: BatchSetDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: BatchSetDcdnIpaDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnIpaDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: BatchSetDcdnIpaDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnIpaDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_ipa_domain_configs(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: BatchSetDcdnIpaDomainConfigsRequest
        @return: BatchSetDcdnIpaDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: BatchSetDcdnIpaDomainConfigsRequest
        @return: BatchSetDcdnIpaDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_waf_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnWafDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchSetDcdnWafDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnWafDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ip_tag):
            body['ClientIpTag'] = request.client_ip_tag
        if not UtilClient.is_unset(request.defense_status):
            body['DefenseStatus'] = request.defense_status
        if not UtilClient.is_unset(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnWafDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_dcdn_waf_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnWafDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchSetDcdnWafDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDcdnWafDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ip_tag):
            body['ClientIpTag'] = request.client_ip_tag
        if not UtilClient.is_unset(request.defense_status):
            body['DefenseStatus'] = request.defense_status
        if not UtilClient.is_unset(request.domain_names):
            body['DomainNames'] = request.domain_names
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSetDcdnWafDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_dcdn_waf_domain_configs(
        self,
        request: dcdn_20180115_models.BatchSetDcdnWafDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchSetDcdnWafDomainConfigsRequest
        @return: BatchSetDcdnWafDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_waf_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_waf_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnWafDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnWafDomainConfigsResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: BatchSetDcdnWafDomainConfigsRequest
        @return: BatchSetDcdnWafDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_waf_domain_configs_with_options_async(request, runtime)

    def batch_start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStartDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStartDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStartDcdnDomainRequest
        @return: BatchStartDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    async def batch_start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStartDcdnDomainRequest
        @return: BatchStartDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_dcdn_domain_with_options_async(request, runtime)

    def batch_stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        """
        >
        *   After an accelerated domain name is disabled, Dynamic Content Delivery Network (DCDN) retains the domain name information. The system automatically reroutes all requests that are destined for the accelerated domain name to the origin.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStopDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        """
        >
        *   After an accelerated domain name is disabled, Dynamic Content Delivery Network (DCDN) retains the domain name information. The system automatically reroutes all requests that are destined for the accelerated domain name to the origin.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStopDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        """
        >
        *   After an accelerated domain name is disabled, Dynamic Content Delivery Network (DCDN) retains the domain name information. The system automatically reroutes all requests that are destined for the accelerated domain name to the origin.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStopDcdnDomainRequest
        @return: BatchStopDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    async def batch_stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        """
        >
        *   After an accelerated domain name is disabled, Dynamic Content Delivery Network (DCDN) retains the domain name information. The system automatically reroutes all requests that are destined for the accelerated domain name to the origin.
        *   You can specify up to 50 domain names in each request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: BatchStopDcdnDomainRequest
        @return: BatchStopDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_dcdn_domain_with_options_async(request, runtime)

    def check_dcdn_project_exist_with_options(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CheckDcdnProjectExistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDcdnProjectExistResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDcdnProjectExist',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CheckDcdnProjectExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dcdn_project_exist_with_options_async(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CheckDcdnProjectExistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDcdnProjectExistResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDcdnProjectExist',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CheckDcdnProjectExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dcdn_project_exist(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CheckDcdnProjectExistRequest
        @return: CheckDcdnProjectExistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_dcdn_project_exist_with_options(request, runtime)

    async def check_dcdn_project_exist_async(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CheckDcdnProjectExistRequest
        @return: CheckDcdnProjectExistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_dcdn_project_exist_with_options_async(request, runtime)

    def commit_staging_routine_code_with_options(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        """
        >  The call frequency of the API is no more than 100 queries per second.
        
        @param request: CommitStagingRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitStagingRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_staging_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        """
        >  The call frequency of the API is no more than 100 queries per second.
        
        @param request: CommitStagingRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitStagingRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_staging_routine_code(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        """
        >  The call frequency of the API is no more than 100 queries per second.
        
        @param request: CommitStagingRoutineCodeRequest
        @return: CommitStagingRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.commit_staging_routine_code_with_options(request, runtime)

    async def commit_staging_routine_code_async(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        """
        >  The call frequency of the API is no more than 100 queries per second.
        
        @param request: CommitStagingRoutineCodeRequest
        @return: CommitStagingRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.commit_staging_routine_code_with_options_async(request, runtime)

    def create_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_deliver_task_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_deliver_task(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnDeliverTaskRequest
        @return: CreateDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_deliver_task_with_options(request, runtime)

    async def create_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnDeliverTaskRequest
        @return: CreateDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_deliver_task_with_options_async(request, runtime)

    def create_dcdn_slsreal_time_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CreateDcdnSLSRealTimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnSLSRealTimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSLSRealTimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_slsreal_time_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CreateDcdnSLSRealTimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnSLSRealTimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSLSRealTimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_slsreal_time_log_delivery(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CreateDcdnSLSRealTimeLogDeliveryRequest
        @return: CreateDcdnSLSRealTimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_slsreal_time_log_delivery_with_options(request, runtime)

    async def create_dcdn_slsreal_time_log_delivery_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: CreateDcdnSLSRealTimeLogDeliveryRequest
        @return: CreateDcdnSLSRealTimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_slsreal_time_log_delivery_with_options_async(request, runtime)

    def create_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        """
        >
        *   This operation allows you to customize an operations report for a specific domain name. You can view the statistics about the domain name in the report.
        *   You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnSubTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_sub_task_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        """
        >
        *   This operation allows you to customize an operations report for a specific domain name. You can view the statistics about the domain name in the report.
        *   You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnSubTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_sub_task(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        """
        >
        *   This operation allows you to customize an operations report for a specific domain name. You can view the statistics about the domain name in the report.
        *   You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnSubTaskRequest
        @return: CreateDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_sub_task_with_options(request, runtime)

    async def create_dcdn_sub_task_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        """
        >
        *   This operation allows you to customize an operations report for a specific domain name. You can view the statistics about the domain name in the report.
        *   You can call this operation up to three times per second per account.
        
        @param request: CreateDcdnSubTaskRequest
        @return: CreateDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_sub_task_with_options_async(request, runtime)

    def create_dcdn_waf_policy_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnWafPolicyResponse:
        """
        You can call this operation up to 20 times per second per user.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: CreateDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.defense_scene):
            body['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_waf_policy_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnWafPolicyResponse:
        """
        You can call this operation up to 20 times per second per user.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: CreateDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.defense_scene):
            body['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        if not UtilClient.is_unset(request.policy_type):
            body['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_waf_policy(
        self,
        request: dcdn_20180115_models.CreateDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.CreateDcdnWafPolicyResponse:
        """
        You can call this operation up to 20 times per second per user.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: CreateDcdnWafPolicyRequest
        @return: CreateDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_waf_policy_with_options(request, runtime)

    async def create_dcdn_waf_policy_async(
        self,
        request: dcdn_20180115_models.CreateDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.CreateDcdnWafPolicyResponse:
        """
        You can call this operation up to 20 times per second per user.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: CreateDcdnWafPolicyRequest
        @return: CreateDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_waf_policy_with_options_async(request, runtime)

    def create_routine_with_options(
        self,
        tmp_req: dcdn_20180115_models.CreateRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        """
        >
        *   The parameters must comply with the rules of EnvConf. The description of a routine cannot exceed 50 characters in length.
        *   This operation creates a routine that contains only production and staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: CreateRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_routine_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.CreateRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        """
        >
        *   The parameters must comply with the rules of EnvConf. The description of a routine cannot exceed 50 characters in length.
        *   This operation creates a routine that contains only production and staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: CreateRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_routine(
        self,
        request: dcdn_20180115_models.CreateRoutineRequest,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        """
        >
        *   The parameters must comply with the rules of EnvConf. The description of a routine cannot exceed 50 characters in length.
        *   This operation creates a routine that contains only production and staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: CreateRoutineRequest
        @return: CreateRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    async def create_routine_async(
        self,
        request: dcdn_20180115_models.CreateRoutineRequest,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        """
        >
        *   The parameters must comply with the rules of EnvConf. The description of a routine cannot exceed 50 characters in length.
        *   This operation creates a routine that contains only production and staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: CreateRoutineRequest
        @return: CreateRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_routine_with_options_async(request, runtime)

    def create_slr_and_sls_project_with_options(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: CreateSlrAndSlsProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSlrAndSlsProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlrAndSlsProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateSlrAndSlsProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slr_and_sls_project_with_options_async(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: CreateSlrAndSlsProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSlrAndSlsProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlrAndSlsProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateSlrAndSlsProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slr_and_sls_project(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: CreateSlrAndSlsProjectRequest
        @return: CreateSlrAndSlsProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_slr_and_sls_project_with_options(request, runtime)

    async def create_slr_and_sls_project_async(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: CreateSlrAndSlsProjectRequest
        @return: CreateSlrAndSlsProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_slr_and_sls_project_with_options_async(request, runtime)

    def delete_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 3.
        
        @param request: DeleteDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_deliver_task_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 3.
        
        @param request: DeleteDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_deliver_task(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 3.
        
        @param request: DeleteDcdnDeliverTaskRequest
        @return: DeleteDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_deliver_task_with_options(request, runtime)

    async def delete_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 3.
        
        @param request: DeleteDcdnDeliverTaskRequest
        @return: DeleteDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_deliver_task_with_options_async(request, runtime)

    def delete_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        """
        >    Before you delete your domain name, you must request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        > *   If you call the **DeleteDcdnDomain** operation, all the information about the accelerated domain name is deleted. If you want to disable an accelerated domain name, call the [StopDcdnDomain](~~130622~~) operation.
        > *   The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DeleteDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        """
        >    Before you delete your domain name, you must request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        > *   If you call the **DeleteDcdnDomain** operation, all the information about the accelerated domain name is deleted. If you want to disable an accelerated domain name, call the [StopDcdnDomain](~~130622~~) operation.
        > *   The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DeleteDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_domain(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        """
        >    Before you delete your domain name, you must request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        > *   If you call the **DeleteDcdnDomain** operation, all the information about the accelerated domain name is deleted. If you want to disable an accelerated domain name, call the [StopDcdnDomain](~~130622~~) operation.
        > *   The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DeleteDcdnDomainRequest
        @return: DeleteDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    async def delete_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        """
        >    Before you delete your domain name, you must request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        > *   If you call the **DeleteDcdnDomain** operation, all the information about the accelerated domain name is deleted. If you want to disable an accelerated domain name, call the [StopDcdnDomain](~~130622~~) operation.
        > *   The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DeleteDcdnDomainRequest
        @return: DeleteDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        """
        >
        *   Before you delete your domain name, we recommend that you request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        *   This operation deletes all records of the specified accelerated domain name. If you want to temporarily disable an accelerated domain name, call the **StopDcdnIpaDomain** operation.****\
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        """
        >
        *   Before you delete your domain name, we recommend that you request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        *   This operation deletes all records of the specified accelerated domain name. If you want to temporarily disable an accelerated domain name, call the **StopDcdnIpaDomain** operation.****\
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        """
        >
        *   Before you delete your domain name, we recommend that you request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        *   This operation deletes all records of the specified accelerated domain name. If you want to temporarily disable an accelerated domain name, call the **StopDcdnIpaDomain** operation.****\
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaDomainRequest
        @return: DeleteDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    async def delete_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        """
        >
        *   Before you delete your domain name, we recommend that you request the Domain Name System (DNS) provider to restore the A record of the domain name. Otherwise, the domain name may become inaccessible after you delete it.
        *   This operation deletes all records of the specified accelerated domain name. If you want to temporarily disable an accelerated domain name, call the **StopDcdnIpaDomain** operation.****\
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaDomainRequest
        @return: DeleteDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnIpaSpecificConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnIpaSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_ipa_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnIpaSpecificConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnIpaSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_ipa_specific_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaSpecificConfigRequest
        @return: DeleteDcdnIpaSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    async def delete_dcdn_ipa_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DeleteDcdnIpaSpecificConfigRequest
        @return: DeleteDcdnIpaSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_specific_config_with_options_async(request, runtime)

    def delete_dcdn_kv_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnKvResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_kv_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnKvResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_kv(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvRequest,
    ) -> dcdn_20180115_models.DeleteDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_kv_with_options(request, runtime)

    async def delete_dcdn_kv_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvRequest,
    ) -> dcdn_20180115_models.DeleteDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_kv_with_options_async(request, runtime)

    def delete_dcdn_kv_namespace_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_kv_namespace_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_kv_namespace(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.DeleteDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_kv_namespace_with_options(request, runtime)

    async def delete_dcdn_kv_namespace_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.DeleteDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_kv_namespace_with_options_async(request, runtime)

    def delete_dcdn_real_time_log_project_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DeleteDcdnRealTimeLogProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnRealTimeLogProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnRealTimeLogProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_real_time_log_project_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DeleteDcdnRealTimeLogProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnRealTimeLogProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnRealTimeLogProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_real_time_log_project(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DeleteDcdnRealTimeLogProjectRequest
        @return: DeleteDcdnRealTimeLogProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_real_time_log_project_with_options(request, runtime)

    async def delete_dcdn_real_time_log_project_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DeleteDcdnRealTimeLogProjectRequest
        @return: DeleteDcdnRealTimeLogProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_real_time_log_project_with_options_async(request, runtime)

    def delete_dcdn_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteDcdnSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSpecificConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteDcdnSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSpecificConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_specific_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteDcdnSpecificConfigRequest
        @return: DeleteDcdnSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    async def delete_dcdn_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteDcdnSpecificConfigRequest
        @return: DeleteDcdnSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_config_with_options_async(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteDcdnSpecificStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSpecificStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnSpecificStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_specific_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteDcdnSpecificStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSpecificStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnSpecificStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_specific_staging_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteDcdnSpecificStagingConfigRequest
        @return: DeleteDcdnSpecificStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    async def delete_dcdn_specific_staging_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteDcdnSpecificStagingConfigRequest
        @return: DeleteDcdnSpecificStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_staging_config_with_options_async(request, runtime)

    def delete_dcdn_sub_task_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        """
        > You can call this operation up to 3 times per second per account.
        
        @param request: DeleteDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSubTaskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DeleteDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_sub_task_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        """
        > You can call this operation up to 3 times per second per account.
        
        @param request: DeleteDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnSubTaskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DeleteDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_sub_task(self) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        """
        > You can call this operation up to 3 times per second per account.
        
        @return: DeleteDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_sub_task_with_options(runtime)

    async def delete_dcdn_sub_task_async(self) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        """
        > You can call this operation up to 3 times per second per account.
        
        @return: DeleteDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_sub_task_with_options_async(runtime)

    def delete_dcdn_waf_policy_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: DeleteDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dcdn_waf_policy_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: DeleteDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dcdn_waf_policy(
        self,
        request: dcdn_20180115_models.DeleteDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.DeleteDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: DeleteDcdnWafPolicyRequest
        @return: DeleteDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_waf_policy_with_options(request, runtime)

    async def delete_dcdn_waf_policy_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.DeleteDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: DeleteDcdnWafPolicyRequest
        @return: DeleteDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_waf_policy_with_options_async(request, runtime)

    def delete_routine_with_options(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineRequest
        @return: DeleteRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    async def delete_routine_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineRequest
        @return: DeleteRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_with_options_async(request, runtime)

    def delete_routine_code_revision_with_options(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_code_revision_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_code_revision(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineCodeRevisionRequest
        @return: DeleteRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_code_revision_with_options(request, runtime)

    async def delete_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineCodeRevisionRequest
        @return: DeleteRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_code_revision_with_options_async(request, runtime)

    def delete_routine_conf_envs_with_options(
        self,
        tmp_req: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        """
        >
        *   This operation deletes only custom preset canary release environments. You cannot delete production or staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: DeleteRoutineConfEnvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineConfEnvsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineConfEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_conf_envs_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        """
        >
        *   This operation deletes only custom preset canary release environments. You cannot delete production or staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: DeleteRoutineConfEnvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineConfEnvsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineConfEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_conf_envs(
        self,
        request: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        """
        >
        *   This operation deletes only custom preset canary release environments. You cannot delete production or staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineConfEnvsRequest
        @return: DeleteRoutineConfEnvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_conf_envs_with_options(request, runtime)

    async def delete_routine_conf_envs_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        """
        >
        *   This operation deletes only custom preset canary release environments. You cannot delete production or staging environments.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRoutineConfEnvsRequest
        @return: DeleteRoutineConfEnvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_conf_envs_with_options_async(request, runtime)

    def describe_dcdn_acl_fields_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnAclFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnAclFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnAclFields',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnAclFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_acl_fields_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnAclFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnAclFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnAclFields',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnAclFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_acl_fields(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnAclFieldsRequest
        @return: DescribeDcdnAclFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_acl_fields_with_options(request, runtime)

    async def describe_dcdn_acl_fields_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnAclFieldsRequest
        @return: DescribeDcdnAclFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_acl_fields_with_options_async(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both of them empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range from the start time to the end time is 31 days. The start time is specified by the StartTime parameter and the end time is specified by the EndTime parameter.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBgpBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_port):
            query['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_bgp_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both of them empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range from the start time to the end time is 31 days. The start time is specified by the StartTime parameter and the end time is specified by the EndTime parameter.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBgpBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_port):
            query['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_bgp_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both of them empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range from the start time to the end time is 31 days. The start time is specified by the StartTime parameter and the end time is specified by the EndTime parameter.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpBpsDataRequest
        @return: DescribeDcdnBgpBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    async def describe_dcdn_bgp_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both of them empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range from the start time to the end time is 31 days. The start time is specified by the StartTime parameter and the end time is specified by the EndTime parameter.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpBpsDataRequest
        @return: DescribeDcdnBgpBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_bps_data_with_options_async(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range that you can specify is 31 days. StartTime specifies the start time and EndTime specifies the end time of the time range.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBgpTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_bgp_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range that you can specify is 31 days. StartTime specifies the start time and EndTime specifies the end time of the time range.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBgpTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_bgp_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range that you can specify is 31 days. StartTime specifies the start time and EndTime specifies the end time of the time range.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpTrafficDataRequest
        @return: DescribeDcdnBgpTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    async def describe_dcdn_bgp_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        *   If you specify multiple Internet service providers (ISPs), the data for the ISPs is aggregated.
        *   You can query data in the last 90 days.
        *   The maximum time range that you can specify is 31 days. StartTime specifies the start time and EndTime specifies the end time of the time range.
        *   If the time range from the start time to the end time is 72 hours or shorter, you can specify the interval as 5 minutes. If the time range is longer than 72 hours, you must specify the interval as 1 hour.
        *   You can call this operation up to five times per second per account.
        
        @param request: DescribeDcdnBgpTrafficDataRequest
        @return: DescribeDcdnBgpTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_blocked_regions_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnBlockedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBlockedRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBlockedRegions',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_blocked_regions_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnBlockedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnBlockedRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBlockedRegions',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_blocked_regions(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnBlockedRegionsRequest
        @return: DescribeDcdnBlockedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_blocked_regions_with_options(request, runtime)

    async def describe_dcdn_blocked_regions_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnBlockedRegionsRequest
        @return: DescribeDcdnBlockedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_blocked_regions_with_options_async(request, runtime)

    def describe_dcdn_certificate_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_certificate_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_certificate_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateDetailRequest
        @return: DescribeDcdnCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    async def describe_dcdn_certificate_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateDetailRequest
        @return: DescribeDcdnCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_detail_with_options_async(request, runtime)

    def describe_dcdn_certificate_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_certificate_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_certificate_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateListRequest
        @return: DescribeDcdnCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    async def describe_dcdn_certificate_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnCertificateListRequest
        @return: DescribeDcdnCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_list_with_options_async(request, runtime)

    def describe_dcdn_deleted_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDeletedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDeletedDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeletedDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_deleted_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDeletedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDeletedDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeletedDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_deleted_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDeletedDomainsRequest
        @return: DescribeDcdnDeletedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deleted_domains_with_options(request, runtime)

    async def describe_dcdn_deleted_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDeletedDomainsRequest
        @return: DescribeDcdnDeletedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_deleted_domains_with_options_async(request, runtime)

    def describe_dcdn_deliver_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        """
        *\
        **You can call this operation up to three times per second.
        
        @param request: DescribeDcdnDeliverListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDeliverListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeliverList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_deliver_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        """
        *\
        **You can call this operation up to three times per second.
        
        @param request: DescribeDcdnDeliverListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDeliverListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeliverList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_deliver_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        """
        *\
        **You can call this operation up to three times per second.
        
        @param request: DescribeDcdnDeliverListRequest
        @return: DescribeDcdnDeliverListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deliver_list_with_options(request, runtime)

    async def describe_dcdn_deliver_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        """
        *\
        **You can call this operation up to three times per second.
        
        @param request: DescribeDcdnDeliverListRequest
        @return: DescribeDcdnDeliverListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_deliver_list_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainBpsDataRequest
        @return: DescribeDcdnDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainBpsDataRequest
        @return: DescribeDcdnDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_by_layer_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainBpsDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_bps_data_by_layer_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainBpsDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_bps_data_by_layer(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_by_layer_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainByCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainByCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainByCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_by_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainByCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainByCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainByCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_by_certificate(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainByCertificateRequest
        @return: DescribeDcdnDomainByCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    async def describe_dcdn_domain_by_certificate_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainByCertificateRequest
        @return: DescribeDcdnDomainByCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_dcdn_domain_cc_activity_log_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        """
        >
        *   If you do not configure the StartTime or EndTime parameter, data collected over the last 24 hours is queried. If you configure both the StartTime and EndTime parameters, data collected within the specified time range is queried.
        *   You can query data collected over the last 30 days.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: DescribeDcdnDomainCcActivityLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCcActivityLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trigger_object):
            query['TriggerObject'] = request.trigger_object
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCcActivityLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_cc_activity_log_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        """
        >
        *   If you do not configure the StartTime or EndTime parameter, data collected over the last 24 hours is queried. If you configure both the StartTime and EndTime parameters, data collected within the specified time range is queried.
        *   You can query data collected over the last 30 days.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: DescribeDcdnDomainCcActivityLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCcActivityLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trigger_object):
            query['TriggerObject'] = request.trigger_object
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCcActivityLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_cc_activity_log(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        """
        >
        *   If you do not configure the StartTime or EndTime parameter, data collected over the last 24 hours is queried. If you configure both the StartTime and EndTime parameters, data collected within the specified time range is queried.
        *   You can query data collected over the last 30 days.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: DescribeDcdnDomainCcActivityLogRequest
        @return: DescribeDcdnDomainCcActivityLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cc_activity_log_with_options(request, runtime)

    async def describe_dcdn_domain_cc_activity_log_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        """
        >
        *   If you do not configure the StartTime or EndTime parameter, data collected over the last 24 hours is queried. If you configure both the StartTime and EndTime parameters, data collected within the specified time range is queried.
        *   You can query data collected over the last 30 days.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: DescribeDcdnDomainCcActivityLogRequest
        @return: DescribeDcdnDomainCcActivityLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        """
        The ID of the request.
        
        @param request: DescribeDcdnDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCertificateInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_certificate_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        """
        The ID of the request.
        
        @param request: DescribeDcdnDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCertificateInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_certificate_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        """
        The ID of the request.
        
        @param request: DescribeDcdnDomainCertificateInfoRequest
        @return: DescribeDcdnDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    async def describe_dcdn_domain_certificate_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        """
        The ID of the request.
        
        @param request: DescribeDcdnDomainCertificateInfoRequest
        @return: DescribeDcdnDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_dcdn_domain_cname_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnDomainCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCnameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCname',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_cname_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnDomainCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainCnameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCname',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_cname(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnDomainCnameRequest
        @return: DescribeDcdnDomainCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    async def describe_dcdn_domain_cname_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnDomainCnameRequest
        @return: DescribeDcdnDomainCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_cname_with_options_async(request, runtime)

    def describe_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        """
        >
        *   You can query the configurations of one or more features in a request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        """
        >
        *   You can query the configurations of one or more features in a request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        """
        >
        *   You can query the configurations of one or more features in a request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainConfigsRequest
        @return: DescribeDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    async def describe_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        """
        >
        *   You can query the configurations of one or more features in a request.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainConfigsRequest
        @return: DescribeDcdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainDetailRequest
        @return: DescribeDcdnDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    async def describe_dcdn_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnDomainDetailRequest
        @return: DescribeDcdnDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHitRateDataRequest
        @return: DescribeDcdnDomainHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHitRateDataRequest
        @return: DescribeDcdnDomainHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainHttpCodeDataRequest
        @return: DescribeDcdnDomainHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainHttpCodeDataRequest
        @return: DescribeDcdnDomainHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_by_layer_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   You cannot query the distribution of HTTP status codes by IP protocol.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHttpCodeDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHttpCodeDataByLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHttpCodeDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_by_layer_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   You cannot query the distribution of HTTP status codes by IP protocol.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHttpCodeDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainHttpCodeDataByLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainHttpCodeDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_http_code_data_by_layer(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   You cannot query the distribution of HTTP status codes by IP protocol.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHttpCodeDataByLayerRequest
        @return: DescribeDcdnDomainHttpCodeDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_by_layer_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataByLayerResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   You cannot query the distribution of HTTP status codes by IP protocol.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainHttpCodeDataByLayerRequest
        @return: DescribeDcdnDomainHttpCodeDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        """
        >
        *   The bandwidth is measured in bit/s.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        """
        >
        *   The bandwidth is measured in bit/s.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        """
        >
        *   The bandwidth is measured in bit/s.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaBpsDataRequest
        @return: DescribeDcdnDomainIpaBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        """
        >
        *   The bandwidth is measured in bit/s.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaBpsDataRequest
        @return: DescribeDcdnDomainIpaBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_conn_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   The minimum time granularity at which the data is queried is 5 minutes. The maximum time range for a single query is 31 days. The period within which historical data is available is 366 days. The data latency is no more than 10 minutes.
        
        @param request: DescribeDcdnDomainIpaConnDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaConnDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaConnData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_conn_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   The minimum time granularity at which the data is queried is 5 minutes. The maximum time range for a single query is 31 days. The period within which historical data is available is 366 days. The data latency is no more than 10 minutes.
        
        @param request: DescribeDcdnDomainIpaConnDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaConnDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaConnData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_conn_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaConnDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   The minimum time granularity at which the data is queried is 5 minutes. The maximum time range for a single query is 31 days. The period within which historical data is available is 366 days. The data latency is no more than 10 minutes.
        
        @param request: DescribeDcdnDomainIpaConnDataRequest
        @return: DescribeDcdnDomainIpaConnDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_conn_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_conn_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaConnDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaConnDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   The minimum time granularity at which the data is queried is 5 minutes. The maximum time range for a single query is 31 days. The period within which historical data is available is 366 days. The data latency is no more than 10 minutes.
        
        @param request: DescribeDcdnDomainIpaConnDataRequest
        @return: DescribeDcdnDomainIpaConnDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_conn_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        """
        >
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   Unit: bytes.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_ipa_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        """
        >
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   Unit: bytes.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIpaTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        """
        >
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   Unit: bytes.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaTrafficDataRequest
        @return: DescribeDcdnDomainIpaTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        """
        >
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        *   Unit: bytes.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainIpaTrafficDataRequest
        @return: DescribeDcdnDomainIpaTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   If **StartTime** is set but **EndTime** is not set, the data within the hour that starts from **StartTime** is queried.
        *   If **EndTime** is set but **StartTime** is not set, the data within the last hour that precedes **EndTime** is queried.
        *   You can query data of a domain name or all domain names that belong to your account.
        *   You can view data that is collected over the last seven days. The interval at which data is queried is based on the time range specified by **StartTime** and **EndTime**.
        *   **If the time range is shorter than or equal to one hour**, data is queried every minute.
        *   **If the time range is longer than 1 hour but shorter than or equal to three days**, data is queried every five minutes.
        *   **If the time range is longer than three days but shorter than or equal to seven days**, data is queried every hour.
        
        @param request: DescribeDcdnDomainIspDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIspDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIspData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_isp_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   If **StartTime** is set but **EndTime** is not set, the data within the hour that starts from **StartTime** is queried.
        *   If **EndTime** is set but **StartTime** is not set, the data within the last hour that precedes **EndTime** is queried.
        *   You can query data of a domain name or all domain names that belong to your account.
        *   You can view data that is collected over the last seven days. The interval at which data is queried is based on the time range specified by **StartTime** and **EndTime**.
        *   **If the time range is shorter than or equal to one hour**, data is queried every minute.
        *   **If the time range is longer than 1 hour but shorter than or equal to three days**, data is queried every five minutes.
        *   **If the time range is longer than three days but shorter than or equal to seven days**, data is queried every hour.
        
        @param request: DescribeDcdnDomainIspDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainIspDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIspData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_isp_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   If **StartTime** is set but **EndTime** is not set, the data within the hour that starts from **StartTime** is queried.
        *   If **EndTime** is set but **StartTime** is not set, the data within the last hour that precedes **EndTime** is queried.
        *   You can query data of a domain name or all domain names that belong to your account.
        *   You can view data that is collected over the last seven days. The interval at which data is queried is based on the time range specified by **StartTime** and **EndTime**.
        *   **If the time range is shorter than or equal to one hour**, data is queried every minute.
        *   **If the time range is longer than 1 hour but shorter than or equal to three days**, data is queried every five minutes.
        *   **If the time range is longer than three days but shorter than or equal to seven days**, data is queried every hour.
        
        @param request: DescribeDcdnDomainIspDataRequest
        @return: DescribeDcdnDomainIspDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    async def describe_dcdn_domain_isp_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   If **StartTime** is set but **EndTime** is not set, the data within the hour that starts from **StartTime** is queried.
        *   If **EndTime** is set but **StartTime** is not set, the data within the last hour that precedes **EndTime** is queried.
        *   You can query data of a domain name or all domain names that belong to your account.
        *   You can view data that is collected over the last seven days. The interval at which data is queried is based on the time range specified by **StartTime** and **EndTime**.
        *   **If the time range is shorter than or equal to one hour**, data is queried every minute.
        *   **If the time range is longer than 1 hour but shorter than or equal to three days**, data is queried every five minutes.
        *   **If the time range is longer than three days but shorter than or equal to seven days**, data is queried every hour.
        
        @param request: DescribeDcdnDomainIspDataRequest
        @return: DescribeDcdnDomainIspDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_isp_data_with_options_async(request, runtime)

    def describe_dcdn_domain_log_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        """
        >
        *   If you specify neither the **StartTime** parameter nor the **EndTime** parameter, the data in the last 24 hours is returned. If you specify the **StartTime** and **EndTime** parameters, the data within the specified time range is returned.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDcdnDomainLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_log_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        """
        >
        *   If you specify neither the **StartTime** parameter nor the **EndTime** parameter, the data in the last 24 hours is returned. If you specify the **StartTime** and **EndTime** parameters, the data within the specified time range is returned.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDcdnDomainLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_log(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        """
        >
        *   If you specify neither the **StartTime** parameter nor the **EndTime** parameter, the data in the last 24 hours is returned. If you specify the **StartTime** and **EndTime** parameters, the data within the specified time range is returned.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainLogRequest
        @return: DescribeDcdnDomainLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    async def describe_dcdn_domain_log_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        """
        >
        *   If you specify neither the **StartTime** parameter nor the **EndTime** parameter, the data in the last 24 hours is returned. If you specify the **StartTime** and **EndTime** parameters, the data within the specified time range is returned.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainLogRequest
        @return: DescribeDcdnDomainLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_log_with_options_async(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        """
        When you call this operation, take note of the following rules:
        *   If you do not set the StartTime or EndTime parameter, data within the last 10 minutes is queried. You can set both the StartTime and EndTime parameters to specify a time range.
        *   You can specify one or more accelerated domain names. Separate domain names with commas (,).
        *   You can query data within the last 90 days.
        *   The time range cannot exceed 1 hour.
        
        @param request: DescribeDcdnDomainMultiUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainMultiUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainMultiUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_multi_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        """
        When you call this operation, take note of the following rules:
        *   If you do not set the StartTime or EndTime parameter, data within the last 10 minutes is queried. You can set both the StartTime and EndTime parameters to specify a time range.
        *   You can specify one or more accelerated domain names. Separate domain names with commas (,).
        *   You can query data within the last 90 days.
        *   The time range cannot exceed 1 hour.
        
        @param request: DescribeDcdnDomainMultiUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainMultiUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainMultiUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_multi_usage_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        """
        When you call this operation, take note of the following rules:
        *   If you do not set the StartTime or EndTime parameter, data within the last 10 minutes is queried. You can set both the StartTime and EndTime parameters to specify a time range.
        *   You can specify one or more accelerated domain names. Separate domain names with commas (,).
        *   You can query data within the last 90 days.
        *   The time range cannot exceed 1 hour.
        
        @param request: DescribeDcdnDomainMultiUsageDataRequest
        @return: DescribeDcdnDomainMultiUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_multi_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        """
        When you call this operation, take note of the following rules:
        *   If you do not set the StartTime or EndTime parameter, data within the last 10 minutes is queried. You can set both the StartTime and EndTime parameters to specify a time range.
        *   You can specify one or more accelerated domain names. Separate domain names with commas (,).
        *   You can query data within the last 90 days.
        *   The time range cannot exceed 1 hour.
        
        @param request: DescribeDcdnDomainMultiUsageDataRequest
        @return: DescribeDcdnDomainMultiUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainOriginBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainOriginBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainOriginBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_origin_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainOriginBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainOriginBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainOriginBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_origin_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainOriginBpsDataRequest
        @return: DescribeDcdnDomainOriginBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainOriginBpsDataRequest
        @return: DescribeDcdnDomainOriginBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        """
        - You can call this operation up to 100 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameters, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainOriginTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainOriginTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainOriginTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_origin_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        """
        - You can call this operation up to 100 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameters, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainOriginTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainOriginTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainOriginTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_origin_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        """
        - You can call this operation up to 100 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameters, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainOriginTrafficDataRequest
        @return: DescribeDcdnDomainOriginTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        """
        - You can call this operation up to 100 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameters, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainOriginTrafficDataRequest
        @return: DescribeDcdnDomainOriginTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_property_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_property_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_property(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainPropertyRequest
        @return: DescribeDcdnDomainPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    async def describe_dcdn_domain_property_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainPropertyRequest
        @return: DescribeDcdnDomainPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_property_with_options_async(request, runtime)

    def describe_dcdn_domain_pv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainPvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_pv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainPvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_pv_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_pv_data_with_options(request, runtime)

    async def describe_dcdn_domain_pv_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_pv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_qps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainQpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainQpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_qps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainQpsDataRequest
        @return: DescribeDcdnDomainQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainQpsDataRequest
        @return: DescribeDcdnDomainQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_qps_data_by_layer_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse:
        """
        - You can call this operation up to 20 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainQpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainQpsDataByLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainQpsDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_qps_data_by_layer_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse:
        """
        - You can call this operation up to 20 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainQpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainQpsDataByLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainQpsDataByLayer',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_qps_data_by_layer(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse:
        """
        - You can call this operation up to 20 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainQpsDataByLayerRequest
        @return: DescribeDcdnDomainQpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_by_layer_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_by_layer_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataByLayerResponse:
        """
        - You can call this operation up to 20 times per second per account.
        - If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        | ---------------- | ---------------------------- | ------------------------- | ---------- |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        | 1 day | 366 days | 366 days | 04:00 on the next day |
        
        @param request: DescribeDcdnDomainQpsDataByLayerRequest
        @return: DescribeDcdnDomainQpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_by_layer_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |----|------|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeByteHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeByteHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeByteHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |----|------|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeByteHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeByteHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeByteHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_byte_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |----|------|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeByteHitRateDataRequest
        @return: DescribeDcdnDomainRealTimeByteHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |----|------|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes |
        | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeByteHitRateDataRequest
        @return: DescribeDcdnDomainRealTimeByteHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainRealTimeDetailDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeDetailDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeDetailData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_detail_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainRealTimeDetailDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeDetailDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeDetailData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_detail_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainRealTimeDetailDataRequest
        @return: DescribeDcdnDomainRealTimeDetailDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_detail_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnDomainRealTimeDetailDataRequest
        @return: DescribeDcdnDomainRealTimeDetailDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeHttpCodeDataRequest
        @return: DescribeDcdnDomainRealTimeHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeHttpCodeDataRequest
        @return: DescribeDcdnDomainRealTimeHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeQpsDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeQpsDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_qps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeQpsDataRequest
        @return: DescribeDcdnDomainRealTimeQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeQpsDataRequest
        @return: DescribeDcdnDomainRealTimeQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeReqHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeReqHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeReqHitRateDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeReqHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_req_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeReqHitRateDataRequest
        @return: DescribeDcdnDomainRealTimeReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        """
        #
        *   You can call this operation up to 10 times per second per account.
        *   The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last hour. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeReqHitRateDataRequest
        @return: DescribeDcdnDomainRealTimeReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |-----|-----|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes | | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |-----|-----|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes | | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |-----|-----|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes | | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeSrcBpsDataRequest
        @return: DescribeDcdnDomainRealTimeSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        | Time granularity | Maximum time range per query | Historical data available | Data delay |
        |-----|-----|-----|--------|
        | 1 minute | 1 hour | 7 days | 5 minutes |
        | 5 minutes | 3 days | 93 days | 15 minutes | | 1 hour | 31 days | 186 days | 4 hours |
        
        @param request: DescribeDcdnDomainRealTimeSrcBpsDataRequest
        @return: DescribeDcdnDomainRealTimeSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest
        @return: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest
        @return: DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeSrcTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeSrcTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcTrafficDataRequest
        @return: DescribeDcdnDomainRealTimeSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        """
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeSrcTrafficDataRequest
        @return: DescribeDcdnDomainRealTimeSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        """
        #
        You can call this operation up to 50 times per second per user.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        """
        #
        You can call this operation up to 50 times per second per user.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRealTimeTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        """
        #
        You can call this operation up to 50 times per second per user.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeTrafficDataRequest
        @return: DescribeDcdnDomainRealTimeTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        """
        #
        You can call this operation up to 50 times per second per user.
        **Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay. |Time granularity |Maximum time range per query |Historical data available|Data delay| |---------------|--------| |1 minute|1 hour|7 days|5 minutes| |5 minutes|3 days|93 days|15 minutes| |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDcdnDomainRealTimeTrafficDataRequest
        @return: DescribeDcdnDomainRealTimeTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_region_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        """
        >
        *   If you do not specify the StartTime and EndTime parameters, the data within the last 24 hours is queried. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRegionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRegionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_region_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        """
        >
        *   If you do not specify the StartTime and EndTime parameters, the data within the last 24 hours is queried. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainRegionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRegionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_region_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        """
        >
        *   If you do not specify the StartTime and EndTime parameters, the data within the last 24 hours is queried. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainRegionDataRequest
        @return: DescribeDcdnDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    async def describe_dcdn_domain_region_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        """
        >
        *   If you do not specify the StartTime and EndTime parameters, the data within the last 24 hours is queried. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnDomainRegionDataRequest
        @return: DescribeDcdnDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_region_data_with_options_async(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        """
        The name of the accelerated domain.
        
        @param request: DescribeDcdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        """
        The name of the accelerated domain.
        
        @param request: DescribeDcdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_staging_config(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        """
        The name of the accelerated domain.
        
        @param request: DescribeDcdnDomainStagingConfigRequest
        @return: DescribeDcdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    async def describe_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        """
        The name of the accelerated domain.
        
        @param request: DescribeDcdnDomainStagingConfigRequest
        @return: DescribeDcdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_staging_config_with_options_async(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        """
        *Before you call this operation, take note of the following rules:**\
        *   If you do not set the StartTime parameter, the data on the previous day is queried.
        *   You can specify only one domain name.
        
        @param request: DescribeDcdnDomainTopReferVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTopReferVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTopReferVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_top_refer_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        """
        *Before you call this operation, take note of the following rules:**\
        *   If you do not set the StartTime parameter, the data on the previous day is queried.
        *   You can specify only one domain name.
        
        @param request: DescribeDcdnDomainTopReferVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTopReferVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTopReferVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_top_refer_visit(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        """
        *Before you call this operation, take note of the following rules:**\
        *   If you do not set the StartTime parameter, the data on the previous day is queried.
        *   You can specify only one domain name.
        
        @param request: DescribeDcdnDomainTopReferVisitRequest
        @return: DescribeDcdnDomainTopReferVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_refer_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        """
        *Before you call this operation, take note of the following rules:**\
        *   If you do not set the StartTime parameter, the data on the previous day is queried.
        *   You can specify only one domain name.
        
        @param request: DescribeDcdnDomainTopReferVisitRequest
        @return: DescribeDcdnDomainTopReferVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        """
        > You can query data in the last seven days.
        
        @param request: DescribeDcdnDomainTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTopUrlVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_top_url_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        """
        > You can query data in the last seven days.
        
        @param request: DescribeDcdnDomainTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTopUrlVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_top_url_visit(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        """
        > You can query data in the last seven days.
        
        @param request: DescribeDcdnDomainTopUrlVisitRequest
        @return: DescribeDcdnDomainTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_url_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        """
        > You can query data in the last seven days.
        
        @param request: DescribeDcdnDomainTopUrlVisitRequest
        @return: DescribeDcdnDomainTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainTrafficDataRequest
        @return: DescribeDcdnDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        """
        If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        * You can call this operation up to 100 times per second per account.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainTrafficDataRequest
        @return: DescribeDcdnDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * Usage data includes traffic (measured in bytes), bandwidth values (measured in bit/s), and the number of requests.
        **Time granularity**:
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.data_protocol):
            query['DataProtocol'] = request.data_protocol
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * Usage data includes traffic (measured in bytes), bandwidth values (measured in bit/s), and the number of requests.
        **Time granularity**:
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.data_protocol):
            query['DataProtocol'] = request.data_protocol
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_usage_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * Usage data includes traffic (measured in bytes), bandwidth values (measured in bit/s), and the number of requests.
        **Time granularity**:
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainUsageDataRequest
        @return: DescribeDcdnDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
        """
        You can call this operation up to 10 times per second per account.
        * Usage data includes traffic (measured in bytes), bandwidth values (measured in bit/s), and the number of requests.
        **Time granularity**:
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainUsageDataRequest
        @return: DescribeDcdnDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        """
        ***\
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   You can specify only one accelerated domain name or all the accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDcdnDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainUvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_uv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        """
        ***\
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   You can specify only one accelerated domain name or all the accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDcdnDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainUvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_uv_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        """
        ***\
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   You can specify only one accelerated domain name or all the accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDcdnDomainUvDataRequest
        @return: DescribeDcdnDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    async def describe_dcdn_domain_uv_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        """
        ***\
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   You can specify only one accelerated domain name or all the accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDcdnDomainUvDataRequest
        @return: DescribeDcdnDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_uv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketBpsDataRequest
        @return: DescribeDcdnDomainWebsocketBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        """
        #
        *   You can call this operation up to 100 times per second per account.
        *   If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketBpsDataRequest
        @return: DescribeDcdnDomainWebsocketBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        """
        #
        You can call this operation up to 100 times per second per account.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        """
        #
        You can call this operation up to 100 times per second per account.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketHttpCodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        """
        #
        You can call this operation up to 100 times per second per account.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketHttpCodeDataRequest
        @return: DescribeDcdnDomainWebsocketHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        """
        #
        You can call this operation up to 100 times per second per account.
        **Time granularity** The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table. |Time granularity |Maximum time range per query |Historical data available |Data delay | -------------- | -------------- | ------ |5 minutes |3 days |93 days |15 minutes |1 hour |31 days |186 days |4 hours |1 day |366 days |366 days |04:00 on the next day
        
        @param request: DescribeDcdnDomainWebsocketHttpCodeDataRequest
        @return: DescribeDcdnDomainWebsocketHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainWebsocketTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_domain_websocket_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainWebsocketTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnDomainWebsocketTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainWebsocketTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainWebsocketTrafficDataRequest
        @return: DescribeDcdnDomainWebsocketTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        """
        You can call this operation up to 100 times per second per account.
        * If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the last 24 hours. If you set both the **StartTime** and **EndTime** parameters, the request returns the data collected within the specified time range.
        **Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDcdnDomainWebsocketTrafficDataRequest
        @return: DescribeDcdnDomainWebsocketTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_er_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnErUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnErUsageDataResponse:
        """
        # Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 1 hour. The maximum time span for a query is 24 hours. The time period within which historical data is available for a query is 366 days.
        
        @param request: DescribeDcdnErUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnErUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.routine_id):
            query['RoutineID'] = request.routine_id
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnErUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnErUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_er_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnErUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnErUsageDataResponse:
        """
        # Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 1 hour. The maximum time span for a query is 24 hours. The time period within which historical data is available for a query is 366 days.
        
        @param request: DescribeDcdnErUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnErUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.routine_id):
            query['RoutineID'] = request.routine_id
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnErUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnErUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_er_usage_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnErUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnErUsageDataResponse:
        """
        # Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 1 hour. The maximum time span for a query is 24 hours. The time period within which historical data is available for a query is 366 days.
        
        @param request: DescribeDcdnErUsageDataRequest
        @return: DescribeDcdnErUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_er_usage_data_with_options(request, runtime)

    async def describe_dcdn_er_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnErUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnErUsageDataResponse:
        """
        # Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 1 hour. The maximum time span for a query is 24 hours. The time period within which historical data is available for a query is 366 days.
        
        @param request: DescribeDcdnErUsageDataRequest
        @return: DescribeDcdnErUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_er_usage_data_with_options_async(request, runtime)

    def describe_dcdn_full_domains_block_ipconfig_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        """
        If you specify IP addresses or CIDR blocks, IP addresses that are effective and corresponding expiration time are returned. If you do not specify IP addresses or CIDR blocks, all effective IP addresses and the corresponding expiration time are returned.
        *   The results are written to OSS and returned as OSS URLs. The OSS objects are in the format of `IP address-Corresponding expiration time`. The expiration time is in the yyyy-MM-dd HH:mm:ss format.
        *   You can share URLs of OSS objects with others. The shared URLs are valid for three days.
        
        @param request: DescribeDcdnFullDomainsBlockIPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnFullDomainsBlockIPConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnFullDomainsBlockIPConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_full_domains_block_ipconfig_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        """
        If you specify IP addresses or CIDR blocks, IP addresses that are effective and corresponding expiration time are returned. If you do not specify IP addresses or CIDR blocks, all effective IP addresses and the corresponding expiration time are returned.
        *   The results are written to OSS and returned as OSS URLs. The OSS objects are in the format of `IP address-Corresponding expiration time`. The expiration time is in the yyyy-MM-dd HH:mm:ss format.
        *   You can share URLs of OSS objects with others. The shared URLs are valid for three days.
        
        @param request: DescribeDcdnFullDomainsBlockIPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnFullDomainsBlockIPConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnFullDomainsBlockIPConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_full_domains_block_ipconfig(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        """
        If you specify IP addresses or CIDR blocks, IP addresses that are effective and corresponding expiration time are returned. If you do not specify IP addresses or CIDR blocks, all effective IP addresses and the corresponding expiration time are returned.
        *   The results are written to OSS and returned as OSS URLs. The OSS objects are in the format of `IP address-Corresponding expiration time`. The expiration time is in the yyyy-MM-dd HH:mm:ss format.
        *   You can share URLs of OSS objects with others. The shared URLs are valid for three days.
        
        @param request: DescribeDcdnFullDomainsBlockIPConfigRequest
        @return: DescribeDcdnFullDomainsBlockIPConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_full_domains_block_ipconfig_with_options(request, runtime)

    async def describe_dcdn_full_domains_block_ipconfig_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPConfigResponse:
        """
        If you specify IP addresses or CIDR blocks, IP addresses that are effective and corresponding expiration time are returned. If you do not specify IP addresses or CIDR blocks, all effective IP addresses and the corresponding expiration time are returned.
        *   The results are written to OSS and returned as OSS URLs. The OSS objects are in the format of `IP address-Corresponding expiration time`. The expiration time is in the yyyy-MM-dd HH:mm:ss format.
        *   You can share URLs of OSS objects with others. The shared URLs are valid for three days.
        
        @param request: DescribeDcdnFullDomainsBlockIPConfigRequest
        @return: DescribeDcdnFullDomainsBlockIPConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_full_domains_block_ipconfig_with_options_async(request, runtime)

    def describe_dcdn_full_domains_block_iphistory_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        """
        For a specified IP addresses and time range, the time when the IP address was delivered to the edge and the corresponding result are returned.
        *   If a specified IP address or CIDR block has multiple blocking records in a specified time range, the records are sorted by delivery time in descending order.
        *   The maximum time range to query is 90 days.
        *   If no blocking record exists or delivery fails for the given IP address and time range, the delivery time is empty.
        
        @param request: DescribeDcdnFullDomainsBlockIPHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnFullDomainsBlockIPHistoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDcdnFullDomainsBlockIPHistory',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_full_domains_block_iphistory_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        """
        For a specified IP addresses and time range, the time when the IP address was delivered to the edge and the corresponding result are returned.
        *   If a specified IP address or CIDR block has multiple blocking records in a specified time range, the records are sorted by delivery time in descending order.
        *   The maximum time range to query is 90 days.
        *   If no blocking record exists or delivery fails for the given IP address and time range, the delivery time is empty.
        
        @param request: DescribeDcdnFullDomainsBlockIPHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnFullDomainsBlockIPHistoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDcdnFullDomainsBlockIPHistory',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_full_domains_block_iphistory(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        """
        For a specified IP addresses and time range, the time when the IP address was delivered to the edge and the corresponding result are returned.
        *   If a specified IP address or CIDR block has multiple blocking records in a specified time range, the records are sorted by delivery time in descending order.
        *   The maximum time range to query is 90 days.
        *   If no blocking record exists or delivery fails for the given IP address and time range, the delivery time is empty.
        
        @param request: DescribeDcdnFullDomainsBlockIPHistoryRequest
        @return: DescribeDcdnFullDomainsBlockIPHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_full_domains_block_iphistory_with_options(request, runtime)

    async def describe_dcdn_full_domains_block_iphistory_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnFullDomainsBlockIPHistoryResponse:
        """
        For a specified IP addresses and time range, the time when the IP address was delivered to the edge and the corresponding result are returned.
        *   If a specified IP address or CIDR block has multiple blocking records in a specified time range, the records are sorted by delivery time in descending order.
        *   The maximum time range to query is 90 days.
        *   If no blocking record exists or delivery fails for the given IP address and time range, the delivery time is empty.
        
        @param request: DescribeDcdnFullDomainsBlockIPHistoryRequest
        @return: DescribeDcdnFullDomainsBlockIPHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_full_domains_block_iphistory_with_options_async(request, runtime)

    def describe_dcdn_https_domain_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeDcdnHttpsDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnHttpsDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnHttpsDomainList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_https_domain_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeDcdnHttpsDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnHttpsDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnHttpsDomainList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_https_domain_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeDcdnHttpsDomainListRequest
        @return: DescribeDcdnHttpsDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    async def describe_dcdn_https_domain_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeDcdnHttpsDomainListRequest
        @return: DescribeDcdnHttpsDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_https_domain_list_with_options_async(request, runtime)

    def describe_dcdn_ip_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ip_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ip_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnIpInfoRequest
        @return: DescribeDcdnIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    async def describe_dcdn_ip_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnIpInfoRequest
        @return: DescribeDcdnIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ip_info_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnIpaDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnIpaDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_configs(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnIpaDomainConfigsRequest
        @return: DescribeDcdnIpaDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnIpaDomainConfigsRequest
        @return: DescribeDcdnIpaDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaDomainDetailRequest
        @return: DescribeDcdnIpaDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaDomainDetailRequest
        @return: DescribeDcdnIpaDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_ipa_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeDcdnIpaServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeDcdnIpaServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeDcdnIpaServiceRequest
        @return: DescribeDcdnIpaServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    async def describe_dcdn_ipa_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeDcdnIpaServiceRequest
        @return: DescribeDcdnIpaServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_service_with_options_async(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaUserDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_ipa_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnIpaUserDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_ipa_user_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaUserDomainsRequest
        @return: DescribeDcdnIpaUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    async def describe_dcdn_ipa_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnIpaUserDomainsRequest
        @return: DescribeDcdnIpaUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_user_domains_with_options_async(request, runtime)

    def describe_dcdn_kv_account_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvAccountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnKvAccount',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_account_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvAccountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnKvAccount',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_account(self) -> dcdn_20180115_models.DescribeDcdnKvAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_kv_account_with_options(runtime)

    async def describe_dcdn_kv_account_async(self) -> dcdn_20180115_models.DescribeDcdnKvAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_kv_account_with_options_async(runtime)

    def describe_dcdn_kv_account_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnKvAccountStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_account_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnKvAccountStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_account_status(self) -> dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_kv_account_status_with_options(runtime)

    async def describe_dcdn_kv_account_status_async(self) -> dcdn_20180115_models.DescribeDcdnKvAccountStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_kv_account_status_with_options_async(runtime)

    def describe_dcdn_kv_namespace_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_kv_namespace_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_kv_namespace(
        self,
        request: dcdn_20180115_models.DescribeDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_kv_namespace_with_options(request, runtime)

    async def describe_dcdn_kv_namespace_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_kv_namespace_with_options_async(request, runtime)

    def describe_dcdn_l2ips_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnL2IpsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnL2Ips',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnL2IpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_l2ips_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnL2IpsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnL2Ips',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnL2IpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_l2ips(self) -> dcdn_20180115_models.DescribeDcdnL2IpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_l2ips_with_options(runtime)

    async def describe_dcdn_l2ips_async(self) -> dcdn_20180115_models.DescribeDcdnL2IpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_l2ips_with_options_async(runtime)

    def describe_dcdn_l2vips_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnL2VipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnL2VipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnL2Vips',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnL2VipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_l2vips_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnL2VipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnL2VipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnL2Vips',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnL2VipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_l2vips(
        self,
        request: dcdn_20180115_models.DescribeDcdnL2VipsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnL2VipsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_l2vips_with_options(request, runtime)

    async def describe_dcdn_l2vips_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnL2VipsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnL2VipsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_l2vips_with_options_async(request, runtime)

    def describe_dcdn_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        """
        >  You can call this API operation up to 100 times per second per account.
        
        @param request: DescribeDcdnRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_real_time_delivery_field_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        """
        >  You can call this API operation up to 100 times per second per account.
        
        @param request: DescribeDcdnRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_real_time_delivery_field(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        """
        >  You can call this API operation up to 100 times per second per account.
        
        @param request: DescribeDcdnRealTimeDeliveryFieldRequest
        @return: DescribeDcdnRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        """
        >  You can call this API operation up to 100 times per second per account.
        
        @param request: DescribeDcdnRealTimeDeliveryFieldRequest
        @return: DescribeDcdnRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_refresh_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        """
        >  You can call the **RefreshDcdnObjectCaches** operation to refresh content and call the **PreloadDcdnObjectCaches** operation to prefetch content.
        > *   You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnRefreshQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        """
        >  You can call the **RefreshDcdnObjectCaches** operation to refresh content and call the **PreloadDcdnObjectCaches** operation to prefetch content.
        > *   You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnRefreshQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_quota(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        """
        >  You can call the **RefreshDcdnObjectCaches** operation to refresh content and call the **PreloadDcdnObjectCaches** operation to prefetch content.
        > *   You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnRefreshQuotaRequest
        @return: DescribeDcdnRefreshQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    async def describe_dcdn_refresh_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        """
        >  You can call the **RefreshDcdnObjectCaches** operation to refresh content and call the **PreloadDcdnObjectCaches** operation to prefetch content.
        > *   You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnRefreshQuotaRequest
        @return: DescribeDcdnRefreshQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_quota_with_options_async(request, runtime)

    def describe_dcdn_refresh_task_by_id_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        """
        >
        *   You can query data within the last three days.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRefreshTaskByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshTaskByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshTaskById',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_task_by_id_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        """
        >
        *   You can query data within the last three days.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRefreshTaskByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshTaskByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshTaskById',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_task_by_id(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        """
        >
        *   You can query data within the last three days.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRefreshTaskByIdRequest
        @return: DescribeDcdnRefreshTaskByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_task_by_id_with_options(request, runtime)

    async def describe_dcdn_refresh_task_by_id_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        """
        >
        *   You can query data within the last three days.
        *   You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRefreshTaskByIdRequest
        @return: DescribeDcdnRefreshTaskByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_task_by_id_with_options_async(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        """
        >
        *   You can query the refresh or prefetch tasks by ID or URL.
        *   You can set both **TaskId** and **ObjectPath** in a request. If you do not set **TaskId** or **ObjectPath**, the data in the last 3 days on the first page is returned. By default, a maximum of 20 entries can be displayed on each page.
        *   If you specify **DomainName** or **Status**, you must also specify **ObjectType**.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnRefreshTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshTasks',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_refresh_tasks_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        """
        >
        *   You can query the refresh or prefetch tasks by ID or URL.
        *   You can set both **TaskId** and **ObjectPath** in a request. If you do not set **TaskId** or **ObjectPath**, the data in the last 3 days on the first page is returned. By default, a maximum of 20 entries can be displayed on each page.
        *   If you specify **DomainName** or **Status**, you must also specify **ObjectType**.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnRefreshTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRefreshTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshTasks',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_refresh_tasks(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        """
        >
        *   You can query the refresh or prefetch tasks by ID or URL.
        *   You can set both **TaskId** and **ObjectPath** in a request. If you do not set **TaskId** or **ObjectPath**, the data in the last 3 days on the first page is returned. By default, a maximum of 20 entries can be displayed on each page.
        *   If you specify **DomainName** or **Status**, you must also specify **ObjectType**.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnRefreshTasksRequest
        @return: DescribeDcdnRefreshTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    async def describe_dcdn_refresh_tasks_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        """
        >
        *   You can query the refresh or prefetch tasks by ID or URL.
        *   You can set both **TaskId** and **ObjectPath** in a request. If you do not set **TaskId** or **ObjectPath**, the data in the last 3 days on the first page is returned. By default, a maximum of 20 entries can be displayed on each page.
        *   If you specify **DomainName** or **Status**, you must also specify **ObjectType**.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnRefreshTasksRequest
        @return: DescribeDcdnRefreshTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_tasks_with_options_async(request, runtime)

    def describe_dcdn_region_and_isp_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRegionAndIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRegionAndIspResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRegionAndIsp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_region_and_isp_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRegionAndIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnRegionAndIspResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRegionAndIsp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_region_and_isp(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRegionAndIspRequest
        @return: DescribeDcdnRegionAndIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    async def describe_dcdn_region_and_isp_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnRegionAndIspRequest
        @return: DescribeDcdnRegionAndIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_region_and_isp_with_options_async(request, runtime)

    def describe_dcdn_report_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.http_code):
            query['HttpCode'] = request.http_code
        if not UtilClient.is_unset(request.is_overseas):
            query['IsOverseas'] = request.is_overseas
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReport',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_report_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.http_code):
            query['HttpCode'] = request.http_code
        if not UtilClient.is_unset(request.is_overseas):
            query['IsOverseas'] = request.is_overseas
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReport',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_report(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportRequest
        @return: DescribeDcdnReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_with_options(request, runtime)

    async def describe_dcdn_report_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportRequest
        @return: DescribeDcdnReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_report_with_options_async(request, runtime)

    def describe_dcdn_report_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        """
        >  This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        > * You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReportList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_report_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        """
        >  This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        > * You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReportList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_report_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        """
        >  This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        > * You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportListRequest
        @return: DescribeDcdnReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_list_with_options(request, runtime)

    async def describe_dcdn_report_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        """
        >  This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        > * You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnReportListRequest
        @return: DescribeDcdnReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_report_list_with_options_async(request, runtime)

    def describe_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnSLSRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSLSRealtimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_slsrealtime_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnSLSRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSLSRealtimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_slsrealtime_log_delivery(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnSLSRealtimeLogDeliveryRequest
        @return: DescribeDcdnSLSRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def describe_dcdn_slsrealtime_log_delivery_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnSLSRealtimeLogDeliveryRequest
        @return: DescribeDcdnSLSRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSMCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSMCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_smcertificate_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSMCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSMCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_smcertificate_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateDetailRequest
        @return: DescribeDcdnSMCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_detail_with_options(request, runtime)

    async def describe_dcdn_smcertificate_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateDetailRequest
        @return: DescribeDcdnSMCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSMCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSMCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_smcertificate_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSMCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSMCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_smcertificate_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateListRequest
        @return: DescribeDcdnSMCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_list_with_options(request, runtime)

    async def describe_dcdn_smcertificate_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnSMCertificateListRequest
        @return: DescribeDcdnSMCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_smcertificate_list_with_options_async(request, runtime)

    def describe_dcdn_sec_func_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecFuncInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSecFuncInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.sec_func_type):
            query['SecFuncType'] = request.sec_func_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSecFuncInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sec_func_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecFuncInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSecFuncInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.sec_func_type):
            query['SecFuncType'] = request.sec_func_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSecFuncInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sec_func_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecFuncInfoRequest
        @return: DescribeDcdnSecFuncInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_func_info_with_options(request, runtime)

    async def describe_dcdn_sec_func_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecFuncInfoRequest
        @return: DescribeDcdnSecFuncInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sec_func_info_with_options_async(request, runtime)

    def describe_dcdn_sec_spec_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSecSpecInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnSecSpecInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sec_spec_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnSecSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSecSpecInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnSecSpecInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sec_spec_info(self) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @return: DescribeDcdnSecSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_spec_info_with_options(runtime)

    async def describe_dcdn_sec_spec_info_async(self) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @return: DescribeDcdnSecSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sec_spec_info_with_options_async(runtime)

    def describe_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnServiceRequest
        @return: DescribeDcdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    async def describe_dcdn_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnServiceRequest
        @return: DescribeDcdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_service_with_options_async(request, runtime)

    def describe_dcdn_staging_ip_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnStagingIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnStagingIpResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnStagingIp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_staging_ip_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnStagingIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnStagingIpResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnStagingIp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_staging_ip(self) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @return: DescribeDcdnStagingIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(runtime)

    async def describe_dcdn_staging_ip_async(self) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @return: DescribeDcdnStagingIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_staging_ip_with_options_async(runtime)

    def describe_dcdn_sub_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        """
        >
        *   By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        *   You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnSubListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSubListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnSubList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_sub_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        """
        >
        *   By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        *   You can call this operation up to three times per second per account.
        
        @param request: DescribeDcdnSubListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnSubListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnSubList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_sub_list(self) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        """
        >
        *   By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        *   You can call this operation up to three times per second per account.
        
        @return: DescribeDcdnSubListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sub_list_with_options(runtime)

    async def describe_dcdn_sub_list_async(self) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        """
        >
        *   By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        *   You can call this operation up to three times per second per account.
        
        @return: DescribeDcdnSubListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sub_list_with_options_async(runtime)

    def describe_dcdn_tag_resources_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnTagResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_tag_resources_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnTagResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_tag_resources(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnTagResourcesRequest
        @return: DescribeDcdnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    async def describe_dcdn_tag_resources_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDcdnTagResourcesRequest
        @return: DescribeDcdnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_tag_resources_with_options_async(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        """
        \\\\*Before you call this operation, pay attention to the following considerations:\\*\\* If you do not specify the StartTime and EndTime parameters, the data within the current month is queried by default. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        
        @param request: DescribeDcdnTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnTopDomainsByFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnTopDomainsByFlow',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_top_domains_by_flow_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        """
        \\\\*Before you call this operation, pay attention to the following considerations:\\*\\* If you do not specify the StartTime and EndTime parameters, the data within the current month is queried by default. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        
        @param request: DescribeDcdnTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnTopDomainsByFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnTopDomainsByFlow',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_top_domains_by_flow(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        """
        \\\\*Before you call this operation, pay attention to the following considerations:\\*\\* If you do not specify the StartTime and EndTime parameters, the data within the current month is queried by default. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        
        @param request: DescribeDcdnTopDomainsByFlowRequest
        @return: DescribeDcdnTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_dcdn_top_domains_by_flow_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        """
        \\\\*Before you call this operation, pay attention to the following considerations:\\*\\* If you do not specify the StartTime and EndTime parameters, the data within the current month is queried by default. If you specify the StartTime and EndTime parameters, the data within the specified time range is queried.
        
        @param request: DescribeDcdnTopDomainsByFlowRequest
        @return: DescribeDcdnTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_dcdn_user_bill_history_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserBillHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserBillHistoryResponse
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
            action='DescribeDcdnUserBillHistory',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_bill_history_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserBillHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserBillHistoryResponse
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
            action='DescribeDcdnUserBillHistory',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_bill_history(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserBillHistoryRequest
        @return: DescribeDcdnUserBillHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    async def describe_dcdn_user_bill_history_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserBillHistoryRequest
        @return: DescribeDcdnUserBillHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_bill_history_with_options_async(request, runtime)

    def describe_dcdn_user_bill_type_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
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
            action='DescribeDcdnUserBillType',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_bill_type_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
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
            action='DescribeDcdnUserBillType',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_bill_type(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_type_with_options(request, runtime)

    async def describe_dcdn_user_bill_type_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_bill_type_with_options_async(request, runtime)

    def describe_dcdn_user_certificate_expire_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse:
        """
        # Usage notes
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserCertificateExpireCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserCertificateExpireCountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnUserCertificateExpireCount',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_certificate_expire_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse:
        """
        # Usage notes
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserCertificateExpireCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserCertificateExpireCountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnUserCertificateExpireCount',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_certificate_expire_count(self) -> dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse:
        """
        # Usage notes
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeDcdnUserCertificateExpireCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_certificate_expire_count_with_options(runtime)

    async def describe_dcdn_user_certificate_expire_count_async(self) -> dcdn_20180115_models.DescribeDcdnUserCertificateExpireCountResponse:
        """
        # Usage notes
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeDcdnUserCertificateExpireCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_certificate_expire_count_with_options_async(runtime)

    def describe_dcdn_user_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserConfigsResponse:
        """
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserConfigsResponse:
        """
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_configs(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserConfigsResponse:
        """
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnUserConfigsRequest
        @return: DescribeDcdnUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_configs_with_options(request, runtime)

    async def describe_dcdn_user_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserConfigsResponse:
        """
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDcdnUserConfigsRequest
        @return: DescribeDcdnUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_configs_with_options_async(request, runtime)

    def describe_dcdn_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnUserDomainsRequest
        @return: DescribeDcdnUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    async def describe_dcdn_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        """
        > You can call this operation up to 80 times per second per account.
        
        @param request: DescribeDcdnUserDomainsRequest
        @return: DescribeDcdnUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_with_options_async(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserDomainsByFuncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserDomainsByFuncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
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
            action='DescribeDcdnUserDomainsByFunc',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_domains_by_func_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserDomainsByFuncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserDomainsByFuncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
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
            action='DescribeDcdnUserDomainsByFunc',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_domains_by_func(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserDomainsByFuncRequest
        @return: DescribeDcdnUserDomainsByFuncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    async def describe_dcdn_user_domains_by_func_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserDomainsByFuncRequest
        @return: DescribeDcdnUserDomainsByFuncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_dcdn_user_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_quota(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserQuotaRequest
        @return: DescribeDcdnUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    async def describe_dcdn_user_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        """
        >  The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserQuotaRequest
        @return: DescribeDcdnUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_quota_with_options_async(request, runtime)

    def describe_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_real_time_delivery_field_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_real_time_delivery_field(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserRealTimeDeliveryFieldRequest
        @return: DescribeDcdnUserRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_user_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserRealTimeDeliveryFieldRequest
        @return: DescribeDcdnUserRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_user_resource_package_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserResourcePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserResourcePackage',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_resource_package_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserResourcePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserResourcePackage',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_resource_package(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserResourcePackageRequest
        @return: DescribeDcdnUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    async def describe_dcdn_user_resource_package_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeDcdnUserResourcePackageRequest
        @return: DescribeDcdnUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_resource_package_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserSecDropResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDrop',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_sec_drop_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserSecDropResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDrop',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropRequest
        @return: DescribeDcdnUserSecDropResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropRequest
        @return: DescribeDcdnUserSecDropResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_by_minute_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropByMinuteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserSecDropByMinuteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDropByMinute',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_sec_drop_by_minute_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropByMinuteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserSecDropByMinuteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDropByMinute',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop_by_minute(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropByMinuteRequest
        @return: DescribeDcdnUserSecDropByMinuteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_by_minute_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_by_minute_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnUserSecDropByMinuteRequest
        @return: DescribeDcdnUserSecDropByMinuteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_by_minute_with_options_async(request, runtime)

    def describe_dcdn_user_tags_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserTagsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnUserTags',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_user_tags_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnUserTagsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnUserTags',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_user_tags(self) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeDcdnUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(runtime)

    async def describe_dcdn_user_tags_async(self) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeDcdnUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_tags_with_options_async(runtime)

    def describe_dcdn_verify_content_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnVerifyContent',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_verify_content_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnVerifyContent',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_verify_content(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnVerifyContentRequest
        @return: DescribeDcdnVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    async def describe_dcdn_verify_content_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnVerifyContentRequest
        @return: DescribeDcdnVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_verify_content_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnWafDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnWafDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domain(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnWafDomainRequest
        @return: DescribeDcdnWafDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    async def describe_dcdn_waf_domain_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        """
        > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDcdnWafDomainRequest
        @return: DescribeDcdnWafDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_domain_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domain_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainDetailRequest
        @return: DescribeDcdnWafDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_detail_with_options(request, runtime)

    async def describe_dcdn_waf_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainDetailResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainDetailRequest
        @return: DescribeDcdnWafDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_waf_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainsRequest
        @return: DescribeDcdnWafDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domains_with_options(request, runtime)

    async def describe_dcdn_waf_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafDomainsRequest
        @return: DescribeDcdnWafDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_filter_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafFilterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafFilterInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafFilterInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafFilterInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_filter_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafFilterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafFilterInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafFilterInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafFilterInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_filter_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafFilterInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafFilterInfoRequest
        @return: DescribeDcdnWafFilterInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_filter_info_with_options(request, runtime)

    async def describe_dcdn_waf_filter_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafFilterInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafFilterInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafFilterInfoRequest
        @return: DescribeDcdnWafFilterInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_filter_info_with_options_async(request, runtime)

    def describe_dcdn_waf_geo_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafGeoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafGeoInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafGeoInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafGeoInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_geo_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafGeoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafGeoInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafGeoInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafGeoInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_geo_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafGeoInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafGeoInfoRequest
        @return: DescribeDcdnWafGeoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_geo_info_with_options(request, runtime)

    async def describe_dcdn_waf_geo_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafGeoInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafGeoInfoResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafGeoInfoRequest
        @return: DescribeDcdnWafGeoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_geo_info_with_options_async(request, runtime)

    def describe_dcdn_waf_logs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafLogsResponse:
        """
        >
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   The log data is collected every hour.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnWafLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDcdnWafLogs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_logs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafLogsResponse:
        """
        >
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   The log data is collected every hour.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnWafLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDcdnWafLogs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_logs(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafLogsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafLogsResponse:
        """
        >
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   The log data is collected every hour.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnWafLogsRequest
        @return: DescribeDcdnWafLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_logs_with_options(request, runtime)

    async def describe_dcdn_waf_logs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafLogsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafLogsResponse:
        """
        >
        *   If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *   The log data is collected every hour.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDcdnWafLogsRequest
        @return: DescribeDcdnWafLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_logs_with_options_async(request, runtime)

    def describe_dcdn_waf_policies_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPoliciesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicies',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policies_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPoliciesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicies',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policies(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPoliciesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPoliciesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPoliciesRequest
        @return: DescribeDcdnWafPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_policies_with_options(request, runtime)

    async def describe_dcdn_waf_policies_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPoliciesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPoliciesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPoliciesRequest
        @return: DescribeDcdnWafPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_policies_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyRequest
        @return: DescribeDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_policy_with_options(request, runtime)

    async def describe_dcdn_waf_policy_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyRequest
        @return: DescribeDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_policy_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafPolicyDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicyDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafPolicyDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicyDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafPolicyDomainsRequest
        @return: DescribeDcdnWafPolicyDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_policy_domains_with_options(request, runtime)

    async def describe_dcdn_waf_policy_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyDomainsResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafPolicyDomainsRequest
        @return: DescribeDcdnWafPolicyDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_policy_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_policy_valid_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyValidDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyValidDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.domain_name_like):
            query['DomainNameLike'] = request.domain_name_like
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicyValidDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_policy_valid_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyValidDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafPolicyValidDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.domain_name_like):
            query['DomainNameLike'] = request.domain_name_like
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafPolicyValidDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_policy_valid_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyValidDomainsRequest
        @return: DescribeDcdnWafPolicyValidDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_policy_valid_domains_with_options(request, runtime)

    async def describe_dcdn_waf_policy_valid_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafPolicyValidDomainsResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafPolicyValidDomainsRequest
        @return: DescribeDcdnWafPolicyValidDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_policy_valid_domains_with_options_async(request, runtime)

    def describe_dcdn_waf_rule_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafRuleResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafRule',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_rule_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafRuleResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafRule',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_rule(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRuleRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafRuleResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRuleRequest
        @return: DescribeDcdnWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_rule_with_options(request, runtime)

    async def describe_dcdn_waf_rule_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRuleRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafRuleResponse:
        """
        #
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRuleRequest
        @return: DescribeDcdnWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_rule_with_options_async(request, runtime)

    def describe_dcdn_waf_rules_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_rules_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args):
            query['QueryArgs'] = request.query_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafRules',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_rules(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRulesRequest
        @return: DescribeDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_rules_with_options(request, runtime)

    async def describe_dcdn_waf_rules_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafRulesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafRulesResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafRulesRequest
        @return: DescribeDcdnWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_rules_with_options_async(request, runtime)

    def describe_dcdn_waf_scenes_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafScenesResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafScenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafScenes',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_scenes_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafScenesResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafScenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scenes):
            query['DefenseScenes'] = request.defense_scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafScenes',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_scenes(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafScenesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafScenesResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafScenesRequest
        @return: DescribeDcdnWafScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_scenes_with_options(request, runtime)

    async def describe_dcdn_waf_scenes_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafScenesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafScenesResponse:
        """
        You can call this operation up to 20 times per second per user.
        
        @param request: DescribeDcdnWafScenesRequest
        @return: DescribeDcdnWafScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_scenes_with_options_async(request, runtime)

    def describe_dcdn_waf_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafServiceResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafServiceResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafServiceResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafServiceRequest
        @return: DescribeDcdnWafServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_service_with_options(request, runtime)

    async def describe_dcdn_waf_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafServiceResponse:
        """
        # Usage notes
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafServiceRequest
        @return: DescribeDcdnWafServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_service_with_options_async(request, runtime)

    def describe_dcdn_waf_spec_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafSpecInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnWafSpecInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_spec_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnWafSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafSpecInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeDcdnWafSpecInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_spec_info(self) -> dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @return: DescribeDcdnWafSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_spec_info_with_options(runtime)

    async def describe_dcdn_waf_spec_info_async(self) -> dcdn_20180115_models.DescribeDcdnWafSpecInfoResponse:
        """
        You can call this operation up to 20 times per second per account.
        
        @return: DescribeDcdnWafSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_spec_info_with_options_async(runtime)

    def describe_dcdn_waf_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafUsageDataResponse:
        """
        >   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 5 minutes. The maximum time span for a query is 31 days. The time period within which historical data is available for a query is 90 days.
        
        @param request: DescribeDcdnWafUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_waf_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafUsageDataResponse:
        """
        >   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 5 minutes. The maximum time span for a query is 31 days. The time period within which historical data is available for a query is 90 days.
        
        @param request: DescribeDcdnWafUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnWafUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_waf_usage_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafUsageDataResponse:
        """
        >   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 5 minutes. The maximum time span for a query is 31 days. The time period within which historical data is available for a query is 90 days.
        
        @param request: DescribeDcdnWafUsageDataRequest
        @return: DescribeDcdnWafUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_usage_data_with_options(request, runtime)

    async def describe_dcdn_waf_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafUsageDataResponse:
        """
        >   You can call this operation up to 10 times per second per account.
        *   The minimum time granularity for a query is 5 minutes. The maximum time span for a query is 31 days. The time period within which historical data is available for a query is 90 days.
        
        @param request: DescribeDcdnWafUsageDataRequest
        @return: DescribeDcdnWafUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_usage_data_with_options_async(request, runtime)

    def describe_dcdnsec_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnsecServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnsecServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnsecService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnsecServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdnsec_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnsecServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDcdnsecServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnsecService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnsecServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdnsec_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnsecServiceRequest
        @return: DescribeDcdnsecServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdnsec_service_with_options(request, runtime)

    async def describe_dcdnsec_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDcdnsecServiceRequest
        @return: DescribeDcdnsecServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdnsec_service_with_options_async(request, runtime)

    def describe_rddomain_config_with_options(
        self,
        request: dcdn_20180115_models.DescribeRDDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRDDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDDomainConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRDDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rddomain_config_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRDDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRDDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDDomainConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRDDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rddomain_config(
        self,
        request: dcdn_20180115_models.DescribeRDDomainConfigRequest,
    ) -> dcdn_20180115_models.DescribeRDDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rddomain_config_with_options(request, runtime)

    async def describe_rddomain_config_async(
        self,
        request: dcdn_20180115_models.DescribeRDDomainConfigRequest,
    ) -> dcdn_20180115_models.DescribeRDDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rddomain_config_with_options_async(request, runtime)

    def describe_rddomains_with_options(
        self,
        request: dcdn_20180115_models.DescribeRDDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRDDomainsResponse:
        """
        A domain name can be in one of the following states:
        *   online
        *   offline
        *   configuring
        *   configure_failed
        *   checking
        *   check_failed
        
        @param request: DescribeRDDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRDDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRDDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rddomains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRDDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRDDomainsResponse:
        """
        A domain name can be in one of the following states:
        *   online
        *   offline
        *   configuring
        *   configure_failed
        *   checking
        *   check_failed
        
        @param request: DescribeRDDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRDDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRDDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rddomains(
        self,
        request: dcdn_20180115_models.DescribeRDDomainsRequest,
    ) -> dcdn_20180115_models.DescribeRDDomainsResponse:
        """
        A domain name can be in one of the following states:
        *   online
        *   offline
        *   configuring
        *   configure_failed
        *   checking
        *   check_failed
        
        @param request: DescribeRDDomainsRequest
        @return: DescribeRDDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rddomains_with_options(request, runtime)

    async def describe_rddomains_async(
        self,
        request: dcdn_20180115_models.DescribeRDDomainsRequest,
    ) -> dcdn_20180115_models.DescribeRDDomainsResponse:
        """
        A domain name can be in one of the following states:
        *   online
        *   offline
        *   configuring
        *   configure_failed
        *   checking
        *   check_failed
        
        @param request: DescribeRDDomainsRequest
        @return: DescribeRDDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rddomains_with_options_async(request, runtime)

    def describe_routine_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineRequest
        @return: DescribeRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_with_options(request, runtime)

    async def describe_routine_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineRequest
        @return: DescribeRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_with_options_async(request, runtime)

    def describe_routine_canary_envs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCanaryEnvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineCanaryEnvsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineCanaryEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_canary_envs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCanaryEnvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineCanaryEnvsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineCanaryEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_canary_envs(self) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineCanaryEnvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_canary_envs_with_options(runtime)

    async def describe_routine_canary_envs_async(self) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineCanaryEnvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_canary_envs_with_options_async(runtime)

    def describe_routine_code_revision_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_code_revision_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_code_revision(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCodeRevisionRequest
        @return: DescribeRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_code_revision_with_options(request, runtime)

    async def describe_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineCodeRevisionRequest
        @return: DescribeRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_code_revision_with_options_async(request, runtime)

    def describe_routine_spec_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineSpecResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineSpec',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_spec_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineSpecResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineSpec',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_spec(self) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_spec_with_options(runtime)

    async def describe_routine_spec_async(self) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_spec_with_options_async(runtime)

    def describe_routine_user_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineUserInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineUserInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_routine_user_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRoutineUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoutineUserInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRoutineUserInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_routine_user_info(self) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_user_info_with_options(runtime)

    async def describe_routine_user_info_async(self) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        """
        >  You can call this operation up to 100 times per second per account.
        
        @return: DescribeRoutineUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_user_info_with_options_async(runtime)

    def describe_user_dcdn_ipa_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeUserDcdnIpaStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDcdnIpaStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDcdnIpaStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_dcdn_ipa_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeUserDcdnIpaStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDcdnIpaStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDcdnIpaStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_dcdn_ipa_status(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeUserDcdnIpaStatusRequest
        @return: DescribeUserDcdnIpaStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    async def describe_user_dcdn_ipa_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        """
        *\
        **The maximum number of times that each user can call this operation per second is 20.
        
        @param request: DescribeUserDcdnIpaStatusRequest
        @return: DescribeUserDcdnIpaStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_ipa_status_with_options_async(request, runtime)

    def describe_user_dcdn_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserDcdnStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDcdnStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDcdnStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_dcdn_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserDcdnStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDcdnStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDcdnStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_dcdn_status(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserDcdnStatusRequest
        @return: DescribeUserDcdnStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    async def describe_user_dcdn_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserDcdnStatusRequest
        @return: DescribeUserDcdnStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_status_with_options_async(request, runtime)

    def describe_user_er_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserErStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserErStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserErStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_er_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserErStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserErStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserErStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_er_status(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserErStatusRequest
        @return: DescribeUserErStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_er_status_with_options(request, runtime)

    async def describe_user_er_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserErStatusRequest
        @return: DescribeUserErStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_er_status_with_options_async(request, runtime)

    def describe_user_logservice_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeUserLogserviceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogserviceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLogserviceStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_logservice_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeUserLogserviceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogserviceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLogserviceStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_logservice_status(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeUserLogserviceStatusRequest
        @return: DescribeUserLogserviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_logservice_status_with_options(request, runtime)

    async def describe_user_logservice_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        """
        > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeUserLogserviceStatusRequest
        @return: DescribeUserLogserviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_logservice_status_with_options_async(request, runtime)

    def edit_routine_conf_with_options(
        self,
        tmp_req: dcdn_20180115_models.EditRoutineConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        """
        >
        *   This operation modifies only the specified configurations. Other configurations remain unchanged.
        *   If you want to delete a setting, delete the parameter value.
        *   This operation can add canary release environments. Make sure that the environment names comply with the naming rules. Otherwise, you will fail to add the environments.
        *   Dynamic Route for CDN (DCDN) provides 35 canary release environments. Among these environments, 34 are deployed in China and 1 is deployed outside China. The canary release environments are:
        *   Outside China: presetCanaryOverseas.
        *   In China: The 34 canary release environments are named in the format of presetCanaryXX. For example, presetCanaryBeijing represents the canary release environment in Beijing. A canary release environment is in each of the following regions: Anhui, Beijing, Chongqing, Fujian, Gansu, Guangdong, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Henan, Hong Kong, Hubei, Hunan, Jiangsu, Jiangxi, Jilin, Liaoning, Macao, Neimenggu, Ningxia, Qinghai, Shaanxi, Shandong, Shanghai, Shanxi, Sichuan, Taiwan, Tianjin, Xinjiang, Xizang, Yunan, and Zhejiang.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: EditRoutineConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditRoutineConfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditRoutineConf',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_routine_conf_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.EditRoutineConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        """
        >
        *   This operation modifies only the specified configurations. Other configurations remain unchanged.
        *   If you want to delete a setting, delete the parameter value.
        *   This operation can add canary release environments. Make sure that the environment names comply with the naming rules. Otherwise, you will fail to add the environments.
        *   Dynamic Route for CDN (DCDN) provides 35 canary release environments. Among these environments, 34 are deployed in China and 1 is deployed outside China. The canary release environments are:
        *   Outside China: presetCanaryOverseas.
        *   In China: The 34 canary release environments are named in the format of presetCanaryXX. For example, presetCanaryBeijing represents the canary release environment in Beijing. A canary release environment is in each of the following regions: Anhui, Beijing, Chongqing, Fujian, Gansu, Guangdong, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Henan, Hong Kong, Hubei, Hunan, Jiangsu, Jiangxi, Jilin, Liaoning, Macao, Neimenggu, Ningxia, Qinghai, Shaanxi, Shandong, Shanghai, Shanxi, Sichuan, Taiwan, Tianjin, Xinjiang, Xizang, Yunan, and Zhejiang.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: EditRoutineConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditRoutineConfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditRoutineConf',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_routine_conf(
        self,
        request: dcdn_20180115_models.EditRoutineConfRequest,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        """
        >
        *   This operation modifies only the specified configurations. Other configurations remain unchanged.
        *   If you want to delete a setting, delete the parameter value.
        *   This operation can add canary release environments. Make sure that the environment names comply with the naming rules. Otherwise, you will fail to add the environments.
        *   Dynamic Route for CDN (DCDN) provides 35 canary release environments. Among these environments, 34 are deployed in China and 1 is deployed outside China. The canary release environments are:
        *   Outside China: presetCanaryOverseas.
        *   In China: The 34 canary release environments are named in the format of presetCanaryXX. For example, presetCanaryBeijing represents the canary release environment in Beijing. A canary release environment is in each of the following regions: Anhui, Beijing, Chongqing, Fujian, Gansu, Guangdong, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Henan, Hong Kong, Hubei, Hunan, Jiangsu, Jiangxi, Jilin, Liaoning, Macao, Neimenggu, Ningxia, Qinghai, Shaanxi, Shandong, Shanghai, Shanxi, Sichuan, Taiwan, Tianjin, Xinjiang, Xizang, Yunan, and Zhejiang.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: EditRoutineConfRequest
        @return: EditRoutineConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_routine_conf_with_options(request, runtime)

    async def edit_routine_conf_async(
        self,
        request: dcdn_20180115_models.EditRoutineConfRequest,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        """
        >
        *   This operation modifies only the specified configurations. Other configurations remain unchanged.
        *   If you want to delete a setting, delete the parameter value.
        *   This operation can add canary release environments. Make sure that the environment names comply with the naming rules. Otherwise, you will fail to add the environments.
        *   Dynamic Route for CDN (DCDN) provides 35 canary release environments. Among these environments, 34 are deployed in China and 1 is deployed outside China. The canary release environments are:
        *   Outside China: presetCanaryOverseas.
        *   In China: The 34 canary release environments are named in the format of presetCanaryXX. For example, presetCanaryBeijing represents the canary release environment in Beijing. A canary release environment is in each of the following regions: Anhui, Beijing, Chongqing, Fujian, Gansu, Guangdong, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Henan, Hong Kong, Hubei, Hunan, Jiangsu, Jiangxi, Jilin, Liaoning, Macao, Neimenggu, Ningxia, Qinghai, Shaanxi, Shandong, Shanghai, Shanxi, Sichuan, Taiwan, Tianjin, Xinjiang, Xizang, Yunan, and Zhejiang.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: EditRoutineConfRequest
        @return: EditRoutineConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_routine_conf_with_options_async(request, runtime)

    def get_dcdn_kv_with_options(
        self,
        request: dcdn_20180115_models.GetDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.GetDcdnKvResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.GetDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dcdn_kv_with_options_async(
        self,
        request: dcdn_20180115_models.GetDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.GetDcdnKvResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.GetDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dcdn_kv(
        self,
        request: dcdn_20180115_models.GetDcdnKvRequest,
    ) -> dcdn_20180115_models.GetDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dcdn_kv_with_options(request, runtime)

    async def get_dcdn_kv_async(
        self,
        request: dcdn_20180115_models.GetDcdnKvRequest,
    ) -> dcdn_20180115_models.GetDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dcdn_kv_with_options_async(request, runtime)

    def list_dcdn_kv_with_options(
        self,
        request: dcdn_20180115_models.ListDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ListDcdnKvResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ListDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dcdn_kv_with_options_async(
        self,
        request: dcdn_20180115_models.ListDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ListDcdnKvResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ListDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dcdn_kv(
        self,
        request: dcdn_20180115_models.ListDcdnKvRequest,
    ) -> dcdn_20180115_models.ListDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dcdn_kv_with_options(request, runtime)

    async def list_dcdn_kv_async(
        self,
        request: dcdn_20180115_models.ListDcdnKvRequest,
    ) -> dcdn_20180115_models.ListDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dcdn_kv_with_options_async(request, runtime)

    def list_dcdn_real_time_delivery_project_with_options(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ListDcdnRealTimeDeliveryProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDcdnRealTimeDeliveryProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDcdnRealTimeDeliveryProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dcdn_real_time_delivery_project_with_options_async(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ListDcdnRealTimeDeliveryProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDcdnRealTimeDeliveryProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDcdnRealTimeDeliveryProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dcdn_real_time_delivery_project(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ListDcdnRealTimeDeliveryProjectRequest
        @return: ListDcdnRealTimeDeliveryProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dcdn_real_time_delivery_project_with_options(request, runtime)

    async def list_dcdn_real_time_delivery_project_async(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ListDcdnRealTimeDeliveryProjectRequest
        @return: ListDcdnRealTimeDeliveryProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dcdn_real_time_delivery_project_with_options_async(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyDCdnDomainSchdmByPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDCdnDomainSchdmByPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDCdnDomainSchdmByProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_domain_schdm_by_property_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyDCdnDomainSchdmByPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDCdnDomainSchdmByPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDCdnDomainSchdmByProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_domain_schdm_by_property(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyDCdnDomainSchdmByPropertyRequest
        @return: ModifyDCdnDomainSchdmByPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_dcdn_domain_schdm_by_property_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyDCdnDomainSchdmByPropertyRequest
        @return: ModifyDCdnDomainSchdmByPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_dcdn_waf_group_with_options(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafGroup',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_group_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafGroup',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_group(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafGroupRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_waf_group_with_options(request, runtime)

    async def modify_dcdn_waf_group_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafGroupRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_waf_group_with_options_async(request, runtime)

    def modify_dcdn_waf_policy_with_options(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_policy_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_status):
            body['PolicyStatus'] = request.policy_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafPolicy',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_policy(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyRequest
        @return: ModifyDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_waf_policy_with_options(request, runtime)

    async def modify_dcdn_waf_policy_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyResponse:
        """
        #
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Content Delivery Network (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyRequest
        @return: ModifyDcdnWafPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_waf_policy_with_options_async(request, runtime)

    def modify_dcdn_waf_policy_domains_with_options(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafPolicyDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bind_domains):
            body['BindDomains'] = request.bind_domains
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.unbind_domains):
            body['UnbindDomains'] = request.unbind_domains
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafPolicyDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_policy_domains_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafPolicyDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bind_domains):
            body['BindDomains'] = request.bind_domains
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.unbind_domains):
            body['UnbindDomains'] = request.unbind_domains
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafPolicyDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_policy_domains(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyDomainsRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyDomainsRequest
        @return: ModifyDcdnWafPolicyDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_waf_policy_domains_with_options(request, runtime)

    async def modify_dcdn_waf_policy_domains_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafPolicyDomainsRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafPolicyDomainsResponse:
        """
        # Usage notes
        *   You can call this operation up to 20 times per second per account.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        
        @param request: ModifyDcdnWafPolicyDomainsRequest
        @return: ModifyDcdnWafPolicyDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_waf_policy_domains_with_options_async(request, runtime)

    def modify_dcdn_waf_rule_with_options(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafRuleResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        *   You must configure at least one of the **RuleStatus**, **RuleName** and **RuleConfig** parameters.
        
        @param request: ModifyDcdnWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_config):
            body['RuleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            body['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafRule',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dcdn_waf_rule_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDcdnWafRuleResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        *   You must configure at least one of the **RuleStatus**, **RuleName** and **RuleConfig** parameters.
        
        @param request: ModifyDcdnWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDcdnWafRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_config):
            body['RuleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            body['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDcdnWafRule',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDcdnWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dcdn_waf_rule(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafRuleRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafRuleResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        *   You must configure at least one of the **RuleStatus**, **RuleName** and **RuleConfig** parameters.
        
        @param request: ModifyDcdnWafRuleRequest
        @return: ModifyDcdnWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_waf_rule_with_options(request, runtime)

    async def modify_dcdn_waf_rule_async(
        self,
        request: dcdn_20180115_models.ModifyDcdnWafRuleRequest,
    ) -> dcdn_20180115_models.ModifyDcdnWafRuleResponse:
        """
        #
        *   You can call this operation up to 20 times per second.
        *   Alibaba Cloud Dynamic Route for CDN (DCDN) supports POST requests.
        *   You must configure at least one of the **RuleStatus**, **RuleName** and **RuleConfig** parameters.
        
        @param request: ModifyDcdnWafRuleRequest
        @return: ModifyDcdnWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_waf_rule_with_options_async(request, runtime)

    def open_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        """
        >    DCDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must pass real-name verification.
        >*   You can call this operation up to 5 times per second per account.
        
        @param request: OpenDcdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDcdnServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.websocket_bill_type):
            query['WebsocketBillType'] = request.websocket_bill_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        """
        >    DCDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must pass real-name verification.
        >*   You can call this operation up to 5 times per second per account.
        
        @param request: OpenDcdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenDcdnServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.websocket_bill_type):
            query['WebsocketBillType'] = request.websocket_bill_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_dcdn_service(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        """
        >    DCDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must pass real-name verification.
        >*   You can call this operation up to 5 times per second per account.
        
        @param request: OpenDcdnServiceRequest
        @return: OpenDcdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    async def open_dcdn_service_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        """
        >    DCDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must pass real-name verification.
        >*   You can call this operation up to 5 times per second per account.
        
        @param request: OpenDcdnServiceRequest
        @return: OpenDcdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_dcdn_service_with_options_async(request, runtime)

    def preload_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        """
        #
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   Dynamic Content Delivery Network (DCDN) supports POST requests in which parameters are sent as a form.
        *   By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        *   You can specify at most 100 URLs in each prefetch request.
        *   The prefetch queue of each Alibaba Cloud account can contain up to 50,000 URLs. DCDN executes prefetch tasks based on the time at which you submit the URLs.
        *   You can call this operation up to 15 times per second per account.
        # Usage notes
        *   After a refresh task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        *   The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        *   To allow RAM users to perform this operation, you need to first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: PreloadDcdnObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadDcdnObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreloadDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        """
        #
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   Dynamic Content Delivery Network (DCDN) supports POST requests in which parameters are sent as a form.
        *   By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        *   You can specify at most 100 URLs in each prefetch request.
        *   The prefetch queue of each Alibaba Cloud account can contain up to 50,000 URLs. DCDN executes prefetch tasks based on the time at which you submit the URLs.
        *   You can call this operation up to 15 times per second per account.
        # Usage notes
        *   After a refresh task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        *   The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        *   To allow RAM users to perform this operation, you need to first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: PreloadDcdnObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadDcdnObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreloadDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_dcdn_object_caches(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        """
        #
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   Dynamic Content Delivery Network (DCDN) supports POST requests in which parameters are sent as a form.
        *   By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        *   You can specify at most 100 URLs in each prefetch request.
        *   The prefetch queue of each Alibaba Cloud account can contain up to 50,000 URLs. DCDN executes prefetch tasks based on the time at which you submit the URLs.
        *   You can call this operation up to 15 times per second per account.
        # Usage notes
        *   After a refresh task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        *   The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        *   To allow RAM users to perform this operation, you need to first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: PreloadDcdnObjectCachesRequest
        @return: PreloadDcdnObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    async def preload_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        """
        #
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   Dynamic Content Delivery Network (DCDN) supports POST requests in which parameters are sent as a form.
        *   By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        *   You can specify at most 100 URLs in each prefetch request.
        *   The prefetch queue of each Alibaba Cloud account can contain up to 50,000 URLs. DCDN executes prefetch tasks based on the time at which you submit the URLs.
        *   You can call this operation up to 15 times per second per account.
        # Usage notes
        *   After a refresh task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        *   The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        *   To allow RAM users to perform this operation, you need to first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: PreloadDcdnObjectCachesRequest
        @return: PreloadDcdnObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preload_dcdn_object_caches_with_options_async(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: PublishDcdnStagingConfigToProductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishDcdnStagingConfigToProductionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDcdnStagingConfigToProduction',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_dcdn_staging_config_to_production_with_options_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: PublishDcdnStagingConfigToProductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishDcdnStagingConfigToProductionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDcdnStagingConfigToProduction',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_dcdn_staging_config_to_production(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: PublishDcdnStagingConfigToProductionRequest
        @return: PublishDcdnStagingConfigToProductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    async def publish_dcdn_staging_config_to_production_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: PublishDcdnStagingConfigToProductionRequest
        @return: PublishDcdnStagingConfigToProductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_dcdn_staging_config_to_production_with_options_async(request, runtime)

    def publish_routine_code_revision_with_options(
        self,
        tmp_req: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param tmp_req: PublishRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_routine_code_revision_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param tmp_req: PublishRoutineCodeRevisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRoutineCodeRevisionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_routine_code_revision(
        self,
        request: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: PublishRoutineCodeRevisionRequest
        @return: PublishRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_routine_code_revision_with_options(request, runtime)

    async def publish_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: PublishRoutineCodeRevisionRequest
        @return: PublishRoutineCodeRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_routine_code_revision_with_options_async(request, runtime)

    def put_dcdn_kv_with_options(
        self,
        request: dcdn_20180115_models.PutDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PutDcdnKvResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PutDcdnKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_dcdn_kv_with_options_async(
        self,
        request: dcdn_20180115_models.PutDcdnKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PutDcdnKvResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutDcdnKv',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PutDcdnKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_dcdn_kv(
        self,
        request: dcdn_20180115_models.PutDcdnKvRequest,
    ) -> dcdn_20180115_models.PutDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_dcdn_kv_with_options(request, runtime)

    async def put_dcdn_kv_async(
        self,
        request: dcdn_20180115_models.PutDcdnKvRequest,
    ) -> dcdn_20180115_models.PutDcdnKvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_dcdn_kv_with_options_async(request, runtime)

    def put_dcdn_kv_namespace_with_options(
        self,
        request: dcdn_20180115_models.PutDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PutDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PutDcdnKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_dcdn_kv_namespace_with_options_async(
        self,
        request: dcdn_20180115_models.PutDcdnKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PutDcdnKvNamespaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutDcdnKvNamespace',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PutDcdnKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_dcdn_kv_namespace(
        self,
        request: dcdn_20180115_models.PutDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.PutDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_dcdn_kv_namespace_with_options(request, runtime)

    async def put_dcdn_kv_namespace_async(
        self,
        request: dcdn_20180115_models.PutDcdnKvNamespaceRequest,
    ) -> dcdn_20180115_models.PutDcdnKvNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_dcdn_kv_namespace_with_options_async(request, runtime)

    def refresh_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        """
        #
        *   DCDN supports POST requests in which parameters are sent as a form.
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   By default, each Alibaba Cloud account can refresh content from a maximum of 10,000 URLs and 100 directories per day, including subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. DCDN evaluates your application based on your workloads.
        *   You can specify up to 1,000 URLs or 100 directories that you want to refresh in each request.
        *   You can refresh up to 1,000 URLs per minute for each domain name.
        *   You can call this operation up to 30 times per second per account.
        # Precautions
        *   After a refresh task is submitted and completed, your resources that are stored on DCDN POPs are removed. When a POP receives a request to your resources, the request is redirected to the origin server to retrieve the resources. Then, the resources are returned to the client and cached on the POP. If you frequently run refresh tasks, more requests will be redirected back to the origin server for resources, which result in high bandwidth costs and undue pressure on the origin server.
        *   A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        *   If you want to use RAM users to refresh or prefetch resources, you need to obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: RefreshDcdnObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDcdnObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        """
        #
        *   DCDN supports POST requests in which parameters are sent as a form.
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   By default, each Alibaba Cloud account can refresh content from a maximum of 10,000 URLs and 100 directories per day, including subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. DCDN evaluates your application based on your workloads.
        *   You can specify up to 1,000 URLs or 100 directories that you want to refresh in each request.
        *   You can refresh up to 1,000 URLs per minute for each domain name.
        *   You can call this operation up to 30 times per second per account.
        # Precautions
        *   After a refresh task is submitted and completed, your resources that are stored on DCDN POPs are removed. When a POP receives a request to your resources, the request is redirected to the origin server to retrieve the resources. Then, the resources are returned to the client and cached on the POP. If you frequently run refresh tasks, more requests will be redirected back to the origin server for resources, which result in high bandwidth costs and undue pressure on the origin server.
        *   A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        *   If you want to use RAM users to refresh or prefetch resources, you need to obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: RefreshDcdnObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDcdnObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_dcdn_object_caches(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        """
        #
        *   DCDN supports POST requests in which parameters are sent as a form.
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   By default, each Alibaba Cloud account can refresh content from a maximum of 10,000 URLs and 100 directories per day, including subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. DCDN evaluates your application based on your workloads.
        *   You can specify up to 1,000 URLs or 100 directories that you want to refresh in each request.
        *   You can refresh up to 1,000 URLs per minute for each domain name.
        *   You can call this operation up to 30 times per second per account.
        # Precautions
        *   After a refresh task is submitted and completed, your resources that are stored on DCDN POPs are removed. When a POP receives a request to your resources, the request is redirected to the origin server to retrieve the resources. Then, the resources are returned to the client and cached on the POP. If you frequently run refresh tasks, more requests will be redirected back to the origin server for resources, which result in high bandwidth costs and undue pressure on the origin server.
        *   A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        *   If you want to use RAM users to refresh or prefetch resources, you need to obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: RefreshDcdnObjectCachesRequest
        @return: RefreshDcdnObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    async def refresh_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        """
        #
        *   DCDN supports POST requests in which parameters are sent as a form.
        *   You can call the [RefreshDcdnObjectCaches](~~130620~~) operation to refresh content and call the [PreloadDcdnObjectCaches](~~130636~~) operation to prefetch content.
        *   By default, each Alibaba Cloud account can refresh content from a maximum of 10,000 URLs and 100 directories per day, including subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. DCDN evaluates your application based on your workloads.
        *   You can specify up to 1,000 URLs or 100 directories that you want to refresh in each request.
        *   You can refresh up to 1,000 URLs per minute for each domain name.
        *   You can call this operation up to 30 times per second per account.
        # Precautions
        *   After a refresh task is submitted and completed, your resources that are stored on DCDN POPs are removed. When a POP receives a request to your resources, the request is redirected to the origin server to retrieve the resources. Then, the resources are returned to the client and cached on the POP. If you frequently run refresh tasks, more requests will be redirected back to the origin server for resources, which result in high bandwidth costs and undue pressure on the origin server.
        *   A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        *   If you want to use RAM users to refresh or prefetch resources, you need to obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](~~445051~~).
        
        @param request: RefreshDcdnObjectCachesRequest
        @return: RefreshDcdnObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_dcdn_object_caches_with_options_async(request, runtime)

    def rollback_dcdn_staging_config_with_options(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackDcdnStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackDcdnStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackDcdnStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_dcdn_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackDcdnStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackDcdnStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackDcdnStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_dcdn_staging_config(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackDcdnStagingConfigRequest
        @return: RollbackDcdnStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    async def rollback_dcdn_staging_config_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackDcdnStagingConfigRequest
        @return: RollbackDcdnStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_dcdn_staging_config_with_options_async(request, runtime)

    def set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        """
        @deprecated : SetDcdnDomainCertificate is deprecated, please use dcdn::2018-01-15::SetDcdnDomainSSLCertificate instead.
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainCertificateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        """
        @deprecated : SetDcdnDomainCertificate is deprecated, please use dcdn::2018-01-15::SetDcdnDomainSSLCertificate instead.
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainCertificateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_certificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        """
        @deprecated : SetDcdnDomainCertificate is deprecated, please use dcdn::2018-01-15::SetDcdnDomainSSLCertificate instead.
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainCertificateRequest
        @return: SetDcdnDomainCertificateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_certificate_with_options(request, runtime)

    async def set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        """
        @deprecated : SetDcdnDomainCertificate is deprecated, please use dcdn::2018-01-15::SetDcdnDomainSSLCertificate instead.
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainCertificateRequest
        @return: SetDcdnDomainCertificateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_certificate_with_options_async(request, runtime)

    def set_dcdn_domain_smcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainSMCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainSMCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainSMCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_smcertificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainSMCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainSMCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainSMCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainSMCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_smcertificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainSMCertificateRequest
        @return: SetDcdnDomainSMCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_smcertificate_with_options(request, runtime)

    async def set_dcdn_domain_smcertificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainSMCertificateRequest
        @return: SetDcdnDomainSMCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_smcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_sslcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainSSLCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_sslcertificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainSSLCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_sslcertificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSSLCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_sslcertificate_with_options(request, runtime)

    async def set_dcdn_domain_sslcertificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSSLCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_sslcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnDomainStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_staging_config(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainStagingConfigRequest
        @return: SetDcdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    async def set_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnDomainStagingConfigRequest
        @return: SetDcdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_staging_config_with_options_async(request, runtime)

    def set_dcdn_full_domains_block_ipwith_options(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: SetDcdnFullDomainsBlockIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnFullDomainsBlockIPResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDcdnFullDomainsBlockIP',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_full_domains_block_ipwith_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: SetDcdnFullDomainsBlockIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnFullDomainsBlockIPResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDcdnFullDomainsBlockIP',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_full_domains_block_ip(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: SetDcdnFullDomainsBlockIPRequest
        @return: SetDcdnFullDomainsBlockIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_full_domains_block_ipwith_options(request, runtime)

    async def set_dcdn_full_domains_block_ip_async(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        """
        > You can call this operation up to 10 times per second per account.
        
        @param request: SetDcdnFullDomainsBlockIPRequest
        @return: SetDcdnFullDomainsBlockIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_full_domains_block_ipwith_options_async(request, runtime)

    def set_dcdn_user_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnUserConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_user_config_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDcdnUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnUserConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_user_config(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnUserConfigRequest
        @return: SetDcdnUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_user_config_with_options(request, runtime)

    async def set_dcdn_user_config_async(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
        """
        > You can call this operation up to 30 times per second per account.
        
        @param request: SetDcdnUserConfigRequest
        @return: SetDcdnUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_user_config_with_options_async(request, runtime)

    def set_routine_subdomain_with_options(
        self,
        tmp_req: dcdn_20180115_models.SetRoutineSubdomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        """
        >
        *   Each subdomain is globally unique. Resource Access Management (RAM) users cannot create duplicate subdomains.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: SetRoutineSubdomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRoutineSubdomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        body = {}
        if not UtilClient.is_unset(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRoutineSubdomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_routine_subdomain_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.SetRoutineSubdomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        """
        >
        *   Each subdomain is globally unique. Resource Access Management (RAM) users cannot create duplicate subdomains.
        *   You can call this operation up to 100 times per second per account.
        
        @param tmp_req: SetRoutineSubdomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRoutineSubdomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        body = {}
        if not UtilClient.is_unset(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRoutineSubdomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_routine_subdomain(
        self,
        request: dcdn_20180115_models.SetRoutineSubdomainRequest,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        """
        >
        *   Each subdomain is globally unique. Resource Access Management (RAM) users cannot create duplicate subdomains.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: SetRoutineSubdomainRequest
        @return: SetRoutineSubdomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_routine_subdomain_with_options(request, runtime)

    async def set_routine_subdomain_async(
        self,
        request: dcdn_20180115_models.SetRoutineSubdomainRequest,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        """
        >
        *   Each subdomain is globally unique. Resource Access Management (RAM) users cannot create duplicate subdomains.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: SetRoutineSubdomainRequest
        @return: SetRoutineSubdomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_routine_subdomain_with_options_async(request, runtime)

    def start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain is in an invalid state or your account has an overdue payment, the accelerated domain cannot be enabled.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StartDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain is in an invalid state or your account has an overdue payment, the accelerated domain cannot be enabled.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StartDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dcdn_domain(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain is in an invalid state or your account has an overdue payment, the accelerated domain cannot be enabled.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StartDcdnDomainRequest
        @return: StartDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    async def start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        """
        >
        *   If an accelerated domain is in an invalid state or your account has an overdue payment, the accelerated domain cannot be enabled.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StartDcdnDomainRequest
        @return: StartDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_domain_with_options_async(request, runtime)

    def start_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        """
        If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StartDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        """
        If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StartDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        """
        If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StartDcdnIpaDomainRequest
        @return: StartDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    async def start_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        """
        If an accelerated domain name is in invalid state or your account has an overdue payment, the accelerated domain name cannot be enabled.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StartDcdnIpaDomainRequest
        @return: StartDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_ipa_domain_with_options_async(request, runtime)

    def stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        """
        >
        *   After the accelerated domain is disabled, Dynamic Route for CDN retains its information and reroutes all the requests that are destined for the accelerated domain to the origin.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StopDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        """
        >
        *   After the accelerated domain is disabled, Dynamic Route for CDN retains its information and reroutes all the requests that are destined for the accelerated domain to the origin.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StopDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dcdn_domain(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        """
        >
        *   After the accelerated domain is disabled, Dynamic Route for CDN retains its information and reroutes all the requests that are destined for the accelerated domain to the origin.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StopDcdnDomainRequest
        @return: StopDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    async def stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        """
        >
        *   After the accelerated domain is disabled, Dynamic Route for CDN retains its information and reroutes all the requests that are destined for the accelerated domain to the origin.
        *   The maximum number of times that each user can call this operation per second is 30.
        
        @param request: StopDcdnDomainRequest
        @return: StopDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_domain_with_options_async(request, runtime)

    def stop_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        """
        >
        *   If you disable an accelerated domain, the configurations of the accelerated domain are still retained. The system automatically forwards all the requests that are destined for this domain to the origin.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StopDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        """
        >
        *   If you disable an accelerated domain, the configurations of the accelerated domain are still retained. The system automatically forwards all the requests that are destined for this domain to the origin.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StopDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        """
        >
        *   If you disable an accelerated domain, the configurations of the accelerated domain are still retained. The system automatically forwards all the requests that are destined for this domain to the origin.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StopDcdnIpaDomainRequest
        @return: StopDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    async def stop_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        """
        >
        *   If you disable an accelerated domain, the configurations of the accelerated domain are still retained. The system automatically forwards all the requests that are destined for this domain to the origin.
        *   You can call this operation up to 20 times per second per account.
        
        @param request: StopDcdnIpaDomainRequest
        @return: StopDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_ipa_domain_with_options_async(request, runtime)

    def tag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: TagDcdnResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagDcdnResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: TagDcdnResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagDcdnResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_dcdn_resources(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: TagDcdnResourcesRequest
        @return: TagDcdnResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    async def tag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: TagDcdnResourcesRequest
        @return: TagDcdnResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_dcdn_resources_with_options_async(request, runtime)

    def untag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UntagDcdnResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagDcdnResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UntagDcdnResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagDcdnResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_dcdn_resources(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UntagDcdnResourcesRequest
        @return: UntagDcdnResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    async def untag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UntagDcdnResourcesRequest
        @return: UntagDcdnResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_dcdn_resources_with_options_async(request, runtime)

    def update_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        """
        The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        
        @param request: UpdateDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.deliver_id):
            body['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_deliver_task_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        """
        The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        
        @param request: UpdateDcdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.deliver_id):
            body['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_deliver_task(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        """
        The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        
        @param request: UpdateDcdnDeliverTaskRequest
        @return: UpdateDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_deliver_task_with_options(request, runtime)

    async def update_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        """
        The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        
        @param request: UpdateDcdnDeliverTaskRequest
        @return: UpdateDcdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_deliver_task_with_options_async(request, runtime)

    def update_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: UpdateDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: UpdateDcdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_domain(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: UpdateDcdnDomainRequest
        @return: UpdateDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    async def update_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        """
        >  You can call this operation up to 30 times per second per account.
        
        @param request: UpdateDcdnDomainRequest
        @return: UpdateDcdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_domain_with_options_async(request, runtime)

    def update_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        """
        >  You can call this operation up to 20 times per second per account.
        
        @param request: UpdateDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        """
        >  You can call this operation up to 20 times per second per account.
        
        @param request: UpdateDcdnIpaDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnIpaDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        """
        >  You can call this operation up to 20 times per second per account.
        
        @param request: UpdateDcdnIpaDomainRequest
        @return: UpdateDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    async def update_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        """
        >  You can call this operation up to 20 times per second per account.
        
        @param request: UpdateDcdnIpaDomainRequest
        @return: UpdateDcdnIpaDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_ipa_domain_with_options_async(request, runtime)

    def update_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnSLSRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnSLSRealtimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_slsrealtime_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnSLSRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnSLSRealtimeLogDeliveryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_slsrealtime_log_delivery(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnSLSRealtimeLogDeliveryRequest
        @return: UpdateDcdnSLSRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def update_dcdn_slsrealtime_log_delivery_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnSLSRealtimeLogDeliveryRequest
        @return: UpdateDcdnSLSRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def update_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: UpdateDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnSubTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_sub_task_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: UpdateDcdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnSubTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_sub_task(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: UpdateDcdnSubTaskRequest
        @return: UpdateDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_sub_task_with_options(request, runtime)

    async def update_dcdn_sub_task_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        """
        > You can call this operation up to three times per second per account.
        
        @param request: UpdateDcdnSubTaskRequest
        @return: UpdateDcdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_sub_task_with_options_async(request, runtime)

    def update_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnUserRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnUserRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dcdn_user_real_time_delivery_field_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnUserRealTimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDcdnUserRealTimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dcdn_user_real_time_delivery_field(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnUserRealTimeDeliveryFieldRequest
        @return: UpdateDcdnUserRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def update_dcdn_user_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: UpdateDcdnUserRealTimeDeliveryFieldRequest
        @return: UpdateDcdnUserRealTimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def upload_routine_code_with_options(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        """
        >
        *   Each time you submit code, a version of the code is generated. You can manage and publish code by version.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you must call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        """
        >
        *   Each time you submit code, a version of the code is generated. You can manage and publish code by version.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you must call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_routine_code(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        """
        >
        *   Each time you submit code, a version of the code is generated. You can manage and publish code by version.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you must call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadRoutineCodeRequest
        @return: UploadRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_routine_code_with_options(request, runtime)

    async def upload_routine_code_async(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        """
        >
        *   Each time you submit code, a version of the code is generated. You can manage and publish code by version.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you must call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadRoutineCodeRequest
        @return: UploadRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_routine_code_with_options_async(request, runtime)

    def upload_staging_routine_code_with_options(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        """
        >
        *   Each time you upload code to a routine, a version is generated. The number of versions is counted by CodeRev. The uploaded code is used only for testing.
        *   The code is automatically published to a staging environment.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you need to call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadStagingRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadStagingRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_staging_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        """
        >
        *   Each time you upload code to a routine, a version is generated. The number of versions is counted by CodeRev. The uploaded code is used only for testing.
        *   The code is automatically published to a staging environment.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you need to call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadStagingRoutineCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadStagingRoutineCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_staging_routine_code(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        """
        >
        *   Each time you upload code to a routine, a version is generated. The number of versions is counted by CodeRev. The uploaded code is used only for testing.
        *   The code is automatically published to a staging environment.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you need to call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadStagingRoutineCodeRequest
        @return: UploadStagingRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_staging_routine_code_with_options(request, runtime)

    async def upload_staging_routine_code_async(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        """
        >
        *   Each time you upload code to a routine, a version is generated. The number of versions is counted by CodeRev. The uploaded code is used only for testing.
        *   The code is automatically published to a staging environment.
        *   Each routine can retain at most 10 versions. If the upper limit is reached, you need to call the DeleteRoutineCodeRevision operation to manually delete versions that are no longer needed before new versions can be saved.
        *   You can call this operation up to 100 times per second per account.
        
        @param request: UploadStagingRoutineCodeRequest
        @return: UploadStagingRoutineCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_staging_routine_code_with_options_async(request, runtime)

    def verify_dcdn_domain_owner_with_options(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDcdnDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyDcdnDomainOwnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyDcdnDomainOwner',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_dcdn_domain_owner_with_options_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDcdnDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyDcdnDomainOwnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyDcdnDomainOwner',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_dcdn_domain_owner(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDcdnDomainOwnerRequest
        @return: VerifyDcdnDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)

    async def verify_dcdn_domain_owner_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        """
        > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDcdnDomainOwnerRequest
        @return: VerifyDcdnDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_dcdn_domain_owner_with_options_async(request, runtime)
