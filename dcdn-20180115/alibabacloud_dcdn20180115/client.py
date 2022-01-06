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
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    async def add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_domain_with_options_async(request, runtime)

    def add_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    async def add_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_ipa_domain_with_options_async(request, runtime)

    def batch_add_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    async def batch_add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_dcdn_domain_with_options_async(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    async def batch_delete_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_certificate_with_options(request, runtime)

    async def batch_set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_certificate_with_options_async(request, runtime)

    def batch_set_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def batch_start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    async def batch_start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_dcdn_domain_with_options_async(request, runtime)

    def batch_stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    async def batch_stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_dcdn_domain_with_options_async(request, runtime)

    def check_dcdn_project_exist_with_options(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_dcdn_project_exist_with_options(request, runtime)

    async def check_dcdn_project_exist_async(
        self,
        request: dcdn_20180115_models.CheckDcdnProjectExistRequest,
    ) -> dcdn_20180115_models.CheckDcdnProjectExistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_dcdn_project_exist_with_options_async(request, runtime)

    def commit_staging_routine_code_with_options(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.commit_staging_routine_code_with_options(request, runtime)

    async def commit_staging_routine_code_async(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commit_staging_routine_code_with_options_async(request, runtime)

    def create_dcdn_certificate_signing_request_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sans):
            query['SANs'] = request.sans
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDcdnCertificateSigningRequest',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dcdn_certificate_signing_request_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sans):
            query['SANs'] = request.sans
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDcdnCertificateSigningRequest',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dcdn_certificate_signing_request(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_certificate_signing_request_with_options(request, runtime)

    async def create_dcdn_certificate_signing_request_async(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_certificate_signing_request_with_options_async(request, runtime)

    def create_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_deliver_task_with_options(request, runtime)

    async def create_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_deliver_task_with_options_async(request, runtime)

    def create_dcdn_slsreal_time_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_slsreal_time_log_delivery_with_options(request, runtime)

    async def create_dcdn_slsreal_time_log_delivery_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_slsreal_time_log_delivery_with_options_async(request, runtime)

    def create_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_sub_task_with_options(request, runtime)

    async def create_dcdn_sub_task_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_sub_task_with_options_async(request, runtime)

    def create_routine_with_options(
        self,
        tmp_req: dcdn_20180115_models.CreateRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    async def create_routine_async(
        self,
        request: dcdn_20180115_models.CreateRoutineRequest,
    ) -> dcdn_20180115_models.CreateRoutineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_routine_with_options_async(request, runtime)

    def create_slr_and_sls_project_with_options(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.create_slr_and_sls_project_with_options(request, runtime)

    async def create_slr_and_sls_project_async(
        self,
        request: dcdn_20180115_models.CreateSlrAndSlsProjectRequest,
    ) -> dcdn_20180115_models.CreateSlrAndSlsProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_slr_and_sls_project_with_options_async(request, runtime)

    def delete_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_deliver_task_with_options(request, runtime)

    async def delete_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_deliver_task_with_options_async(request, runtime)

    def delete_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    async def delete_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    async def delete_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    async def delete_dcdn_ipa_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_specific_config_with_options_async(request, runtime)

    def delete_dcdn_real_time_log_project_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_real_time_log_project_with_options(request, runtime)

    async def delete_dcdn_real_time_log_project_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnRealTimeLogProjectRequest,
    ) -> dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_real_time_log_project_with_options_async(request, runtime)

    def delete_dcdn_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    async def delete_dcdn_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_config_with_options_async(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    async def delete_dcdn_specific_staging_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_staging_config_with_options_async(request, runtime)

    def delete_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DeleteDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def delete_dcdn_sub_task(
        self,
        request: dcdn_20180115_models.DeleteDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_sub_task_with_options(request, runtime)

    async def delete_dcdn_sub_task_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_sub_task_with_options_async(request, runtime)

    def delete_routine_with_options(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    async def delete_routine_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_with_options_async(request, runtime)

    def delete_routine_code_revision_with_options(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_code_revision_with_options(request, runtime)

    async def delete_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_code_revision_with_options_async(request, runtime)

    def delete_routine_conf_envs_with_options(
        self,
        tmp_req: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_conf_envs_with_options(request, runtime)

    async def delete_routine_conf_envs_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineConfEnvsRequest,
    ) -> dcdn_20180115_models.DeleteRoutineConfEnvsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_conf_envs_with_options_async(request, runtime)

    def describe_dcdn_acl_fields_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_acl_fields_with_options(request, runtime)

    async def describe_dcdn_acl_fields_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnAclFieldsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnAclFieldsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_acl_fields_with_options_async(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    async def describe_dcdn_bgp_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_bps_data_with_options_async(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    async def describe_dcdn_bgp_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_blocked_regions_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_blocked_regions_with_options(request, runtime)

    async def describe_dcdn_blocked_regions_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_blocked_regions_with_options_async(request, runtime)

    def describe_dcdn_certificate_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    async def describe_dcdn_certificate_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_detail_with_options_async(request, runtime)

    def describe_dcdn_certificate_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    async def describe_dcdn_certificate_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_list_with_options_async(request, runtime)

    def describe_dcdn_config_group_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.config_group_name):
            query['ConfigGroupName'] = request.config_group_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigGroupDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_config_group_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.config_group_name):
            query['ConfigGroupName'] = request.config_group_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigGroupDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_config_group_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigGroupDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_group_detail_with_options(request, runtime)

    async def describe_dcdn_config_group_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigGroupDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_config_group_detail_with_options_async(request, runtime)

    def describe_dcdn_config_of_version_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_config_of_version(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_of_version_with_options(request, runtime)

    async def describe_dcdn_config_of_version_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_config_of_version_with_options_async(request, runtime)

    def describe_dcdn_deleted_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deleted_domains_with_options(request, runtime)

    async def describe_dcdn_deleted_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeletedDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_deleted_domains_with_options_async(request, runtime)

    def describe_dcdn_deliver_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deliver_list_with_options(request, runtime)

    async def describe_dcdn_deliver_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_deliver_list_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    async def describe_dcdn_domain_by_certificate_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_dcdn_domain_cc_activity_log_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cc_activity_log_with_options(request, runtime)

    async def describe_dcdn_domain_cc_activity_log_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCcActivityLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    async def describe_dcdn_domain_certificate_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_dcdn_domain_cname_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    async def describe_dcdn_domain_cname_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_cname_with_options_async(request, runtime)

    def describe_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    async def describe_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    async def describe_dcdn_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    async def describe_dcdn_domain_isp_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_isp_data_with_options_async(request, runtime)

    def describe_dcdn_domain_log_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    async def describe_dcdn_domain_log_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_log_with_options_async(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_multi_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_property_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    async def describe_dcdn_domain_property_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_with_options_async(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_detail_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_region_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    async def describe_dcdn_domain_region_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_region_data_with_options_async(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    async def describe_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_staging_config_with_options_async(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_refer_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_url_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    async def describe_dcdn_domain_uv_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_uv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_es_exception_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExceptionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExceptionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_es_exception_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExceptionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExceptionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_es_exception_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExceptionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_es_exception_data_with_options(request, runtime)

    async def describe_dcdn_es_exception_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExceptionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_es_exception_data_with_options_async(request, runtime)

    def describe_dcdn_es_execute_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExecuteDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExecuteData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dcdn_es_execute_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExecuteDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExecuteData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dcdn_es_execute_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExecuteDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_es_execute_data_with_options(request, runtime)

    async def describe_dcdn_es_execute_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnEsExecuteDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_es_execute_data_with_options_async(request, runtime)

    def describe_dcdn_https_domain_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    async def describe_dcdn_https_domain_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_https_domain_list_with_options_async(request, runtime)

    def describe_dcdn_ip_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    async def describe_dcdn_ip_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ip_info_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_ipa_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    async def describe_dcdn_ipa_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_service_with_options_async(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    async def describe_dcdn_ipa_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_user_domains_with_options_async(request, runtime)

    def describe_dcdn_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_refresh_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    async def describe_dcdn_refresh_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_quota_with_options_async(request, runtime)

    def describe_dcdn_refresh_task_by_id_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_task_by_id_with_options(request, runtime)

    async def describe_dcdn_refresh_task_by_id_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_task_by_id_with_options_async(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    async def describe_dcdn_refresh_tasks_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_tasks_with_options_async(request, runtime)

    def describe_dcdn_region_and_isp_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    async def describe_dcdn_region_and_isp_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_region_and_isp_with_options_async(request, runtime)

    def describe_dcdn_report_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_with_options(request, runtime)

    async def describe_dcdn_report_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_report_with_options_async(request, runtime)

    def describe_dcdn_report_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_list_with_options(request, runtime)

    async def describe_dcdn_report_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_report_list_with_options_async(request, runtime)

    def describe_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def describe_dcdn_slsrealtime_log_delivery_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_detail_with_options(request, runtime)

    async def describe_dcdn_smcertificate_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_dcdn_smcertificate_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_list_with_options(request, runtime)

    async def describe_dcdn_smcertificate_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSMCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSMCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_smcertificate_list_with_options_async(request, runtime)

    def describe_dcdn_sec_func_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_func_info_with_options(request, runtime)

    async def describe_dcdn_sec_func_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sec_func_info_with_options_async(request, runtime)

    def describe_dcdn_sec_spec_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeDcdnSecSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_dcdn_sec_spec_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecSpecInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_spec_info_with_options(request, runtime)

    async def describe_dcdn_sec_spec_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecSpecInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sec_spec_info_with_options_async(request, runtime)

    def describe_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    async def describe_dcdn_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_service_with_options_async(request, runtime)

    def describe_dcdn_staging_ip_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_dcdn_staging_ip(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(request, runtime)

    async def describe_dcdn_staging_ip_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_staging_ip_with_options_async(request, runtime)

    def describe_dcdn_sub_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSubListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeDcdnSubListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_dcdn_sub_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnSubListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sub_list_with_options(request, runtime)

    async def describe_dcdn_sub_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSubListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_sub_list_with_options_async(request, runtime)

    def describe_dcdn_tag_resources_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    async def describe_dcdn_tag_resources_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_tag_resources_with_options_async(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_dcdn_top_domains_by_flow_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_dcdn_user_bill_history_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    async def describe_dcdn_user_bill_history_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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

    def describe_dcdn_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    async def describe_dcdn_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_with_options_async(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    async def describe_dcdn_user_domains_by_func_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_dcdn_user_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    async def describe_dcdn_user_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_quota_with_options_async(request, runtime)

    def describe_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def describe_dcdn_user_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_user_resource_package_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    async def describe_dcdn_user_resource_package_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_resource_package_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_by_minute_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_by_minute_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_by_minute_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_by_minute_with_options_async(request, runtime)

    def describe_dcdn_user_tags_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_dcdn_user_tags(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(request, runtime)

    async def describe_dcdn_user_tags_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_tags_with_options_async(request, runtime)

    def describe_dcdn_verify_content_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    async def describe_dcdn_verify_content_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_verify_content_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    async def describe_dcdn_waf_domain_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_domain_with_options_async(request, runtime)

    def describe_dcdnsec_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdnsec_service_with_options(request, runtime)

    async def describe_dcdnsec_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnsecServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnsecServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdnsec_service_with_options_async(request, runtime)

    def describe_routine_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_with_options(request, runtime)

    async def describe_routine_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_with_options_async(request, runtime)

    def describe_routine_canary_envs_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineCanaryEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeRoutineCanaryEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_routine_canary_envs(
        self,
        request: dcdn_20180115_models.DescribeRoutineCanaryEnvsRequest,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_canary_envs_with_options(request, runtime)

    async def describe_routine_canary_envs_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCanaryEnvsRequest,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_canary_envs_with_options_async(request, runtime)

    def describe_routine_code_revision_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_code_revision_with_options(request, runtime)

    async def describe_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_code_revision_with_options_async(request, runtime)

    def describe_routine_spec_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeRoutineSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_routine_spec(
        self,
        request: dcdn_20180115_models.DescribeRoutineSpecRequest,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_spec_with_options(request, runtime)

    async def describe_routine_spec_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineSpecRequest,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_spec_with_options_async(request, runtime)

    def describe_routine_user_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: dcdn_20180115_models.DescribeRoutineUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def describe_routine_user_info(
        self,
        request: dcdn_20180115_models.DescribeRoutineUserInfoRequest,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_user_info_with_options(request, runtime)

    async def describe_routine_user_info_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineUserInfoRequest,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_routine_user_info_with_options_async(request, runtime)

    def describe_user_dcdn_ipa_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    async def describe_user_dcdn_ipa_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_ipa_status_with_options_async(request, runtime)

    def describe_user_dcdn_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    async def describe_user_dcdn_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_status_with_options_async(request, runtime)

    def describe_user_er_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_user_er_status_with_options(request, runtime)

    async def describe_user_er_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_er_status_with_options_async(request, runtime)

    def describe_user_logservice_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_user_logservice_status_with_options(request, runtime)

    async def describe_user_logservice_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_logservice_status_with_options_async(request, runtime)

    def edit_routine_conf_with_options(
        self,
        tmp_req: dcdn_20180115_models.EditRoutineConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.edit_routine_conf_with_options(request, runtime)

    async def edit_routine_conf_async(
        self,
        request: dcdn_20180115_models.EditRoutineConfRequest,
    ) -> dcdn_20180115_models.EditRoutineConfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_routine_conf_with_options_async(request, runtime)

    def list_dcdn_real_time_delivery_project_with_options(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.list_dcdn_real_time_delivery_project_with_options(request, runtime)

    async def list_dcdn_real_time_delivery_project_async(
        self,
        request: dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectRequest,
    ) -> dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dcdn_real_time_delivery_project_with_options_async(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_dcdn_domain_schdm_by_property_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_domain_schdm_by_property_with_options_async(request, runtime)

    def open_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    async def open_dcdn_service_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_dcdn_service_with_options_async(request, runtime)

    def preload_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
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
        runtime = util_models.RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    async def preload_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_dcdn_object_caches_with_options_async(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    async def publish_dcdn_staging_config_to_production_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_dcdn_staging_config_to_production_with_options_async(request, runtime)

    def publish_routine_code_revision_with_options(
        self,
        tmp_req: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.publish_routine_code_revision_with_options(request, runtime)

    async def publish_routine_code_revision_async(
        self,
        request: dcdn_20180115_models.PublishRoutineCodeRevisionRequest,
    ) -> dcdn_20180115_models.PublishRoutineCodeRevisionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_routine_code_revision_with_options_async(request, runtime)

    def refresh_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    async def refresh_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_dcdn_object_caches_with_options_async(request, runtime)

    def rollback_dcdn_staging_config_with_options(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    async def rollback_dcdn_staging_config_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_dcdn_staging_config_with_options_async(request, runtime)

    def set_dcdn_config_of_version_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_config_of_version(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_config_of_version_with_options(request, runtime)

    async def set_dcdn_config_of_version_async(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_config_of_version_with_options_async(request, runtime)

    def set_dcdn_domain_csrcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainCSRCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dcdn_domain_csrcertificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainCSRCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dcdn_domain_csrcertificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_csrcertificate_with_options(request, runtime)

    async def set_dcdn_domain_csrcertificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_certificate_with_options(request, runtime)

    async def set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_certificate_with_options_async(request, runtime)

    def set_dcdn_domain_smcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_smcertificate_with_options(request, runtime)

    async def set_dcdn_domain_smcertificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainSMCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainSMCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_smcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    async def set_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_staging_config_with_options_async(request, runtime)

    def set_dcdn_full_domains_block_ipwith_options(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_full_domains_block_ipwith_options(request, runtime)

    async def set_dcdn_full_domains_block_ip_async(
        self,
        request: dcdn_20180115_models.SetDcdnFullDomainsBlockIPRequest,
    ) -> dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_full_domains_block_ipwith_options_async(request, runtime)

    def set_dcdn_user_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_user_config_with_options(request, runtime)

    async def set_dcdn_user_config_async(
        self,
        request: dcdn_20180115_models.SetDcdnUserConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_user_config_with_options_async(request, runtime)

    def set_routine_subdomain_with_options(
        self,
        tmp_req: dcdn_20180115_models.SetRoutineSubdomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.set_routine_subdomain_with_options(request, runtime)

    async def set_routine_subdomain_async(
        self,
        request: dcdn_20180115_models.SetRoutineSubdomainRequest,
    ) -> dcdn_20180115_models.SetRoutineSubdomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_routine_subdomain_with_options_async(request, runtime)

    def start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    async def start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_domain_with_options_async(request, runtime)

    def start_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    async def start_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_ipa_domain_with_options_async(request, runtime)

    def stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    async def stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_domain_with_options_async(request, runtime)

    def stop_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    async def stop_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_ipa_domain_with_options_async(request, runtime)

    def tag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    async def tag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_dcdn_resources_with_options_async(request, runtime)

    def untag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    async def untag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_dcdn_resources_with_options_async(request, runtime)

    def update_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_deliver_task_with_options(request, runtime)

    async def update_dcdn_deliver_task_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_deliver_task_with_options_async(request, runtime)

    def update_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    async def update_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_domain_with_options_async(request, runtime)

    def update_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    async def update_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_ipa_domain_with_options_async(request, runtime)

    def update_dcdn_slsrealtime_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    async def update_dcdn_slsrealtime_log_delivery_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_slsrealtime_log_delivery_with_options_async(request, runtime)

    def update_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_sub_task_with_options(request, runtime)

    async def update_dcdn_sub_task_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_sub_task_with_options_async(request, runtime)

    def update_dcdn_user_real_time_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    async def update_dcdn_user_real_time_delivery_field_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldRequest,
    ) -> dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_user_real_time_delivery_field_with_options_async(request, runtime)

    def upload_routine_code_with_options(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.upload_routine_code_with_options(request, runtime)

    async def upload_routine_code_async(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_routine_code_with_options_async(request, runtime)

    def upload_staging_routine_code_with_options(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        runtime = util_models.RuntimeOptions()
        return self.upload_staging_routine_code_with_options(request, runtime)

    async def upload_staging_routine_code_async(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_staging_routine_code_with_options_async(request, runtime)

    def verify_dcdn_domain_owner_with_options(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)

    async def verify_dcdn_domain_owner_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_dcdn_domain_owner_with_options_async(request, runtime)
