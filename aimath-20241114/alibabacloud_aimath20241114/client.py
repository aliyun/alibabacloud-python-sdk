# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aimath20241114 import models as aimath_20241114_models
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
        self._endpoint = self.get_endpoint('aimath', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def gen_analysis_with_options(
        self,
        request: aimath_20241114_models.GenAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GenAnalysisResponse:
        """
        @summary 生成解题分析
        
        @param request: GenAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_content):
            body['ExerciseContent'] = request.exercise_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenAnalysis',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GenAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_analysis_with_options_async(
        self,
        request: aimath_20241114_models.GenAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GenAnalysisResponse:
        """
        @summary 生成解题分析
        
        @param request: GenAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_content):
            body['ExerciseContent'] = request.exercise_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenAnalysis',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GenAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_analysis(
        self,
        request: aimath_20241114_models.GenAnalysisRequest,
    ) -> aimath_20241114_models.GenAnalysisResponse:
        """
        @summary 生成解题分析
        
        @param request: GenAnalysisRequest
        @return: GenAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.gen_analysis_with_options(request, runtime)

    async def gen_analysis_async(
        self,
        request: aimath_20241114_models.GenAnalysisRequest,
    ) -> aimath_20241114_models.GenAnalysisResponse:
        """
        @summary 生成解题分析
        
        @param request: GenAnalysisRequest
        @return: GenAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.gen_analysis_with_options_async(request, runtime)

    def gen_step_with_options(
        self,
        request: aimath_20241114_models.GenStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GenStepResponse:
        """
        @summary 生成数学解题步骤
        
        @param request: GenStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenStepResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenStep',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GenStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_step_with_options_async(
        self,
        request: aimath_20241114_models.GenStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GenStepResponse:
        """
        @summary 生成数学解题步骤
        
        @param request: GenStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenStepResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenStep',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GenStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_step(
        self,
        request: aimath_20241114_models.GenStepRequest,
    ) -> aimath_20241114_models.GenStepResponse:
        """
        @summary 生成数学解题步骤
        
        @param request: GenStepRequest
        @return: GenStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.gen_step_with_options(request, runtime)

    async def gen_step_async(
        self,
        request: aimath_20241114_models.GenStepRequest,
    ) -> aimath_20241114_models.GenStepResponse:
        """
        @summary 生成数学解题步骤
        
        @param request: GenStepRequest
        @return: GenStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.gen_step_with_options_async(request, runtime)

    def global_confirm_with_options(
        self,
        request: aimath_20241114_models.GlobalConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GlobalConfirmResponse:
        """
        @summary 全局确认修订完成
        
        @param request: GlobalConfirmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GlobalConfirmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GlobalConfirm',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GlobalConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_confirm_with_options_async(
        self,
        request: aimath_20241114_models.GlobalConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.GlobalConfirmResponse:
        """
        @summary 全局确认修订完成
        
        @param request: GlobalConfirmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GlobalConfirmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GlobalConfirm',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.GlobalConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_confirm(
        self,
        request: aimath_20241114_models.GlobalConfirmRequest,
    ) -> aimath_20241114_models.GlobalConfirmResponse:
        """
        @summary 全局确认修订完成
        
        @param request: GlobalConfirmRequest
        @return: GlobalConfirmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.global_confirm_with_options(request, runtime)

    async def global_confirm_async(
        self,
        request: aimath_20241114_models.GlobalConfirmRequest,
    ) -> aimath_20241114_models.GlobalConfirmResponse:
        """
        @summary 全局确认修订完成
        
        @param request: GlobalConfirmRequest
        @return: GlobalConfirmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.global_confirm_with_options_async(request, runtime)

    def update_analysis_with_options(
        self,
        request: aimath_20241114_models.UpdateAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.UpdateAnalysisResponse:
        """
        @summary 修订解题分析
        
        @param request: UpdateAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_code):
            body['ContentCode'] = request.content_code
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAnalysis',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.UpdateAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_analysis_with_options_async(
        self,
        request: aimath_20241114_models.UpdateAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.UpdateAnalysisResponse:
        """
        @summary 修订解题分析
        
        @param request: UpdateAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_code):
            body['ContentCode'] = request.content_code
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAnalysis',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.UpdateAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_analysis(
        self,
        request: aimath_20241114_models.UpdateAnalysisRequest,
    ) -> aimath_20241114_models.UpdateAnalysisResponse:
        """
        @summary 修订解题分析
        
        @param request: UpdateAnalysisRequest
        @return: UpdateAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_analysis_with_options(request, runtime)

    async def update_analysis_async(
        self,
        request: aimath_20241114_models.UpdateAnalysisRequest,
    ) -> aimath_20241114_models.UpdateAnalysisResponse:
        """
        @summary 修订解题分析
        
        @param request: UpdateAnalysisRequest
        @return: UpdateAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_analysis_with_options_async(request, runtime)

    def update_step_with_options(
        self,
        request: aimath_20241114_models.UpdateStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.UpdateStepResponse:
        """
        @summary 修订解题步骤
        
        @param request: UpdateStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStepResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_code):
            body['ContentCode'] = request.content_code
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStep',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.UpdateStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_step_with_options_async(
        self,
        request: aimath_20241114_models.UpdateStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aimath_20241114_models.UpdateStepResponse:
        """
        @summary 修订解题步骤
        
        @param request: UpdateStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStepResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_code):
            body['ContentCode'] = request.content_code
        if not UtilClient.is_unset(request.exercise_code):
            body['ExerciseCode'] = request.exercise_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStep',
            version='2024-11-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aimath_20241114_models.UpdateStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_step(
        self,
        request: aimath_20241114_models.UpdateStepRequest,
    ) -> aimath_20241114_models.UpdateStepResponse:
        """
        @summary 修订解题步骤
        
        @param request: UpdateStepRequest
        @return: UpdateStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_step_with_options(request, runtime)

    async def update_step_async(
        self,
        request: aimath_20241114_models.UpdateStepRequest,
    ) -> aimath_20241114_models.UpdateStepResponse:
        """
        @summary 修订解题步骤
        
        @param request: UpdateStepRequest
        @return: UpdateStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_step_with_options_async(request, runtime)
