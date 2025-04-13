# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_et_industry_openapi20200824 import models as et_industry_openapi_20200824_models
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
            'cn-hangzhou': 'et-industry.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('et-industry-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_mqtt_connect_with_options(
        self,
        request: et_industry_openapi_20200824_models.GetMqttConnectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.GetMqttConnectResponse:
        """
        @param request: GetMqttConnectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMqttConnectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMqttConnect',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/collaboration/pop/getmqttconnect',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetMqttConnectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetMqttConnectResponse(),
                self.execute(params, req, runtime)
            )

    async def get_mqtt_connect_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.GetMqttConnectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.GetMqttConnectResponse:
        """
        @param request: GetMqttConnectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMqttConnectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMqttConnect',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/collaboration/pop/getmqttconnect',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetMqttConnectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetMqttConnectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_mqtt_connect(
        self,
        request: et_industry_openapi_20200824_models.GetMqttConnectRequest,
    ) -> et_industry_openapi_20200824_models.GetMqttConnectResponse:
        """
        @param request: GetMqttConnectRequest
        @return: GetMqttConnectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mqtt_connect_with_options(request, headers, runtime)

    async def get_mqtt_connect_async(
        self,
        request: et_industry_openapi_20200824_models.GetMqttConnectRequest,
    ) -> et_industry_openapi_20200824_models.GetMqttConnectResponse:
        """
        @param request: GetMqttConnectRequest
        @return: GetMqttConnectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mqtt_connect_with_options_async(request, headers, runtime)

    def get_nonce_with_options(
        self,
        request: et_industry_openapi_20200824_models.GetNonceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.GetNonceResponse:
        """
        @param request: GetNonceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNonceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNonce',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/collaboration/pop/getnonce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetNonceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetNonceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_nonce_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.GetNonceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.GetNonceResponse:
        """
        @param request: GetNonceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNonceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNonce',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/collaboration/pop/getnonce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetNonceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.GetNonceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_nonce(
        self,
        request: et_industry_openapi_20200824_models.GetNonceRequest,
    ) -> et_industry_openapi_20200824_models.GetNonceResponse:
        """
        @param request: GetNonceRequest
        @return: GetNonceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_nonce_with_options(request, headers, runtime)

    async def get_nonce_async(
        self,
        request: et_industry_openapi_20200824_models.GetNonceRequest,
    ) -> et_industry_openapi_20200824_models.GetNonceResponse:
        """
        @param request: GetNonceRequest
        @return: GetNonceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_nonce_with_options_async(request, headers, runtime)

    def list_measure_point_list_by_node_code_page_with_options(
        self,
        request: et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse:
        """
        @param request: ListMeasurePointListByNodeCodePageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMeasurePointListByNodeCodePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMeasurePointListByNodeCodePage',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/node/pop/measurepointlistbynodecodepage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse(),
                self.execute(params, req, runtime)
            )

    async def list_measure_point_list_by_node_code_page_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse:
        """
        @param request: ListMeasurePointListByNodeCodePageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMeasurePointListByNodeCodePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMeasurePointListByNodeCodePage',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/node/pop/measurepointlistbynodecodepage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_measure_point_list_by_node_code_page(
        self,
        request: et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageRequest,
    ) -> et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse:
        """
        @param request: ListMeasurePointListByNodeCodePageRequest
        @return: ListMeasurePointListByNodeCodePageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_measure_point_list_by_node_code_page_with_options(request, headers, runtime)

    async def list_measure_point_list_by_node_code_page_async(
        self,
        request: et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageRequest,
    ) -> et_industry_openapi_20200824_models.ListMeasurePointListByNodeCodePageResponse:
        """
        @param request: ListMeasurePointListByNodeCodePageRequest
        @return: ListMeasurePointListByNodeCodePageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_measure_point_list_by_node_code_page_with_options_async(request, headers, runtime)

    def multi_field_batch_upload_with_options(
        self,
        request: et_industry_openapi_20200824_models.MultiFieldBatchUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse:
        """
        @summary 多值批量上报
        
        @param request: MultiFieldBatchUploadRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiFieldBatchUploadResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MultiFieldBatchUpload',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/multifieldbatchv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse(),
                self.execute(params, req, runtime)
            )

    async def multi_field_batch_upload_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.MultiFieldBatchUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse:
        """
        @summary 多值批量上报
        
        @param request: MultiFieldBatchUploadRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiFieldBatchUploadResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MultiFieldBatchUpload',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/multifieldbatchv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse(),
                await self.execute_async(params, req, runtime)
            )

    def multi_field_batch_upload(
        self,
        request: et_industry_openapi_20200824_models.MultiFieldBatchUploadRequest,
    ) -> et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse:
        """
        @summary 多值批量上报
        
        @param request: MultiFieldBatchUploadRequest
        @return: MultiFieldBatchUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.multi_field_batch_upload_with_options(request, headers, runtime)

    async def multi_field_batch_upload_async(
        self,
        request: et_industry_openapi_20200824_models.MultiFieldBatchUploadRequest,
    ) -> et_industry_openapi_20200824_models.MultiFieldBatchUploadResponse:
        """
        @summary 多值批量上报
        
        @param request: MultiFieldBatchUploadRequest
        @return: MultiFieldBatchUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.multi_field_batch_upload_with_options_async(request, headers, runtime)

    def multi_source_point_batch_upload_with_options(
        self,
        request: et_industry_openapi_20200824_models.MultiSourcePointBatchUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse:
        """
        @summary 多源点位批量上报
        
        @param request: MultiSourcePointBatchUploadRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiSourcePointBatchUploadResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MultiSourcePointBatchUpload',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/sourcepointbatchv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse(),
                self.execute(params, req, runtime)
            )

    async def multi_source_point_batch_upload_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.MultiSourcePointBatchUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse:
        """
        @summary 多源点位批量上报
        
        @param request: MultiSourcePointBatchUploadRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultiSourcePointBatchUploadResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MultiSourcePointBatchUpload',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/sourcepointbatchv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse(),
                await self.execute_async(params, req, runtime)
            )

    def multi_source_point_batch_upload(
        self,
        request: et_industry_openapi_20200824_models.MultiSourcePointBatchUploadRequest,
    ) -> et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse:
        """
        @summary 多源点位批量上报
        
        @param request: MultiSourcePointBatchUploadRequest
        @return: MultiSourcePointBatchUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.multi_source_point_batch_upload_with_options(request, headers, runtime)

    async def multi_source_point_batch_upload_async(
        self,
        request: et_industry_openapi_20200824_models.MultiSourcePointBatchUploadRequest,
    ) -> et_industry_openapi_20200824_models.MultiSourcePointBatchUploadResponse:
        """
        @summary 多源点位批量上报
        
        @param request: MultiSourcePointBatchUploadRequest
        @return: MultiSourcePointBatchUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.multi_source_point_batch_upload_with_options_async(request, headers, runtime)

    def query_field_latest_by_source_point_with_options(
        self,
        request: et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse:
        """
        @param request: QueryFieldLatestBySourcePointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFieldLatestBySourcePointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFieldLatestBySourcePoint',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldlatestbysourcepoint',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse(),
                self.execute(params, req, runtime)
            )

    async def query_field_latest_by_source_point_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse:
        """
        @param request: QueryFieldLatestBySourcePointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFieldLatestBySourcePointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFieldLatestBySourcePoint',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldlatestbysourcepoint',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_field_latest_by_source_point(
        self,
        request: et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointRequest,
    ) -> et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse:
        """
        @param request: QueryFieldLatestBySourcePointRequest
        @return: QueryFieldLatestBySourcePointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_field_latest_by_source_point_with_options(request, headers, runtime)

    async def query_field_latest_by_source_point_async(
        self,
        request: et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointRequest,
    ) -> et_industry_openapi_20200824_models.QueryFieldLatestBySourcePointResponse:
        """
        @param request: QueryFieldLatestBySourcePointRequest
        @return: QueryFieldLatestBySourcePointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_field_latest_by_source_point_with_options_async(request, headers, runtime)

    def query_industry_device_data_with_options(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse:
        """
        @param request: QueryIndustryDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldlatest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse(),
                self.execute(params, req, runtime)
            )

    async def query_industry_device_data_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse:
        """
        @param request: QueryIndustryDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldlatest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_industry_device_data(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse:
        """
        @param request: QueryIndustryDeviceDataRequest
        @return: QueryIndustryDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_industry_device_data_with_options(request, headers, runtime)

    async def query_industry_device_data_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceDataResponse:
        """
        @param request: QueryIndustryDeviceDataRequest
        @return: QueryIndustryDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_industry_device_data_with_options_async(request, headers, runtime)

    def query_industry_device_limits_data_with_options(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse:
        """
        @param request: QueryIndustryDeviceLimitsDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceLimitsDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceLimitsData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldrange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse(),
                self.execute(params, req, runtime)
            )

    async def query_industry_device_limits_data_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse:
        """
        @param request: QueryIndustryDeviceLimitsDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceLimitsDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceLimitsData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldrange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_industry_device_limits_data(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse:
        """
        @param request: QueryIndustryDeviceLimitsDataRequest
        @return: QueryIndustryDeviceLimitsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_industry_device_limits_data_with_options(request, headers, runtime)

    async def query_industry_device_limits_data_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceLimitsDataResponse:
        """
        @param request: QueryIndustryDeviceLimitsDataRequest
        @return: QueryIndustryDeviceLimitsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_industry_device_limits_data_with_options_async(request, headers, runtime)

    def query_industry_device_status_data_with_options(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse:
        """
        @param request: QueryIndustryDeviceStatusDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceStatusDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceStatusData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldrangestatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse(),
                self.execute(params, req, runtime)
            )

    async def query_industry_device_status_data_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse:
        """
        @param request: QueryIndustryDeviceStatusDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndustryDeviceStatusDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryIndustryDeviceStatusData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/query/pop/multifieldrangestatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_industry_device_status_data(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse:
        """
        @param request: QueryIndustryDeviceStatusDataRequest
        @return: QueryIndustryDeviceStatusDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_industry_device_status_data_with_options(request, headers, runtime)

    async def query_industry_device_status_data_async(
        self,
        request: et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataRequest,
    ) -> et_industry_openapi_20200824_models.QueryIndustryDeviceStatusDataResponse:
        """
        @param request: QueryIndustryDeviceStatusDataRequest
        @return: QueryIndustryDeviceStatusDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_industry_device_status_data_with_options_async(request, headers, runtime)

    def source_point_batch_with_options(
        self,
        request: et_industry_openapi_20200824_models.SourcePointBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.SourcePointBatchResponse:
        """
        @param request: SourcePointBatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SourcePointBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SourcePointBatch',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/sourcepointbatch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.SourcePointBatchResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.SourcePointBatchResponse(),
                self.execute(params, req, runtime)
            )

    async def source_point_batch_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.SourcePointBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.SourcePointBatchResponse:
        """
        @param request: SourcePointBatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SourcePointBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SourcePointBatch',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/sourcepointbatch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.SourcePointBatchResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.SourcePointBatchResponse(),
                await self.execute_async(params, req, runtime)
            )

    def source_point_batch(
        self,
        request: et_industry_openapi_20200824_models.SourcePointBatchRequest,
    ) -> et_industry_openapi_20200824_models.SourcePointBatchResponse:
        """
        @param request: SourcePointBatchRequest
        @return: SourcePointBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.source_point_batch_with_options(request, headers, runtime)

    async def source_point_batch_async(
        self,
        request: et_industry_openapi_20200824_models.SourcePointBatchRequest,
    ) -> et_industry_openapi_20200824_models.SourcePointBatchResponse:
        """
        @param request: SourcePointBatchRequest
        @return: SourcePointBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.source_point_batch_with_options_async(request, headers, runtime)

    def upload_industry_device_data_with_options(
        self,
        request: et_industry_openapi_20200824_models.UploadIndustryDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse:
        """
        @param request: UploadIndustryDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadIndustryDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadIndustryDeviceData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/multifieldbatch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse(),
                self.execute(params, req, runtime)
            )

    async def upload_industry_device_data_with_options_async(
        self,
        request: et_industry_openapi_20200824_models.UploadIndustryDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse:
        """
        @param request: UploadIndustryDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadIndustryDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request):
            body['Request'] = request.request
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadIndustryDeviceData',
            version='2020-08-24',
            protocol='HTTPS',
            pathname=f'/api/igate/timeseries/upload/pop/multifieldbatch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upload_industry_device_data(
        self,
        request: et_industry_openapi_20200824_models.UploadIndustryDeviceDataRequest,
    ) -> et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse:
        """
        @param request: UploadIndustryDeviceDataRequest
        @return: UploadIndustryDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_industry_device_data_with_options(request, headers, runtime)

    async def upload_industry_device_data_async(
        self,
        request: et_industry_openapi_20200824_models.UploadIndustryDeviceDataRequest,
    ) -> et_industry_openapi_20200824_models.UploadIndustryDeviceDataResponse:
        """
        @param request: UploadIndustryDeviceDataRequest
        @return: UploadIndustryDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_industry_device_data_with_options_async(request, headers, runtime)
