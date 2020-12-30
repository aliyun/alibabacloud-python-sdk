# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.AddCdnDomainResponse().from_map(
            self.do_rpcrequest('AddCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.AddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.AddCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('AddCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.AddFCTriggerResponse().from_map(
            self.do_rpcrequest('AddFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.AddFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.AddFCTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.AddFCTriggerResponse().from_map(
            await self.do_rpcrequest_async('AddFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchAddCdnDomainResponse().from_map(
            self.do_rpcrequest('BatchAddCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchAddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchAddCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchAddCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchAddCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_set_cdn_domain_config_with_options(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchSetCdnDomainConfigResponse().from_map(
            self.do_rpcrequest('BatchSetCdnDomainConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_cdn_domain_config_with_options_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchSetCdnDomainConfigResponse().from_map(
            await self.do_rpcrequest_async('BatchSetCdnDomainConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse().from_map(
            self.do_rpcrequest('BatchSetCdnDomainServerCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_cdn_domain_server_certificate_with_options_async(
        self,
        request: cdn_20180510_models.BatchSetCdnDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse().from_map(
            await self.do_rpcrequest_async('BatchSetCdnDomainServerCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchStartCdnDomainResponse().from_map(
            self.do_rpcrequest('BatchStartCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_start_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchStartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStartCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchStartCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStartCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchStopCdnDomainResponse().from_map(
            self.do_rpcrequest('BatchStopCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchStopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchStopCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchStopCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStopCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchUpdateCdnDomainResponse().from_map(
            self.do_rpcrequest('BatchUpdateCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_update_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.BatchUpdateCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.BatchUpdateCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.BatchUpdateCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchUpdateCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateCdnCertificateSigningRequestResponse().from_map(
            self.do_rpcrequest('CreateCdnCertificateSigningRequest', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cdn_certificate_signing_request_with_options_async(
        self,
        request: cdn_20180510_models.CreateCdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateCdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateCdnCertificateSigningRequestResponse().from_map(
            await self.do_rpcrequest_async('CreateCdnCertificateSigningRequest', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_illegal_url_export_task_with_options(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateIllegalUrlExportTaskResponse().from_map(
            self.do_rpcrequest('CreateIllegalUrlExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_illegal_url_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateIllegalUrlExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateIllegalUrlExportTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateIllegalUrlExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.CreateRealTimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('CreateRealTimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_real_time_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.CreateRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.CreateRealTimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('CreateRealTimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateUsageDetailDataExportTaskResponse().from_map(
            self.do_rpcrequest('CreateUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUsageDetailDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateUsageDetailDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateUserUsageDataExportTaskResponse().from_map(
            self.do_rpcrequest('CreateUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.CreateUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.CreateUserUsageDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.CreateUserUsageDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_cdn_domain_with_options(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteCdnDomainResponse().from_map(
            self.do_rpcrequest('DeleteCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.DeleteCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteFCTriggerResponse().from_map(
            self.do_rpcrequest('DeleteFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.DeleteFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteFCTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteFCTriggerResponse().from_map(
            await self.do_rpcrequest_async('DeleteFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DeleteRealtimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('DeleteRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DeleteRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DeleteRealtimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DeleteRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteSpecificConfigResponse().from_map(
            self.do_rpcrequest('DeleteSpecificConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_specific_config_with_options_async(
        self,
        request: cdn_20180510_models.DeleteSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteSpecificConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteSpecificConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteSpecificStagingConfigResponse().from_map(
            self.do_rpcrequest('DeleteSpecificStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_specific_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.DeleteSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteSpecificStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteSpecificStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse().from_map(
            self.do_rpcrequest('DeleteUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteUserUsageDataExportTaskResponse().from_map(
            self.do_rpcrequest('DeleteUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DeleteUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DeleteUserUsageDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DeleteUserUsageDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse().from_map(
            self.do_rpcrequest('DescribeActiveVersionOfConfigGroup', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_active_version_of_config_group_with_options_async(
        self,
        request: cdn_20180510_models.DescribeActiveVersionOfConfigGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeActiveVersionOfConfigGroup', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cdn_certificate_detail_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnCertificateDetailResponse().from_map(
            self.do_rpcrequest('DescribeCdnCertificateDetail', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_certificate_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnCertificateDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnCertificateDetail', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnCertificateListResponse().from_map(
            self.do_rpcrequest('DescribeCdnCertificateList', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_certificate_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnCertificateListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnCertificateList', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cdn_domain_by_certificate_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainByCertificateResponse().from_map(
            self.do_rpcrequest('DescribeCdnDomainByCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_domain_by_certificate_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainByCertificateResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnDomainByCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('DescribeCdnDomainConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_domain_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnDomainConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeCdnDomainDetail', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_domain_detail_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnDomainDetail', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainLogsResponse().from_map(
            self.do_rpcrequest('DescribeCdnDomainLogs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_domain_logs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnDomainLogs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainStagingConfigResponse().from_map(
            self.do_rpcrequest('DescribeCdnDomainStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_domain_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnDomainStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnDomainStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnHttpsDomainListResponse().from_map(
            self.do_rpcrequest('DescribeCdnHttpsDomainList', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_https_domain_list_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnHttpsDomainListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnHttpsDomainList', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnRegionAndIspResponse().from_map(
            self.do_rpcrequest('DescribeCdnRegionAndIsp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_region_and_isp_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnRegionAndIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnRegionAndIspResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnRegionAndIsp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cdn_service_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnServiceResponse().from_map(
            self.do_rpcrequest('DescribeCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_service_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cdn_user_bill_history_with_options(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillHistoryResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserBillHistory', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_bill_history_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserBillHistory', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillPredictionResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserBillPrediction', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_bill_prediction_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillPredictionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillPredictionResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserBillPrediction', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillTypeResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserBillType', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_bill_type_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserBillTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserBillTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserBillType', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserConfigsResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserDomainsByFunc', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_domains_by_func_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserDomainsByFunc', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserQuotaResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserQuota', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_quota_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserQuota', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserResourcePackageResponse().from_map(
            self.do_rpcrequest('DescribeCdnUserResourcePackage', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_user_resource_package_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnUserResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnUserResourcePackage', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnWafDomainResponse().from_map(
            self.do_rpcrequest('DescribeCdnWafDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cdn_waf_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCdnWafDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeCdnWafDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeCdnWafDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeCertificateInfoByIDResponse().from_map(
            self.do_rpcrequest('DescribeCertificateInfoByID', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_certificate_info_by_idwith_options_async(
        self,
        request: cdn_20180510_models.DescribeCertificateInfoByIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCertificateInfoByIDResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeCertificateInfoByIDResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertificateInfoByID', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def describe_config_of_version_with_options(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeConfigOfVersionResponse().from_map(
            self.do_rpcrequest('DescribeConfigOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_config_of_version_with_options_async(
        self,
        request: cdn_20180510_models.DescribeConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeConfigOfVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeConfigOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeCustomLogConfigResponse().from_map(
            self.do_rpcrequest('DescribeCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeCustomLogConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainAverageResponseTimeResponse().from_map(
            self.do_rpcrequest('DescribeDomainAverageResponseTime', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_average_response_time_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainAverageResponseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainAverageResponseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainAverageResponseTimeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAverageResponseTime', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataByLayerResponse().from_map(
            self.do_rpcrequest('DescribeDomainBpsDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_bps_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByLayerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataByLayerResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainBpsDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse().from_map(
            self.do_rpcrequest('DescribeDomainBpsDataByTimeStamp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainBpsDataByTimeStamp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainCcActivityLogResponse().from_map(
            self.do_rpcrequest('DescribeDomainCcActivityLog', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_cc_activity_log_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCcActivityLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCcActivityLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainCcActivityLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainCcActivityLog', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainCertificateInfoResponse().from_map(
            self.do_rpcrequest('DescribeDomainCertificateInfo', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_certificate_info_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainCertificateInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainCertificateInfo', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainCustomLogConfigResponse().from_map(
            self.do_rpcrequest('DescribeDomainCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainCustomLogConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainDetailDataByLayerResponse().from_map(
            self.do_rpcrequest('DescribeDomainDetailDataByLayer', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_detail_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainDetailDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainDetailDataByLayerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainDetailDataByLayerResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainDetailDataByLayer', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainFileSizeProportionData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_file_size_proportion_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainFileSizeProportionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainFileSizeProportionData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainHitRateData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainHitRateData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse().from_map(
            self.do_rpcrequest('DescribeDomainHttpCodeDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_http_code_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainHttpCodeDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainHttpCodeDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainISPDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainISPData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_ispdata_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainISPDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainISPDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainISPData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainMax95BpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainMax95BpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_max_95bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainMax95BpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainMax95BpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainMax95BpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainMax95BpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_names_of_version_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainNamesOfVersionResponse().from_map(
            self.do_rpcrequest('DescribeDomainNamesOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_names_of_version_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainNamesOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainNamesOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainNamesOfVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainNamesOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainPathDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainPathData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_path_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainPathDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPathDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainPathDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainPathData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainPvDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainPvData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_pv_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainPvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainPvData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainQpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainQpsDataByLayerResponse().from_map(
            self.do_rpcrequest('DescribeDomainQpsDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_qps_data_by_layer_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainQpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainQpsDataByLayerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainQpsDataByLayerResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainQpsDataByLayer', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeBpsData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeBpsData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeByteHitRateData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeByteHitRateData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeDetailData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_detail_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeDetailData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_realtime_log_delivery_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def describe_domain_real_time_qps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeQpsData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeQpsData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeReqHitRateData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeReqHitRateData', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeSrcBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_src_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeSrcBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeSrcHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeSrcHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeSrcTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeSrcTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRealTimeTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_real_time_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRealTimeTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_region_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRegionDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainRegionData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_region_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainRegionDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRegionData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainReqHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainReqHitRateData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_req_hit_rate_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainReqHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainReqHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainReqHitRateData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domains_by_source_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainsBySourceResponse().from_map(
            self.do_rpcrequest('DescribeDomainsBySource', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_by_source_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainsBySourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainsBySource', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_src_bps_data_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainSrcBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_src_bps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSrcBpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainSrcHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_src_http_code_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSrcHttpCodeData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainSrcQpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_src_qps_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSrcQpsData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse().from_map(
            self.do_rpcrequest('DescribeDomainSrcTopUrlVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_src_top_url_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSrcTopUrlVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainSrcTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_src_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainSrcTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainSrcTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domains_usage_by_day_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainsUsageByDayResponse().from_map(
            self.do_rpcrequest('DescribeDomainsUsageByDay', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_usage_by_day_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainsUsageByDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainsUsageByDayResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainsUsageByDay', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_top_client_ip_visit_with_options(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopClientIpVisitResponse().from_map(
            self.do_rpcrequest('DescribeDomainTopClientIpVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_top_client_ip_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopClientIpVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopClientIpVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopClientIpVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainTopClientIpVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopReferVisitResponse().from_map(
            self.do_rpcrequest('DescribeDomainTopReferVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_top_refer_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopReferVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainTopReferVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopUrlVisitResponse().from_map(
            self.do_rpcrequest('DescribeDomainTopUrlVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_top_url_visit_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTopUrlVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainTopUrlVisit', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_traffic_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainTrafficData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainUsageDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainUsageData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_usage_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainUsageDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainUsageData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainUvDataResponse().from_map(
            self.do_rpcrequest('DescribeDomainUvData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_uv_data_with_options_async(
        self,
        request: cdn_20180510_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeDomainUvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainUvData', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_fctrigger_with_options(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeFCTriggerResponse().from_map(
            self.do_rpcrequest('DescribeFCTrigger', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.DescribeFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeFCTriggerResponse().from_map(
            await self.do_rpcrequest_async('DescribeFCTrigger', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeIllegalUrlExportTaskResponse().from_map(
            self.do_rpcrequest('DescribeIllegalUrlExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_illegal_url_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeIllegalUrlExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIllegalUrlExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeIllegalUrlExportTaskResponse().from_map(
            await self.do_rpcrequest_async('DescribeIllegalUrlExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeIpInfoResponse().from_map(
            self.do_rpcrequest('DescribeIpInfo', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_info_with_options_async(
        self,
        request: cdn_20180510_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeIpInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpInfo', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeL2VipsByDomainResponse().from_map(
            self.do_rpcrequest('DescribeL2VipsByDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_l2vips_by_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeL2VipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeL2VipsByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeL2VipsByDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeL2VipsByDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse().from_map(
            self.do_rpcrequest('DescribeRangeDataByLocateAndIspService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_range_data_by_locate_and_isp_service_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeRangeDataByLocateAndIspService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRealtimeDeliveryAccResponse().from_map(
            self.do_rpcrequest('DescribeRealtimeDeliveryAcc', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_realtime_delivery_acc_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRealtimeDeliveryAccResponse().from_map(
            await self.do_rpcrequest_async('DescribeRealtimeDeliveryAcc', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshQuotaResponse().from_map(
            self.do_rpcrequest('DescribeRefreshQuota', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_refresh_quota_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeRefreshQuota', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshTaskByIdResponse().from_map(
            self.do_rpcrequest('DescribeRefreshTaskById', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_refresh_task_by_id_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTaskByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshTaskByIdResponse().from_map(
            await self.do_rpcrequest_async('DescribeRefreshTaskById', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshTasksResponse().from_map(
            self.do_rpcrequest('DescribeRefreshTasks', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_refresh_tasks_with_options_async(
        self,
        request: cdn_20180510_models.DescribeRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeRefreshTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeRefreshTasks', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeStagingIpResponse().from_map(
            self.do_rpcrequest('DescribeStagingIp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_staging_ip_with_options_async(
        self,
        request: cdn_20180510_models.DescribeStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeStagingIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeStagingIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeStagingIp', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeTagResourcesResponse().from_map(
            self.do_rpcrequest('DescribeTagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_resources_with_options_async(
        self,
        request: cdn_20180510_models.DescribeTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('DescribeTagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeTopDomainsByFlowResponse().from_map(
            self.do_rpcrequest('DescribeTopDomainsByFlow', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_top_domains_by_flow_with_options_async(
        self,
        request: cdn_20180510_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeTopDomainsByFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeTopDomainsByFlow', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserCertificateExpireCountResponse().from_map(
            self.do_rpcrequest('DescribeUserCertificateExpireCount', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_certificate_expire_count_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserCertificateExpireCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserCertificateExpireCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserCertificateExpireCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserCertificateExpireCount', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserConfigsResponse().from_map(
            self.do_rpcrequest('DescribeUserConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_configs_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserConfigs', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserDomainsResponse().from_map(
            self.do_rpcrequest('DescribeUserDomains', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_domains_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserDomains', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserTagsResponse().from_map(
            self.do_rpcrequest('DescribeUserTags', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_tags_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserTags', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserUsageDataExportTaskResponse().from_map(
            self.do_rpcrequest('DescribeUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_usage_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserUsageDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserUsageDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse().from_map(
            self.do_rpcrequest('DescribeUserUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_usage_detail_data_export_task_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserUsageDetailDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserUsageDetailDataExportTask', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DescribeUserVipsByDomainResponse().from_map(
            self.do_rpcrequest('DescribeUserVipsByDomain', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_user_vips_by_domain_with_options_async(
        self,
        request: cdn_20180510_models.DescribeUserVipsByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeUserVipsByDomainResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DescribeUserVipsByDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserVipsByDomain', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeVerifyContentResponse().from_map(
            self.do_rpcrequest('DescribeVerifyContent', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_verify_content_with_options_async(
        self,
        request: cdn_20180510_models.DescribeVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DescribeVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.DescribeVerifyContentResponse().from_map(
            await self.do_rpcrequest_async('DescribeVerifyContent', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.DisableRealtimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('DisableRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def disable_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.DisableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.DisableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.DisableRealtimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DisableRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.EnableRealtimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('EnableRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def enable_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.EnableRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.EnableRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.EnableRealtimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('EnableRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ListDomainsByLogConfigIdResponse().from_map(
            self.do_rpcrequest('ListDomainsByLogConfigId', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_domains_by_log_config_id_with_options_async(
        self,
        request: cdn_20180510_models.ListDomainsByLogConfigIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListDomainsByLogConfigIdResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ListDomainsByLogConfigIdResponse().from_map(
            await self.do_rpcrequest_async('ListDomainsByLogConfigId', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ListFCTriggerResponse().from_map(
            self.do_rpcrequest('ListFCTrigger', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.ListFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListFCTriggerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ListFCTriggerResponse().from_map(
            await self.do_rpcrequest_async('ListFCTrigger', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse().from_map(
            self.do_rpcrequest('ListRealtimeLogDeliveryDomains', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_realtime_log_delivery_domains_with_options_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse().from_map(
            await self.do_rpcrequest_async('ListRealtimeLogDeliveryDomains', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse().from_map(
            self.do_rpcrequest('ListRealtimeLogDeliveryInfos', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_realtime_log_delivery_infos_with_options_async(
        self,
        request: cdn_20180510_models.ListRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse().from_map(
            await self.do_rpcrequest_async('ListRealtimeLogDeliveryInfos', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ListUserCustomLogConfigResponse().from_map(
            self.do_rpcrequest('ListUserCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_user_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ListUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ListUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ListUserCustomLogConfigResponse().from_map(
            await self.do_rpcrequest_async('ListUserCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnDomainResponse().from_map(
            self.do_rpcrequest('ModifyCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('ModifyCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse().from_map(
            self.do_rpcrequest('ModifyCdnDomainSchdmByProperty', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cdn_domain_schdm_by_property_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse().from_map(
            await self.do_rpcrequest_async('ModifyCdnDomainSchdmByProperty', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_cdn_service_with_options(
        self,
        request: cdn_20180510_models.ModifyCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnServiceResponse().from_map(
            self.do_rpcrequest('ModifyCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cdn_service_with_options_async(
        self,
        request: cdn_20180510_models.ModifyCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyCdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.ModifyCdnServiceResponse().from_map(
            await self.do_rpcrequest_async('ModifyCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cdn_service(
        self,
        request: cdn_20180510_models.ModifyCdnServiceRequest,
    ) -> cdn_20180510_models.ModifyCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_service_with_options(request, runtime)

    async def modify_cdn_service_async(
        self,
        request: cdn_20180510_models.ModifyCdnServiceRequest,
    ) -> cdn_20180510_models.ModifyCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cdn_service_with_options_async(request, runtime)

    def modify_domain_custom_log_config_with_options(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ModifyDomainCustomLogConfigResponse().from_map(
            self.do_rpcrequest('ModifyDomainCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_domain_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ModifyDomainCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyDomainCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ModifyDomainCustomLogConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ModifyRealtimeLogDeliveryResponse().from_map(
            self.do_rpcrequest('ModifyRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_realtime_log_delivery_with_options_async(
        self,
        request: cdn_20180510_models.ModifyRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ModifyRealtimeLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('ModifyRealtimeLogDelivery', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return cdn_20180510_models.ModifyUserCustomLogConfigResponse().from_map(
            self.do_rpcrequest('ModifyUserCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_user_custom_log_config_with_options_async(
        self,
        request: cdn_20180510_models.ModifyUserCustomLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.ModifyUserCustomLogConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return cdn_20180510_models.ModifyUserCustomLogConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyUserCustomLogConfig', '2018-05-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.OpenCdnServiceResponse().from_map(
            self.do_rpcrequest('OpenCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_cdn_service_with_options_async(
        self,
        request: cdn_20180510_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.OpenCdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.OpenCdnServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenCdnService', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.PublishStagingConfigToProductionResponse().from_map(
            self.do_rpcrequest('PublishStagingConfigToProduction', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_staging_config_to_production_with_options_async(
        self,
        request: cdn_20180510_models.PublishStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PublishStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.PublishStagingConfigToProductionResponse().from_map(
            await self.do_rpcrequest_async('PublishStagingConfigToProduction', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.PushObjectCacheResponse().from_map(
            self.do_rpcrequest('PushObjectCache', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_object_cache_with_options_async(
        self,
        request: cdn_20180510_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.PushObjectCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.PushObjectCacheResponse().from_map(
            await self.do_rpcrequest_async('PushObjectCache', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.RefreshObjectCachesResponse().from_map(
            self.do_rpcrequest('RefreshObjectCaches', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_object_caches_with_options_async(
        self,
        request: cdn_20180510_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RefreshObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.RefreshObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('RefreshObjectCaches', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.RollbackStagingConfigResponse().from_map(
            self.do_rpcrequest('RollbackStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.RollbackStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.RollbackStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.RollbackStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('RollbackStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCcConfigResponse().from_map(
            self.do_rpcrequest('SetCcConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_cc_config_with_options_async(
        self,
        request: cdn_20180510_models.SetCcConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCcConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCcConfigResponse().from_map(
            await self.do_rpcrequest_async('SetCcConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCdnDomainCSRCertificateResponse().from_map(
            self.do_rpcrequest('SetCdnDomainCSRCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_cdn_domain_csrcertificate_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCdnDomainCSRCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetCdnDomainCSRCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_cdn_domain_staging_config_with_options(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCdnDomainStagingConfigResponse().from_map(
            self.do_rpcrequest('SetCdnDomainStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_cdn_domain_staging_config_with_options_async(
        self,
        request: cdn_20180510_models.SetCdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetCdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetCdnDomainStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('SetCdnDomainStagingConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetConfigOfVersionResponse().from_map(
            self.do_rpcrequest('SetConfigOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_config_of_version_with_options_async(
        self,
        request: cdn_20180510_models.SetConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetConfigOfVersionResponse().from_map(
            await self.do_rpcrequest_async('SetConfigOfVersion', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetDomainGreenManagerConfigResponse().from_map(
            self.do_rpcrequest('SetDomainGreenManagerConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_green_manager_config_with_options_async(
        self,
        request: cdn_20180510_models.SetDomainGreenManagerConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainGreenManagerConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetDomainGreenManagerConfigResponse().from_map(
            await self.do_rpcrequest_async('SetDomainGreenManagerConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetDomainServerCertificateResponse().from_map(
            self.do_rpcrequest('SetDomainServerCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_server_certificate_with_options_async(
        self,
        request: cdn_20180510_models.SetDomainServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetDomainServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetDomainServerCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetDomainServerCertificate', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetErrorPageConfigResponse().from_map(
            self.do_rpcrequest('SetErrorPageConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_error_page_config_with_options_async(
        self,
        request: cdn_20180510_models.SetErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetErrorPageConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetErrorPageConfigResponse().from_map(
            await self.do_rpcrequest_async('SetErrorPageConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetFileCacheExpiredConfigResponse().from_map(
            self.do_rpcrequest('SetFileCacheExpiredConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_file_cache_expired_config_with_options_async(
        self,
        request: cdn_20180510_models.SetFileCacheExpiredConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetFileCacheExpiredConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetFileCacheExpiredConfigResponse().from_map(
            await self.do_rpcrequest_async('SetFileCacheExpiredConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetForceRedirectConfigResponse().from_map(
            self.do_rpcrequest('SetForceRedirectConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_force_redirect_config_with_options_async(
        self,
        request: cdn_20180510_models.SetForceRedirectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForceRedirectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetForceRedirectConfigResponse().from_map(
            await self.do_rpcrequest_async('SetForceRedirectConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetForwardSchemeConfigResponse().from_map(
            self.do_rpcrequest('SetForwardSchemeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_forward_scheme_config_with_options_async(
        self,
        request: cdn_20180510_models.SetForwardSchemeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetForwardSchemeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetForwardSchemeConfigResponse().from_map(
            await self.do_rpcrequest_async('SetForwardSchemeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpErrorPageConfigResponse().from_map(
            self.do_rpcrequest('SetHttpErrorPageConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_http_error_page_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpErrorPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpErrorPageConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpErrorPageConfigResponse().from_map(
            await self.do_rpcrequest_async('SetHttpErrorPageConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpHeaderConfigResponse().from_map(
            self.do_rpcrequest('SetHttpHeaderConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_http_header_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpHeaderConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpHeaderConfigResponse().from_map(
            await self.do_rpcrequest_async('SetHttpHeaderConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpsOptionConfigResponse().from_map(
            self.do_rpcrequest('SetHttpsOptionConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_https_option_config_with_options_async(
        self,
        request: cdn_20180510_models.SetHttpsOptionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetHttpsOptionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetHttpsOptionConfigResponse().from_map(
            await self.do_rpcrequest_async('SetHttpsOptionConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIgnoreQueryStringConfigResponse().from_map(
            self.do_rpcrequest('SetIgnoreQueryStringConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_ignore_query_string_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIgnoreQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIgnoreQueryStringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIgnoreQueryStringConfigResponse().from_map(
            await self.do_rpcrequest_async('SetIgnoreQueryStringConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIpAllowListConfigResponse().from_map(
            self.do_rpcrequest('SetIpAllowListConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_ip_allow_list_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIpAllowListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpAllowListConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIpAllowListConfigResponse().from_map(
            await self.do_rpcrequest_async('SetIpAllowListConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIpBlackListConfigResponse().from_map(
            self.do_rpcrequest('SetIpBlackListConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_ip_black_list_config_with_options_async(
        self,
        request: cdn_20180510_models.SetIpBlackListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetIpBlackListConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetIpBlackListConfigResponse().from_map(
            await self.do_rpcrequest_async('SetIpBlackListConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetOptimizeConfigResponse().from_map(
            self.do_rpcrequest('SetOptimizeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_optimize_config_with_options_async(
        self,
        request: cdn_20180510_models.SetOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetOptimizeConfigResponse().from_map(
            await self.do_rpcrequest_async('SetOptimizeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetPageCompressConfigResponse().from_map(
            self.do_rpcrequest('SetPageCompressConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_page_compress_config_with_options_async(
        self,
        request: cdn_20180510_models.SetPageCompressConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetPageCompressConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetPageCompressConfigResponse().from_map(
            await self.do_rpcrequest_async('SetPageCompressConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRangeConfigResponse().from_map(
            self.do_rpcrequest('SetRangeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_range_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRangeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRangeConfigResponse().from_map(
            await self.do_rpcrequest_async('SetRangeConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRefererConfigResponse().from_map(
            self.do_rpcrequest('SetRefererConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_referer_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRefererConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRefererConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRefererConfigResponse().from_map(
            await self.do_rpcrequest_async('SetRefererConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRemoveQueryStringConfigResponse().from_map(
            self.do_rpcrequest('SetRemoveQueryStringConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_remove_query_string_config_with_options_async(
        self,
        request: cdn_20180510_models.SetRemoveQueryStringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetRemoveQueryStringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetRemoveQueryStringConfigResponse().from_map(
            await self.do_rpcrequest_async('SetRemoveQueryStringConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetReqAuthConfigResponse().from_map(
            self.do_rpcrequest('SetReqAuthConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_req_auth_config_with_options_async(
        self,
        request: cdn_20180510_models.SetReqAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqAuthConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetReqAuthConfigResponse().from_map(
            await self.do_rpcrequest_async('SetReqAuthConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetReqHeaderConfigResponse().from_map(
            self.do_rpcrequest('SetReqHeaderConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_req_header_config_with_options_async(
        self,
        request: cdn_20180510_models.SetReqHeaderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetReqHeaderConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetReqHeaderConfigResponse().from_map(
            await self.do_rpcrequest_async('SetReqHeaderConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetSourceHostConfigResponse().from_map(
            self.do_rpcrequest('SetSourceHostConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_source_host_config_with_options_async(
        self,
        request: cdn_20180510_models.SetSourceHostConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetSourceHostConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetSourceHostConfigResponse().from_map(
            await self.do_rpcrequest_async('SetSourceHostConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_waiting_room_config_with_options(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetWaitingRoomConfigResponse().from_map(
            self.do_rpcrequest('SetWaitingRoomConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_waiting_room_config_with_options_async(
        self,
        request: cdn_20180510_models.SetWaitingRoomConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.SetWaitingRoomConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.SetWaitingRoomConfigResponse().from_map(
            await self.do_rpcrequest_async('SetWaitingRoomConfig', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.StartCdnDomainResponse().from_map(
            self.do_rpcrequest('StartCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.StartCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StartCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.StartCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StartCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.StopCdnDomainResponse().from_map(
            self.do_rpcrequest('StopCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_cdn_domain_with_options_async(
        self,
        request: cdn_20180510_models.StopCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.StopCdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.StopCdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StopCdnDomain', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cdn_20180510_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cdn_20180510_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_fctrigger_with_options(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.UpdateFCTriggerResponse().from_map(
            self.do_rpcrequest('UpdateFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_fctrigger_with_options_async(
        self,
        request: cdn_20180510_models.UpdateFCTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.UpdateFCTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.UpdateFCTriggerResponse().from_map(
            await self.do_rpcrequest_async('UpdateFCTrigger', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.VerifyDomainOwnerResponse().from_map(
            self.do_rpcrequest('VerifyDomainOwner', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_domain_owner_with_options_async(
        self,
        request: cdn_20180510_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20180510_models.VerifyDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cdn_20180510_models.VerifyDomainOwnerResponse().from_map(
            await self.do_rpcrequest_async('VerifyDomainOwner', '2018-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
