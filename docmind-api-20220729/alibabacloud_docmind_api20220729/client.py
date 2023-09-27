# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_docmind_api20220729 import models as docmind_api_20220729_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


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
            'ap-northeast-1': 'docmind-api.aliyuncs.com',
            'ap-northeast-2-pop': 'docmind-api.aliyuncs.com',
            'ap-south-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-1': 'docmind-api.aliyuncs.com',
            'ap-southeast-2': 'docmind-api.aliyuncs.com',
            'ap-southeast-3': 'docmind-api.aliyuncs.com',
            'ap-southeast-5': 'docmind-api.aliyuncs.com',
            'cn-beijing': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-beijing-gov-1': 'docmind-api.aliyuncs.com',
            'cn-beijing-nu16-b01': 'docmind-api.aliyuncs.com',
            'cn-chengdu': 'docmind-api.aliyuncs.com',
            'cn-edge-1': 'docmind-api.aliyuncs.com',
            'cn-fujian': 'docmind-api.aliyuncs.com',
            'cn-haidian-cm12-c01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-finance': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'docmind-api.aliyuncs.com',
            'cn-hangzhou-test-306': 'docmind-api.aliyuncs.com',
            'cn-hongkong': 'docmind-api.aliyuncs.com',
            'cn-hongkong-finance-pop': 'docmind-api.aliyuncs.com',
            'cn-huhehaote': 'docmind-api.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'docmind-api.aliyuncs.com',
            'cn-north-2-gov-1': 'docmind-api.aliyuncs.com',
            'cn-qingdao': 'docmind-api.aliyuncs.com',
            'cn-qingdao-nebula': 'docmind-api.aliyuncs.com',
            'cn-shanghai': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et15-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-et2-b01': 'docmind-api.aliyuncs.com',
            'cn-shanghai-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shanghai-inner': 'docmind-api.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-finance-1': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-inner': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'docmind-api.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'docmind-api.aliyuncs.com',
            'cn-wuhan': 'docmind-api.aliyuncs.com',
            'cn-wulanchabu': 'docmind-api.aliyuncs.com',
            'cn-yushanfang': 'docmind-api.aliyuncs.com',
            'cn-zhangbei': 'docmind-api.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou': 'docmind-api.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'docmind-api.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'docmind-api.aliyuncs.com',
            'eu-central-1': 'docmind-api.aliyuncs.com',
            'eu-west-1': 'docmind-api.aliyuncs.com',
            'eu-west-1-oxs': 'docmind-api.aliyuncs.com',
            'me-east-1': 'docmind-api.aliyuncs.com',
            'rus-west-1-pop': 'docmind-api.aliyuncs.com',
            'us-east-1': 'docmind-api.aliyuncs.com',
            'us-west-1': 'docmind-api.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('docmind-api', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def extract_feedback_with_options(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feedback_url):
            query['FeedbackUrl'] = request.feedback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractFeedback',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.ExtractFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_feedback_with_options_async(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feedback_url):
            query['FeedbackUrl'] = request.feedback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractFeedback',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.ExtractFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_feedback(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackRequest,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_feedback_with_options(request, runtime)

    async def extract_feedback_async(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackRequest,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_feedback_with_options_async(request, runtime)

    def extract_feedback_advance(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        extract_feedback_req = docmind_api_20220729_models.ExtractFeedbackRequest()
        OpenApiUtilClient.convert(request, extract_feedback_req)
        if not UtilClient.is_unset(request.feedback_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.feedback_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            extract_feedback_req.feedback_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_feedback_resp = self.extract_feedback_with_options(extract_feedback_req, runtime)
        return extract_feedback_resp

    async def extract_feedback_advance_async(
        self,
        request: docmind_api_20220729_models.ExtractFeedbackAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ExtractFeedbackResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        extract_feedback_req = docmind_api_20220729_models.ExtractFeedbackRequest()
        OpenApiUtilClient.convert(request, extract_feedback_req)
        if not UtilClient.is_unset(request.feedback_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.feedback_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            extract_feedback_req.feedback_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_feedback_resp = await self.extract_feedback_with_options_async(extract_feedback_req, runtime)
        return extract_feedback_resp

    def get_single_document_extract_result_with_options(
        self,
        request: docmind_api_20220729_models.GetSingleDocumentExtractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.GetSingleDocumentExtractResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSingleDocumentExtractResult',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.GetSingleDocumentExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_single_document_extract_result_with_options_async(
        self,
        request: docmind_api_20220729_models.GetSingleDocumentExtractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.GetSingleDocumentExtractResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSingleDocumentExtractResult',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.GetSingleDocumentExtractResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_single_document_extract_result(
        self,
        request: docmind_api_20220729_models.GetSingleDocumentExtractResultRequest,
    ) -> docmind_api_20220729_models.GetSingleDocumentExtractResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_single_document_extract_result_with_options(request, runtime)

    async def get_single_document_extract_result_async(
        self,
        request: docmind_api_20220729_models.GetSingleDocumentExtractResultRequest,
    ) -> docmind_api_20220729_models.GetSingleDocumentExtractResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_single_document_extract_result_with_options_async(request, runtime)

    def re_classify_trade_document_extract_with_options(
        self,
        tmp_req: docmind_api_20220729_models.ReClassifyTradeDocumentExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse:
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220729_models.ReClassifyTradeDocumentExtractShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page_update_info_models):
            request.page_update_info_models_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_update_info_models, 'PageUpdateInfoModels', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_update_info_models_shrink):
            query['PageUpdateInfoModels'] = request.page_update_info_models_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReClassifyTradeDocumentExtract',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_classify_trade_document_extract_with_options_async(
        self,
        tmp_req: docmind_api_20220729_models.ReClassifyTradeDocumentExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse:
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220729_models.ReClassifyTradeDocumentExtractShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page_update_info_models):
            request.page_update_info_models_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_update_info_models, 'PageUpdateInfoModels', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_update_info_models_shrink):
            query['PageUpdateInfoModels'] = request.page_update_info_models_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReClassifyTradeDocumentExtract',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_classify_trade_document_extract(
        self,
        request: docmind_api_20220729_models.ReClassifyTradeDocumentExtractRequest,
    ) -> docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_classify_trade_document_extract_with_options(request, runtime)

    async def re_classify_trade_document_extract_async(
        self,
        request: docmind_api_20220729_models.ReClassifyTradeDocumentExtractRequest,
    ) -> docmind_api_20220729_models.ReClassifyTradeDocumentExtractResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_classify_trade_document_extract_with_options_async(request, runtime)

    def retry_trade_document_extract_with_options(
        self,
        request: docmind_api_20220729_models.RetryTradeDocumentExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.RetryTradeDocumentExtractResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryTradeDocumentExtract',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.RetryTradeDocumentExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_trade_document_extract_with_options_async(
        self,
        request: docmind_api_20220729_models.RetryTradeDocumentExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.RetryTradeDocumentExtractResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryTradeDocumentExtract',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.RetryTradeDocumentExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_trade_document_extract(
        self,
        request: docmind_api_20220729_models.RetryTradeDocumentExtractRequest,
    ) -> docmind_api_20220729_models.RetryTradeDocumentExtractResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_trade_document_extract_with_options(request, runtime)

    async def retry_trade_document_extract_async(
        self,
        request: docmind_api_20220729_models.RetryTradeDocumentExtractRequest,
    ) -> docmind_api_20220729_models.RetryTradeDocumentExtractResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_trade_document_extract_with_options_async(request, runtime)

    def submit_air_waybill_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAirWaybillExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_air_waybill_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAirWaybillExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_air_waybill_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_air_waybill_extract_job_with_options(request, runtime)

    async def submit_air_waybill_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_air_waybill_extract_job_with_options_async(request, runtime)

    def submit_air_waybill_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_air_waybill_extract_job_req = docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_air_waybill_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_air_waybill_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_air_waybill_extract_job_resp = self.submit_air_waybill_extract_job_with_options(submit_air_waybill_extract_job_req, runtime)
        return submit_air_waybill_extract_job_resp

    async def submit_air_waybill_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitAirWaybillExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitAirWaybillExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_air_waybill_extract_job_req = docmind_api_20220729_models.SubmitAirWaybillExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_air_waybill_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_air_waybill_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_air_waybill_extract_job_resp = await self.submit_air_waybill_extract_job_with_options_async(submit_air_waybill_extract_job_req, runtime)
        return submit_air_waybill_extract_job_resp

    def submit_bill_of_lading_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBillOfLadingExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_bill_of_lading_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBillOfLadingExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_bill_of_lading_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_bill_of_lading_extract_job_with_options(request, runtime)

    async def submit_bill_of_lading_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_bill_of_lading_extract_job_with_options_async(request, runtime)

    def submit_bill_of_lading_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_bill_of_lading_extract_job_req = docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_bill_of_lading_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_bill_of_lading_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_bill_of_lading_extract_job_resp = self.submit_bill_of_lading_extract_job_with_options(submit_bill_of_lading_extract_job_req, runtime)
        return submit_bill_of_lading_extract_job_resp

    async def submit_bill_of_lading_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitBillOfLadingExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBillOfLadingExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_bill_of_lading_extract_job_req = docmind_api_20220729_models.SubmitBillOfLadingExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_bill_of_lading_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_bill_of_lading_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_bill_of_lading_extract_job_resp = await self.submit_bill_of_lading_extract_job_with_options_async(submit_bill_of_lading_extract_job_req, runtime)
        return submit_bill_of_lading_extract_job_resp

    def submit_booking_note_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBookingNoteExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_booking_note_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBookingNoteExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_booking_note_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_booking_note_extract_job_with_options(request, runtime)

    async def submit_booking_note_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_booking_note_extract_job_with_options_async(request, runtime)

    def submit_booking_note_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_booking_note_extract_job_req = docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_booking_note_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_booking_note_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_booking_note_extract_job_resp = self.submit_booking_note_extract_job_with_options(submit_booking_note_extract_job_req, runtime)
        return submit_booking_note_extract_job_resp

    async def submit_booking_note_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitBookingNoteExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitBookingNoteExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_booking_note_extract_job_req = docmind_api_20220729_models.SubmitBookingNoteExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_booking_note_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_booking_note_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_booking_note_extract_job_resp = await self.submit_booking_note_extract_job_with_options_async(submit_booking_note_extract_job_req, runtime)
        return submit_booking_note_extract_job_resp

    def submit_certificate_of_origin_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCertificateOfOriginExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_certificate_of_origin_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCertificateOfOriginExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_certificate_of_origin_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_certificate_of_origin_extract_job_with_options(request, runtime)

    async def submit_certificate_of_origin_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_certificate_of_origin_extract_job_with_options_async(request, runtime)

    def submit_certificate_of_origin_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_certificate_of_origin_extract_job_req = docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_certificate_of_origin_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_certificate_of_origin_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_certificate_of_origin_extract_job_resp = self.submit_certificate_of_origin_extract_job_with_options(submit_certificate_of_origin_extract_job_req, runtime)
        return submit_certificate_of_origin_extract_job_resp

    async def submit_certificate_of_origin_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_certificate_of_origin_extract_job_req = docmind_api_20220729_models.SubmitCertificateOfOriginExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_certificate_of_origin_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_certificate_of_origin_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_certificate_of_origin_extract_job_resp = await self.submit_certificate_of_origin_extract_job_with_options_async(submit_certificate_of_origin_extract_job_req, runtime)
        return submit_certificate_of_origin_extract_job_resp

    def submit_container_load_plan_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitContainerLoadPlanExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_container_load_plan_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitContainerLoadPlanExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_container_load_plan_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_container_load_plan_extract_job_with_options(request, runtime)

    async def submit_container_load_plan_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_container_load_plan_extract_job_with_options_async(request, runtime)

    def submit_container_load_plan_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_container_load_plan_extract_job_req = docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_container_load_plan_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_container_load_plan_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_container_load_plan_extract_job_resp = self.submit_container_load_plan_extract_job_with_options(submit_container_load_plan_extract_job_req, runtime)
        return submit_container_load_plan_extract_job_resp

    async def submit_container_load_plan_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_container_load_plan_extract_job_req = docmind_api_20220729_models.SubmitContainerLoadPlanExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_container_load_plan_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_container_load_plan_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_container_load_plan_extract_job_resp = await self.submit_container_load_plan_extract_job_with_options_async(submit_container_load_plan_extract_job_req, runtime)
        return submit_container_load_plan_extract_job_resp

    def submit_export_declaration_sheet_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitExportDeclarationSheetExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_export_declaration_sheet_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitExportDeclarationSheetExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_export_declaration_sheet_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_export_declaration_sheet_extract_job_with_options(request, runtime)

    async def submit_export_declaration_sheet_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_export_declaration_sheet_extract_job_with_options_async(request, runtime)

    def submit_export_declaration_sheet_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_export_declaration_sheet_extract_job_req = docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_export_declaration_sheet_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_export_declaration_sheet_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_export_declaration_sheet_extract_job_resp = self.submit_export_declaration_sheet_extract_job_with_options(submit_export_declaration_sheet_extract_job_req, runtime)
        return submit_export_declaration_sheet_extract_job_resp

    async def submit_export_declaration_sheet_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_export_declaration_sheet_extract_job_req = docmind_api_20220729_models.SubmitExportDeclarationSheetExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_export_declaration_sheet_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_export_declaration_sheet_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_export_declaration_sheet_extract_job_resp = await self.submit_export_declaration_sheet_extract_job_with_options_async(submit_export_declaration_sheet_extract_job_req, runtime)
        return submit_export_declaration_sheet_extract_job_resp

    def submit_general_contract_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contract_model):
            query['ContractModel'] = request.contract_model
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitGeneralContractExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_general_contract_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contract_model):
            query['ContractModel'] = request.contract_model
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitGeneralContractExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_general_contract_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_general_contract_extract_job_with_options(request, runtime)

    async def submit_general_contract_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_general_contract_extract_job_with_options_async(request, runtime)

    def submit_general_contract_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_general_contract_extract_job_req = docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_general_contract_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_general_contract_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_general_contract_extract_job_resp = self.submit_general_contract_extract_job_with_options(submit_general_contract_extract_job_req, runtime)
        return submit_general_contract_extract_job_resp

    async def submit_general_contract_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitGeneralContractExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitGeneralContractExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_general_contract_extract_job_req = docmind_api_20220729_models.SubmitGeneralContractExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_general_contract_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_general_contract_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_general_contract_extract_job_resp = await self.submit_general_contract_extract_job_with_options_async(submit_general_contract_extract_job_req, runtime)
        return submit_general_contract_extract_job_resp

    def submit_import_declaration_sheet_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitImportDeclarationSheetExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_import_declaration_sheet_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitImportDeclarationSheetExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_import_declaration_sheet_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_import_declaration_sheet_extract_job_with_options(request, runtime)

    async def submit_import_declaration_sheet_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_import_declaration_sheet_extract_job_with_options_async(request, runtime)

    def submit_import_declaration_sheet_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_import_declaration_sheet_extract_job_req = docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_import_declaration_sheet_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_import_declaration_sheet_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_import_declaration_sheet_extract_job_resp = self.submit_import_declaration_sheet_extract_job_with_options(submit_import_declaration_sheet_extract_job_req, runtime)
        return submit_import_declaration_sheet_extract_job_resp

    async def submit_import_declaration_sheet_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_import_declaration_sheet_extract_job_req = docmind_api_20220729_models.SubmitImportDeclarationSheetExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_import_declaration_sheet_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_import_declaration_sheet_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_import_declaration_sheet_extract_job_resp = await self.submit_import_declaration_sheet_extract_job_with_options_async(submit_import_declaration_sheet_extract_job_req, runtime)
        return submit_import_declaration_sheet_extract_job_resp

    def submit_invoice_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInvoiceExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitInvoiceExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_invoice_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitInvoiceExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitInvoiceExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_invoice_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_invoice_extract_job_with_options(request, runtime)

    async def submit_invoice_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_invoice_extract_job_with_options_async(request, runtime)

    def submit_invoice_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_invoice_extract_job_req = docmind_api_20220729_models.SubmitInvoiceExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_invoice_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_invoice_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_invoice_extract_job_resp = self.submit_invoice_extract_job_with_options(submit_invoice_extract_job_req, runtime)
        return submit_invoice_extract_job_resp

    async def submit_invoice_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitInvoiceExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitInvoiceExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_invoice_extract_job_req = docmind_api_20220729_models.SubmitInvoiceExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_invoice_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_invoice_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_invoice_extract_job_resp = await self.submit_invoice_extract_job_with_options_async(submit_invoice_extract_job_req, runtime)
        return submit_invoice_extract_job_resp

    def submit_packing_list_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPackingListExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitPackingListExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_packing_list_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPackingListExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitPackingListExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_packing_list_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_packing_list_extract_job_with_options(request, runtime)

    async def submit_packing_list_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_packing_list_extract_job_with_options_async(request, runtime)

    def submit_packing_list_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_packing_list_extract_job_req = docmind_api_20220729_models.SubmitPackingListExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_packing_list_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_packing_list_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_packing_list_extract_job_resp = self.submit_packing_list_extract_job_with_options(submit_packing_list_extract_job_req, runtime)
        return submit_packing_list_extract_job_resp

    async def submit_packing_list_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitPackingListExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitPackingListExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_packing_list_extract_job_req = docmind_api_20220729_models.SubmitPackingListExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_packing_list_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_packing_list_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_packing_list_extract_job_resp = await self.submit_packing_list_extract_job_with_options_async(submit_packing_list_extract_job_req, runtime)
        return submit_packing_list_extract_job_resp

    def submit_sales_confirmation_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSalesConfirmationExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sales_confirmation_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSalesConfirmationExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sales_confirmation_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sales_confirmation_extract_job_with_options(request, runtime)

    async def submit_sales_confirmation_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sales_confirmation_extract_job_with_options_async(request, runtime)

    def submit_sales_confirmation_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_sales_confirmation_extract_job_req = docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_sales_confirmation_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_sales_confirmation_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_sales_confirmation_extract_job_resp = self.submit_sales_confirmation_extract_job_with_options(submit_sales_confirmation_extract_job_req, runtime)
        return submit_sales_confirmation_extract_job_resp

    async def submit_sales_confirmation_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitSalesConfirmationExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSalesConfirmationExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_sales_confirmation_extract_job_req = docmind_api_20220729_models.SubmitSalesConfirmationExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_sales_confirmation_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_sales_confirmation_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_sales_confirmation_extract_job_resp = await self.submit_sales_confirmation_extract_job_with_options_async(submit_sales_confirmation_extract_job_req, runtime)
        return submit_sales_confirmation_extract_job_resp

    def submit_sea_waybill_extract_job_with_options(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSeaWaybillExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sea_waybill_extract_job_with_options_async(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.parser_config_id):
            query['ParserConfigId'] = request.parser_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSeaWaybillExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sea_waybill_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sea_waybill_extract_job_with_options(request, runtime)

    async def submit_sea_waybill_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sea_waybill_extract_job_with_options_async(request, runtime)

    def submit_sea_waybill_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_sea_waybill_extract_job_req = docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_sea_waybill_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_sea_waybill_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_sea_waybill_extract_job_resp = self.submit_sea_waybill_extract_job_with_options(submit_sea_waybill_extract_job_req, runtime)
        return submit_sea_waybill_extract_job_resp

    async def submit_sea_waybill_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitSeaWaybillExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitSeaWaybillExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_sea_waybill_extract_job_req = docmind_api_20220729_models.SubmitSeaWaybillExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_sea_waybill_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_sea_waybill_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_sea_waybill_extract_job_resp = await self.submit_sea_waybill_extract_job_with_options_async(submit_sea_waybill_extract_job_req, runtime)
        return submit_sea_waybill_extract_job_resp

    def submit_trade_document_package_extract_job_with_options(
        self,
        tmp_req: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTradeDocumentPackageExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_trade_document_package_extract_job_with_options_async(
        self,
        tmp_req: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        UtilClient.validate_model(tmp_req)
        request = docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_extraction_range):
            request.custom_extraction_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_extraction_range, 'CustomExtractionRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_extraction_range_shrink):
            query['CustomExtractionRange'] = request.custom_extraction_range_shrink
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_name_extension):
            query['FileNameExtension'] = request.file_name_extension
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTradeDocumentPackageExtractJob',
            version='2022-07-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_trade_document_package_extract_job(
        self,
        request: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_trade_document_package_extract_job_with_options(request, runtime)

    async def submit_trade_document_package_extract_job_async(
        self,
        request: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_trade_document_package_extract_job_with_options_async(request, runtime)

    def submit_trade_document_package_extract_job_advance(
        self,
        request: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_trade_document_package_extract_job_req = docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_trade_document_package_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            submit_trade_document_package_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_trade_document_package_extract_job_resp = self.submit_trade_document_package_extract_job_with_options(submit_trade_document_package_extract_job_req, runtime)
        return submit_trade_document_package_extract_job_resp

    async def submit_trade_document_package_extract_job_advance_async(
        self,
        request: docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='docmind-api',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        submit_trade_document_package_extract_job_req = docmind_api_20220729_models.SubmitTradeDocumentPackageExtractJobRequest()
        OpenApiUtilClient.convert(request, submit_trade_document_package_extract_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            submit_trade_document_package_extract_job_req.file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        submit_trade_document_package_extract_job_resp = await self.submit_trade_document_package_extract_job_with_options_async(submit_trade_document_package_extract_job_req, runtime)
        return submit_trade_document_package_extract_job_resp
