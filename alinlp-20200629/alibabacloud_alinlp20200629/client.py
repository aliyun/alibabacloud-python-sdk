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
        runtime = util_models.RuntimeOptions()
        return self.a_dclock_with_options(request, runtime)

    async def a_dclock_async(
        self,
        request: alinlp_20200629_models.ADClockRequest,
    ) -> alinlp_20200629_models.ADClockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.a_dclock_with_options_async(request, runtime)

    def a_dmmuwith_options(
        self,
        request: alinlp_20200629_models.ADMMURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMMUResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.a_dmmuwith_options(request, runtime)

    async def a_dmmu_async(
        self,
        request: alinlp_20200629_models.ADMMURequest,
    ) -> alinlp_20200629_models.ADMMUResponse:
        runtime = util_models.RuntimeOptions()
        return await self.a_dmmuwith_options_async(request, runtime)

    def a_dmini_cog_with_options(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_with_options(request, runtime)

    async def a_dmini_cog_async(
        self,
        request: alinlp_20200629_models.ADMiniCogRequest,
    ) -> alinlp_20200629_models.ADMiniCogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.a_dmini_cog_with_options_async(request, runtime)

    def a_dmini_cog_result_with_options(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_result_with_options(request, runtime)

    async def a_dmini_cog_result_async(
        self,
        request: alinlp_20200629_models.ADMiniCogResultRequest,
    ) -> alinlp_20200629_models.ADMiniCogResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.a_dmini_cog_result_with_options_async(request, runtime)

    def delete_service_data_by_conditions_with_options(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_conditions_with_options(request, runtime)

    async def delete_service_data_by_conditions_async(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByConditionsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByConditionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_data_by_conditions_with_options_async(request, runtime)

    def delete_service_data_by_ids_with_options(
        self,
        tmp_req: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_ids_with_options(request, runtime)

    async def delete_service_data_by_ids_async(
        self,
        request: alinlp_20200629_models.DeleteServiceDataByIdsRequest,
    ) -> alinlp_20200629_models.DeleteServiceDataByIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_data_by_ids_with_options_async(request, runtime)

    def get_brand_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_brand_ch_ecom_with_options(request, runtime)

    async def get_brand_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetBrandChEcomRequest,
    ) -> alinlp_20200629_models.GetBrandChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_brand_ch_ecom_with_options_async(request, runtime)

    def get_cate_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_cate_ch_ecom_with_options(request, runtime)

    async def get_cate_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetCateChEcomRequest,
    ) -> alinlp_20200629_models.GetCateChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cate_ch_ecom_with_options_async(request, runtime)

    def get_check_duplication_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_check_duplication_ch_medical_with_options(request, runtime)

    async def get_check_duplication_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetCheckDuplicationChMedicalRequest,
    ) -> alinlp_20200629_models.GetCheckDuplicationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_check_duplication_ch_medical_with_options_async(request, runtime)

    def get_diagnosis_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_ch_medical_with_options(request, runtime)

    async def get_diagnosis_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetDiagnosisChMedicalRequest,
    ) -> alinlp_20200629_models.GetDiagnosisChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnosis_ch_medical_with_options_async(request, runtime)

    def get_dp_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_ecom_with_options(request, runtime)

    async def get_dp_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetDpChEcomRequest,
    ) -> alinlp_20200629_models.GetDpChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_ecom_with_options_async(request, runtime)

    def get_dp_ch_general_ctbwith_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_ctbwith_options(request, runtime)

    async def get_dp_ch_general_ctb_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralCTBRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralCTBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_ctbwith_options_async(request, runtime)

    def get_dp_ch_general_stanford_with_options(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_stanford_with_options(request, runtime)

    async def get_dp_ch_general_stanford_async(
        self,
        request: alinlp_20200629_models.GetDpChGeneralStanfordRequest,
    ) -> alinlp_20200629_models.GetDpChGeneralStanfordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dp_ch_general_stanford_with_options_async(request, runtime)

    def get_ec_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ec_ch_general_with_options(request, runtime)

    async def get_ec_ch_general_async(
        self,
        request: alinlp_20200629_models.GetEcChGeneralRequest,
    ) -> alinlp_20200629_models.GetEcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_ch_general_with_options_async(request, runtime)

    def get_ec_en_general_with_options(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ec_en_general_with_options(request, runtime)

    async def get_ec_en_general_async(
        self,
        request: alinlp_20200629_models.GetEcEnGeneralRequest,
    ) -> alinlp_20200629_models.GetEcEnGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ec_en_general_with_options_async(request, runtime)

    def get_embedding_with_options(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_embedding_with_options(request, runtime)

    async def get_embedding_async(
        self,
        request: alinlp_20200629_models.GetEmbeddingRequest,
    ) -> alinlp_20200629_models.GetEmbeddingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_embedding_with_options_async(request, runtime)

    def get_item_pub_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_item_pub_ch_ecom_with_options(request, runtime)

    async def get_item_pub_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetItemPubChEcomRequest,
    ) -> alinlp_20200629_models.GetItemPubChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_pub_ch_ecom_with_options_async(request, runtime)

    def get_keyword_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_ch_ecom_with_options(request, runtime)

    async def get_keyword_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordChEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_ch_ecom_with_options_async(request, runtime)

    def get_keyword_en_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_en_ecom_with_options(request, runtime)

    async def get_keyword_en_ecom_async(
        self,
        request: alinlp_20200629_models.GetKeywordEnEcomRequest,
    ) -> alinlp_20200629_models.GetKeywordEnEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_en_ecom_with_options_async(request, runtime)

    def get_medicine_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_medicine_ch_medical_with_options(request, runtime)

    async def get_medicine_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetMedicineChMedicalRequest,
    ) -> alinlp_20200629_models.GetMedicineChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_medicine_ch_medical_with_options_async(request, runtime)

    def get_ner_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_ecom_with_options(request, runtime)

    async def get_ner_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerChEcomRequest,
    ) -> alinlp_20200629_models.GetNerChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_ecom_with_options_async(request, runtime)

    def get_ner_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_medical_with_options(request, runtime)

    async def get_ner_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetNerChMedicalRequest,
    ) -> alinlp_20200629_models.GetNerChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_ch_medical_with_options_async(request, runtime)

    def get_ner_customized_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_ch_ecom_with_options(request, runtime)

    async def get_ner_customized_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedChEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_ch_ecom_with_options_async(request, runtime)

    def get_ner_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_sea_ecom_with_options(request, runtime)

    async def get_ner_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetNerCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetNerCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ner_customized_sea_ecom_with_options_async(request, runtime)

    def get_open_nluwith_options(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluwith_options(request, runtime)

    async def get_open_nlu_async(
        self,
        request: alinlp_20200629_models.GetOpenNLURequest,
    ) -> alinlp_20200629_models.GetOpenNLUResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_open_nluwith_options_async(request, runtime)

    def get_open_nluhigh_recall_with_options(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluhigh_recall_with_options(request, runtime)

    async def get_open_nluhigh_recall_async(
        self,
        request: alinlp_20200629_models.GetOpenNLUHighRecallRequest,
    ) -> alinlp_20200629_models.GetOpenNLUHighRecallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_open_nluhigh_recall_with_options_async(request, runtime)

    def get_operation_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_operation_ch_medical_with_options(request, runtime)

    async def get_operation_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetOperationChMedicalRequest,
    ) -> alinlp_20200629_models.GetOperationChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_ch_medical_with_options_async(request, runtime)

    def get_pos_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_ecom_with_options(request, runtime)

    async def get_pos_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetPosChEcomRequest,
    ) -> alinlp_20200629_models.GetPosChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_ecom_with_options_async(request, runtime)

    def get_pos_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_general_with_options(request, runtime)

    async def get_pos_ch_general_async(
        self,
        request: alinlp_20200629_models.GetPosChGeneralRequest,
    ) -> alinlp_20200629_models.GetPosChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pos_ch_general_with_options_async(request, runtime)

    def get_price_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_price_ch_ecom_with_options(request, runtime)

    async def get_price_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetPriceChEcomRequest,
    ) -> alinlp_20200629_models.GetPriceChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_price_ch_ecom_with_options_async(request, runtime)

    def get_ssetest_with_options(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSSETestResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ssetest_with_options(request, runtime)

    async def get_ssetest_async(
        self,
        request: alinlp_20200629_models.GetSSETestRequest,
    ) -> alinlp_20200629_models.GetSSETestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ssetest_with_options_async(request, runtime)

    def get_sa_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_sa_ch_general_with_options(request, runtime)

    async def get_sa_ch_general_async(
        self,
        request: alinlp_20200629_models.GetSaChGeneralRequest,
    ) -> alinlp_20200629_models.GetSaChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_ch_general_with_options_async(request, runtime)

    def get_sa_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_sa_sea_ecom_with_options(request, runtime)

    async def get_sa_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetSaSeaEcomRequest,
    ) -> alinlp_20200629_models.GetSaSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_sea_ecom_with_options_async(request, runtime)

    def get_service_data_import_status_with_options(
        self,
        tmp_req: alinlp_20200629_models.GetServiceDataImportStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_service_data_import_status_with_options(request, runtime)

    async def get_service_data_import_status_async(
        self,
        request: alinlp_20200629_models.GetServiceDataImportStatusRequest,
    ) -> alinlp_20200629_models.GetServiceDataImportStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_data_import_status_with_options_async(request, runtime)

    def get_similarity_ch_medical_with_options(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_similarity_ch_medical_with_options(request, runtime)

    async def get_similarity_ch_medical_async(
        self,
        request: alinlp_20200629_models.GetSimilarityChMedicalRequest,
    ) -> alinlp_20200629_models.GetSimilarityChMedicalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_similarity_ch_medical_with_options_async(request, runtime)

    def get_summary_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_summary_ch_ecom_with_options(request, runtime)

    async def get_summary_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetSummaryChEcomRequest,
    ) -> alinlp_20200629_models.GetSummaryChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_summary_ch_ecom_with_options_async(request, runtime)

    def get_table_qaservice_info_by_id_with_options(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_table_qaservice_info_by_id_with_options(request, runtime)

    async def get_table_qaservice_info_by_id_async(
        self,
        request: alinlp_20200629_models.GetTableQAServiceInfoByIdRequest,
    ) -> alinlp_20200629_models.GetTableQAServiceInfoByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_table_qaservice_info_by_id_with_options_async(request, runtime)

    def get_tc_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_ecom_with_options(request, runtime)

    async def get_tc_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTcChEcomRequest,
    ) -> alinlp_20200629_models.GetTcChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_ecom_with_options_async(request, runtime)

    def get_tc_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_general_with_options(request, runtime)

    async def get_tc_ch_general_async(
        self,
        request: alinlp_20200629_models.GetTcChGeneralRequest,
    ) -> alinlp_20200629_models.GetTcChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tc_ch_general_with_options_async(request, runtime)

    def get_ts_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ts_ch_ecom_with_options(request, runtime)

    async def get_ts_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetTsChEcomRequest,
    ) -> alinlp_20200629_models.GetTsChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ts_ch_ecom_with_options_async(request, runtime)

    def get_user_upload_sign_with_options(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_user_upload_sign_with_options(request, runtime)

    async def get_user_upload_sign_async(
        self,
        request: alinlp_20200629_models.GetUserUploadSignRequest,
    ) -> alinlp_20200629_models.GetUserUploadSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_upload_sign_with_options_async(request, runtime)

    def get_we_ch_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_comment_with_options(request, runtime)

    async def get_we_ch_comment_async(
        self,
        request: alinlp_20200629_models.GetWeChCommentRequest,
    ) -> alinlp_20200629_models.GetWeChCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_comment_with_options_async(request, runtime)

    def get_we_ch_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_ecom_with_options(request, runtime)

    async def get_we_ch_ecom_async(
        self,
        request: alinlp_20200629_models.GetWeChEcomRequest,
    ) -> alinlp_20200629_models.GetWeChEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_ecom_with_options_async(request, runtime)

    def get_we_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_entertainment_with_options(request, runtime)

    async def get_we_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWeChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWeChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_entertainment_with_options_async(request, runtime)

    def get_we_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_general_with_options(request, runtime)

    async def get_we_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWeChGeneralRequest,
    ) -> alinlp_20200629_models.GetWeChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_general_with_options_async(request, runtime)

    def get_we_ch_search_with_options(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_search_with_options(request, runtime)

    async def get_we_ch_search_async(
        self,
        request: alinlp_20200629_models.GetWeChSearchRequest,
    ) -> alinlp_20200629_models.GetWeChSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_we_ch_search_with_options_async(request, runtime)

    def get_ws_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_ch_general_with_options(request, runtime)

    async def get_ws_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_comment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_comment_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_comment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomCommentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_comment_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_content_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_content_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_content_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomContentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_content_with_options_async(request, runtime)

    def get_ws_customized_ch_ecom_title_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_title_with_options(request, runtime)

    async def get_ws_customized_ch_ecom_title_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEcomTitleRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_ecom_title_with_options_async(request, runtime)

    def get_ws_customized_ch_entertainment_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_entertainment_with_options(request, runtime)

    async def get_ws_customized_ch_entertainment_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChEntertainmentRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_entertainment_with_options_async(request, runtime)

    def get_ws_customized_ch_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_general_with_options(request, runtime)

    async def get_ws_customized_ch_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_general_with_options_async(request, runtime)

    def get_ws_customized_ch_o2owith_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_o2owith_options(request, runtime)

    async def get_ws_customized_ch_o2o_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedChO2ORequest,
    ) -> alinlp_20200629_models.GetWsCustomizedChO2OResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_ch_o2owith_options_async(request, runtime)

    def get_ws_customized_sea_ecom_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_ecom_with_options(request, runtime)

    async def get_ws_customized_sea_ecom_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaEcomRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaEcomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_ecom_with_options_async(request, runtime)

    def get_ws_customized_sea_general_with_options(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_general_with_options(request, runtime)

    async def get_ws_customized_sea_general_async(
        self,
        request: alinlp_20200629_models.GetWsCustomizedSeaGeneralRequest,
    ) -> alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ws_customized_sea_general_with_options_async(request, runtime)

    def import_service_data_with_options(
        self,
        tmp_req: alinlp_20200629_models.ImportServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.import_service_data_with_options(request, runtime)

    async def import_service_data_async(
        self,
        request: alinlp_20200629_models.ImportServiceDataRequest,
    ) -> alinlp_20200629_models.ImportServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_service_data_with_options_async(request, runtime)

    def insert_custom_with_options(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.InsertCustomResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.insert_custom_with_options(request, runtime)

    async def insert_custom_async(
        self,
        request: alinlp_20200629_models.InsertCustomRequest,
    ) -> alinlp_20200629_models.InsertCustomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_custom_with_options_async(request, runtime)

    def open_alinlp_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.open_alinlp_service_with_options(runtime)

    async def open_alinlp_service_async(self) -> alinlp_20200629_models.OpenAlinlpServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_alinlp_service_with_options_async(runtime)

    def post_msconv_search_token_generated_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.post_msconv_search_token_generated_with_options(runtime)

    async def post_msconv_search_token_generated_async(self) -> alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.post_msconv_search_token_generated_with_options_async(runtime)

    def request_table_qawith_options(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.request_table_qawith_options(request, runtime)

    async def request_table_qa_async(
        self,
        request: alinlp_20200629_models.RequestTableQARequest,
    ) -> alinlp_20200629_models.RequestTableQAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_table_qawith_options_async(request, runtime)

    def request_table_qaonline_with_options(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.request_table_qaonline_with_options(request, runtime)

    async def request_table_qaonline_async(
        self,
        request: alinlp_20200629_models.RequestTableQAOnlineRequest,
    ) -> alinlp_20200629_models.RequestTableQAOnlineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_table_qaonline_with_options_async(request, runtime)

    def update_service_data_with_options(
        self,
        tmp_req: alinlp_20200629_models.UpdateServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_service_data_with_options(request, runtime)

    async def update_service_data_async(
        self,
        request: alinlp_20200629_models.UpdateServiceDataRequest,
    ) -> alinlp_20200629_models.UpdateServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_data_with_options_async(request, runtime)
