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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            self.do_rpcrequest('AddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            await self.do_rpcrequest_async('AddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            self.do_rpcrequest('AddDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            await self.do_rpcrequest_async('AddDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            self.do_rpcrequest('BatchAddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            await self.do_rpcrequest_async('BatchAddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            self.do_rpcrequest('BatchDeleteDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchDeleteDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            self.do_rpcrequest('BatchSetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            await self.do_rpcrequest_async('BatchSetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchSetDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchSetDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            self.do_rpcrequest('BatchStartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            await self.do_rpcrequest_async('BatchStartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            self.do_rpcrequest('BatchStopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            await self.do_rpcrequest_async('BatchStopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def commit_staging_routine_code_with_options(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            self.do_rpcrequest('CommitStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def commit_staging_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.CommitStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CommitStagingRoutineCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            await self.do_rpcrequest_async('CommitStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            self.do_rpcrequest('CreateDcdnCertificateSigningRequest', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_certificate_signing_request_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            await self.do_rpcrequest_async('CreateDcdnCertificateSigningRequest', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        tmp_req: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            self.do_rpcrequest('CreateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_deliver_task_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.CreateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDeliverTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            await self.do_rpcrequest_async('CreateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('CreateDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse(),
            await self.do_rpcrequest_async('CreateDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def create_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def create_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            self.do_rpcrequest('CreateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_sub_task_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            await self.do_rpcrequest_async('CreateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            self.do_rpcrequest('CreateRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            await self.do_rpcrequest_async('CreateRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_dcdn_deliver_task_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            self.do_rpcrequest('DeleteDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_deliver_task_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDeliverTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            await self.do_rpcrequest_async('DeleteDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            self.do_rpcrequest('DeleteDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            await self.do_rpcrequest_async('DeleteDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            self.do_rpcrequest('DeleteDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            await self.do_rpcrequest_async('DeleteDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            self.do_rpcrequest('DeleteDcdnIpaSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_ipa_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            await self.do_rpcrequest_async('DeleteDcdnIpaSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_dcdn_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            self.do_rpcrequest('DeleteDcdnSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            await self.do_rpcrequest_async('DeleteDcdnSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            self.do_rpcrequest('DeleteDcdnSpecificStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_specific_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            await self.do_rpcrequest_async('DeleteDcdnSpecificStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            self.do_rpcrequest('DeleteDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_sub_task_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            await self.do_rpcrequest_async('DeleteDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            self.do_rpcrequest('DeleteRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_routine_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            await self.do_rpcrequest_async('DeleteRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            self.do_rpcrequest('DeleteRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_routine_code_revision_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteRoutineCodeRevisionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            await self.do_rpcrequest_async('DeleteRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            self.do_rpcrequest('DeleteRoutineConfEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            await self.do_rpcrequest_async('DeleteRoutineConfEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_bgp_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnBgpBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_bgp_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnBgpBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnBgpTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_bgp_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnBgpTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            self.do_rpcrequest('DescribeDcdnBlockedRegions', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_blocked_regions_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBlockedRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnBlockedRegions', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            self.do_rpcrequest('DescribeDcdnCertificateDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_certificate_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            await self.do_rpcrequest_async('DescribeDcdnCertificateDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            self.do_rpcrequest('DescribeDcdnCertificateList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_certificate_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            await self.do_rpcrequest_async('DescribeDcdnCertificateList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_config_of_version_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            self.do_rpcrequest('DescribeDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            await self.do_rpcrequest_async('DescribeDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_deliver_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            self.do_rpcrequest('DescribeDcdnDeliverList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_deliver_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDeliverListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDeliverListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDeliverList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            self.do_rpcrequest('DescribeDcdnDomainByCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_by_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainByCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_domain_certificate_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            self.do_rpcrequest('DescribeDcdnDomainCertificateInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_certificate_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainCertificateInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            self.do_rpcrequest('DescribeDcdnDomainCname', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_cname_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainCname', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            self.do_rpcrequest('DescribeDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            self.do_rpcrequest('DescribeDcdnDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainHitRateData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainHitRateData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIpaBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_ipa_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainIpaBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIpaTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_ipa_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainIpaTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIspData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_isp_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainIspData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            self.do_rpcrequest('DescribeDcdnDomainLog', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_log_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainLog', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainMultiUsageData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_multi_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainMultiUsageData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainOriginBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_origin_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainOriginBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainOriginTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_origin_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainOriginTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            self.do_rpcrequest('DescribeDcdnDomainProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_property_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainPvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_pv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainPvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainQpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainQpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeBpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeBpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeByteHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeByteHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeDetailData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_detail_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeDetailData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeQpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeQpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeReqHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeReqHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRegionData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_region_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainRegionData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            self.do_rpcrequest('DescribeDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTopReferVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_top_refer_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainTopReferVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTopUrlVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_top_url_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainTopUrlVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_domain_uv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainUvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_uv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainUvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_https_domain_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            self.do_rpcrequest('DescribeDcdnHttpsDomainList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_https_domain_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            await self.do_rpcrequest_async('DescribeDcdnHttpsDomainList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            self.do_rpcrequest('DescribeDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            self.do_rpcrequest('DescribeDcdnIpaDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            await self.do_rpcrequest_async('DescribeDcdnIpaDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            self.do_rpcrequest('DescribeDcdnIpaService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            await self.do_rpcrequest_async('DescribeDcdnIpaService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            self.do_rpcrequest('DescribeDcdnIpaUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnIpaUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_ip_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            self.do_rpcrequest('DescribeDcdnIpInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ip_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            await self.do_rpcrequest_async('DescribeDcdnIpInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse(),
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryField', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_field_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse(),
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryField', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_field(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_field_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_regions_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryRegions', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_regions_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryRegions', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_regions(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_regions_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_regions_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_regions_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse(),
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_status(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_status_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_status_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_status_with_options_async(request, runtime)

    def describe_dcdn_refresh_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_refresh_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            await self.do_rpcrequest_async('DescribeDcdnRefreshQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshTaskById', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_refresh_task_by_id_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            await self.do_rpcrequest_async('DescribeDcdnRefreshTaskById', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshTasks', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_refresh_tasks_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            await self.do_rpcrequest_async('DescribeDcdnRefreshTasks', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            self.do_rpcrequest('DescribeDcdnRegionAndIsp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_region_and_isp_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            await self.do_rpcrequest_async('DescribeDcdnRegionAndIsp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            self.do_rpcrequest('DescribeDcdnReport', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_report_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            await self.do_rpcrequest_async('DescribeDcdnReport', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            self.do_rpcrequest('DescribeDcdnReportList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_report_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            await self.do_rpcrequest_async('DescribeDcdnReportList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_sec_func_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            self.do_rpcrequest('DescribeDcdnSecFuncInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_sec_func_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSecFuncInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            await self.do_rpcrequest_async('DescribeDcdnSecFuncInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            self.do_rpcrequest('DescribeDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            await self.do_rpcrequest_async('DescribeDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            self.do_rpcrequest('DescribeDcdnStagingIp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_staging_ip_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            await self.do_rpcrequest_async('DescribeDcdnStagingIp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            self.do_rpcrequest('DescribeDcdnSubList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_sub_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnSubListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnSubListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            await self.do_rpcrequest_async('DescribeDcdnSubList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            self.do_rpcrequest('DescribeDcdnTagResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_tag_resources_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            await self.do_rpcrequest_async('DescribeDcdnTagResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            self.do_rpcrequest('DescribeDcdnTopDomainsByFlow', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_top_domains_by_flow_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            await self.do_rpcrequest_async('DescribeDcdnTopDomainsByFlow', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            self.do_rpcrequest('DescribeDcdnUserBillHistory', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_bill_history_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserBillHistory', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            self.do_rpcrequest('DescribeDcdnUserBillType', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_bill_type_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserBillType', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            self.do_rpcrequest('DescribeDcdnUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            self.do_rpcrequest('DescribeDcdnUserDomainsByFunc', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_domains_by_func_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserDomainsByFunc', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            self.do_rpcrequest('DescribeDcdnUserQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dcdn_user_resource_package_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            self.do_rpcrequest('DescribeDcdnUserResourcePackage', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_resource_package_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserResourcePackage', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            self.do_rpcrequest('DescribeDcdnUserSecDrop', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_sec_drop_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserSecDrop', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            self.do_rpcrequest('DescribeDcdnUserSecDropByMinute', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_sec_drop_by_minute_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserSecDropByMinute', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            self.do_rpcrequest('DescribeDcdnUserTags', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_tags_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            await self.do_rpcrequest_async('DescribeDcdnUserTags', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            self.do_rpcrequest('DescribeDcdnVerifyContent', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_verify_content_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            await self.do_rpcrequest_async('DescribeDcdnVerifyContent', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            self.do_rpcrequest('DescribeDcdnWafDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_waf_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            await self.do_rpcrequest_async('DescribeDcdnWafDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_routine_with_options(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            self.do_rpcrequest('DescribeRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_routine_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            await self.do_rpcrequest_async('DescribeRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            self.do_rpcrequest('DescribeRoutineCanaryEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_routine_canary_envs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCanaryEnvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            await self.do_rpcrequest_async('DescribeRoutineCanaryEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            self.do_rpcrequest('DescribeRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_routine_code_revision_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineCodeRevisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineCodeRevisionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            await self.do_rpcrequest_async('DescribeRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            self.do_rpcrequest('DescribeRoutineSpec', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_routine_spec_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            await self.do_rpcrequest_async('DescribeRoutineSpec', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            self.do_rpcrequest('DescribeRoutineUserInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_routine_user_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeRoutineUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeRoutineUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            await self.do_rpcrequest_async('DescribeRoutineUserInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            self.do_rpcrequest('DescribeUserDcdnIpaStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_dcdn_ipa_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserDcdnIpaStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            self.do_rpcrequest('DescribeUserDcdnStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_dcdn_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserDcdnStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            self.do_rpcrequest('DescribeUserErStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_er_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserErStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserErStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserErStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            self.do_rpcrequest('DescribeUserLogserviceStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_logservice_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserLogserviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserLogserviceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserLogserviceStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def disable_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DisableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse(),
            await self.do_rpcrequest_async('DisableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def disable_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def disable_dcdn_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DisableDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_dcdn_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse(),
            await self.do_rpcrequest_async('DisableDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_offline_log_delivery_with_options(request, runtime)

    async def disable_dcdn_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_dcdn_offline_log_delivery_with_options_async(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            self.do_rpcrequest('EditRoutineConf', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            await self.do_rpcrequest_async('EditRoutineConf', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def enable_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('EnableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse(),
            await self.do_rpcrequest_async('EnableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def enable_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            self.do_rpcrequest('ModifyDCdnDomainSchdmByProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dcdn_domain_schdm_by_property_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            await self.do_rpcrequest_async('ModifyDCdnDomainSchdmByProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            self.do_rpcrequest('OpenDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            await self.do_rpcrequest_async('OpenDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            self.do_rpcrequest('PreloadDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preload_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            await self.do_rpcrequest_async('PreloadDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            self.do_rpcrequest('PublishDcdnStagingConfigToProduction', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_dcdn_staging_config_to_production_with_options_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            await self.do_rpcrequest_async('PublishDcdnStagingConfigToProduction', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            self.do_rpcrequest('PublishRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            await self.do_rpcrequest_async('PublishRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            self.do_rpcrequest('RefreshDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            await self.do_rpcrequest_async('RefreshDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            self.do_rpcrequest('RollbackDcdnStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_dcdn_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            await self.do_rpcrequest_async('RollbackDcdnStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            self.do_rpcrequest('SetDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            await self.do_rpcrequest_async('SetDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            self.do_rpcrequest('SetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            await self.do_rpcrequest_async('SetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_dcdn_domain_csrcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            self.do_rpcrequest('SetDcdnDomainCSRCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_csrcertificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            await self.do_rpcrequest_async('SetDcdnDomainCSRCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            self.do_rpcrequest('SetDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            await self.do_rpcrequest_async('SetDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            self.do_rpcrequest('SetRoutineSubdomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            await self.do_rpcrequest_async('SetRoutineSubdomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            self.do_rpcrequest('StartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            await self.do_rpcrequest_async('StartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            self.do_rpcrequest('StartDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            await self.do_rpcrequest_async('StartDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            self.do_rpcrequest('StopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            await self.do_rpcrequest_async('StopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            self.do_rpcrequest('StopDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            await self.do_rpcrequest_async('StopDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            self.do_rpcrequest('TagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            await self.do_rpcrequest_async('TagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            self.do_rpcrequest('UntagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            await self.do_rpcrequest_async('UntagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        tmp_req: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.UpdateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            self.do_rpcrequest('UpdateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_deliver_task_with_options_async(
        self,
        tmp_req: dcdn_20180115_models.UpdateDcdnDeliverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDeliverTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.UpdateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            await self.do_rpcrequest_async('UpdateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            self.do_rpcrequest('UpdateDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            await self.do_rpcrequest_async('UpdateDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            self.do_rpcrequest('UpdateDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            await self.do_rpcrequest_async('UpdateDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_dcdn_sub_task_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            self.do_rpcrequest('UpdateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_sub_task_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnSubTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            await self.do_rpcrequest_async('UpdateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def upload_routine_code_with_options(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            self.do_rpcrequest('UploadRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.UploadRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadRoutineCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            await self.do_rpcrequest_async('UploadRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            self.do_rpcrequest('UploadStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_staging_routine_code_with_options_async(
        self,
        request: dcdn_20180115_models.UploadStagingRoutineCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UploadStagingRoutineCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            await self.do_rpcrequest_async('UploadStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            self.do_rpcrequest('VerifyDcdnDomainOwner', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_dcdn_domain_owner_with_options_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            await self.do_rpcrequest_async('VerifyDcdnDomainOwner', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
