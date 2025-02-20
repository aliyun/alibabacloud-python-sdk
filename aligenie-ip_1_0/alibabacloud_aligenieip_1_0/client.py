# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieip_1_0 import models as ali_genieip__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cartoon_with_options(
        self,
        request: ali_genieip__1__0_models.AddCartoonRequest,
        headers: ali_genieip__1__0_models.AddCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCartoonResponse:
        """
        @summary 添加动画
        
        @param request: AddCartoonRequest
        @param headers: AddCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.start_video_md_5):
            body['StartVideoMd5'] = request.start_video_md_5
        if not UtilClient.is_unset(request.start_video_url):
            body['StartVideoUrl'] = request.start_video_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCartoonResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCartoonResponse(),
                self.execute(params, req, runtime)
            )

    async def add_cartoon_with_options_async(
        self,
        request: ali_genieip__1__0_models.AddCartoonRequest,
        headers: ali_genieip__1__0_models.AddCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCartoonResponse:
        """
        @summary 添加动画
        
        @param request: AddCartoonRequest
        @param headers: AddCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.start_video_md_5):
            body['StartVideoMd5'] = request.start_video_md_5
        if not UtilClient.is_unset(request.start_video_url):
            body['StartVideoUrl'] = request.start_video_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCartoonResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCartoonResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_cartoon(
        self,
        request: ali_genieip__1__0_models.AddCartoonRequest,
    ) -> ali_genieip__1__0_models.AddCartoonResponse:
        """
        @summary 添加动画
        
        @param request: AddCartoonRequest
        @return: AddCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCartoonHeaders()
        return self.add_cartoon_with_options(request, headers, runtime)

    async def add_cartoon_async(
        self,
        request: ali_genieip__1__0_models.AddCartoonRequest,
    ) -> ali_genieip__1__0_models.AddCartoonResponse:
        """
        @summary 添加动画
        
        @param request: AddCartoonRequest
        @return: AddCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCartoonHeaders()
        return await self.add_cartoon_with_options_async(request, headers, runtime)

    def add_custom_qawith_options(
        self,
        tmp_req: ali_genieip__1__0_models.AddCustomQARequest,
        headers: ali_genieip__1__0_models.AddCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCustomQAResponse:
        """
        @summary 新增自定义问答
        
        @param tmp_req: AddCustomQARequest
        @param headers: AddCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAResponse(),
                self.execute(params, req, runtime)
            )

    async def add_custom_qawith_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AddCustomQARequest,
        headers: ali_genieip__1__0_models.AddCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCustomQAResponse:
        """
        @summary 新增自定义问答
        
        @param tmp_req: AddCustomQARequest
        @param headers: AddCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_custom_qa(
        self,
        request: ali_genieip__1__0_models.AddCustomQARequest,
    ) -> ali_genieip__1__0_models.AddCustomQAResponse:
        """
        @summary 新增自定义问答
        
        @param request: AddCustomQARequest
        @return: AddCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCustomQAHeaders()
        return self.add_custom_qawith_options(request, headers, runtime)

    async def add_custom_qa_async(
        self,
        request: ali_genieip__1__0_models.AddCustomQARequest,
    ) -> ali_genieip__1__0_models.AddCustomQAResponse:
        """
        @summary 新增自定义问答
        
        @param request: AddCustomQARequest
        @return: AddCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCustomQAHeaders()
        return await self.add_custom_qawith_options_async(request, headers, runtime)

    def add_custom_qav2with_options(
        self,
        tmp_req: ali_genieip__1__0_models.AddCustomQAV2Request,
        headers: ali_genieip__1__0_models.AddCustomQAV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCustomQAV2Response:
        """
        @summary 添加问答V2
        
        @param tmp_req: AddCustomQAV2Request
        @param headers: AddCustomQAV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomQAV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddCustomQAV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomQAV2',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addQAV2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAV2Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAV2Response(),
                self.execute(params, req, runtime)
            )

    async def add_custom_qav2with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AddCustomQAV2Request,
        headers: ali_genieip__1__0_models.AddCustomQAV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddCustomQAV2Response:
        """
        @summary 添加问答V2
        
        @param tmp_req: AddCustomQAV2Request
        @param headers: AddCustomQAV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomQAV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddCustomQAV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCustomQAV2',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addQAV2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAV2Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddCustomQAV2Response(),
                await self.execute_async(params, req, runtime)
            )

    def add_custom_qav2(
        self,
        request: ali_genieip__1__0_models.AddCustomQAV2Request,
    ) -> ali_genieip__1__0_models.AddCustomQAV2Response:
        """
        @summary 添加问答V2
        
        @param request: AddCustomQAV2Request
        @return: AddCustomQAV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCustomQAV2Headers()
        return self.add_custom_qav2with_options(request, headers, runtime)

    async def add_custom_qav2_async(
        self,
        request: ali_genieip__1__0_models.AddCustomQAV2Request,
    ) -> ali_genieip__1__0_models.AddCustomQAV2Response:
        """
        @summary 添加问答V2
        
        @param request: AddCustomQAV2Request
        @return: AddCustomQAV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddCustomQAV2Headers()
        return await self.add_custom_qav2with_options_async(request, headers, runtime)

    def add_message_template_with_options(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
        headers: ali_genieip__1__0_models.AddMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        """
        @summary 添加消息模板
        
        @param request: AddMessageTemplateRequest
        @param headers: AddMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddMessageTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddMessageTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def add_message_template_with_options_async(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
        headers: ali_genieip__1__0_models.AddMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        """
        @summary 添加消息模板
        
        @param request: AddMessageTemplateRequest
        @param headers: AddMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddMessageTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddMessageTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_message_template(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        """
        @summary 添加消息模板
        
        @param request: AddMessageTemplateRequest
        @return: AddMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddMessageTemplateHeaders()
        return self.add_message_template_with_options(request, headers, runtime)

    async def add_message_template_async(
        self,
        request: ali_genieip__1__0_models.AddMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.AddMessageTemplateResponse:
        """
        @summary 添加消息模板
        
        @param request: AddMessageTemplateRequest
        @return: AddMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddMessageTemplateHeaders()
        return await self.add_message_template_with_options_async(request, headers, runtime)

    def add_or_update_dis_play_modes_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateDisPlayModesRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateDisPlayModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse:
        """
        @summary 新增或者编辑带屏展示模式
        
        @param tmp_req: AddOrUpdateDisPlayModesRequest
        @param headers: AddOrUpdateDisPlayModesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateDisPlayModesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateDisPlayModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateDisPlayModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateDisPlayModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse(),
                self.execute(params, req, runtime)
            )

    async def add_or_update_dis_play_modes_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateDisPlayModesRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateDisPlayModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse:
        """
        @summary 新增或者编辑带屏展示模式
        
        @param tmp_req: AddOrUpdateDisPlayModesRequest
        @param headers: AddOrUpdateDisPlayModesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateDisPlayModesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateDisPlayModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateDisPlayModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateDisPlayModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_or_update_dis_play_modes(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateDisPlayModesRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse:
        """
        @summary 新增或者编辑带屏展示模式
        
        @param request: AddOrUpdateDisPlayModesRequest
        @return: AddOrUpdateDisPlayModesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateDisPlayModesHeaders()
        return self.add_or_update_dis_play_modes_with_options(request, headers, runtime)

    async def add_or_update_dis_play_modes_async(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateDisPlayModesRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateDisPlayModesResponse:
        """
        @summary 新增或者编辑带屏展示模式
        
        @param request: AddOrUpdateDisPlayModesRequest
        @return: AddOrUpdateDisPlayModesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateDisPlayModesHeaders()
        return await self.add_or_update_dis_play_modes_with_options_async(request, headers, runtime)

    def add_or_update_hotel_setting_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateHotelSettingRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse:
        """
        @summary 新增或者编辑定制配置
        
        @param tmp_req: AddOrUpdateHotelSettingRequest
        @param headers: AddOrUpdateHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateHotelSettingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateHotelSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        if not UtilClient.is_unset(tmp_req.night_mode):
            request.night_mode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.night_mode, 'NightMode', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        if not UtilClient.is_unset(request.night_mode_shrink):
            body['NightMode'] = request.night_mode_shrink
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def add_or_update_hotel_setting_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateHotelSettingRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse:
        """
        @summary 新增或者编辑定制配置
        
        @param tmp_req: AddOrUpdateHotelSettingRequest
        @param headers: AddOrUpdateHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateHotelSettingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateHotelSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_device_mode_list):
            request.hotel_device_mode_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_device_mode_list, 'HotelDeviceModeList', 'json')
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        if not UtilClient.is_unset(tmp_req.night_mode):
            request.night_mode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.night_mode, 'NightMode', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_device_mode_list_shrink):
            body['HotelDeviceModeList'] = request.hotel_device_mode_list_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        if not UtilClient.is_unset(request.night_mode_shrink):
            body['NightMode'] = request.night_mode_shrink
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_or_update_hotel_setting(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateHotelSettingRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse:
        """
        @summary 新增或者编辑定制配置
        
        @param request: AddOrUpdateHotelSettingRequest
        @return: AddOrUpdateHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateHotelSettingHeaders()
        return self.add_or_update_hotel_setting_with_options(request, headers, runtime)

    async def add_or_update_hotel_setting_async(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateHotelSettingRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateHotelSettingResponse:
        """
        @summary 新增或者编辑定制配置
        
        @param request: AddOrUpdateHotelSettingRequest
        @return: AddOrUpdateHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateHotelSettingHeaders()
        return await self.add_or_update_hotel_setting_with_options_async(request, headers, runtime)

    def add_or_update_screen_saver_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateScreenSaverRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse:
        """
        @summary 新增或者编辑带屏屏保
        
        @param tmp_req: AddOrUpdateScreenSaverRequest
        @param headers: AddOrUpdateScreenSaverHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateScreenSaverResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse(),
                self.execute(params, req, runtime)
            )

    async def add_or_update_screen_saver_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AddOrUpdateScreenSaverRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse:
        """
        @summary 新增或者编辑带屏屏保
        
        @param tmp_req: AddOrUpdateScreenSaverRequest
        @param headers: AddOrUpdateScreenSaverHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateScreenSaverResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AddOrUpdateScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_screen_saver):
            request.hotel_screen_saver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_screen_saver, 'HotelScreenSaver', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_screen_saver_shrink):
            body['HotelScreenSaver'] = request.hotel_screen_saver_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_or_update_screen_saver(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateScreenSaverRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse:
        """
        @summary 新增或者编辑带屏屏保
        
        @param request: AddOrUpdateScreenSaverRequest
        @return: AddOrUpdateScreenSaverResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateScreenSaverHeaders()
        return self.add_or_update_screen_saver_with_options(request, headers, runtime)

    async def add_or_update_screen_saver_async(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateScreenSaverRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateScreenSaverResponse:
        """
        @summary 新增或者编辑带屏屏保
        
        @param request: AddOrUpdateScreenSaverRequest
        @return: AddOrUpdateScreenSaverResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateScreenSaverHeaders()
        return await self.add_or_update_screen_saver_with_options_async(request, headers, runtime)

    def add_or_update_welcome_text_with_options(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateWelcomeTextRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateWelcomeTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse:
        """
        @summary 添加/更新欢迎语信息
        
        @param request: AddOrUpdateWelcomeTextRequest
        @param headers: AddOrUpdateWelcomeTextHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateWelcomeTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_url):
            body['MusicUrl'] = request.music_url
        if not UtilClient.is_unset(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateWelcomeText',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateWelcomeText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse(),
                self.execute(params, req, runtime)
            )

    async def add_or_update_welcome_text_with_options_async(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateWelcomeTextRequest,
        headers: ali_genieip__1__0_models.AddOrUpdateWelcomeTextHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse:
        """
        @summary 添加/更新欢迎语信息
        
        @param request: AddOrUpdateWelcomeTextRequest
        @param headers: AddOrUpdateWelcomeTextHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateWelcomeTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_url):
            body['MusicUrl'] = request.music_url
        if not UtilClient.is_unset(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateWelcomeText',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/addOrUpdateWelcomeText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_or_update_welcome_text(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateWelcomeTextRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse:
        """
        @summary 添加/更新欢迎语信息
        
        @param request: AddOrUpdateWelcomeTextRequest
        @return: AddOrUpdateWelcomeTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateWelcomeTextHeaders()
        return self.add_or_update_welcome_text_with_options(request, headers, runtime)

    async def add_or_update_welcome_text_async(
        self,
        request: ali_genieip__1__0_models.AddOrUpdateWelcomeTextRequest,
    ) -> ali_genieip__1__0_models.AddOrUpdateWelcomeTextResponse:
        """
        @summary 添加/更新欢迎语信息
        
        @param request: AddOrUpdateWelcomeTextRequest
        @return: AddOrUpdateWelcomeTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AddOrUpdateWelcomeTextHeaders()
        return await self.add_or_update_welcome_text_with_options_async(request, headers, runtime)

    def audit_hotel_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.AuditHotelRequest,
        headers: ali_genieip__1__0_models.AuditHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AuditHotelResponse:
        """
        @summary 审批酒店
        
        @param tmp_req: AuditHotelRequest
        @param headers: AuditHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AuditHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.audit_hotel_req):
            request.audit_hotel_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audit_hotel_req, 'AuditHotelReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_hotel_req_shrink):
            query['AuditHotelReq'] = request.audit_hotel_req_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/auditHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AuditHotelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AuditHotelResponse(),
                self.execute(params, req, runtime)
            )

    async def audit_hotel_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.AuditHotelRequest,
        headers: ali_genieip__1__0_models.AuditHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.AuditHotelResponse:
        """
        @summary 审批酒店
        
        @param tmp_req: AuditHotelRequest
        @param headers: AuditHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.AuditHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.audit_hotel_req):
            request.audit_hotel_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audit_hotel_req, 'AuditHotelReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_hotel_req_shrink):
            query['AuditHotelReq'] = request.audit_hotel_req_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/auditHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.AuditHotelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.AuditHotelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def audit_hotel(
        self,
        request: ali_genieip__1__0_models.AuditHotelRequest,
    ) -> ali_genieip__1__0_models.AuditHotelResponse:
        """
        @summary 审批酒店
        
        @param request: AuditHotelRequest
        @return: AuditHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AuditHotelHeaders()
        return self.audit_hotel_with_options(request, headers, runtime)

    async def audit_hotel_async(
        self,
        request: ali_genieip__1__0_models.AuditHotelRequest,
    ) -> ali_genieip__1__0_models.AuditHotelResponse:
        """
        @summary 审批酒店
        
        @param request: AuditHotelRequest
        @return: AuditHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.AuditHotelHeaders()
        return await self.audit_hotel_with_options_async(request, headers, runtime)

    def batch_add_hotel_room_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchAddHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        """
        @summary 批量创建房间
        
        @param tmp_req: BatchAddHotelRoomRequest
        @param headers: BatchAddHotelRoomHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddHotelRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchAddHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchAddHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_add_hotel_room_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchAddHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        """
        @summary 批量创建房间
        
        @param tmp_req: BatchAddHotelRoomRequest
        @param headers: BatchAddHotelRoomHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddHotelRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchAddHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchAddHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchAddHotelRoomResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_add_hotel_room(
        self,
        request: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        """
        @summary 批量创建房间
        
        @param request: BatchAddHotelRoomRequest
        @return: BatchAddHotelRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchAddHotelRoomHeaders()
        return self.batch_add_hotel_room_with_options(request, headers, runtime)

    async def batch_add_hotel_room_async(
        self,
        request: ali_genieip__1__0_models.BatchAddHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchAddHotelRoomResponse:
        """
        @summary 批量创建房间
        
        @param request: BatchAddHotelRoomRequest
        @return: BatchAddHotelRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchAddHotelRoomHeaders()
        return await self.batch_add_hotel_room_with_options_async(request, headers, runtime)

    def batch_delete_hotel_room_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        """
        @summary 批量删除房间
        
        @param tmp_req: BatchDeleteHotelRoomRequest
        @param headers: BatchDeleteHotelRoomHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteHotelRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchDeleteHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchDeleteHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_delete_hotel_room_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
        headers: ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        """
        @summary 批量删除房间
        
        @param tmp_req: BatchDeleteHotelRoomRequest
        @param headers: BatchDeleteHotelRoomHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteHotelRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.BatchDeleteHotelRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_no_list):
            request.room_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_no_list, 'RoomNoList', 'simple')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no_list_shrink):
            body['RoomNoList'] = request.room_no_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteHotelRoom',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/batchDeleteHotelRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.BatchDeleteHotelRoomResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_delete_hotel_room(
        self,
        request: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        """
        @summary 批量删除房间
        
        @param request: BatchDeleteHotelRoomRequest
        @return: BatchDeleteHotelRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders()
        return self.batch_delete_hotel_room_with_options(request, headers, runtime)

    async def batch_delete_hotel_room_async(
        self,
        request: ali_genieip__1__0_models.BatchDeleteHotelRoomRequest,
    ) -> ali_genieip__1__0_models.BatchDeleteHotelRoomResponse:
        """
        @summary 批量删除房间
        
        @param request: BatchDeleteHotelRoomRequest
        @return: BatchDeleteHotelRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.BatchDeleteHotelRoomHeaders()
        return await self.batch_delete_hotel_room_with_options_async(request, headers, runtime)

    def checkout_with_akwith_options(
        self,
        request: ali_genieip__1__0_models.CheckoutWithAKRequest,
        headers: ali_genieip__1__0_models.CheckoutWithAKHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CheckoutWithAKResponse:
        """
        @summary 酒店退房，清楚例如闹钟等定时信息
        
        @param request: CheckoutWithAKRequest
        @param headers: CheckoutWithAKHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckoutWithAKResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckoutWithAK',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/checkoutWithAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CheckoutWithAKResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CheckoutWithAKResponse(),
                self.execute(params, req, runtime)
            )

    async def checkout_with_akwith_options_async(
        self,
        request: ali_genieip__1__0_models.CheckoutWithAKRequest,
        headers: ali_genieip__1__0_models.CheckoutWithAKHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CheckoutWithAKResponse:
        """
        @summary 酒店退房，清楚例如闹钟等定时信息
        
        @param request: CheckoutWithAKRequest
        @param headers: CheckoutWithAKHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckoutWithAKResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckoutWithAK',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/checkoutWithAK',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CheckoutWithAKResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CheckoutWithAKResponse(),
                await self.execute_async(params, req, runtime)
            )

    def checkout_with_ak(
        self,
        request: ali_genieip__1__0_models.CheckoutWithAKRequest,
    ) -> ali_genieip__1__0_models.CheckoutWithAKResponse:
        """
        @summary 酒店退房，清楚例如闹钟等定时信息
        
        @param request: CheckoutWithAKRequest
        @return: CheckoutWithAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CheckoutWithAKHeaders()
        return self.checkout_with_akwith_options(request, headers, runtime)

    async def checkout_with_ak_async(
        self,
        request: ali_genieip__1__0_models.CheckoutWithAKRequest,
    ) -> ali_genieip__1__0_models.CheckoutWithAKResponse:
        """
        @summary 酒店退房，清楚例如闹钟等定时信息
        
        @param request: CheckoutWithAKRequest
        @return: CheckoutWithAKResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CheckoutWithAKHeaders()
        return await self.checkout_with_akwith_options_async(request, headers, runtime)

    def child_account_auth_with_options(
        self,
        request: ali_genieip__1__0_models.ChildAccountAuthRequest,
        headers: ali_genieip__1__0_models.ChildAccountAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ChildAccountAuthResponse:
        """
        @summary 子账号授权
        
        @param request: ChildAccountAuthRequest
        @param headers: ChildAccountAuthHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChildAccountAuthResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/childAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ChildAccountAuthResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ChildAccountAuthResponse(),
                self.execute(params, req, runtime)
            )

    async def child_account_auth_with_options_async(
        self,
        request: ali_genieip__1__0_models.ChildAccountAuthRequest,
        headers: ali_genieip__1__0_models.ChildAccountAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ChildAccountAuthResponse:
        """
        @summary 子账号授权
        
        @param request: ChildAccountAuthRequest
        @param headers: ChildAccountAuthHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChildAccountAuthResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/childAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ChildAccountAuthResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ChildAccountAuthResponse(),
                await self.execute_async(params, req, runtime)
            )

    def child_account_auth(
        self,
        request: ali_genieip__1__0_models.ChildAccountAuthRequest,
    ) -> ali_genieip__1__0_models.ChildAccountAuthResponse:
        """
        @summary 子账号授权
        
        @param request: ChildAccountAuthRequest
        @return: ChildAccountAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ChildAccountAuthHeaders()
        return self.child_account_auth_with_options(request, headers, runtime)

    async def child_account_auth_async(
        self,
        request: ali_genieip__1__0_models.ChildAccountAuthRequest,
    ) -> ali_genieip__1__0_models.ChildAccountAuthResponse:
        """
        @summary 子账号授权
        
        @param request: ChildAccountAuthRequest
        @return: ChildAccountAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ChildAccountAuthHeaders()
        return await self.child_account_auth_with_options_async(request, headers, runtime)

    def control_room_device_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ControlRoomDeviceRequest,
        headers: ali_genieip__1__0_models.ControlRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ControlRoomDeviceResponse:
        """
        @summary 控制房间内设备
        
        @param tmp_req: ControlRoomDeviceRequest
        @param headers: ControlRoomDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ControlRoomDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ControlRoomDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not UtilClient.is_unset(request.cmd):
            body['Cmd'] = request.cmd
        if not UtilClient.is_unset(request.device_index):
            body['DeviceIndex'] = request.device_index
        if not UtilClient.is_unset(request.device_number):
            body['DeviceNumber'] = request.device_number
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ControlRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/controlRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ControlRoomDeviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ControlRoomDeviceResponse(),
                self.execute(params, req, runtime)
            )

    async def control_room_device_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ControlRoomDeviceRequest,
        headers: ali_genieip__1__0_models.ControlRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ControlRoomDeviceResponse:
        """
        @summary 控制房间内设备
        
        @param tmp_req: ControlRoomDeviceRequest
        @param headers: ControlRoomDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ControlRoomDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ControlRoomDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.properties):
            request.properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.properties, 'Properties', 'json')
        body = {}
        if not UtilClient.is_unset(request.cmd):
            body['Cmd'] = request.cmd
        if not UtilClient.is_unset(request.device_index):
            body['DeviceIndex'] = request.device_index
        if not UtilClient.is_unset(request.device_number):
            body['DeviceNumber'] = request.device_number
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.properties_shrink):
            body['Properties'] = request.properties_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ControlRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/controlRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ControlRoomDeviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ControlRoomDeviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def control_room_device(
        self,
        request: ali_genieip__1__0_models.ControlRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.ControlRoomDeviceResponse:
        """
        @summary 控制房间内设备
        
        @param request: ControlRoomDeviceRequest
        @return: ControlRoomDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ControlRoomDeviceHeaders()
        return self.control_room_device_with_options(request, headers, runtime)

    async def control_room_device_async(
        self,
        request: ali_genieip__1__0_models.ControlRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.ControlRoomDeviceResponse:
        """
        @summary 控制房间内设备
        
        @param request: ControlRoomDeviceRequest
        @return: ControlRoomDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ControlRoomDeviceHeaders()
        return await self.control_room_device_with_options_async(request, headers, runtime)

    def create_hotel_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelRequest,
        headers: ali_genieip__1__0_models.CreateHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelResponse:
        """
        @summary 创建酒店项目
        
        @param tmp_req: CreateHotelRequest
        @param headers: CreateHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pk):
            body['RelatedPk'] = request.related_pk
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelResponse(),
                self.execute(params, req, runtime)
            )

    async def create_hotel_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelRequest,
        headers: ali_genieip__1__0_models.CreateHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelResponse:
        """
        @summary 创建酒店项目
        
        @param tmp_req: CreateHotelRequest
        @param headers: CreateHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pk):
            body['RelatedPk'] = request.related_pk
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_hotel(
        self,
        request: ali_genieip__1__0_models.CreateHotelRequest,
    ) -> ali_genieip__1__0_models.CreateHotelResponse:
        """
        @summary 创建酒店项目
        
        @param request: CreateHotelRequest
        @return: CreateHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelHeaders()
        return self.create_hotel_with_options(request, headers, runtime)

    async def create_hotel_async(
        self,
        request: ali_genieip__1__0_models.CreateHotelRequest,
    ) -> ali_genieip__1__0_models.CreateHotelResponse:
        """
        @summary 创建酒店项目
        
        @param request: CreateHotelRequest
        @return: CreateHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelHeaders()
        return await self.create_hotel_with_options_async(request, headers, runtime)

    def create_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.CreateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        """
        @summary 批量创建闹钟
        
        @param tmp_req: CreateHotelAlarmRequest
        @param headers: CreateHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_type):
            body['MusicType'] = request.music_type
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelAlarmResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelAlarmResponse(),
                self.execute(params, req, runtime)
            )

    async def create_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.CreateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.CreateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        """
        @summary 批量创建闹钟
        
        @param tmp_req: CreateHotelAlarmRequest
        @param headers: CreateHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.music_type):
            body['MusicType'] = request.music_type
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelAlarmResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateHotelAlarmResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.CreateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        """
        @summary 批量创建闹钟
        
        @param request: CreateHotelAlarmRequest
        @return: CreateHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelAlarmHeaders()
        return self.create_hotel_alarm_with_options(request, headers, runtime)

    async def create_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.CreateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.CreateHotelAlarmResponse:
        """
        @summary 批量创建闹钟
        
        @param request: CreateHotelAlarmRequest
        @return: CreateHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateHotelAlarmHeaders()
        return await self.create_hotel_alarm_with_options_async(request, headers, runtime)

    def create_rcu_scene_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.CreateRcuSceneRequest,
        headers: ali_genieip__1__0_models.CreateRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateRcuSceneResponse:
        """
        @summary 酒店rcu自定义场景创建
        
        @param tmp_req: CreateRcuSceneRequest
        @param headers: CreateRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRcuSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateRcuSceneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateRcuSceneResponse(),
                self.execute(params, req, runtime)
            )

    async def create_rcu_scene_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.CreateRcuSceneRequest,
        headers: ali_genieip__1__0_models.CreateRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.CreateRcuSceneResponse:
        """
        @summary 酒店rcu自定义场景创建
        
        @param tmp_req: CreateRcuSceneRequest
        @param headers: CreateRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRcuSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.CreateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/createRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateRcuSceneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.CreateRcuSceneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_rcu_scene(
        self,
        request: ali_genieip__1__0_models.CreateRcuSceneRequest,
    ) -> ali_genieip__1__0_models.CreateRcuSceneResponse:
        """
        @summary 酒店rcu自定义场景创建
        
        @param request: CreateRcuSceneRequest
        @return: CreateRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateRcuSceneHeaders()
        return self.create_rcu_scene_with_options(request, headers, runtime)

    async def create_rcu_scene_async(
        self,
        request: ali_genieip__1__0_models.CreateRcuSceneRequest,
    ) -> ali_genieip__1__0_models.CreateRcuSceneResponse:
        """
        @summary 酒店rcu自定义场景创建
        
        @param request: CreateRcuSceneRequest
        @return: CreateRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.CreateRcuSceneHeaders()
        return await self.create_rcu_scene_with_options_async(request, headers, runtime)

    def delete_cartoon_with_options(
        self,
        request: ali_genieip__1__0_models.DeleteCartoonRequest,
        headers: ali_genieip__1__0_models.DeleteCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteCartoonResponse:
        """
        @summary 删除动画
        
        @param request: DeleteCartoonRequest
        @param headers: DeleteCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCartoonResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCartoonResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_cartoon_with_options_async(
        self,
        request: ali_genieip__1__0_models.DeleteCartoonRequest,
        headers: ali_genieip__1__0_models.DeleteCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteCartoonResponse:
        """
        @summary 删除动画
        
        @param request: DeleteCartoonRequest
        @param headers: DeleteCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCartoonResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCartoonResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_cartoon(
        self,
        request: ali_genieip__1__0_models.DeleteCartoonRequest,
    ) -> ali_genieip__1__0_models.DeleteCartoonResponse:
        """
        @summary 删除动画
        
        @param request: DeleteCartoonRequest
        @return: DeleteCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCartoonHeaders()
        return self.delete_cartoon_with_options(request, headers, runtime)

    async def delete_cartoon_async(
        self,
        request: ali_genieip__1__0_models.DeleteCartoonRequest,
    ) -> ali_genieip__1__0_models.DeleteCartoonResponse:
        """
        @summary 删除动画
        
        @param request: DeleteCartoonRequest
        @return: DeleteCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCartoonHeaders()
        return await self.delete_cartoon_with_options_async(request, headers, runtime)

    def delete_custom_qawith_options(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteCustomQARequest,
        headers: ali_genieip__1__0_models.DeleteCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteCustomQAResponse:
        """
        @summary 删除自定义问答
        
        @param tmp_req: DeleteCustomQARequest
        @param headers: DeleteCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_qaids):
            request.custom_qaids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_qaids, 'CustomQAIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.custom_qaids_shrink):
            body['CustomQAIds'] = request.custom_qaids_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCustomQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCustomQAResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_custom_qawith_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteCustomQARequest,
        headers: ali_genieip__1__0_models.DeleteCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteCustomQAResponse:
        """
        @summary 删除自定义问答
        
        @param tmp_req: DeleteCustomQARequest
        @param headers: DeleteCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_qaids):
            request.custom_qaids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_qaids, 'CustomQAIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.custom_qaids_shrink):
            body['CustomQAIds'] = request.custom_qaids_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCustomQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteCustomQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_custom_qa(
        self,
        request: ali_genieip__1__0_models.DeleteCustomQARequest,
    ) -> ali_genieip__1__0_models.DeleteCustomQAResponse:
        """
        @summary 删除自定义问答
        
        @param request: DeleteCustomQARequest
        @return: DeleteCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCustomQAHeaders()
        return self.delete_custom_qawith_options(request, headers, runtime)

    async def delete_custom_qa_async(
        self,
        request: ali_genieip__1__0_models.DeleteCustomQARequest,
    ) -> ali_genieip__1__0_models.DeleteCustomQAResponse:
        """
        @summary 删除自定义问答
        
        @param request: DeleteCustomQARequest
        @return: DeleteCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteCustomQAHeaders()
        return await self.delete_custom_qawith_options_async(request, headers, runtime)

    def delete_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
        headers: ali_genieip__1__0_models.DeleteHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        """
        @summary 删除酒店闹钟
        
        @param tmp_req: DeleteHotelAlarmRequest
        @param headers: DeleteHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
        headers: ali_genieip__1__0_models.DeleteHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        """
        @summary 删除酒店闹钟
        
        @param tmp_req: DeleteHotelAlarmRequest
        @param headers: DeleteHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeleteHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelAlarmResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        """
        @summary 删除酒店闹钟
        
        @param request: DeleteHotelAlarmRequest
        @return: DeleteHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelAlarmHeaders()
        return self.delete_hotel_alarm_with_options(request, headers, runtime)

    async def delete_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelAlarmResponse:
        """
        @summary 删除酒店闹钟
        
        @param request: DeleteHotelAlarmRequest
        @return: DeleteHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelAlarmHeaders()
        return await self.delete_hotel_alarm_with_options_async(request, headers, runtime)

    def delete_hotel_scene_book_item_with_options(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.DeleteHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订删除
        
        @param request: DeleteHotelSceneBookItemRequest
        @param headers: DeleteHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelSceneBookItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_hotel_scene_book_item_with_options_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.DeleteHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订删除
        
        @param request: DeleteHotelSceneBookItemRequest
        @param headers: DeleteHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelSceneBookItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_hotel_scene_book_item(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订删除
        
        @param request: DeleteHotelSceneBookItemRequest
        @return: DeleteHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSceneBookItemHeaders()
        return self.delete_hotel_scene_book_item_with_options(request, headers, runtime)

    async def delete_hotel_scene_book_item_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订删除
        
        @param request: DeleteHotelSceneBookItemRequest
        @return: DeleteHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSceneBookItemHeaders()
        return await self.delete_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def delete_hotel_setting_with_options(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSettingRequest,
        headers: ali_genieip__1__0_models.DeleteHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelSettingResponse:
        """
        @summary 删除定制配置
        
        @param request: DeleteHotelSettingRequest
        @param headers: DeleteHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_hotel_setting_with_options_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSettingRequest,
        headers: ali_genieip__1__0_models.DeleteHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteHotelSettingResponse:
        """
        @summary 删除定制配置
        
        @param request: DeleteHotelSettingRequest
        @param headers: DeleteHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHotelSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteHotelSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_hotel_setting(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSettingRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelSettingResponse:
        """
        @summary 删除定制配置
        
        @param request: DeleteHotelSettingRequest
        @return: DeleteHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSettingHeaders()
        return self.delete_hotel_setting_with_options(request, headers, runtime)

    async def delete_hotel_setting_async(
        self,
        request: ali_genieip__1__0_models.DeleteHotelSettingRequest,
    ) -> ali_genieip__1__0_models.DeleteHotelSettingResponse:
        """
        @summary 删除定制配置
        
        @param request: DeleteHotelSettingRequest
        @return: DeleteHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteHotelSettingHeaders()
        return await self.delete_hotel_setting_with_options_async(request, headers, runtime)

    def delete_message_template_with_options(
        self,
        request: ali_genieip__1__0_models.DeleteMessageTemplateRequest,
        headers: ali_genieip__1__0_models.DeleteMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteMessageTemplateResponse:
        """
        @summary 删除消息通知模板
        
        @param request: DeleteMessageTemplateRequest
        @param headers: DeleteMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteMessageTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteMessageTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_message_template_with_options_async(
        self,
        request: ali_genieip__1__0_models.DeleteMessageTemplateRequest,
        headers: ali_genieip__1__0_models.DeleteMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteMessageTemplateResponse:
        """
        @summary 删除消息通知模板
        
        @param request: DeleteMessageTemplateRequest
        @param headers: DeleteMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteMessageTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteMessageTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_message_template(
        self,
        request: ali_genieip__1__0_models.DeleteMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.DeleteMessageTemplateResponse:
        """
        @summary 删除消息通知模板
        
        @param request: DeleteMessageTemplateRequest
        @return: DeleteMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteMessageTemplateHeaders()
        return self.delete_message_template_with_options(request, headers, runtime)

    async def delete_message_template_async(
        self,
        request: ali_genieip__1__0_models.DeleteMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.DeleteMessageTemplateResponse:
        """
        @summary 删除消息通知模板
        
        @param request: DeleteMessageTemplateRequest
        @return: DeleteMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteMessageTemplateHeaders()
        return await self.delete_message_template_with_options_async(request, headers, runtime)

    def delete_rcu_scene_with_options(
        self,
        request: ali_genieip__1__0_models.DeleteRcuSceneRequest,
        headers: ali_genieip__1__0_models.DeleteRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteRcuSceneResponse:
        """
        @summary 删除酒店自定义rcu场景
        
        @param request: DeleteRcuSceneRequest
        @param headers: DeleteRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRcuSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteRcuSceneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteRcuSceneResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_rcu_scene_with_options_async(
        self,
        request: ali_genieip__1__0_models.DeleteRcuSceneRequest,
        headers: ali_genieip__1__0_models.DeleteRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeleteRcuSceneResponse:
        """
        @summary 删除酒店自定义rcu场景
        
        @param request: DeleteRcuSceneRequest
        @param headers: DeleteRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRcuSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deleteRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteRcuSceneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeleteRcuSceneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_rcu_scene(
        self,
        request: ali_genieip__1__0_models.DeleteRcuSceneRequest,
    ) -> ali_genieip__1__0_models.DeleteRcuSceneResponse:
        """
        @summary 删除酒店自定义rcu场景
        
        @param request: DeleteRcuSceneRequest
        @return: DeleteRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteRcuSceneHeaders()
        return self.delete_rcu_scene_with_options(request, headers, runtime)

    async def delete_rcu_scene_async(
        self,
        request: ali_genieip__1__0_models.DeleteRcuSceneRequest,
    ) -> ali_genieip__1__0_models.DeleteRcuSceneResponse:
        """
        @summary 删除酒店自定义rcu场景
        
        @param request: DeleteRcuSceneRequest
        @return: DeleteRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeleteRcuSceneHeaders()
        return await self.delete_rcu_scene_with_options_async(request, headers, runtime)

    def device_control_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.DeviceControlRequest,
        headers: ali_genieip__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        """
        @summary 设备控制
        
        @param tmp_req: DeviceControlRequest
        @param headers: DeviceControlHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeviceControlResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deviceControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeviceControlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeviceControlResponse(),
                self.execute(params, req, runtime)
            )

    async def device_control_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.DeviceControlRequest,
        headers: ali_genieip__1__0_models.DeviceControlHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        """
        @summary 设备控制
        
        @param tmp_req: DeviceControlRequest
        @param headers: DeviceControlHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeviceControlResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.DeviceControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeviceControl',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/deviceControl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeviceControlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.DeviceControlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def device_control(
        self,
        request: ali_genieip__1__0_models.DeviceControlRequest,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        """
        @summary 设备控制
        
        @param request: DeviceControlRequest
        @return: DeviceControlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeviceControlHeaders()
        return self.device_control_with_options(request, headers, runtime)

    async def device_control_async(
        self,
        request: ali_genieip__1__0_models.DeviceControlRequest,
    ) -> ali_genieip__1__0_models.DeviceControlResponse:
        """
        @summary 设备控制
        
        @param request: DeviceControlRequest
        @return: DeviceControlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.DeviceControlHeaders()
        return await self.device_control_with_options_async(request, headers, runtime)

    def execute_scene_with_options(
        self,
        request: ali_genieip__1__0_models.ExecuteSceneRequest,
        headers: ali_genieip__1__0_models.ExecuteSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ExecuteSceneResponse:
        """
        @summary 控制房间场景
        
        @param request: ExecuteSceneRequest
        @param headers: ExecuteSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/executeScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ExecuteSceneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ExecuteSceneResponse(),
                self.execute(params, req, runtime)
            )

    async def execute_scene_with_options_async(
        self,
        request: ali_genieip__1__0_models.ExecuteSceneRequest,
        headers: ali_genieip__1__0_models.ExecuteSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ExecuteSceneResponse:
        """
        @summary 控制房间场景
        
        @param request: ExecuteSceneRequest
        @param headers: ExecuteSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/executeScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ExecuteSceneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ExecuteSceneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def execute_scene(
        self,
        request: ali_genieip__1__0_models.ExecuteSceneRequest,
    ) -> ali_genieip__1__0_models.ExecuteSceneResponse:
        """
        @summary 控制房间场景
        
        @param request: ExecuteSceneRequest
        @return: ExecuteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ExecuteSceneHeaders()
        return self.execute_scene_with_options(request, headers, runtime)

    async def execute_scene_async(
        self,
        request: ali_genieip__1__0_models.ExecuteSceneRequest,
    ) -> ali_genieip__1__0_models.ExecuteSceneResponse:
        """
        @summary 控制房间场景
        
        @param request: ExecuteSceneRequest
        @return: ExecuteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ExecuteSceneHeaders()
        return await self.execute_scene_with_options_async(request, headers, runtime)

    def get_basic_info_qawith_options(
        self,
        request: ali_genieip__1__0_models.GetBasicInfoQARequest,
        headers: ali_genieip__1__0_models.GetBasicInfoQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetBasicInfoQAResponse:
        """
        @summary 获取基础信息问答
        
        @param request: GetBasicInfoQARequest
        @param headers: GetBasicInfoQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBasicInfoQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetBasicInfoQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetBasicInfoQAResponse(),
                self.execute(params, req, runtime)
            )

    async def get_basic_info_qawith_options_async(
        self,
        request: ali_genieip__1__0_models.GetBasicInfoQARequest,
        headers: ali_genieip__1__0_models.GetBasicInfoQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetBasicInfoQAResponse:
        """
        @summary 获取基础信息问答
        
        @param request: GetBasicInfoQARequest
        @param headers: GetBasicInfoQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBasicInfoQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetBasicInfoQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetBasicInfoQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_basic_info_qa(
        self,
        request: ali_genieip__1__0_models.GetBasicInfoQARequest,
    ) -> ali_genieip__1__0_models.GetBasicInfoQAResponse:
        """
        @summary 获取基础信息问答
        
        @param request: GetBasicInfoQARequest
        @return: GetBasicInfoQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetBasicInfoQAHeaders()
        return self.get_basic_info_qawith_options(request, headers, runtime)

    async def get_basic_info_qa_async(
        self,
        request: ali_genieip__1__0_models.GetBasicInfoQARequest,
    ) -> ali_genieip__1__0_models.GetBasicInfoQAResponse:
        """
        @summary 获取基础信息问答
        
        @param request: GetBasicInfoQARequest
        @return: GetBasicInfoQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetBasicInfoQAHeaders()
        return await self.get_basic_info_qawith_options_async(request, headers, runtime)

    def get_cartoon_with_options(
        self,
        request: ali_genieip__1__0_models.GetCartoonRequest,
        headers: ali_genieip__1__0_models.GetCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetCartoonResponse:
        """
        @summary 查询动画
        
        @param request: GetCartoonRequest
        @param headers: GetCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetCartoonResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetCartoonResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cartoon_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetCartoonRequest,
        headers: ali_genieip__1__0_models.GetCartoonHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetCartoonResponse:
        """
        @summary 查询动画
        
        @param request: GetCartoonRequest
        @param headers: GetCartoonHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCartoonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCartoon',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getCartoon',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetCartoonResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetCartoonResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cartoon(
        self,
        request: ali_genieip__1__0_models.GetCartoonRequest,
    ) -> ali_genieip__1__0_models.GetCartoonResponse:
        """
        @summary 查询动画
        
        @param request: GetCartoonRequest
        @return: GetCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetCartoonHeaders()
        return self.get_cartoon_with_options(request, headers, runtime)

    async def get_cartoon_async(
        self,
        request: ali_genieip__1__0_models.GetCartoonRequest,
    ) -> ali_genieip__1__0_models.GetCartoonResponse:
        """
        @summary 查询动画
        
        @param request: GetCartoonRequest
        @return: GetCartoonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetCartoonHeaders()
        return await self.get_cartoon_with_options_async(request, headers, runtime)

    def get_hotel_contact_by_genie_device_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactByGenieDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelContactByGenieDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse:
        """
        @summary 获取当前设备的通话信息
        
        @param tmp_req: GetHotelContactByGenieDeviceRequest
        @param headers: GetHotelContactByGenieDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactByGenieDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByGenieDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelContactByGenieDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContactByGenieDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_contact_by_genie_device_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactByGenieDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelContactByGenieDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse:
        """
        @summary 获取当前设备的通话信息
        
        @param tmp_req: GetHotelContactByGenieDeviceRequest
        @param headers: GetHotelContactByGenieDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactByGenieDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByGenieDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelContactByGenieDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContactByGenieDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_contact_by_genie_device(
        self,
        request: ali_genieip__1__0_models.GetHotelContactByGenieDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse:
        """
        @summary 获取当前设备的通话信息
        
        @param request: GetHotelContactByGenieDeviceRequest
        @return: GetHotelContactByGenieDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByGenieDeviceHeaders()
        return self.get_hotel_contact_by_genie_device_with_options(request, headers, runtime)

    async def get_hotel_contact_by_genie_device_async(
        self,
        request: ali_genieip__1__0_models.GetHotelContactByGenieDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactByGenieDeviceResponse:
        """
        @summary 获取当前设备的通话信息
        
        @param request: GetHotelContactByGenieDeviceRequest
        @return: GetHotelContactByGenieDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByGenieDeviceHeaders()
        return await self.get_hotel_contact_by_genie_device_with_options_async(request, headers, runtime)

    def get_hotel_contact_by_number_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactByNumberRequest,
        headers: ali_genieip__1__0_models.GetHotelContactByNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactByNumberResponse:
        """
        @summary 根据号码获取酒店联系人
        
        @param tmp_req: GetHotelContactByNumberRequest
        @param headers: GetHotelContactByNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactByNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelContactByNumber',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContactByNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByNumberResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByNumberResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_contact_by_number_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactByNumberRequest,
        headers: ali_genieip__1__0_models.GetHotelContactByNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactByNumberResponse:
        """
        @summary 根据号码获取酒店联系人
        
        @param tmp_req: GetHotelContactByNumberRequest
        @param headers: GetHotelContactByNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactByNumberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactByNumberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        body = {}
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelContactByNumber',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContactByNumber',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByNumberResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactByNumberResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_contact_by_number(
        self,
        request: ali_genieip__1__0_models.GetHotelContactByNumberRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactByNumberResponse:
        """
        @summary 根据号码获取酒店联系人
        
        @param request: GetHotelContactByNumberRequest
        @return: GetHotelContactByNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByNumberHeaders()
        return self.get_hotel_contact_by_number_with_options(request, headers, runtime)

    async def get_hotel_contact_by_number_async(
        self,
        request: ali_genieip__1__0_models.GetHotelContactByNumberRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactByNumberResponse:
        """
        @summary 根据号码获取酒店联系人
        
        @param request: GetHotelContactByNumberRequest
        @return: GetHotelContactByNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactByNumberHeaders()
        return await self.get_hotel_contact_by_number_with_options_async(request, headers, runtime)

    def get_hotel_contacts_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactsRequest,
        headers: ali_genieip__1__0_models.GetHotelContactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactsResponse:
        """
        @summary 获取酒店联系人
        
        @param tmp_req: GetHotelContactsRequest
        @param headers: GetHotelContactsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelContacts',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_contacts_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelContactsRequest,
        headers: ali_genieip__1__0_models.GetHotelContactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelContactsResponse:
        """
        @summary 获取酒店联系人
        
        @param tmp_req: GetHotelContactsRequest
        @param headers: GetHotelContactsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelContactsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelContactsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelContacts',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelContacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelContactsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_contacts(
        self,
        request: ali_genieip__1__0_models.GetHotelContactsRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactsResponse:
        """
        @summary 获取酒店联系人
        
        @param request: GetHotelContactsRequest
        @return: GetHotelContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactsHeaders()
        return self.get_hotel_contacts_with_options(request, headers, runtime)

    async def get_hotel_contacts_async(
        self,
        request: ali_genieip__1__0_models.GetHotelContactsRequest,
    ) -> ali_genieip__1__0_models.GetHotelContactsResponse:
        """
        @summary 获取酒店联系人
        
        @param request: GetHotelContactsRequest
        @return: GetHotelContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelContactsHeaders()
        return await self.get_hotel_contacts_with_options_async(request, headers, runtime)

    def get_hotel_home_back_image_and_modes_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
        headers: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        """
        @summary 获取首页背景图和场景模式
        
        @param tmp_req: GetHotelHomeBackImageAndModesRequest
        @param headers: GetHotelHomeBackImageAndModesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelHomeBackImageAndModesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelHomeBackImageAndModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_home_back_image_and_modes_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
        headers: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        """
        @summary 获取首页背景图和场景模式
        
        @param tmp_req: GetHotelHomeBackImageAndModesRequest
        @param headers: GetHotelHomeBackImageAndModesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelHomeBackImageAndModesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelHomeBackImageAndModes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelHomeBackImageAndModes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_home_back_image_and_modes(
        self,
        request: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        """
        @summary 获取首页背景图和场景模式
        
        @param request: GetHotelHomeBackImageAndModesRequest
        @return: GetHotelHomeBackImageAndModesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders()
        return self.get_hotel_home_back_image_and_modes_with_options(request, headers, runtime)

    async def get_hotel_home_back_image_and_modes_async(
        self,
        request: ali_genieip__1__0_models.GetHotelHomeBackImageAndModesRequest,
    ) -> ali_genieip__1__0_models.GetHotelHomeBackImageAndModesResponse:
        """
        @summary 获取首页背景图和场景模式
        
        @param request: GetHotelHomeBackImageAndModesRequest
        @return: GetHotelHomeBackImageAndModesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelHomeBackImageAndModesHeaders()
        return await self.get_hotel_home_back_image_and_modes_with_options_async(request, headers, runtime)

    def get_hotel_notice_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeRequest,
        headers: ali_genieip__1__0_models.GetHotelNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        """
        @summary 获取酒店通知
        
        @param tmp_req: GetHotelNoticeRequest
        @param headers: GetHotelNoticeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelNoticeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelNotice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_notice_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeRequest,
        headers: ali_genieip__1__0_models.GetHotelNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        """
        @summary 获取酒店通知
        
        @param tmp_req: GetHotelNoticeRequest
        @param headers: GetHotelNoticeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelNoticeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelNotice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_notice(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeRequest,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        """
        @summary 获取酒店通知
        
        @param request: GetHotelNoticeRequest
        @return: GetHotelNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeHeaders()
        return self.get_hotel_notice_with_options(request, headers, runtime)

    async def get_hotel_notice_async(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeRequest,
    ) -> ali_genieip__1__0_models.GetHotelNoticeResponse:
        """
        @summary 获取酒店通知
        
        @param request: GetHotelNoticeRequest
        @return: GetHotelNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeHeaders()
        return await self.get_hotel_notice_with_options_async(request, headers, runtime)

    def get_hotel_notice_v2with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeV2Request,
        headers: ali_genieip__1__0_models.GetHotelNoticeV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeV2Response:
        """
        @summary 获取酒店通知
        
        @param tmp_req: GetHotelNoticeV2Request
        @param headers: GetHotelNoticeV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelNoticeV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelNoticeV2',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNoticeV2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeV2Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeV2Response(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_notice_v2with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelNoticeV2Request,
        headers: ali_genieip__1__0_models.GetHotelNoticeV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelNoticeV2Response:
        """
        @summary 获取酒店通知
        
        @param tmp_req: GetHotelNoticeV2Request
        @param headers: GetHotelNoticeV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelNoticeV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelNoticeV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelNoticeV2',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelNoticeV2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeV2Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelNoticeV2Response(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_notice_v2(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeV2Request,
    ) -> ali_genieip__1__0_models.GetHotelNoticeV2Response:
        """
        @summary 获取酒店通知
        
        @param request: GetHotelNoticeV2Request
        @return: GetHotelNoticeV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeV2Headers()
        return self.get_hotel_notice_v2with_options(request, headers, runtime)

    async def get_hotel_notice_v2_async(
        self,
        request: ali_genieip__1__0_models.GetHotelNoticeV2Request,
    ) -> ali_genieip__1__0_models.GetHotelNoticeV2Response:
        """
        @summary 获取酒店通知
        
        @param request: GetHotelNoticeV2Request
        @return: GetHotelNoticeV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelNoticeV2Headers()
        return await self.get_hotel_notice_v2with_options_async(request, headers, runtime)

    def get_hotel_order_detail_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelOrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        """
        @summary 获取酒店订单详情
        
        @param tmp_req: GetHotelOrderDetailRequest
        @param headers: GetHotelOrderDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelOrderDetailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelOrderDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelOrderDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelOrderDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_order_detail_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelOrderDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        """
        @summary 获取酒店订单详情
        
        @param tmp_req: GetHotelOrderDetailRequest
        @param headers: GetHotelOrderDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelOrderDetailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelOrderDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelOrderDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelOrderDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelOrderDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_order_detail(
        self,
        request: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        """
        @summary 获取酒店订单详情
        
        @param request: GetHotelOrderDetailRequest
        @return: GetHotelOrderDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelOrderDetailHeaders()
        return self.get_hotel_order_detail_with_options(request, headers, runtime)

    async def get_hotel_order_detail_async(
        self,
        request: ali_genieip__1__0_models.GetHotelOrderDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelOrderDetailResponse:
        """
        @summary 获取酒店订单详情
        
        @param request: GetHotelOrderDetailRequest
        @return: GetHotelOrderDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelOrderDetailHeaders()
        return await self.get_hotel_order_detail_with_options_async(request, headers, runtime)

    def get_hotel_room_device_with_options(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        """
        @summary 获取酒店房间猫精设备信息
        
        @param request: GetHotelRoomDeviceRequest
        @param headers: GetHotelRoomDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelRoomDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_room_device_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
        headers: ali_genieip__1__0_models.GetHotelRoomDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        """
        @summary 获取酒店房间猫精设备信息
        
        @param request: GetHotelRoomDeviceRequest
        @param headers: GetHotelRoomDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelRoomDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelRoomDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelRoomDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelRoomDeviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_room_device(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        """
        @summary 获取酒店房间猫精设备信息
        
        @param request: GetHotelRoomDeviceRequest
        @return: GetHotelRoomDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelRoomDeviceHeaders()
        return self.get_hotel_room_device_with_options(request, headers, runtime)

    async def get_hotel_room_device_async(
        self,
        request: ali_genieip__1__0_models.GetHotelRoomDeviceRequest,
    ) -> ali_genieip__1__0_models.GetHotelRoomDeviceResponse:
        """
        @summary 获取酒店房间猫精设备信息
        
        @param request: GetHotelRoomDeviceRequest
        @return: GetHotelRoomDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelRoomDeviceHeaders()
        return await self.get_hotel_room_device_with_options_async(request, headers, runtime)

    def get_hotel_sample_utterances_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
        headers: ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        """
        @summary 获取推荐语料
        
        @param tmp_req: GetHotelSampleUtterancesRequest
        @param headers: GetHotelSampleUtterancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSampleUtterancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelSampleUtterancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelSampleUtterances',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSampleUtterances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_sample_utterances_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
        headers: ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        """
        @summary 获取推荐语料
        
        @param tmp_req: GetHotelSampleUtterancesRequest
        @param headers: GetHotelSampleUtterancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSampleUtterancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelSampleUtterancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelSampleUtterances',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSampleUtterances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSampleUtterancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_sample_utterances(
        self,
        request: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        """
        @summary 获取推荐语料
        
        @param request: GetHotelSampleUtterancesRequest
        @return: GetHotelSampleUtterancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders()
        return self.get_hotel_sample_utterances_with_options(request, headers, runtime)

    async def get_hotel_sample_utterances_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSampleUtterancesRequest,
    ) -> ali_genieip__1__0_models.GetHotelSampleUtterancesResponse:
        """
        @summary 获取推荐语料
        
        @param request: GetHotelSampleUtterancesRequest
        @return: GetHotelSampleUtterancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSampleUtterancesHeaders()
        return await self.get_hotel_sample_utterances_with_options_async(request, headers, runtime)

    def get_hotel_scene_item_detail_with_options(
        self,
        request: ali_genieip__1__0_models.GetHotelSceneItemDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelSceneItemDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSceneItemDetailResponse:
        """
        @summary 酒店场景详情
        
        @param request: GetHotelSceneItemDetailRequest
        @param headers: GetHotelSceneItemDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSceneItemDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelSceneItemDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSceneItemDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSceneItemDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSceneItemDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_scene_item_detail_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSceneItemDetailRequest,
        headers: ali_genieip__1__0_models.GetHotelSceneItemDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSceneItemDetailResponse:
        """
        @summary 酒店场景详情
        
        @param request: GetHotelSceneItemDetailRequest
        @param headers: GetHotelSceneItemDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSceneItemDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelSceneItemDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSceneItemDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSceneItemDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSceneItemDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_scene_item_detail(
        self,
        request: ali_genieip__1__0_models.GetHotelSceneItemDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelSceneItemDetailResponse:
        """
        @summary 酒店场景详情
        
        @param request: GetHotelSceneItemDetailRequest
        @return: GetHotelSceneItemDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSceneItemDetailHeaders()
        return self.get_hotel_scene_item_detail_with_options(request, headers, runtime)

    async def get_hotel_scene_item_detail_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSceneItemDetailRequest,
    ) -> ali_genieip__1__0_models.GetHotelSceneItemDetailResponse:
        """
        @summary 酒店场景详情
        
        @param request: GetHotelSceneItemDetailRequest
        @return: GetHotelSceneItemDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSceneItemDetailHeaders()
        return await self.get_hotel_scene_item_detail_with_options_async(request, headers, runtime)

    def get_hotel_screen_saver_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        """
        @summary 获取酒店屏保
        
        @param tmp_req: GetHotelScreenSaverRequest
        @param headers: GetHotelScreenSaverHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelScreenSaverResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_screen_saver_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        """
        @summary 获取酒店屏保
        
        @param tmp_req: GetHotelScreenSaverRequest
        @param headers: GetHotelScreenSaverHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelScreenSaverResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.GetHotelScreenSaverShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaver',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_screen_saver(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        """
        @summary 获取酒店屏保
        
        @param request: GetHotelScreenSaverRequest
        @return: GetHotelScreenSaverResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverHeaders()
        return self.get_hotel_screen_saver_with_options(request, headers, runtime)

    async def get_hotel_screen_saver_async(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverResponse:
        """
        @summary 获取酒店屏保
        
        @param request: GetHotelScreenSaverRequest
        @return: GetHotelScreenSaverResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverHeaders()
        return await self.get_hotel_screen_saver_with_options_async(request, headers, runtime)

    def get_hotel_screen_saver_style_with_options(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverStyleRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverStyleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse:
        """
        @summary 获取屏保列表
        
        @param request: GetHotelScreenSaverStyleRequest
        @param headers: GetHotelScreenSaverStyleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelScreenSaverStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaverStyle',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaverStyle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_screen_saver_style_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverStyleRequest,
        headers: ali_genieip__1__0_models.GetHotelScreenSaverStyleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse:
        """
        @summary 获取屏保列表
        
        @param request: GetHotelScreenSaverStyleRequest
        @param headers: GetHotelScreenSaverStyleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelScreenSaverStyleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelScreenSaverStyle',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelScreenSaverStyle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_screen_saver_style(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverStyleRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse:
        """
        @summary 获取屏保列表
        
        @param request: GetHotelScreenSaverStyleRequest
        @return: GetHotelScreenSaverStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverStyleHeaders()
        return self.get_hotel_screen_saver_style_with_options(request, headers, runtime)

    async def get_hotel_screen_saver_style_async(
        self,
        request: ali_genieip__1__0_models.GetHotelScreenSaverStyleRequest,
    ) -> ali_genieip__1__0_models.GetHotelScreenSaverStyleResponse:
        """
        @summary 获取屏保列表
        
        @param request: GetHotelScreenSaverStyleRequest
        @return: GetHotelScreenSaverStyleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelScreenSaverStyleHeaders()
        return await self.get_hotel_screen_saver_style_with_options_async(request, headers, runtime)

    def get_hotel_setting_with_options(
        self,
        request: ali_genieip__1__0_models.GetHotelSettingRequest,
        headers: ali_genieip__1__0_models.GetHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSettingResponse:
        """
        @summary 查询定制配置
        
        @param request: GetHotelSettingRequest
        @param headers: GetHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hotel_setting_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSettingRequest,
        headers: ali_genieip__1__0_models.GetHotelSettingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetHotelSettingResponse:
        """
        @summary 查询定制配置
        
        @param request: GetHotelSettingRequest
        @param headers: GetHotelSettingHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotelSettingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.setting_type):
            body['SettingType'] = request.setting_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotelSetting',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelSetting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetHotelSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hotel_setting(
        self,
        request: ali_genieip__1__0_models.GetHotelSettingRequest,
    ) -> ali_genieip__1__0_models.GetHotelSettingResponse:
        """
        @summary 查询定制配置
        
        @param request: GetHotelSettingRequest
        @return: GetHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSettingHeaders()
        return self.get_hotel_setting_with_options(request, headers, runtime)

    async def get_hotel_setting_async(
        self,
        request: ali_genieip__1__0_models.GetHotelSettingRequest,
    ) -> ali_genieip__1__0_models.GetHotelSettingResponse:
        """
        @summary 查询定制配置
        
        @param request: GetHotelSettingRequest
        @return: GetHotelSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetHotelSettingHeaders()
        return await self.get_hotel_setting_with_options_async(request, headers, runtime)

    def get_relation_product_list_with_options(
        self,
        headers: ali_genieip__1__0_models.GetRelationProductListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetRelationProductListResponse:
        """
        @summary 关联产品列表查看
        
        @param headers: GetRelationProductListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRelationProductListResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetRelationProductList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getRelationProductList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetRelationProductListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetRelationProductListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_relation_product_list_with_options_async(
        self,
        headers: ali_genieip__1__0_models.GetRelationProductListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetRelationProductListResponse:
        """
        @summary 关联产品列表查看
        
        @param headers: GetRelationProductListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRelationProductListResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetRelationProductList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getRelationProductList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetRelationProductListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetRelationProductListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_relation_product_list(self) -> ali_genieip__1__0_models.GetRelationProductListResponse:
        """
        @summary 关联产品列表查看
        
        @return: GetRelationProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetRelationProductListHeaders()
        return self.get_relation_product_list_with_options(headers, runtime)

    async def get_relation_product_list_async(self) -> ali_genieip__1__0_models.GetRelationProductListResponse:
        """
        @summary 关联产品列表查看
        
        @return: GetRelationProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetRelationProductListHeaders()
        return await self.get_relation_product_list_with_options_async(headers, runtime)

    def get_union_id_with_options(
        self,
        request: ali_genieip__1__0_models.GetUnionIdRequest,
        headers: ali_genieip__1__0_models.GetUnionIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetUnionIdResponse:
        """
        @summary 获取组织下unionId列表
        
        @param request: GetUnionIdRequest
        @param headers: GetUnionIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUnionIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.id_type):
            body['IdType'] = request.id_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUnionId',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getUnionId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetUnionIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetUnionIdResponse(),
                self.execute(params, req, runtime)
            )

    async def get_union_id_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetUnionIdRequest,
        headers: ali_genieip__1__0_models.GetUnionIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetUnionIdResponse:
        """
        @summary 获取组织下unionId列表
        
        @param request: GetUnionIdRequest
        @param headers: GetUnionIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUnionIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encode_key):
            body['EncodeKey'] = request.encode_key
        if not UtilClient.is_unset(request.encode_type):
            body['EncodeType'] = request.encode_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.id_type):
            body['IdType'] = request.id_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUnionId',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getUnionId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetUnionIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetUnionIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_union_id(
        self,
        request: ali_genieip__1__0_models.GetUnionIdRequest,
    ) -> ali_genieip__1__0_models.GetUnionIdResponse:
        """
        @summary 获取组织下unionId列表
        
        @param request: GetUnionIdRequest
        @return: GetUnionIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetUnionIdHeaders()
        return self.get_union_id_with_options(request, headers, runtime)

    async def get_union_id_async(
        self,
        request: ali_genieip__1__0_models.GetUnionIdRequest,
    ) -> ali_genieip__1__0_models.GetUnionIdResponse:
        """
        @summary 获取组织下unionId列表
        
        @param request: GetUnionIdRequest
        @return: GetUnionIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetUnionIdHeaders()
        return await self.get_union_id_with_options_async(request, headers, runtime)

    def get_welcome_text_and_music_with_options(
        self,
        request: ali_genieip__1__0_models.GetWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.GetWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse:
        """
        @summary 查询欢迎语信息
        
        @param request: GetWelcomeTextAndMusicRequest
        @param headers: GetWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse(),
                self.execute(params, req, runtime)
            )

    async def get_welcome_text_and_music_with_options_async(
        self,
        request: ali_genieip__1__0_models.GetWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.GetWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse:
        """
        @summary 查询欢迎语信息
        
        @param request: GetWelcomeTextAndMusicRequest
        @param headers: GetWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_welcome_text_and_music(
        self,
        request: ali_genieip__1__0_models.GetWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse:
        """
        @summary 查询欢迎语信息
        
        @param request: GetWelcomeTextAndMusicRequest
        @return: GetWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetWelcomeTextAndMusicHeaders()
        return self.get_welcome_text_and_music_with_options(request, headers, runtime)

    async def get_welcome_text_and_music_async(
        self,
        request: ali_genieip__1__0_models.GetWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.GetWelcomeTextAndMusicResponse:
        """
        @summary 查询欢迎语信息
        
        @param request: GetWelcomeTextAndMusicRequest
        @return: GetWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.GetWelcomeTextAndMusicHeaders()
        return await self.get_welcome_text_and_music_with_options_async(request, headers, runtime)

    def hotel_qr_bind_with_options(
        self,
        request: ali_genieip__1__0_models.HotelQrBindRequest,
        headers: ali_genieip__1__0_models.HotelQrBindHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.HotelQrBindResponse:
        """
        @summary 酒店带屏设备扫码绑定
        
        @param request: HotelQrBindRequest
        @param headers: HotelQrBindHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotelQrBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelQrBind',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/hotelQrBind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.HotelQrBindResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.HotelQrBindResponse(),
                self.execute(params, req, runtime)
            )

    async def hotel_qr_bind_with_options_async(
        self,
        request: ali_genieip__1__0_models.HotelQrBindRequest,
        headers: ali_genieip__1__0_models.HotelQrBindHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.HotelQrBindResponse:
        """
        @summary 酒店带屏设备扫码绑定
        
        @param request: HotelQrBindRequest
        @param headers: HotelQrBindHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotelQrBindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HotelQrBind',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/hotelQrBind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.HotelQrBindResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.HotelQrBindResponse(),
                await self.execute_async(params, req, runtime)
            )

    def hotel_qr_bind(
        self,
        request: ali_genieip__1__0_models.HotelQrBindRequest,
    ) -> ali_genieip__1__0_models.HotelQrBindResponse:
        """
        @summary 酒店带屏设备扫码绑定
        
        @param request: HotelQrBindRequest
        @return: HotelQrBindResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.HotelQrBindHeaders()
        return self.hotel_qr_bind_with_options(request, headers, runtime)

    async def hotel_qr_bind_async(
        self,
        request: ali_genieip__1__0_models.HotelQrBindRequest,
    ) -> ali_genieip__1__0_models.HotelQrBindResponse:
        """
        @summary 酒店带屏设备扫码绑定
        
        @param request: HotelQrBindRequest
        @return: HotelQrBindResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.HotelQrBindHeaders()
        return await self.hotel_qr_bind_with_options_async(request, headers, runtime)

    def import_hotel_config_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ImportHotelConfigRequest,
        headers: ali_genieip__1__0_models.ImportHotelConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportHotelConfigResponse:
        """
        @summary 批量导入酒店配置
        
        @param tmp_req: ImportHotelConfigRequest
        @param headers: ImportHotelConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportHotelConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportHotelConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_hotel_config):
            request.import_hotel_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_hotel_config, 'ImportHotelConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.import_hotel_config_shrink):
            body['ImportHotelConfig'] = request.import_hotel_config_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportHotelConfig',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importHotelConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportHotelConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportHotelConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def import_hotel_config_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ImportHotelConfigRequest,
        headers: ali_genieip__1__0_models.ImportHotelConfigHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportHotelConfigResponse:
        """
        @summary 批量导入酒店配置
        
        @param tmp_req: ImportHotelConfigRequest
        @param headers: ImportHotelConfigHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportHotelConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportHotelConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_hotel_config):
            request.import_hotel_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_hotel_config, 'ImportHotelConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.import_hotel_config_shrink):
            body['ImportHotelConfig'] = request.import_hotel_config_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportHotelConfig',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importHotelConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportHotelConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportHotelConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def import_hotel_config(
        self,
        request: ali_genieip__1__0_models.ImportHotelConfigRequest,
    ) -> ali_genieip__1__0_models.ImportHotelConfigResponse:
        """
        @summary 批量导入酒店配置
        
        @param request: ImportHotelConfigRequest
        @return: ImportHotelConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportHotelConfigHeaders()
        return self.import_hotel_config_with_options(request, headers, runtime)

    async def import_hotel_config_async(
        self,
        request: ali_genieip__1__0_models.ImportHotelConfigRequest,
    ) -> ali_genieip__1__0_models.ImportHotelConfigResponse:
        """
        @summary 批量导入酒店配置
        
        @param request: ImportHotelConfigRequest
        @return: ImportHotelConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportHotelConfigHeaders()
        return await self.import_hotel_config_with_options_async(request, headers, runtime)

    def import_room_control_devices_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.ImportRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        """
        @summary 批量导入设备（同时补充房型）
        
        @param tmp_req: ImportRoomControlDevicesRequest
        @param headers: ImportRoomControlDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportRoomControlDevicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomControlDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.location_devices):
            request.location_devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_infrared_device_import):
            body['EnableInfraredDeviceImport'] = request.enable_infrared_device_import
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
                self.execute(params, req, runtime)
            )

    async def import_room_control_devices_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.ImportRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        """
        @summary 批量导入设备（同时补充房型）
        
        @param tmp_req: ImportRoomControlDevicesRequest
        @param headers: ImportRoomControlDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportRoomControlDevicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomControlDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.location_devices):
            request.location_devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_devices, 'LocationDevices', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_infrared_device_import):
            body['EnableInfraredDeviceImport'] = request.enable_infrared_device_import
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location_devices_shrink):
            body['LocationDevices'] = request.location_devices_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomControlDevicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def import_room_control_devices(
        self,
        request: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        """
        @summary 批量导入设备（同时补充房型）
        
        @param request: ImportRoomControlDevicesRequest
        @return: ImportRoomControlDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomControlDevicesHeaders()
        return self.import_room_control_devices_with_options(request, headers, runtime)

    async def import_room_control_devices_async(
        self,
        request: ali_genieip__1__0_models.ImportRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomControlDevicesResponse:
        """
        @summary 批量导入设备（同时补充房型）
        
        @param request: ImportRoomControlDevicesRequest
        @return: ImportRoomControlDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomControlDevicesHeaders()
        return await self.import_room_control_devices_with_options_async(request, headers, runtime)

    def import_room_genie_scenes_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomGenieScenesRequest,
        headers: ali_genieip__1__0_models.ImportRoomGenieScenesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomGenieScenesResponse:
        """
        @summary 导入房间内精灵场景
        
        @param tmp_req: ImportRoomGenieScenesRequest
        @param headers: ImportRoomGenieScenesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportRoomGenieScenesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomGenieScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_list):
            request.scene_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_list, 'SceneList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.scene_list_shrink):
            body['SceneList'] = request.scene_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomGenieScenes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomGenieScenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomGenieScenesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomGenieScenesResponse(),
                self.execute(params, req, runtime)
            )

    async def import_room_genie_scenes_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ImportRoomGenieScenesRequest,
        headers: ali_genieip__1__0_models.ImportRoomGenieScenesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ImportRoomGenieScenesResponse:
        """
        @summary 导入房间内精灵场景
        
        @param tmp_req: ImportRoomGenieScenesRequest
        @param headers: ImportRoomGenieScenesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportRoomGenieScenesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ImportRoomGenieScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_list):
            request.scene_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_list, 'SceneList', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.scene_list_shrink):
            body['SceneList'] = request.scene_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportRoomGenieScenes',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/importRoomGenieScenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomGenieScenesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ImportRoomGenieScenesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def import_room_genie_scenes(
        self,
        request: ali_genieip__1__0_models.ImportRoomGenieScenesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomGenieScenesResponse:
        """
        @summary 导入房间内精灵场景
        
        @param request: ImportRoomGenieScenesRequest
        @return: ImportRoomGenieScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomGenieScenesHeaders()
        return self.import_room_genie_scenes_with_options(request, headers, runtime)

    async def import_room_genie_scenes_async(
        self,
        request: ali_genieip__1__0_models.ImportRoomGenieScenesRequest,
    ) -> ali_genieip__1__0_models.ImportRoomGenieScenesResponse:
        """
        @summary 导入房间内精灵场景
        
        @param request: ImportRoomGenieScenesRequest
        @return: ImportRoomGenieScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ImportRoomGenieScenesHeaders()
        return await self.import_room_genie_scenes_with_options_async(request, headers, runtime)

    def insert_hotel_scene_book_item_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.InsertHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.InsertHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.InsertHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订新增
        
        @param tmp_req: InsertHotelSceneBookItemRequest
        @param headers: InsertHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertHotelSceneBookItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.InsertHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_hotel_scene_item_req):
            request.add_hotel_scene_item_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_hotel_scene_item_req, 'AddHotelSceneItemReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_hotel_scene_item_req_shrink):
            query['AddHotelSceneItemReq'] = request.add_hotel_scene_item_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/insertHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.InsertHotelSceneBookItemResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.InsertHotelSceneBookItemResponse(),
                self.execute(params, req, runtime)
            )

    async def insert_hotel_scene_book_item_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.InsertHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.InsertHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.InsertHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订新增
        
        @param tmp_req: InsertHotelSceneBookItemRequest
        @param headers: InsertHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertHotelSceneBookItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.InsertHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_hotel_scene_item_req):
            request.add_hotel_scene_item_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_hotel_scene_item_req, 'AddHotelSceneItemReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.add_hotel_scene_item_req_shrink):
            query['AddHotelSceneItemReq'] = request.add_hotel_scene_item_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/insertHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.InsertHotelSceneBookItemResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.InsertHotelSceneBookItemResponse(),
                await self.execute_async(params, req, runtime)
            )

    def insert_hotel_scene_book_item(
        self,
        request: ali_genieip__1__0_models.InsertHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.InsertHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订新增
        
        @param request: InsertHotelSceneBookItemRequest
        @return: InsertHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InsertHotelSceneBookItemHeaders()
        return self.insert_hotel_scene_book_item_with_options(request, headers, runtime)

    async def insert_hotel_scene_book_item_async(
        self,
        request: ali_genieip__1__0_models.InsertHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.InsertHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订新增
        
        @param request: InsertHotelSceneBookItemRequest
        @return: InsertHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InsertHotelSceneBookItemHeaders()
        return await self.insert_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def invoke_robot_push_with_options(
        self,
        request: ali_genieip__1__0_models.InvokeRobotPushRequest,
        headers: ali_genieip__1__0_models.InvokeRobotPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.InvokeRobotPushResponse:
        """
        @summary 机器人服务，消息推送
        
        @param request: InvokeRobotPushRequest
        @param headers: InvokeRobotPushHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeRobotPushResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.push_type):
            body['PushType'] = request.push_type
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeRobotPush',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/invokeRobotPush',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.InvokeRobotPushResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.InvokeRobotPushResponse(),
                self.execute(params, req, runtime)
            )

    async def invoke_robot_push_with_options_async(
        self,
        request: ali_genieip__1__0_models.InvokeRobotPushRequest,
        headers: ali_genieip__1__0_models.InvokeRobotPushHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.InvokeRobotPushResponse:
        """
        @summary 机器人服务，消息推送
        
        @param request: InvokeRobotPushRequest
        @param headers: InvokeRobotPushHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeRobotPushResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.push_type):
            body['PushType'] = request.push_type
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeRobotPush',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/invokeRobotPush',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.InvokeRobotPushResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.InvokeRobotPushResponse(),
                await self.execute_async(params, req, runtime)
            )

    def invoke_robot_push(
        self,
        request: ali_genieip__1__0_models.InvokeRobotPushRequest,
    ) -> ali_genieip__1__0_models.InvokeRobotPushResponse:
        """
        @summary 机器人服务，消息推送
        
        @param request: InvokeRobotPushRequest
        @return: InvokeRobotPushResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InvokeRobotPushHeaders()
        return self.invoke_robot_push_with_options(request, headers, runtime)

    async def invoke_robot_push_async(
        self,
        request: ali_genieip__1__0_models.InvokeRobotPushRequest,
    ) -> ali_genieip__1__0_models.InvokeRobotPushResponse:
        """
        @summary 机器人服务，消息推送
        
        @param request: InvokeRobotPushRequest
        @return: InvokeRobotPushResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.InvokeRobotPushHeaders()
        return await self.invoke_robot_push_with_options_async(request, headers, runtime)

    def list_all_provinces_with_options(
        self,
        headers: ali_genieip__1__0_models.ListAllProvincesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListAllProvincesResponse:
        """
        @summary 查询省份
        
        @param headers: ListAllProvincesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProvincesResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListAllProvinces',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listAllProvinces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListAllProvincesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListAllProvincesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_all_provinces_with_options_async(
        self,
        headers: ali_genieip__1__0_models.ListAllProvincesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListAllProvincesResponse:
        """
        @summary 查询省份
        
        @param headers: ListAllProvincesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProvincesResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListAllProvinces',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listAllProvinces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListAllProvincesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListAllProvincesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_all_provinces(self) -> ali_genieip__1__0_models.ListAllProvincesResponse:
        """
        @summary 查询省份
        
        @return: ListAllProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListAllProvincesHeaders()
        return self.list_all_provinces_with_options(headers, runtime)

    async def list_all_provinces_async(self) -> ali_genieip__1__0_models.ListAllProvincesResponse:
        """
        @summary 查询省份
        
        @return: ListAllProvincesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListAllProvincesHeaders()
        return await self.list_all_provinces_with_options_async(headers, runtime)

    def list_cities_by_province_with_options(
        self,
        request: ali_genieip__1__0_models.ListCitiesByProvinceRequest,
        headers: ali_genieip__1__0_models.ListCitiesByProvinceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListCitiesByProvinceResponse:
        """
        @summary 查询城市
        
        @param request: ListCitiesByProvinceRequest
        @param headers: ListCitiesByProvinceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCitiesByProvinceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCitiesByProvince',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listCitiesByProvince',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCitiesByProvinceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCitiesByProvinceResponse(),
                self.execute(params, req, runtime)
            )

    async def list_cities_by_province_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListCitiesByProvinceRequest,
        headers: ali_genieip__1__0_models.ListCitiesByProvinceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListCitiesByProvinceResponse:
        """
        @summary 查询城市
        
        @param request: ListCitiesByProvinceRequest
        @param headers: ListCitiesByProvinceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCitiesByProvinceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCitiesByProvince',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listCitiesByProvince',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCitiesByProvinceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCitiesByProvinceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_cities_by_province(
        self,
        request: ali_genieip__1__0_models.ListCitiesByProvinceRequest,
    ) -> ali_genieip__1__0_models.ListCitiesByProvinceResponse:
        """
        @summary 查询城市
        
        @param request: ListCitiesByProvinceRequest
        @return: ListCitiesByProvinceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCitiesByProvinceHeaders()
        return self.list_cities_by_province_with_options(request, headers, runtime)

    async def list_cities_by_province_async(
        self,
        request: ali_genieip__1__0_models.ListCitiesByProvinceRequest,
    ) -> ali_genieip__1__0_models.ListCitiesByProvinceResponse:
        """
        @summary 查询城市
        
        @param request: ListCitiesByProvinceRequest
        @return: ListCitiesByProvinceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCitiesByProvinceHeaders()
        return await self.list_cities_by_province_with_options_async(request, headers, runtime)

    def list_custom_qawith_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListCustomQARequest,
        headers: ali_genieip__1__0_models.ListCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListCustomQAResponse:
        """
        @summary 查询自定义问答列表
        
        @param tmp_req: ListCustomQARequest
        @param headers: ListCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCustomQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCustomQAResponse(),
                self.execute(params, req, runtime)
            )

    async def list_custom_qawith_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListCustomQARequest,
        headers: ali_genieip__1__0_models.ListCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListCustomQAResponse:
        """
        @summary 查询自定义问答列表
        
        @param tmp_req: ListCustomQARequest
        @param headers: ListCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCustomQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListCustomQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_custom_qa(
        self,
        request: ali_genieip__1__0_models.ListCustomQARequest,
    ) -> ali_genieip__1__0_models.ListCustomQAResponse:
        """
        @summary 查询自定义问答列表
        
        @param request: ListCustomQARequest
        @return: ListCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCustomQAHeaders()
        return self.list_custom_qawith_options(request, headers, runtime)

    async def list_custom_qa_async(
        self,
        request: ali_genieip__1__0_models.ListCustomQARequest,
    ) -> ali_genieip__1__0_models.ListCustomQAResponse:
        """
        @summary 查询自定义问答列表
        
        @param request: ListCustomQARequest
        @return: ListCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListCustomQAHeaders()
        return await self.list_custom_qawith_options_async(request, headers, runtime)

    def list_dialogue_template_with_options(
        self,
        request: ali_genieip__1__0_models.ListDialogueTemplateRequest,
        headers: ali_genieip__1__0_models.ListDialogueTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListDialogueTemplateResponse:
        """
        @summary 酒店场景对话模板
        
        @param request: ListDialogueTemplateRequest
        @param headers: ListDialogueTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogueTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogueTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listDialogueTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListDialogueTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListDialogueTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def list_dialogue_template_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListDialogueTemplateRequest,
        headers: ali_genieip__1__0_models.ListDialogueTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListDialogueTemplateResponse:
        """
        @summary 酒店场景对话模板
        
        @param request: ListDialogueTemplateRequest
        @param headers: ListDialogueTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialogueTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogueTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listDialogueTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListDialogueTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListDialogueTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_dialogue_template(
        self,
        request: ali_genieip__1__0_models.ListDialogueTemplateRequest,
    ) -> ali_genieip__1__0_models.ListDialogueTemplateResponse:
        """
        @summary 酒店场景对话模板
        
        @param request: ListDialogueTemplateRequest
        @return: ListDialogueTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListDialogueTemplateHeaders()
        return self.list_dialogue_template_with_options(request, headers, runtime)

    async def list_dialogue_template_async(
        self,
        request: ali_genieip__1__0_models.ListDialogueTemplateRequest,
    ) -> ali_genieip__1__0_models.ListDialogueTemplateResponse:
        """
        @summary 酒店场景对话模板
        
        @param request: ListDialogueTemplateRequest
        @return: ListDialogueTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListDialogueTemplateHeaders()
        return await self.list_dialogue_template_with_options_async(request, headers, runtime)

    def list_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelAlarmRequest,
        headers: ali_genieip__1__0_models.ListHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        """
        @summary 查询酒店闹钟
        
        @param tmp_req: ListHotelAlarmRequest
        @param headers: ListHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelAlarmList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelAlarmResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelAlarmResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelAlarmRequest,
        headers: ali_genieip__1__0_models.ListHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        """
        @summary 查询酒店闹钟
        
        @param tmp_req: ListHotelAlarmRequest
        @param headers: ListHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rooms):
            request.rooms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rooms, 'Rooms', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.rooms_shrink):
            body['Rooms'] = request.rooms_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/getHotelAlarmList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelAlarmResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelAlarmResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.ListHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        """
        @summary 查询酒店闹钟
        
        @param request: ListHotelAlarmRequest
        @return: ListHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelAlarmHeaders()
        return self.list_hotel_alarm_with_options(request, headers, runtime)

    async def list_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.ListHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.ListHotelAlarmResponse:
        """
        @summary 查询酒店闹钟
        
        @param request: ListHotelAlarmRequest
        @return: ListHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelAlarmHeaders()
        return await self.list_hotel_alarm_with_options_async(request, headers, runtime)

    def list_hotel_control_device_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
        headers: ali_genieip__1__0_models.ListHotelControlDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        """
        @summary 酒店设备列表
        
        @param tmp_req: ListHotelControlDeviceRequest
        @param headers: ListHotelControlDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelControlDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelControlDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelControlDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelControlDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_control_device_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
        headers: ali_genieip__1__0_models.ListHotelControlDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        """
        @summary 酒店设备列表
        
        @param tmp_req: ListHotelControlDeviceRequest
        @param headers: ListHotelControlDeviceHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelControlDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelControlDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelControlDevice',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelControlDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelControlDeviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_control_device(
        self,
        request: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        """
        @summary 酒店设备列表
        
        @param request: ListHotelControlDeviceRequest
        @return: ListHotelControlDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelControlDeviceHeaders()
        return self.list_hotel_control_device_with_options(request, headers, runtime)

    async def list_hotel_control_device_async(
        self,
        request: ali_genieip__1__0_models.ListHotelControlDeviceRequest,
    ) -> ali_genieip__1__0_models.ListHotelControlDeviceResponse:
        """
        @summary 酒店设备列表
        
        @param request: ListHotelControlDeviceRequest
        @return: ListHotelControlDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelControlDeviceHeaders()
        return await self.list_hotel_control_device_with_options_async(request, headers, runtime)

    def list_hotel_info_with_options(
        self,
        headers: ali_genieip__1__0_models.ListHotelInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        """
        @summary 获取酒店列表
        
        @param headers: ListHotelInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelInfoResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelInfo',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_info_with_options_async(
        self,
        headers: ali_genieip__1__0_models.ListHotelInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        """
        @summary 获取酒店列表
        
        @param headers: ListHotelInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelInfoResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelInfo',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_info(self) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        """
        @summary 获取酒店列表
        
        @return: ListHotelInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelInfoHeaders()
        return self.list_hotel_info_with_options(headers, runtime)

    async def list_hotel_info_async(self) -> ali_genieip__1__0_models.ListHotelInfoResponse:
        """
        @summary 获取酒店列表
        
        @return: ListHotelInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelInfoHeaders()
        return await self.list_hotel_info_with_options_async(headers, runtime)

    def list_hotel_message_template_with_options(
        self,
        headers: ali_genieip__1__0_models.ListHotelMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        """
        @summary 获取消息模板
        
        @param headers: ListHotelMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelMessageTemplateResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_message_template_with_options_async(
        self,
        headers: ali_genieip__1__0_models.ListHotelMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        """
        @summary 获取消息模板
        
        @param headers: ListHotelMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelMessageTemplateResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListHotelMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelMessageTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_message_template(self) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        """
        @summary 获取消息模板
        
        @return: ListHotelMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelMessageTemplateHeaders()
        return self.list_hotel_message_template_with_options(headers, runtime)

    async def list_hotel_message_template_async(self) -> ali_genieip__1__0_models.ListHotelMessageTemplateResponse:
        """
        @summary 获取消息模板
        
        @return: ListHotelMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelMessageTemplateHeaders()
        return await self.list_hotel_message_template_with_options_async(headers, runtime)

    def list_hotel_order_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelOrderRequest,
        headers: ali_genieip__1__0_models.ListHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        """
        @summary 酒店订单列表
        
        @param tmp_req: ListHotelOrderRequest
        @param headers: ListHotelOrderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelOrderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelOrderResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_order_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelOrderRequest,
        headers: ali_genieip__1__0_models.ListHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        """
        @summary 酒店订单列表
        
        @param tmp_req: ListHotelOrderRequest
        @param headers: ListHotelOrderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelOrderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelOrderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_order(
        self,
        request: ali_genieip__1__0_models.ListHotelOrderRequest,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        """
        @summary 酒店订单列表
        
        @param request: ListHotelOrderRequest
        @return: ListHotelOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelOrderHeaders()
        return self.list_hotel_order_with_options(request, headers, runtime)

    async def list_hotel_order_async(
        self,
        request: ali_genieip__1__0_models.ListHotelOrderRequest,
    ) -> ali_genieip__1__0_models.ListHotelOrderResponse:
        """
        @summary 酒店订单列表
        
        @param request: ListHotelOrderRequest
        @return: ListHotelOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelOrderHeaders()
        return await self.list_hotel_order_with_options_async(request, headers, runtime)

    def list_hotel_rooms_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelRoomsRequest,
        headers: ali_genieip__1__0_models.ListHotelRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        """
        @summary 获取酒店的所有房间
        
        @param tmp_req: ListHotelRoomsRequest
        @param headers: ListHotelRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelRoomsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelRoomsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_admin_room):
            request.hotel_admin_room_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_admin_room, 'HotelAdminRoom', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_admin_room_shrink):
            body['HotelAdminRoom'] = request.hotel_admin_room_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelRooms',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelRoomsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelRoomsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_rooms_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelRoomsRequest,
        headers: ali_genieip__1__0_models.ListHotelRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        """
        @summary 获取酒店的所有房间
        
        @param tmp_req: ListHotelRoomsRequest
        @param headers: ListHotelRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelRoomsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelRoomsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_admin_room):
            request.hotel_admin_room_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_admin_room, 'HotelAdminRoom', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_admin_room_shrink):
            body['HotelAdminRoom'] = request.hotel_admin_room_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelRooms',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelRoomsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelRoomsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_rooms(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        """
        @summary 获取酒店的所有房间
        
        @param request: ListHotelRoomsRequest
        @return: ListHotelRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelRoomsHeaders()
        return self.list_hotel_rooms_with_options(request, headers, runtime)

    async def list_hotel_rooms_async(
        self,
        request: ali_genieip__1__0_models.ListHotelRoomsRequest,
    ) -> ali_genieip__1__0_models.ListHotelRoomsResponse:
        """
        @summary 获取酒店的所有房间
        
        @param request: ListHotelRoomsRequest
        @return: ListHotelRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelRoomsHeaders()
        return await self.list_hotel_rooms_with_options_async(request, headers, runtime)

    def list_hotel_scene_book_items_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneBookItemsRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneBookItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneBookItemsResponse:
        """
        @summary 酒店场景预订列表（餐饮/SPA休闲/打车）
        
        @param tmp_req: ListHotelSceneBookItemsRequest
        @param headers: ListHotelSceneBookItemsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneBookItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneBookItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelSceneBookItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneBookItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneBookItemsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneBookItemsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_scene_book_items_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneBookItemsRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneBookItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneBookItemsResponse:
        """
        @summary 酒店场景预订列表（餐饮/SPA休闲/打车）
        
        @param tmp_req: ListHotelSceneBookItemsRequest
        @param headers: ListHotelSceneBookItemsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneBookItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneBookItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelSceneBookItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneBookItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneBookItemsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneBookItemsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_scene_book_items(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneBookItemsRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneBookItemsResponse:
        """
        @summary 酒店场景预订列表（餐饮/SPA休闲/打车）
        
        @param request: ListHotelSceneBookItemsRequest
        @return: ListHotelSceneBookItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneBookItemsHeaders()
        return self.list_hotel_scene_book_items_with_options(request, headers, runtime)

    async def list_hotel_scene_book_items_async(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneBookItemsRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneBookItemsResponse:
        """
        @summary 酒店场景预订列表（餐饮/SPA休闲/打车）
        
        @param request: ListHotelSceneBookItemsRequest
        @return: ListHotelSceneBookItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneBookItemsHeaders()
        return await self.list_hotel_scene_book_items_with_options_async(request, headers, runtime)

    def list_hotel_scene_item_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        """
        @summary 服务项目
        
        @param tmp_req: ListHotelSceneItemRequest
        @param headers: ListHotelSceneItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_scene_item_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        """
        @summary 服务项目
        
        @param tmp_req: ListHotelSceneItemRequest
        @param headers: ListHotelSceneItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_scene_item(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        """
        @summary 服务项目
        
        @param request: ListHotelSceneItemRequest
        @return: ListHotelSceneItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemHeaders()
        return self.list_hotel_scene_item_with_options(request, headers, runtime)

    async def list_hotel_scene_item_async(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemResponse:
        """
        @summary 服务项目
        
        @param request: ListHotelSceneItemRequest
        @return: ListHotelSceneItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemHeaders()
        return await self.list_hotel_scene_item_with_options_async(request, headers, runtime)

    def list_hotel_scene_items_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemsRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemsResponse:
        """
        @summary 酒店场景列表（物品/服务/维修）
        
        @param tmp_req: ListHotelSceneItemsRequest
        @param headers: ListHotelSceneItemsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_hotel_scene_req):
            request.list_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_hotel_scene_req, 'ListHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.list_hotel_scene_req_shrink):
            query['ListHotelSceneReq'] = request.list_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_scene_items_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelSceneItemsRequest,
        headers: ali_genieip__1__0_models.ListHotelSceneItemsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemsResponse:
        """
        @summary 酒店场景列表（物品/服务/维修）
        
        @param tmp_req: ListHotelSceneItemsRequest
        @param headers: ListHotelSceneItemsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelSceneItemsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelSceneItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_hotel_scene_req):
            request.list_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_hotel_scene_req, 'ListHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.list_hotel_scene_req_shrink):
            query['ListHotelSceneReq'] = request.list_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotelSceneItems',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelSceneItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelSceneItemsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_scene_items(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemsRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemsResponse:
        """
        @summary 酒店场景列表（物品/服务/维修）
        
        @param request: ListHotelSceneItemsRequest
        @return: ListHotelSceneItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemsHeaders()
        return self.list_hotel_scene_items_with_options(request, headers, runtime)

    async def list_hotel_scene_items_async(
        self,
        request: ali_genieip__1__0_models.ListHotelSceneItemsRequest,
    ) -> ali_genieip__1__0_models.ListHotelSceneItemsResponse:
        """
        @summary 酒店场景列表（物品/服务/维修）
        
        @param request: ListHotelSceneItemsRequest
        @return: ListHotelSceneItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelSceneItemsHeaders()
        return await self.list_hotel_scene_items_with_options_async(request, headers, runtime)

    def list_hotel_service_category_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
        headers: ali_genieip__1__0_models.ListHotelServiceCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        """
        @summary 服务分类列表
        
        @param tmp_req: ListHotelServiceCategoryRequest
        @param headers: ListHotelServiceCategoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelServiceCategoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelServiceCategoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelServiceCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelServiceCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotel_service_category_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
        headers: ali_genieip__1__0_models.ListHotelServiceCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        """
        @summary 服务分类列表
        
        @param tmp_req: ListHotelServiceCategoryRequest
        @param headers: ListHotelServiceCategoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelServiceCategoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelServiceCategoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotelServiceCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotelServiceCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelServiceCategoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotel_service_category(
        self,
        request: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        """
        @summary 服务分类列表
        
        @param request: ListHotelServiceCategoryRequest
        @return: ListHotelServiceCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelServiceCategoryHeaders()
        return self.list_hotel_service_category_with_options(request, headers, runtime)

    async def list_hotel_service_category_async(
        self,
        request: ali_genieip__1__0_models.ListHotelServiceCategoryRequest,
    ) -> ali_genieip__1__0_models.ListHotelServiceCategoryResponse:
        """
        @summary 服务分类列表
        
        @param request: ListHotelServiceCategoryRequest
        @return: ListHotelServiceCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelServiceCategoryHeaders()
        return await self.list_hotel_service_category_with_options_async(request, headers, runtime)

    def list_hotels_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelsRequest,
        headers: ali_genieip__1__0_models.ListHotelsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelsResponse:
        """
        @summary 酒店列表(待审批/已拒绝/已通过)
        
        @param tmp_req: ListHotelsRequest
        @param headers: ListHotelsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_request):
            request.hotel_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_request, 'HotelRequest', 'json')
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.hotel_request_shrink):
            query['HotelRequest'] = request.hotel_request_shrink
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotels',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_hotels_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListHotelsRequest,
        headers: ali_genieip__1__0_models.ListHotelsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListHotelsResponse:
        """
        @summary 酒店列表(待审批/已拒绝/已通过)
        
        @param tmp_req: ListHotelsRequest
        @param headers: ListHotelsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListHotelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hotel_request):
            request.hotel_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hotel_request, 'HotelRequest', 'json')
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.hotel_request_shrink):
            query['HotelRequest'] = request.hotel_request_shrink
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotels',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listHotels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListHotelsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_hotels(
        self,
        request: ali_genieip__1__0_models.ListHotelsRequest,
    ) -> ali_genieip__1__0_models.ListHotelsResponse:
        """
        @summary 酒店列表(待审批/已拒绝/已通过)
        
        @param request: ListHotelsRequest
        @return: ListHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelsHeaders()
        return self.list_hotels_with_options(request, headers, runtime)

    async def list_hotels_async(
        self,
        request: ali_genieip__1__0_models.ListHotelsRequest,
    ) -> ali_genieip__1__0_models.ListHotelsResponse:
        """
        @summary 酒店列表(待审批/已拒绝/已通过)
        
        @param request: ListHotelsRequest
        @return: ListHotelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListHotelsHeaders()
        return await self.list_hotels_with_options_async(request, headers, runtime)

    def list_infrared_device_brands_with_options(
        self,
        request: ali_genieip__1__0_models.ListInfraredDeviceBrandsRequest,
        headers: ali_genieip__1__0_models.ListInfraredDeviceBrandsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse:
        """
        @summary 查询红外品牌列表
        
        @param request: ListInfraredDeviceBrandsRequest
        @param headers: ListInfraredDeviceBrandsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInfraredDeviceBrandsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInfraredDeviceBrands',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listInfraredDeviceBrands',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_infrared_device_brands_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListInfraredDeviceBrandsRequest,
        headers: ali_genieip__1__0_models.ListInfraredDeviceBrandsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse:
        """
        @summary 查询红外品牌列表
        
        @param request: ListInfraredDeviceBrandsRequest
        @param headers: ListInfraredDeviceBrandsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInfraredDeviceBrandsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInfraredDeviceBrands',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listInfraredDeviceBrands',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_infrared_device_brands(
        self,
        request: ali_genieip__1__0_models.ListInfraredDeviceBrandsRequest,
    ) -> ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse:
        """
        @summary 查询红外品牌列表
        
        @param request: ListInfraredDeviceBrandsRequest
        @return: ListInfraredDeviceBrandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredDeviceBrandsHeaders()
        return self.list_infrared_device_brands_with_options(request, headers, runtime)

    async def list_infrared_device_brands_async(
        self,
        request: ali_genieip__1__0_models.ListInfraredDeviceBrandsRequest,
    ) -> ali_genieip__1__0_models.ListInfraredDeviceBrandsResponse:
        """
        @summary 查询红外品牌列表
        
        @param request: ListInfraredDeviceBrandsRequest
        @return: ListInfraredDeviceBrandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredDeviceBrandsHeaders()
        return await self.list_infrared_device_brands_with_options_async(request, headers, runtime)

    def list_infrared_remote_controllers_with_options(
        self,
        request: ali_genieip__1__0_models.ListInfraredRemoteControllersRequest,
        headers: ali_genieip__1__0_models.ListInfraredRemoteControllersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListInfraredRemoteControllersResponse:
        """
        @summary 查询红外码库列表
        
        @param request: ListInfraredRemoteControllersRequest
        @param headers: ListInfraredRemoteControllersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInfraredRemoteControllersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInfraredRemoteControllers',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listInfraredRemoteControllers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredRemoteControllersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredRemoteControllersResponse(),
                self.execute(params, req, runtime)
            )

    async def list_infrared_remote_controllers_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListInfraredRemoteControllersRequest,
        headers: ali_genieip__1__0_models.ListInfraredRemoteControllersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListInfraredRemoteControllersResponse:
        """
        @summary 查询红外码库列表
        
        @param request: ListInfraredRemoteControllersRequest
        @param headers: ListInfraredRemoteControllersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInfraredRemoteControllersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.service_provider):
            body['ServiceProvider'] = request.service_provider
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInfraredRemoteControllers',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listInfraredRemoteControllers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredRemoteControllersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListInfraredRemoteControllersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_infrared_remote_controllers(
        self,
        request: ali_genieip__1__0_models.ListInfraredRemoteControllersRequest,
    ) -> ali_genieip__1__0_models.ListInfraredRemoteControllersResponse:
        """
        @summary 查询红外码库列表
        
        @param request: ListInfraredRemoteControllersRequest
        @return: ListInfraredRemoteControllersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredRemoteControllersHeaders()
        return self.list_infrared_remote_controllers_with_options(request, headers, runtime)

    async def list_infrared_remote_controllers_async(
        self,
        request: ali_genieip__1__0_models.ListInfraredRemoteControllersRequest,
    ) -> ali_genieip__1__0_models.ListInfraredRemoteControllersResponse:
        """
        @summary 查询红外码库列表
        
        @param request: ListInfraredRemoteControllersRequest
        @return: ListInfraredRemoteControllersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListInfraredRemoteControllersHeaders()
        return await self.list_infrared_remote_controllers_with_options_async(request, headers, runtime)

    def list_stbservice_providers_with_options(
        self,
        request: ali_genieip__1__0_models.ListSTBServiceProvidersRequest,
        headers: ali_genieip__1__0_models.ListSTBServiceProvidersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListSTBServiceProvidersResponse:
        """
        @summary 查询服务提供商
        
        @param request: ListSTBServiceProvidersRequest
        @param headers: ListSTBServiceProvidersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSTBServiceProvidersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSTBServiceProviders',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listSTBServiceProviders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSTBServiceProvidersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSTBServiceProvidersResponse(),
                self.execute(params, req, runtime)
            )

    async def list_stbservice_providers_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListSTBServiceProvidersRequest,
        headers: ali_genieip__1__0_models.ListSTBServiceProvidersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListSTBServiceProvidersResponse:
        """
        @summary 查询服务提供商
        
        @param request: ListSTBServiceProvidersRequest
        @param headers: ListSTBServiceProvidersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSTBServiceProvidersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSTBServiceProviders',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listSTBServiceProviders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSTBServiceProvidersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSTBServiceProvidersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_stbservice_providers(
        self,
        request: ali_genieip__1__0_models.ListSTBServiceProvidersRequest,
    ) -> ali_genieip__1__0_models.ListSTBServiceProvidersResponse:
        """
        @summary 查询服务提供商
        
        @param request: ListSTBServiceProvidersRequest
        @return: ListSTBServiceProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSTBServiceProvidersHeaders()
        return self.list_stbservice_providers_with_options(request, headers, runtime)

    async def list_stbservice_providers_async(
        self,
        request: ali_genieip__1__0_models.ListSTBServiceProvidersRequest,
    ) -> ali_genieip__1__0_models.ListSTBServiceProvidersResponse:
        """
        @summary 查询服务提供商
        
        @param request: ListSTBServiceProvidersRequest
        @return: ListSTBServiceProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSTBServiceProvidersHeaders()
        return await self.list_stbservice_providers_with_options_async(request, headers, runtime)

    def list_scene_category_with_options(
        self,
        request: ali_genieip__1__0_models.ListSceneCategoryRequest,
        headers: ali_genieip__1__0_models.ListSceneCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListSceneCategoryResponse:
        """
        @summary 酒店场景分类
        
        @param request: ListSceneCategoryRequest
        @param headers: ListSceneCategoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSceneCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listSceneCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSceneCategoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSceneCategoryResponse(),
                self.execute(params, req, runtime)
            )

    async def list_scene_category_with_options_async(
        self,
        request: ali_genieip__1__0_models.ListSceneCategoryRequest,
        headers: ali_genieip__1__0_models.ListSceneCategoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListSceneCategoryResponse:
        """
        @summary 酒店场景分类
        
        @param request: ListSceneCategoryRequest
        @param headers: ListSceneCategoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneCategoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSceneCategory',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listSceneCategory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSceneCategoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListSceneCategoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_scene_category(
        self,
        request: ali_genieip__1__0_models.ListSceneCategoryRequest,
    ) -> ali_genieip__1__0_models.ListSceneCategoryResponse:
        """
        @summary 酒店场景分类
        
        @param request: ListSceneCategoryRequest
        @return: ListSceneCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSceneCategoryHeaders()
        return self.list_scene_category_with_options(request, headers, runtime)

    async def list_scene_category_async(
        self,
        request: ali_genieip__1__0_models.ListSceneCategoryRequest,
    ) -> ali_genieip__1__0_models.ListSceneCategoryResponse:
        """
        @summary 酒店场景分类
        
        @param request: ListSceneCategoryRequest
        @return: ListSceneCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListSceneCategoryHeaders()
        return await self.list_scene_category_with_options_async(request, headers, runtime)

    def list_service_qawith_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListServiceQARequest,
        headers: ali_genieip__1__0_models.ListServiceQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListServiceQAResponse:
        """
        @summary 查询服务设施问答列表
        
        @param tmp_req: ListServiceQARequest
        @param headers: ListServiceQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListServiceQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListServiceQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListServiceQAResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_qawith_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListServiceQARequest,
        headers: ali_genieip__1__0_models.ListServiceQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListServiceQAResponse:
        """
        @summary 查询服务设施问答列表
        
        @param tmp_req: ListServiceQARequest
        @param headers: ListServiceQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListServiceQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListServiceQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListServiceQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_qa(
        self,
        request: ali_genieip__1__0_models.ListServiceQARequest,
    ) -> ali_genieip__1__0_models.ListServiceQAResponse:
        """
        @summary 查询服务设施问答列表
        
        @param request: ListServiceQARequest
        @return: ListServiceQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListServiceQAHeaders()
        return self.list_service_qawith_options(request, headers, runtime)

    async def list_service_qa_async(
        self,
        request: ali_genieip__1__0_models.ListServiceQARequest,
    ) -> ali_genieip__1__0_models.ListServiceQAResponse:
        """
        @summary 查询服务设施问答列表
        
        @param request: ListServiceQARequest
        @return: ListServiceQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListServiceQAHeaders()
        return await self.list_service_qawith_options_async(request, headers, runtime)

    def list_tickets_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.ListTicketsRequest,
        headers: ali_genieip__1__0_models.ListTicketsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListTicketsResponse:
        """
        @summary 查询工单列表
        
        @param tmp_req: ListTicketsRequest
        @param headers: ListTicketsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTicketsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.is_desc):
            body['IsDesc'] = request.is_desc
        if not UtilClient.is_unset(request.is_need_callback):
            body['IsNeedCallback'] = request.is_need_callback
        if not UtilClient.is_unset(request.is_need_charges):
            body['IsNeedCharges'] = request.is_need_charges
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTickets',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listTickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListTicketsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListTicketsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tickets_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.ListTicketsRequest,
        headers: ali_genieip__1__0_models.ListTicketsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ListTicketsResponse:
        """
        @summary 查询工单列表
        
        @param tmp_req: ListTicketsRequest
        @param headers: ListTicketsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTicketsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.ListTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.is_desc):
            body['IsDesc'] = request.is_desc
        if not UtilClient.is_unset(request.is_need_callback):
            body['IsNeedCallback'] = request.is_need_callback
        if not UtilClient.is_unset(request.is_need_charges):
            body['IsNeedCharges'] = request.is_need_charges
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTickets',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/listTickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListTicketsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ListTicketsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tickets(
        self,
        request: ali_genieip__1__0_models.ListTicketsRequest,
    ) -> ali_genieip__1__0_models.ListTicketsResponse:
        """
        @summary 查询工单列表
        
        @param request: ListTicketsRequest
        @return: ListTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListTicketsHeaders()
        return self.list_tickets_with_options(request, headers, runtime)

    async def list_tickets_async(
        self,
        request: ali_genieip__1__0_models.ListTicketsRequest,
    ) -> ali_genieip__1__0_models.ListTicketsResponse:
        """
        @summary 查询工单列表
        
        @param request: ListTicketsRequest
        @return: ListTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ListTicketsHeaders()
        return await self.list_tickets_with_options_async(request, headers, runtime)

    def page_get_hotel_room_devices_with_options(
        self,
        request: ali_genieip__1__0_models.PageGetHotelRoomDevicesRequest,
        headers: ali_genieip__1__0_models.PageGetHotelRoomDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse:
        """
        @summary 分页查询酒店房间主控设备
        
        @param request: PageGetHotelRoomDevicesRequest
        @param headers: PageGetHotelRoomDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageGetHotelRoomDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageGetHotelRoomDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pageGetHotelRoomDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse(),
                self.execute(params, req, runtime)
            )

    async def page_get_hotel_room_devices_with_options_async(
        self,
        request: ali_genieip__1__0_models.PageGetHotelRoomDevicesRequest,
        headers: ali_genieip__1__0_models.PageGetHotelRoomDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse:
        """
        @summary 分页查询酒店房间主控设备
        
        @param request: PageGetHotelRoomDevicesRequest
        @param headers: PageGetHotelRoomDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageGetHotelRoomDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageGetHotelRoomDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pageGetHotelRoomDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def page_get_hotel_room_devices(
        self,
        request: ali_genieip__1__0_models.PageGetHotelRoomDevicesRequest,
    ) -> ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse:
        """
        @summary 分页查询酒店房间主控设备
        
        @param request: PageGetHotelRoomDevicesRequest
        @return: PageGetHotelRoomDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PageGetHotelRoomDevicesHeaders()
        return self.page_get_hotel_room_devices_with_options(request, headers, runtime)

    async def page_get_hotel_room_devices_async(
        self,
        request: ali_genieip__1__0_models.PageGetHotelRoomDevicesRequest,
    ) -> ali_genieip__1__0_models.PageGetHotelRoomDevicesResponse:
        """
        @summary 分页查询酒店房间主控设备
        
        @param request: PageGetHotelRoomDevicesRequest
        @return: PageGetHotelRoomDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PageGetHotelRoomDevicesHeaders()
        return await self.page_get_hotel_room_devices_with_options_async(request, headers, runtime)

    def pms_event_report_with_options(
        self,
        request: ali_genieip__1__0_models.PmsEventReportRequest,
        headers: ali_genieip__1__0_models.PmsEventReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PmsEventReportResponse:
        """
        @summary pms事件上报
        
        @param request: PmsEventReportRequest
        @param headers: PmsEventReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PmsEventReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PmsEventReport',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pmsEventReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PmsEventReportResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PmsEventReportResponse(),
                self.execute(params, req, runtime)
            )

    async def pms_event_report_with_options_async(
        self,
        request: ali_genieip__1__0_models.PmsEventReportRequest,
        headers: ali_genieip__1__0_models.PmsEventReportHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PmsEventReportResponse:
        """
        @summary pms事件上报
        
        @param request: PmsEventReportRequest
        @param headers: PmsEventReportHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PmsEventReportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PmsEventReport',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pmsEventReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PmsEventReportResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PmsEventReportResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pms_event_report(
        self,
        request: ali_genieip__1__0_models.PmsEventReportRequest,
    ) -> ali_genieip__1__0_models.PmsEventReportResponse:
        """
        @summary pms事件上报
        
        @param request: PmsEventReportRequest
        @return: PmsEventReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PmsEventReportHeaders()
        return self.pms_event_report_with_options(request, headers, runtime)

    async def pms_event_report_async(
        self,
        request: ali_genieip__1__0_models.PmsEventReportRequest,
    ) -> ali_genieip__1__0_models.PmsEventReportResponse:
        """
        @summary pms事件上报
        
        @param request: PmsEventReportRequest
        @return: PmsEventReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PmsEventReportHeaders()
        return await self.pms_event_report_with_options_async(request, headers, runtime)

    def push_hotel_message_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.PushHotelMessageRequest,
        headers: ali_genieip__1__0_models.PushHotelMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        """
        @summary 推送酒店消息
        
        @param tmp_req: PushHotelMessageRequest
        @param headers: PushHotelMessageHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushHotelMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushHotelMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.push_hotel_message_req, 'PushHotelMessageReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushHotelMessage',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushHotelMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushHotelMessageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushHotelMessageResponse(),
                self.execute(params, req, runtime)
            )

    async def push_hotel_message_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.PushHotelMessageRequest,
        headers: ali_genieip__1__0_models.PushHotelMessageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        """
        @summary 推送酒店消息
        
        @param tmp_req: PushHotelMessageRequest
        @param headers: PushHotelMessageHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushHotelMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushHotelMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.push_hotel_message_req):
            request.push_hotel_message_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.push_hotel_message_req, 'PushHotelMessageReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.push_hotel_message_req_shrink):
            query['PushHotelMessageReq'] = request.push_hotel_message_req_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushHotelMessage',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushHotelMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushHotelMessageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushHotelMessageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_hotel_message(
        self,
        request: ali_genieip__1__0_models.PushHotelMessageRequest,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        """
        @summary 推送酒店消息
        
        @param request: PushHotelMessageRequest
        @return: PushHotelMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushHotelMessageHeaders()
        return self.push_hotel_message_with_options(request, headers, runtime)

    async def push_hotel_message_async(
        self,
        request: ali_genieip__1__0_models.PushHotelMessageRequest,
    ) -> ali_genieip__1__0_models.PushHotelMessageResponse:
        """
        @summary 推送酒店消息
        
        @param request: PushHotelMessageRequest
        @return: PushHotelMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushHotelMessageHeaders()
        return await self.push_hotel_message_with_options_async(request, headers, runtime)

    def push_voice_box_commands_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.PushVoiceBoxCommandsRequest,
        headers: ali_genieip__1__0_models.PushVoiceBoxCommandsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushVoiceBoxCommandsResponse:
        """
        @summary 推送音箱指令
        
        @param tmp_req: PushVoiceBoxCommandsRequest
        @param headers: PushVoiceBoxCommandsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushVoiceBoxCommandsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushVoiceBoxCommandsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commands):
            request.commands_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        body = {}
        if not UtilClient.is_unset(request.commands_shrink):
            body['Commands'] = request.commands_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushVoiceBoxCommands',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushVoiceBoxCommands',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushVoiceBoxCommandsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushVoiceBoxCommandsResponse(),
                self.execute(params, req, runtime)
            )

    async def push_voice_box_commands_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.PushVoiceBoxCommandsRequest,
        headers: ali_genieip__1__0_models.PushVoiceBoxCommandsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushVoiceBoxCommandsResponse:
        """
        @summary 推送音箱指令
        
        @param tmp_req: PushVoiceBoxCommandsRequest
        @param headers: PushVoiceBoxCommandsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushVoiceBoxCommandsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushVoiceBoxCommandsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commands):
            request.commands_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        body = {}
        if not UtilClient.is_unset(request.commands_shrink):
            body['Commands'] = request.commands_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushVoiceBoxCommands',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushVoiceBoxCommands',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushVoiceBoxCommandsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushVoiceBoxCommandsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_voice_box_commands(
        self,
        request: ali_genieip__1__0_models.PushVoiceBoxCommandsRequest,
    ) -> ali_genieip__1__0_models.PushVoiceBoxCommandsResponse:
        """
        @summary 推送音箱指令
        
        @param request: PushVoiceBoxCommandsRequest
        @return: PushVoiceBoxCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushVoiceBoxCommandsHeaders()
        return self.push_voice_box_commands_with_options(request, headers, runtime)

    async def push_voice_box_commands_async(
        self,
        request: ali_genieip__1__0_models.PushVoiceBoxCommandsRequest,
    ) -> ali_genieip__1__0_models.PushVoiceBoxCommandsResponse:
        """
        @summary 推送音箱指令
        
        @param request: PushVoiceBoxCommandsRequest
        @return: PushVoiceBoxCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushVoiceBoxCommandsHeaders()
        return await self.push_voice_box_commands_with_options_async(request, headers, runtime)

    def push_welcome_with_options(
        self,
        request: ali_genieip__1__0_models.PushWelcomeRequest,
        headers: ali_genieip__1__0_models.PushWelcomeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushWelcomeResponse:
        """
        @summary 直接推送欢迎语
        
        @param request: PushWelcomeRequest
        @param headers: PushWelcomeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushWelcomeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.welcome_music_url):
            body['WelcomeMusicUrl'] = request.welcome_music_url
        if not UtilClient.is_unset(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushWelcome',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushWelcome',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeResponse(),
                self.execute(params, req, runtime)
            )

    async def push_welcome_with_options_async(
        self,
        request: ali_genieip__1__0_models.PushWelcomeRequest,
        headers: ali_genieip__1__0_models.PushWelcomeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushWelcomeResponse:
        """
        @summary 直接推送欢迎语
        
        @param request: PushWelcomeRequest
        @param headers: PushWelcomeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushWelcomeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.welcome_music_url):
            body['WelcomeMusicUrl'] = request.welcome_music_url
        if not UtilClient.is_unset(request.welcome_text):
            body['WelcomeText'] = request.welcome_text
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushWelcome',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushWelcome',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_welcome(
        self,
        request: ali_genieip__1__0_models.PushWelcomeRequest,
    ) -> ali_genieip__1__0_models.PushWelcomeResponse:
        """
        @summary 直接推送欢迎语
        
        @param request: PushWelcomeRequest
        @return: PushWelcomeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushWelcomeHeaders()
        return self.push_welcome_with_options(request, headers, runtime)

    async def push_welcome_async(
        self,
        request: ali_genieip__1__0_models.PushWelcomeRequest,
    ) -> ali_genieip__1__0_models.PushWelcomeResponse:
        """
        @summary 直接推送欢迎语
        
        @param request: PushWelcomeRequest
        @return: PushWelcomeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushWelcomeHeaders()
        return await self.push_welcome_with_options_async(request, headers, runtime)

    def push_welcome_text_and_music_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.PushWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.PushWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse:
        """
        @summary 推送欢迎语
        
        @param tmp_req: PushWelcomeTextAndMusicRequest
        @param headers: PushWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushWelcomeTextAndMusicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_variable):
            request.template_variable_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_variable, 'TemplateVariable', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.template_variable_shrink):
            body['TemplateVariable'] = request.template_variable_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse(),
                self.execute(params, req, runtime)
            )

    async def push_welcome_text_and_music_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.PushWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.PushWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse:
        """
        @summary 推送欢迎语
        
        @param tmp_req: PushWelcomeTextAndMusicRequest
        @param headers: PushWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.PushWelcomeTextAndMusicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_variable):
            request.template_variable_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_variable, 'TemplateVariable', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.template_variable_shrink):
            body['TemplateVariable'] = request.template_variable_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/pushWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_welcome_text_and_music(
        self,
        request: ali_genieip__1__0_models.PushWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse:
        """
        @summary 推送欢迎语
        
        @param request: PushWelcomeTextAndMusicRequest
        @return: PushWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushWelcomeTextAndMusicHeaders()
        return self.push_welcome_text_and_music_with_options(request, headers, runtime)

    async def push_welcome_text_and_music_async(
        self,
        request: ali_genieip__1__0_models.PushWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.PushWelcomeTextAndMusicResponse:
        """
        @summary 推送欢迎语
        
        @param request: PushWelcomeTextAndMusicRequest
        @return: PushWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.PushWelcomeTextAndMusicHeaders()
        return await self.push_welcome_text_and_music_with_options_async(request, headers, runtime)

    def query_device_status_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.QueryDeviceStatusRequest,
        headers: ali_genieip__1__0_models.QueryDeviceStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        """
        @summary 查询酒店设备状态/模式状态查询
        
        @param tmp_req: QueryDeviceStatusRequest
        @param headers: QueryDeviceStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryDeviceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryDeviceStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryDeviceStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryDeviceStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def query_device_status_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.QueryDeviceStatusRequest,
        headers: ali_genieip__1__0_models.QueryDeviceStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        """
        @summary 查询酒店设备状态/模式状态查询
        
        @param tmp_req: QueryDeviceStatusRequest
        @param headers: QueryDeviceStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QueryDeviceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryDeviceStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryDeviceStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryDeviceStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_device_status(
        self,
        request: ali_genieip__1__0_models.QueryDeviceStatusRequest,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        """
        @summary 查询酒店设备状态/模式状态查询
        
        @param request: QueryDeviceStatusRequest
        @return: QueryDeviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryDeviceStatusHeaders()
        return self.query_device_status_with_options(request, headers, runtime)

    async def query_device_status_async(
        self,
        request: ali_genieip__1__0_models.QueryDeviceStatusRequest,
    ) -> ali_genieip__1__0_models.QueryDeviceStatusResponse:
        """
        @summary 查询酒店设备状态/模式状态查询
        
        @param request: QueryDeviceStatusRequest
        @return: QueryDeviceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryDeviceStatusHeaders()
        return await self.query_device_status_with_options_async(request, headers, runtime)

    def query_hotel_room_detail_with_options(
        self,
        request: ali_genieip__1__0_models.QueryHotelRoomDetailRequest,
        headers: ali_genieip__1__0_models.QueryHotelRoomDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryHotelRoomDetailResponse:
        """
        @summary 查询房间详细信息
        
        @param request: QueryHotelRoomDetailRequest
        @param headers: QueryHotelRoomDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelRoomDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryHotelRoomDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryHotelRoomDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryHotelRoomDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryHotelRoomDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def query_hotel_room_detail_with_options_async(
        self,
        request: ali_genieip__1__0_models.QueryHotelRoomDetailRequest,
        headers: ali_genieip__1__0_models.QueryHotelRoomDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryHotelRoomDetailResponse:
        """
        @summary 查询房间详细信息
        
        @param request: QueryHotelRoomDetailRequest
        @param headers: QueryHotelRoomDetailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHotelRoomDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryHotelRoomDetail',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryHotelRoomDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryHotelRoomDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryHotelRoomDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_hotel_room_detail(
        self,
        request: ali_genieip__1__0_models.QueryHotelRoomDetailRequest,
    ) -> ali_genieip__1__0_models.QueryHotelRoomDetailResponse:
        """
        @summary 查询房间详细信息
        
        @param request: QueryHotelRoomDetailRequest
        @return: QueryHotelRoomDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryHotelRoomDetailHeaders()
        return self.query_hotel_room_detail_with_options(request, headers, runtime)

    async def query_hotel_room_detail_async(
        self,
        request: ali_genieip__1__0_models.QueryHotelRoomDetailRequest,
    ) -> ali_genieip__1__0_models.QueryHotelRoomDetailResponse:
        """
        @summary 查询房间详细信息
        
        @param request: QueryHotelRoomDetailRequest
        @return: QueryHotelRoomDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryHotelRoomDetailHeaders()
        return await self.query_hotel_room_detail_with_options_async(request, headers, runtime)

    def query_room_control_devices_with_options(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        """
        @summary 查询酒店房间客控设备
        
        @param request: QueryRoomControlDevicesRequest
        @param headers: QueryRoomControlDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomControlDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
                self.execute(params, req, runtime)
            )

    async def query_room_control_devices_with_options_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        """
        @summary 查询酒店房间客控设备
        
        @param request: QueryRoomControlDevicesRequest
        @param headers: QueryRoomControlDevicesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomControlDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hotel_id):
            query['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            query['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRoomControlDevices',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_room_control_devices(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        """
        @summary 查询酒店房间客控设备
        
        @param request: QueryRoomControlDevicesRequest
        @return: QueryRoomControlDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesHeaders()
        return self.query_room_control_devices_with_options(request, headers, runtime)

    async def query_room_control_devices_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesResponse:
        """
        @summary 查询酒店房间客控设备
        
        @param request: QueryRoomControlDevicesRequest
        @return: QueryRoomControlDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesHeaders()
        return await self.query_room_control_devices_with_options_async(request, headers, runtime)

    def query_room_control_devices_and_status_with_options(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse:
        """
        @summary 查询房间被控设备包含设备状态
        
        @param request: QueryRoomControlDevicesAndStatusRequest
        @param headers: QueryRoomControlDevicesAndStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomControlDevicesAndStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRoomControlDevicesAndStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevicesAndStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def query_room_control_devices_and_status_with_options_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusRequest,
        headers: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse:
        """
        @summary 查询房间被控设备包含设备状态
        
        @param request: QueryRoomControlDevicesAndStatusRequest
        @param headers: QueryRoomControlDevicesAndStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomControlDevicesAndStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRoomControlDevicesAndStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomControlDevicesAndStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_room_control_devices_and_status(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse:
        """
        @summary 查询房间被控设备包含设备状态
        
        @param request: QueryRoomControlDevicesAndStatusRequest
        @return: QueryRoomControlDevicesAndStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusHeaders()
        return self.query_room_control_devices_and_status_with_options(request, headers, runtime)

    async def query_room_control_devices_and_status_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusRequest,
    ) -> ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusResponse:
        """
        @summary 查询房间被控设备包含设备状态
        
        @param request: QueryRoomControlDevicesAndStatusRequest
        @return: QueryRoomControlDevicesAndStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomControlDevicesAndStatusHeaders()
        return await self.query_room_control_devices_and_status_with_options_async(request, headers, runtime)

    def query_room_status_with_options(
        self,
        request: ali_genieip__1__0_models.QueryRoomStatusRequest,
        headers: ali_genieip__1__0_models.QueryRoomStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomStatusResponse:
        """
        @summary 查询房态信息
        
        @param request: QueryRoomStatusRequest
        @param headers: QueryRoomStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRoomStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def query_room_status_with_options_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomStatusRequest,
        headers: ali_genieip__1__0_models.QueryRoomStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QueryRoomStatusResponse:
        """
        @summary 查询房态信息
        
        @param request: QueryRoomStatusRequest
        @param headers: QueryRoomStatusHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRoomStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRoomStatus',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/queryRoomStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QueryRoomStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_room_status(
        self,
        request: ali_genieip__1__0_models.QueryRoomStatusRequest,
    ) -> ali_genieip__1__0_models.QueryRoomStatusResponse:
        """
        @summary 查询房态信息
        
        @param request: QueryRoomStatusRequest
        @return: QueryRoomStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomStatusHeaders()
        return self.query_room_status_with_options(request, headers, runtime)

    async def query_room_status_async(
        self,
        request: ali_genieip__1__0_models.QueryRoomStatusRequest,
    ) -> ali_genieip__1__0_models.QueryRoomStatusResponse:
        """
        @summary 查询房态信息
        
        @param request: QueryRoomStatusRequest
        @return: QueryRoomStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QueryRoomStatusHeaders()
        return await self.query_room_status_with_options_async(request, headers, runtime)

    def query_scene_list_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.QuerySceneListRequest,
        headers: ali_genieip__1__0_models.QuerySceneListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QuerySceneListResponse:
        """
        @summary 查询酒店场景列表
        
        @param tmp_req: QuerySceneListRequest
        @param headers: QuerySceneListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySceneListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QuerySceneListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_states):
            request.scene_states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_states, 'SceneStates', 'json')
        if not UtilClient.is_unset(tmp_req.scene_types):
            request.scene_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_types, 'SceneTypes', 'json')
        if not UtilClient.is_unset(tmp_req.template_info_ids):
            request.template_info_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_info_ids, 'TemplateInfoIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_states_shrink):
            body['SceneStates'] = request.scene_states_shrink
        if not UtilClient.is_unset(request.scene_types_shrink):
            body['SceneTypes'] = request.scene_types_shrink
        if not UtilClient.is_unset(request.template_info_ids_shrink):
            body['TemplateInfoIds'] = request.template_info_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySceneList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/querySceneList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QuerySceneListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QuerySceneListResponse(),
                self.execute(params, req, runtime)
            )

    async def query_scene_list_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.QuerySceneListRequest,
        headers: ali_genieip__1__0_models.QuerySceneListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.QuerySceneListResponse:
        """
        @summary 查询酒店场景列表
        
        @param tmp_req: QuerySceneListRequest
        @param headers: QuerySceneListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySceneListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.QuerySceneListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_states):
            request.scene_states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_states, 'SceneStates', 'json')
        if not UtilClient.is_unset(tmp_req.scene_types):
            request.scene_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_types, 'SceneTypes', 'json')
        if not UtilClient.is_unset(tmp_req.template_info_ids):
            request.template_info_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_info_ids, 'TemplateInfoIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_states_shrink):
            body['SceneStates'] = request.scene_states_shrink
        if not UtilClient.is_unset(request.scene_types_shrink):
            body['SceneTypes'] = request.scene_types_shrink
        if not UtilClient.is_unset(request.template_info_ids_shrink):
            body['TemplateInfoIds'] = request.template_info_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySceneList',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/querySceneList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.QuerySceneListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.QuerySceneListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_scene_list(
        self,
        request: ali_genieip__1__0_models.QuerySceneListRequest,
    ) -> ali_genieip__1__0_models.QuerySceneListResponse:
        """
        @summary 查询酒店场景列表
        
        @param request: QuerySceneListRequest
        @return: QuerySceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QuerySceneListHeaders()
        return self.query_scene_list_with_options(request, headers, runtime)

    async def query_scene_list_async(
        self,
        request: ali_genieip__1__0_models.QuerySceneListRequest,
    ) -> ali_genieip__1__0_models.QuerySceneListResponse:
        """
        @summary 查询酒店场景列表
        
        @param request: QuerySceneListRequest
        @return: QuerySceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.QuerySceneListHeaders()
        return await self.query_scene_list_with_options_async(request, headers, runtime)

    def remove_child_account_auth_with_options(
        self,
        request: ali_genieip__1__0_models.RemoveChildAccountAuthRequest,
        headers: ali_genieip__1__0_models.RemoveChildAccountAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RemoveChildAccountAuthResponse:
        """
        @summary 删除子账号授权
        
        @param request: RemoveChildAccountAuthRequest
        @param headers: RemoveChildAccountAuthHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveChildAccountAuthResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.child_account_name):
            body['ChildAccountName'] = request.child_account_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/removeChildAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveChildAccountAuthResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveChildAccountAuthResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_child_account_auth_with_options_async(
        self,
        request: ali_genieip__1__0_models.RemoveChildAccountAuthRequest,
        headers: ali_genieip__1__0_models.RemoveChildAccountAuthHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RemoveChildAccountAuthResponse:
        """
        @summary 删除子账号授权
        
        @param request: RemoveChildAccountAuthRequest
        @param headers: RemoveChildAccountAuthHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveChildAccountAuthResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.child_account_name):
            body['ChildAccountName'] = request.child_account_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveChildAccountAuth',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/removeChildAccountAuth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveChildAccountAuthResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveChildAccountAuthResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_child_account_auth(
        self,
        request: ali_genieip__1__0_models.RemoveChildAccountAuthRequest,
    ) -> ali_genieip__1__0_models.RemoveChildAccountAuthResponse:
        """
        @summary 删除子账号授权
        
        @param request: RemoveChildAccountAuthRequest
        @return: RemoveChildAccountAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveChildAccountAuthHeaders()
        return self.remove_child_account_auth_with_options(request, headers, runtime)

    async def remove_child_account_auth_async(
        self,
        request: ali_genieip__1__0_models.RemoveChildAccountAuthRequest,
    ) -> ali_genieip__1__0_models.RemoveChildAccountAuthResponse:
        """
        @summary 删除子账号授权
        
        @param request: RemoveChildAccountAuthRequest
        @return: RemoveChildAccountAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveChildAccountAuthHeaders()
        return await self.remove_child_account_auth_with_options_async(request, headers, runtime)

    def remove_hotel_with_options(
        self,
        request: ali_genieip__1__0_models.RemoveHotelRequest,
        headers: ali_genieip__1__0_models.RemoveHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RemoveHotelResponse:
        """
        @summary 删除酒店项目
        
        @param request: RemoveHotelRequest
        @param headers: RemoveHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveHotelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/removeHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveHotelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveHotelResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_hotel_with_options_async(
        self,
        request: ali_genieip__1__0_models.RemoveHotelRequest,
        headers: ali_genieip__1__0_models.RemoveHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RemoveHotelResponse:
        """
        @summary 删除酒店项目
        
        @param request: RemoveHotelRequest
        @param headers: RemoveHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveHotelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/removeHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveHotelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RemoveHotelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_hotel(
        self,
        request: ali_genieip__1__0_models.RemoveHotelRequest,
    ) -> ali_genieip__1__0_models.RemoveHotelResponse:
        """
        @summary 删除酒店项目
        
        @param request: RemoveHotelRequest
        @return: RemoveHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveHotelHeaders()
        return self.remove_hotel_with_options(request, headers, runtime)

    async def remove_hotel_async(
        self,
        request: ali_genieip__1__0_models.RemoveHotelRequest,
    ) -> ali_genieip__1__0_models.RemoveHotelResponse:
        """
        @summary 删除酒店项目
        
        @param request: RemoveHotelRequest
        @return: RemoveHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RemoveHotelHeaders()
        return await self.remove_hotel_with_options_async(request, headers, runtime)

    def reset_welcome_text_and_music_with_options(
        self,
        request: ali_genieip__1__0_models.ResetWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.ResetWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse:
        """
        @summary 重置欢迎语信息
        
        @param request: ResetWelcomeTextAndMusicRequest
        @param headers: ResetWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/resetWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse(),
                self.execute(params, req, runtime)
            )

    async def reset_welcome_text_and_music_with_options_async(
        self,
        request: ali_genieip__1__0_models.ResetWelcomeTextAndMusicRequest,
        headers: ali_genieip__1__0_models.ResetWelcomeTextAndMusicHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse:
        """
        @summary 重置欢迎语信息
        
        @param request: ResetWelcomeTextAndMusicRequest
        @param headers: ResetWelcomeTextAndMusicHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetWelcomeTextAndMusicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetWelcomeTextAndMusic',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/resetWelcomeTextAndMusic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def reset_welcome_text_and_music(
        self,
        request: ali_genieip__1__0_models.ResetWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse:
        """
        @summary 重置欢迎语信息
        
        @param request: ResetWelcomeTextAndMusicRequest
        @return: ResetWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ResetWelcomeTextAndMusicHeaders()
        return self.reset_welcome_text_and_music_with_options(request, headers, runtime)

    async def reset_welcome_text_and_music_async(
        self,
        request: ali_genieip__1__0_models.ResetWelcomeTextAndMusicRequest,
    ) -> ali_genieip__1__0_models.ResetWelcomeTextAndMusicResponse:
        """
        @summary 重置欢迎语信息
        
        @param request: ResetWelcomeTextAndMusicRequest
        @return: ResetWelcomeTextAndMusicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.ResetWelcomeTextAndMusicHeaders()
        return await self.reset_welcome_text_and_music_with_options_async(request, headers, runtime)

    def room_check_out_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.RoomCheckOutRequest,
        headers: ali_genieip__1__0_models.RoomCheckOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        """
        @summary 退房
        
        @param tmp_req: RoomCheckOutRequest
        @param headers: RoomCheckOutHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RoomCheckOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.RoomCheckOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoomCheckOut',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/roomCheckOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RoomCheckOutResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RoomCheckOutResponse(),
                self.execute(params, req, runtime)
            )

    async def room_check_out_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.RoomCheckOutRequest,
        headers: ali_genieip__1__0_models.RoomCheckOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        """
        @summary 退房
        
        @param tmp_req: RoomCheckOutRequest
        @param headers: RoomCheckOutHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RoomCheckOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.RoomCheckOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoomCheckOut',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/roomCheckOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.RoomCheckOutResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.RoomCheckOutResponse(),
                await self.execute_async(params, req, runtime)
            )

    def room_check_out(
        self,
        request: ali_genieip__1__0_models.RoomCheckOutRequest,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        """
        @summary 退房
        
        @param request: RoomCheckOutRequest
        @return: RoomCheckOutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RoomCheckOutHeaders()
        return self.room_check_out_with_options(request, headers, runtime)

    async def room_check_out_async(
        self,
        request: ali_genieip__1__0_models.RoomCheckOutRequest,
    ) -> ali_genieip__1__0_models.RoomCheckOutResponse:
        """
        @summary 退房
        
        @param request: RoomCheckOutRequest
        @return: RoomCheckOutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.RoomCheckOutHeaders()
        return await self.room_check_out_with_options_async(request, headers, runtime)

    def submit_hotel_order_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.SubmitHotelOrderRequest,
        headers: ali_genieip__1__0_models.SubmitHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        """
        @summary 提交酒店订单
        
        @param tmp_req: SubmitHotelOrderRequest
        @param headers: SubmitHotelOrderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitHotelOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.SubmitHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/submitHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.SubmitHotelOrderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.SubmitHotelOrderResponse(),
                self.execute(params, req, runtime)
            )

    async def submit_hotel_order_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.SubmitHotelOrderRequest,
        headers: ali_genieip__1__0_models.SubmitHotelOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        """
        @summary 提交酒店订单
        
        @param tmp_req: SubmitHotelOrderRequest
        @param headers: SubmitHotelOrderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitHotelOrderResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.SubmitHotelOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.user_info_shrink):
            query['UserInfo'] = request.user_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotelOrder',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/submitHotelOrder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.SubmitHotelOrderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.SubmitHotelOrderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def submit_hotel_order(
        self,
        request: ali_genieip__1__0_models.SubmitHotelOrderRequest,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        """
        @summary 提交酒店订单
        
        @param request: SubmitHotelOrderRequest
        @return: SubmitHotelOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SubmitHotelOrderHeaders()
        return self.submit_hotel_order_with_options(request, headers, runtime)

    async def submit_hotel_order_async(
        self,
        request: ali_genieip__1__0_models.SubmitHotelOrderRequest,
    ) -> ali_genieip__1__0_models.SubmitHotelOrderResponse:
        """
        @summary 提交酒店订单
        
        @param request: SubmitHotelOrderRequest
        @return: SubmitHotelOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SubmitHotelOrderHeaders()
        return await self.submit_hotel_order_with_options_async(request, headers, runtime)

    def sync_device_status_with_ak_with_options(
        self,
        request: ali_genieip__1__0_models.SyncDeviceStatusWithAkRequest,
        headers: ali_genieip__1__0_models.SyncDeviceStatusWithAkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse:
        """
        @summary 同步客控设备状态到主控设备
        
        @param request: SyncDeviceStatusWithAkRequest
        @param headers: SyncDeviceStatusWithAkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncDeviceStatusWithAkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_cn_name):
            body['CategoryCnName'] = request.category_cn_name
        if not UtilClient.is_unset(request.category_en_name):
            body['CategoryEnName'] = request.category_en_name
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.location_cn_name):
            body['LocationCnName'] = request.location_cn_name
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.switch):
            body['Switch'] = request.switch
        if not UtilClient.is_unset(request.fan_speed):
            body['fanSpeed'] = request.fan_speed
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.room_temperature):
            body['roomTemperature'] = request.room_temperature
        if not UtilClient.is_unset(request.temperature):
            body['temperature'] = request.temperature
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncDeviceStatusWithAk',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/syncDeviceStatusWithAk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse(),
                self.execute(params, req, runtime)
            )

    async def sync_device_status_with_ak_with_options_async(
        self,
        request: ali_genieip__1__0_models.SyncDeviceStatusWithAkRequest,
        headers: ali_genieip__1__0_models.SyncDeviceStatusWithAkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse:
        """
        @summary 同步客控设备状态到主控设备
        
        @param request: SyncDeviceStatusWithAkRequest
        @param headers: SyncDeviceStatusWithAkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncDeviceStatusWithAkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_cn_name):
            body['CategoryCnName'] = request.category_cn_name
        if not UtilClient.is_unset(request.category_en_name):
            body['CategoryEnName'] = request.category_en_name
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.location_cn_name):
            body['LocationCnName'] = request.location_cn_name
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.room_no):
            body['RoomNo'] = request.room_no
        if not UtilClient.is_unset(request.switch):
            body['Switch'] = request.switch
        if not UtilClient.is_unset(request.fan_speed):
            body['fanSpeed'] = request.fan_speed
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.room_temperature):
            body['roomTemperature'] = request.room_temperature
        if not UtilClient.is_unset(request.temperature):
            body['temperature'] = request.temperature
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncDeviceStatusWithAk',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/syncDeviceStatusWithAk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse(),
                await self.execute_async(params, req, runtime)
            )

    def sync_device_status_with_ak(
        self,
        request: ali_genieip__1__0_models.SyncDeviceStatusWithAkRequest,
    ) -> ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse:
        """
        @summary 同步客控设备状态到主控设备
        
        @param request: SyncDeviceStatusWithAkRequest
        @return: SyncDeviceStatusWithAkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SyncDeviceStatusWithAkHeaders()
        return self.sync_device_status_with_ak_with_options(request, headers, runtime)

    async def sync_device_status_with_ak_async(
        self,
        request: ali_genieip__1__0_models.SyncDeviceStatusWithAkRequest,
    ) -> ali_genieip__1__0_models.SyncDeviceStatusWithAkResponse:
        """
        @summary 同步客控设备状态到主控设备
        
        @param request: SyncDeviceStatusWithAkRequest
        @return: SyncDeviceStatusWithAkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.SyncDeviceStatusWithAkHeaders()
        return await self.sync_device_status_with_ak_with_options_async(request, headers, runtime)

    def update_basic_info_qawith_options(
        self,
        request: ali_genieip__1__0_models.UpdateBasicInfoQARequest,
        headers: ali_genieip__1__0_models.UpdateBasicInfoQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateBasicInfoQAResponse:
        """
        @summary 修改基础信息问答
        
        @param request: UpdateBasicInfoQARequest
        @param headers: UpdateBasicInfoQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBasicInfoQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_in_time):
            body['CheckInTime'] = request.check_in_time
        if not UtilClient.is_unset(request.check_out_time):
            body['CheckOutTime'] = request.check_out_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_introduction):
            body['HotelIntroduction'] = request.hotel_introduction
        if not UtilClient.is_unset(request.hotel_member):
            body['HotelMember'] = request.hotel_member
        if not UtilClient.is_unset(request.hotel_service):
            body['HotelService'] = request.hotel_service
        if not UtilClient.is_unset(request.parking_expenses):
            body['ParkingExpenses'] = request.parking_expenses
        if not UtilClient.is_unset(request.parking_position):
            body['ParkingPosition'] = request.parking_position
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.wifi_name):
            body['WifiName'] = request.wifi_name
        if not UtilClient.is_unset(request.wifi_password):
            body['WifiPassword'] = request.wifi_password
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateBasicInfoQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateBasicInfoQAResponse(),
                self.execute(params, req, runtime)
            )

    async def update_basic_info_qawith_options_async(
        self,
        request: ali_genieip__1__0_models.UpdateBasicInfoQARequest,
        headers: ali_genieip__1__0_models.UpdateBasicInfoQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateBasicInfoQAResponse:
        """
        @summary 修改基础信息问答
        
        @param request: UpdateBasicInfoQARequest
        @param headers: UpdateBasicInfoQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBasicInfoQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_in_time):
            body['CheckInTime'] = request.check_in_time
        if not UtilClient.is_unset(request.check_out_time):
            body['CheckOutTime'] = request.check_out_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_introduction):
            body['HotelIntroduction'] = request.hotel_introduction
        if not UtilClient.is_unset(request.hotel_member):
            body['HotelMember'] = request.hotel_member
        if not UtilClient.is_unset(request.hotel_service):
            body['HotelService'] = request.hotel_service
        if not UtilClient.is_unset(request.parking_expenses):
            body['ParkingExpenses'] = request.parking_expenses
        if not UtilClient.is_unset(request.parking_position):
            body['ParkingPosition'] = request.parking_position
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.wifi_name):
            body['WifiName'] = request.wifi_name
        if not UtilClient.is_unset(request.wifi_password):
            body['WifiPassword'] = request.wifi_password
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBasicInfoQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateBasicInfoQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateBasicInfoQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateBasicInfoQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_basic_info_qa(
        self,
        request: ali_genieip__1__0_models.UpdateBasicInfoQARequest,
    ) -> ali_genieip__1__0_models.UpdateBasicInfoQAResponse:
        """
        @summary 修改基础信息问答
        
        @param request: UpdateBasicInfoQARequest
        @return: UpdateBasicInfoQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateBasicInfoQAHeaders()
        return self.update_basic_info_qawith_options(request, headers, runtime)

    async def update_basic_info_qa_async(
        self,
        request: ali_genieip__1__0_models.UpdateBasicInfoQARequest,
    ) -> ali_genieip__1__0_models.UpdateBasicInfoQAResponse:
        """
        @summary 修改基础信息问答
        
        @param request: UpdateBasicInfoQARequest
        @return: UpdateBasicInfoQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateBasicInfoQAHeaders()
        return await self.update_basic_info_qawith_options_async(request, headers, runtime)

    def update_custom_qawith_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateCustomQARequest,
        headers: ali_genieip__1__0_models.UpdateCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateCustomQAResponse:
        """
        @summary 修改自定义问答
        
        @param tmp_req: UpdateCustomQARequest
        @param headers: UpdateCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.custom_qaid):
            body['CustomQAId'] = request.custom_qaid
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateCustomQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateCustomQAResponse(),
                self.execute(params, req, runtime)
            )

    async def update_custom_qawith_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateCustomQARequest,
        headers: ali_genieip__1__0_models.UpdateCustomQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateCustomQAResponse:
        """
        @summary 修改自定义问答
        
        @param tmp_req: UpdateCustomQARequest
        @param headers: UpdateCustomQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomQAResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateCustomQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.answers):
            request.answers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.answers, 'Answers', 'json')
        if not UtilClient.is_unset(tmp_req.key_words):
            request.key_words_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.key_words, 'KeyWords', 'json')
        if not UtilClient.is_unset(tmp_req.supplementary_questions):
            request.supplementary_questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supplementary_questions, 'SupplementaryQuestions', 'json')
        body = {}
        if not UtilClient.is_unset(request.answers_shrink):
            body['Answers'] = request.answers_shrink
        if not UtilClient.is_unset(request.custom_qaid):
            body['CustomQAId'] = request.custom_qaid
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.key_words_shrink):
            body['KeyWords'] = request.key_words_shrink
        if not UtilClient.is_unset(request.major_question):
            body['MajorQuestion'] = request.major_question
        if not UtilClient.is_unset(request.supplementary_questions_shrink):
            body['SupplementaryQuestions'] = request.supplementary_questions_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateCustomQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateCustomQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateCustomQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_custom_qa(
        self,
        request: ali_genieip__1__0_models.UpdateCustomQARequest,
    ) -> ali_genieip__1__0_models.UpdateCustomQAResponse:
        """
        @summary 修改自定义问答
        
        @param request: UpdateCustomQARequest
        @return: UpdateCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateCustomQAHeaders()
        return self.update_custom_qawith_options(request, headers, runtime)

    async def update_custom_qa_async(
        self,
        request: ali_genieip__1__0_models.UpdateCustomQARequest,
    ) -> ali_genieip__1__0_models.UpdateCustomQAResponse:
        """
        @summary 修改自定义问答
        
        @param request: UpdateCustomQARequest
        @return: UpdateCustomQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateCustomQAHeaders()
        return await self.update_custom_qawith_options_async(request, headers, runtime)

    def update_hotel_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelRequest,
        headers: ali_genieip__1__0_models.UpdateHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelResponse:
        """
        @summary 修改酒店项目
        
        @param tmp_req: UpdateHotelRequest
        @param headers: UpdateHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelResponse(),
                self.execute(params, req, runtime)
            )

    async def update_hotel_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelRequest,
        headers: ali_genieip__1__0_models.UpdateHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelResponse:
        """
        @summary 修改酒店项目
        
        @param tmp_req: UpdateHotelRequest
        @param headers: UpdateHotelHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_pks):
            request.related_pks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_pks, 'RelatedPks', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.est_open_time):
            body['EstOpenTime'] = request.est_open_time
        if not UtilClient.is_unset(request.hotel_address):
            body['HotelAddress'] = request.hotel_address
        if not UtilClient.is_unset(request.hotel_email):
            body['HotelEmail'] = request.hotel_email
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.hotel_name):
            body['HotelName'] = request.hotel_name
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.related_pks_shrink):
            body['RelatedPks'] = request.related_pks_shrink
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.room_num):
            body['RoomNum'] = request.room_num
        if not UtilClient.is_unset(request.tb_open_id):
            body['TbOpenId'] = request.tb_open_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotel',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_hotel(
        self,
        request: ali_genieip__1__0_models.UpdateHotelRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelResponse:
        """
        @summary 修改酒店项目
        
        @param request: UpdateHotelRequest
        @return: UpdateHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelHeaders()
        return self.update_hotel_with_options(request, headers, runtime)

    async def update_hotel_async(
        self,
        request: ali_genieip__1__0_models.UpdateHotelRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelResponse:
        """
        @summary 修改酒店项目
        
        @param request: UpdateHotelRequest
        @return: UpdateHotelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelHeaders()
        return await self.update_hotel_with_options_async(request, headers, runtime)

    def update_hotel_alarm_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.UpdateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        """
        @summary 修改酒店闹钟
        
        @param tmp_req: UpdateHotelAlarmRequest
        @param headers: UpdateHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
                self.execute(params, req, runtime)
            )

    async def update_hotel_alarm_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
        headers: ali_genieip__1__0_models.UpdateHotelAlarmHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        """
        @summary 修改酒店闹钟
        
        @param tmp_req: UpdateHotelAlarmRequest
        @param headers: UpdateHotelAlarmHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelAlarmResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelAlarmShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarms):
            request.alarms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarms, 'Alarms', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_info):
            request.schedule_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_info, 'ScheduleInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.alarms_shrink):
            body['Alarms'] = request.alarms_shrink
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.schedule_info_shrink):
            body['ScheduleInfo'] = request.schedule_info_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelAlarm',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelAlarm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelAlarmResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_hotel_alarm(
        self,
        request: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        """
        @summary 修改酒店闹钟
        
        @param request: UpdateHotelAlarmRequest
        @return: UpdateHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelAlarmHeaders()
        return self.update_hotel_alarm_with_options(request, headers, runtime)

    async def update_hotel_alarm_async(
        self,
        request: ali_genieip__1__0_models.UpdateHotelAlarmRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelAlarmResponse:
        """
        @summary 修改酒店闹钟
        
        @param request: UpdateHotelAlarmRequest
        @return: UpdateHotelAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelAlarmHeaders()
        return await self.update_hotel_alarm_with_options_async(request, headers, runtime)

    def update_hotel_scene_book_item_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.UpdateHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订编辑
        
        @param tmp_req: UpdateHotelSceneBookItemRequest
        @param headers: UpdateHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelSceneBookItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_book_req):
            request.update_hotel_scene_book_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_book_req, 'UpdateHotelSceneBookReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_book_req_shrink):
            query['UpdateHotelSceneBookReq'] = request.update_hotel_scene_book_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse(),
                self.execute(params, req, runtime)
            )

    async def update_hotel_scene_book_item_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelSceneBookItemRequest,
        headers: ali_genieip__1__0_models.UpdateHotelSceneBookItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订编辑
        
        @param tmp_req: UpdateHotelSceneBookItemRequest
        @param headers: UpdateHotelSceneBookItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelSceneBookItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneBookItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_book_req):
            request.update_hotel_scene_book_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_book_req, 'UpdateHotelSceneBookReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_book_req_shrink):
            query['UpdateHotelSceneBookReq'] = request.update_hotel_scene_book_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelSceneBookItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelSceneBookItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_hotel_scene_book_item(
        self,
        request: ali_genieip__1__0_models.UpdateHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订编辑
        
        @param request: UpdateHotelSceneBookItemRequest
        @return: UpdateHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneBookItemHeaders()
        return self.update_hotel_scene_book_item_with_options(request, headers, runtime)

    async def update_hotel_scene_book_item_async(
        self,
        request: ali_genieip__1__0_models.UpdateHotelSceneBookItemRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneBookItemResponse:
        """
        @summary 酒店场景预订编辑
        
        @param request: UpdateHotelSceneBookItemRequest
        @return: UpdateHotelSceneBookItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneBookItemHeaders()
        return await self.update_hotel_scene_book_item_with_options_async(request, headers, runtime)

    def update_hotel_scene_item_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.UpdateHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneItemResponse:
        """
        @summary 酒店场景修改（开启/关闭/编辑）
        
        @param tmp_req: UpdateHotelSceneItemRequest
        @param headers: UpdateHotelSceneItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelSceneItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_operate_req):
            request.update_hotel_scene_operate_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_operate_req, 'UpdateHotelSceneOperateReq', 'json')
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_req):
            request.update_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_req, 'UpdateHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_operate_req_shrink):
            query['UpdateHotelSceneOperateReq'] = request.update_hotel_scene_operate_req_shrink
        if not UtilClient.is_unset(request.update_hotel_scene_req_shrink):
            query['UpdateHotelSceneReq'] = request.update_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneItemResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneItemResponse(),
                self.execute(params, req, runtime)
            )

    async def update_hotel_scene_item_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateHotelSceneItemRequest,
        headers: ali_genieip__1__0_models.UpdateHotelSceneItemHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneItemResponse:
        """
        @summary 酒店场景修改（开启/关闭/编辑）
        
        @param tmp_req: UpdateHotelSceneItemRequest
        @param headers: UpdateHotelSceneItemHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHotelSceneItemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateHotelSceneItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_operate_req):
            request.update_hotel_scene_operate_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_operate_req, 'UpdateHotelSceneOperateReq', 'json')
        if not UtilClient.is_unset(tmp_req.update_hotel_scene_req):
            request.update_hotel_scene_req_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_hotel_scene_req, 'UpdateHotelSceneReq', 'json')
        query = {}
        if not UtilClient.is_unset(request.update_hotel_scene_operate_req_shrink):
            query['UpdateHotelSceneOperateReq'] = request.update_hotel_scene_operate_req_shrink
        if not UtilClient.is_unset(request.update_hotel_scene_req_shrink):
            query['UpdateHotelSceneReq'] = request.update_hotel_scene_req_shrink
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHotelSceneItem',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateHotelSceneItem',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneItemResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateHotelSceneItemResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_hotel_scene_item(
        self,
        request: ali_genieip__1__0_models.UpdateHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneItemResponse:
        """
        @summary 酒店场景修改（开启/关闭/编辑）
        
        @param request: UpdateHotelSceneItemRequest
        @return: UpdateHotelSceneItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneItemHeaders()
        return self.update_hotel_scene_item_with_options(request, headers, runtime)

    async def update_hotel_scene_item_async(
        self,
        request: ali_genieip__1__0_models.UpdateHotelSceneItemRequest,
    ) -> ali_genieip__1__0_models.UpdateHotelSceneItemResponse:
        """
        @summary 酒店场景修改（开启/关闭/编辑）
        
        @param request: UpdateHotelSceneItemRequest
        @return: UpdateHotelSceneItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateHotelSceneItemHeaders()
        return await self.update_hotel_scene_item_with_options_async(request, headers, runtime)

    def update_message_template_with_options(
        self,
        request: ali_genieip__1__0_models.UpdateMessageTemplateRequest,
        headers: ali_genieip__1__0_models.UpdateMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateMessageTemplateResponse:
        """
        @summary 更新消息通知模板
        
        @param request: UpdateMessageTemplateRequest
        @param headers: UpdateMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateMessageTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateMessageTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def update_message_template_with_options_async(
        self,
        request: ali_genieip__1__0_models.UpdateMessageTemplateRequest,
        headers: ali_genieip__1__0_models.UpdateMessageTemplateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateMessageTemplateResponse:
        """
        @summary 更新消息通知模板
        
        @param request: UpdateMessageTemplateRequest
        @param headers: UpdateMessageTemplateHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMessageTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_detail):
            body['TemplateDetail'] = request.template_detail
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMessageTemplate',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateMessageTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateMessageTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateMessageTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_message_template(
        self,
        request: ali_genieip__1__0_models.UpdateMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.UpdateMessageTemplateResponse:
        """
        @summary 更新消息通知模板
        
        @param request: UpdateMessageTemplateRequest
        @return: UpdateMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateMessageTemplateHeaders()
        return self.update_message_template_with_options(request, headers, runtime)

    async def update_message_template_async(
        self,
        request: ali_genieip__1__0_models.UpdateMessageTemplateRequest,
    ) -> ali_genieip__1__0_models.UpdateMessageTemplateResponse:
        """
        @summary 更新消息通知模板
        
        @param request: UpdateMessageTemplateRequest
        @return: UpdateMessageTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateMessageTemplateHeaders()
        return await self.update_message_template_with_options_async(request, headers, runtime)

    def update_rcu_scene_with_options(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateRcuSceneRequest,
        headers: ali_genieip__1__0_models.UpdateRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateRcuSceneResponse:
        """
        @summary 修改酒店自定义rcu场景
        
        @param tmp_req: UpdateRcuSceneRequest
        @param headers: UpdateRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRcuSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateRcuSceneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateRcuSceneResponse(),
                self.execute(params, req, runtime)
            )

    async def update_rcu_scene_with_options_async(
        self,
        tmp_req: ali_genieip__1__0_models.UpdateRcuSceneRequest,
        headers: ali_genieip__1__0_models.UpdateRcuSceneHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateRcuSceneResponse:
        """
        @summary 修改酒店自定义rcu场景
        
        @param tmp_req: UpdateRcuSceneRequest
        @param headers: UpdateRcuSceneHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRcuSceneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieip__1__0_models.UpdateRcuSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_relation_ext_dto):
            request.scene_relation_ext_dtoshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_relation_ext_dto, 'SceneRelationExtDTO', 'json')
        body = {}
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_relation_ext_dtoshrink):
            body['SceneRelationExtDTO'] = request.scene_relation_ext_dtoshrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRcuScene',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateRcuScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateRcuSceneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateRcuSceneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_rcu_scene(
        self,
        request: ali_genieip__1__0_models.UpdateRcuSceneRequest,
    ) -> ali_genieip__1__0_models.UpdateRcuSceneResponse:
        """
        @summary 修改酒店自定义rcu场景
        
        @param request: UpdateRcuSceneRequest
        @return: UpdateRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateRcuSceneHeaders()
        return self.update_rcu_scene_with_options(request, headers, runtime)

    async def update_rcu_scene_async(
        self,
        request: ali_genieip__1__0_models.UpdateRcuSceneRequest,
    ) -> ali_genieip__1__0_models.UpdateRcuSceneResponse:
        """
        @summary 修改酒店自定义rcu场景
        
        @param request: UpdateRcuSceneRequest
        @return: UpdateRcuSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateRcuSceneHeaders()
        return await self.update_rcu_scene_with_options_async(request, headers, runtime)

    def update_service_qawith_options(
        self,
        request: ali_genieip__1__0_models.UpdateServiceQARequest,
        headers: ali_genieip__1__0_models.UpdateServiceQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateServiceQAResponse:
        """
        @summary 修改服务设施问答
        
        @param request: UpdateServiceQARequest
        @param headers: UpdateServiceQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer):
            body['Answer'] = request.answer
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.service_qaid):
            body['ServiceQAId'] = request.service_qaid
        if not UtilClient.is_unset(request.is_active):
            body['isActive'] = request.is_active
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateServiceQAResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateServiceQAResponse(),
                self.execute(params, req, runtime)
            )

    async def update_service_qawith_options_async(
        self,
        request: ali_genieip__1__0_models.UpdateServiceQARequest,
        headers: ali_genieip__1__0_models.UpdateServiceQAHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateServiceQAResponse:
        """
        @summary 修改服务设施问答
        
        @param request: UpdateServiceQARequest
        @param headers: UpdateServiceQAHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceQAResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer):
            body['Answer'] = request.answer
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.service_qaid):
            body['ServiceQAId'] = request.service_qaid
        if not UtilClient.is_unset(request.is_active):
            body['isActive'] = request.is_active
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceQA',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateServiceQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateServiceQAResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateServiceQAResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_service_qa(
        self,
        request: ali_genieip__1__0_models.UpdateServiceQARequest,
    ) -> ali_genieip__1__0_models.UpdateServiceQAResponse:
        """
        @summary 修改服务设施问答
        
        @param request: UpdateServiceQARequest
        @return: UpdateServiceQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateServiceQAHeaders()
        return self.update_service_qawith_options(request, headers, runtime)

    async def update_service_qa_async(
        self,
        request: ali_genieip__1__0_models.UpdateServiceQARequest,
    ) -> ali_genieip__1__0_models.UpdateServiceQAResponse:
        """
        @summary 修改服务设施问答
        
        @param request: UpdateServiceQARequest
        @return: UpdateServiceQAResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateServiceQAHeaders()
        return await self.update_service_qawith_options_async(request, headers, runtime)

    def update_ticket_with_options(
        self,
        request: ali_genieip__1__0_models.UpdateTicketRequest,
        headers: ali_genieip__1__0_models.UpdateTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateTicketResponse:
        """
        @summary 修改工单
        
        @param request: UpdateTicketRequest
        @param headers: UpdateTicketHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_key):
            body['GroupKey'] = request.group_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTicket',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateTicket',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateTicketResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateTicketResponse(),
                self.execute(params, req, runtime)
            )

    async def update_ticket_with_options_async(
        self,
        request: ali_genieip__1__0_models.UpdateTicketRequest,
        headers: ali_genieip__1__0_models.UpdateTicketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieip__1__0_models.UpdateTicketResponse:
        """
        @summary 修改工单
        
        @param request: UpdateTicketRequest
        @param headers: UpdateTicketHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_key):
            body['GroupKey'] = request.group_key
        if not UtilClient.is_unset(request.hotel_id):
            body['HotelId'] = request.hotel_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTicket',
            version='ip_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/ip/updateTicket',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateTicketResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ali_genieip__1__0_models.UpdateTicketResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_ticket(
        self,
        request: ali_genieip__1__0_models.UpdateTicketRequest,
    ) -> ali_genieip__1__0_models.UpdateTicketResponse:
        """
        @summary 修改工单
        
        @param request: UpdateTicketRequest
        @return: UpdateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateTicketHeaders()
        return self.update_ticket_with_options(request, headers, runtime)

    async def update_ticket_async(
        self,
        request: ali_genieip__1__0_models.UpdateTicketRequest,
    ) -> ali_genieip__1__0_models.UpdateTicketResponse:
        """
        @summary 修改工单
        
        @param request: UpdateTicketRequest
        @return: UpdateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieip__1__0_models.UpdateTicketHeaders()
        return await self.update_ticket_with_options_async(request, headers, runtime)
