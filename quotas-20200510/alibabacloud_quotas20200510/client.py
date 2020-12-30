# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quotas20200510 import models as quotas_20200510_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('quotas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.CreateQuotaAlarmResponse().from_map(
            self.do_rpcrequest('CreateQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.CreateQuotaAlarmResponse().from_map(
            await self.do_rpcrequest_async('CreateQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quota_alarm(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quota_alarm_with_options(request, runtime)

    async def create_quota_alarm_async(
        self,
        request: quotas_20200510_models.CreateQuotaAlarmRequest,
    ) -> quotas_20200510_models.CreateQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_alarm_with_options_async(request, runtime)

    def create_quota_application_with_options(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.CreateQuotaApplicationResponse().from_map(
            self.do_rpcrequest('CreateQuotaApplication', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quota_application_with_options_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.CreateQuotaApplicationResponse().from_map(
            await self.do_rpcrequest_async('CreateQuotaApplication', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quota_application(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quota_application_with_options(request, runtime)

    async def create_quota_application_async(
        self,
        request: quotas_20200510_models.CreateQuotaApplicationRequest,
    ) -> quotas_20200510_models.CreateQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quota_application_with_options_async(request, runtime)

    def delete_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.DeleteQuotaAlarmResponse().from_map(
            self.do_rpcrequest('DeleteQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.DeleteQuotaAlarmResponse().from_map(
            await self.do_rpcrequest_async('DeleteQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quota_alarm(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quota_alarm_with_options(request, runtime)

    async def delete_quota_alarm_async(
        self,
        request: quotas_20200510_models.DeleteQuotaAlarmRequest,
    ) -> quotas_20200510_models.DeleteQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quota_alarm_with_options_async(request, runtime)

    def get_product_quota_with_options(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetProductQuotaResponse().from_map(
            self.do_rpcrequest('GetProductQuota', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_product_quota_with_options_async(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetProductQuotaResponse().from_map(
            await self.do_rpcrequest_async('GetProductQuota', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_product_quota(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_with_options(request, runtime)

    async def get_product_quota_async(
        self,
        request: quotas_20200510_models.GetProductQuotaRequest,
    ) -> quotas_20200510_models.GetProductQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_quota_with_options_async(request, runtime)

    def get_product_quota_dimension_with_options(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetProductQuotaDimensionResponse().from_map(
            self.do_rpcrequest('GetProductQuotaDimension', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_product_quota_dimension_with_options_async(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetProductQuotaDimensionResponse().from_map(
            await self.do_rpcrequest_async('GetProductQuotaDimension', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_product_quota_dimension(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_dimension_with_options(request, runtime)

    async def get_product_quota_dimension_async(
        self,
        request: quotas_20200510_models.GetProductQuotaDimensionRequest,
    ) -> quotas_20200510_models.GetProductQuotaDimensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_quota_dimension_with_options_async(request, runtime)

    def get_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetQuotaAlarmResponse().from_map(
            self.do_rpcrequest('GetQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetQuotaAlarmResponse().from_map(
            await self.do_rpcrequest_async('GetQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quota_alarm(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quota_alarm_with_options(request, runtime)

    async def get_quota_alarm_async(
        self,
        request: quotas_20200510_models.GetQuotaAlarmRequest,
    ) -> quotas_20200510_models.GetQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_alarm_with_options_async(request, runtime)

    def get_quota_application_with_options(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetQuotaApplicationResponse().from_map(
            self.do_rpcrequest('GetQuotaApplication', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quota_application_with_options_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.GetQuotaApplicationResponse().from_map(
            await self.do_rpcrequest_async('GetQuotaApplication', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quota_application(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quota_application_with_options(request, runtime)

    async def get_quota_application_async(
        self,
        request: quotas_20200510_models.GetQuotaApplicationRequest,
    ) -> quotas_20200510_models.GetQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_application_with_options_async(request, runtime)

    def list_alarm_histories_with_options(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListAlarmHistoriesResponse().from_map(
            self.do_rpcrequest('ListAlarmHistories', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_alarm_histories_with_options_async(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListAlarmHistoriesResponse().from_map(
            await self.do_rpcrequest_async('ListAlarmHistories', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_alarm_histories(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    async def list_alarm_histories_async(
        self,
        request: quotas_20200510_models.ListAlarmHistoriesRequest,
    ) -> quotas_20200510_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_histories_with_options_async(request, runtime)

    def list_dependent_quotas_with_options(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListDependentQuotasResponse().from_map(
            self.do_rpcrequest('ListDependentQuotas', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dependent_quotas_with_options_async(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListDependentQuotasResponse().from_map(
            await self.do_rpcrequest_async('ListDependentQuotas', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dependent_quotas(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dependent_quotas_with_options(request, runtime)

    async def list_dependent_quotas_async(
        self,
        request: quotas_20200510_models.ListDependentQuotasRequest,
    ) -> quotas_20200510_models.ListDependentQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dependent_quotas_with_options_async(request, runtime)

    def list_product_quota_dimensions_with_options(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductQuotaDimensionsResponse().from_map(
            self.do_rpcrequest('ListProductQuotaDimensions', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_product_quota_dimensions_with_options_async(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductQuotaDimensionsResponse().from_map(
            await self.do_rpcrequest_async('ListProductQuotaDimensions', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_product_quota_dimensions(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_quota_dimensions_with_options(request, runtime)

    async def list_product_quota_dimensions_async(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_quota_dimensions_with_options_async(request, runtime)

    def list_product_quotas_with_options(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductQuotasResponse().from_map(
            self.do_rpcrequest('ListProductQuotas', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_product_quotas_with_options_async(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductQuotasResponse().from_map(
            await self.do_rpcrequest_async('ListProductQuotas', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_product_quotas(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_quotas_with_options(request, runtime)

    async def list_product_quotas_async(
        self,
        request: quotas_20200510_models.ListProductQuotasRequest,
    ) -> quotas_20200510_models.ListProductQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_quotas_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        request: quotas_20200510_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductsResponse().from_map(
            self.do_rpcrequest('ListProducts', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: quotas_20200510_models.ListProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListProductsResponse().from_map(
            await self.do_rpcrequest_async('ListProducts', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_products(
        self,
        request: quotas_20200510_models.ListProductsRequest,
    ) -> quotas_20200510_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: quotas_20200510_models.ListProductsRequest,
    ) -> quotas_20200510_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_quota_alarms_with_options(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListQuotaAlarmsResponse().from_map(
            self.do_rpcrequest('ListQuotaAlarms', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_quota_alarms_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListQuotaAlarmsResponse().from_map(
            await self.do_rpcrequest_async('ListQuotaAlarms', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quota_alarms(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_alarms_with_options(request, runtime)

    async def list_quota_alarms_async(
        self,
        request: quotas_20200510_models.ListQuotaAlarmsRequest,
    ) -> quotas_20200510_models.ListQuotaAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_alarms_with_options_async(request, runtime)

    def list_quota_applications_with_options(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListQuotaApplicationsResponse().from_map(
            self.do_rpcrequest('ListQuotaApplications', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_quota_applications_with_options_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.ListQuotaApplicationsResponse().from_map(
            await self.do_rpcrequest_async('ListQuotaApplications', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quota_applications(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_with_options(request, runtime)

    async def list_quota_applications_async(
        self,
        request: quotas_20200510_models.ListQuotaApplicationsRequest,
    ) -> quotas_20200510_models.ListQuotaApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quota_applications_with_options_async(request, runtime)

    def update_quota_alarm_with_options(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.UpdateQuotaAlarmResponse().from_map(
            self.do_rpcrequest('UpdateQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_quota_alarm_with_options_async(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return quotas_20200510_models.UpdateQuotaAlarmResponse().from_map(
            await self.do_rpcrequest_async('UpdateQuotaAlarm', '2020-05-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_quota_alarm(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_quota_alarm_with_options(request, runtime)

    async def update_quota_alarm_async(
        self,
        request: quotas_20200510_models.UpdateQuotaAlarmRequest,
    ) -> quotas_20200510_models.UpdateQuotaAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_quota_alarm_with_options_async(request, runtime)
