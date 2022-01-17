# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdn20180510 import models as cdn_20180510_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'cdn.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='AddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='AddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cdn_domain(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cdn_domain_with_options(request, runtime)

    async def add_cdn_domain_async(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cdn_domain_with_options_async(request, runtime)

    def add_fctrigger_with_options(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.event_meta_name):
            body['EventMetaName'] = request.event_meta_name
        if not UtilClient.is_unset(request.event_meta_version):
            body['EventMetaVersion'] = request.event_meta_version
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.event_meta_name):
            body['EventMetaName'] = request.event_meta_name
        if not UtilClient.is_unset(request.event_meta_version):
            body['EventMetaVersion'] = request.event_meta_version
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fctrigger(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_fctrigger_with_options(request, runtime)

    async def add_fctrigger_async(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_fctrigger_with_options_async(request, runtime)

    def batch_add_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='BatchAddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchAddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='BatchAddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchAddCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_cdn_domain(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_cdn_domain_with_options(request, runtime)

    async def batch_add_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_cdn_domain_with_options_async(request, runtime)

    def batch_delete_cdn_domain_config_with_options(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
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
            action='BatchDeleteCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchDeleteCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_cdn_domain_config_with_options_async(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
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
            action='BatchDeleteCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchDeleteCdnDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_cdn_domain_config(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_cdn_domain_config_with_options(request, runtime)

    async def batch_delete_cdn_domain_config_async(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_cdn_domain_config_with_options_async(request, runtime)

    def batch_set_cdn_domain_config_with_options(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
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
            action='BatchSetCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_cdn_domain_config_with_options_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
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
            action='BatchSetCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_cdn_domain_config(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_config_with_options(request, runtime)

    async def batch_set_cdn_domain_config_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_cdn_domain_config_with_options_async(request, runtime)

    def batch_set_cdn_domain_server_certificate_with_options(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
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
            action='BatchSetCdnDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_cdn_domain_server_certificate_with_options_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
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
            action='BatchSetCdnDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_cdn_domain_server_certificate(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_server_certificate_with_options(request, runtime)

    async def batch_set_cdn_domain_server_certificate_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_cdn_domain_server_certificate_with_options_async(request, runtime)

    def batch_start_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
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
            action='BatchStartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
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
            action='BatchStartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStartCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_cdn_domain(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_start_cdn_domain_with_options(request, runtime)

    async def batch_start_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_cdn_domain_with_options_async(request, runtime)

    def batch_stop_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
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
            action='BatchStopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
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
            action='BatchStopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStopCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_cdn_domain(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_cdn_domain_with_options(request, runtime)

    async def batch_stop_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_cdn_domain_with_options_async(request, runtime)

    def batch_update_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
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
            action='BatchUpdateCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchUpdateCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
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
            action='BatchUpdateCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchUpdateCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_cdn_domain(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_update_cdn_domain_with_options(request, runtime)

    async def batch_update_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_cdn_domain_with_options_async(request, runtime)

    def create_cdn_certificate_signing_request_with_options(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
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
            action='CreateCdnCertificateSigningRequest',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_certificate_signing_request_with_options_async(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
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
            action='CreateCdnCertificateSigningRequest',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnCertificateSigningRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_certificate_signing_request(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_certificate_signing_request_with_options(request, runtime)

    async def create_cdn_certificate_signing_request_async(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_certificate_signing_request_with_options_async(request, runtime)

    def create_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
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
            action='CreateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_deliver_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
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
            action='CreateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_deliver_task(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_deliver_task_with_options(request, runtime)

    async def create_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_deliver_task_with_options_async(request, runtime)

    def create_cdn_sub_task_with_options(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
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
            action='CreateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_sub_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
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
            action='CreateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_sub_task(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_sub_task_with_options(request, runtime)

    async def create_cdn_sub_task_async(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_sub_task_with_options_async(request, runtime)

    def create_illegal_url_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateIllegalUrlExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_illegal_url_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateIllegalUrlExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_illegal_url_export_task(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_illegal_url_export_task_with_options(request, runtime)

    async def create_illegal_url_export_task_async(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_illegal_url_export_task_with_options_async(request, runtime)

    def create_real_time_log_delivery_with_options(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRealTimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_real_time_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRealTimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateRealTimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_real_time_log_delivery(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_real_time_log_delivery_with_options(request, runtime)

    async def create_real_time_log_delivery_async(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_real_time_log_delivery_with_options_async(request, runtime)

    def create_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_usage_detail_data_export_task(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_usage_detail_data_export_task_with_options(request, runtime)

    async def create_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_usage_detail_data_export_task_with_options_async(request, runtime)

    def create_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_usage_data_export_task(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_usage_data_export_task_with_options(request, runtime)

    async def create_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_usage_data_export_task_with_options_async(request, runtime)

    def delete_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
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
            action='DeleteCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_deliver_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
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
            action='DeleteCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_deliver_task(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_deliver_task_with_options(request, runtime)

    async def delete_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_deliver_task_with_options_async(request, runtime)

    def delete_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
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
            action='DeleteCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
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
            action='DeleteCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_domain(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_domain_with_options(request, runtime)

    async def delete_cdn_domain_async(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_domain_with_options_async(request, runtime)

    def delete_cdn_sub_task_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_sub_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_sub_task(
        self,
        request: cdn_20180510_models.DeleteCdnSubTaskRequest,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_sub_task_with_options(request, runtime)

    async def delete_cdn_sub_task_async(
        self,
        request: cdn_20180510_models.DeleteCdnSubTaskRequest,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_sub_task_with_options_async(request, runtime)

    def delete_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fctrigger(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_fctrigger_with_options(request, runtime)

    async def delete_fctrigger_async(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_fctrigger_with_options_async(request, runtime)

    def delete_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_realtime_log_delivery(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_realtime_log_delivery_with_options(request, runtime)

    async def delete_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_realtime_log_delivery_with_options_async(request, runtime)

    def delete_specific_config_with_options(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
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
            action='DeleteSpecificConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_specific_config_with_options_async(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
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
            action='DeleteSpecificConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_specific_config(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_config_with_options(request, runtime)

    async def delete_specific_config_async(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_specific_config_with_options_async(request, runtime)

    def delete_specific_staging_config_with_options(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
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
            action='DeleteSpecificStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_specific_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
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
            action='DeleteSpecificStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_specific_staging_config(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_staging_config_with_options(request, runtime)

    async def delete_specific_staging_config_async(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_specific_staging_config_with_options_async(request, runtime)

    def delete_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
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
            action='DeleteUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
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
            action='DeleteUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_usage_detail_data_export_task(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_usage_detail_data_export_task_with_options(request, runtime)

    async def delete_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_usage_detail_data_export_task_with_options_async(request, runtime)

    def delete_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
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
            action='DeleteUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
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
            action='DeleteUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_usage_data_export_task(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_usage_data_export_task_with_options(request, runtime)

    async def delete_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_active_version_of_config_group_with_options(
        self,
        request: cdn_20180510_models.DescribeActiveVersionOfConfigGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveVersionOfConfigGroup',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_version_of_config_group_with_options_async(
        self,
        request: cdn_20180510_models.DescribeActiveVersionOfConfigGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveVersionOfConfigGroup',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_version_of_config_group(
        self,
        request: cdn_20180510_models.DescribeActiveVersionOfConfigGroupRequest,
    ) -> cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_version_of_config_group_with_options(request, runtime)

    async def describe_active_version_of_config_group_async(
        self,
        request: cdn_20180510_models.DescribeActiveVersionOfConfigGroupRequest,
    ) -> cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_version_of_config_group_with_options_async(request, runtime)

    def describe_blocked_regions_with_options(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockedRegions',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blocked_regions_with_options_async(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockedRegions',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeBlockedRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blocked_regions(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blocked_regions_with_options(request, runtime)

    async def describe_blocked_regions_async(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blocked_regions_with_options_async(request, runtime)

    def describe_cdn_certificate_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
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
            action='DescribeCdnCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
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
            action='DescribeCdnCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_detail(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_detail_with_options(request, runtime)

    async def describe_cdn_certificate_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certificate_detail_with_options_async(request, runtime)

    def describe_cdn_certificate_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
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
            action='DescribeCdnCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
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
            action='DescribeCdnCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_list(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_list_with_options(request, runtime)

    async def describe_cdn_certificate_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certificate_list_with_options_async(request, runtime)

    def describe_cdn_deleted_domains_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
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
            action='DescribeCdnDeletedDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_deleted_domains_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
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
            action='DescribeCdnDeletedDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeletedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_deleted_domains(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deleted_domains_with_options(request, runtime)

    async def describe_cdn_deleted_domains_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_deleted_domains_with_options_async(request, runtime)

    def describe_cdn_deliver_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
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
            action='DescribeCdnDeliverList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_deliver_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
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
            action='DescribeCdnDeliverList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeliverListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_deliver_list(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deliver_list_with_options(request, runtime)

    async def describe_cdn_deliver_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_deliver_list_with_options_async(request, runtime)

    def describe_cdn_domain_by_certificate_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
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
            action='DescribeCdnDomainByCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_by_certificate_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
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
            action='DescribeCdnDomainByCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainByCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_by_certificate(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_by_certificate_with_options(request, runtime)

    async def describe_cdn_domain_by_certificate_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_cdn_domain_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
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
            action='DescribeCdnDomainConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
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
            action='DescribeCdnDomainConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_configs(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_configs_with_options(request, runtime)

    async def describe_cdn_domain_configs_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_configs_with_options_async(request, runtime)

    def describe_cdn_domain_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
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
            action='DescribeCdnDomainDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
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
            action='DescribeCdnDomainDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_detail(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_detail_with_options(request, runtime)

    async def describe_cdn_domain_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_detail_with_options_async(request, runtime)

    def describe_cdn_domain_logs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
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
            action='DescribeCdnDomainLogs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_logs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
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
            action='DescribeCdnDomainLogs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_logs(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_logs_with_options(request, runtime)

    async def describe_cdn_domain_logs_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_logs_with_options_async(request, runtime)

    def describe_cdn_domain_staging_config_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
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
            action='DescribeCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
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
            action='DescribeCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_staging_config(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_staging_config_with_options(request, runtime)

    async def describe_cdn_domain_staging_config_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_staging_config_with_options_async(request, runtime)

    def describe_cdn_https_domain_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
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
            action='DescribeCdnHttpsDomainList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_https_domain_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
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
            action='DescribeCdnHttpsDomainList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnHttpsDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_https_domain_list(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_https_domain_list_with_options(request, runtime)

    async def describe_cdn_https_domain_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_https_domain_list_with_options_async(request, runtime)

    def describe_cdn_region_and_isp_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
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
            action='DescribeCdnRegionAndIsp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_region_and_isp_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
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
            action='DescribeCdnRegionAndIsp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnRegionAndIspResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_region_and_isp(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_region_and_isp_with_options(request, runtime)

    async def describe_cdn_region_and_isp_async(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_region_and_isp_with_options_async(request, runtime)

    def describe_cdn_report_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
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
            action='DescribeCdnReport',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_report_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
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
            action='DescribeCdnReport',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_report(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_with_options(request, runtime)

    async def describe_cdn_report_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_report_with_options_async(request, runtime)

    def describe_cdn_report_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
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
            action='DescribeCdnReportList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_report_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
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
            action='DescribeCdnReportList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_report_list(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_list_with_options(request, runtime)

    async def describe_cdn_report_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_report_list_with_options_async(request, runtime)

    def describe_cdn_smcertificate_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
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
            action='DescribeCdnSMCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_smcertificate_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
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
            action='DescribeCdnSMCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_smcertificate_detail(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_detail_with_options(request, runtime)

    async def describe_cdn_smcertificate_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_cdn_smcertificate_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
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
            action='DescribeCdnSMCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_smcertificate_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
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
            action='DescribeCdnSMCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_smcertificate_list(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_list_with_options(request, runtime)

    async def describe_cdn_smcertificate_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_smcertificate_list_with_options_async(request, runtime)

    def describe_cdn_service_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
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
            action='DescribeCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_service_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
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
            action='DescribeCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_service(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_service_with_options(request, runtime)

    async def describe_cdn_service_async(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_service_with_options_async(request, runtime)

    def describe_cdn_sub_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSubListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSubList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sub_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnSubListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSubList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSubListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sub_list(
        self,
        request: cdn_20180510_models.DescribeCdnSubListRequest,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_sub_list_with_options(request, runtime)

    async def describe_cdn_sub_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnSubListRequest,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_sub_list_with_options_async(request, runtime)

    def describe_cdn_user_bill_history_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
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
            action='DescribeCdnUserBillHistory',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_history_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
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
            action='DescribeCdnUserBillHistory',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_history(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_history_with_options(request, runtime)

    async def describe_cdn_user_bill_history_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_history_with_options_async(request, runtime)

    def describe_cdn_user_bill_prediction_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
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
            action='DescribeCdnUserBillPrediction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillPredictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_prediction_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
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
            action='DescribeCdnUserBillPrediction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillPredictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_prediction(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_prediction_with_options(request, runtime)

    async def describe_cdn_user_bill_prediction_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_prediction_with_options_async(request, runtime)

    def describe_cdn_user_bill_type_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
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
            action='DescribeCdnUserBillType',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_bill_type_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
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
            action='DescribeCdnUserBillType',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_bill_type(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_type_with_options(request, runtime)

    async def describe_cdn_user_bill_type_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_type_with_options_async(request, runtime)

    def describe_cdn_user_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_configs(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_configs_with_options(request, runtime)

    async def describe_cdn_user_configs_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_configs_with_options_async(request, runtime)

    def describe_cdn_user_domains_by_func_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeCdnUserDomainsByFunc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_domains_by_func_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeCdnUserDomainsByFunc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_domains_by_func(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_domains_by_func_with_options(request, runtime)

    async def describe_cdn_user_domains_by_func_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_cdn_user_quota_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
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
            action='DescribeCdnUserQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_quota_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
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
            action='DescribeCdnUserQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_quota(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_quota_with_options(request, runtime)

    async def describe_cdn_user_quota_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_quota_with_options_async(request, runtime)

    def describe_cdn_user_resource_package_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
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
            action='DescribeCdnUserResourcePackage',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_user_resource_package_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
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
            action='DescribeCdnUserResourcePackage',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_user_resource_package(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_resource_package_with_options(request, runtime)

    async def describe_cdn_user_resource_package_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_resource_package_with_options_async(request, runtime)

    def describe_cdn_waf_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
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
            action='DescribeCdnWafDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_waf_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
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
            action='DescribeCdnWafDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnWafDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_waf_domain(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_waf_domain_with_options(request, runtime)

    async def describe_cdn_waf_domain_async(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_waf_domain_with_options_async(request, runtime)

    def describe_certificate_info_by_idwith_options(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificateInfoByID',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCertificateInfoByIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_info_by_idwith_options_async(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificateInfoByID',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCertificateInfoByIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_info_by_id(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_info_by_idwith_options(request, runtime)

    async def describe_certificate_info_by_id_async(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_info_by_idwith_options_async(request, runtime)

    def describe_config_group_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeConfigGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigGroupDetailResponse:
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
            action='DescribeConfigGroupDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_group_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeConfigGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigGroupDetailResponse:
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
            action='DescribeConfigGroupDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_group_detail(
        self,
        request: cdn_20180510_models.DescribeConfigGroupDetailRequest,
    ) -> cdn_20180510_models.DescribeConfigGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_config_group_detail_with_options(request, runtime)

    async def describe_config_group_detail_async(
        self,
        request: cdn_20180510_models.DescribeConfigGroupDetailRequest,
    ) -> cdn_20180510_models.DescribeConfigGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_config_group_detail_with_options_async(request, runtime)

    def describe_config_of_version_with_options(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
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
            action='DescribeConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_of_version_with_options_async(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
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
            action='DescribeConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigOfVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_of_version(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_config_of_version_with_options(request, runtime)

    async def describe_config_of_version_async(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_config_of_version_with_options_async(request, runtime)

    def describe_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_log_config(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_log_config_with_options(request, runtime)

    async def describe_custom_log_config_async(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_log_config_with_options_async(request, runtime)

    def describe_domain_average_response_time_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
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
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAverageResponseTime',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainAverageResponseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_average_response_time_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
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
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAverageResponseTime',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainAverageResponseTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_average_response_time(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_average_response_time_with_options(request, runtime)

    async def describe_domain_average_response_time_async(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_average_response_time_with_options_async(request, runtime)

    def describe_domain_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
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
            action='DescribeDomainBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
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
            action='DescribeDomainBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_with_options(request, runtime)

    async def describe_domain_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_with_options_async(request, runtime)

    def describe_domain_bps_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data_by_layer(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_domain_bps_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_bps_data_by_time_stamp_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByTimeStamp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByTimeStamp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data_by_time_stamp(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_time_stamp_with_options(request, runtime)

    async def describe_domain_bps_data_by_time_stamp_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_by_time_stamp_with_options_async(request, runtime)

    def describe_domain_cc_activity_log_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
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
            action='DescribeDomainCcActivityLog',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_cc_activity_log_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
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
            action='DescribeDomainCcActivityLog',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCcActivityLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_cc_activity_log(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_cc_activity_log_with_options(request, runtime)

    async def describe_domain_cc_activity_log_async(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_domain_certificate_info_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
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
            action='DescribeDomainCertificateInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_certificate_info_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
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
            action='DescribeDomainCertificateInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_certificate_info(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_certificate_info_with_options(request, runtime)

    async def describe_domain_certificate_info_async(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_certificate_info_with_options_async(request, runtime)

    def describe_domain_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_custom_log_config(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_custom_log_config_with_options(request, runtime)

    async def describe_domain_custom_log_config_async(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_custom_log_config_with_options_async(request, runtime)

    def describe_domain_detail_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetailDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainDetailDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetailDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainDetailDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail_data_by_layer(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_data_by_layer_with_options(request, runtime)

    async def describe_domain_detail_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_detail_data_by_layer_with_options_async(request, runtime)

    def describe_domain_file_size_proportion_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainFileSizeProportionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFileSizeProportionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_file_size_proportion_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainFileSizeProportionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFileSizeProportionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_file_size_proportion_data(
        self,
        request: cdn_20180510_models.DescribeDomainFileSizeProportionDataRequest,
    ) -> cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_file_size_proportion_data_with_options(request, runtime)

    async def describe_domain_file_size_proportion_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainFileSizeProportionDataRequest,
    ) -> cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_file_size_proportion_data_with_options_async(request, runtime)

    def describe_domain_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
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
            action='DescribeDomainHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
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
            action='DescribeDomainHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_hit_rate_data(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_hit_rate_data_with_options(request, runtime)

    async def describe_domain_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
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
            action='DescribeDomainHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
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
            action='DescribeDomainHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_http_code_data(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_with_options(request, runtime)

    async def describe_domain_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_http_code_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHttpCodeDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_http_code_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHttpCodeDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_http_code_data_by_layer(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_by_layer_with_options(request, runtime)

    async def describe_domain_http_code_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_http_code_data_by_layer_with_options_async(request, runtime)

    def describe_domain_ispdata_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
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
            action='DescribeDomainISPData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainISPDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_ispdata_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
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
            action='DescribeDomainISPData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainISPDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_ispdata(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ispdata_with_options(request, runtime)

    async def describe_domain_ispdata_async(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_ispdata_with_options_async(request, runtime)

    def describe_domain_max_95bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainMax95BpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMax95BpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_max_95bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainMax95BpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMax95BpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_max_95bps_data(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_max_95bps_data_with_options(request, runtime)

    async def describe_domain_max_95bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_max_95bps_data_with_options_async(request, runtime)

    def describe_domain_multi_usage_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
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
            action='DescribeDomainMultiUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_multi_usage_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
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
            action='DescribeDomainMultiUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMultiUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_multi_usage_data(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_multi_usage_data_with_options(request, runtime)

    async def describe_domain_multi_usage_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_domain_names_of_version_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNamesOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainNamesOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_names_of_version_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNamesOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainNamesOfVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_names_of_version(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_of_version_with_options(request, runtime)

    async def describe_domain_names_of_version_async(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_names_of_version_with_options_async(request, runtime)

    def describe_domain_path_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainPathData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPathDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_path_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainPathData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPathDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_path_data(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_path_data_with_options(request, runtime)

    async def describe_domain_path_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_path_data_with_options_async(request, runtime)

    def describe_domain_pv_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
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
            action='DescribeDomainPvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_pv_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
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
            action='DescribeDomainPvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_pv_data(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_pv_data_with_options(request, runtime)

    async def describe_domain_pv_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_pv_data_with_options_async(request, runtime)

    def describe_domain_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
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
            action='DescribeDomainQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
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
            action='DescribeDomainQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_data(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_with_options(request, runtime)

    async def describe_domain_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_data_with_options_async(request, runtime)

    def describe_domain_qps_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_data_by_layer(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_by_layer_with_options(request, runtime)

    async def describe_domain_qps_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_real_time_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_bps_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeByteHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeByteHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_byte_hit_rate_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_byte_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_detail_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeDetailData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_detail_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeDetailData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_detail_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_domain_real_time_detail_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_domain_real_time_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
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
            action='DescribeDomainRealTimeHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
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
            action='DescribeDomainRealTimeHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_http_code_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_qps_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_domain_real_time_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_req_hit_rate_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_req_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
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
            action='DescribeDomainRealTimeSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
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
            action='DescribeDomainRealTimeSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_bps_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_src_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
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
            action='DescribeDomainRealTimeSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
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
            action='DescribeDomainRealTimeSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_http_code_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_src_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
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
            action='DescribeDomainRealTimeSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
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
            action='DescribeDomainRealTimeSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_src_traffic_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_src_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_real_time_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
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
            action='DescribeDomainRealTimeTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_real_time_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
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
            action='DescribeDomainRealTimeTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_real_time_traffic_data(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_domain_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_realtime_log_delivery(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_realtime_log_delivery_with_options(request, runtime)

    async def describe_domain_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_realtime_log_delivery_with_options_async(request, runtime)

    def describe_domain_region_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
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
            action='DescribeDomainRegionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_region_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
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
            action='DescribeDomainRegionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_region_data(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_region_data_with_options(request, runtime)

    async def describe_domain_region_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_region_data_with_options_async(request, runtime)

    def describe_domain_req_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
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
            action='DescribeDomainReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_req_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
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
            action='DescribeDomainReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_req_hit_rate_data(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_req_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_src_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
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
            action='DescribeDomainSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
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
            action='DescribeDomainSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_bps_data(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_bps_data_with_options(request, runtime)

    async def describe_domain_src_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_bps_data_with_options_async(request, runtime)

    def describe_domain_src_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
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
            action='DescribeDomainSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
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
            action='DescribeDomainSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_http_code_data(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_http_code_data_with_options(request, runtime)

    async def describe_domain_src_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_src_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
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
            action='DescribeDomainSrcQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
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
            action='DescribeDomainSrcQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_qps_data(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_qps_data_with_options(request, runtime)

    async def describe_domain_src_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_qps_data_with_options_async(request, runtime)

    def describe_domain_src_top_url_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainSrcTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_top_url_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainSrcTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_top_url_visit(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_top_url_visit_with_options(request, runtime)

    async def describe_domain_src_top_url_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_top_url_visit_with_options_async(request, runtime)

    def describe_domain_src_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
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
            action='DescribeDomainSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
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
            action='DescribeDomainSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_traffic_data(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_traffic_data_with_options(request, runtime)

    async def describe_domain_src_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_top_client_ip_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
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
            action='DescribeDomainTopClientIpVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopClientIpVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_client_ip_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
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
            action='DescribeDomainTopClientIpVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopClientIpVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_client_ip_visit(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_client_ip_visit_with_options(request, runtime)

    async def describe_domain_top_client_ip_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_client_ip_visit_with_options_async(request, runtime)

    def describe_domain_top_refer_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent):
            query['Percent'] = request.percent
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopReferVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_refer_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent):
            query['Percent'] = request.percent
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopReferVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopReferVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_refer_visit(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_refer_visit_with_options(request, runtime)

    async def describe_domain_top_refer_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_domain_top_url_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_top_url_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_top_url_visit(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_url_visit_with_options(request, runtime)

    async def describe_domain_top_url_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_url_visit_with_options_async(request, runtime)

    def describe_domain_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
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
            action='DescribeDomainTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
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
            action='DescribeDomainTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_traffic_data(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_traffic_data_with_options(request, runtime)

    async def describe_domain_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_traffic_data_with_options_async(request, runtime)

    def describe_domain_usage_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_usage_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_usage_data(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    async def describe_domain_usage_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_usage_data_with_options_async(request, runtime)

    def describe_domain_uv_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
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
            action='DescribeDomainUvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_uv_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
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
            action='DescribeDomainUvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_uv_data(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_uv_data_with_options(request, runtime)

    async def describe_domain_uv_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_uv_data_with_options_async(request, runtime)

    def describe_domains_by_source_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsBySource',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsBySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_by_source_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsBySource',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsBySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_by_source(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_by_source_with_options(request, runtime)

    async def describe_domains_by_source_async(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_by_source_with_options_async(request, runtime)

    def describe_domains_usage_by_day_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
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
            action='DescribeDomainsUsageByDay',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsUsageByDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_usage_by_day_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
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
            action='DescribeDomainsUsageByDay',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsUsageByDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_usage_by_day(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_usage_by_day_with_options(request, runtime)

    async def describe_domains_usage_by_day_async(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_usage_by_day_with_options_async(request, runtime)

    def describe_es_exception_data_with_options(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
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
            action='DescribeEsExceptionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExceptionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_es_exception_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
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
            action='DescribeEsExceptionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExceptionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_es_exception_data(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_es_exception_data_with_options(request, runtime)

    async def describe_es_exception_data_async(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_es_exception_data_with_options_async(request, runtime)

    def describe_es_execute_data_with_options(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
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
            action='DescribeEsExecuteData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExecuteDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_es_execute_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
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
            action='DescribeEsExecuteData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExecuteDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_es_execute_data(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_es_execute_data_with_options(request, runtime)

    async def describe_es_execute_data_async(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_es_execute_data_with_options_async(request, runtime)

    def describe_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fctrigger(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fctrigger_with_options(request, runtime)

    async def describe_fctrigger_async(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fctrigger_with_options_async(request, runtime)

    def describe_illegal_url_export_task_with_options(
        self,
        request: cdn_20180510_models.DescribeIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIllegalUrlExportTaskResponse:
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
            action='DescribeIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIllegalUrlExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_illegal_url_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIllegalUrlExportTaskResponse:
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
            action='DescribeIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIllegalUrlExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_illegal_url_export_task(
        self,
        request: cdn_20180510_models.DescribeIllegalUrlExportTaskRequest,
    ) -> cdn_20180510_models.DescribeIllegalUrlExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_illegal_url_export_task_with_options(request, runtime)

    async def describe_illegal_url_export_task_async(
        self,
        request: cdn_20180510_models.DescribeIllegalUrlExportTaskRequest,
    ) -> cdn_20180510_models.DescribeIllegalUrlExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_illegal_url_export_task_with_options_async(request, runtime)

    def describe_ip_info_with_options(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
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
            action='DescribeIpInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_info_with_options_async(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
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
            action='DescribeIpInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_info(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    async def describe_ip_info_async(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_info_with_options_async(request, runtime)

    def describe_l2vips_by_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
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
            action='DescribeL2VipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeL2VipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_l2vips_by_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
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
            action='DescribeL2VipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeL2VipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_l2vips_by_domain(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_l2vips_by_domain_with_options(request, runtime)

    async def describe_l2vips_by_domain_async(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_l2vips_by_domain_with_options_async(request, runtime)

    def describe_range_data_by_locate_and_isp_service_with_options(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRangeDataByLocateAndIspService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_range_data_by_locate_and_isp_service_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRangeDataByLocateAndIspService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_range_data_by_locate_and_isp_service(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_range_data_by_locate_and_isp_service_with_options(request, runtime)

    async def describe_range_data_by_locate_and_isp_service_async(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_range_data_by_locate_and_isp_service_with_options_async(request, runtime)

    def describe_realtime_delivery_acc_with_options(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRealtimeDeliveryAcc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRealtimeDeliveryAccResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_realtime_delivery_acc_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRealtimeDeliveryAcc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRealtimeDeliveryAccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_realtime_delivery_acc(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_realtime_delivery_acc_with_options(request, runtime)

    async def describe_realtime_delivery_acc_async(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_realtime_delivery_acc_with_options_async(request, runtime)

    def describe_refresh_quota_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
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
            action='DescribeRefreshQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_quota_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
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
            action='DescribeRefreshQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_quota(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_quota_with_options(request, runtime)

    async def describe_refresh_quota_async(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_quota_with_options_async(request, runtime)

    def describe_refresh_task_by_id_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
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
            action='DescribeRefreshTaskById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_task_by_id_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
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
            action='DescribeRefreshTaskById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTaskByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_task_by_id(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_task_by_id_with_options(request, runtime)

    async def describe_refresh_task_by_id_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_task_by_id_with_options_async(request, runtime)

    def describe_refresh_tasks_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeRefreshTasks',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_tasks_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeRefreshTasks',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_tasks(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_tasks_with_options(request, runtime)

    async def describe_refresh_tasks_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_tasks_with_options_async(request, runtime)

    def describe_staging_ip_with_options(
        self,
        request: cdn_20180510_models.DescribeStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStagingIp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_staging_ip_with_options_async(
        self,
        request: cdn_20180510_models.DescribeStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStagingIp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeStagingIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_staging_ip(
        self,
        request: cdn_20180510_models.DescribeStagingIpRequest,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_staging_ip_with_options(request, runtime)

    async def describe_staging_ip_async(
        self,
        request: cdn_20180510_models.DescribeStagingIpRequest,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_staging_ip_with_options_async(request, runtime)

    def describe_tag_resources_with_options(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
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
            action='DescribeTagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
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
            action='DescribeTagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_resources(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_top_domains_by_flow_with_options(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
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
            action='DescribeTopDomainsByFlow',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_domains_by_flow_with_options_async(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
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
            action='DescribeTopDomainsByFlow',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_domains_by_flow(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_domains_by_flow_with_options(request, runtime)

    async def describe_top_domains_by_flow_async(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_domains_by_flow_with_options_async(request, runtime)

    def describe_user_certificate_expire_count_with_options(
        self,
        request: cdn_20180510_models.DescribeUserCertificateExpireCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserCertificateExpireCount',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserCertificateExpireCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_certificate_expire_count_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserCertificateExpireCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserCertificateExpireCount',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserCertificateExpireCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_certificate_expire_count(
        self,
        request: cdn_20180510_models.DescribeUserCertificateExpireCountRequest,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_certificate_expire_count_with_options(request, runtime)

    async def describe_user_certificate_expire_count_async(
        self,
        request: cdn_20180510_models.DescribeUserCertificateExpireCountRequest,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_certificate_expire_count_with_options_async(request, runtime)

    def describe_user_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_configs(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_configs_with_options(request, runtime)

    async def describe_user_configs_async(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_configs_with_options_async(request, runtime)

    def describe_user_domains_with_options(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_domains_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_domains(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_domains_with_options(request, runtime)

    async def describe_user_domains_async(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_domains_with_options_async(request, runtime)

    def describe_user_tags_with_options(
        self,
        request: cdn_20180510_models.DescribeUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserTags',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_tags_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserTags',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_tags(
        self,
        request: cdn_20180510_models.DescribeUserTagsRequest,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_tags_with_options(request, runtime)

    async def describe_user_tags_async(
        self,
        request: cdn_20180510_models.DescribeUserTagsRequest,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_tags_with_options_async(request, runtime)

    def describe_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
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
            action='DescribeUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
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
            action='DescribeUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_usage_data_export_task(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_data_export_task_with_options(request, runtime)

    async def describe_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_user_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
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
            action='DescribeUserUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
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
            action='DescribeUserUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_usage_detail_data_export_task(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_detail_data_export_task_with_options(request, runtime)

    async def describe_user_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_usage_detail_data_export_task_with_options_async(request, runtime)

    def describe_user_vips_by_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserVipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserVipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_vips_by_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserVipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserVipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_vips_by_domain(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_vips_by_domain_with_options(request, runtime)

    async def describe_user_vips_by_domain_async(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_vips_by_domain_with_options_async(request, runtime)

    def describe_verify_content_with_options(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
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
            action='DescribeVerifyContent',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_content_with_options_async(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
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
            action='DescribeVerifyContent',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_content(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_content_with_options(request, runtime)

    async def describe_verify_content_async(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_content_with_options_async(request, runtime)

    def disable_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DisableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DisableRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_realtime_log_delivery(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_realtime_log_delivery_with_options(request, runtime)

    async def disable_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_realtime_log_delivery_with_options_async(request, runtime)

    def enable_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.EnableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.EnableRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_realtime_log_delivery(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_realtime_log_delivery_with_options(request, runtime)

    async def enable_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_realtime_log_delivery_with_options_async(request, runtime)

    def list_domains_by_log_config_id_with_options(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainsByLogConfigId',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListDomainsByLogConfigIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_by_log_config_id_with_options_async(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainsByLogConfigId',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListDomainsByLogConfigIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains_by_log_config_id(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_domains_by_log_config_id_with_options(request, runtime)

    async def list_domains_by_log_config_id_async(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_domains_by_log_config_id_with_options_async(request, runtime)

    def list_fctrigger_with_options(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fctrigger(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fctrigger_with_options(request, runtime)

    async def list_fctrigger_async(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fctrigger_with_options_async(request, runtime)

    def list_realtime_log_delivery_domains_with_options(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_log_delivery_domains_with_options_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_log_delivery_domains(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_domains_with_options(request, runtime)

    async def list_realtime_log_delivery_domains_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_log_delivery_domains_with_options_async(request, runtime)

    def list_realtime_log_delivery_infos_with_options(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryInfos',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_realtime_log_delivery_infos_with_options_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryInfos',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_realtime_log_delivery_infos(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryInfosRequest,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_infos_with_options(request, runtime)

    async def list_realtime_log_delivery_infos_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryInfosRequest,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_log_delivery_infos_with_options_async(request, runtime)

    def list_user_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.ListUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListUserCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ListUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListUserCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_custom_log_config(
        self,
        request: cdn_20180510_models.ListUserCustomLogConfigRequest,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_custom_log_config_with_options(request, runtime)

    async def list_user_custom_log_config_async(
        self,
        request: cdn_20180510_models.ListUserCustomLogConfigRequest,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_custom_log_config_with_options_async(request, runtime)

    def modify_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
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
            action='ModifyCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
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
            action='ModifyCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_with_options(request, runtime)

    async def modify_cdn_domain_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_domain_with_options_async(request, runtime)

    def modify_cdn_domain_schdm_by_property_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
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
            action='ModifyCdnDomainSchdmByProperty',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_schdm_by_property_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
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
            action='ModifyCdnDomainSchdmByProperty',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain_schdm_by_property(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_cdn_domain_schdm_by_property_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_domain_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyDomainCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyDomainCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_custom_log_config(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_custom_log_config_with_options(request, runtime)

    async def modify_domain_custom_log_config_async(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_custom_log_config_with_options_async(request, runtime)

    def modify_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_realtime_log_delivery(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_realtime_log_delivery_with_options(request, runtime)

    async def modify_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_realtime_log_delivery_with_options_async(request, runtime)

    def modify_user_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.ModifyUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyUserCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ModifyUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyUserCustomLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_custom_log_config(
        self,
        request: cdn_20180510_models.ModifyUserCustomLogConfigRequest,
    ) -> cdn_20180510_models.ModifyUserCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_custom_log_config_with_options(request, runtime)

    async def modify_user_custom_log_config_async(
        self,
        request: cdn_20180510_models.ModifyUserCustomLogConfigRequest,
    ) -> cdn_20180510_models.ModifyUserCustomLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_custom_log_config_with_options_async(request, runtime)

    def open_cdn_service_with_options(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.OpenCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdn_service_with_options_async(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.OpenCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdn_service(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cdn_service_with_options(request, runtime)

    async def open_cdn_service_async(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cdn_service_with_options_async(request, runtime)

    def publish_staging_config_to_production_with_options(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
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
            action='PublishStagingConfigToProduction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PublishStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_staging_config_to_production_with_options_async(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
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
            action='PublishStagingConfigToProduction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PublishStagingConfigToProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_staging_config_to_production(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_staging_config_to_production_with_options(request, runtime)

    async def publish_staging_config_to_production_async(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_staging_config_to_production_with_options_async(request, runtime)

    def push_object_cache_with_options(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
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
            action='PushObjectCache',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PushObjectCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_object_cache_with_options_async(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
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
            action='PushObjectCache',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PushObjectCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_object_cache(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_object_cache_with_options(request, runtime)

    async def push_object_cache_async(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_object_cache_with_options_async(request, runtime)

    def refresh_object_caches_with_options(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
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
            action='RefreshObjectCaches',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RefreshObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_object_caches_with_options_async(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
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
            action='RefreshObjectCaches',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RefreshObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_object_caches(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_object_caches_with_options(request, runtime)

    async def refresh_object_caches_async(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_object_caches_with_options_async(request, runtime)

    def rollback_staging_config_with_options(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
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
            action='RollbackStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RollbackStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
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
            action='RollbackStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RollbackStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_staging_config(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_staging_config_with_options(request, runtime)

    async def rollback_staging_config_async(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_staging_config_with_options_async(request, runtime)

    def set_cc_config_with_options(
        self,
        request: cdn_20180510_models.SetCcConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCcConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
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
            action='SetCcConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCcConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cc_config_with_options_async(
        self,
        request: cdn_20180510_models.SetCcConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCcConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
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
            action='SetCcConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCcConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cc_config(
        self,
        request: cdn_20180510_models.SetCcConfigRequest,
    ) -> cdn_20180510_models.SetCcConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cc_config_with_options(request, runtime)

    async def set_cc_config_async(
        self,
        request: cdn_20180510_models.SetCcConfigRequest,
    ) -> cdn_20180510_models.SetCcConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cc_config_with_options_async(request, runtime)

    def set_cdn_domain_csrcertificate_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
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
            action='SetCdnDomainCSRCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_csrcertificate_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
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
            action='SetCdnDomainCSRCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainCSRCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_csrcertificate(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_csrcertificate_with_options(request, runtime)

    async def set_cdn_domain_csrcertificate_async(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_cdn_domain_smcertificate_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
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
            action='SetCdnDomainSMCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_smcertificate_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
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
            action='SetCdnDomainSMCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainSMCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_smcertificate(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_smcertificate_with_options(request, runtime)

    async def set_cdn_domain_smcertificate_async(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_smcertificate_with_options_async(request, runtime)

    def set_cdn_domain_staging_config_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
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
            action='SetCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
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
            action='SetCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_staging_config(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_staging_config_with_options(request, runtime)

    async def set_cdn_domain_staging_config_async(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_staging_config_with_options_async(request, runtime)

    def set_config_of_version_with_options(
        self,
        request: cdn_20180510_models.SetConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_matches):
            query['FunctionMatches'] = request.function_matches
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
            action='SetConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_config_of_version_with_options_async(
        self,
        request: cdn_20180510_models.SetConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetConfigOfVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_matches):
            query['FunctionMatches'] = request.function_matches
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
            action='SetConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetConfigOfVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_config_of_version(
        self,
        request: cdn_20180510_models.SetConfigOfVersionRequest,
    ) -> cdn_20180510_models.SetConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_config_of_version_with_options(request, runtime)

    async def set_config_of_version_async(
        self,
        request: cdn_20180510_models.SetConfigOfVersionRequest,
    ) -> cdn_20180510_models.SetConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_config_of_version_with_options_async(request, runtime)

    def set_domain_green_manager_config_with_options(
        self,
        request: cdn_20180510_models.SetDomainGreenManagerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainGreenManagerConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainGreenManagerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_green_manager_config_with_options_async(
        self,
        request: cdn_20180510_models.SetDomainGreenManagerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainGreenManagerConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainGreenManagerConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_green_manager_config(
        self,
        request: cdn_20180510_models.SetDomainGreenManagerConfigRequest,
    ) -> cdn_20180510_models.SetDomainGreenManagerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_green_manager_config_with_options(request, runtime)

    async def set_domain_green_manager_config_async(
        self,
        request: cdn_20180510_models.SetDomainGreenManagerConfigRequest,
    ) -> cdn_20180510_models.SetDomainGreenManagerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_green_manager_config_with_options_async(request, runtime)

    def set_domain_server_certificate_with_options(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
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
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_status):
            query['ServerCertificateStatus'] = request.server_certificate_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_server_certificate_with_options_async(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
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
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_status):
            query['ServerCertificateStatus'] = request.server_certificate_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_server_certificate(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_server_certificate_with_options(request, runtime)

    async def set_domain_server_certificate_async(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_server_certificate_with_options_async(request, runtime)

    def set_error_page_config_with_options(
        self,
        request: cdn_20180510_models.SetErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetErrorPageConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_url):
            query['CustomPageUrl'] = request.custom_page_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_type):
            query['PageType'] = request.page_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetErrorPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_error_page_config_with_options_async(
        self,
        request: cdn_20180510_models.SetErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetErrorPageConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_url):
            query['CustomPageUrl'] = request.custom_page_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_type):
            query['PageType'] = request.page_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetErrorPageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_error_page_config(
        self,
        request: cdn_20180510_models.SetErrorPageConfigRequest,
    ) -> cdn_20180510_models.SetErrorPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_error_page_config_with_options(request, runtime)

    async def set_error_page_config_async(
        self,
        request: cdn_20180510_models.SetErrorPageConfigRequest,
    ) -> cdn_20180510_models.SetErrorPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_error_page_config_with_options_async(request, runtime)

    def set_file_cache_expired_config_with_options(
        self,
        request: cdn_20180510_models.SetFileCacheExpiredConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetFileCacheExpiredConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_content):
            query['CacheContent'] = request.cache_content
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFileCacheExpiredConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetFileCacheExpiredConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_file_cache_expired_config_with_options_async(
        self,
        request: cdn_20180510_models.SetFileCacheExpiredConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetFileCacheExpiredConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_content):
            query['CacheContent'] = request.cache_content
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFileCacheExpiredConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetFileCacheExpiredConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_file_cache_expired_config(
        self,
        request: cdn_20180510_models.SetFileCacheExpiredConfigRequest,
    ) -> cdn_20180510_models.SetFileCacheExpiredConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_file_cache_expired_config_with_options(request, runtime)

    async def set_file_cache_expired_config_async(
        self,
        request: cdn_20180510_models.SetFileCacheExpiredConfigRequest,
    ) -> cdn_20180510_models.SetFileCacheExpiredConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_file_cache_expired_config_with_options_async(request, runtime)

    def set_force_redirect_config_with_options(
        self,
        request: cdn_20180510_models.SetForceRedirectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForceRedirectConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.redirect_type):
            query['RedirectType'] = request.redirect_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForceRedirectConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForceRedirectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_force_redirect_config_with_options_async(
        self,
        request: cdn_20180510_models.SetForceRedirectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForceRedirectConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.redirect_type):
            query['RedirectType'] = request.redirect_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForceRedirectConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForceRedirectConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_force_redirect_config(
        self,
        request: cdn_20180510_models.SetForceRedirectConfigRequest,
    ) -> cdn_20180510_models.SetForceRedirectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_force_redirect_config_with_options(request, runtime)

    async def set_force_redirect_config_async(
        self,
        request: cdn_20180510_models.SetForceRedirectConfigRequest,
    ) -> cdn_20180510_models.SetForceRedirectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_force_redirect_config_with_options_async(request, runtime)

    def set_forward_scheme_config_with_options(
        self,
        request: cdn_20180510_models.SetForwardSchemeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForwardSchemeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scheme_origin):
            query['SchemeOrigin'] = request.scheme_origin
        if not UtilClient.is_unset(request.scheme_origin_port):
            query['SchemeOriginPort'] = request.scheme_origin_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForwardSchemeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForwardSchemeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_forward_scheme_config_with_options_async(
        self,
        request: cdn_20180510_models.SetForwardSchemeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForwardSchemeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scheme_origin):
            query['SchemeOrigin'] = request.scheme_origin
        if not UtilClient.is_unset(request.scheme_origin_port):
            query['SchemeOriginPort'] = request.scheme_origin_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForwardSchemeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForwardSchemeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_forward_scheme_config(
        self,
        request: cdn_20180510_models.SetForwardSchemeConfigRequest,
    ) -> cdn_20180510_models.SetForwardSchemeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_forward_scheme_config_with_options(request, runtime)

    async def set_forward_scheme_config_async(
        self,
        request: cdn_20180510_models.SetForwardSchemeConfigRequest,
    ) -> cdn_20180510_models.SetForwardSchemeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_forward_scheme_config_with_options_async(request, runtime)

    def set_http_error_page_config_with_options(
        self,
        request: cdn_20180510_models.SetHttpErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpErrorPageConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_url):
            query['PageUrl'] = request.page_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpErrorPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_http_error_page_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpErrorPageConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_url):
            query['PageUrl'] = request.page_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpErrorPageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_http_error_page_config(
        self,
        request: cdn_20180510_models.SetHttpErrorPageConfigRequest,
    ) -> cdn_20180510_models.SetHttpErrorPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_http_error_page_config_with_options(request, runtime)

    async def set_http_error_page_config_async(
        self,
        request: cdn_20180510_models.SetHttpErrorPageConfigRequest,
    ) -> cdn_20180510_models.SetHttpErrorPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_http_error_page_config_with_options_async(request, runtime)

    def set_http_header_config_with_options(
        self,
        request: cdn_20180510_models.SetHttpHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpHeaderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.header_key):
            query['HeaderKey'] = request.header_key
        if not UtilClient.is_unset(request.header_value):
            query['HeaderValue'] = request.header_value
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpHeaderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_http_header_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpHeaderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.header_key):
            query['HeaderKey'] = request.header_key
        if not UtilClient.is_unset(request.header_value):
            query['HeaderValue'] = request.header_value
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpHeaderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_http_header_config(
        self,
        request: cdn_20180510_models.SetHttpHeaderConfigRequest,
    ) -> cdn_20180510_models.SetHttpHeaderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_http_header_config_with_options(request, runtime)

    async def set_http_header_config_async(
        self,
        request: cdn_20180510_models.SetHttpHeaderConfigRequest,
    ) -> cdn_20180510_models.SetHttpHeaderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_http_header_config_with_options_async(request, runtime)

    def set_https_option_config_with_options(
        self,
        request: cdn_20180510_models.SetHttpsOptionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpsOptionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_2):
            query['Http2'] = request.http_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpsOptionConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpsOptionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_https_option_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpsOptionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpsOptionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_2):
            query['Http2'] = request.http_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpsOptionConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpsOptionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_https_option_config(
        self,
        request: cdn_20180510_models.SetHttpsOptionConfigRequest,
    ) -> cdn_20180510_models.SetHttpsOptionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_https_option_config_with_options(request, runtime)

    async def set_https_option_config_async(
        self,
        request: cdn_20180510_models.SetHttpsOptionConfigRequest,
    ) -> cdn_20180510_models.SetHttpsOptionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_https_option_config_with_options_async(request, runtime)

    def set_ignore_query_string_config_with_options(
        self,
        request: cdn_20180510_models.SetIgnoreQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIgnoreQueryStringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.hash_key_args):
            query['HashKeyArgs'] = request.hash_key_args
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIgnoreQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIgnoreQueryStringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ignore_query_string_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIgnoreQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIgnoreQueryStringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.hash_key_args):
            query['HashKeyArgs'] = request.hash_key_args
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIgnoreQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIgnoreQueryStringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ignore_query_string_config(
        self,
        request: cdn_20180510_models.SetIgnoreQueryStringConfigRequest,
    ) -> cdn_20180510_models.SetIgnoreQueryStringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ignore_query_string_config_with_options(request, runtime)

    async def set_ignore_query_string_config_async(
        self,
        request: cdn_20180510_models.SetIgnoreQueryStringConfigRequest,
    ) -> cdn_20180510_models.SetIgnoreQueryStringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ignore_query_string_config_with_options_async(request, runtime)

    def set_ip_allow_list_config_with_options(
        self,
        request: cdn_20180510_models.SetIpAllowListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpAllowListConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
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
            action='SetIpAllowListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpAllowListConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ip_allow_list_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIpAllowListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpAllowListConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
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
            action='SetIpAllowListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpAllowListConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ip_allow_list_config(
        self,
        request: cdn_20180510_models.SetIpAllowListConfigRequest,
    ) -> cdn_20180510_models.SetIpAllowListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ip_allow_list_config_with_options(request, runtime)

    async def set_ip_allow_list_config_async(
        self,
        request: cdn_20180510_models.SetIpAllowListConfigRequest,
    ) -> cdn_20180510_models.SetIpAllowListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ip_allow_list_config_with_options_async(request, runtime)

    def set_ip_black_list_config_with_options(
        self,
        request: cdn_20180510_models.SetIpBlackListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpBlackListConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpBlackListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpBlackListConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ip_black_list_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIpBlackListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpBlackListConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpBlackListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpBlackListConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ip_black_list_config(
        self,
        request: cdn_20180510_models.SetIpBlackListConfigRequest,
    ) -> cdn_20180510_models.SetIpBlackListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ip_black_list_config_with_options(request, runtime)

    async def set_ip_black_list_config_async(
        self,
        request: cdn_20180510_models.SetIpBlackListConfigRequest,
    ) -> cdn_20180510_models.SetIpBlackListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ip_black_list_config_with_options_async(request, runtime)

    def set_optimize_config_with_options(
        self,
        request: cdn_20180510_models.SetOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetOptimizeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOptimizeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_optimize_config_with_options_async(
        self,
        request: cdn_20180510_models.SetOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetOptimizeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOptimizeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetOptimizeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_optimize_config(
        self,
        request: cdn_20180510_models.SetOptimizeConfigRequest,
    ) -> cdn_20180510_models.SetOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_optimize_config_with_options(request, runtime)

    async def set_optimize_config_async(
        self,
        request: cdn_20180510_models.SetOptimizeConfigRequest,
    ) -> cdn_20180510_models.SetOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_optimize_config_with_options_async(request, runtime)

    def set_page_compress_config_with_options(
        self,
        request: cdn_20180510_models.SetPageCompressConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetPageCompressConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPageCompressConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetPageCompressConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_page_compress_config_with_options_async(
        self,
        request: cdn_20180510_models.SetPageCompressConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetPageCompressConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPageCompressConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetPageCompressConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_page_compress_config(
        self,
        request: cdn_20180510_models.SetPageCompressConfigRequest,
    ) -> cdn_20180510_models.SetPageCompressConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_page_compress_config_with_options(request, runtime)

    async def set_page_compress_config_async(
        self,
        request: cdn_20180510_models.SetPageCompressConfigRequest,
    ) -> cdn_20180510_models.SetPageCompressConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_page_compress_config_with_options_async(request, runtime)

    def set_range_config_with_options(
        self,
        request: cdn_20180510_models.SetRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRangeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRangeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRangeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_range_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRangeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRangeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRangeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_range_config(
        self,
        request: cdn_20180510_models.SetRangeConfigRequest,
    ) -> cdn_20180510_models.SetRangeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_range_config_with_options(request, runtime)

    async def set_range_config_async(
        self,
        request: cdn_20180510_models.SetRangeConfigRequest,
    ) -> cdn_20180510_models.SetRangeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_range_config_with_options_async(request, runtime)

    def set_referer_config_with_options(
        self,
        request: cdn_20180510_models.SetRefererConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRefererConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_empty):
            query['AllowEmpty'] = request.allow_empty
        if not UtilClient.is_unset(request.disable_ast):
            query['DisableAst'] = request.disable_ast
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.refer_list):
            query['ReferList'] = request.refer_list
        if not UtilClient.is_unset(request.refer_type):
            query['ReferType'] = request.refer_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRefererConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRefererConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_referer_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRefererConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRefererConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_empty):
            query['AllowEmpty'] = request.allow_empty
        if not UtilClient.is_unset(request.disable_ast):
            query['DisableAst'] = request.disable_ast
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.refer_list):
            query['ReferList'] = request.refer_list
        if not UtilClient.is_unset(request.refer_type):
            query['ReferType'] = request.refer_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRefererConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRefererConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_referer_config(
        self,
        request: cdn_20180510_models.SetRefererConfigRequest,
    ) -> cdn_20180510_models.SetRefererConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_referer_config_with_options(request, runtime)

    async def set_referer_config_async(
        self,
        request: cdn_20180510_models.SetRefererConfigRequest,
    ) -> cdn_20180510_models.SetRefererConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_referer_config_with_options_async(request, runtime)

    def set_remove_query_string_config_with_options(
        self,
        request: cdn_20180510_models.SetRemoveQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRemoveQueryStringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_remove_args):
            query['AliRemoveArgs'] = request.ali_remove_args
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRemoveQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRemoveQueryStringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_remove_query_string_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRemoveQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRemoveQueryStringConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_remove_args):
            query['AliRemoveArgs'] = request.ali_remove_args
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRemoveQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRemoveQueryStringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_remove_query_string_config(
        self,
        request: cdn_20180510_models.SetRemoveQueryStringConfigRequest,
    ) -> cdn_20180510_models.SetRemoveQueryStringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_remove_query_string_config_with_options(request, runtime)

    async def set_remove_query_string_config_async(
        self,
        request: cdn_20180510_models.SetRemoveQueryStringConfigRequest,
    ) -> cdn_20180510_models.SetRemoveQueryStringConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_remove_query_string_config_with_options_async(request, runtime)

    def set_req_auth_config_with_options(
        self,
        request: cdn_20180510_models.SetReqAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqAuthConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_remote_desc):
            query['AuthRemoteDesc'] = request.auth_remote_desc
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_1):
            query['Key1'] = request.key_1
        if not UtilClient.is_unset(request.key_2):
            query['Key2'] = request.key_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time_out):
            query['TimeOut'] = request.time_out
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqAuthConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_req_auth_config_with_options_async(
        self,
        request: cdn_20180510_models.SetReqAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqAuthConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_remote_desc):
            query['AuthRemoteDesc'] = request.auth_remote_desc
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_1):
            query['Key1'] = request.key_1
        if not UtilClient.is_unset(request.key_2):
            query['Key2'] = request.key_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time_out):
            query['TimeOut'] = request.time_out
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqAuthConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_req_auth_config(
        self,
        request: cdn_20180510_models.SetReqAuthConfigRequest,
    ) -> cdn_20180510_models.SetReqAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_req_auth_config_with_options(request, runtime)

    async def set_req_auth_config_async(
        self,
        request: cdn_20180510_models.SetReqAuthConfigRequest,
    ) -> cdn_20180510_models.SetReqAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_req_auth_config_with_options_async(request, runtime)

    def set_req_header_config_with_options(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqHeaderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_req_header_config_with_options_async(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqHeaderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_req_header_config(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_req_header_config_with_options(request, runtime)

    async def set_req_header_config_async(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_req_header_config_with_options_async(request, runtime)

    def set_source_host_config_with_options(
        self,
        request: cdn_20180510_models.SetSourceHostConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetSourceHostConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.back_src_domain):
            query['BackSrcDomain'] = request.back_src_domain
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSourceHostConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetSourceHostConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_source_host_config_with_options_async(
        self,
        request: cdn_20180510_models.SetSourceHostConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetSourceHostConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.back_src_domain):
            query['BackSrcDomain'] = request.back_src_domain
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSourceHostConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetSourceHostConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_source_host_config(
        self,
        request: cdn_20180510_models.SetSourceHostConfigRequest,
    ) -> cdn_20180510_models.SetSourceHostConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_source_host_config_with_options(request, runtime)

    async def set_source_host_config_async(
        self,
        request: cdn_20180510_models.SetSourceHostConfigRequest,
    ) -> cdn_20180510_models.SetSourceHostConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_source_host_config_with_options_async(request, runtime)

    def set_user_green_manager_config_with_options(
        self,
        request: cdn_20180510_models.SetUserGreenManagerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetUserGreenManagerConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        if not UtilClient.is_unset(request.ratio):
            query['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetUserGreenManagerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_green_manager_config_with_options_async(
        self,
        request: cdn_20180510_models.SetUserGreenManagerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetUserGreenManagerConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        if not UtilClient.is_unset(request.ratio):
            query['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetUserGreenManagerConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_green_manager_config(
        self,
        request: cdn_20180510_models.SetUserGreenManagerConfigRequest,
    ) -> cdn_20180510_models.SetUserGreenManagerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_user_green_manager_config_with_options(request, runtime)

    async def set_user_green_manager_config_async(
        self,
        request: cdn_20180510_models.SetUserGreenManagerConfigRequest,
    ) -> cdn_20180510_models.SetUserGreenManagerConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_user_green_manager_config_with_options_async(request, runtime)

    def set_waiting_room_config_with_options(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_pct):
            query['AllowPct'] = request.allow_pct
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.gap_time):
            query['GapTime'] = request.gap_time
        if not UtilClient.is_unset(request.max_time_wait):
            query['MaxTimeWait'] = request.max_time_wait
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.wait_uri):
            query['WaitUri'] = request.wait_uri
        if not UtilClient.is_unset(request.wait_url):
            query['WaitUrl'] = request.wait_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWaitingRoomConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetWaitingRoomConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_waiting_room_config_with_options_async(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_pct):
            query['AllowPct'] = request.allow_pct
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.gap_time):
            query['GapTime'] = request.gap_time
        if not UtilClient.is_unset(request.max_time_wait):
            query['MaxTimeWait'] = request.max_time_wait
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.wait_uri):
            query['WaitUri'] = request.wait_uri
        if not UtilClient.is_unset(request.wait_url):
            query['WaitUrl'] = request.wait_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWaitingRoomConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetWaitingRoomConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_waiting_room_config(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_waiting_room_config_with_options(request, runtime)

    async def set_waiting_room_config_async(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_waiting_room_config_with_options_async(request, runtime)

    def start_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
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
            action='StartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
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
            action='StartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StartCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cdn_domain(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_cdn_domain_with_options(request, runtime)

    async def start_cdn_domain_async(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_cdn_domain_with_options_async(request, runtime)

    def stop_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
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
            action='StopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
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
            action='StopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StopCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cdn_domain(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_cdn_domain_with_options(request, runtime)

    async def stop_cdn_domain_async(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_cdn_domain_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.TagResourcesResponse:
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
            action='TagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.TagResourcesResponse:
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
            action='TagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
    ) -> cdn_20180510_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
    ) -> cdn_20180510_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UntagResourcesResponse:
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
            action='UntagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UntagResourcesResponse:
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
            action='UntagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
    ) -> cdn_20180510_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
    ) -> cdn_20180510_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
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
            action='UpdateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cdn_deliver_task_with_options_async(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
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
            action='UpdateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnDeliverTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cdn_deliver_task(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_deliver_task_with_options(request, runtime)

    async def update_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cdn_deliver_task_with_options_async(request, runtime)

    def update_cdn_sub_task_with_options(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
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
            action='UpdateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cdn_sub_task_with_options_async(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
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
            action='UpdateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cdn_sub_task(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_sub_task_with_options(request, runtime)

    async def update_cdn_sub_task_async(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cdn_sub_task_with_options_async(request, runtime)

    def update_fctrigger_with_options(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateFCTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_fctrigger(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_fctrigger_with_options(request, runtime)

    async def update_fctrigger_async(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_fctrigger_with_options_async(request, runtime)

    def verify_domain_owner_with_options(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
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
            action='VerifyDomainOwner',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_domain_owner_with_options_async(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
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
            action='VerifyDomainOwner',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.VerifyDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_domain_owner(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    async def verify_domain_owner_async(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_domain_owner_with_options_async(request, runtime)
