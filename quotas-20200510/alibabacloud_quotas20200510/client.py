# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quotas20200510 import models as quotas_20200510_models
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
        params = open_api_models.Params(
            action='CreateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='CreateQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='DeleteQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProductQuota',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProductQuota',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProductQuotaDimension',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaDimensionResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetProductQuotaDimension',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaDimensionResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListAlarmHistoriesResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListAlarmHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListDependentQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListDependentQuotasResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListDependentQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListDependentQuotasResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_product_dimension_groups_with_options(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDimensionGroups',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductDimensionGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_dimension_groups_with_options_async(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDimensionGroups',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductDimensionGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_dimension_groups(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_dimension_groups_with_options(request, runtime)

    async def list_product_dimension_groups_async(
        self,
        request: quotas_20200510_models.ListProductDimensionGroupsRequest,
    ) -> quotas_20200510_models.ListProductDimensionGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_dimension_groups_with_options_async(request, runtime)

    def list_product_quota_dimensions_with_options(
        self,
        request: quotas_20200510_models.ListProductQuotaDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quotas_20200510_models.ListProductQuotaDimensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProductQuotaDimensions',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotaDimensionsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProductQuotaDimensions',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotaDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProductQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotasResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProductQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotasResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProducts',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListProducts',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListQuotaAlarms',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaAlarmsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListQuotaAlarms',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListQuotaApplications',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListQuotaApplications',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.UpdateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='UpdateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.UpdateQuotaAlarmResponse(),
            await self.call_api_async(params, req, runtime)
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
