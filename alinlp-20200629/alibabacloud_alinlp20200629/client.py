# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alinlp20200629 import models as alinlp_20200629_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('alinlp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_dclock_with_options(
        self,
        request: alinlp_20200629_models.ADClockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADClockResponse:
        """
        @summary ad画钟算法处理算法
        
        @param request: ADClockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADClockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADClock',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADClockResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_dclock_with_options_async(
        self,
        request: alinlp_20200629_models.ADClockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADClockResponse:
        """
        @summary ad画钟算法处理算法
        
        @param request: ADClockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADClockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADClock',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADClockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_dclock(
        self,
        request: alinlp_20200629_models.ADClockRequest,
    ) -> alinlp_20200629_models.ADClockResponse:
        """
        @summary ad画钟算法处理算法
        
        @param request: ADClockRequest
        @return: ADClockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.a_dclock_with_options(request, runtime)

    async def a_dclock_async(
        self,
        request: alinlp_20200629_models.ADClockRequest,
    ) -> alinlp_20200629_models.ADClockResponse:
        """
        @summary ad画钟算法处理算法
        
        @param request: ADClockRequest
        @return: ADClockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.a_dclock_with_options_async(request, runtime)

    def a_dmmuwith_options(
        self,
        request: alinlp_20200629_models.ADMMURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMMUResponse:
        """
        @summary ad语音处理算法
        
        @param request: ADMMURequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMMUResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMMU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMMUResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_dmmuwith_options_async(
        self,
        request: alinlp_20200629_models.ADMMURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMMUResponse:
        """
        @summary ad语音处理算法
        
        @param request: ADMMURequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMMUResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMMU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMMUResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_dmmu(
        self,
        request: alinlp_20200629_models.ADMMURequest,
    ) -> alinlp_20200629_models.ADMMUResponse:
        """
        @summary ad语音处理算法
        
        @param request: ADMMURequest
        @return: ADMMUResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.a_dmmuwith_options(request, runtime)

    async def a_dmmu_async(
        self,
        request: alinlp_20200629_models.ADMMURequest,
    ) -> alinlp_20200629_models.ADMMUResponse:
        """
        @summary ad语音处理算法
        
        @param request: ADMMURequest
        @return: ADMMUResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.a_dmmuwith_options_async(request, runtime)

    def a_dmini_cog_with_options(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
        """
        @summary AD筛查能力，处理用户传入的答题音频和画钟图片从而计算风险结果
        
        @param request: ADMiniCogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMiniCogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCog',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_dmini_cog_with_options_async(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
        """
        @summary AD筛查能力，处理用户传入的答题音频和画钟图片从而计算风险结果
        
        @param request: ADMiniCogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMiniCogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCog',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_dmini_cog(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
        """
        @summary AD筛查能力，处理用户传入的答题音频和画钟图片从而计算风险结果
        
        @param request: ADMiniCogRequest
        @return: ADMiniCogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_with_options(request, runtime)

    async def a_dmini_cog_async(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
        """
        @summary AD筛查能力，处理用户传入的答题音频和画钟图片从而计算风险结果
        
        @param request: ADMiniCogRequest
        @return: ADMiniCogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.a_dmini_cog_with_options_async(request, runtime)

    def a_dmini_cog_result_with_options(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
        """
        @summary AD筛查能力,提供给用户查询筛查结果，筛查结果来源自接口ADMIniCog
        
        @param request: ADMiniCogResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMiniCogResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCogResult',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_dmini_cog_result_with_options_async(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
        """
        @summary AD筛查能力,提供给用户查询筛查结果，筛查结果来源自接口ADMIniCog
        
        @param request: ADMiniCogResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ADMiniCogResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCogResult',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_dmini_cog_result(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
        """
        @summary AD筛查能力,提供给用户查询筛查结果，筛查结果来源自接口ADMIniCog
        
        @param request: ADMiniCogResultRequest
        @return: ADMiniCogResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_result_with_options(request, runtime)

    async def a_dmini_cog_result_async(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
        """
        @summary AD筛查能力,提供给用户查询筛查结果，筛查结果来源自接口ADMIniCog
        
        @param request: ADMiniCogResultRequest
        @return: ADMiniCogResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.a_dmini_cog_result_with_options_async(request, runtime)

    def delete_service_data_by_conditions_with_options(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
        """
        @summary 根据条件删除服务数据
        
        @param tmp_req: DeleteServiceDataByConditionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceDataByConditionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByConditionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByConditions',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_data_by_conditions_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
        """
        @summary 根据条件删除服务数据
        
        @param tmp_req: DeleteServiceDataByConditionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceDataByConditionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByConditionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByConditions',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByConditionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_data_by_conditions(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
        """
        @summary 根据条件删除服务数据
        
        @param request: DeleteServiceDataByConditionsRequest
        @return: DeleteServiceDataByConditionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_conditions_with_options(request, runtime)

    async def delete_service_data_by_conditions_async(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
        """
        @summary 根据条件删除服务数据
        
        @param request: DeleteServiceDataByConditionsRequest
        @return: DeleteServiceDataByConditionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_data_by_conditions_with_options_async(request, runtime)

    def delete_service_data_by_ids_with_options(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
        """
        @summary 根据ids删除服务数据
        
        @param tmp_req: DeleteServiceDataByIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceDataByIdsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByIds',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_data_by_ids_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
        """
        @summary 根据ids删除服务数据
        
        @param tmp_req: DeleteServiceDataByIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceDataByIdsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByIds',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_data_by_ids(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
        """
        @summary 根据ids删除服务数据
        
        @param request: DeleteServiceDataByIdsRequest
        @return: DeleteServiceDataByIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_ids_with_options(request, runtime)

    async def delete_service_data_by_ids_async(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
        """
        @summary 根据ids删除服务数据
        
        @param request: DeleteServiceDataByIdsRequest
        @return: DeleteServiceDataByIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_data_by_ids_with_options_async(request, runtime)

    def get_brand_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
        """
        @summary 品牌预测
        
        @param request: GetBrandChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrandChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBrandChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetBrandChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_brand_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
        """
        @summary 品牌预测
        
        @param request: GetBrandChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrandChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBrandChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetBrandChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_brand_ch_ecom(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
        """
        @summary 品牌预测
        
        @param request: GetBrandChEcomRequest
        @return: GetBrandChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_brand_ch_ecom_with_options(request, runtime)

    async def get_brand_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
        """
        @summary 品牌预测
        
        @param request: GetBrandChEcomRequest
        @return: GetBrandChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_brand_ch_ecom_with_options_async(request, runtime)

    def get_cate_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
        """
        @summary 类目预测
        
        @param request: GetCateChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCateChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCateChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCateChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cate_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
        """
        @summary 类目预测
        
        @param request: GetCateChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCateChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCateChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCateChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cate_ch_ecom(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
        """
        @summary 类目预测
        
        @param request: GetCateChEcomRequest
        @return: GetCateChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cate_ch_ecom_with_options(request, runtime)

    async def get_cate_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
        """
        @summary 类目预测
        
        @param request: GetCateChEcomRequest
        @return: GetCateChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cate_ch_ecom_with_options_async(request, runtime)

    def get_check_duplication_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        """
        @param request: GetCheckDuplicationChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCheckDuplicationChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCheckDuplicationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCheckDuplicationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_check_duplication_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        """
        @param request: GetCheckDuplicationChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCheckDuplicationChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCheckDuplicationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCheckDuplicationChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_check_duplication_ch_medical(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        """
        @param request: GetCheckDuplicationChMedicalRequest
        @return: GetCheckDuplicationChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_check_duplication_ch_medical_with_options(request, runtime)

    async def get_check_duplication_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        """
        @param request: GetCheckDuplicationChMedicalRequest
        @return: GetCheckDuplicationChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_check_duplication_ch_medical_with_options_async(request, runtime)

    def get_diagnosis_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        """
        @param request: GetDiagnosisChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDiagnosisChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDiagnosisChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        """
        @param request: GetDiagnosisChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDiagnosisChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDiagnosisChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_ch_medical(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        """
        @param request: GetDiagnosisChMedicalRequest
        @return: GetDiagnosisChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_ch_medical_with_options(request, runtime)

    async def get_diagnosis_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        """
        @param request: GetDiagnosisChMedicalRequest
        @return: GetDiagnosisChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnosis_ch_medical_with_options_async(request, runtime)

    def get_dp_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        """
        @param request: GetDpChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        """
        @param request: GetDpChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_ecom(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        """
        @param request: GetDpChEcomRequest
        @return: GetDpChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_ecom_with_options(request, runtime)

    async def get_dp_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        """
        @param request: GetDpChEcomRequest
        @return: GetDpChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_ecom_with_options_async(request, runtime)

    def get_dp_ch_general_ctbwith_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        """
        @param request: GetDpChGeneralCTBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChGeneralCTBResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralCTB',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralCTBResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_general_ctbwith_options_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        """
        @param request: GetDpChGeneralCTBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChGeneralCTBResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralCTB',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralCTBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_general_ctb(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        """
        @param request: GetDpChGeneralCTBRequest
        @return: GetDpChGeneralCTBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_ctbwith_options(request, runtime)

    async def get_dp_ch_general_ctb_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        """
        @param request: GetDpChGeneralCTBRequest
        @return: GetDpChGeneralCTBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_ctbwith_options_async(request, runtime)

    def get_dp_ch_general_stanford_with_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        """
        @param request: GetDpChGeneralStanfordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChGeneralStanfordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralStanford',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralStanfordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dp_ch_general_stanford_with_options_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        """
        @param request: GetDpChGeneralStanfordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDpChGeneralStanfordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralStanford',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralStanfordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dp_ch_general_stanford(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        """
        @param request: GetDpChGeneralStanfordRequest
        @return: GetDpChGeneralStanfordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_stanford_with_options(request, runtime)

    async def get_dp_ch_general_stanford_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        """
        @param request: GetDpChGeneralStanfordRequest
        @return: GetDpChGeneralStanfordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_stanford_with_options_async(request, runtime)

    def get_ec_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        """
        @param request: GetEcChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEcChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ec_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        """
        @param request: GetEcChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEcChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ec_ch_general(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        """
        @param request: GetEcChGeneralRequest
        @return: GetEcChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ec_ch_general_with_options(request, runtime)

    async def get_ec_ch_general_async(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        """
        @param request: GetEcChGeneralRequest
        @return: GetEcChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_ch_general_with_options_async(request, runtime)

    def get_ec_en_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        """
        @param request: GetEcEnGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEcEnGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcEnGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcEnGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ec_en_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        """
        @param request: GetEcEnGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEcEnGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcEnGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcEnGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ec_en_general(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        """
        @param request: GetEcEnGeneralRequest
        @return: GetEcEnGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ec_en_general_with_options(request, runtime)

    async def get_ec_en_general_async(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        """
        @param request: GetEcEnGeneralRequest
        @return: GetEcEnGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_en_general_with_options_async(request, runtime)

    def get_embedding_with_options(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
        """
        @summary embedding
        
        @param request: GetEmbeddingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.text_type):
            body['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmbedding',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEmbeddingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_embedding_with_options_async(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
        """
        @summary embedding
        
        @param request: GetEmbeddingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmbeddingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.text_type):
            body['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmbedding',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEmbeddingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_embedding(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
        """
        @summary embedding
        
        @param request: GetEmbeddingRequest
        @return: GetEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_embedding_with_options(request, runtime)

    async def get_embedding_async(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
        """
        @summary embedding
        
        @param request: GetEmbeddingRequest
        @return: GetEmbeddingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_embedding_with_options_async(request, runtime)

    def get_item_pub_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
        """
        @summary 微购整合接口
        
        @param request: GetItemPubChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetItemPubChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetItemPubChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetItemPubChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_item_pub_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
        """
        @summary 微购整合接口
        
        @param request: GetItemPubChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetItemPubChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetItemPubChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetItemPubChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_item_pub_ch_ecom(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
        """
        @summary 微购整合接口
        
        @param request: GetItemPubChEcomRequest
        @return: GetItemPubChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_item_pub_ch_ecom_with_options(request, runtime)

    async def get_item_pub_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
        """
        @summary 微购整合接口
        
        @param request: GetItemPubChEcomRequest
        @return: GetItemPubChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_item_pub_ch_ecom_with_options_async(request, runtime)

    def get_keyword_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        """
        @param request: GetKeywordChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_version):
            body['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        """
        @param request: GetKeywordChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_version):
            body['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_ch_ecom(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        """
        @param request: GetKeywordChEcomRequest
        @return: GetKeywordChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_ch_ecom_with_options(request, runtime)

    async def get_keyword_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        """
        @param request: GetKeywordChEcomRequest
        @return: GetKeywordChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_ch_ecom_with_options_async(request, runtime)

    def get_keyword_en_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        """
        @param request: GetKeywordEnEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordEnEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordEnEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordEnEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_en_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        """
        @param request: GetKeywordEnEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordEnEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordEnEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordEnEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_en_ecom(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        """
        @param request: GetKeywordEnEcomRequest
        @return: GetKeywordEnEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_en_ecom_with_options(request, runtime)

    async def get_keyword_en_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        """
        @param request: GetKeywordEnEcomRequest
        @return: GetKeywordEnEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_en_ecom_with_options_async(request, runtime)

    def get_medicine_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        """
        @param request: GetMedicineChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMedicineChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory):
            body['Factory'] = request.factory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.specification):
            body['Specification'] = request.specification
        if not UtilClient.is_unset(request.unit):
            body['Unit'] = request.unit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMedicineChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetMedicineChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_medicine_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        """
        @param request: GetMedicineChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMedicineChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory):
            body['Factory'] = request.factory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.specification):
            body['Specification'] = request.specification
        if not UtilClient.is_unset(request.unit):
            body['Unit'] = request.unit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMedicineChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetMedicineChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_medicine_ch_medical(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        """
        @param request: GetMedicineChMedicalRequest
        @return: GetMedicineChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_medicine_ch_medical_with_options(request, runtime)

    async def get_medicine_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        """
        @param request: GetMedicineChMedicalRequest
        @return: GetMedicineChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_medicine_ch_medical_with_options_async(request, runtime)

    def get_ner_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        """
        @param request: GetNerChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        """
        @param request: GetNerChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_ch_ecom(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        """
        @param request: GetNerChEcomRequest
        @return: GetNerChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_ecom_with_options(request, runtime)

    async def get_ner_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        """
        @param request: GetNerChEcomRequest
        @return: GetNerChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_ecom_with_options_async(request, runtime)

    def get_ner_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        """
        @param request: GetNerChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        """
        @param request: GetNerChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_ch_medical(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        """
        @param request: GetNerChMedicalRequest
        @return: GetNerChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_medical_with_options(request, runtime)

    async def get_ner_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        """
        @param request: GetNerChMedicalRequest
        @return: GetNerChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_medical_with_options_async(request, runtime)

    def get_ner_customized_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        """
        @param request: GetNerCustomizedChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerCustomizedChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_customized_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        """
        @param request: GetNerCustomizedChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerCustomizedChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_customized_ch_ecom(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        """
        @param request: GetNerCustomizedChEcomRequest
        @return: GetNerCustomizedChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_ch_ecom_with_options(request, runtime)

    async def get_ner_customized_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        """
        @param request: GetNerCustomizedChEcomRequest
        @return: GetNerCustomizedChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_ch_ecom_with_options_async(request, runtime)

    def get_ner_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        """
        @param request: GetNerCustomizedSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerCustomizedSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ner_customized_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        """
        @param request: GetNerCustomizedSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNerCustomizedSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ner_customized_sea_ecom(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        """
        @param request: GetNerCustomizedSeaEcomRequest
        @return: GetNerCustomizedSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_sea_ecom_with_options(request, runtime)

    async def get_ner_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        """
        @param request: GetNerCustomizedSeaEcomRequest
        @return: GetNerCustomizedSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_sea_ecom_with_options_async(request, runtime)

    def get_open_nluwith_options(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
        """
        @summary openNLU
        
        @param request: GetOpenNLURequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenNLUResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_nluwith_options_async(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
        """
        @summary openNLU
        
        @param request: GetOpenNLURequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenNLUResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_nlu(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
        """
        @summary openNLU
        
        @param request: GetOpenNLURequest
        @return: GetOpenNLUResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluwith_options(request, runtime)

    async def get_open_nlu_async(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
        """
        @summary openNLU
        
        @param request: GetOpenNLURequest
        @return: GetOpenNLUResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_open_nluwith_options_async(request, runtime)

    def get_open_nluhigh_recall_with_options(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
        """
        @summary openNLU高召回版
        
        @param request: GetOpenNLUHighRecallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenNLUHighRecallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLUHighRecall',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUHighRecallResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_nluhigh_recall_with_options_async(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
        """
        @summary openNLU高召回版
        
        @param request: GetOpenNLUHighRecallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOpenNLUHighRecallResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLUHighRecall',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUHighRecallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_nluhigh_recall(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
        """
        @summary openNLU高召回版
        
        @param request: GetOpenNLUHighRecallRequest
        @return: GetOpenNLUHighRecallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluhigh_recall_with_options(request, runtime)

    async def get_open_nluhigh_recall_async(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
        """
        @summary openNLU高召回版
        
        @param request: GetOpenNLUHighRecallRequest
        @return: GetOpenNLUHighRecallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_open_nluhigh_recall_with_options_async(request, runtime)

    def get_operation_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        """
        @param request: GetOperationChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOperationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOperationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        """
        @param request: GetOperationChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOperationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOperationChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_ch_medical(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        """
        @param request: GetOperationChMedicalRequest
        @return: GetOperationChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_operation_ch_medical_with_options(request, runtime)

    async def get_operation_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        """
        @param request: GetOperationChMedicalRequest
        @return: GetOperationChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_ch_medical_with_options_async(request, runtime)

    def get_pos_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        """
        @param request: GetPosChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPosChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pos_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        """
        @param request: GetPosChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPosChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pos_ch_ecom(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        """
        @param request: GetPosChEcomRequest
        @return: GetPosChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_ecom_with_options(request, runtime)

    async def get_pos_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        """
        @param request: GetPosChEcomRequest
        @return: GetPosChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_ecom_with_options_async(request, runtime)

    def get_pos_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        """
        @param request: GetPosChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPosChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pos_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        """
        @param request: GetPosChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPosChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pos_ch_general(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        """
        @param request: GetPosChGeneralRequest
        @return: GetPosChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_general_with_options(request, runtime)

    async def get_pos_ch_general_async(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        """
        @param request: GetPosChGeneralRequest
        @return: GetPosChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_general_with_options_async(request, runtime)

    def get_price_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
        """
        @param request: GetPriceChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPriceChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPriceChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPriceChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_price_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
        """
        @param request: GetPriceChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPriceChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPriceChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPriceChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_price_ch_ecom(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
        """
        @param request: GetPriceChEcomRequest
        @return: GetPriceChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_price_ch_ecom_with_options(request, runtime)

    async def get_price_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
        """
        @param request: GetPriceChEcomRequest
        @return: GetPriceChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_price_ch_ecom_with_options_async(request, runtime)

    def get_ssetest_with_options(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSSETestResponse:
        """
        @summary 测试sse
        
        @param request: GetSSETestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSSETestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSSETest',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSSETestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ssetest_with_options_async(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSSETestResponse:
        """
        @summary 测试sse
        
        @param request: GetSSETestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSSETestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSSETest',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSSETestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ssetest(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
    ) -> alinlp_20200629_models.GetSSETestResponse:
        """
        @summary 测试sse
        
        @param request: GetSSETestRequest
        @return: GetSSETestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ssetest_with_options(request, runtime)

    async def get_ssetest_async(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
    ) -> alinlp_20200629_models.GetSSETestResponse:
        """
        @summary 测试sse
        
        @param request: GetSSETestRequest
        @return: GetSSETestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ssetest_with_options_async(request, runtime)

    def get_sa_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        """
        @param request: GetSaChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSaChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sa_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        """
        @param request: GetSaChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSaChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sa_ch_general(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        """
        @param request: GetSaChGeneralRequest
        @return: GetSaChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sa_ch_general_with_options(request, runtime)

    async def get_sa_ch_general_async(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        """
        @param request: GetSaChGeneralRequest
        @return: GetSaChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_ch_general_with_options_async(request, runtime)

    def get_sa_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        """
        @param request: GetSaSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSaSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sa_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        """
        @param request: GetSaSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSaSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sa_sea_ecom(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        """
        @param request: GetSaSeaEcomRequest
        @return: GetSaSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sa_sea_ecom_with_options(request, runtime)

    async def get_sa_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        """
        @param request: GetSaSeaEcomRequest
        @return: GetSaSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_sea_ecom_with_options_async(request, runtime)

    def get_service_data_import_status_with_options(
        self,
        tmp_req: alinlp_20200629_models.GetServiceDataImportStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
        """
        @summary 获取服务数据导入状态
        
        @param tmp_req: GetServiceDataImportStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDataImportStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.GetServiceDataImportStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_import_ids):
            request.data_import_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_import_ids, 'DataImportIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_import_ids_shrink):
            body['DataImportIds'] = request.data_import_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceDataImportStatus',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetServiceDataImportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_data_import_status_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.GetServiceDataImportStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
        """
        @summary 获取服务数据导入状态
        
        @param tmp_req: GetServiceDataImportStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDataImportStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.GetServiceDataImportStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_import_ids):
            request.data_import_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_import_ids, 'DataImportIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_import_ids_shrink):
            body['DataImportIds'] = request.data_import_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceDataImportStatus',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetServiceDataImportStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_data_import_status(
        self,
        request: alinlp_20200629_models.GetServiceDataImportStatusRequest,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
        """
        @summary 获取服务数据导入状态
        
        @param request: GetServiceDataImportStatusRequest
        @return: GetServiceDataImportStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_data_import_status_with_options(request, runtime)

    async def get_service_data_import_status_async(
        self,
        request: alinlp_20200629_models.GetServiceDataImportStatusRequest,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
        """
        @summary 获取服务数据导入状态
        
        @param request: GetServiceDataImportStatusRequest
        @return: GetServiceDataImportStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_data_import_status_with_options_async(request, runtime)

    def get_similarity_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        """
        @param request: GetSimilarityChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarityChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSimilarityChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_similarity_ch_medical_with_options_async(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        """
        @param request: GetSimilarityChMedicalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityChMedicalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarityChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSimilarityChMedicalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_similarity_ch_medical(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        """
        @param request: GetSimilarityChMedicalRequest
        @return: GetSimilarityChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_similarity_ch_medical_with_options(request, runtime)

    async def get_similarity_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        """
        @param request: GetSimilarityChMedicalRequest
        @return: GetSimilarityChMedicalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_similarity_ch_medical_with_options_async(request, runtime)

    def get_summary_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        """
        @param request: GetSummaryChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSummaryChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSummaryChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        """
        @param request: GetSummaryChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSummaryChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSummaryChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSummaryChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_ch_ecom(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        """
        @param request: GetSummaryChEcomRequest
        @return: GetSummaryChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_summary_ch_ecom_with_options(request, runtime)

    async def get_summary_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        """
        @param request: GetSummaryChEcomRequest
        @return: GetSummaryChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_summary_ch_ecom_with_options_async(request, runtime)

    def get_table_qaservice_info_by_id_with_options(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
        """
        @summary 根据id查询tableqa服务基本信息
        
        @param request: GetTableQAServiceInfoByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableQAServiceInfoByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTableQAServiceInfoById',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTableQAServiceInfoByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_qaservice_info_by_id_with_options_async(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
        """
        @summary 根据id查询tableqa服务基本信息
        
        @param request: GetTableQAServiceInfoByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableQAServiceInfoByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTableQAServiceInfoById',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTableQAServiceInfoByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_qaservice_info_by_id(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
        """
        @summary 根据id查询tableqa服务基本信息
        
        @param request: GetTableQAServiceInfoByIdRequest
        @return: GetTableQAServiceInfoByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_table_qaservice_info_by_id_with_options(request, runtime)

    async def get_table_qaservice_info_by_id_async(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
        """
        @summary 根据id查询tableqa服务基本信息
        
        @param request: GetTableQAServiceInfoByIdRequest
        @return: GetTableQAServiceInfoByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_table_qaservice_info_by_id_with_options_async(request, runtime)

    def get_tc_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        """
        @param request: GetTcChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTcChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tc_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        """
        @param request: GetTcChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTcChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tc_ch_ecom(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        """
        @param request: GetTcChEcomRequest
        @return: GetTcChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_ecom_with_options(request, runtime)

    async def get_tc_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        """
        @param request: GetTcChEcomRequest
        @return: GetTcChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_ecom_with_options_async(request, runtime)

    def get_tc_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        """
        @param request: GetTcChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTcChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tc_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        """
        @param request: GetTcChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTcChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tc_ch_general(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        """
        @param request: GetTcChGeneralRequest
        @return: GetTcChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_general_with_options(request, runtime)

    async def get_tc_ch_general_async(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        """
        @param request: GetTcChGeneralRequest
        @return: GetTcChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_general_with_options_async(request, runtime)

    def get_ts_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        """
        @param request: GetTsChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTsChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTsChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTsChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ts_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        """
        @param request: GetTsChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTsChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTsChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTsChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ts_ch_ecom(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        """
        @param request: GetTsChEcomRequest
        @return: GetTsChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ts_ch_ecom_with_options(request, runtime)

    async def get_ts_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        """
        @param request: GetTsChEcomRequest
        @return: GetTsChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ts_ch_ecom_with_options_async(request, runtime)

    def get_user_upload_sign_with_options(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
        """
        @param request: GetUserUploadSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserUploadSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserUploadSign',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetUserUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_upload_sign_with_options_async(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
        """
        @param request: GetUserUploadSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserUploadSignResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserUploadSign',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetUserUploadSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_upload_sign(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
        """
        @param request: GetUserUploadSignRequest
        @return: GetUserUploadSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_upload_sign_with_options(request, runtime)

    async def get_user_upload_sign_async(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
        """
        @param request: GetUserUploadSignRequest
        @return: GetUserUploadSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_upload_sign_with_options_async(request, runtime)

    def get_we_ch_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        """
        @param request: GetWeChCommentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChCommentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_comment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        """
        @param request: GetWeChCommentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChCommentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_comment(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        """
        @param request: GetWeChCommentRequest
        @return: GetWeChCommentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_comment_with_options(request, runtime)

    async def get_we_ch_comment_async(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        """
        @param request: GetWeChCommentRequest
        @return: GetWeChCommentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_comment_with_options_async(request, runtime)

    def get_we_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        """
        @param request: GetWeChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        """
        @param request: GetWeChEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_ecom(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        """
        @param request: GetWeChEcomRequest
        @return: GetWeChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_ecom_with_options(request, runtime)

    async def get_we_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        """
        @param request: GetWeChEcomRequest
        @return: GetWeChEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_ecom_with_options_async(request, runtime)

    def get_we_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        """
        @param request: GetWeChEntertainmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChEntertainmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_entertainment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        """
        @param request: GetWeChEntertainmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChEntertainmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEntertainmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_entertainment(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        """
        @param request: GetWeChEntertainmentRequest
        @return: GetWeChEntertainmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_entertainment_with_options(request, runtime)

    async def get_we_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        """
        @param request: GetWeChEntertainmentRequest
        @return: GetWeChEntertainmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_entertainment_with_options_async(request, runtime)

    def get_we_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        """
        @param request: GetWeChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        """
        @param request: GetWeChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_general(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        """
        @param request: GetWeChGeneralRequest
        @return: GetWeChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_general_with_options(request, runtime)

    async def get_we_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        """
        @param request: GetWeChGeneralRequest
        @return: GetWeChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_general_with_options_async(request, runtime)

    def get_we_ch_search_with_options(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        """
        @param request: GetWeChSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChSearch',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_we_ch_search_with_options_async(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        """
        @param request: GetWeChSearchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWeChSearchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChSearch',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_we_ch_search(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        """
        @param request: GetWeChSearchRequest
        @return: GetWeChSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_search_with_options(request, runtime)

    async def get_we_ch_search_async(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        """
        @param request: GetWeChSearchRequest
        @return: GetWeChSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_search_with_options_async(request, runtime)

    def get_ws_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        """
        @param request: GetWsChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        """
        @param request: GetWsChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_ch_general(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        """
        @param request: GetWsChGeneralRequest
        @return: GetWsChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_ch_general_with_options(request, runtime)

    async def get_ws_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        """
        @param request: GetWsChGeneralRequest
        @return: GetWsChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        """
        @param request: GetWsCustomizedChEcomCommentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomCommentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_comment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        """
        @param request: GetWsCustomizedChEcomCommentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomCommentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_comment(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        """
        @param request: GetWsCustomizedChEcomCommentRequest
        @return: GetWsCustomizedChEcomCommentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_comment_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_comment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        """
        @param request: GetWsCustomizedChEcomCommentRequest
        @return: GetWsCustomizedChEcomCommentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_comment_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_content_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        """
        @param request: GetWsCustomizedChEcomContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomContent',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_content_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        """
        @param request: GetWsCustomizedChEcomContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomContent',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_content(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        """
        @param request: GetWsCustomizedChEcomContentRequest
        @return: GetWsCustomizedChEcomContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_content_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_content_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        """
        @param request: GetWsCustomizedChEcomContentRequest
        @return: GetWsCustomizedChEcomContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_content_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_title_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        """
        @param request: GetWsCustomizedChEcomTitleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomTitleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomTitle',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_ecom_title_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        """
        @param request: GetWsCustomizedChEcomTitleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEcomTitleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomTitle',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_title(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        """
        @param request: GetWsCustomizedChEcomTitleRequest
        @return: GetWsCustomizedChEcomTitleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_title_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_title_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        """
        @param request: GetWsCustomizedChEcomTitleRequest
        @return: GetWsCustomizedChEcomTitleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_title_with_options_async(request, runtime)

    def get_ws_customized_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        """
        @param request: GetWsCustomizedChEntertainmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEntertainmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_entertainment_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        """
        @param request: GetWsCustomizedChEntertainmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChEntertainmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_entertainment(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        """
        @param request: GetWsCustomizedChEntertainmentRequest
        @return: GetWsCustomizedChEntertainmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_entertainment_with_options(request, runtime)

    async def get_ws_customized_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        """
        @param request: GetWsCustomizedChEntertainmentRequest
        @return: GetWsCustomizedChEntertainmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_entertainment_with_options_async(request, runtime)

    def get_ws_customized_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        """
        @summary a
        
        @param request: GetWsCustomizedChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        """
        @summary a
        
        @param request: GetWsCustomizedChGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_general(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        """
        @summary a
        
        @param request: GetWsCustomizedChGeneralRequest
        @return: GetWsCustomizedChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_general_with_options(request, runtime)

    async def get_ws_customized_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        """
        @summary a
        
        @param request: GetWsCustomizedChGeneralRequest
        @return: GetWsCustomizedChGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_o2owith_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        """
        @param request: GetWsCustomizedChO2ORequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChO2OResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChO2O',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChO2OResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_ch_o2owith_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        """
        @param request: GetWsCustomizedChO2ORequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedChO2OResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChO2O',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChO2OResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_ch_o2o(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        """
        @param request: GetWsCustomizedChO2ORequest
        @return: GetWsCustomizedChO2OResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_o2owith_options(request, runtime)

    async def get_ws_customized_ch_o2o_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        """
        @param request: GetWsCustomizedChO2ORequest
        @return: GetWsCustomizedChO2OResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_o2owith_options_async(request, runtime)

    def get_ws_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        """
        @param request: GetWsCustomizedSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_sea_ecom_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        """
        @param request: GetWsCustomizedSeaEcomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedSeaEcomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaEcomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_sea_ecom(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        """
        @param request: GetWsCustomizedSeaEcomRequest
        @return: GetWsCustomizedSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_ecom_with_options(request, runtime)

    async def get_ws_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        """
        @param request: GetWsCustomizedSeaEcomRequest
        @return: GetWsCustomizedSeaEcomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_ecom_with_options_async(request, runtime)

    def get_ws_customized_sea_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        """
        @param request: GetWsCustomizedSeaGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedSeaGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ws_customized_sea_general_with_options_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        """
        @param request: GetWsCustomizedSeaGeneralRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWsCustomizedSeaGeneralResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ws_customized_sea_general(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        """
        @param request: GetWsCustomizedSeaGeneralRequest
        @return: GetWsCustomizedSeaGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_general_with_options(request, runtime)

    async def get_ws_customized_sea_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        """
        @param request: GetWsCustomizedSeaGeneralRequest
        @return: GetWsCustomizedSeaGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_general_with_options_async(request, runtime)

    def import_service_data_with_options(
        self,
        tmp_req: alinlp_20200629_models.ImportServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
        """
        @summary 导入服务数据
        
        @param tmp_req: ImportServiceDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportServiceDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition):
            request.partition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition, 'Partition', 'json')
        body = {}
        if not UtilClient.is_unset(request.partition_shrink):
            body['Partition'] = request.partition_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sub_path):
            body['SubPath'] = request.sub_path
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_service_data_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.ImportServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
        """
        @summary 导入服务数据
        
        @param tmp_req: ImportServiceDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportServiceDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition):
            request.partition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition, 'Partition', 'json')
        body = {}
        if not UtilClient.is_unset(request.partition_shrink):
            body['Partition'] = request.partition_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sub_path):
            body['SubPath'] = request.sub_path
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_service_data(
        self,
        request: alinlp_20200629_models.ImportServiceDataRequest,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
        """
        @summary 导入服务数据
        
        @param request: ImportServiceDataRequest
        @return: ImportServiceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_service_data_with_options(request, runtime)

    async def import_service_data_async(
        self,
        request: alinlp_20200629_models.ImportServiceDataRequest,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
        """
        @summary 导入服务数据
        
        @param request: ImportServiceDataRequest
        @return: ImportServiceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_service_data_with_options_async(request, runtime)

    def import_service_data_v2with_options(
        self,
        tmp_req: alinlp_20200629_models.ImportServiceDataV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ImportServiceDataV2Response:
        """
        @summary 导入服务数据V2
        
        @param tmp_req: ImportServiceDataV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportServiceDataV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceDataV2',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataV2Response(),
            self.call_api(params, req, runtime)
        )

    async def import_service_data_v2with_options_async(
        self,
        tmp_req: alinlp_20200629_models.ImportServiceDataV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ImportServiceDataV2Response:
        """
        @summary 导入服务数据V2
        
        @param tmp_req: ImportServiceDataV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportServiceDataV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceDataV2',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def import_service_data_v2(
        self,
        request: alinlp_20200629_models.ImportServiceDataV2Request,
    ) -> alinlp_20200629_models.ImportServiceDataV2Response:
        """
        @summary 导入服务数据V2
        
        @param request: ImportServiceDataV2Request
        @return: ImportServiceDataV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.import_service_data_v2with_options(request, runtime)

    async def import_service_data_v2_async(
        self,
        request: alinlp_20200629_models.ImportServiceDataV2Request,
    ) -> alinlp_20200629_models.ImportServiceDataV2Response:
        """
        @summary 导入服务数据V2
        
        @param request: ImportServiceDataV2Request
        @return: ImportServiceDataV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_service_data_v2with_options_async(request, runtime)

    def insert_custom_with_options(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.InsertCustomResponse:
        """
        @param request: InsertCustomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertCustomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_file_name):
            body['CustomFileName'] = request.custom_file_name
        if not UtilClient.is_unset(request.custom_url):
            body['CustomUrl'] = request.custom_url
        if not UtilClient.is_unset(request.reg_file_name):
            body['RegFileName'] = request.reg_file_name
        if not UtilClient.is_unset(request.reg_url):
            body['RegUrl'] = request.reg_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertCustom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.InsertCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_custom_with_options_async(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.InsertCustomResponse:
        """
        @param request: InsertCustomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertCustomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_file_name):
            body['CustomFileName'] = request.custom_file_name
        if not UtilClient.is_unset(request.custom_url):
            body['CustomUrl'] = request.custom_url
        if not UtilClient.is_unset(request.reg_file_name):
            body['RegFileName'] = request.reg_file_name
        if not UtilClient.is_unset(request.reg_url):
            body['RegUrl'] = request.reg_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertCustom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.InsertCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_custom(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
    ) -> alinlp_20200629_models.InsertCustomResponse:
        """
        @param request: InsertCustomRequest
        @return: InsertCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_custom_with_options(request, runtime)

    async def insert_custom_async(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
    ) -> alinlp_20200629_models.InsertCustomResponse:
        """
        @param request: InsertCustomRequest
        @return: InsertCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_custom_with_options_async(request, runtime)

    def open_alinlp_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        """
        @param request: OpenAlinlpServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAlinlpServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenAlinlpService',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.OpenAlinlpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_alinlp_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        """
        @param request: OpenAlinlpServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAlinlpServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenAlinlpService',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.OpenAlinlpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_alinlp_service(self) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        """
        @return: OpenAlinlpServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_alinlp_service_with_options(runtime)

    async def open_alinlp_service_async(self) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        """
        @return: OpenAlinlpServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_alinlp_service_with_options_async(runtime)

    def post_isconv_rewriter_with_options(
        self,
        tmp_req: alinlp_20200629_models.PostISConvRewriterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostISConvRewriterResponse:
        """
        @summary 多轮改写
        
        @param tmp_req: PostISConvRewriterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostISConvRewriterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISConvRewriterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISConvRewriter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISConvRewriterResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_isconv_rewriter_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.PostISConvRewriterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostISConvRewriterResponse:
        """
        @summary 多轮改写
        
        @param tmp_req: PostISConvRewriterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostISConvRewriterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISConvRewriterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISConvRewriter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISConvRewriterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_isconv_rewriter(
        self,
        request: alinlp_20200629_models.PostISConvRewriterRequest,
    ) -> alinlp_20200629_models.PostISConvRewriterResponse:
        """
        @summary 多轮改写
        
        @param request: PostISConvRewriterRequest
        @return: PostISConvRewriterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_isconv_rewriter_with_options(request, runtime)

    async def post_isconv_rewriter_async(
        self,
        request: alinlp_20200629_models.PostISConvRewriterRequest,
    ) -> alinlp_20200629_models.PostISConvRewriterResponse:
        """
        @summary 多轮改写
        
        @param request: PostISConvRewriterRequest
        @return: PostISConvRewriterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_isconv_rewriter_with_options_async(request, runtime)

    def post_isretrieve_router_with_options(
        self,
        tmp_req: alinlp_20200629_models.PostISRetrieveRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostISRetrieveRouterResponse:
        """
        @summary 开放域搜索判定
        
        @param tmp_req: PostISRetrieveRouterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostISRetrieveRouterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISRetrieveRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISRetrieveRouter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISRetrieveRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_isretrieve_router_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.PostISRetrieveRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostISRetrieveRouterResponse:
        """
        @summary 开放域搜索判定
        
        @param tmp_req: PostISRetrieveRouterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostISRetrieveRouterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISRetrieveRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISRetrieveRouter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISRetrieveRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_isretrieve_router(
        self,
        request: alinlp_20200629_models.PostISRetrieveRouterRequest,
    ) -> alinlp_20200629_models.PostISRetrieveRouterResponse:
        """
        @summary 开放域搜索判定
        
        @param request: PostISRetrieveRouterRequest
        @return: PostISRetrieveRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_isretrieve_router_with_options(request, runtime)

    async def post_isretrieve_router_async(
        self,
        request: alinlp_20200629_models.PostISRetrieveRouterRequest,
    ) -> alinlp_20200629_models.PostISRetrieveRouterResponse:
        """
        @summary 开放域搜索判定
        
        @param request: PostISRetrieveRouterRequest
        @return: PostISRetrieveRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_isretrieve_router_with_options_async(request, runtime)

    def post_msconv_search_token_generated_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
        """
        @summary 对话搜索身份凭证生成
        
        @param request: PostMSConvSearchTokenGeneratedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSConvSearchTokenGeneratedResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PostMSConvSearchTokenGenerated',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_msconv_search_token_generated_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
        """
        @summary 对话搜索身份凭证生成
        
        @param request: PostMSConvSearchTokenGeneratedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSConvSearchTokenGeneratedResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PostMSConvSearchTokenGenerated',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_msconv_search_token_generated(self) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
        """
        @summary 对话搜索身份凭证生成
        
        @return: PostMSConvSearchTokenGeneratedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_msconv_search_token_generated_with_options(runtime)

    async def post_msconv_search_token_generated_async(self) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
        """
        @summary 对话搜索身份凭证生成
        
        @return: PostMSConvSearchTokenGeneratedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_msconv_search_token_generated_with_options_async(runtime)

    def post_msdata_processing_count_with_options(
        self,
        tmp_req: alinlp_20200629_models.PostMSDataProcessingCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSDataProcessingCountResponse:
        """
        @summary 数据处理进度查询
        
        @param tmp_req: PostMSDataProcessingCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSDataProcessingCountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSDataProcessingCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ids):
            request.data_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ids, 'DataIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_ids_shrink):
            body['DataIds'] = request.data_ids_shrink
        if not UtilClient.is_unset(request.data_import_id):
            body['DataImportId'] = request.data_import_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSDataProcessingCount',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSDataProcessingCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_msdata_processing_count_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.PostMSDataProcessingCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSDataProcessingCountResponse:
        """
        @summary 数据处理进度查询
        
        @param tmp_req: PostMSDataProcessingCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSDataProcessingCountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSDataProcessingCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ids):
            request.data_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ids, 'DataIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_ids_shrink):
            body['DataIds'] = request.data_ids_shrink
        if not UtilClient.is_unset(request.data_import_id):
            body['DataImportId'] = request.data_import_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSDataProcessingCount',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSDataProcessingCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_msdata_processing_count(
        self,
        request: alinlp_20200629_models.PostMSDataProcessingCountRequest,
    ) -> alinlp_20200629_models.PostMSDataProcessingCountResponse:
        """
        @summary 数据处理进度查询
        
        @param request: PostMSDataProcessingCountRequest
        @return: PostMSDataProcessingCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_msdata_processing_count_with_options(request, runtime)

    async def post_msdata_processing_count_async(
        self,
        request: alinlp_20200629_models.PostMSDataProcessingCountRequest,
    ) -> alinlp_20200629_models.PostMSDataProcessingCountResponse:
        """
        @summary 数据处理进度查询
        
        @param request: PostMSDataProcessingCountRequest
        @return: PostMSDataProcessingCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_msdata_processing_count_with_options_async(request, runtime)

    def post_mssearch_enhance_with_options(
        self,
        tmp_req: alinlp_20200629_models.PostMSSearchEnhanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSSearchEnhanceResponse:
        """
        @summary 搜索增强
        
        @param tmp_req: PostMSSearchEnhanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSSearchEnhanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSSearchEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_config_info):
            request.custom_config_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_config_info, 'CustomConfigInfo', 'json')
        if not UtilClient.is_unset(tmp_req.fields):
            request.fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fields, 'Fields', 'json')
        if not UtilClient.is_unset(tmp_req.rank_model_info):
            request.rank_model_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rank_model_info, 'RankModelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.custom_config_info_shrink):
            body['CustomConfigInfo'] = request.custom_config_info_shrink
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.fields_shrink):
            body['Fields'] = request.fields_shrink
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.min_score):
            body['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.queries):
            body['Queries'] = request.queries
        if not UtilClient.is_unset(request.rank_model_info_shrink):
            body['RankModelInfo'] = request.rank_model_info_shrink
        if not UtilClient.is_unset(request.rows):
            body['Rows'] = request.rows
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uq):
            body['Uq'] = request.uq
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSSearchEnhance',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSSearchEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_mssearch_enhance_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.PostMSSearchEnhanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSSearchEnhanceResponse:
        """
        @summary 搜索增强
        
        @param tmp_req: PostMSSearchEnhanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSSearchEnhanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSSearchEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_config_info):
            request.custom_config_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_config_info, 'CustomConfigInfo', 'json')
        if not UtilClient.is_unset(tmp_req.fields):
            request.fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fields, 'Fields', 'json')
        if not UtilClient.is_unset(tmp_req.rank_model_info):
            request.rank_model_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rank_model_info, 'RankModelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.custom_config_info_shrink):
            body['CustomConfigInfo'] = request.custom_config_info_shrink
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.fields_shrink):
            body['Fields'] = request.fields_shrink
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.min_score):
            body['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.queries):
            body['Queries'] = request.queries
        if not UtilClient.is_unset(request.rank_model_info_shrink):
            body['RankModelInfo'] = request.rank_model_info_shrink
        if not UtilClient.is_unset(request.rows):
            body['Rows'] = request.rows
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uq):
            body['Uq'] = request.uq
        if not UtilClient.is_unset(request.x_dash_scope_open_apisource):
            body['X-DashScope-OpenAPISource'] = request.x_dash_scope_open_apisource
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSSearchEnhance',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSSearchEnhanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_mssearch_enhance(
        self,
        request: alinlp_20200629_models.PostMSSearchEnhanceRequest,
    ) -> alinlp_20200629_models.PostMSSearchEnhanceResponse:
        """
        @summary 搜索增强
        
        @param request: PostMSSearchEnhanceRequest
        @return: PostMSSearchEnhanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_mssearch_enhance_with_options(request, runtime)

    async def post_mssearch_enhance_async(
        self,
        request: alinlp_20200629_models.PostMSSearchEnhanceRequest,
    ) -> alinlp_20200629_models.PostMSSearchEnhanceResponse:
        """
        @summary 搜索增强
        
        @param request: PostMSSearchEnhanceRequest
        @return: PostMSSearchEnhanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_mssearch_enhance_with_options_async(request, runtime)

    def post_msservice_data_import_with_options(
        self,
        tmp_req: alinlp_20200629_models.PostMSServiceDataImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSServiceDataImportResponse:
        """
        @summary 导入服务数据V2
        
        @param tmp_req: PostMSServiceDataImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSServiceDataImportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSServiceDataImportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSServiceDataImport',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSServiceDataImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_msservice_data_import_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.PostMSServiceDataImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSServiceDataImportResponse:
        """
        @summary 导入服务数据V2
        
        @param tmp_req: PostMSServiceDataImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PostMSServiceDataImportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSServiceDataImportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSServiceDataImport',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSServiceDataImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_msservice_data_import(
        self,
        request: alinlp_20200629_models.PostMSServiceDataImportRequest,
    ) -> alinlp_20200629_models.PostMSServiceDataImportResponse:
        """
        @summary 导入服务数据V2
        
        @param request: PostMSServiceDataImportRequest
        @return: PostMSServiceDataImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.post_msservice_data_import_with_options(request, runtime)

    async def post_msservice_data_import_async(
        self,
        request: alinlp_20200629_models.PostMSServiceDataImportRequest,
    ) -> alinlp_20200629_models.PostMSServiceDataImportResponse:
        """
        @summary 导入服务数据V2
        
        @param request: PostMSServiceDataImportRequest
        @return: PostMSServiceDataImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.post_msservice_data_import_with_options_async(request, runtime)

    def request_table_qawith_options(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
        """
        @param request: RequestTableQARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestTableQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQA',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_table_qawith_options_async(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
        """
        @param request: RequestTableQARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestTableQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQA',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_table_qa(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
        """
        @param request: RequestTableQARequest
        @return: RequestTableQAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.request_table_qawith_options(request, runtime)

    async def request_table_qa_async(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
        """
        @param request: RequestTableQARequest
        @return: RequestTableQAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.request_table_qawith_options_async(request, runtime)

    def request_table_qaonline_with_options(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
        """
        @summary 表格问答在线接口
        
        @param request: RequestTableQAOnlineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestTableQAOnlineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bot_id):
            body['BotId'] = request.bot_id
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.question):
            body['Question'] = request.question
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQAOnline',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAOnlineResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_table_qaonline_with_options_async(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
        """
        @summary 表格问答在线接口
        
        @param request: RequestTableQAOnlineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestTableQAOnlineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bot_id):
            body['BotId'] = request.bot_id
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.question):
            body['Question'] = request.question
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQAOnline',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAOnlineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_table_qaonline(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
        """
        @summary 表格问答在线接口
        
        @param request: RequestTableQAOnlineRequest
        @return: RequestTableQAOnlineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.request_table_qaonline_with_options(request, runtime)

    async def request_table_qaonline_async(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
        """
        @summary 表格问答在线接口
        
        @param request: RequestTableQAOnlineRequest
        @return: RequestTableQAOnlineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.request_table_qaonline_with_options_async(request, runtime)

    def update_service_data_with_options(
        self,
        tmp_req: alinlp_20200629_models.UpdateServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
        """
        @summary 更新服务数据
        
        @param tmp_req: UpdateServiceDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.UpdateServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.UpdateServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_data_with_options_async(
        self,
        tmp_req: alinlp_20200629_models.UpdateServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
        """
        @summary 更新服务数据
        
        @param tmp_req: UpdateServiceDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.UpdateServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.UpdateServiceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_data(
        self,
        request: alinlp_20200629_models.UpdateServiceDataRequest,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
        """
        @summary 更新服务数据
        
        @param request: UpdateServiceDataRequest
        @return: UpdateServiceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_data_with_options(request, runtime)

    async def update_service_data_async(
        self,
        request: alinlp_20200629_models.UpdateServiceDataRequest,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
        """
        @summary 更新服务数据
        
        @param request: UpdateServiceDataRequest
        @return: UpdateServiceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_data_with_options_async(request, runtime)
