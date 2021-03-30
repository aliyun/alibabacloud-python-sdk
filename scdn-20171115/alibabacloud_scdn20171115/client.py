# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_scdn20171115 import models as scdn_20171115_models
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
            'ap-northeast-1': 'scdn.aliyuncs.com',
            'ap-northeast-2-pop': 'scdn.aliyuncs.com',
            'ap-south-1': 'scdn.aliyuncs.com',
            'ap-southeast-1': 'scdn.aliyuncs.com',
            'ap-southeast-2': 'scdn.aliyuncs.com',
            'ap-southeast-3': 'scdn.aliyuncs.com',
            'ap-southeast-5': 'scdn.aliyuncs.com',
            'cn-beijing': 'scdn.aliyuncs.com',
            'cn-beijing-finance-1': 'scdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'scdn.aliyuncs.com',
            'cn-beijing-gov-1': 'scdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'scdn.aliyuncs.com',
            'cn-chengdu': 'scdn.aliyuncs.com',
            'cn-edge-1': 'scdn.aliyuncs.com',
            'cn-fujian': 'scdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'scdn.aliyuncs.com',
            'cn-hangzhou': 'scdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'scdn.aliyuncs.com',
            'cn-hangzhou-finance': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'scdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'scdn.aliyuncs.com',
            'cn-hongkong': 'scdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'scdn.aliyuncs.com',
            'cn-huhehaote': 'scdn.aliyuncs.com',
            'cn-north-2-gov-1': 'scdn.aliyuncs.com',
            'cn-qingdao': 'scdn.aliyuncs.com',
            'cn-qingdao-nebula': 'scdn.aliyuncs.com',
            'cn-shanghai': 'scdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'scdn.aliyuncs.com',
            'cn-shanghai-inner': 'scdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'scdn.aliyuncs.com',
            'cn-shenzhen': 'scdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'scdn.aliyuncs.com',
            'cn-shenzhen-inner': 'scdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'scdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'scdn.aliyuncs.com',
            'cn-wuhan': 'scdn.aliyuncs.com',
            'cn-yushanfang': 'scdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'scdn.aliyuncs.com',
            'cn-zhangjiakou': 'scdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'scdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'scdn.aliyuncs.com',
            'eu-central-1': 'scdn.aliyuncs.com',
            'eu-west-1': 'scdn.aliyuncs.com',
            'eu-west-1-oxs': 'scdn.aliyuncs.com',
            'me-east-1': 'scdn.aliyuncs.com',
            'rus-west-1-pop': 'scdn.aliyuncs.com',
            'us-east-1': 'scdn.aliyuncs.com',
            'us-west-1': 'scdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('scdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['ResourceGroupId'] = request.resource_group_id
        query['Sources'] = request.sources
        query['CheckUrl'] = request.check_url
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.AddScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['ResourceGroupId'] = request.resource_group_id
        query['Sources'] = request.sources
        query['CheckUrl'] = request.check_url
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.AddScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_scdn_domain(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scdn_domain_with_options(request, runtime)

    async def add_scdn_domain_async(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scdn_domain_with_options_async(request, runtime)

    def batch_delete_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainNames'] = request.domain_names
        query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeleteScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainNames'] = request.domain_names
        query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeleteScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_scdn_domain_configs(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_scdn_domain_configs_with_options(request, runtime)

    async def batch_delete_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_scdn_domain_configs_with_options_async(request, runtime)

    def batch_set_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainNames'] = request.domain_names
        query['Functions'] = request.functions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchSetScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchSetScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainNames'] = request.domain_names
        query['Functions'] = request.functions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchSetScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchSetScdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_scdn_domain_configs(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_scdn_domain_configs_with_options(request, runtime)

    async def batch_set_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_scdn_domain_configs_with_options_async(request, runtime)

    def batch_update_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['Sources'] = request.sources
        query['ResourceGroupId'] = request.resource_group_id
        query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchUpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchUpdateScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['Sources'] = request.sources
        query['ResourceGroupId'] = request.resource_group_id
        query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchUpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchUpdateScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_scdn_domain(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_update_scdn_domain_with_options(request, runtime)

    async def batch_update_scdn_domain_async(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_scdn_domain_with_options_async(request, runtime)

    def check_scdn_service_with_options(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.CheckScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.CheckScdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_scdn_service(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_scdn_service_with_options(request, runtime)

    async def check_scdn_service_async(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_scdn_service_with_options_async(request, runtime)

    def delete_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['OwnerAccount'] = request.owner_account
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scdn_domain(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_domain_with_options(request, runtime)

    async def delete_scdn_domain_async(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scdn_domain_with_options_async(request, runtime)

    def delete_scdn_specific_config_with_options(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['ConfigId'] = request.config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScdnSpecificConfig',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scdn_specific_config_with_options_async(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['ConfigId'] = request.config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScdnSpecificConfig',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scdn_specific_config(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_specific_config_with_options(request, runtime)

    async def delete_scdn_specific_config_async(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scdn_specific_config_with_options_async(request, runtime)

    def describe_scdn_cc_qps_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcQpsInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcQpsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_cc_qps_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcQpsInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcQpsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_cc_qps_info(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_qps_info_with_options(request, runtime)

    async def describe_scdn_cc_qps_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_qps_info_with_options_async(request, runtime)

    def describe_scdn_cc_top_ip_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopIp',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_cc_top_ip_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopIp',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_cc_top_ip(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_ip_with_options(request, runtime)

    async def describe_scdn_cc_top_ip_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_top_ip_with_options_async(request, runtime)

    def describe_scdn_cc_top_url_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopUrl',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_cc_top_url_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopUrl',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_cc_top_url(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_url_with_options(request, runtime)

    async def describe_scdn_cc_top_url_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_top_url_with_options_async(request, runtime)

    def describe_scdn_certificate_detail_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['CertName'] = request.cert_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_certificate_detail_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['CertName'] = request.cert_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_certificate_detail(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_detail_with_options(request, runtime)

    async def describe_scdn_certificate_detail_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_certificate_detail_with_options_async(request, runtime)

    def describe_scdn_certificate_list_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateList',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_certificate_list_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateList',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_certificate_list(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_list_with_options(request, runtime)

    async def describe_scdn_certificate_list_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_certificate_list_with_options_async(request, runtime)

    def describe_scdn_ddo_sinfo_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_ddo_sinfo_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_ddo_sinfo(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_sinfo_with_options(request, runtime)

    async def describe_scdn_ddo_sinfo_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_ddo_sinfo_with_options_async(request, runtime)

    def describe_scdn_ddo_straffic_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSTrafficInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_ddo_straffic_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSTrafficInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_ddo_straffic_info(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_straffic_info_with_options(request, runtime)

    async def describe_scdn_ddo_straffic_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_ddo_straffic_info_with_options_async(request, runtime)

    def describe_scdn_domain_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_certificate_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCertificateInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_certificate_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCertificateInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_certificate_info(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_certificate_info_with_options(request, runtime)

    async def describe_scdn_domain_certificate_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_scdn_domain_cname_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCname',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_cname_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCname',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_cname(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_cname_with_options(request, runtime)

    async def describe_scdn_domain_cname_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_cname_with_options_async(request, runtime)

    def describe_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['FunctionNames'] = request.function_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_configs(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_configs_with_options(request, runtime)

    async def describe_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_configs_with_options_async(request, runtime)

    def describe_scdn_domain_detail_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_detail_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_detail(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_detail_with_options(request, runtime)

    async def describe_scdn_domain_detail_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_detail_with_options_async(request, runtime)

    def describe_scdn_domain_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_http_code_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_http_code_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_http_code_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_http_code_data_with_options(request, runtime)

    async def describe_scdn_domain_http_code_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_scdn_domain_isp_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainIspData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainIspDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_isp_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainIspData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainIspDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_isp_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_isp_data_with_options(request, runtime)

    async def describe_scdn_domain_isp_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_isp_data_with_options_async(request, runtime)

    def describe_scdn_domain_log_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainLog',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_log_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainLog',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_log(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_log_with_options(request, runtime)

    async def describe_scdn_domain_log_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_log_with_options_async(request, runtime)

    def describe_scdn_domain_origin_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_origin_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_origin_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_origin_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_origin_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_origin_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_origin_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_origin_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_pv_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainPvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_pv_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainPvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_pv_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_pv_data_with_options(request, runtime)

    async def describe_scdn_domain_pv_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_pv_data_with_options_async(request, runtime)

    def describe_scdn_domain_qps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_qps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_qps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_qps_data_with_options(request, runtime)

    async def describe_scdn_domain_qps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_qps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeByteHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeByteHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_byte_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_http_code_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_http_code_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_http_code_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_qps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_qps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_qps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_qps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeReqHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeReqHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_req_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_src_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_src_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_src_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_src_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_src_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_real_time_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_region_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRegionData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_region_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRegionData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_region_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_region_data_with_options(request, runtime)

    async def describe_scdn_domain_region_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_region_data_with_options_async(request, runtime)

    def describe_scdn_domain_top_refer_visit_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopReferVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_top_refer_visit_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopReferVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_top_refer_visit(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_scdn_domain_top_refer_visit_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_scdn_domain_top_url_visit_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopUrlVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_top_url_visit_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopUrlVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_top_url_visit(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_scdn_domain_top_url_visit_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_scdn_domain_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Interval'] = request.interval
        query['IspNameEn'] = request.isp_name_en
        query['LocationNameEn'] = request.location_name_en
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_uv_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainUvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_domain_uv_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['DomainName'] = request.domain_name
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainUvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_domain_uv_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_uv_data_with_options(request, runtime)

    async def describe_scdn_domain_uv_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_uv_data_with_options_async(request, runtime)

    def describe_scdn_refresh_quota_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_refresh_quota_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_refresh_quota(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_quota_with_options(request, runtime)

    async def describe_scdn_refresh_quota_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_refresh_quota_with_options_async(request, runtime)

    def describe_scdn_refresh_tasks_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['TaskId'] = request.task_id
        query['ObjectPath'] = request.object_path
        query['PageNumber'] = request.page_number
        query['ObjectType'] = request.object_type
        query['DomainName'] = request.domain_name
        query['Status'] = request.status
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshTasks',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_refresh_tasks_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['TaskId'] = request.task_id
        query['ObjectPath'] = request.object_path
        query['PageNumber'] = request.page_number
        query['ObjectType'] = request.object_type
        query['DomainName'] = request.domain_name
        query['Status'] = request.status
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshTasks',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_refresh_tasks(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_tasks_with_options(request, runtime)

    async def describe_scdn_refresh_tasks_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_refresh_tasks_with_options_async(request, runtime)

    def describe_scdn_service_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_service(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_service_with_options(request, runtime)

    async def describe_scdn_service_async(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_service_with_options_async(request, runtime)

    def describe_scdn_top_domains_by_flow_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Product'] = request.product
        query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnTopDomainsByFlow',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_top_domains_by_flow_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Product'] = request.product
        query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnTopDomainsByFlow',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_top_domains_by_flow(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_scdn_top_domains_by_flow_async(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_scdn_user_domains_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['DomainName'] = request.domain_name
        query['DomainStatus'] = request.domain_status
        query['DomainSearchType'] = request.domain_search_type
        query['CheckDomainShow'] = request.check_domain_show
        query['ResourceGroupId'] = request.resource_group_id
        query['ChangeStartTime'] = request.change_start_time
        query['ChangeEndTime'] = request.change_end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserDomains',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_user_domains_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['DomainName'] = request.domain_name
        query['DomainStatus'] = request.domain_status
        query['DomainSearchType'] = request.domain_search_type
        query['CheckDomainShow'] = request.check_domain_show
        query['ResourceGroupId'] = request.resource_group_id
        query['ChangeStartTime'] = request.change_start_time
        query['ChangeEndTime'] = request.change_end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserDomains',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_user_domains(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_domains_with_options(request, runtime)

    async def describe_scdn_user_domains_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_domains_with_options_async(request, runtime)

    def describe_scdn_user_protect_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserProtectInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserProtectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_user_protect_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserProtectInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserProtectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_user_protect_info(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_protect_info_with_options(request, runtime)

    async def describe_scdn_user_protect_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_protect_info_with_options_async(request, runtime)

    def describe_scdn_user_quota_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scdn_user_quota_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scdn_user_quota(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_quota_with_options(request, runtime)

    async def describe_scdn_user_quota_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_quota_with_options_async(request, runtime)

    def open_scdn_service_with_options(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['Bandwidth'] = request.bandwidth
        query['ProtectType'] = request.protect_type
        query['DDoSBasic'] = request.ddo_sbasic
        query['ElasticProtection'] = request.elastic_protection
        query['CcProtection'] = request.cc_protection
        query['DomainCount'] = request.domain_count
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.OpenScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['Bandwidth'] = request.bandwidth
        query['ProtectType'] = request.protect_type
        query['DDoSBasic'] = request.ddo_sbasic
        query['ElasticProtection'] = request.elastic_protection
        query['CcProtection'] = request.cc_protection
        query['DomainCount'] = request.domain_count
        query['StartDate'] = request.start_date
        query['EndDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.OpenScdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_scdn_service(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_scdn_service_with_options(request, runtime)

    async def open_scdn_service_async(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_scdn_service_with_options_async(request, runtime)

    def preload_scdn_object_caches_with_options(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ObjectPath'] = request.object_path
        query['Area'] = request.area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PreloadScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.PreloadScdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_scdn_object_caches_with_options_async(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ObjectPath'] = request.object_path
        query['Area'] = request.area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PreloadScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.PreloadScdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_scdn_object_caches(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_scdn_object_caches_with_options(request, runtime)

    async def preload_scdn_object_caches_async(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_scdn_object_caches_with_options_async(request, runtime)

    def refresh_scdn_object_caches_with_options(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ObjectPath'] = request.object_path
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.RefreshScdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_scdn_object_caches_with_options_async(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ObjectPath'] = request.object_path
        query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.RefreshScdnObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_scdn_object_caches(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_scdn_object_caches_with_options(request, runtime)

    async def refresh_scdn_object_caches_async(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_scdn_object_caches_with_options_async(request, runtime)

    def set_scdn_bot_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnBotInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnBotInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scdn_bot_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnBotInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnBotInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scdn_bot_info(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_bot_info_with_options(request, runtime)

    async def set_scdn_bot_info_async(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_bot_info_with_options_async(request, runtime)

    def set_scdn_cc_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnCcInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnCcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scdn_cc_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnCcInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnCcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scdn_cc_info(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_cc_info_with_options(request, runtime)

    async def set_scdn_cc_info_async(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_cc_info_with_options_async(request, runtime)

    def set_scdn_ddo_sinfo_with_options(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDDoSInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scdn_ddo_sinfo_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDDoSInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scdn_ddo_sinfo(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_ddo_sinfo_with_options(request, runtime)

    async def set_scdn_ddo_sinfo_async(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_ddo_sinfo_with_options_async(request, runtime)

    def set_scdn_domain_biz_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDomainBizInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainBizInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scdn_domain_biz_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDomainBizInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainBizInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scdn_domain_biz_info(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_biz_info_with_options(request, runtime)

    async def set_scdn_domain_biz_info_async(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_domain_biz_info_with_options_async(request, runtime)

    def set_scdn_domain_certificate_with_options(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['CertType'] = request.cert_type
        query['CertName'] = request.cert_name
        query['SSLProtocol'] = request.sslprotocol
        query['SSLPub'] = request.sslpub
        query['SSLPri'] = request.sslpri
        query['Region'] = request.region
        query['ForceSet'] = request.force_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetScdnDomainCertificate',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scdn_domain_certificate_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['CertType'] = request.cert_type
        query['CertName'] = request.cert_name
        query['SSLProtocol'] = request.sslprotocol
        query['SSLPub'] = request.sslpub
        query['SSLPri'] = request.sslpri
        query['Region'] = request.region
        query['ForceSet'] = request.force_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetScdnDomainCertificate',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scdn_domain_certificate(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_certificate_with_options(request, runtime)

    async def set_scdn_domain_certificate_async(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_domain_certificate_with_options_async(request, runtime)

    def start_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StartScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StartScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_scdn_domain(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_scdn_domain_with_options(request, runtime)

    async def start_scdn_domain_async(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_scdn_domain_with_options_async(request, runtime)

    def stop_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StopScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StopScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_scdn_domain(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_scdn_domain_with_options(request, runtime)

    async def stop_scdn_domain_async(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_scdn_domain_with_options_async(request, runtime)

    def update_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['Sources'] = request.sources
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.UpdateScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['DomainName'] = request.domain_name
        query['Sources'] = request.sources
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.UpdateScdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scdn_domain(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scdn_domain_with_options(request, runtime)

    async def update_scdn_domain_async(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scdn_domain_with_options_async(request, runtime)
