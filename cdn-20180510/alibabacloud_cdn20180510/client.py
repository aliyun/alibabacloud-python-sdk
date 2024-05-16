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
        """
        @summary Adds a domain name to accelerate.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        The domain name that you want to add has a valid Internet Content Provider (ICP) number.
        You can add only one domain name to Alibaba Cloud CDN in each call. Each Alibaba Cloud account can add a maximum of 50 domain names to Alibaba Cloud CDN.
        If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review will be completed by the end of the next business day after you submit the application.
        You can call this operation up to 30 times per second per account.
        
        @param request: AddCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCdnDomainResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Adds a domain name to accelerate.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        The domain name that you want to add has a valid Internet Content Provider (ICP) number.
        You can add only one domain name to Alibaba Cloud CDN in each call. Each Alibaba Cloud account can add a maximum of 50 domain names to Alibaba Cloud CDN.
        If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review will be completed by the end of the next business day after you submit the application.
        You can call this operation up to 30 times per second per account.
        
        @param request: AddCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCdnDomainResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Adds a domain name to accelerate.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        The domain name that you want to add has a valid Internet Content Provider (ICP) number.
        You can add only one domain name to Alibaba Cloud CDN in each call. Each Alibaba Cloud account can add a maximum of 50 domain names to Alibaba Cloud CDN.
        If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review will be completed by the end of the next business day after you submit the application.
        You can call this operation up to 30 times per second per account.
        
        @param request: AddCdnDomainRequest
        @return: AddCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_cdn_domain_with_options(request, runtime)

    async def add_cdn_domain_async(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        """
        @summary Adds a domain name to accelerate.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        The domain name that you want to add has a valid Internet Content Provider (ICP) number.
        You can add only one domain name to Alibaba Cloud CDN in each call. Each Alibaba Cloud account can add a maximum of 50 domain names to Alibaba Cloud CDN.
        If the content of the origin server is not stored on Alibaba Cloud, the content must be reviewed. The review will be completed by the end of the next business day after you submit the application.
        You can call this operation up to 30 times per second per account.
        
        @param request: AddCdnDomainRequest
        @return: AddCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_cdn_domain_with_options_async(request, runtime)

    def add_fctrigger_with_options(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        """
        @summary Adds a Function Compute trigger.
        
        @param request: AddFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Adds a Function Compute trigger.
        
        @param request: AddFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Adds a Function Compute trigger.
        
        @param request: AddFCTriggerRequest
        @return: AddFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_fctrigger_with_options(request, runtime)

    async def add_fctrigger_async(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        """
        @summary Adds a Function Compute trigger.
        
        @param request: AddFCTriggerRequest
        @return: AddFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_fctrigger_with_options_async(request, runtime)

    def batch_add_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        """
        @summary Adds one or more domain names to Alibaba Cloud CDN. You can add a maximum of 50 domain names at a time.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        If the acceleration region is Chinese Mainland Only or Global, you must apply for an ICP filing for the domain name.
        You can specify multiple domain names and separate them with commas (,). You can specify at most 50 domain names in each call.
        For more information, see [Add a domain name](https://help.aliyun.com/document_detail/122181.html).
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddCdnDomainResponse
        """
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
        """
        @summary Adds one or more domain names to Alibaba Cloud CDN. You can add a maximum of 50 domain names at a time.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        If the acceleration region is Chinese Mainland Only or Global, you must apply for an ICP filing for the domain name.
        You can specify multiple domain names and separate them with commas (,). You can specify at most 50 domain names in each call.
        For more information, see [Add a domain name](https://help.aliyun.com/document_detail/122181.html).
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddCdnDomainResponse
        """
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
        """
        @summary Adds one or more domain names to Alibaba Cloud CDN. You can add a maximum of 50 domain names at a time.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        If the acceleration region is Chinese Mainland Only or Global, you must apply for an ICP filing for the domain name.
        You can specify multiple domain names and separate them with commas (,). You can specify at most 50 domain names in each call.
        For more information, see [Add a domain name](https://help.aliyun.com/document_detail/122181.html).
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddCdnDomainRequest
        @return: BatchAddCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_add_cdn_domain_with_options(request, runtime)

    async def batch_add_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        """
        @summary Adds one or more domain names to Alibaba Cloud CDN. You can add a maximum of 50 domain names at a time.
        
        @description    You must activate Alibaba Cloud CDN before you can add a domain name to it. For more information, see [Activate Alibaba Cloud CDN](https://help.aliyun.com/document_detail/27272.html).
        If the acceleration region is Chinese Mainland Only or Global, you must apply for an ICP filing for the domain name.
        You can specify multiple domain names and separate them with commas (,). You can specify at most 50 domain names in each call.
        For more information, see [Add a domain name](https://help.aliyun.com/document_detail/122181.html).
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchAddCdnDomainRequest
        @return: BatchAddCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_cdn_domain_with_options_async(request, runtime)

    def batch_delete_cdn_domain_config_with_options(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
        """
        @summary Deletes configurations of multiple accelerated domain names at a time.
        
        @description    You can specify up to 50 domain names in each request.
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteCdnDomainConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteCdnDomainConfigResponse
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
        """
        @summary Deletes configurations of multiple accelerated domain names at a time.
        
        @description    You can specify up to 50 domain names in each request.
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteCdnDomainConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteCdnDomainConfigResponse
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
        """
        @summary Deletes configurations of multiple accelerated domain names at a time.
        
        @description    You can specify up to 50 domain names in each request.
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteCdnDomainConfigRequest
        @return: BatchDeleteCdnDomainConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_cdn_domain_config_with_options(request, runtime)

    async def batch_delete_cdn_domain_config_async(
        self,
        request: cdn_20180510_models.BatchDeleteCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchDeleteCdnDomainConfigResponse:
        """
        @summary Deletes configurations of multiple accelerated domain names at a time.
        
        @description    You can specify up to 50 domain names in each request.
        You can call this operation up to 30 times per second per account.
        
        @param request: BatchDeleteCdnDomainConfigRequest
        @return: BatchDeleteCdnDomainConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_cdn_domain_config_with_options_async(request, runtime)

    def batch_describe_cdn_ip_info_with_options(
        self,
        request: cdn_20180510_models.BatchDescribeCdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchDescribeCdnIpInfoResponse:
        """
        @summary Queries whether one or more IP addresses are assigned to Alibaba Cloud CDN.
        
        @description >The maximum number of times that each user can call this operation per second is 20.
        
        @param request: BatchDescribeCdnIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDescribeCdnIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDescribeCdnIpInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchDescribeCdnIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_describe_cdn_ip_info_with_options_async(
        self,
        request: cdn_20180510_models.BatchDescribeCdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchDescribeCdnIpInfoResponse:
        """
        @summary Queries whether one or more IP addresses are assigned to Alibaba Cloud CDN.
        
        @description >The maximum number of times that each user can call this operation per second is 20.
        
        @param request: BatchDescribeCdnIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDescribeCdnIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDescribeCdnIpInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchDescribeCdnIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_describe_cdn_ip_info(
        self,
        request: cdn_20180510_models.BatchDescribeCdnIpInfoRequest,
    ) -> cdn_20180510_models.BatchDescribeCdnIpInfoResponse:
        """
        @summary Queries whether one or more IP addresses are assigned to Alibaba Cloud CDN.
        
        @description >The maximum number of times that each user can call this operation per second is 20.
        
        @param request: BatchDescribeCdnIpInfoRequest
        @return: BatchDescribeCdnIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_describe_cdn_ip_info_with_options(request, runtime)

    async def batch_describe_cdn_ip_info_async(
        self,
        request: cdn_20180510_models.BatchDescribeCdnIpInfoRequest,
    ) -> cdn_20180510_models.BatchDescribeCdnIpInfoResponse:
        """
        @summary Queries whether one or more IP addresses are assigned to Alibaba Cloud CDN.
        
        @description >The maximum number of times that each user can call this operation per second is 20.
        
        @param request: BatchDescribeCdnIpInfoRequest
        @return: BatchDescribeCdnIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_describe_cdn_ip_info_with_options_async(request, runtime)

    def batch_set_cdn_domain_config_with_options(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        """
        @summary Configures multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify multiple domain names and must separate them with commas (,). You can specify up to 50 domain names in each call.
        If the BatchSetCdnDomainConfig operation is successful, a unique configuration ID (ConfigId) is generated. You can use configuration IDs to update or delete configurations. For more information, see [Usage notes on ConfigId](https://help.aliyun.com/document_detail/388994.html).
        
        @param request: BatchSetCdnDomainConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetCdnDomainConfigResponse
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
        """
        @summary Configures multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify multiple domain names and must separate them with commas (,). You can specify up to 50 domain names in each call.
        If the BatchSetCdnDomainConfig operation is successful, a unique configuration ID (ConfigId) is generated. You can use configuration IDs to update or delete configurations. For more information, see [Usage notes on ConfigId](https://help.aliyun.com/document_detail/388994.html).
        
        @param request: BatchSetCdnDomainConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetCdnDomainConfigResponse
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
        """
        @summary Configures multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify multiple domain names and must separate them with commas (,). You can specify up to 50 domain names in each call.
        If the BatchSetCdnDomainConfig operation is successful, a unique configuration ID (ConfigId) is generated. You can use configuration IDs to update or delete configurations. For more information, see [Usage notes on ConfigId](https://help.aliyun.com/document_detail/388994.html).
        
        @param request: BatchSetCdnDomainConfigRequest
        @return: BatchSetCdnDomainConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_config_with_options(request, runtime)

    async def batch_set_cdn_domain_config_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        """
        @summary Configures multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify multiple domain names and must separate them with commas (,). You can specify up to 50 domain names in each call.
        If the BatchSetCdnDomainConfig operation is successful, a unique configuration ID (ConfigId) is generated. You can use configuration IDs to update or delete configurations. For more information, see [Usage notes on ConfigId](https://help.aliyun.com/document_detail/388994.html).
        
        @param request: BatchSetCdnDomainConfigRequest
        @return: BatchSetCdnDomainConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_cdn_domain_config_with_options_async(request, runtime)

    def batch_set_cdn_domain_server_certificate_with_options(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
        """
        @summary Enables, disables, or configures the SSL certificates of one or more accelerated domain names at a time.
        
        @description >    You can call this operation up to 10 times per second per account.
        >   You can specify up to 10 domain names in each request. Separate multiple domain names with commas (,)
        >   If the service type of a domain name is live streaming, the service may be unavailable after you configure the certificate for the domain name. Therefore, you cannot use this operation to configure the certificate for a domain name that is used for live streaming.
        
        @param request: BatchSetCdnDomainServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetCdnDomainServerCertificateResponse
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
        """
        @summary Enables, disables, or configures the SSL certificates of one or more accelerated domain names at a time.
        
        @description >    You can call this operation up to 10 times per second per account.
        >   You can specify up to 10 domain names in each request. Separate multiple domain names with commas (,)
        >   If the service type of a domain name is live streaming, the service may be unavailable after you configure the certificate for the domain name. Therefore, you cannot use this operation to configure the certificate for a domain name that is used for live streaming.
        
        @param request: BatchSetCdnDomainServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetCdnDomainServerCertificateResponse
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
        """
        @summary Enables, disables, or configures the SSL certificates of one or more accelerated domain names at a time.
        
        @description >    You can call this operation up to 10 times per second per account.
        >   You can specify up to 10 domain names in each request. Separate multiple domain names with commas (,)
        >   If the service type of a domain name is live streaming, the service may be unavailable after you configure the certificate for the domain name. Therefore, you cannot use this operation to configure the certificate for a domain name that is used for live streaming.
        
        @param request: BatchSetCdnDomainServerCertificateRequest
        @return: BatchSetCdnDomainServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_server_certificate_with_options(request, runtime)

    async def batch_set_cdn_domain_server_certificate_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
        """
        @summary Enables, disables, or configures the SSL certificates of one or more accelerated domain names at a time.
        
        @description >    You can call this operation up to 10 times per second per account.
        >   You can specify up to 10 domain names in each request. Separate multiple domain names with commas (,)
        >   If the service type of a domain name is live streaming, the service may be unavailable after you configure the certificate for the domain name. Therefore, you cannot use this operation to configure the certificate for a domain name that is used for live streaming.
        
        @param request: BatchSetCdnDomainServerCertificateRequest
        @return: BatchSetCdnDomainServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_cdn_domain_server_certificate_with_options_async(request, runtime)

    def batch_start_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
        """
        @summary Enables one or more domain names at a time. After a domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If a domain name specified in the request is in an invalid state or your account has an overdue payment, the domain name cannot be enabled.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStartCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartCdnDomainResponse
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
        """
        @summary Enables one or more domain names at a time. After a domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If a domain name specified in the request is in an invalid state or your account has an overdue payment, the domain name cannot be enabled.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStartCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartCdnDomainResponse
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
        """
        @summary Enables one or more domain names at a time. After a domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If a domain name specified in the request is in an invalid state or your account has an overdue payment, the domain name cannot be enabled.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStartCdnDomainRequest
        @return: BatchStartCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_cdn_domain_with_options(request, runtime)

    async def batch_start_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
        """
        @summary Enables one or more domain names at a time. After a domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If a domain name specified in the request is in an invalid state or your account has an overdue payment, the domain name cannot be enabled.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStartCdnDomainRequest
        @return: BatchStartCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_cdn_domain_with_options_async(request, runtime)

    def batch_stop_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
        """
        @summary Disables one or more accelerated domain names at a time. After an accelerated domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain name is disabled, Alibaba Cloud CDN retains its information and reroutes all the requests that are destined for the accelerated domain name to the origin.
        If you need to temporarily disable CDN acceleration for a domain name, we recommend that you call the StopDomain operation.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStopCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopCdnDomainResponse
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
        """
        @summary Disables one or more accelerated domain names at a time. After an accelerated domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain name is disabled, Alibaba Cloud CDN retains its information and reroutes all the requests that are destined for the accelerated domain name to the origin.
        If you need to temporarily disable CDN acceleration for a domain name, we recommend that you call the StopDomain operation.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStopCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopCdnDomainResponse
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
        """
        @summary Disables one or more accelerated domain names at a time. After an accelerated domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain name is disabled, Alibaba Cloud CDN retains its information and reroutes all the requests that are destined for the accelerated domain name to the origin.
        If you need to temporarily disable CDN acceleration for a domain name, we recommend that you call the StopDomain operation.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStopCdnDomainRequest
        @return: BatchStopCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_cdn_domain_with_options(request, runtime)

    async def batch_stop_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
        """
        @summary Disables one or more accelerated domain names at a time. After an accelerated domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain name is disabled, Alibaba Cloud CDN retains its information and reroutes all the requests that are destined for the accelerated domain name to the origin.
        If you need to temporarily disable CDN acceleration for a domain name, we recommend that you call the StopDomain operation.
        You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request.
        
        @param request: BatchStopCdnDomainRequest
        @return: BatchStopCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_cdn_domain_with_options_async(request, runtime)

    def batch_update_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
        """
        @summary Updates the configurations of multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: BatchUpdateCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateCdnDomainResponse
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
        """
        @summary Updates the configurations of multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: BatchUpdateCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateCdnDomainResponse
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
        """
        @summary Updates the configurations of multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: BatchUpdateCdnDomainRequest
        @return: BatchUpdateCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_update_cdn_domain_with_options(request, runtime)

    async def batch_update_cdn_domain_async(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
        """
        @summary Updates the configurations of multiple accelerated domain names at a time.
        
        @description    You can call this operation up to 30 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: BatchUpdateCdnDomainRequest
        @return: BatchUpdateCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_cdn_domain_with_options_async(request, runtime)

    def cdn_migrate_register_with_options(
        self,
        request: cdn_20180510_models.CdnMigrateRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CdnMigrateRegisterResponse:
        """
        @summary Registers the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for an Alibaba Cloud CDN-accelerated domain name. After the registration is successful, the routing center generates the dynamic routing information and send it to DCDN points of presence (POPs). This is a prerequisite for you to transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: CdnMigrateRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CdnMigrateRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CdnMigrateRegister',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CdnMigrateRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def cdn_migrate_register_with_options_async(
        self,
        request: cdn_20180510_models.CdnMigrateRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CdnMigrateRegisterResponse:
        """
        @summary Registers the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for an Alibaba Cloud CDN-accelerated domain name. After the registration is successful, the routing center generates the dynamic routing information and send it to DCDN points of presence (POPs). This is a prerequisite for you to transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: CdnMigrateRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CdnMigrateRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CdnMigrateRegister',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CdnMigrateRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cdn_migrate_register(
        self,
        request: cdn_20180510_models.CdnMigrateRegisterRequest,
    ) -> cdn_20180510_models.CdnMigrateRegisterResponse:
        """
        @summary Registers the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for an Alibaba Cloud CDN-accelerated domain name. After the registration is successful, the routing center generates the dynamic routing information and send it to DCDN points of presence (POPs). This is a prerequisite for you to transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: CdnMigrateRegisterRequest
        @return: CdnMigrateRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cdn_migrate_register_with_options(request, runtime)

    async def cdn_migrate_register_async(
        self,
        request: cdn_20180510_models.CdnMigrateRegisterRequest,
    ) -> cdn_20180510_models.CdnMigrateRegisterResponse:
        """
        @summary Registers the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for an Alibaba Cloud CDN-accelerated domain name. After the registration is successful, the routing center generates the dynamic routing information and send it to DCDN points of presence (POPs). This is a prerequisite for you to transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: CdnMigrateRegisterRequest
        @return: CdnMigrateRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cdn_migrate_register_with_options_async(request, runtime)

    def change_cdn_domain_to_dcdn_with_options(
        self,
        request: cdn_20180510_models.ChangeCdnDomainToDcdnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ChangeCdnDomainToDcdnResponse:
        """
        @summary Transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: ChangeCdnDomainToDcdnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCdnDomainToDcdnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
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
            action='ChangeCdnDomainToDcdn',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ChangeCdnDomainToDcdnResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cdn_domain_to_dcdn_with_options_async(
        self,
        request: cdn_20180510_models.ChangeCdnDomainToDcdnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ChangeCdnDomainToDcdnResponse:
        """
        @summary Transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: ChangeCdnDomainToDcdnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCdnDomainToDcdnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
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
            action='ChangeCdnDomainToDcdn',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ChangeCdnDomainToDcdnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cdn_domain_to_dcdn(
        self,
        request: cdn_20180510_models.ChangeCdnDomainToDcdnRequest,
    ) -> cdn_20180510_models.ChangeCdnDomainToDcdnResponse:
        """
        @summary Transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: ChangeCdnDomainToDcdnRequest
        @return: ChangeCdnDomainToDcdnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_cdn_domain_to_dcdn_with_options(request, runtime)

    async def change_cdn_domain_to_dcdn_async(
        self,
        request: cdn_20180510_models.ChangeCdnDomainToDcdnRequest,
    ) -> cdn_20180510_models.ChangeCdnDomainToDcdnResponse:
        """
        @summary Transfer a domain name from Alibaba Cloud CDN to DCDN.
        
        @param request: ChangeCdnDomainToDcdnRequest
        @return: ChangeCdnDomainToDcdnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_cdn_domain_to_dcdn_with_options_async(request, runtime)

    def check_cdn_domain_exist_with_options(
        self,
        request: cdn_20180510_models.CheckCdnDomainExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CheckCdnDomainExistResponse:
        """
        @summary Checks whether a domain name exists.
        
        @param request: CheckCdnDomainExistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCdnDomainExistResponse
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
            action='CheckCdnDomainExist',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CheckCdnDomainExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cdn_domain_exist_with_options_async(
        self,
        request: cdn_20180510_models.CheckCdnDomainExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CheckCdnDomainExistResponse:
        """
        @summary Checks whether a domain name exists.
        
        @param request: CheckCdnDomainExistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCdnDomainExistResponse
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
            action='CheckCdnDomainExist',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CheckCdnDomainExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cdn_domain_exist(
        self,
        request: cdn_20180510_models.CheckCdnDomainExistRequest,
    ) -> cdn_20180510_models.CheckCdnDomainExistResponse:
        """
        @summary Checks whether a domain name exists.
        
        @param request: CheckCdnDomainExistRequest
        @return: CheckCdnDomainExistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cdn_domain_exist_with_options(request, runtime)

    async def check_cdn_domain_exist_async(
        self,
        request: cdn_20180510_models.CheckCdnDomainExistRequest,
    ) -> cdn_20180510_models.CheckCdnDomainExistResponse:
        """
        @summary Checks whether a domain name exists.
        
        @param request: CheckCdnDomainExistRequest
        @return: CheckCdnDomainExistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_cdn_domain_exist_with_options_async(request, runtime)

    def check_cdn_domain_icpwith_options(
        self,
        request: cdn_20180510_models.CheckCdnDomainICPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CheckCdnDomainICPResponse:
        """
        @summary Checks whether an ICP filing is obtained for the domain name.
        
        @param request: CheckCdnDomainICPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCdnDomainICPResponse
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
            action='CheckCdnDomainICP',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CheckCdnDomainICPResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cdn_domain_icpwith_options_async(
        self,
        request: cdn_20180510_models.CheckCdnDomainICPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CheckCdnDomainICPResponse:
        """
        @summary Checks whether an ICP filing is obtained for the domain name.
        
        @param request: CheckCdnDomainICPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCdnDomainICPResponse
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
            action='CheckCdnDomainICP',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CheckCdnDomainICPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cdn_domain_icp(
        self,
        request: cdn_20180510_models.CheckCdnDomainICPRequest,
    ) -> cdn_20180510_models.CheckCdnDomainICPResponse:
        """
        @summary Checks whether an ICP filing is obtained for the domain name.
        
        @param request: CheckCdnDomainICPRequest
        @return: CheckCdnDomainICPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cdn_domain_icpwith_options(request, runtime)

    async def check_cdn_domain_icp_async(
        self,
        request: cdn_20180510_models.CheckCdnDomainICPRequest,
    ) -> cdn_20180510_models.CheckCdnDomainICPResponse:
        """
        @summary Checks whether an ICP filing is obtained for the domain name.
        
        @param request: CheckCdnDomainICPRequest
        @return: CheckCdnDomainICPResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_cdn_domain_icpwith_options_async(request, runtime)

    def create_cdn_certificate_signing_request_with_options(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
        """
        @summary Creates a certificate signing request (CSR).
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: CreateCdnCertificateSigningRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnCertificateSigningRequestResponse
        """
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
        """
        @summary Creates a certificate signing request (CSR).
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: CreateCdnCertificateSigningRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnCertificateSigningRequestResponse
        """
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
        """
        @summary Creates a certificate signing request (CSR).
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: CreateCdnCertificateSigningRequestRequest
        @return: CreateCdnCertificateSigningRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_certificate_signing_request_with_options(request, runtime)

    async def create_cdn_certificate_signing_request_async(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
        """
        @summary Creates a certificate signing request (CSR).
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: CreateCdnCertificateSigningRequestRequest
        @return: CreateCdnCertificateSigningRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_certificate_signing_request_with_options_async(request, runtime)

    def create_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
        """
        @summary Creates a tracking task. After you create a tracking task, the system sends operations reports to you by email on a regular basis.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: CreateCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnDeliverTaskResponse
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
        """
        @summary Creates a tracking task. After you create a tracking task, the system sends operations reports to you by email on a regular basis.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: CreateCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnDeliverTaskResponse
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
        """
        @summary Creates a tracking task. After you create a tracking task, the system sends operations reports to you by email on a regular basis.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: CreateCdnDeliverTaskRequest
        @return: CreateCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_deliver_task_with_options(request, runtime)

    async def create_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.CreateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.CreateCdnDeliverTaskResponse:
        """
        @summary Creates a tracking task. After you create a tracking task, the system sends operations reports to you by email on a regular basis.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: CreateCdnDeliverTaskRequest
        @return: CreateCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_deliver_task_with_options_async(request, runtime)

    def create_cdn_sub_task_with_options(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
        """
        @summary Creates a custom operations report.
        
        @description    This operation allows you to create a custom operations report for a specific domain name. You can view the statistics about the domain name in the report.
        You can call this operation up to three times per second per account.
        
        @param request: CreateCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnSubTaskResponse
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
        """
        @summary Creates a custom operations report.
        
        @description    This operation allows you to create a custom operations report for a specific domain name. You can view the statistics about the domain name in the report.
        You can call this operation up to three times per second per account.
        
        @param request: CreateCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCdnSubTaskResponse
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
        """
        @summary Creates a custom operations report.
        
        @description    This operation allows you to create a custom operations report for a specific domain name. You can view the statistics about the domain name in the report.
        You can call this operation up to three times per second per account.
        
        @param request: CreateCdnSubTaskRequest
        @return: CreateCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_sub_task_with_options(request, runtime)

    async def create_cdn_sub_task_async(
        self,
        request: cdn_20180510_models.CreateCdnSubTaskRequest,
    ) -> cdn_20180510_models.CreateCdnSubTaskResponse:
        """
        @summary Creates a custom operations report.
        
        @description    This operation allows you to create a custom operations report for a specific domain name. You can view the statistics about the domain name in the report.
        You can call this operation up to three times per second per account.
        
        @param request: CreateCdnSubTaskRequest
        @return: CreateCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_sub_task_with_options_async(request, runtime)

    def create_real_time_log_delivery_with_options(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        """
        @summary Enables real-time log delivery for specific accelerated domain names.
        
        @description >  You can call this API operation up to 100 times per second per account.
        
        @param request: CreateRealTimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRealTimeLogDeliveryResponse
        """
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
        """
        @summary Enables real-time log delivery for specific accelerated domain names.
        
        @description >  You can call this API operation up to 100 times per second per account.
        
        @param request: CreateRealTimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRealTimeLogDeliveryResponse
        """
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
        """
        @summary Enables real-time log delivery for specific accelerated domain names.
        
        @description >  You can call this API operation up to 100 times per second per account.
        
        @param request: CreateRealTimeLogDeliveryRequest
        @return: CreateRealTimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_real_time_log_delivery_with_options(request, runtime)

    async def create_real_time_log_delivery_async(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        """
        @summary Enables real-time log delivery for specific accelerated domain names.
        
        @description >  You can call this API operation up to 100 times per second per account.
        
        @param request: CreateRealTimeLogDeliveryRequest
        @return: CreateRealTimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_real_time_log_delivery_with_options_async(request, runtime)

    def create_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        """
        @summary Creates a task to export resource usage details to an Excel file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsageDetailDataExportTaskResponse
        """
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
        """
        @summary Creates a task to export resource usage details to an Excel file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsageDetailDataExportTaskResponse
        """
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
        """
        @summary Creates a task to export resource usage details to an Excel file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUsageDetailDataExportTaskRequest
        @return: CreateUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_usage_detail_data_export_task_with_options(request, runtime)

    async def create_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        """
        @summary Creates a task to export resource usage details to an Excel file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUsageDetailDataExportTaskRequest
        @return: CreateUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_usage_detail_data_export_task_with_options_async(request, runtime)

    def create_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        """
        @summary Creates a task to export your resource usage history to a PDF file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserUsageDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
        """
        @summary Creates a task to export your resource usage history to a PDF file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserUsageDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
        """
        @summary Creates a task to export your resource usage history to a PDF file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUserUsageDataExportTaskRequest
        @return: CreateUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_usage_data_export_task_with_options(request, runtime)

    async def create_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        """
        @summary Creates a task to export your resource usage history to a PDF file.
        
        @description    You can create a task to query data in the last year. The maximum time range that can be queried is one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: CreateUserUsageDataExportTaskRequest
        @return: CreateUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_usage_data_export_task_with_options_async(request, runtime)

    def delete_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
        """
        @summary Deletes tracking tasks by task ID.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DeleteCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
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
        """
        @summary Deletes tracking tasks by task ID.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DeleteCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnDeliverTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
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
        """
        @summary Deletes tracking tasks by task ID.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DeleteCdnDeliverTaskRequest
        @return: DeleteCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_deliver_task_with_options(request, runtime)

    async def delete_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.DeleteCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.DeleteCdnDeliverTaskResponse:
        """
        @summary Deletes tracking tasks by task ID.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DeleteCdnDeliverTaskRequest
        @return: DeleteCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_deliver_task_with_options_async(request, runtime)

    def delete_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        """
        @summary Removes an accelerated domain name from Alibaba Cloud CDN.
        
        @description    We recommend that you add an A record for the domain name in the system of your DNS service provider before you remove the domain name from Alibaba Cloud CDN. Otherwise, the domain name may become inaccessible. Proceed with caution.
        After you successfully call the DeleteCdnDomain operation, all records of the removed domain name are deleted. If you need to only disable the domain name, we recommend that you call the StopCdnDomain operation.
        You can call this operation up to 10 times per second per account.
        
        @param request: DeleteCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        """
        @summary Removes an accelerated domain name from Alibaba Cloud CDN.
        
        @description    We recommend that you add an A record for the domain name in the system of your DNS service provider before you remove the domain name from Alibaba Cloud CDN. Otherwise, the domain name may become inaccessible. Proceed with caution.
        After you successfully call the DeleteCdnDomain operation, all records of the removed domain name are deleted. If you need to only disable the domain name, we recommend that you call the StopCdnDomain operation.
        You can call this operation up to 10 times per second per account.
        
        @param request: DeleteCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        """
        @summary Removes an accelerated domain name from Alibaba Cloud CDN.
        
        @description    We recommend that you add an A record for the domain name in the system of your DNS service provider before you remove the domain name from Alibaba Cloud CDN. Otherwise, the domain name may become inaccessible. Proceed with caution.
        After you successfully call the DeleteCdnDomain operation, all records of the removed domain name are deleted. If you need to only disable the domain name, we recommend that you call the StopCdnDomain operation.
        You can call this operation up to 10 times per second per account.
        
        @param request: DeleteCdnDomainRequest
        @return: DeleteCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_domain_with_options(request, runtime)

    async def delete_cdn_domain_async(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        """
        @summary Removes an accelerated domain name from Alibaba Cloud CDN.
        
        @description    We recommend that you add an A record for the domain name in the system of your DNS service provider before you remove the domain name from Alibaba Cloud CDN. Otherwise, the domain name may become inaccessible. Proceed with caution.
        After you successfully call the DeleteCdnDomain operation, all records of the removed domain name are deleted. If you need to only disable the domain name, we recommend that you call the StopCdnDomain operation.
        You can call this operation up to 10 times per second per account.
        
        @param request: DeleteCdnDomainRequest
        @return: DeleteCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_domain_with_options_async(request, runtime)

    def delete_cdn_sub_task_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        """
        @summary The ID of the request.
        
        @description >  You can call this API operation up to three times per second per account.
        
        @param request: DeleteCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnSubTaskResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        """
        @summary The ID of the request.
        
        @description >  You can call this API operation up to three times per second per account.
        
        @param request: DeleteCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCdnSubTaskResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def delete_cdn_sub_task(self) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        """
        @summary The ID of the request.
        
        @description >  You can call this API operation up to three times per second per account.
        
        @return: DeleteCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_sub_task_with_options(runtime)

    async def delete_cdn_sub_task_async(self) -> cdn_20180510_models.DeleteCdnSubTaskResponse:
        """
        @summary The ID of the request.
        
        @description >  You can call this API operation up to three times per second per account.
        
        @return: DeleteCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_sub_task_with_options_async(runtime)

    def delete_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        """
        @summary Deletes a specified Function Compute trigger.
        
        @param request: DeleteFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a specified Function Compute trigger.
        
        @param request: DeleteFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a specified Function Compute trigger.
        
        @param request: DeleteFCTriggerRequest
        @return: DeleteFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_fctrigger_with_options(request, runtime)

    async def delete_fctrigger_async(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        """
        @summary Deletes a specified Function Compute trigger.
        
        @param request: DeleteFCTriggerRequest
        @return: DeleteFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_fctrigger_with_options_async(request, runtime)

    def delete_real_time_log_logstore_with_options(
        self,
        request: cdn_20180510_models.DeleteRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealTimeLogLogstoreResponse:
        """
        @summary Deletes the Logstore that is used by a specified configuration record of real-time log delivery.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealTimeLogLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRealTimeLogLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealTimeLogLogstore',
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
            cdn_20180510_models.DeleteRealTimeLogLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_real_time_log_logstore_with_options_async(
        self,
        request: cdn_20180510_models.DeleteRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealTimeLogLogstoreResponse:
        """
        @summary Deletes the Logstore that is used by a specified configuration record of real-time log delivery.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealTimeLogLogstoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRealTimeLogLogstoreResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealTimeLogLogstore',
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
            cdn_20180510_models.DeleteRealTimeLogLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_real_time_log_logstore(
        self,
        request: cdn_20180510_models.DeleteRealTimeLogLogstoreRequest,
    ) -> cdn_20180510_models.DeleteRealTimeLogLogstoreResponse:
        """
        @summary Deletes the Logstore that is used by a specified configuration record of real-time log delivery.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealTimeLogLogstoreRequest
        @return: DeleteRealTimeLogLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_real_time_log_logstore_with_options(request, runtime)

    async def delete_real_time_log_logstore_async(
        self,
        request: cdn_20180510_models.DeleteRealTimeLogLogstoreRequest,
    ) -> cdn_20180510_models.DeleteRealTimeLogLogstoreResponse:
        """
        @summary Deletes the Logstore that is used by a specified configuration record of real-time log delivery.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealTimeLogLogstoreRequest
        @return: DeleteRealTimeLogLogstoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_real_time_log_logstore_with_options_async(request, runtime)

    def delete_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        """
        @summary Deletes the configurations of real-time log delivery for specific accelerated domain names.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRealtimeLogDeliveryResponse
        """
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
        """
        @summary Deletes the configurations of real-time log delivery for specific accelerated domain names.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRealtimeLogDeliveryResponse
        """
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
        """
        @summary Deletes the configurations of real-time log delivery for specific accelerated domain names.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealtimeLogDeliveryRequest
        @return: DeleteRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_realtime_log_delivery_with_options(request, runtime)

    async def delete_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        """
        @summary Deletes the configurations of real-time log delivery for specific accelerated domain names.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteRealtimeLogDeliveryRequest
        @return: DeleteRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_realtime_log_delivery_with_options_async(request, runtime)

    def delete_specific_config_with_options(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
        """
        @summary Deletes specified configurations of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpecificConfigResponse
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
        """
        @summary Deletes specified configurations of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteSpecificConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpecificConfigResponse
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
        """
        @summary Deletes specified configurations of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteSpecificConfigRequest
        @return: DeleteSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_config_with_options(request, runtime)

    async def delete_specific_config_async(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
        """
        @summary Deletes specified configurations of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DeleteSpecificConfigRequest
        @return: DeleteSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_specific_config_with_options_async(request, runtime)

    def delete_specific_staging_config_with_options(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
        """
        @summary Deletes a specified configuration of the staging environment.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteSpecificStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpecificStagingConfigResponse
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
        """
        @summary Deletes a specified configuration of the staging environment.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteSpecificStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpecificStagingConfigResponse
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
        """
        @summary Deletes a specified configuration of the staging environment.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteSpecificStagingConfigRequest
        @return: DeleteSpecificStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_staging_config_with_options(request, runtime)

    async def delete_specific_staging_config_async(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
        """
        @summary Deletes a specified configuration of the staging environment.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DeleteSpecificStagingConfigRequest
        @return: DeleteSpecificStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_specific_staging_config_with_options_async(request, runtime)

    def delete_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
        """
        @summary Deletes a task that was used to export usage details.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsageDetailDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a task that was used to export usage details.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsageDetailDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a task that was used to export usage details.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUsageDetailDataExportTaskRequest
        @return: DeleteUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_usage_detail_data_export_task_with_options(request, runtime)

    async def delete_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
        """
        @summary Deletes a task that was used to export usage details.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUsageDetailDataExportTaskRequest
        @return: DeleteUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_usage_detail_data_export_task_with_options_async(request, runtime)

    def delete_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
        """
        @summary Deletes a task that was used to export usage history.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserUsageDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a task that was used to export usage history.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserUsageDataExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Deletes a task that was used to export usage history.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUserUsageDataExportTaskRequest
        @return: DeleteUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_usage_data_export_task_with_options(request, runtime)

    async def delete_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
        """
        @summary Deletes a task that was used to export usage history.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DeleteUserUsageDataExportTaskRequest
        @return: DeleteUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_blocked_regions_with_options(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        """
        @summary Queries countries and regions that can be added to the blacklist.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeBlockedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlockedRegionsResponse
        """
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
        """
        @summary Queries countries and regions that can be added to the blacklist.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeBlockedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlockedRegionsResponse
        """
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
        """
        @summary Queries countries and regions that can be added to the blacklist.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeBlockedRegionsRequest
        @return: DescribeBlockedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_blocked_regions_with_options(request, runtime)

    async def describe_blocked_regions_async(
        self,
        request: cdn_20180510_models.DescribeBlockedRegionsRequest,
    ) -> cdn_20180510_models.DescribeBlockedRegionsResponse:
        """
        @summary Queries countries and regions that can be added to the blacklist.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeBlockedRegionsRequest
        @return: DescribeBlockedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_blocked_regions_with_options_async(request, runtime)

    def describe_cdn_certificate_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        """
        @summary Queries the detailed information about an SSL certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateDetailResponse
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
        """
        @summary Queries the detailed information about an SSL certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateDetailResponse
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
        """
        @summary Queries the detailed information about an SSL certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnCertificateDetailRequest
        @return: DescribeCdnCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_detail_with_options(request, runtime)

    async def describe_cdn_certificate_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        """
        @summary Queries the detailed information about an SSL certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnCertificateDetailRequest
        @return: DescribeCdnCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certificate_detail_with_options_async(request, runtime)

    def describe_cdn_certificate_detail_by_id_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse:
        """
        @summary Queries certificate details by certificate ID.
        
        @param request: DescribeCdnCertificateDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateDetailByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnCertificateDetailById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certificate_detail_by_id_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse:
        """
        @summary Queries certificate details by certificate ID.
        
        @param request: DescribeCdnCertificateDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateDetailByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnCertificateDetailById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certificate_detail_by_id(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailByIdRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse:
        """
        @summary Queries certificate details by certificate ID.
        
        @param request: DescribeCdnCertificateDetailByIdRequest
        @return: DescribeCdnCertificateDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_detail_by_id_with_options(request, runtime)

    async def describe_cdn_certificate_detail_by_id_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailByIdRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailByIdResponse:
        """
        @summary Queries certificate details by certificate ID.
        
        @param request: DescribeCdnCertificateDetailByIdRequest
        @return: DescribeCdnCertificateDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certificate_detail_by_id_with_options_async(request, runtime)

    def describe_cdn_certificate_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
        """
        @deprecated OpenAPI DescribeCdnCertificateList is deprecated, please use Cdn::2018-05-10::DescribeCdnSSLCertificateList instead.
        
        @summary Queries the certificates of accelerated domain names.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateListResponse
        Deprecated
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
        """
        @deprecated OpenAPI DescribeCdnCertificateList is deprecated, please use Cdn::2018-05-10::DescribeCdnSSLCertificateList instead.
        
        @summary Queries the certificates of accelerated domain names.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnCertificateListResponse
        Deprecated
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
        """
        @deprecated OpenAPI DescribeCdnCertificateList is deprecated, please use Cdn::2018-05-10::DescribeCdnSSLCertificateList instead.
        
        @summary Queries the certificates of accelerated domain names.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnCertificateListRequest
        @return: DescribeCdnCertificateListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_list_with_options(request, runtime)

    async def describe_cdn_certificate_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
        """
        @deprecated OpenAPI DescribeCdnCertificateList is deprecated, please use Cdn::2018-05-10::DescribeCdnSSLCertificateList instead.
        
        @summary Queries the certificates of accelerated domain names.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnCertificateListRequest
        @return: DescribeCdnCertificateListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certificate_list_with_options_async(request, runtime)

    def describe_cdn_condition_ipbinfo_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnConditionIPBInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnConditionIPBInfoResponse:
        """
        @summary Queries the Internet service provider (ISP), region, and country that are required for advanced conditions.
        
        @param request: DescribeCdnConditionIPBInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnConditionIPBInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnConditionIPBInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnConditionIPBInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_condition_ipbinfo_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnConditionIPBInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnConditionIPBInfoResponse:
        """
        @summary Queries the Internet service provider (ISP), region, and country that are required for advanced conditions.
        
        @param request: DescribeCdnConditionIPBInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnConditionIPBInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnConditionIPBInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnConditionIPBInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_condition_ipbinfo(
        self,
        request: cdn_20180510_models.DescribeCdnConditionIPBInfoRequest,
    ) -> cdn_20180510_models.DescribeCdnConditionIPBInfoResponse:
        """
        @summary Queries the Internet service provider (ISP), region, and country that are required for advanced conditions.
        
        @param request: DescribeCdnConditionIPBInfoRequest
        @return: DescribeCdnConditionIPBInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_condition_ipbinfo_with_options(request, runtime)

    async def describe_cdn_condition_ipbinfo_async(
        self,
        request: cdn_20180510_models.DescribeCdnConditionIPBInfoRequest,
    ) -> cdn_20180510_models.DescribeCdnConditionIPBInfoResponse:
        """
        @summary Queries the Internet service provider (ISP), region, and country that are required for advanced conditions.
        
        @param request: DescribeCdnConditionIPBInfoRequest
        @return: DescribeCdnConditionIPBInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_condition_ipbinfo_with_options_async(request, runtime)

    def describe_cdn_deleted_domains_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
        """
        @summary Queries the domain names that are deleted from your account.
        
        @description > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeCdnDeletedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDeletedDomainsResponse
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
        """
        @summary Queries the domain names that are deleted from your account.
        
        @description > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeCdnDeletedDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDeletedDomainsResponse
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
        """
        @summary Queries the domain names that are deleted from your account.
        
        @description > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeCdnDeletedDomainsRequest
        @return: DescribeCdnDeletedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deleted_domains_with_options(request, runtime)

    async def describe_cdn_deleted_domains_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeletedDomainsRequest,
    ) -> cdn_20180510_models.DescribeCdnDeletedDomainsResponse:
        """
        @summary Queries the domain names that are deleted from your account.
        
        @description > You can call this operation up to 10 times per second per account.
        
        @param request: DescribeCdnDeletedDomainsRequest
        @return: DescribeCdnDeletedDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_deleted_domains_with_options_async(request, runtime)

    def describe_cdn_deliver_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
        """
        @summary Queries one or more tracking tasks of operations reports.
        
        @description > You can call this operation up to 3 times per second per account.
        
        @param request: DescribeCdnDeliverListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDeliverListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
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
        """
        @summary Queries one or more tracking tasks of operations reports.
        
        @description > You can call this operation up to 3 times per second per account.
        
        @param request: DescribeCdnDeliverListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDeliverListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
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
        """
        @summary Queries one or more tracking tasks of operations reports.
        
        @description > You can call this operation up to 3 times per second per account.
        
        @param request: DescribeCdnDeliverListRequest
        @return: DescribeCdnDeliverListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deliver_list_with_options(request, runtime)

    async def describe_cdn_deliver_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnDeliverListRequest,
    ) -> cdn_20180510_models.DescribeCdnDeliverListResponse:
        """
        @summary Queries one or more tracking tasks of operations reports.
        
        @description > You can call this operation up to 3 times per second per account.
        
        @param request: DescribeCdnDeliverListRequest
        @return: DescribeCdnDeliverListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_deliver_list_with_options_async(request, runtime)

    def describe_cdn_domain_atoa_logs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainAtoaLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse:
        """
        @summary 天翼定制化小时日志下载接口
        
        @param request: DescribeCdnDomainAtoaLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainAtoaLogsResponse
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
            action='DescribeCdnDomainAtoaLogs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_atoa_logs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainAtoaLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse:
        """
        @summary 天翼定制化小时日志下载接口
        
        @param request: DescribeCdnDomainAtoaLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainAtoaLogsResponse
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
            action='DescribeCdnDomainAtoaLogs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_atoa_logs(
        self,
        request: cdn_20180510_models.DescribeCdnDomainAtoaLogsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse:
        """
        @summary 天翼定制化小时日志下载接口
        
        @param request: DescribeCdnDomainAtoaLogsRequest
        @return: DescribeCdnDomainAtoaLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_atoa_logs_with_options(request, runtime)

    async def describe_cdn_domain_atoa_logs_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainAtoaLogsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainAtoaLogsResponse:
        """
        @summary 天翼定制化小时日志下载接口
        
        @param request: DescribeCdnDomainAtoaLogsRequest
        @return: DescribeCdnDomainAtoaLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_atoa_logs_with_options_async(request, runtime)

    def describe_cdn_domain_by_certificate_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        """
        @summary Queries accelerated domain names by SSL certificate.
        
        @description >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainByCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainByCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exact):
            query['Exact'] = request.exact
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
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
        """
        @summary Queries accelerated domain names by SSL certificate.
        
        @description >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainByCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainByCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exact):
            query['Exact'] = request.exact
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.sslstatus):
            query['SSLStatus'] = request.sslstatus
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
        """
        @summary Queries accelerated domain names by SSL certificate.
        
        @description >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainByCertificateRequest
        @return: DescribeCdnDomainByCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_by_certificate_with_options(request, runtime)

    async def describe_cdn_domain_by_certificate_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        """
        @summary Queries accelerated domain names by SSL certificate.
        
        @description >  You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainByCertificateRequest
        @return: DescribeCdnDomainByCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_cdn_domain_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
        """
        @summary Queries the configurations of an accelerated domain name. You can query the configurations of one or more features at the same time.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainConfigsResponse
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
        """
        @summary Queries the configurations of an accelerated domain name. You can query the configurations of one or more features at the same time.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainConfigsResponse
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
        """
        @summary Queries the configurations of an accelerated domain name. You can query the configurations of one or more features at the same time.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainConfigsRequest
        @return: DescribeCdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_configs_with_options(request, runtime)

    async def describe_cdn_domain_configs_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
        """
        @summary Queries the configurations of an accelerated domain name. You can query the configurations of one or more features at the same time.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnDomainConfigsRequest
        @return: DescribeCdnDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_configs_with_options_async(request, runtime)

    def describe_cdn_domain_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
        """
        @summary Queries the basic information about an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainDetailResponse
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
        """
        @summary Queries the basic information about an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainDetailResponse
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
        """
        @summary Queries the basic information about an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainDetailRequest
        @return: DescribeCdnDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_detail_with_options(request, runtime)

    async def describe_cdn_domain_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
        """
        @summary Queries the basic information about an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainDetailRequest
        @return: DescribeCdnDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_detail_with_options_async(request, runtime)

    def describe_cdn_domain_logs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
        """
        @summary Queries the address where you can download the log data of a specific domain name.
        
        @description    If you do not set **StartTime** or **EndTime**, the request returns the data collected in the last 24 hours. If you set both **StartTime** and **EndTime**, the request returns the data collected within the specified time range.
        The log data is collected every hour.
        You can call this operation up to 100 times per second per account.
        You can query only logs in the last month. The start time and the current time cannot exceed 31 days.
        
        @param request: DescribeCdnDomainLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainLogsResponse
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
        """
        @summary Queries the address where you can download the log data of a specific domain name.
        
        @description    If you do not set **StartTime** or **EndTime**, the request returns the data collected in the last 24 hours. If you set both **StartTime** and **EndTime**, the request returns the data collected within the specified time range.
        The log data is collected every hour.
        You can call this operation up to 100 times per second per account.
        You can query only logs in the last month. The start time and the current time cannot exceed 31 days.
        
        @param request: DescribeCdnDomainLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainLogsResponse
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
        """
        @summary Queries the address where you can download the log data of a specific domain name.
        
        @description    If you do not set **StartTime** or **EndTime**, the request returns the data collected in the last 24 hours. If you set both **StartTime** and **EndTime**, the request returns the data collected within the specified time range.
        The log data is collected every hour.
        You can call this operation up to 100 times per second per account.
        You can query only logs in the last month. The start time and the current time cannot exceed 31 days.
        
        @param request: DescribeCdnDomainLogsRequest
        @return: DescribeCdnDomainLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_logs_with_options(request, runtime)

    async def describe_cdn_domain_logs_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
        """
        @summary Queries the address where you can download the log data of a specific domain name.
        
        @description    If you do not set **StartTime** or **EndTime**, the request returns the data collected in the last 24 hours. If you set both **StartTime** and **EndTime**, the request returns the data collected within the specified time range.
        The log data is collected every hour.
        You can call this operation up to 100 times per second per account.
        You can query only logs in the last month. The start time and the current time cannot exceed 31 days.
        
        @param request: DescribeCdnDomainLogsRequest
        @return: DescribeCdnDomainLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_logs_with_options_async(request, runtime)

    def describe_cdn_domain_logs_ex_ttl_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsExTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse:
        """
        @param request: DescribeCdnDomainLogsExTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainLogsExTtlResponse
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
            action='DescribeCdnDomainLogsExTtl',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_logs_ex_ttl_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsExTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse:
        """
        @param request: DescribeCdnDomainLogsExTtlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainLogsExTtlResponse
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
            action='DescribeCdnDomainLogsExTtl',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_logs_ex_ttl(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsExTtlRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse:
        """
        @param request: DescribeCdnDomainLogsExTtlRequest
        @return: DescribeCdnDomainLogsExTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_logs_ex_ttl_with_options(request, runtime)

    async def describe_cdn_domain_logs_ex_ttl_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsExTtlRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsExTtlResponse:
        """
        @param request: DescribeCdnDomainLogsExTtlRequest
        @return: DescribeCdnDomainLogsExTtlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_logs_ex_ttl_with_options_async(request, runtime)

    def describe_cdn_domain_staging_config_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
        """
        @summary Queries the configurations of features in the staging environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainStagingConfigResponse
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
        """
        @summary Queries the configurations of features in the staging environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnDomainStagingConfigResponse
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
        """
        @summary Queries the configurations of features in the staging environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainStagingConfigRequest
        @return: DescribeCdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_staging_config_with_options(request, runtime)

    async def describe_cdn_domain_staging_config_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
        """
        @summary Queries the configurations of features in the staging environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnDomainStagingConfigRequest
        @return: DescribeCdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_staging_config_with_options_async(request, runtime)

    def describe_cdn_https_domain_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
        """
        @summary Queries the information about SSL certificates that belong to your Alibaba Cloud account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnHttpsDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnHttpsDomainListResponse
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
        """
        @summary Queries the information about SSL certificates that belong to your Alibaba Cloud account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnHttpsDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnHttpsDomainListResponse
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
        """
        @summary Queries the information about SSL certificates that belong to your Alibaba Cloud account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnHttpsDomainListRequest
        @return: DescribeCdnHttpsDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_https_domain_list_with_options(request, runtime)

    async def describe_cdn_https_domain_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
        """
        @summary Queries the information about SSL certificates that belong to your Alibaba Cloud account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnHttpsDomainListRequest
        @return: DescribeCdnHttpsDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_https_domain_list_with_options_async(request, runtime)

    def describe_cdn_migrate_register_status_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnMigrateRegisterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse:
        """
        @summary Queries the registration status of the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for a domain name that is added to Alibaba Cloud CDN.
        
        @description >  If a domain name is not transferred from Alibaba Cloud CDN to DCDN after it is registered in the routing center of DCDN, the registration information is retained for only one day.
        
        @param request: DescribeCdnMigrateRegisterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnMigrateRegisterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnMigrateRegisterStatus',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_migrate_register_status_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnMigrateRegisterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse:
        """
        @summary Queries the registration status of the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for a domain name that is added to Alibaba Cloud CDN.
        
        @description >  If a domain name is not transferred from Alibaba Cloud CDN to DCDN after it is registered in the routing center of DCDN, the registration information is retained for only one day.
        
        @param request: DescribeCdnMigrateRegisterStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnMigrateRegisterStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnMigrateRegisterStatus',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_migrate_register_status(
        self,
        request: cdn_20180510_models.DescribeCdnMigrateRegisterStatusRequest,
    ) -> cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse:
        """
        @summary Queries the registration status of the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for a domain name that is added to Alibaba Cloud CDN.
        
        @description >  If a domain name is not transferred from Alibaba Cloud CDN to DCDN after it is registered in the routing center of DCDN, the registration information is retained for only one day.
        
        @param request: DescribeCdnMigrateRegisterStatusRequest
        @return: DescribeCdnMigrateRegisterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_migrate_register_status_with_options(request, runtime)

    async def describe_cdn_migrate_register_status_async(
        self,
        request: cdn_20180510_models.DescribeCdnMigrateRegisterStatusRequest,
    ) -> cdn_20180510_models.DescribeCdnMigrateRegisterStatusResponse:
        """
        @summary Queries the registration status of the dynamic routing feature of Dynamic Content Delivery Network (DCDN) for a domain name that is added to Alibaba Cloud CDN.
        
        @description >  If a domain name is not transferred from Alibaba Cloud CDN to DCDN after it is registered in the routing center of DCDN, the registration information is retained for only one day.
        
        @param request: DescribeCdnMigrateRegisterStatusRequest
        @return: DescribeCdnMigrateRegisterStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_migrate_register_status_with_options_async(request, runtime)

    def describe_cdn_order_commodity_code_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnOrderCommodityCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse:
        """
        @summary Queries the code of a commodity by account UID.
        
        @param request: DescribeCdnOrderCommodityCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnOrderCommodityCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnOrderCommodityCode',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_order_commodity_code_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnOrderCommodityCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse:
        """
        @summary Queries the code of a commodity by account UID.
        
        @param request: DescribeCdnOrderCommodityCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnOrderCommodityCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnOrderCommodityCode',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_order_commodity_code(
        self,
        request: cdn_20180510_models.DescribeCdnOrderCommodityCodeRequest,
    ) -> cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse:
        """
        @summary Queries the code of a commodity by account UID.
        
        @param request: DescribeCdnOrderCommodityCodeRequest
        @return: DescribeCdnOrderCommodityCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_order_commodity_code_with_options(request, runtime)

    async def describe_cdn_order_commodity_code_async(
        self,
        request: cdn_20180510_models.DescribeCdnOrderCommodityCodeRequest,
    ) -> cdn_20180510_models.DescribeCdnOrderCommodityCodeResponse:
        """
        @summary Queries the code of a commodity by account UID.
        
        @param request: DescribeCdnOrderCommodityCodeRequest
        @return: DescribeCdnOrderCommodityCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_order_commodity_code_with_options_async(request, runtime)

    def describe_cdn_region_and_isp_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
        """
        @summary Queries Internet service providers (ISPs) and regions that are supported by Alibaba Cloud CDN.
        
        @description    The lists of ISPs and regions that are supported by Alibaba Cloud CDN are updated and published on the Alibaba Cloud International site.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnRegionAndIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnRegionAndIspResponse
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
        """
        @summary Queries Internet service providers (ISPs) and regions that are supported by Alibaba Cloud CDN.
        
        @description    The lists of ISPs and regions that are supported by Alibaba Cloud CDN are updated and published on the Alibaba Cloud International site.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnRegionAndIspRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnRegionAndIspResponse
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
        """
        @summary Queries Internet service providers (ISPs) and regions that are supported by Alibaba Cloud CDN.
        
        @description    The lists of ISPs and regions that are supported by Alibaba Cloud CDN are updated and published on the Alibaba Cloud International site.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnRegionAndIspRequest
        @return: DescribeCdnRegionAndIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_region_and_isp_with_options(request, runtime)

    async def describe_cdn_region_and_isp_async(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
        """
        @summary Queries Internet service providers (ISPs) and regions that are supported by Alibaba Cloud CDN.
        
        @description    The lists of ISPs and regions that are supported by Alibaba Cloud CDN are updated and published on the Alibaba Cloud International site.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnRegionAndIspRequest
        @return: DescribeCdnRegionAndIspResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_region_and_isp_with_options_async(request, runtime)

    def describe_cdn_report_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
        """
        @summary Queries the content of an operations report.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnReportResponse
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
        """
        @summary Queries the content of an operations report.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnReportResponse
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
        """
        @summary Queries the content of an operations report.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportRequest
        @return: DescribeCdnReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_with_options(request, runtime)

    async def describe_cdn_report_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportRequest,
    ) -> cdn_20180510_models.DescribeCdnReportResponse:
        """
        @summary Queries the content of an operations report.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportRequest
        @return: DescribeCdnReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_report_with_options_async(request, runtime)

    def describe_cdn_report_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
        """
        @summary Queries operations reports.
        
        @description    This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries operations reports.
        
        @description    This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnReportListResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries operations reports.
        
        @description    This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportListRequest
        @return: DescribeCdnReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_list_with_options(request, runtime)

    async def describe_cdn_report_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnReportListRequest,
    ) -> cdn_20180510_models.DescribeCdnReportListResponse:
        """
        @summary Queries operations reports.
        
        @description    This operation queries the metadata of all operations reports. The statistics in the reports are not returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnReportListRequest
        @return: DescribeCdnReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_report_list_with_options_async(request, runtime)

    def describe_cdn_smcertificate_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
        """
        @summary Queries the details about a ShangMi (SM) certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnSMCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSMCertificateDetailResponse
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
        """
        @summary Queries the details about a ShangMi (SM) certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnSMCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSMCertificateDetailResponse
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
        """
        @summary Queries the details about a ShangMi (SM) certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnSMCertificateDetailRequest
        @return: DescribeCdnSMCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_detail_with_options(request, runtime)

    async def describe_cdn_smcertificate_detail_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateDetailRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateDetailResponse:
        """
        @summary Queries the details about a ShangMi (SM) certificate.
        
        @description > You can call this operation up to 20 times per second per account.
        
        @param request: DescribeCdnSMCertificateDetailRequest
        @return: DescribeCdnSMCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_smcertificate_detail_with_options_async(request, runtime)

    def describe_cdn_smcertificate_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
        """
        @summary Queries the ShangMi (SM) certificates of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnSMCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSMCertificateListResponse
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
        """
        @summary Queries the ShangMi (SM) certificates of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnSMCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSMCertificateListResponse
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
        """
        @summary Queries the ShangMi (SM) certificates of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnSMCertificateListRequest
        @return: DescribeCdnSMCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_list_with_options(request, runtime)

    async def describe_cdn_smcertificate_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnSMCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnSMCertificateListResponse:
        """
        @summary Queries the ShangMi (SM) certificates of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnSMCertificateListRequest
        @return: DescribeCdnSMCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_smcertificate_list_with_options_async(request, runtime)

    def describe_cdn_sslcertificate_list_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSSLCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSSLCertificateListResponse:
        """
        @summary Queries the certificate list by domain name.
        
        @param request: DescribeCdnSSLCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSSLCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSSLCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSSLCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sslcertificate_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnSSLCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSSLCertificateListResponse:
        """
        @summary Queries the certificate list by domain name.
        
        @param request: DescribeCdnSSLCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSSLCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSSLCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSSLCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sslcertificate_list(
        self,
        request: cdn_20180510_models.DescribeCdnSSLCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnSSLCertificateListResponse:
        """
        @summary Queries the certificate list by domain name.
        
        @param request: DescribeCdnSSLCertificateListRequest
        @return: DescribeCdnSSLCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_sslcertificate_list_with_options(request, runtime)

    async def describe_cdn_sslcertificate_list_async(
        self,
        request: cdn_20180510_models.DescribeCdnSSLCertificateListRequest,
    ) -> cdn_20180510_models.DescribeCdnSSLCertificateListResponse:
        """
        @summary Queries the certificate list by domain name.
        
        @param request: DescribeCdnSSLCertificateListRequest
        @return: DescribeCdnSSLCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_sslcertificate_list_with_options_async(request, runtime)

    def describe_cdn_sec_func_info_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSecFuncInfoResponse:
        """
        @summary Queries information about security features of Alibaba Cloud CDN.
        
        @param request: DescribeCdnSecFuncInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSecFuncInfoResponse
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
            action='DescribeCdnSecFuncInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSecFuncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_sec_func_info_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSecFuncInfoResponse:
        """
        @summary Queries information about security features of Alibaba Cloud CDN.
        
        @param request: DescribeCdnSecFuncInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSecFuncInfoResponse
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
            action='DescribeCdnSecFuncInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSecFuncInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_sec_func_info(
        self,
        request: cdn_20180510_models.DescribeCdnSecFuncInfoRequest,
    ) -> cdn_20180510_models.DescribeCdnSecFuncInfoResponse:
        """
        @summary Queries information about security features of Alibaba Cloud CDN.
        
        @param request: DescribeCdnSecFuncInfoRequest
        @return: DescribeCdnSecFuncInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_sec_func_info_with_options(request, runtime)

    async def describe_cdn_sec_func_info_async(
        self,
        request: cdn_20180510_models.DescribeCdnSecFuncInfoRequest,
    ) -> cdn_20180510_models.DescribeCdnSecFuncInfoResponse:
        """
        @summary Queries information about security features of Alibaba Cloud CDN.
        
        @param request: DescribeCdnSecFuncInfoRequest
        @return: DescribeCdnSecFuncInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_sec_func_info_with_options_async(request, runtime)

    def describe_cdn_service_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        """
        @summary Queries the status of your Alibaba Cloud CDN service. The information includes the service activation time, the current service status, the current metering method, and the metering method for the next cycle.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnServiceResponse
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
        """
        @summary Queries the status of your Alibaba Cloud CDN service. The information includes the service activation time, the current service status, the current metering method, and the metering method for the next cycle.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnServiceResponse
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
        """
        @summary Queries the status of your Alibaba Cloud CDN service. The information includes the service activation time, the current service status, the current metering method, and the metering method for the next cycle.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnServiceRequest
        @return: DescribeCdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_service_with_options(request, runtime)

    async def describe_cdn_service_async(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        """
        @summary Queries the status of your Alibaba Cloud CDN service. The information includes the service activation time, the current service status, the current metering method, and the metering method for the next cycle.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnServiceRequest
        @return: DescribeCdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_service_with_options_async(request, runtime)

    def describe_cdn_sub_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        """
        @summary Queries the tracking tasks that you have created.
        
        @description    By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnSubListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSubListResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnSubListResponse:
        """
        @summary Queries the tracking tasks that you have created.
        
        @description    By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        You can call this operation up to three times per second per account.
        
        @param request: DescribeCdnSubListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnSubListResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def describe_cdn_sub_list(self) -> cdn_20180510_models.DescribeCdnSubListResponse:
        """
        @summary Queries the tracking tasks that you have created.
        
        @description    By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        You can call this operation up to three times per second per account.
        
        @return: DescribeCdnSubListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_sub_list_with_options(runtime)

    async def describe_cdn_sub_list_async(self) -> cdn_20180510_models.DescribeCdnSubListResponse:
        """
        @summary Queries the tracking tasks that you have created.
        
        @description    By default, this operation queries all custom operations reports. However, only one operations report can be displayed. Therefore, only one operations report is returned.
        You can call this operation up to three times per second per account.
        
        @return: DescribeCdnSubListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_sub_list_with_options_async(runtime)

    def describe_cdn_user_bill_history_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        """
        @summary Queries the billing history under your Alibaba Cloud account.
        
        @description    You can query billing history up to the last one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillHistoryResponse
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
        """
        @summary Queries the billing history under your Alibaba Cloud account.
        
        @description    You can query billing history up to the last one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillHistoryResponse
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
        """
        @summary Queries the billing history under your Alibaba Cloud account.
        
        @description    You can query billing history up to the last one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillHistoryRequest
        @return: DescribeCdnUserBillHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_history_with_options(request, runtime)

    async def describe_cdn_user_bill_history_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        """
        @summary Queries the billing history under your Alibaba Cloud account.
        
        @description    You can query billing history up to the last one month.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillHistoryRequest
        @return: DescribeCdnUserBillHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_history_with_options_async(request, runtime)

    def describe_cdn_user_bill_prediction_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        """
        @summary Estimates resource usage of the current month.
        
        @description You can call this operation to estimate resource usage of the current month based on the metering method that is specified on the first day of the current month. You can call this operation to estimate resource usage only of the current month within your Alibaba Cloud account. The time range used for the estimation starts at 00:00 on the first day of the current month and ends 2 hours earlier than the current time.
        Pay by monthly 95th percentile: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        Pay by average daily peak bandwidth per month: Estimated value = Sum of daily peak bandwidth values/Number of days. The current day is excluded.
        Pay by 4th peak bandwidth per month: The estimated value is the 4th peak bandwidth value between the start time and end time. If the time range is less than four days, the estimated value is 0.
        Pay by average daily 95th percentile bandwidth per month: Estimated value = Sum of daily 95th percentile bandwidth values/Number of days. The current day is excluded.
        Pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        > You can call this operation only once per second per account.
        
        @param request: DescribeCdnUserBillPredictionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillPredictionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Estimates resource usage of the current month.
        
        @description You can call this operation to estimate resource usage of the current month based on the metering method that is specified on the first day of the current month. You can call this operation to estimate resource usage only of the current month within your Alibaba Cloud account. The time range used for the estimation starts at 00:00 on the first day of the current month and ends 2 hours earlier than the current time.
        Pay by monthly 95th percentile: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        Pay by average daily peak bandwidth per month: Estimated value = Sum of daily peak bandwidth values/Number of days. The current day is excluded.
        Pay by 4th peak bandwidth per month: The estimated value is the 4th peak bandwidth value between the start time and end time. If the time range is less than four days, the estimated value is 0.
        Pay by average daily 95th percentile bandwidth per month: Estimated value = Sum of daily 95th percentile bandwidth values/Number of days. The current day is excluded.
        Pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        > You can call this operation only once per second per account.
        
        @param request: DescribeCdnUserBillPredictionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillPredictionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Estimates resource usage of the current month.
        
        @description You can call this operation to estimate resource usage of the current month based on the metering method that is specified on the first day of the current month. You can call this operation to estimate resource usage only of the current month within your Alibaba Cloud account. The time range used for the estimation starts at 00:00 on the first day of the current month and ends 2 hours earlier than the current time.
        Pay by monthly 95th percentile: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        Pay by average daily peak bandwidth per month: Estimated value = Sum of daily peak bandwidth values/Number of days. The current day is excluded.
        Pay by 4th peak bandwidth per month: The estimated value is the 4th peak bandwidth value between the start time and end time. If the time range is less than four days, the estimated value is 0.
        Pay by average daily 95th percentile bandwidth per month: Estimated value = Sum of daily 95th percentile bandwidth values/Number of days. The current day is excluded.
        Pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        > You can call this operation only once per second per account.
        
        @param request: DescribeCdnUserBillPredictionRequest
        @return: DescribeCdnUserBillPredictionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_prediction_with_options(request, runtime)

    async def describe_cdn_user_bill_prediction_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        """
        @summary Estimates resource usage of the current month.
        
        @description You can call this operation to estimate resource usage of the current month based on the metering method that is specified on the first day of the current month. You can call this operation to estimate resource usage only of the current month within your Alibaba Cloud account. The time range used for the estimation starts at 00:00 on the first day of the current month and ends 2 hours earlier than the current time.
        Pay by monthly 95th percentile: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        Pay by average daily peak bandwidth per month: Estimated value = Sum of daily peak bandwidth values/Number of days. The current day is excluded.
        Pay by 4th peak bandwidth per month: The estimated value is the 4th peak bandwidth value between the start time and end time. If the time range is less than four days, the estimated value is 0.
        Pay by average daily 95th percentile bandwidth per month: Estimated value = Sum of daily 95th percentile bandwidth values/Number of days. The current day is excluded.
        Pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00: The top 5% values between the start time and end time are excluded. The estimated value is the highest value among the remaining values.
        > You can call this operation only once per second per account.
        
        @param request: DescribeCdnUserBillPredictionRequest
        @return: DescribeCdnUserBillPredictionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_prediction_with_options_async(request, runtime)

    def describe_cdn_user_bill_type_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
        """
        @summary Queries information about the metering methods of an account. The maximum time range to query is one month.
        
        @description    You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillTypeResponse
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
        """
        @summary Queries information about the metering methods of an account. The maximum time range to query is one month.
        
        @description    You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserBillTypeResponse
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
        """
        @summary Queries information about the metering methods of an account. The maximum time range to query is one month.
        
        @description    You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillTypeRequest
        @return: DescribeCdnUserBillTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_type_with_options(request, runtime)

    async def describe_cdn_user_bill_type_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
        """
        @summary Queries information about the metering methods of an account. The maximum time range to query is one month.
        
        @description    You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCdnUserBillTypeRequest
        @return: DescribeCdnUserBillTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_bill_type_with_options_async(request, runtime)

    def describe_cdn_user_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        """
        @summary Queries configurations of security features.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
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
        """
        @summary Queries configurations of security features.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
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
        """
        @summary Queries configurations of security features.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserConfigsRequest
        @return: DescribeCdnUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_configs_with_options(request, runtime)

    async def describe_cdn_user_configs_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        """
        @summary Queries configurations of security features.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserConfigsRequest
        @return: DescribeCdnUserConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_configs_with_options_async(request, runtime)

    def describe_cdn_user_domains_by_func_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        """
        @summary Queries accelerated domain names that have specified features configured and the status of the domain names.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeCdnUserDomainsByFuncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserDomainsByFuncResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries accelerated domain names that have specified features configured and the status of the domain names.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeCdnUserDomainsByFuncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserDomainsByFuncResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries accelerated domain names that have specified features configured and the status of the domain names.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeCdnUserDomainsByFuncRequest
        @return: DescribeCdnUserDomainsByFuncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_domains_by_func_with_options(request, runtime)

    async def describe_cdn_user_domains_by_func_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        """
        @summary Queries accelerated domain names that have specified features configured and the status of the domain names.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DescribeCdnUserDomainsByFuncRequest
        @return: DescribeCdnUserDomainsByFuncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_cdn_user_quota_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
        """
        @summary Queries the quotas and usage of Alibaba Cloud CDN resources.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserQuotaResponse
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
        """
        @summary Queries the quotas and usage of Alibaba Cloud CDN resources.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserQuotaResponse
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
        """
        @summary Queries the quotas and usage of Alibaba Cloud CDN resources.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserQuotaRequest
        @return: DescribeCdnUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_quota_with_options(request, runtime)

    async def describe_cdn_user_quota_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
        """
        @summary Queries the quotas and usage of Alibaba Cloud CDN resources.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserQuotaRequest
        @return: DescribeCdnUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_quota_with_options_async(request, runtime)

    def describe_cdn_user_resource_package_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
        """
        @summary Queries the resource plans that you have purchased for Alibaba Cloud CDN.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserResourcePackageResponse
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
        """
        @summary Queries the resource plans that you have purchased for Alibaba Cloud CDN.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnUserResourcePackageResponse
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
        """
        @summary Queries the resource plans that you have purchased for Alibaba Cloud CDN.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserResourcePackageRequest
        @return: DescribeCdnUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_resource_package_with_options(request, runtime)

    async def describe_cdn_user_resource_package_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
        """
        @summary Queries the resource plans that you have purchased for Alibaba Cloud CDN.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeCdnUserResourcePackageRequest
        @return: DescribeCdnUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_user_resource_package_with_options_async(request, runtime)

    def describe_cdn_waf_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
        """
        @summary Queries domain names that use Web Application Firewall (WAF).
        
        @description > You can call this operation up to 150 times per second per account.
        
        @param request: DescribeCdnWafDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnWafDomainResponse
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
        """
        @summary Queries domain names that use Web Application Firewall (WAF).
        
        @description > You can call this operation up to 150 times per second per account.
        
        @param request: DescribeCdnWafDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCdnWafDomainResponse
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
        """
        @summary Queries domain names that use Web Application Firewall (WAF).
        
        @description > You can call this operation up to 150 times per second per account.
        
        @param request: DescribeCdnWafDomainRequest
        @return: DescribeCdnWafDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_waf_domain_with_options(request, runtime)

    async def describe_cdn_waf_domain_async(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
        """
        @summary Queries domain names that use Web Application Firewall (WAF).
        
        @description > You can call this operation up to 150 times per second per account.
        
        @param request: DescribeCdnWafDomainRequest
        @return: DescribeCdnWafDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_waf_domain_with_options_async(request, runtime)

    def describe_certificate_info_by_idwith_options(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        """
        @summary Queries the information about a specific certificate by certificate ID.
        
        @description    You can call this operation up to 100 times per second per account.
        If a certificate is associated with a domain name but the certificate is not enabled, the result of this operation shows that the certificate does not exist.
        
        @param request: DescribeCertificateInfoByIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateInfoByIDResponse
        """
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
        """
        @summary Queries the information about a specific certificate by certificate ID.
        
        @description    You can call this operation up to 100 times per second per account.
        If a certificate is associated with a domain name but the certificate is not enabled, the result of this operation shows that the certificate does not exist.
        
        @param request: DescribeCertificateInfoByIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateInfoByIDResponse
        """
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
        """
        @summary Queries the information about a specific certificate by certificate ID.
        
        @description    You can call this operation up to 100 times per second per account.
        If a certificate is associated with a domain name but the certificate is not enabled, the result of this operation shows that the certificate does not exist.
        
        @param request: DescribeCertificateInfoByIDRequest
        @return: DescribeCertificateInfoByIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_info_by_idwith_options(request, runtime)

    async def describe_certificate_info_by_id_async(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        """
        @summary Queries the information about a specific certificate by certificate ID.
        
        @description    You can call this operation up to 100 times per second per account.
        If a certificate is associated with a domain name but the certificate is not enabled, the result of this operation shows that the certificate does not exist.
        
        @param request: DescribeCertificateInfoByIDRequest
        @return: DescribeCertificateInfoByIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_info_by_idwith_options_async(request, runtime)

    def describe_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        """
        @summary Queries the details about a custom logging configuration.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLogConfigResponse
        """
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
        """
        @summary Queries the details about a custom logging configuration.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomLogConfigResponse
        """
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
        """
        @summary Queries the details about a custom logging configuration.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCustomLogConfigRequest
        @return: DescribeCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_log_config_with_options(request, runtime)

    async def describe_custom_log_config_async(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        """
        @summary Queries the details about a custom logging configuration.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeCustomLogConfigRequest
        @return: DescribeCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_log_config_with_options_async(request, runtime)

    def describe_domain_average_response_time_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        """
        @summary Queries the average response time of one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        >   You can specify up to 500 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeDomainAverageResponseTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAverageResponseTimeResponse
        """
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
        """
        @summary Queries the average response time of one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        >   You can specify up to 500 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeDomainAverageResponseTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAverageResponseTimeResponse
        """
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
        """
        @summary Queries the average response time of one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        >   You can specify up to 500 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeDomainAverageResponseTimeRequest
        @return: DescribeDomainAverageResponseTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_average_response_time_with_options(request, runtime)

    async def describe_domain_average_response_time_async(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        """
        @summary Queries the average response time of one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        >   You can specify up to 500 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeDomainAverageResponseTimeRequest
        @return: DescribeDomainAverageResponseTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_average_response_time_with_options_async(request, runtime)

    def describe_domain_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
        """
        @summary Queries bandwidth monitoring data for one or more accelerated domain names.
        
        @description  You can call this operation up to 150 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataResponse
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
        """
        @summary Queries bandwidth monitoring data for one or more accelerated domain names.
        
        @description  You can call this operation up to 150 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataResponse
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
        """
        @summary Queries bandwidth monitoring data for one or more accelerated domain names.
        
        @description  You can call this operation up to 150 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataRequest
        @return: DescribeDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_with_options(request, runtime)

    async def describe_domain_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
        """
        @summary Queries bandwidth monitoring data for one or more accelerated domain names.
        
        @description  You can call this operation up to 150 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataRequest
        @return: DescribeDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_with_options_async(request, runtime)

    def describe_domain_bps_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
        """
        @summary Queries bandwidth data by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataByLayerResponse
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
        """
        @summary Queries bandwidth data by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataByLayerResponse
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
        """
        @summary Queries bandwidth data by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataByLayerRequest
        @return: DescribeDomainBpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_domain_bps_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
        """
        @summary Queries bandwidth data by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainBpsDataByLayerRequest
        @return: DescribeDomainBpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_bps_data_by_time_stamp_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        """
        @summary Queries the bandwidth data at a specified time for an accelerated domain.
        
        @description    The bandwidth is measured in bit/s.
        You can specify only one accelerated domain name in each request.
        The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainBpsDataByTimeStampRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataByTimeStampResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
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
        """
        @summary Queries the bandwidth data at a specified time for an accelerated domain.
        
        @description    The bandwidth is measured in bit/s.
        You can specify only one accelerated domain name in each request.
        The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainBpsDataByTimeStampRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBpsDataByTimeStampResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
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
        """
        @summary Queries the bandwidth data at a specified time for an accelerated domain.
        
        @description    The bandwidth is measured in bit/s.
        You can specify only one accelerated domain name in each request.
        The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainBpsDataByTimeStampRequest
        @return: DescribeDomainBpsDataByTimeStampResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_time_stamp_with_options(request, runtime)

    async def describe_domain_bps_data_by_time_stamp_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        """
        @summary Queries the bandwidth data at a specified time for an accelerated domain.
        
        @description    The bandwidth is measured in bit/s.
        You can specify only one accelerated domain name in each request.
        The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainBpsDataByTimeStampRequest
        @return: DescribeDomainBpsDataByTimeStampResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_by_time_stamp_with_options_async(request, runtime)

    def describe_domain_cc_activity_log_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
        """
        @summary Queries log entries of rate limiting.
        
        @description    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        You can specify up to 20 domain names in reach request. If you specify multiple domain names, separate them with commas (,).
        You can query data collected over the last 30 days.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainCcActivityLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCcActivityLogResponse
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
        """
        @summary Queries log entries of rate limiting.
        
        @description    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        You can specify up to 20 domain names in reach request. If you specify multiple domain names, separate them with commas (,).
        You can query data collected over the last 30 days.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainCcActivityLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCcActivityLogResponse
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
        """
        @summary Queries log entries of rate limiting.
        
        @description    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        You can specify up to 20 domain names in reach request. If you specify multiple domain names, separate them with commas (,).
        You can query data collected over the last 30 days.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainCcActivityLogRequest
        @return: DescribeDomainCcActivityLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_cc_activity_log_with_options(request, runtime)

    async def describe_domain_cc_activity_log_async(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
        """
        @summary Queries log entries of rate limiting.
        
        @description    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range. You must set both parameters or leave both parameters empty.
        You can specify up to 20 domain names in reach request. If you specify multiple domain names, separate them with commas (,).
        You can query data collected over the last 30 days.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainCcActivityLogRequest
        @return: DescribeDomainCcActivityLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_cc_activity_log_with_options_async(request, runtime)

    def describe_domain_certificate_info_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
        """
        @summary Queries the certificate information of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Queries the certificate information of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Queries the certificate information of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCertificateInfoRequest
        @return: DescribeDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_certificate_info_with_options(request, runtime)

    async def describe_domain_certificate_info_async(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
        """
        @summary Queries the certificate information of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCertificateInfoRequest
        @return: DescribeDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_certificate_info_with_options_async(request, runtime)

    def describe_domain_cname_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCnameResponse:
        """
        @summary Detects the CNAME for an accelerated domain name. You can check the resolution result to determine whether the CNAME is configured.
        
        @param request: DescribeDomainCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCname',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_cname_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCnameResponse:
        """
        @summary Detects the CNAME for an accelerated domain name. You can check the resolution result to determine whether the CNAME is configured.
        
        @param request: DescribeDomainCnameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCname',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_cname(
        self,
        request: cdn_20180510_models.DescribeDomainCnameRequest,
    ) -> cdn_20180510_models.DescribeDomainCnameResponse:
        """
        @summary Detects the CNAME for an accelerated domain name. You can check the resolution result to determine whether the CNAME is configured.
        
        @param request: DescribeDomainCnameRequest
        @return: DescribeDomainCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_cname_with_options(request, runtime)

    async def describe_domain_cname_async(
        self,
        request: cdn_20180510_models.DescribeDomainCnameRequest,
    ) -> cdn_20180510_models.DescribeDomainCnameResponse:
        """
        @summary Detects the CNAME for an accelerated domain name. You can check the resolution result to determine whether the CNAME is configured.
        
        @param request: DescribeDomainCnameRequest
        @return: DescribeDomainCnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_cname_with_options_async(request, runtime)

    def describe_domain_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        """
        @summary Queries the custom log configuration of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCustomLogConfigResponse
        """
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
        """
        @summary Queries the custom log configuration of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainCustomLogConfigResponse
        """
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
        """
        @summary Queries the custom log configuration of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCustomLogConfigRequest
        @return: DescribeDomainCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_custom_log_config_with_options(request, runtime)

    async def describe_domain_custom_log_config_async(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        """
        @summary Queries the custom log configuration of an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainCustomLogConfigRequest
        @return: DescribeDomainCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_custom_log_config_with_options_async(request, runtime)

    def describe_domain_detail_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        """
        @summary The domain name that you want to query. You can specify multiple domain names and separate them with commas (,). You can specify at most 30 domain names in each call.
        
        @description You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainDetailDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDetailDataByLayerResponse
        """
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
        """
        @summary The domain name that you want to query. You can specify multiple domain names and separate them with commas (,). You can specify at most 30 domain names in each call.
        
        @description You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainDetailDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainDetailDataByLayerResponse
        """
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
        """
        @summary The domain name that you want to query. You can specify multiple domain names and separate them with commas (,). You can specify at most 30 domain names in each call.
        
        @description You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainDetailDataByLayerRequest
        @return: DescribeDomainDetailDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_data_by_layer_with_options(request, runtime)

    async def describe_domain_detail_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        """
        @summary The domain name that you want to query. You can specify multiple domain names and separate them with commas (,). You can specify at most 30 domain names in each call.
        
        @description You can call this operation up to 20 times per second per account.
        
        @param request: DescribeDomainDetailDataByLayerRequest
        @return: DescribeDomainDetailDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_detail_data_by_layer_with_options_async(request, runtime)

    def describe_domain_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
        """
        @summary Queries byte hit ratios that are measured in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHitRateDataResponse
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
        """
        @summary Queries byte hit ratios that are measured in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHitRateDataResponse
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
        """
        @summary Queries byte hit ratios that are measured in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHitRateDataRequest
        @return: DescribeDomainHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_hit_rate_data_with_options(request, runtime)

    async def describe_domain_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
        """
        @summary Queries byte hit ratios that are measured in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHitRateDataRequest
        @return: DescribeDomainHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name. The data is collected every 5 minutes.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name. The data is collected every 5 minutes.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name. The data is collected every 5 minutes.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataRequest
        @return: DescribeDomainHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_with_options(request, runtime)

    async def describe_domain_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name. The data is collected every 5 minutes.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataRequest
        @return: DescribeDomainHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_http_code_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
        """
        @summary Queries HTTP status codes by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHttpCodeDataByLayerResponse
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
        """
        @summary Queries HTTP status codes by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainHttpCodeDataByLayerResponse
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
        """
        @summary Queries HTTP status codes by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataByLayerRequest
        @return: DescribeDomainHttpCodeDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_by_layer_with_options(request, runtime)

    async def describe_domain_http_code_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
        """
        @summary Queries HTTP status codes by protocol.
        
        @description  You can call this operation up to 20 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainHttpCodeDataByLayerRequest
        @return: DescribeDomainHttpCodeDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_http_code_data_by_layer_with_options_async(request, runtime)

    def describe_domain_ispdata_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
        """
        @summary Queries the proportions of data usage of different Internet service providers (ISPs). Data is collected every day. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set StartTime or EndTime, the request returns the data collected in the last 24 hours. If you set both StartTime and EndTime, the request returns the data collected within the specified time range.
        >   This operation queries proportions of data usage of different ISPs for only a specific accelerated domain name, or for all accelerated domain names in your Alibaba Cloud account.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainISPDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainISPDataResponse
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
        """
        @summary Queries the proportions of data usage of different Internet service providers (ISPs). Data is collected every day. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set StartTime or EndTime, the request returns the data collected in the last 24 hours. If you set both StartTime and EndTime, the request returns the data collected within the specified time range.
        >   This operation queries proportions of data usage of different ISPs for only a specific accelerated domain name, or for all accelerated domain names in your Alibaba Cloud account.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainISPDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainISPDataResponse
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
        """
        @summary Queries the proportions of data usage of different Internet service providers (ISPs). Data is collected every day. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set StartTime or EndTime, the request returns the data collected in the last 24 hours. If you set both StartTime and EndTime, the request returns the data collected within the specified time range.
        >   This operation queries proportions of data usage of different ISPs for only a specific accelerated domain name, or for all accelerated domain names in your Alibaba Cloud account.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainISPDataRequest
        @return: DescribeDomainISPDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ispdata_with_options(request, runtime)

    async def describe_domain_ispdata_async(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
        """
        @summary Queries the proportions of data usage of different Internet service providers (ISPs). Data is collected every day. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set StartTime or EndTime, the request returns the data collected in the last 24 hours. If you set both StartTime and EndTime, the request returns the data collected within the specified time range.
        >   This operation queries proportions of data usage of different ISPs for only a specific accelerated domain name, or for all accelerated domain names in your Alibaba Cloud account.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainISPDataRequest
        @return: DescribeDomainISPDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_ispdata_with_options_async(request, runtime)

    def describe_domain_max_95bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        """
        @summary Queries the 95th percentile bandwidth data of a domain name.
        
        @description *You can use one of the following methods to query data:**\
        If you specify the StartTime and EndTime parameters and the time range that is specified by these parameters is less than or equal to 24 hours, the 95th percentile bandwidth data on the day of the start time is returned. If the time range that is specified by these parameters is more than 24 hours, the 95th percentile bandwidth data in the month of the start time is returned.
        If you specify the TimePoint and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you specify the StartTime, EndTime, and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you do not use one of the methods, the 95th percentile bandwidth data of the previous 24 hours is returned by default.
        Maximum time range to query: 90 days
        Minimum data granularity to query: 1 day
        Historical data available: 90 days
        - You can call this operation up to 100 times per second per account.
        - The unit of the bandwidth data returned is bit/s.
        
        @param request: DescribeDomainMax95BpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainMax95BpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the 95th percentile bandwidth data of a domain name.
        
        @description *You can use one of the following methods to query data:**\
        If you specify the StartTime and EndTime parameters and the time range that is specified by these parameters is less than or equal to 24 hours, the 95th percentile bandwidth data on the day of the start time is returned. If the time range that is specified by these parameters is more than 24 hours, the 95th percentile bandwidth data in the month of the start time is returned.
        If you specify the TimePoint and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you specify the StartTime, EndTime, and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you do not use one of the methods, the 95th percentile bandwidth data of the previous 24 hours is returned by default.
        Maximum time range to query: 90 days
        Minimum data granularity to query: 1 day
        Historical data available: 90 days
        - You can call this operation up to 100 times per second per account.
        - The unit of the bandwidth data returned is bit/s.
        
        @param request: DescribeDomainMax95BpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainMax95BpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the 95th percentile bandwidth data of a domain name.
        
        @description *You can use one of the following methods to query data:**\
        If you specify the StartTime and EndTime parameters and the time range that is specified by these parameters is less than or equal to 24 hours, the 95th percentile bandwidth data on the day of the start time is returned. If the time range that is specified by these parameters is more than 24 hours, the 95th percentile bandwidth data in the month of the start time is returned.
        If you specify the TimePoint and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you specify the StartTime, EndTime, and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you do not use one of the methods, the 95th percentile bandwidth data of the previous 24 hours is returned by default.
        Maximum time range to query: 90 days
        Minimum data granularity to query: 1 day
        Historical data available: 90 days
        - You can call this operation up to 100 times per second per account.
        - The unit of the bandwidth data returned is bit/s.
        
        @param request: DescribeDomainMax95BpsDataRequest
        @return: DescribeDomainMax95BpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_max_95bps_data_with_options(request, runtime)

    async def describe_domain_max_95bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        """
        @summary Queries the 95th percentile bandwidth data of a domain name.
        
        @description *You can use one of the following methods to query data:**\
        If you specify the StartTime and EndTime parameters and the time range that is specified by these parameters is less than or equal to 24 hours, the 95th percentile bandwidth data on the day of the start time is returned. If the time range that is specified by these parameters is more than 24 hours, the 95th percentile bandwidth data in the month of the start time is returned.
        If you specify the TimePoint and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you specify the StartTime, EndTime, and Cycle parameters, the 95th percentile bandwidth data of the cycle is returned.
        If you do not use one of the methods, the 95th percentile bandwidth data of the previous 24 hours is returned by default.
        Maximum time range to query: 90 days
        Minimum data granularity to query: 1 day
        Historical data available: 90 days
        - You can call this operation up to 100 times per second per account.
        - The unit of the bandwidth data returned is bit/s.
        
        @param request: DescribeDomainMax95BpsDataRequest
        @return: DescribeDomainMax95BpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_max_95bps_data_with_options_async(request, runtime)

    def describe_domain_multi_usage_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
        """
        @summary Queries the traffic data and the number of requests for multiple accelerated domain names at a time.
        
        @description    If you do not set StartTime or EndTime, data collected within the last 10 minutes is queried.
        The maximum interval between StartTime and EndTime is 1 hour.
        You can query data within the last 90 days.
        You can query the traffic data and the number of requests for accelerated domain names that are deleted.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainMultiUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainMultiUsageDataResponse
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
        """
        @summary Queries the traffic data and the number of requests for multiple accelerated domain names at a time.
        
        @description    If you do not set StartTime or EndTime, data collected within the last 10 minutes is queried.
        The maximum interval between StartTime and EndTime is 1 hour.
        You can query data within the last 90 days.
        You can query the traffic data and the number of requests for accelerated domain names that are deleted.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainMultiUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainMultiUsageDataResponse
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
        """
        @summary Queries the traffic data and the number of requests for multiple accelerated domain names at a time.
        
        @description    If you do not set StartTime or EndTime, data collected within the last 10 minutes is queried.
        The maximum interval between StartTime and EndTime is 1 hour.
        You can query data within the last 90 days.
        You can query the traffic data and the number of requests for accelerated domain names that are deleted.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainMultiUsageDataRequest
        @return: DescribeDomainMultiUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_multi_usage_data_with_options(request, runtime)

    async def describe_domain_multi_usage_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainMultiUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainMultiUsageDataResponse:
        """
        @summary Queries the traffic data and the number of requests for multiple accelerated domain names at a time.
        
        @description    If you do not set StartTime or EndTime, data collected within the last 10 minutes is queried.
        The maximum interval between StartTime and EndTime is 1 hour.
        You can query data within the last 90 days.
        You can query the traffic data and the number of requests for accelerated domain names that are deleted.
        You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainMultiUsageDataRequest
        @return: DescribeDomainMultiUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_domain_path_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        """
        @summary Queries monitoring data including the amount of network traffic and the number of visits by directory.
        
        @description    This operation is available only to users that are on the whitelist. If the daily peak bandwidth value of your workloads reaches 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply to be included in the whitelist.
        You can call this API operation up to 6,000 times per second per account.
        Data collection by directory is available only to specified domain names within your Alibaba Cloud account. It cannot be enabled for all domain names within your Alibaba Cloud account.
        The average size of the files that belong to the domain name must be larger than 1 MB.
        The number of directories specified for a single domain name cannot exceed 100. If the number of directories exceeds 100, the data accuracy reduces.
        If you do not set StartTime or EndTime, data collected within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query data collected within the last 30 days.
        
        @param request: DescribeDomainPathDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainPathDataResponse
        """
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
        """
        @summary Queries monitoring data including the amount of network traffic and the number of visits by directory.
        
        @description    This operation is available only to users that are on the whitelist. If the daily peak bandwidth value of your workloads reaches 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply to be included in the whitelist.
        You can call this API operation up to 6,000 times per second per account.
        Data collection by directory is available only to specified domain names within your Alibaba Cloud account. It cannot be enabled for all domain names within your Alibaba Cloud account.
        The average size of the files that belong to the domain name must be larger than 1 MB.
        The number of directories specified for a single domain name cannot exceed 100. If the number of directories exceeds 100, the data accuracy reduces.
        If you do not set StartTime or EndTime, data collected within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query data collected within the last 30 days.
        
        @param request: DescribeDomainPathDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainPathDataResponse
        """
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
        """
        @summary Queries monitoring data including the amount of network traffic and the number of visits by directory.
        
        @description    This operation is available only to users that are on the whitelist. If the daily peak bandwidth value of your workloads reaches 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply to be included in the whitelist.
        You can call this API operation up to 6,000 times per second per account.
        Data collection by directory is available only to specified domain names within your Alibaba Cloud account. It cannot be enabled for all domain names within your Alibaba Cloud account.
        The average size of the files that belong to the domain name must be larger than 1 MB.
        The number of directories specified for a single domain name cannot exceed 100. If the number of directories exceeds 100, the data accuracy reduces.
        If you do not set StartTime or EndTime, data collected within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query data collected within the last 30 days.
        
        @param request: DescribeDomainPathDataRequest
        @return: DescribeDomainPathDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_path_data_with_options(request, runtime)

    async def describe_domain_path_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        """
        @summary Queries monitoring data including the amount of network traffic and the number of visits by directory.
        
        @description    This operation is available only to users that are on the whitelist. If the daily peak bandwidth value of your workloads reaches 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply to be included in the whitelist.
        You can call this API operation up to 6,000 times per second per account.
        Data collection by directory is available only to specified domain names within your Alibaba Cloud account. It cannot be enabled for all domain names within your Alibaba Cloud account.
        The average size of the files that belong to the domain name must be larger than 1 MB.
        The number of directories specified for a single domain name cannot exceed 100. If the number of directories exceeds 100, the data accuracy reduces.
        If you do not set StartTime or EndTime, data collected within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query data collected within the last 30 days.
        
        @param request: DescribeDomainPathDataRequest
        @return: DescribeDomainPathDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_path_data_with_options_async(request, runtime)

    def describe_domain_pv_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
        """
        @summary Queries the page view (PV) data of an accelerated domain name. The data is collected at an interval of 1 hour. You can query data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainPvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainPvDataResponse
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
        """
        @summary Queries the page view (PV) data of an accelerated domain name. The data is collected at an interval of 1 hour. You can query data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainPvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainPvDataResponse
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
        """
        @summary Queries the page view (PV) data of an accelerated domain name. The data is collected at an interval of 1 hour. You can query data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainPvDataRequest
        @return: DescribeDomainPvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_pv_data_with_options(request, runtime)

    async def describe_domain_pv_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
        """
        @summary Queries the page view (PV) data of an accelerated domain name. The data is collected at an interval of 1 hour. You can query data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 50 times per second per account.
        
        @param request: DescribeDomainPvDataRequest
        @return: DescribeDomainPvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_pv_data_with_options_async(request, runtime)

    def describe_domain_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
        """
        @summary Queries the number of queries per second (QPS) for an accelerated domain name. The data is collected every 5 minutes. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsDataResponse
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
        """
        @summary Queries the number of queries per second (QPS) for an accelerated domain name. The data is collected every 5 minutes. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsDataResponse
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
        """
        @summary Queries the number of queries per second (QPS) for an accelerated domain name. The data is collected every 5 minutes. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataRequest
        @return: DescribeDomainQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_with_options(request, runtime)

    async def describe_domain_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
        """
        @summary Queries the number of queries per second (QPS) for an accelerated domain name. The data is collected every 5 minutes. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataRequest
        @return: DescribeDomainQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_data_with_options_async(request, runtime)

    def describe_domain_qps_data_by_layer_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
        """
        @summary Queries the number of queries per second (QPS) at a specific layer for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 20 times per second per user.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsDataByLayerResponse
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
        """
        @summary Queries the number of queries per second (QPS) at a specific layer for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 20 times per second per user.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataByLayerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainQpsDataByLayerResponse
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
        """
        @summary Queries the number of queries per second (QPS) at a specific layer for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 20 times per second per user.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataByLayerRequest
        @return: DescribeDomainQpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_by_layer_with_options(request, runtime)

    async def describe_domain_qps_data_by_layer_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
        """
        @summary Queries the number of queries per second (QPS) at a specific layer for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description  You can call this operation up to 20 times per second per user.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainQpsDataByLayerRequest
        @return: DescribeDomainQpsDataByLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_data_by_layer_with_options_async(request, runtime)

    def describe_domain_real_time_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        """
        @summary Queries the bandwidth data about one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeBpsDataResponse
        """
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
        """
        @summary Queries the bandwidth data about one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeBpsDataResponse
        """
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
        """
        @summary Queries the bandwidth data about one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeBpsDataRequest
        @return: DescribeDomainRealTimeBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        """
        @summary Queries the bandwidth data about one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity** The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeBpsDataRequest
        @return: DescribeDomainRealTimeBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        """
        @summary Queries the byte hit ratios of accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeByteHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeByteHitRateDataResponse
        """
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
        """
        @summary Queries the byte hit ratios of accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeByteHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeByteHitRateDataResponse
        """
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
        """
        @summary Queries the byte hit ratios of accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeByteHitRateDataRequest
        @return: DescribeDomainRealTimeByteHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_byte_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        """
        @summary Queries the byte hit ratios of accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the byte hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeByteHitRateDataRequest
        @return: DescribeDomainRealTimeByteHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_detail_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        """
        @summary Queries the real-time monitoring data for a domain name.
        
        @description    You can query data in the last seven days. Data is collected every minute.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainRealTimeDetailDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeDetailDataResponse
        """
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
        """
        @summary Queries the real-time monitoring data for a domain name.
        
        @description    You can query data in the last seven days. Data is collected every minute.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainRealTimeDetailDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeDetailDataResponse
        """
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
        """
        @summary Queries the real-time monitoring data for a domain name.
        
        @description    You can query data in the last seven days. Data is collected every minute.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainRealTimeDetailDataRequest
        @return: DescribeDomainRealTimeDetailDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_domain_real_time_detail_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        """
        @summary Queries the real-time monitoring data for a domain name.
        
        @description    You can query data in the last seven days. Data is collected every minute.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainRealTimeDetailDataRequest
        @return: DescribeDomainRealTimeDetailDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_domain_real_time_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeHttpCodeDataRequest
        @return: DescribeDomainRealTimeHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned from an accelerated domain name.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeHttpCodeDataRequest
        @return: DescribeDomainRealTimeHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        """
        @summary Queries the number of queries per second for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeQpsDataResponse
        """
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
        """
        @summary Queries the number of queries per second for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeQpsDataResponse
        """
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
        """
        @summary Queries the number of queries per second for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeQpsDataRequest
        @return: DescribeDomainRealTimeQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_domain_real_time_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        """
        @summary Queries the number of queries per second for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeQpsDataRequest
        @return: DescribeDomainRealTimeQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        """
        @summary Queries the request hit ratios for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        By default, requests in the Go programming language use the POST request method. You must manually change the request method to GET by declaring: request.Method="GET".
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the request hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeReqHitRateDataResponse
        """
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
        """
        @summary Queries the request hit ratios for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        By default, requests in the Go programming language use the POST request method. You must manually change the request method to GET by declaring: request.Method="GET".
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the request hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeReqHitRateDataResponse
        """
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
        """
        @summary Queries the request hit ratios for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        By default, requests in the Go programming language use the POST request method. You must manually change the request method to GET by declaring: request.Method="GET".
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the request hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeReqHitRateDataRequest
        @return: DescribeDomainRealTimeReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_real_time_req_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        """
        @summary Queries the request hit ratios for one or more accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        By default, requests in the Go programming language use the POST request method. You must manually change the request method to GET by declaring: request.Method="GET".
        The network traffic destined for different domain names may be redirected to the same origin server. Therefore, the request hit ratios may be inaccurate. The accuracy of query results is based on the actual configurations.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeReqHitRateDataRequest
        @return: DescribeDomainRealTimeReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
        """
        @summary Queries origin bandwidth data for accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcBpsDataResponse
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
        """
        @summary Queries origin bandwidth data for accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcBpsDataResponse
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
        """
        @summary Queries origin bandwidth data for accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcBpsDataRequest
        @return: DescribeDomainRealTimeSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_domain_real_time_src_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
        """
        @summary Queries origin bandwidth data for accelerated domain names.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcBpsDataRequest
        @return: DescribeDomainRealTimeSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned during back-to-origin routing.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned during back-to-origin routing.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcHttpCodeDataResponse
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
        """
        @summary Queries the total number and proportions of HTTP status codes returned during back-to-origin routing.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcHttpCodeDataRequest
        @return: DescribeDomainRealTimeSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_domain_real_time_src_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        """
        @summary Queries the total number and proportions of HTTP status codes returned during back-to-origin routing.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you set both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcHttpCodeDataRequest
        @return: DescribeDomainRealTimeSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_real_time_src_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        """
        @summary Queries the monitoring data of back-to-origin traffic for one or more specified accelerated domains. The data is collected every minute.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour by default. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcTrafficDataResponse
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
        """
        @summary Queries the monitoring data of back-to-origin traffic for one or more specified accelerated domains. The data is collected every minute.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour by default. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeSrcTrafficDataResponse
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
        """
        @summary Queries the monitoring data of back-to-origin traffic for one or more specified accelerated domains. The data is collected every minute.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour by default. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcTrafficDataRequest
        @return: DescribeDomainRealTimeSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_src_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        """
        @summary Queries the monitoring data of back-to-origin traffic for one or more specified accelerated domains. The data is collected every minute.
        
        @description  You can call this operation up to 10 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour by default. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeSrcTrafficDataRequest
        @return: DescribeDomainRealTimeSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_real_time_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
        """
        @summary Queries the monitoring data of network traffic for one or more accelerated domain names.
        
        @description  You can call this operation up to 50 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeTrafficDataResponse
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
        """
        @summary Queries the monitoring data of network traffic for one or more accelerated domain names.
        
        @description  You can call this operation up to 50 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealTimeTrafficDataResponse
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
        """
        @summary Queries the monitoring data of network traffic for one or more accelerated domain names.
        
        @description  You can call this operation up to 50 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeTrafficDataRequest
        @return: DescribeDomainRealTimeTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_domain_real_time_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
        """
        @summary Queries the monitoring data of network traffic for one or more accelerated domain names.
        
        @description  You can call this operation up to 50 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last hour. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity varies with the time range specified by the StartTime and EndTime parameters. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |1 minute|1 hour|7 days|5 minutes|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        
        @param request: DescribeDomainRealTimeTrafficDataRequest
        @return: DescribeDomainRealTimeTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_domain_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        """
        @summary Queries the real-time log delivery information about an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealtimeLogDeliveryResponse
        """
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
        """
        @summary Queries the real-time log delivery information about an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRealtimeLogDeliveryResponse
        """
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
        """
        @summary Queries the real-time log delivery information about an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRealtimeLogDeliveryRequest
        @return: DescribeDomainRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_realtime_log_delivery_with_options(request, runtime)

    async def describe_domain_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        """
        @summary Queries the real-time log delivery information about an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRealtimeLogDeliveryRequest
        @return: DescribeDomainRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_realtime_log_delivery_with_options_async(request, runtime)

    def describe_domain_region_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        """
        @summary Queries the geographic distribution of users for a domain name. The data is collected at an interval of one day. You can query the data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you not use this operation because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not specify the **StartTime** or **EndTime** parameter, data collected within the last **24** hours is queried. If you specify both the **StartTime** and **EndTime** parameters, data collected within the specified time range is queried.
        >   There is delay in data collection. If you want to query data collected within the last day, we recommend that you query the data on the next day.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRegionDataResponse
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
        """
        @summary Queries the geographic distribution of users for a domain name. The data is collected at an interval of one day. You can query the data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you not use this operation because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not specify the **StartTime** or **EndTime** parameter, data collected within the last **24** hours is queried. If you specify both the **StartTime** and **EndTime** parameters, data collected within the specified time range is queried.
        >   There is delay in data collection. If you want to query data collected within the last day, we recommend that you query the data on the next day.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRegionDataResponse
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
        """
        @summary Queries the geographic distribution of users for a domain name. The data is collected at an interval of one day. You can query the data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you not use this operation because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not specify the **StartTime** or **EndTime** parameter, data collected within the last **24** hours is queried. If you specify both the **StartTime** and **EndTime** parameters, data collected within the specified time range is queried.
        >   There is delay in data collection. If you want to query data collected within the last day, we recommend that you query the data on the next day.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRegionDataRequest
        @return: DescribeDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_region_data_with_options(request, runtime)

    async def describe_domain_region_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        """
        @summary Queries the geographic distribution of users for a domain name. The data is collected at an interval of one day. You can query the data in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you not use this operation because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not specify the **StartTime** or **EndTime** parameter, data collected within the last **24** hours is queried. If you specify both the **StartTime** and **EndTime** parameters, data collected within the specified time range is queried.
        >   There is delay in data collection. If you want to query data collected within the last day, we recommend that you query the data on the next day.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainRegionDataRequest
        @return: DescribeDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_region_data_with_options_async(request, runtime)

    def describe_domain_req_hit_rate_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
        """
        @summary Queries the request hit ratio in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainReqHitRateDataResponse
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
        """
        @summary Queries the request hit ratio in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainReqHitRateDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainReqHitRateDataResponse
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
        """
        @summary Queries the request hit ratio in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainReqHitRateDataRequest
        @return: DescribeDomainReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_req_hit_rate_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
        """
        @summary Queries the request hit ratio in percentage.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainReqHitRateDataRequest
        @return: DescribeDomainReqHitRateDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_src_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        """
        @summary Queries bandwidth monitoring data of requests that are redirected to origin servers for one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the time range to query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcBpsDataResponse
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
        """
        @summary Queries bandwidth monitoring data of requests that are redirected to origin servers for one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the time range to query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcBpsDataResponse
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
        """
        @summary Queries bandwidth monitoring data of requests that are redirected to origin servers for one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the time range to query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcBpsDataRequest
        @return: DescribeDomainSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_bps_data_with_options(request, runtime)

    async def describe_domain_src_bps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        """
        @summary Queries bandwidth monitoring data of requests that are redirected to origin servers for one or more accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not specify the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you specify both the StartTime and EndTime parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the time range to query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcBpsDataRequest
        @return: DescribeDomainSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_bps_data_with_options_async(request, runtime)

    def describe_domain_src_http_code_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
        """
        @summary Queries the proportions of HTTP status codes that are returned during back-to-origin routing.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcHttpCodeDataResponse
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
        """
        @summary Queries the proportions of HTTP status codes that are returned during back-to-origin routing.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcHttpCodeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcHttpCodeDataResponse
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
        """
        @summary Queries the proportions of HTTP status codes that are returned during back-to-origin routing.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcHttpCodeDataRequest
        @return: DescribeDomainSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_http_code_data_with_options(request, runtime)

    async def describe_domain_src_http_code_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
        """
        @summary Queries the proportions of HTTP status codes that are returned during back-to-origin routing.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter varies with the maximum time range per query. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcHttpCodeDataRequest
        @return: DescribeDomainSrcHttpCodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_http_code_data_with_options_async(request, runtime)

    def describe_domain_src_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
        """
        @summary Queries the number of queries per second (QPS) that are sent to the origin server. You can query data collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcQpsDataResponse
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
        """
        @summary Queries the number of queries per second (QPS) that are sent to the origin server. You can query data collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcQpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcQpsDataResponse
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
        """
        @summary Queries the number of queries per second (QPS) that are sent to the origin server. You can query data collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcQpsDataRequest
        @return: DescribeDomainSrcQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_qps_data_with_options(request, runtime)

    async def describe_domain_src_qps_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
        """
        @summary Queries the number of queries per second (QPS) that are sent to the origin server. You can query data collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        ### Time granularity
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcQpsDataRequest
        @return: DescribeDomainSrcQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_qps_data_with_options_async(request, runtime)

    def describe_domain_src_top_url_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        """
        @summary Queries frequently requested origin URLs of one or more accelerated domain names.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    The data is collected at an interval of 5 minutes.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainSrcTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries frequently requested origin URLs of one or more accelerated domain names.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    The data is collected at an interval of 5 minutes.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainSrcTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries frequently requested origin URLs of one or more accelerated domain names.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    The data is collected at an interval of 5 minutes.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainSrcTopUrlVisitRequest
        @return: DescribeDomainSrcTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_top_url_visit_with_options(request, runtime)

    async def describe_domain_src_top_url_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        """
        @summary Queries frequently requested origin URLs of one or more accelerated domain names.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    The data is collected at an interval of 5 minutes.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainSrcTopUrlVisitRequest
        @return: DescribeDomainSrcTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_top_url_visit_with_options_async(request, runtime)

    def describe_domain_src_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
        """
        @summary Queries origin traffic for one or more specified accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcTrafficDataResponse
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
        """
        @summary Queries origin traffic for one or more specified accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainSrcTrafficDataResponse
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
        """
        @summary Queries origin traffic for one or more specified accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcTrafficDataRequest
        @return: DescribeDomainSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_traffic_data_with_options(request, runtime)

    async def describe_domain_src_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
        """
        @summary Queries origin traffic for one or more specified accelerated domain names.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainSrcTrafficDataRequest
        @return: DescribeDomainSrcTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_traffic_data_with_options_async(request, runtime)

    def describe_domain_top_client_ip_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        """
        @summary Queries client IP addresses that are ranked by the number of requests or the amount of network traffic within a specific time range for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   Data is collected every hour.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopClientIpVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopClientIpVisitResponse
        """
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
        """
        @summary Queries client IP addresses that are ranked by the number of requests or the amount of network traffic within a specific time range for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   Data is collected every hour.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopClientIpVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopClientIpVisitResponse
        """
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
        """
        @summary Queries client IP addresses that are ranked by the number of requests or the amount of network traffic within a specific time range for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   Data is collected every hour.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopClientIpVisitRequest
        @return: DescribeDomainTopClientIpVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_client_ip_visit_with_options(request, runtime)

    async def describe_domain_top_client_ip_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        """
        @summary Queries client IP addresses that are ranked by the number of requests or the amount of network traffic within a specific time range for one or more accelerated domain names. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature to for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   Data is collected every hour.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopClientIpVisitRequest
        @return: DescribeDomainTopClientIpVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_client_ip_visit_with_options_async(request, runtime)

    def describe_domain_top_refer_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        """
        @summary Queries frequently requested web pages of one or more accelerated domain names on a specified day and sorts the web pages. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature or [ship real-time logs in Log Service](https://help.aliyun.com/document_detail/440145.html) to analyze data.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        Data is collected at an interval of five minutes.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopReferVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopReferVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries frequently requested web pages of one or more accelerated domain names on a specified day and sorts the web pages. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature or [ship real-time logs in Log Service](https://help.aliyun.com/document_detail/440145.html) to analyze data.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        Data is collected at an interval of five minutes.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopReferVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopReferVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries frequently requested web pages of one or more accelerated domain names on a specified day and sorts the web pages. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature or [ship real-time logs in Log Service](https://help.aliyun.com/document_detail/440145.html) to analyze data.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        Data is collected at an interval of five minutes.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopReferVisitRequest
        @return: DescribeDomainTopReferVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_refer_visit_with_options(request, runtime)

    async def describe_domain_top_refer_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        """
        @summary Queries frequently requested web pages of one or more accelerated domain names on a specified day and sorts the web pages. You can query data collected within the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature or [ship real-time logs in Log Service](https://help.aliyun.com/document_detail/440145.html) to analyze data.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        Data is collected at an interval of five minutes.
        You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopReferVisitRequest
        @return: DescribeDomainTopReferVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_domain_top_url_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        """
        @summary Queries top 100 frequently requested URLs of an accelerated domain name within a specified time range.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can query data collected in the last 90 days.
        >   You can specify only one domain name in each call.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries top 100 frequently requested URLs of an accelerated domain name within a specified time range.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can query data collected in the last 90 days.
        >   You can specify only one domain name in each call.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopUrlVisitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTopUrlVisitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries top 100 frequently requested URLs of an accelerated domain name within a specified time range.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can query data collected in the last 90 days.
        >   You can specify only one domain name in each call.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopUrlVisitRequest
        @return: DescribeDomainTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_url_visit_with_options(request, runtime)

    async def describe_domain_top_url_visit_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        """
        @summary Queries top 100 frequently requested URLs of an accelerated domain name within a specified time range.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can query data collected in the last 90 days.
        >   You can specify only one domain name in each call.
        >   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeDomainTopUrlVisitRequest
        @return: DescribeDomainTopUrlVisitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_top_url_visit_with_options_async(request, runtime)

    def describe_domain_traffic_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
        """
        @summary Queries network traffic for one or more accelerated domain names. You can query data that is collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366|04:00 on the next day|
        
        @param request: DescribeDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTrafficDataResponse
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
        """
        @summary Queries network traffic for one or more accelerated domain names. You can query data that is collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366|04:00 on the next day|
        
        @param request: DescribeDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainTrafficDataResponse
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
        """
        @summary Queries network traffic for one or more accelerated domain names. You can query data that is collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366|04:00 on the next day|
        
        @param request: DescribeDomainTrafficDataRequest
        @return: DescribeDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_traffic_data_with_options(request, runtime)

    async def describe_domain_traffic_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
        """
        @summary Queries network traffic for one or more accelerated domain names. You can query data that is collected in the last 90 days.
        
        @description  You can call this operation up to 100 times per second per account.
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        *Time granularity**\
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|366 days|366|04:00 on the next day|
        
        @param request: DescribeDomainTrafficDataRequest
        @return: DescribeDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_traffic_data_with_options_async(request, runtime)

    def describe_domain_usage_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
        """
        @summary Queries the resource usage data of specific domain names in a specified billable region.
        
        @description  You can call this operation up to 10 times per second per account.
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|90 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainUsageDataResponse
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
        """
        @summary Queries the resource usage data of specific domain names in a specified billable region.
        
        @description  You can call this operation up to 10 times per second per account.
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|90 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainUsageDataResponse
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
        """
        @summary Queries the resource usage data of specific domain names in a specified billable region.
        
        @description  You can call this operation up to 10 times per second per account.
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|90 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainUsageDataRequest
        @return: DescribeDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    async def describe_domain_usage_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
        """
        @summary Queries the resource usage data of specific domain names in a specified billable region.
        
        @description  You can call this operation up to 10 times per second per account.
        The time granularity supported by the Interval parameter, the maximum time period within which historical data is available, and the data delay vary with the maximum time range per query, as described in the following table.
        |Time granularity|Maximum time range per query|Historical data available|Data delay|
        |---|---|---|---|
        |5 minutes|3 days|93 days|15 minutes|
        |1 hour|31 days|186 days|4 hours|
        |1 day|90 days|366 days|04:00 on the next day|
        
        @param request: DescribeDomainUsageDataRequest
        @return: DescribeDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_usage_data_with_options_async(request, runtime)

    def describe_domain_uv_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
        """
        @summary Queries the unique visitor (UV) data of an accelerated domain name. Data is collected every hour. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        You can specify only one accelerated domain name or all accelerated domain names in your Alibaba Cloud account.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainUvDataResponse
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
        """
        @summary Queries the unique visitor (UV) data of an accelerated domain name. Data is collected every hour. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        You can specify only one accelerated domain name or all accelerated domain names in your Alibaba Cloud account.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainUvDataResponse
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
        """
        @summary Queries the unique visitor (UV) data of an accelerated domain name. Data is collected every hour. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        You can specify only one accelerated domain name or all accelerated domain names in your Alibaba Cloud account.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainUvDataRequest
        @return: DescribeDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_uv_data_with_options(request, runtime)

    async def describe_domain_uv_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
        """
        @summary Queries the unique visitor (UV) data of an accelerated domain name. Data is collected every hour. You can query data collected in the last 90 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >
        If you do not set the StartTime or EndTime parameter, the request returns the data collected in the last 24 hours. If you set both these parameters, the request returns the data collected within the specified time range.
        You can specify only one accelerated domain name or all accelerated domain names in your Alibaba Cloud account.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeDomainUvDataRequest
        @return: DescribeDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_uv_data_with_options_async(request, runtime)

    def describe_domain_verify_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainVerifyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainVerifyDataResponse:
        """
        @summary Queries the verification content of a domain name, including the host record and record value.
        
        @description You can call this operation to query the verification content of an accelerated domain name based on whether the global resource plan is enabled.
        
        @param request: DescribeDomainVerifyDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainVerifyDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.global_resource_plan):
            query['GlobalResourcePlan'] = request.global_resource_plan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainVerifyData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainVerifyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_verify_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainVerifyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainVerifyDataResponse:
        """
        @summary Queries the verification content of a domain name, including the host record and record value.
        
        @description You can call this operation to query the verification content of an accelerated domain name based on whether the global resource plan is enabled.
        
        @param request: DescribeDomainVerifyDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainVerifyDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.global_resource_plan):
            query['GlobalResourcePlan'] = request.global_resource_plan
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainVerifyData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainVerifyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_verify_data(
        self,
        request: cdn_20180510_models.DescribeDomainVerifyDataRequest,
    ) -> cdn_20180510_models.DescribeDomainVerifyDataResponse:
        """
        @summary Queries the verification content of a domain name, including the host record and record value.
        
        @description You can call this operation to query the verification content of an accelerated domain name based on whether the global resource plan is enabled.
        
        @param request: DescribeDomainVerifyDataRequest
        @return: DescribeDomainVerifyDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_verify_data_with_options(request, runtime)

    async def describe_domain_verify_data_async(
        self,
        request: cdn_20180510_models.DescribeDomainVerifyDataRequest,
    ) -> cdn_20180510_models.DescribeDomainVerifyDataResponse:
        """
        @summary Queries the verification content of a domain name, including the host record and record value.
        
        @description You can call this operation to query the verification content of an accelerated domain name based on whether the global resource plan is enabled.
        
        @param request: DescribeDomainVerifyDataRequest
        @return: DescribeDomainVerifyDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_verify_data_with_options_async(request, runtime)

    def describe_domains_by_source_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        """
        @summary Queries accelerated domain names by origin server.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDomainsBySourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsBySourceResponse
        """
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
        """
        @summary Queries accelerated domain names by origin server.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDomainsBySourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsBySourceResponse
        """
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
        """
        @summary Queries accelerated domain names by origin server.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDomainsBySourceRequest
        @return: DescribeDomainsBySourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_by_source_with_options(request, runtime)

    async def describe_domains_by_source_async(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        """
        @summary Queries accelerated domain names by origin server.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeDomainsBySourceRequest
        @return: DescribeDomainsBySourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_by_source_with_options_async(request, runtime)

    def describe_domains_usage_by_day_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        """
        @summary Queries the monitoring data of an accelerated domain name. Data is collected every day. You can query data collected within the last 90 days.
        
        @description    You can call this operation up to 10 times per second per account.
        If you do not set StartTime or EndTime, data within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query the monitoring data of a specific accelerated domain name or all accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDomainsUsageByDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsUsageByDayResponse
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
        """
        @summary Queries the monitoring data of an accelerated domain name. Data is collected every day. You can query data collected within the last 90 days.
        
        @description    You can call this operation up to 10 times per second per account.
        If you do not set StartTime or EndTime, data within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query the monitoring data of a specific accelerated domain name or all accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDomainsUsageByDayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainsUsageByDayResponse
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
        """
        @summary Queries the monitoring data of an accelerated domain name. Data is collected every day. You can query data collected within the last 90 days.
        
        @description    You can call this operation up to 10 times per second per account.
        If you do not set StartTime or EndTime, data within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query the monitoring data of a specific accelerated domain name or all accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDomainsUsageByDayRequest
        @return: DescribeDomainsUsageByDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_usage_by_day_with_options(request, runtime)

    async def describe_domains_usage_by_day_async(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        """
        @summary Queries the monitoring data of an accelerated domain name. Data is collected every day. You can query data collected within the last 90 days.
        
        @description    You can call this operation up to 10 times per second per account.
        If you do not set StartTime or EndTime, data within the last 24 hours is queried. If you set both StartTime and EndTime, data within the specified time range is queried.
        You can query the monitoring data of a specific accelerated domain name or all accelerated domain names that belong to your Alibaba Cloud account.
        
        @param request: DescribeDomainsUsageByDayRequest
        @return: DescribeDomainsUsageByDayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_usage_by_day_with_options_async(request, runtime)

    def describe_es_exception_data_with_options(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
        """
        @summary Queries the execution errors of a script in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExceptionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEsExceptionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the execution errors of a script in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExceptionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEsExceptionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the execution errors of a script in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExceptionDataRequest
        @return: DescribeEsExceptionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_es_exception_data_with_options(request, runtime)

    async def describe_es_exception_data_async(
        self,
        request: cdn_20180510_models.DescribeEsExceptionDataRequest,
    ) -> cdn_20180510_models.DescribeEsExceptionDataResponse:
        """
        @summary Queries the execution errors of a script in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExceptionDataRequest
        @return: DescribeEsExceptionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_es_exception_data_with_options_async(request, runtime)

    def describe_es_execute_data_with_options(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
        """
        @summary Queries the execution status of scripts in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExecuteDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEsExecuteDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the execution status of scripts in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExecuteDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEsExecuteDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        """
        @summary Queries the execution status of scripts in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExecuteDataRequest
        @return: DescribeEsExecuteDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_es_execute_data_with_options(request, runtime)

    async def describe_es_execute_data_async(
        self,
        request: cdn_20180510_models.DescribeEsExecuteDataRequest,
    ) -> cdn_20180510_models.DescribeEsExecuteDataResponse:
        """
        @summary Queries the execution status of scripts in EdgeScript (ES).
        
        @description    You can call this operation up to 30 times per second per account.
        
        @param request: DescribeEsExecuteDataRequest
        @return: DescribeEsExecuteDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_es_execute_data_with_options_async(request, runtime)

    def describe_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        """
        @summary Queries a specified Function Compute trigger.
        
        @param request: DescribeFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFCTriggerResponse
        """
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
        """
        @summary Queries a specified Function Compute trigger.
        
        @param request: DescribeFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFCTriggerResponse
        """
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
        """
        @summary Queries a specified Function Compute trigger.
        
        @param request: DescribeFCTriggerRequest
        @return: DescribeFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_fctrigger_with_options(request, runtime)

    async def describe_fctrigger_async(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        """
        @summary Queries a specified Function Compute trigger.
        
        @param request: DescribeFCTriggerRequest
        @return: DescribeFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_fctrigger_with_options_async(request, runtime)

    def describe_ip_info_with_options(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
        """
        @summary Checks whether a specified IP address is the IP address of a CDN point of presence (POP).
        
        @param request: DescribeIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
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
        """
        @summary Checks whether a specified IP address is the IP address of a CDN point of presence (POP).
        
        @param request: DescribeIpInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
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
        """
        @summary Checks whether a specified IP address is the IP address of a CDN point of presence (POP).
        
        @param request: DescribeIpInfoRequest
        @return: DescribeIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    async def describe_ip_info_async(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
        """
        @summary Checks whether a specified IP address is the IP address of a CDN point of presence (POP).
        
        @param request: DescribeIpInfoRequest
        @return: DescribeIpInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_info_with_options_async(request, runtime)

    def describe_ip_status_with_options(
        self,
        request: cdn_20180510_models.DescribeIpStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpStatusResponse:
        """
        @summary Queries the status of IP addresses of points of presence (POPs). The status of an IP address of a POP indicates whether content delivery acceleration is supported by the POP.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeIpStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpStatus',
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
            cdn_20180510_models.DescribeIpStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_status_with_options_async(
        self,
        request: cdn_20180510_models.DescribeIpStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpStatusResponse:
        """
        @summary Queries the status of IP addresses of points of presence (POPs). The status of an IP address of a POP indicates whether content delivery acceleration is supported by the POP.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeIpStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpStatus',
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
            cdn_20180510_models.DescribeIpStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_status(
        self,
        request: cdn_20180510_models.DescribeIpStatusRequest,
    ) -> cdn_20180510_models.DescribeIpStatusResponse:
        """
        @summary Queries the status of IP addresses of points of presence (POPs). The status of an IP address of a POP indicates whether content delivery acceleration is supported by the POP.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeIpStatusRequest
        @return: DescribeIpStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_status_with_options(request, runtime)

    async def describe_ip_status_async(
        self,
        request: cdn_20180510_models.DescribeIpStatusRequest,
    ) -> cdn_20180510_models.DescribeIpStatusResponse:
        """
        @summary Queries the status of IP addresses of points of presence (POPs). The status of an IP address of a POP indicates whether content delivery acceleration is supported by the POP.
        
        @description > You can call this operation up to 50 times per second per account.
        
        @param request: DescribeIpStatusRequest
        @return: DescribeIpStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_status_with_options_async(request, runtime)

    def describe_l2vips_by_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
        """
        @summary Queries the virtual IP addresses (VIPs) of L2 CDN points of presence (POPs) for a specific domain name.
        
        @description    This operation is available only to users whose daily peak bandwidth value is higher than 1 Gbit/s. If you meet this requirement, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply for permissions to use this operation.
        You can call this operation up to 40 times per second per account.
        
        @param request: DescribeL2VipsByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL2VipsByDomainResponse
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
        """
        @summary Queries the virtual IP addresses (VIPs) of L2 CDN points of presence (POPs) for a specific domain name.
        
        @description    This operation is available only to users whose daily peak bandwidth value is higher than 1 Gbit/s. If you meet this requirement, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply for permissions to use this operation.
        You can call this operation up to 40 times per second per account.
        
        @param request: DescribeL2VipsByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeL2VipsByDomainResponse
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
        """
        @summary Queries the virtual IP addresses (VIPs) of L2 CDN points of presence (POPs) for a specific domain name.
        
        @description    This operation is available only to users whose daily peak bandwidth value is higher than 1 Gbit/s. If you meet this requirement, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply for permissions to use this operation.
        You can call this operation up to 40 times per second per account.
        
        @param request: DescribeL2VipsByDomainRequest
        @return: DescribeL2VipsByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_l2vips_by_domain_with_options(request, runtime)

    async def describe_l2vips_by_domain_async(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
        """
        @summary Queries the virtual IP addresses (VIPs) of L2 CDN points of presence (POPs) for a specific domain name.
        
        @description    This operation is available only to users whose daily peak bandwidth value is higher than 1 Gbit/s. If you meet this requirement, you can [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex) to apply for permissions to use this operation.
        You can call this operation up to 40 times per second per account.
        
        @param request: DescribeL2VipsByDomainRequest
        @return: DescribeL2VipsByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_l2vips_by_domain_with_options_async(request, runtime)

    def describe_preload_detail_by_id_with_options(
        self,
        request: cdn_20180510_models.DescribePreloadDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribePreloadDetailByIdResponse:
        """
        @summary Queries the prefetch details of a task, including the prefetch progress of all resources in the task. Only users who are included in the whitelist can use this operation. You can contact your business manager to apply for the whitelist.
        
        @description    You can query data within the last 3 days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribePreloadDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreloadDetailByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreloadDetailById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribePreloadDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_preload_detail_by_id_with_options_async(
        self,
        request: cdn_20180510_models.DescribePreloadDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribePreloadDetailByIdResponse:
        """
        @summary Queries the prefetch details of a task, including the prefetch progress of all resources in the task. Only users who are included in the whitelist can use this operation. You can contact your business manager to apply for the whitelist.
        
        @description    You can query data within the last 3 days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribePreloadDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreloadDetailByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreloadDetailById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribePreloadDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_preload_detail_by_id(
        self,
        request: cdn_20180510_models.DescribePreloadDetailByIdRequest,
    ) -> cdn_20180510_models.DescribePreloadDetailByIdResponse:
        """
        @summary Queries the prefetch details of a task, including the prefetch progress of all resources in the task. Only users who are included in the whitelist can use this operation. You can contact your business manager to apply for the whitelist.
        
        @description    You can query data within the last 3 days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribePreloadDetailByIdRequest
        @return: DescribePreloadDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_preload_detail_by_id_with_options(request, runtime)

    async def describe_preload_detail_by_id_async(
        self,
        request: cdn_20180510_models.DescribePreloadDetailByIdRequest,
    ) -> cdn_20180510_models.DescribePreloadDetailByIdResponse:
        """
        @summary Queries the prefetch details of a task, including the prefetch progress of all resources in the task. Only users who are included in the whitelist can use this operation. You can contact your business manager to apply for the whitelist.
        
        @description    You can query data within the last 3 days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribePreloadDetailByIdRequest
        @return: DescribePreloadDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_preload_detail_by_id_with_options_async(request, runtime)

    def describe_range_data_by_locate_and_isp_service_with_options(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        """
        @summary Queries the bandwidth values by Internet service provider (ISP) and region.
        
        @description    The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeRangeDataByLocateAndIspServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRangeDataByLocateAndIspServiceResponse
        """
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
        """
        @summary Queries the bandwidth values by Internet service provider (ISP) and region.
        
        @description    The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeRangeDataByLocateAndIspServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRangeDataByLocateAndIspServiceResponse
        """
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
        """
        @summary Queries the bandwidth values by Internet service provider (ISP) and region.
        
        @description    The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeRangeDataByLocateAndIspServiceRequest
        @return: DescribeRangeDataByLocateAndIspServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_range_data_by_locate_and_isp_service_with_options(request, runtime)

    async def describe_range_data_by_locate_and_isp_service_async(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        """
        @summary Queries the bandwidth values by Internet service provider (ISP) and region.
        
        @description    The data is collected every 5 minutes.
        You can call this operation up to 20 times per second per account.
        
        @param request: DescribeRangeDataByLocateAndIspServiceRequest
        @return: DescribeRangeDataByLocateAndIspServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_range_data_by_locate_and_isp_service_with_options_async(request, runtime)

    def describe_realtime_delivery_acc_with_options(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        """
        @summary Queries the number of real-time log deliveries.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRealtimeDeliveryAccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRealtimeDeliveryAccResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
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
        """
        @summary Queries the number of real-time log deliveries.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRealtimeDeliveryAccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRealtimeDeliveryAccResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
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
        """
        @summary Queries the number of real-time log deliveries.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRealtimeDeliveryAccRequest
        @return: DescribeRealtimeDeliveryAccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_realtime_delivery_acc_with_options(request, runtime)

    async def describe_realtime_delivery_acc_async(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        """
        @summary Queries the number of real-time log deliveries.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeRealtimeDeliveryAccRequest
        @return: DescribeRealtimeDeliveryAccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_realtime_delivery_acc_with_options_async(request, runtime)

    def describe_refresh_quota_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
        """
        @summary DescribeRefreshQuota
        
        @description Queries the maximum and remaining numbers of URLs and directories that can be refreshed, the maximum and remaining numbers of times that you can prefetch content, and the maximum and remaining numbers of URLs and directories that can be blocked on the current day.
        
        @param request: DescribeRefreshQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshQuotaResponse
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
        """
        @summary DescribeRefreshQuota
        
        @description Queries the maximum and remaining numbers of URLs and directories that can be refreshed, the maximum and remaining numbers of times that you can prefetch content, and the maximum and remaining numbers of URLs and directories that can be blocked on the current day.
        
        @param request: DescribeRefreshQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshQuotaResponse
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
        """
        @summary DescribeRefreshQuota
        
        @description Queries the maximum and remaining numbers of URLs and directories that can be refreshed, the maximum and remaining numbers of times that you can prefetch content, and the maximum and remaining numbers of URLs and directories that can be blocked on the current day.
        
        @param request: DescribeRefreshQuotaRequest
        @return: DescribeRefreshQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_quota_with_options(request, runtime)

    async def describe_refresh_quota_async(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
        """
        @summary DescribeRefreshQuota
        
        @description Queries the maximum and remaining numbers of URLs and directories that can be refreshed, the maximum and remaining numbers of times that you can prefetch content, and the maximum and remaining numbers of URLs and directories that can be blocked on the current day.
        
        @param request: DescribeRefreshQuotaRequest
        @return: DescribeRefreshQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_quota_with_options_async(request, runtime)

    def describe_refresh_task_by_id_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
        """
        @summary Queries the statuses of refresh or prefetch tasks by task ID.
        
        @description    You can query data in the last three days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeRefreshTaskByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshTaskByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries the statuses of refresh or prefetch tasks by task ID.
        
        @description    You can query data in the last three days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeRefreshTaskByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshTaskByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Queries the statuses of refresh or prefetch tasks by task ID.
        
        @description    You can query data in the last three days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeRefreshTaskByIdRequest
        @return: DescribeRefreshTaskByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_task_by_id_with_options(request, runtime)

    async def describe_refresh_task_by_id_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
        """
        @summary Queries the statuses of refresh or prefetch tasks by task ID.
        
        @description    You can query data in the last three days.
        You can call this operation up to 30 times per second per account.
        
        @param request: DescribeRefreshTaskByIdRequest
        @return: DescribeRefreshTaskByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_task_by_id_with_options_async(request, runtime)

    def describe_refresh_tasks_with_options(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
        """
        @summary Queries the status of refresh or prefetch tasks that belong to an accelerated domain name.
        
        @description    You can query the status of tasks by task ID or URL.
        You can set both the **TaskId** and **ObjectPath** parameters. If you do not set the **TaskId** or **ObjectPath** parameter, data entries on the first page (20 entries) collected in the last 3 days are returned.
        You can query data collected in the last 3 days.
        If auto CDN cache update is enabled in the Object Storage Service (OSS) console, you cannot call the DescribeRefreshTasks operation to query automatic refresh tasks in OSS.
        You can call this operation up to 10 times per second per account. If you want to query tasks at a higher frequency, call the [DescribeRefreshTaskById](https://help.aliyun.com/document_detail/187709.html) operation. This operation allows you to query tasks by task ID.
        
        @param request: DescribeRefreshTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshTasksResponse
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
        """
        @summary Queries the status of refresh or prefetch tasks that belong to an accelerated domain name.
        
        @description    You can query the status of tasks by task ID or URL.
        You can set both the **TaskId** and **ObjectPath** parameters. If you do not set the **TaskId** or **ObjectPath** parameter, data entries on the first page (20 entries) collected in the last 3 days are returned.
        You can query data collected in the last 3 days.
        If auto CDN cache update is enabled in the Object Storage Service (OSS) console, you cannot call the DescribeRefreshTasks operation to query automatic refresh tasks in OSS.
        You can call this operation up to 10 times per second per account. If you want to query tasks at a higher frequency, call the [DescribeRefreshTaskById](https://help.aliyun.com/document_detail/187709.html) operation. This operation allows you to query tasks by task ID.
        
        @param request: DescribeRefreshTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRefreshTasksResponse
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
        """
        @summary Queries the status of refresh or prefetch tasks that belong to an accelerated domain name.
        
        @description    You can query the status of tasks by task ID or URL.
        You can set both the **TaskId** and **ObjectPath** parameters. If you do not set the **TaskId** or **ObjectPath** parameter, data entries on the first page (20 entries) collected in the last 3 days are returned.
        You can query data collected in the last 3 days.
        If auto CDN cache update is enabled in the Object Storage Service (OSS) console, you cannot call the DescribeRefreshTasks operation to query automatic refresh tasks in OSS.
        You can call this operation up to 10 times per second per account. If you want to query tasks at a higher frequency, call the [DescribeRefreshTaskById](https://help.aliyun.com/document_detail/187709.html) operation. This operation allows you to query tasks by task ID.
        
        @param request: DescribeRefreshTasksRequest
        @return: DescribeRefreshTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_tasks_with_options(request, runtime)

    async def describe_refresh_tasks_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
        """
        @summary Queries the status of refresh or prefetch tasks that belong to an accelerated domain name.
        
        @description    You can query the status of tasks by task ID or URL.
        You can set both the **TaskId** and **ObjectPath** parameters. If you do not set the **TaskId** or **ObjectPath** parameter, data entries on the first page (20 entries) collected in the last 3 days are returned.
        You can query data collected in the last 3 days.
        If auto CDN cache update is enabled in the Object Storage Service (OSS) console, you cannot call the DescribeRefreshTasks operation to query automatic refresh tasks in OSS.
        You can call this operation up to 10 times per second per account. If you want to query tasks at a higher frequency, call the [DescribeRefreshTaskById](https://help.aliyun.com/document_detail/187709.html) operation. This operation allows you to query tasks by task ID.
        
        @param request: DescribeRefreshTasksRequest
        @return: DescribeRefreshTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_tasks_with_options_async(request, runtime)

    def describe_staging_ip_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        """
        @summary Queries node IP addresses in the staging environment.
        
        @description >The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeStagingIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStagingIpResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        """
        @summary Queries node IP addresses in the staging environment.
        
        @description >The maximum number of times that each user can call this operation per second is 30.
        
        @param request: DescribeStagingIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStagingIpResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def describe_staging_ip(self) -> cdn_20180510_models.DescribeStagingIpResponse:
        """
        @summary Queries node IP addresses in the staging environment.
        
        @description >The maximum number of times that each user can call this operation per second is 30.
        
        @return: DescribeStagingIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_staging_ip_with_options(runtime)

    async def describe_staging_ip_async(self) -> cdn_20180510_models.DescribeStagingIpResponse:
        """
        @summary Queries node IP addresses in the staging environment.
        
        @description >The maximum number of times that each user can call this operation per second is 30.
        
        @return: DescribeStagingIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_staging_ip_with_options_async(runtime)

    def describe_tag_resources_with_options(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @description >  The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DescribeTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResourcesResponse
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
        """
        @summary Queries tags that are added to specified resources.
        
        @description >  The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DescribeTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResourcesResponse
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
        """
        @summary Queries tags that are added to specified resources.
        
        @description >  The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DescribeTagResourcesRequest
        @return: DescribeTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    async def describe_tag_resources_async(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
        """
        @summary Queries tags that are added to specified resources.
        
        @description >  The maximum number of times that each user can call this operation per second is 10.
        
        @param request: DescribeTagResourcesRequest
        @return: DescribeTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_resources_with_options_async(request, runtime)

    def describe_top_domains_by_flow_with_options(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
        """
        @summary Queries the top N domain names ranked by network traffic. You can query data collected in the last 30 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the current month. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopDomainsByFlowResponse
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
        """
        @summary Queries the top N domain names ranked by network traffic. You can query data collected in the last 30 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the current month. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopDomainsByFlowResponse
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
        """
        @summary Queries the top N domain names ranked by network traffic. You can query data collected in the last 30 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the current month. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeTopDomainsByFlowRequest
        @return: DescribeTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_top_domains_by_flow_with_options(request, runtime)

    async def describe_top_domains_by_flow_async(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
        """
        @summary Queries the top N domain names ranked by network traffic. You can query data collected in the last 30 days.
        
        @description The statistical analysis feature of Alibaba Cloud CDN is no longer available. The API operations related to the statistical analysis feature are no longer maintained. We recommend that you do not use the API operations because data may be missing or inaccurate. You can use the [operations report](https://help.aliyun.com/document_detail/279577.html) feature for data analysis.
        >    If you do not set the **StartTime** or **EndTime** parameter, the request returns the data collected in the current month. If you set both these parameters, the request returns the data collected within the specified time range.
        >   You can call this operation up to 100 times per second per account.
        
        @param request: DescribeTopDomainsByFlowRequest
        @return: DescribeTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_domains_by_flow_with_options_async(request, runtime)

    def describe_user_certificate_expire_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        """
        @summary Queries the number of domain names whose SSL certificates are about to expire or have already expired.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserCertificateExpireCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserCertificateExpireCountResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        """
        @summary Queries the number of domain names whose SSL certificates are about to expire or have already expired.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserCertificateExpireCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserCertificateExpireCountResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def describe_user_certificate_expire_count(self) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        """
        @summary Queries the number of domain names whose SSL certificates are about to expire or have already expired.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: DescribeUserCertificateExpireCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_certificate_expire_count_with_options(runtime)

    async def describe_user_certificate_expire_count_async(self) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        """
        @summary Queries the number of domain names whose SSL certificates are about to expire or have already expired.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: DescribeUserCertificateExpireCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_certificate_expire_count_with_options_async(runtime)

    def describe_user_configs_with_options(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        """
        @deprecated OpenAPI DescribeUserConfigs is deprecated
        
        @summary Queries configurations of security features.
        
        @param request: DescribeUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserConfigsResponse
        Deprecated
        """
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
        """
        @deprecated OpenAPI DescribeUserConfigs is deprecated
        
        @summary Queries configurations of security features.
        
        @param request: DescribeUserConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserConfigsResponse
        Deprecated
        """
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
        """
        @deprecated OpenAPI DescribeUserConfigs is deprecated
        
        @summary Queries configurations of security features.
        
        @param request: DescribeUserConfigsRequest
        @return: DescribeUserConfigsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_configs_with_options(request, runtime)

    async def describe_user_configs_async(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        """
        @deprecated OpenAPI DescribeUserConfigs is deprecated
        
        @summary Queries configurations of security features.
        
        @param request: DescribeUserConfigsRequest
        @return: DescribeUserConfigsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_configs_with_options_async(request, runtime)

    def describe_user_domains_with_options(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        """
        @summary Queries all accelerated domain names in your Alibaba Cloud account and the status of the accelerated domain names. You can filter domain names by name or status. Fuzzy match is supported.
        
        @description    You can call this operation up to 100 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDomainsResponse
        """
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
        """
        @summary Queries all accelerated domain names in your Alibaba Cloud account and the status of the accelerated domain names. You can filter domain names by name or status. Fuzzy match is supported.
        
        @description    You can call this operation up to 100 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeUserDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserDomainsResponse
        """
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
        """
        @summary Queries all accelerated domain names in your Alibaba Cloud account and the status of the accelerated domain names. You can filter domain names by name or status. Fuzzy match is supported.
        
        @description    You can call this operation up to 100 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeUserDomainsRequest
        @return: DescribeUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_domains_with_options(request, runtime)

    async def describe_user_domains_async(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        """
        @summary Queries all accelerated domain names in your Alibaba Cloud account and the status of the accelerated domain names. You can filter domain names by name or status. Fuzzy match is supported.
        
        @description    You can call this operation up to 100 times per second per account.
        You can specify up to 50 domain names in each request. Separate multiple domain names with commas (,).
        
        @param request: DescribeUserDomainsRequest
        @return: DescribeUserDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_domains_with_options_async(request, runtime)

    def describe_user_tags_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        """
        @summary Queries user tags.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserTagsResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        """
        @summary Queries user tags.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserTagsResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def describe_user_tags(self) -> cdn_20180510_models.DescribeUserTagsResponse:
        """
        @summary Queries user tags.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: DescribeUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_tags_with_options(runtime)

    async def describe_user_tags_async(self) -> cdn_20180510_models.DescribeUserTagsResponse:
        """
        @summary Queries user tags.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: DescribeUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_tags_with_options_async(runtime)

    def describe_user_usage_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
        """
        @summary Queries usage export tasks that were created in the last three months.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserUsageDataExportTaskResponse
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
        """
        @summary Queries usage export tasks that were created in the last three months.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserUsageDataExportTaskResponse
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
        """
        @summary Queries usage export tasks that were created in the last three months.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDataExportTaskRequest
        @return: DescribeUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_data_export_task_with_options(request, runtime)

    async def describe_user_usage_data_export_task_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
        """
        @summary Queries usage export tasks that were created in the last three months.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDataExportTaskRequest
        @return: DescribeUserUsageDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_usage_data_export_task_with_options_async(request, runtime)

    def describe_user_usage_detail_data_export_task_with_options(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
        """
        @summary Queries tasks that were used to export resource usage details of one or more accelerated domain names that belong to your Alibaba Cloud account. Resource usage information is collected every five minutes.
        
        @description    This operation has been available since July 20, 2018. You can query information about resource usage collected within the last three months.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserUsageDetailDataExportTaskResponse
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
        """
        @summary Queries tasks that were used to export resource usage details of one or more accelerated domain names that belong to your Alibaba Cloud account. Resource usage information is collected every five minutes.
        
        @description    This operation has been available since July 20, 2018. You can query information about resource usage collected within the last three months.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDetailDataExportTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserUsageDetailDataExportTaskResponse
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
        """
        @summary Queries tasks that were used to export resource usage details of one or more accelerated domain names that belong to your Alibaba Cloud account. Resource usage information is collected every five minutes.
        
        @description    This operation has been available since July 20, 2018. You can query information about resource usage collected within the last three months.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDetailDataExportTaskRequest
        @return: DescribeUserUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_detail_data_export_task_with_options(request, runtime)

    async def describe_user_usage_detail_data_export_task_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
        """
        @summary Queries tasks that were used to export resource usage details of one or more accelerated domain names that belong to your Alibaba Cloud account. Resource usage information is collected every five minutes.
        
        @description    This operation has been available since July 20, 2018. You can query information about resource usage collected within the last three months.
        You can call this operation up to 100 times per second per account.
        
        @param request: DescribeUserUsageDetailDataExportTaskRequest
        @return: DescribeUserUsageDetailDataExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_usage_detail_data_export_task_with_options_async(request, runtime)

    def describe_user_vips_by_domain_with_options(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        """
        @summary Queries virtual IP addresses (VIPs) of CDN points of presence (POPs) by domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserVipsByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserVipsByDomainResponse
        """
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
        """
        @summary Queries virtual IP addresses (VIPs) of CDN points of presence (POPs) by domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserVipsByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserVipsByDomainResponse
        """
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
        """
        @summary Queries virtual IP addresses (VIPs) of CDN points of presence (POPs) by domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserVipsByDomainRequest
        @return: DescribeUserVipsByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_vips_by_domain_with_options(request, runtime)

    async def describe_user_vips_by_domain_async(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        """
        @summary Queries virtual IP addresses (VIPs) of CDN points of presence (POPs) by domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: DescribeUserVipsByDomainRequest
        @return: DescribeUserVipsByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_vips_by_domain_with_options_async(request, runtime)

    def describe_verify_content_with_options(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
        """
        @summary Queries the ownership verification content of an accelerated domain name.
        
        @param request: DescribeVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Queries the ownership verification content of an accelerated domain name.
        
        @param request: DescribeVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Queries the ownership verification content of an accelerated domain name.
        
        @param request: DescribeVerifyContentRequest
        @return: DescribeVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_content_with_options(request, runtime)

    async def describe_verify_content_async(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
        """
        @summary Queries the ownership verification content of an accelerated domain name.
        
        @param request: DescribeVerifyContentRequest
        @return: DescribeVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_content_with_options_async(request, runtime)

    def disable_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DisableRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRealtimeLogDeliveryResponse
        """
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
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DisableRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRealtimeLogDeliveryResponse
        """
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
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DisableRealtimeLogDeliveryRequest
        @return: DisableRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_realtime_log_delivery_with_options(request, runtime)

    async def disable_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: DisableRealtimeLogDeliveryRequest
        @return: DisableRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_realtime_log_delivery_with_options_async(request, runtime)

    def enable_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: EnableRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRealtimeLogDeliveryResponse
        """
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
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: EnableRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRealtimeLogDeliveryResponse
        """
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
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: EnableRealtimeLogDeliveryRequest
        @return: EnableRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_realtime_log_delivery_with_options(request, runtime)

    async def enable_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        """
        @summary The ID of the request.
        
        @description >  The maximum number of times that each user can call this operation per second is 100.
        
        @param request: EnableRealtimeLogDeliveryRequest
        @return: EnableRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_realtime_log_delivery_with_options_async(request, runtime)

    def list_domains_by_log_config_id_with_options(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        """
        @summary Queries domain names by log configuration ID.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListDomainsByLogConfigIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsByLogConfigIdResponse
        """
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
        """
        @summary Queries domain names by log configuration ID.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListDomainsByLogConfigIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsByLogConfigIdResponse
        """
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
        """
        @summary Queries domain names by log configuration ID.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListDomainsByLogConfigIdRequest
        @return: ListDomainsByLogConfigIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_domains_by_log_config_id_with_options(request, runtime)

    async def list_domains_by_log_config_id_async(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        """
        @summary Queries domain names by log configuration ID.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListDomainsByLogConfigIdRequest
        @return: ListDomainsByLogConfigIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_domains_by_log_config_id_with_options_async(request, runtime)

    def list_fctrigger_with_options(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        """
        @summary Queries the Function Compute trigger that is set for an Alibaba Cloud CDN event.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFCTriggerResponse
        """
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
        """
        @summary Queries the Function Compute trigger that is set for an Alibaba Cloud CDN event.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFCTriggerResponse
        """
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
        """
        @summary Queries the Function Compute trigger that is set for an Alibaba Cloud CDN event.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListFCTriggerRequest
        @return: ListFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fctrigger_with_options(request, runtime)

    async def list_fctrigger_async(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        """
        @summary Queries the Function Compute trigger that is set for an Alibaba Cloud CDN event.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListFCTriggerRequest
        @return: ListFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fctrigger_with_options_async(request, runtime)

    def list_realtime_log_delivery_domains_with_options(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        """
        @summary Queries all domain names that are associated with a specific real-time log delivery configuration record.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeLogDeliveryDomainsResponse
        """
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
        """
        @summary Queries all domain names that are associated with a specific real-time log delivery configuration record.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeLogDeliveryDomainsResponse
        """
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
        """
        @summary Queries all domain names that are associated with a specific real-time log delivery configuration record.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryDomainsRequest
        @return: ListRealtimeLogDeliveryDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_domains_with_options(request, runtime)

    async def list_realtime_log_delivery_domains_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        """
        @summary Queries all domain names that are associated with a specific real-time log delivery configuration record.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryDomainsRequest
        @return: ListRealtimeLogDeliveryDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_log_delivery_domains_with_options_async(request, runtime)

    def list_realtime_log_delivery_infos_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        """
        @summary Queries the information about the real-time log delivery feature in a specified region.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeLogDeliveryInfosResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        """
        @summary Queries the information about the real-time log delivery feature in a specified region.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListRealtimeLogDeliveryInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRealtimeLogDeliveryInfosResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def list_realtime_log_delivery_infos(self) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        """
        @summary Queries the information about the real-time log delivery feature in a specified region.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: ListRealtimeLogDeliveryInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_infos_with_options(runtime)

    async def list_realtime_log_delivery_infos_async(self) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        """
        @summary Queries the information about the real-time log delivery feature in a specified region.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: ListRealtimeLogDeliveryInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_realtime_log_delivery_infos_with_options_async(runtime)

    def list_tag_resources_with_options(
        self,
        request: cdn_20180510_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cdn_20180510_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cdn_20180510_models.ListTagResourcesRequest,
    ) -> cdn_20180510_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cdn_20180510_models.ListTagResourcesRequest,
    ) -> cdn_20180510_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_custom_log_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        """
        @summary Queries all custom log configurations in your account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListUserCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserCustomLogConfigResponse
        """
        req = open_api_models.OpenApiRequest()
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
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        """
        @summary Queries all custom log configurations in your account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ListUserCustomLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserCustomLogConfigResponse
        """
        req = open_api_models.OpenApiRequest()
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

    def list_user_custom_log_config(self) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        """
        @summary Queries all custom log configurations in your account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: ListUserCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_custom_log_config_with_options(runtime)

    async def list_user_custom_log_config_async(self) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        """
        @summary Queries all custom log configurations in your account.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @return: ListUserCustomLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_custom_log_config_with_options_async(runtime)

    def modify_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
        """
        @summary Modifies the configuration of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: ModifyCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainResponse
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
        """
        @summary Modifies the configuration of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: ModifyCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainResponse
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
        """
        @summary Modifies the configuration of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: ModifyCdnDomainRequest
        @return: ModifyCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_with_options(request, runtime)

    async def modify_cdn_domain_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
        """
        @summary Modifies the configuration of an accelerated domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: ModifyCdnDomainRequest
        @return: ModifyCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_domain_with_options_async(request, runtime)

    def modify_cdn_domain_owner_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainOwnerResponse:
        """
        @summary Transfer domain names from an Alibaba Cloud account to the current account.
        
        @description This operation is used in the following scenario:
        You have multiple Alibaba Cloud accounts and want to transfer domain names from Account A to Account B.
        You are prompted that a domain name has been added when you add the domain name to Alibaba Cloud CDN. You do not know which account does the domain name belong to, and you want to transfer the domain name to your current account.
        
        @param request: ModifyCdnDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainOwnerResponse
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
            action='ModifyCdnDomainOwner',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdn_domain_owner_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainOwnerResponse:
        """
        @summary Transfer domain names from an Alibaba Cloud account to the current account.
        
        @description This operation is used in the following scenario:
        You have multiple Alibaba Cloud accounts and want to transfer domain names from Account A to Account B.
        You are prompted that a domain name has been added when you add the domain name to Alibaba Cloud CDN. You do not know which account does the domain name belong to, and you want to transfer the domain name to your current account.
        
        @param request: ModifyCdnDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainOwnerResponse
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
            action='ModifyCdnDomainOwner',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdn_domain_owner(
        self,
        request: cdn_20180510_models.ModifyCdnDomainOwnerRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainOwnerResponse:
        """
        @summary Transfer domain names from an Alibaba Cloud account to the current account.
        
        @description This operation is used in the following scenario:
        You have multiple Alibaba Cloud accounts and want to transfer domain names from Account A to Account B.
        You are prompted that a domain name has been added when you add the domain name to Alibaba Cloud CDN. You do not know which account does the domain name belong to, and you want to transfer the domain name to your current account.
        
        @param request: ModifyCdnDomainOwnerRequest
        @return: ModifyCdnDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_owner_with_options(request, runtime)

    async def modify_cdn_domain_owner_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainOwnerRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainOwnerResponse:
        """
        @summary Transfer domain names from an Alibaba Cloud account to the current account.
        
        @description This operation is used in the following scenario:
        You have multiple Alibaba Cloud accounts and want to transfer domain names from Account A to Account B.
        You are prompted that a domain name has been added when you add the domain name to Alibaba Cloud CDN. You do not know which account does the domain name belong to, and you want to transfer the domain name to your current account.
        
        @param request: ModifyCdnDomainOwnerRequest
        @return: ModifyCdnDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_domain_owner_with_options_async(request, runtime)

    def modify_cdn_domain_schdm_by_property_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
        """
        @summary Changes the acceleration region for an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyCdnDomainSchdmByPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainSchdmByPropertyResponse
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
        """
        @summary Changes the acceleration region for an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyCdnDomainSchdmByPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCdnDomainSchdmByPropertyResponse
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
        """
        @summary Changes the acceleration region for an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyCdnDomainSchdmByPropertyRequest
        @return: ModifyCdnDomainSchdmByPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_cdn_domain_schdm_by_property_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
        """
        @summary Changes the acceleration region for an accelerated domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyCdnDomainSchdmByPropertyRequest
        @return: ModifyCdnDomainSchdmByPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        """
        @summary Modifies the configurations of real-time log delivery for a specific domain name. Each domain name supports only one Logstore.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRealtimeLogDeliveryResponse
        """
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
        """
        @summary Modifies the configurations of real-time log delivery for a specific domain name. Each domain name supports only one Logstore.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyRealtimeLogDeliveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRealtimeLogDeliveryResponse
        """
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
        """
        @summary Modifies the configurations of real-time log delivery for a specific domain name. Each domain name supports only one Logstore.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyRealtimeLogDeliveryRequest
        @return: ModifyRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_realtime_log_delivery_with_options(request, runtime)

    async def modify_realtime_log_delivery_async(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        """
        @summary Modifies the configurations of real-time log delivery for a specific domain name. Each domain name supports only one Logstore.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: ModifyRealtimeLogDeliveryRequest
        @return: ModifyRealtimeLogDeliveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_realtime_log_delivery_with_options_async(request, runtime)

    def open_cdn_service_with_options(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        """
        @summary Activates Alibaba Cloud CDN. You must activate Alibaba Cloud CDN before you can manage domain names in Alibaba Cloud CDN.
        
        @description    Alibaba Cloud CDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must complete real-name verification to activate Alibaba Cloud CDN.
        You can call this operation up to five times per second per user.
        
        @param request: OpenCdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCdnServiceResponse
        """
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
        """
        @summary Activates Alibaba Cloud CDN. You must activate Alibaba Cloud CDN before you can manage domain names in Alibaba Cloud CDN.
        
        @description    Alibaba Cloud CDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must complete real-name verification to activate Alibaba Cloud CDN.
        You can call this operation up to five times per second per user.
        
        @param request: OpenCdnServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCdnServiceResponse
        """
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
        """
        @summary Activates Alibaba Cloud CDN. You must activate Alibaba Cloud CDN before you can manage domain names in Alibaba Cloud CDN.
        
        @description    Alibaba Cloud CDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must complete real-name verification to activate Alibaba Cloud CDN.
        You can call this operation up to five times per second per user.
        
        @param request: OpenCdnServiceRequest
        @return: OpenCdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_cdn_service_with_options(request, runtime)

    async def open_cdn_service_async(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        """
        @summary Activates Alibaba Cloud CDN. You must activate Alibaba Cloud CDN before you can manage domain names in Alibaba Cloud CDN.
        
        @description    Alibaba Cloud CDN can be activated only once per Alibaba Cloud account. The Alibaba Cloud account must complete real-name verification to activate Alibaba Cloud CDN.
        You can call this operation up to five times per second per user.
        
        @param request: OpenCdnServiceRequest
        @return: OpenCdnServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_cdn_service_with_options_async(request, runtime)

    def publish_staging_config_to_production_with_options(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
        """
        @summary Publishes the configurations of the staging environment to the production environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: PublishStagingConfigToProductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishStagingConfigToProductionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Publishes the configurations of the staging environment to the production environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: PublishStagingConfigToProductionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishStagingConfigToProductionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Publishes the configurations of the staging environment to the production environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: PublishStagingConfigToProductionRequest
        @return: PublishStagingConfigToProductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_staging_config_to_production_with_options(request, runtime)

    async def publish_staging_config_to_production_async(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
        """
        @summary Publishes the configurations of the staging environment to the production environment.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: PublishStagingConfigToProductionRequest
        @return: PublishStagingConfigToProductionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_staging_config_to_production_with_options_async(request, runtime)

    def push_object_cache_with_options(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
        """
        @summary Prefetches content from origin servers to points of presence (POPs). This reduces loads on origin servers because users can directly hit cache upon their first visits.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        You can specify at most 100 URLs in each prefetch request.
        For each Alibaba Cloud account, the prefetch queue can contain up to 50,000 URLs. Content is prefetched based on the time when the URLs are submitted. The URL that is submitted the earliest has the highest priority. If the number of URLs in the queue reaches 50,000, you cannot submit more URLs until the number drops below 50,000.
        You can call this operation up to 50 times per second per account.
        For more information about how to automate refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a prefetch task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        To allow RAM users to perform this operation, you must first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        
        @param request: PushObjectCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushObjectCacheResponse
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
        """
        @summary Prefetches content from origin servers to points of presence (POPs). This reduces loads on origin servers because users can directly hit cache upon their first visits.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        You can specify at most 100 URLs in each prefetch request.
        For each Alibaba Cloud account, the prefetch queue can contain up to 50,000 URLs. Content is prefetched based on the time when the URLs are submitted. The URL that is submitted the earliest has the highest priority. If the number of URLs in the queue reaches 50,000, you cannot submit more URLs until the number drops below 50,000.
        You can call this operation up to 50 times per second per account.
        For more information about how to automate refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a prefetch task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        To allow RAM users to perform this operation, you must first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        
        @param request: PushObjectCacheRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushObjectCacheResponse
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
        """
        @summary Prefetches content from origin servers to points of presence (POPs). This reduces loads on origin servers because users can directly hit cache upon their first visits.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        You can specify at most 100 URLs in each prefetch request.
        For each Alibaba Cloud account, the prefetch queue can contain up to 50,000 URLs. Content is prefetched based on the time when the URLs are submitted. The URL that is submitted the earliest has the highest priority. If the number of URLs in the queue reaches 50,000, you cannot submit more URLs until the number drops below 50,000.
        You can call this operation up to 50 times per second per account.
        For more information about how to automate refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a prefetch task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        To allow RAM users to perform this operation, you must first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        
        @param request: PushObjectCacheRequest
        @return: PushObjectCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_object_cache_with_options(request, runtime)

    async def push_object_cache_async(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
        """
        @summary Prefetches content from origin servers to points of presence (POPs). This reduces loads on origin servers because users can directly hit cache upon their first visits.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        By default, each Alibaba Cloud account can submit up to 1,000 URLs per day. If the daily peak bandwidth value of your workloads exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to increase your daily quota. Alibaba Cloud reviews your application and then increases the quota accordingly.
        You can specify at most 100 URLs in each prefetch request.
        For each Alibaba Cloud account, the prefetch queue can contain up to 50,000 URLs. Content is prefetched based on the time when the URLs are submitted. The URL that is submitted the earliest has the highest priority. If the number of URLs in the queue reaches 50,000, you cannot submit more URLs until the number drops below 50,000.
        You can call this operation up to 50 times per second per account.
        For more information about how to automate refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a prefetch task is submitted and completed, the POPs immediately start to retrieve resources from the origin server. Therefore, a large number of refresh tasks cause a large number of concurrent download tasks. This increases the number of requests that are redirected to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        The time required for a prefetch task to complete is proportional to the size of the prefetched file. In actual practice, most prefetch tasks require 5 to 30 minutes to complete. A task with a smaller average file size requires less time.
        To allow RAM users to perform this operation, you must first grant them the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        
        @param request: PushObjectCacheRequest
        @return: PushObjectCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_object_cache_with_options_async(request, runtime)

    def refresh_object_cache_by_cache_tag_with_options(
        self,
        request: cdn_20180510_models.RefreshObjectCacheByCacheTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCacheByCacheTagResponse:
        """
        @summary 指定缓存tag刷新节点上的文件内容
        
        @param request: RefreshObjectCacheByCacheTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshObjectCacheByCacheTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshObjectCacheByCacheTag',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RefreshObjectCacheByCacheTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_object_cache_by_cache_tag_with_options_async(
        self,
        request: cdn_20180510_models.RefreshObjectCacheByCacheTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCacheByCacheTagResponse:
        """
        @summary 指定缓存tag刷新节点上的文件内容
        
        @param request: RefreshObjectCacheByCacheTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshObjectCacheByCacheTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_tag):
            query['CacheTag'] = request.cache_tag
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshObjectCacheByCacheTag',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RefreshObjectCacheByCacheTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_object_cache_by_cache_tag(
        self,
        request: cdn_20180510_models.RefreshObjectCacheByCacheTagRequest,
    ) -> cdn_20180510_models.RefreshObjectCacheByCacheTagResponse:
        """
        @summary 指定缓存tag刷新节点上的文件内容
        
        @param request: RefreshObjectCacheByCacheTagRequest
        @return: RefreshObjectCacheByCacheTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_object_cache_by_cache_tag_with_options(request, runtime)

    async def refresh_object_cache_by_cache_tag_async(
        self,
        request: cdn_20180510_models.RefreshObjectCacheByCacheTagRequest,
    ) -> cdn_20180510_models.RefreshObjectCacheByCacheTagResponse:
        """
        @summary 指定缓存tag刷新节点上的文件内容
        
        @param request: RefreshObjectCacheByCacheTagRequest
        @return: RefreshObjectCacheByCacheTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_object_cache_by_cache_tag_with_options_async(request, runtime)

    def refresh_object_caches_with_options(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
        """
        @summary Refreshes files on Alibaba Cloud CDN points of presence (POPs). After files are refreshed, the original file content immediately becomes invalid. If clients request the original file content, Alibaba Cloud CDN forwards the requests to the origin server. Then, Alibaba Cloud CDN caches the latest content to the POPs and returns the content to the clients. Alibaba Cloud CDN allows you to refresh content from multiple URLs at the same time.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        You can call the RefreshObjectCaches operation up to 50 times per second per account.
        For more information about how to automatically refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a refresh task is submitted and completed, specific resources are removed from POPs. When a POP receives a request for the removed resources, the POP forwards the request to the origin server to retrieve the resources. The retrieved resources are returned to the client and cached on the POP. Multiple refresh tasks may cause a large number of resources to be removed from the POPs. This increases the number of requests that are forwarded to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        If you want to use RAM users to refresh or prefetch resources, you must obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        ### Refresh quota
        By default, each Alibaba Cloud account can refresh content from up to 10,000 URLs and 100 directories per day. The directories include subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. Alibaba Cloud CDN evaluates your application based on your workloads.
        By default, each Alibaba Cloud account can submit up to 20 refresh rules that contain regular expressions per day. If the daily peak bandwidth of your Alibaba Cloud account exceeds 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex) to request a quota increase.
        You can specify up to 1,000 URL refresh rules, 100 directory refresh rules, or 1 refresh rule that contains regular expressions in each call.
        You can refresh up to 1,000 URLs per minute for each domain name.
        
        @param request: RefreshObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        """
        @summary Refreshes files on Alibaba Cloud CDN points of presence (POPs). After files are refreshed, the original file content immediately becomes invalid. If clients request the original file content, Alibaba Cloud CDN forwards the requests to the origin server. Then, Alibaba Cloud CDN caches the latest content to the POPs and returns the content to the clients. Alibaba Cloud CDN allows you to refresh content from multiple URLs at the same time.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        You can call the RefreshObjectCaches operation up to 50 times per second per account.
        For more information about how to automatically refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a refresh task is submitted and completed, specific resources are removed from POPs. When a POP receives a request for the removed resources, the POP forwards the request to the origin server to retrieve the resources. The retrieved resources are returned to the client and cached on the POP. Multiple refresh tasks may cause a large number of resources to be removed from the POPs. This increases the number of requests that are forwarded to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        If you want to use RAM users to refresh or prefetch resources, you must obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        ### Refresh quota
        By default, each Alibaba Cloud account can refresh content from up to 10,000 URLs and 100 directories per day. The directories include subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. Alibaba Cloud CDN evaluates your application based on your workloads.
        By default, each Alibaba Cloud account can submit up to 20 refresh rules that contain regular expressions per day. If the daily peak bandwidth of your Alibaba Cloud account exceeds 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex) to request a quota increase.
        You can specify up to 1,000 URL refresh rules, 100 directory refresh rules, or 1 refresh rule that contains regular expressions in each call.
        You can refresh up to 1,000 URLs per minute for each domain name.
        
        @param request: RefreshObjectCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        """
        @summary Refreshes files on Alibaba Cloud CDN points of presence (POPs). After files are refreshed, the original file content immediately becomes invalid. If clients request the original file content, Alibaba Cloud CDN forwards the requests to the origin server. Then, Alibaba Cloud CDN caches the latest content to the POPs and returns the content to the clients. Alibaba Cloud CDN allows you to refresh content from multiple URLs at the same time.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        You can call the RefreshObjectCaches operation up to 50 times per second per account.
        For more information about how to automatically refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a refresh task is submitted and completed, specific resources are removed from POPs. When a POP receives a request for the removed resources, the POP forwards the request to the origin server to retrieve the resources. The retrieved resources are returned to the client and cached on the POP. Multiple refresh tasks may cause a large number of resources to be removed from the POPs. This increases the number of requests that are forwarded to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        If you want to use RAM users to refresh or prefetch resources, you must obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        ### Refresh quota
        By default, each Alibaba Cloud account can refresh content from up to 10,000 URLs and 100 directories per day. The directories include subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. Alibaba Cloud CDN evaluates your application based on your workloads.
        By default, each Alibaba Cloud account can submit up to 20 refresh rules that contain regular expressions per day. If the daily peak bandwidth of your Alibaba Cloud account exceeds 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex) to request a quota increase.
        You can specify up to 1,000 URL refresh rules, 100 directory refresh rules, or 1 refresh rule that contains regular expressions in each call.
        You can refresh up to 1,000 URLs per minute for each domain name.
        
        @param request: RefreshObjectCachesRequest
        @return: RefreshObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_object_caches_with_options(request, runtime)

    async def refresh_object_caches_async(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
        """
        @summary Refreshes files on Alibaba Cloud CDN points of presence (POPs). After files are refreshed, the original file content immediately becomes invalid. If clients request the original file content, Alibaba Cloud CDN forwards the requests to the origin server. Then, Alibaba Cloud CDN caches the latest content to the POPs and returns the content to the clients. Alibaba Cloud CDN allows you to refresh content from multiple URLs at the same time.
        
        @description    Alibaba Cloud CDN supports POST requests in which parameters are sent as a form.
        You can call the [RefreshObjectCaches](https://help.aliyun.com/document_detail/91164.html) operation to refresh content and call the [PushObjectCache](https://help.aliyun.com/document_detail/91161.html) operation to prefetch content.
        You can call the RefreshObjectCaches operation up to 50 times per second per account.
        For more information about how to automatically refresh or prefetch tasks, see [Run scripts to refresh and prefetch content](https://help.aliyun.com/document_detail/151829.html).
        ## Precautions
        After a refresh task is submitted and completed, specific resources are removed from POPs. When a POP receives a request for the removed resources, the POP forwards the request to the origin server to retrieve the resources. The retrieved resources are returned to the client and cached on the POP. Multiple refresh tasks may cause a large number of resources to be removed from the POPs. This increases the number of requests that are forwarded to the origin server. The back-to-origin routing process consumes more bandwidth resources and the origin server may be overwhelmed.
        A refresh task takes effect 5 to 6 minutes after being submitted. This means that if the resource you want to refresh has a TTL of less than five minutes, you wait for it to expire instead of manually running a refresh task.
        If you want to use RAM users to refresh or prefetch resources, you must obtain the required permissions. For more information, see [Authorize a RAM user to prefetch and refresh resources](https://help.aliyun.com/document_detail/260300.html).
        ### Refresh quota
        By default, each Alibaba Cloud account can refresh content from up to 10,000 URLs and 100 directories per day. The directories include subdirectories. If the daily peak bandwidth value exceeds 200 Mbit/s, you can [submit a ticket](https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A//ticket-intl.console.aliyun.com/%23/ticket/createIndex) to request a quota increase. Alibaba Cloud CDN evaluates your application based on your workloads.
        By default, each Alibaba Cloud account can submit up to 20 refresh rules that contain regular expressions per day. If the daily peak bandwidth of your Alibaba Cloud account exceeds 10 Gbit/s, you can [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex) to request a quota increase.
        You can specify up to 1,000 URL refresh rules, 100 directory refresh rules, or 1 refresh rule that contains regular expressions in each call.
        You can refresh up to 1,000 URLs per minute for each domain name.
        
        @param request: RefreshObjectCachesRequest
        @return: RefreshObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_object_caches_with_options_async(request, runtime)

    def rollback_staging_config_with_options(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
        """
        @summary Rolls back configurations in the staging environment. After you call this operation, all configurations in the staging environment are cleared.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Rolls back configurations in the staging environment. After you call this operation, all configurations in the staging environment are cleared.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackStagingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary Rolls back configurations in the staging environment. After you call this operation, all configurations in the staging environment are cleared.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackStagingConfigRequest
        @return: RollbackStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_staging_config_with_options(request, runtime)

    async def rollback_staging_config_async(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
        """
        @summary Rolls back configurations in the staging environment. After you call this operation, all configurations in the staging environment are cleared.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: RollbackStagingConfigRequest
        @return: RollbackStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_staging_config_with_options_async(request, runtime)

    def set_cdn_domain_csrcertificate_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
        """
        @summary You can call this operation to configure an SSL certificate for a specific domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: SetCdnDomainCSRCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainCSRCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary You can call this operation to configure an SSL certificate for a specific domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: SetCdnDomainCSRCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainCSRCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
        """
        @summary You can call this operation to configure an SSL certificate for a specific domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: SetCdnDomainCSRCertificateRequest
        @return: SetCdnDomainCSRCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_csrcertificate_with_options(request, runtime)

    async def set_cdn_domain_csrcertificate_async(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
        """
        @summary You can call this operation to configure an SSL certificate for a specific domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: SetCdnDomainCSRCertificateRequest
        @return: SetCdnDomainCSRCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_cdn_domain_smcertificate_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
        """
        @summary Enables or disables a ShangMi (SM) certificate for a domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainSMCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainSMCertificateResponse
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
        """
        @summary Enables or disables a ShangMi (SM) certificate for a domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainSMCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainSMCertificateResponse
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
        """
        @summary Enables or disables a ShangMi (SM) certificate for a domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainSMCertificateRequest
        @return: SetCdnDomainSMCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_smcertificate_with_options(request, runtime)

    async def set_cdn_domain_smcertificate_async(
        self,
        request: cdn_20180510_models.SetCdnDomainSMCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainSMCertificateResponse:
        """
        @summary Enables or disables a ShangMi (SM) certificate for a domain name.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainSMCertificateRequest
        @return: SetCdnDomainSMCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_smcertificate_with_options_async(request, runtime)

    def set_cdn_domain_sslcertificate_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainSSLCertificateResponse:
        """
        @summary Enables or disables the certificate for a domain name and updates the certificate information.
        
        @description    You can call this operation up to 30 times per second per account.
        Method: POST.
        
        @param request: SetCdnDomainSSLCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainSSLCertificateResponse
        """
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
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
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
            action='SetCdnDomainSSLCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cdn_domain_sslcertificate_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainSSLCertificateResponse:
        """
        @summary Enables or disables the certificate for a domain name and updates the certificate information.
        
        @description    You can call this operation up to 30 times per second per account.
        Method: POST.
        
        @param request: SetCdnDomainSSLCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainSSLCertificateResponse
        """
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
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
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
            action='SetCdnDomainSSLCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cdn_domain_sslcertificate(
        self,
        request: cdn_20180510_models.SetCdnDomainSSLCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainSSLCertificateResponse:
        """
        @summary Enables or disables the certificate for a domain name and updates the certificate information.
        
        @description    You can call this operation up to 30 times per second per account.
        Method: POST.
        
        @param request: SetCdnDomainSSLCertificateRequest
        @return: SetCdnDomainSSLCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_sslcertificate_with_options(request, runtime)

    async def set_cdn_domain_sslcertificate_async(
        self,
        request: cdn_20180510_models.SetCdnDomainSSLCertificateRequest,
    ) -> cdn_20180510_models.SetCdnDomainSSLCertificateResponse:
        """
        @summary Enables or disables the certificate for a domain name and updates the certificate information.
        
        @description    You can call this operation up to 30 times per second per account.
        Method: POST.
        
        @param request: SetCdnDomainSSLCertificateRequest
        @return: SetCdnDomainSSLCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_sslcertificate_with_options_async(request, runtime)

    def set_cdn_domain_staging_config_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        """
        @summary Configures a domain name to be accelerated in the staging environment.
        
        @description >  You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainStagingConfigResponse
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
        """
        @summary Configures a domain name to be accelerated in the staging environment.
        
        @description >  You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainStagingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCdnDomainStagingConfigResponse
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
        """
        @summary Configures a domain name to be accelerated in the staging environment.
        
        @description >  You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainStagingConfigRequest
        @return: SetCdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_staging_config_with_options(request, runtime)

    async def set_cdn_domain_staging_config_async(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        """
        @summary Configures a domain name to be accelerated in the staging environment.
        
        @description >  You can call this operation up to 30 times per second per account.
        
        @param request: SetCdnDomainStagingConfigRequest
        @return: SetCdnDomainStagingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_cdn_domain_staging_config_with_options_async(request, runtime)

    def set_domain_server_certificate_with_options(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
        """
        @deprecated OpenAPI SetDomainServerCertificate is deprecated, please use Cdn::2018-05-10::SetCdnDomainSSLCertificate instead.
        
        @summary Configures an SSL certificate for an accelerated domain name.
        
        @description    You can call this operation up to 10 times per second per user.
        Method: POST.
        
        @param request: SetDomainServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainServerCertificateResponse
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
        """
        @deprecated OpenAPI SetDomainServerCertificate is deprecated, please use Cdn::2018-05-10::SetCdnDomainSSLCertificate instead.
        
        @summary Configures an SSL certificate for an accelerated domain name.
        
        @description    You can call this operation up to 10 times per second per user.
        Method: POST.
        
        @param request: SetDomainServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainServerCertificateResponse
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
        """
        @deprecated OpenAPI SetDomainServerCertificate is deprecated, please use Cdn::2018-05-10::SetCdnDomainSSLCertificate instead.
        
        @summary Configures an SSL certificate for an accelerated domain name.
        
        @description    You can call this operation up to 10 times per second per user.
        Method: POST.
        
        @param request: SetDomainServerCertificateRequest
        @return: SetDomainServerCertificateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_server_certificate_with_options(request, runtime)

    async def set_domain_server_certificate_async(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
        """
        @deprecated OpenAPI SetDomainServerCertificate is deprecated, please use Cdn::2018-05-10::SetCdnDomainSSLCertificate instead.
        
        @summary Configures an SSL certificate for an accelerated domain name.
        
        @description    You can call this operation up to 10 times per second per user.
        Method: POST.
        
        @param request: SetDomainServerCertificateRequest
        @return: SetDomainServerCertificateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_server_certificate_with_options_async(request, runtime)

    def set_req_header_config_with_options(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        """
        @summary Sets a custom origin header.
        
        @param request: SetReqHeaderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetReqHeaderConfigResponse
        """
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
        """
        @summary Sets a custom origin header.
        
        @param request: SetReqHeaderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetReqHeaderConfigResponse
        """
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
        """
        @summary Sets a custom origin header.
        
        @param request: SetReqHeaderConfigRequest
        @return: SetReqHeaderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_req_header_config_with_options(request, runtime)

    async def set_req_header_config_async(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        """
        @summary Sets a custom origin header.
        
        @param request: SetReqHeaderConfigRequest
        @return: SetReqHeaderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_req_header_config_with_options_async(request, runtime)

    def set_waiting_room_config_with_options(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        """
        @summary Configures the virtual waiting room feature for an accelerated domain name. This operation is available only for accelerated domain names of the Dynamic CDN workload type.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetWaitingRoomConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetWaitingRoomConfigResponse
        """
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
        """
        @summary Configures the virtual waiting room feature for an accelerated domain name. This operation is available only for accelerated domain names of the Dynamic CDN workload type.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetWaitingRoomConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetWaitingRoomConfigResponse
        """
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
        """
        @summary Configures the virtual waiting room feature for an accelerated domain name. This operation is available only for accelerated domain names of the Dynamic CDN workload type.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetWaitingRoomConfigRequest
        @return: SetWaitingRoomConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_waiting_room_config_with_options(request, runtime)

    async def set_waiting_room_config_async(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        """
        @summary Configures the virtual waiting room feature for an accelerated domain name. This operation is available only for accelerated domain names of the Dynamic CDN workload type.
        
        @description > You can call this operation up to 30 times per second per account.
        
        @param request: SetWaitingRoomConfigRequest
        @return: SetWaitingRoomConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_waiting_room_config_with_options_async(request, runtime)

    def start_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
        """
        @summary Enables a disabled domain name. After the domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If the domain name is in an invalid state or you have an overdue payment in your account, the domain name cannot be enabled.
        You can call this operation up to 100 times per second per account.
        
        @param request: StartCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCdnDomainResponse
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
        """
        @summary Enables a disabled domain name. After the domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If the domain name is in an invalid state or you have an overdue payment in your account, the domain name cannot be enabled.
        You can call this operation up to 100 times per second per account.
        
        @param request: StartCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCdnDomainResponse
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
        """
        @summary Enables a disabled domain name. After the domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If the domain name is in an invalid state or you have an overdue payment in your account, the domain name cannot be enabled.
        You can call this operation up to 100 times per second per account.
        
        @param request: StartCdnDomainRequest
        @return: StartCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_cdn_domain_with_options(request, runtime)

    async def start_cdn_domain_async(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
        """
        @summary Enables a disabled domain name. After the domain name is enabled, the value of the DomainStatus parameter is changed to Online.
        
        @description    If the domain name is in an invalid state or you have an overdue payment in your account, the domain name cannot be enabled.
        You can call this operation up to 100 times per second per account.
        
        @param request: StartCdnDomainRequest
        @return: StartCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_cdn_domain_with_options_async(request, runtime)

    def stop_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
        """
        @summary Disables an accelerated domain name. After the domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain is disabled, Alibaba Cloud CDN retains its information and routes all the requests that are destined for the accelerated domain to the origin server.
        You can call this operation up to 40 times per second per account.
        
        @param request: StopCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCdnDomainResponse
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
        """
        @summary Disables an accelerated domain name. After the domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain is disabled, Alibaba Cloud CDN retains its information and routes all the requests that are destined for the accelerated domain to the origin server.
        You can call this operation up to 40 times per second per account.
        
        @param request: StopCdnDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCdnDomainResponse
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
        """
        @summary Disables an accelerated domain name. After the domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain is disabled, Alibaba Cloud CDN retains its information and routes all the requests that are destined for the accelerated domain to the origin server.
        You can call this operation up to 40 times per second per account.
        
        @param request: StopCdnDomainRequest
        @return: StopCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cdn_domain_with_options(request, runtime)

    async def stop_cdn_domain_async(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
        """
        @summary Disables an accelerated domain name. After the domain name is disabled, the value of the DomainStatus parameter is changed to Offline.
        
        @description    After an accelerated domain is disabled, Alibaba Cloud CDN retains its information and routes all the requests that are destined for the accelerated domain to the origin server.
        You can call this operation up to 40 times per second per account.
        
        @param request: StopCdnDomainRequest
        @return: StopCdnDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_cdn_domain_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.TagResourcesResponse:
        """
        @summary Adds one or more tags to specific resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
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
        """
        @summary Adds one or more tags to specific resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
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
        """
        @summary Adds one or more tags to specific resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
    ) -> cdn_20180510_models.TagResourcesResponse:
        """
        @summary Adds one or more tags to specific resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
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
        """
        @summary Removes tags from specified resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
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
        """
        @summary Removes tags from specified resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
    ) -> cdn_20180510_models.UntagResourcesResponse:
        """
        @summary Removes tags from specified resources.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cdn_deliver_task_with_options(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
        """
        @summary Updates a tracking task.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCdnDeliverTaskResponse
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
        """
        @summary Updates a tracking task.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnDeliverTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCdnDeliverTaskResponse
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
        """
        @summary Updates a tracking task.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnDeliverTaskRequest
        @return: UpdateCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_deliver_task_with_options(request, runtime)

    async def update_cdn_deliver_task_async(
        self,
        request: cdn_20180510_models.UpdateCdnDeliverTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnDeliverTaskResponse:
        """
        @summary Updates a tracking task.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnDeliverTaskRequest
        @return: UpdateCdnDeliverTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cdn_deliver_task_with_options_async(request, runtime)

    def update_cdn_sub_task_with_options(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
        """
        @summary Updates one or more operations reports.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCdnSubTaskResponse
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
        """
        @summary Updates one or more operations reports.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCdnSubTaskResponse
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
        """
        @summary Updates one or more operations reports.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnSubTaskRequest
        @return: UpdateCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_sub_task_with_options(request, runtime)

    async def update_cdn_sub_task_async(
        self,
        request: cdn_20180510_models.UpdateCdnSubTaskRequest,
    ) -> cdn_20180510_models.UpdateCdnSubTaskResponse:
        """
        @summary Updates one or more operations reports.
        
        @description > You can call this operation up to three times per second per account.
        
        @param request: UpdateCdnSubTaskRequest
        @return: UpdateCdnSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cdn_sub_task_with_options_async(request, runtime)

    def update_fctrigger_with_options(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        """
        @summary Updates a specified Function Compute trigger.
        
        @param request: UpdateFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Updates a specified Function Compute trigger.
        
        @param request: UpdateFCTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFCTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        @summary Updates a specified Function Compute trigger.
        
        @param request: UpdateFCTriggerRequest
        @return: UpdateFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_fctrigger_with_options(request, runtime)

    async def update_fctrigger_async(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        """
        @summary Updates a specified Function Compute trigger.
        
        @param request: UpdateFCTriggerRequest
        @return: UpdateFCTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_fctrigger_with_options_async(request, runtime)

    def verify_domain_owner_with_options(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
        """
        @summary Verifies the ownership of a specified domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyDomainOwnerResponse
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
        """
        @summary Verifies the ownership of a specified domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyDomainOwnerResponse
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
        """
        @summary Verifies the ownership of a specified domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDomainOwnerRequest
        @return: VerifyDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    async def verify_domain_owner_async(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
        """
        @summary Verifies the ownership of a specified domain name.
        
        @description > You can call this operation up to 100 times per second per account.
        
        @param request: VerifyDomainOwnerRequest
        @return: VerifyDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_domain_owner_with_options_async(request, runtime)
